#!/usr/bin/env python3
"""
scripts/sync.py
Fetch WakaTime and GitHub stats into data/wakatime.json and data/github.json for Hugo.
Uses only Python standard library.
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
import configparser
import subprocess
from datetime import datetime, timezone
from collections import defaultdict

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

GH_USER = 'jitendradara12'


# ── Helpers ──

def get_wakatime_api_key():
    api_key = os.environ.get('WAKATIME_API_KEY')
    if api_key:
        return api_key.strip()
    cfg_path = os.path.expanduser('~/.wakatime.cfg')
    if os.path.exists(cfg_path):
        c = configparser.ConfigParser()
        c.read(cfg_path)
        if c.has_option('settings', 'api_key'):
            return c.get('settings', 'api_key').strip()
    return None


def get_github_token():
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        return token.strip()
    try:
        res = subprocess.run(
            ['gh', 'auth', 'token'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    except Exception:
        pass
    return None


def fetch_json(url, headers=None):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', f'{GH_USER}-stats-sync/1.0')
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode('utf-8'))


def format_relative_time(dt):
    now = datetime.now(timezone.utc)
    diff = now - dt
    secs = int(diff.total_seconds())
    if secs < 60:
        return 'just now'
    mins = secs // 60
    if mins < 60:
        return f'{mins}m ago'
    hours = mins // 60
    if hours < 24:
        return f'{hours}h ago'
    days = hours // 24
    if days == 1:
        return 'yesterday'
    if days < 30:
        return f'{days}d ago'
    return dt.strftime('%d %b')


# ── WakaTime Sync ──

def sync_wakatime():
    api_key = get_wakatime_api_key()
    out_file = os.path.join(DATA_DIR, 'wakatime.json')
    if not api_key:
        print("[wakatime] No API key found in WAKATIME_API_KEY or ~/.wakatime.cfg. Skipping.")
        return

    b64 = base64.b64encode(api_key.encode()).decode()
    auth_header = {'Authorization': f'Basic {b64}'}

    try:
        today_data = fetch_json(
            'https://wakatime.com/api/v1/users/current/summaries?range=today',
            auth_header
        )
        weekly_data = fetch_json(
            'https://wakatime.com/api/v1/users/current/summaries?range=last_7_days',
            auth_header
        )
    except Exception as e:
        print(f"[wakatime] Error fetching API: {e}")
        return

    if not today_data.get('data'):
        print("[wakatime] No today data returned.")
        return

    day = today_data['data'][0]
    total_seconds = day['grand_total']['total_seconds']
    total_today = day['grand_total']['text']

    # Projects
    projects = [
        {'name': p['name'], 'text': p['text'], 'percent': round(p['percent'], 1)}
        for p in day.get('projects', [])
        if p.get('name') and p.get('name') != 'Unknown Project'
    ]

    # Editors
    editors = [
        {'name': e['name'], 'text': e['text'], 'percent': round(e['percent'], 1)}
        for e in day.get('editors', [])
        if e.get('name') and e.get('name') != 'Unknown Editor'
    ]

    # Operating Systems
    operating_systems = [
        {'name': o['name'], 'text': o['text'], 'percent': round(o['percent'], 1)}
        for o in day.get('operating_systems', [])
    ]

    # Languages: aggregate from the last 7 days for a rich, realistic breakdown
    ignored_langs = {'Other', 'Diff', 'Git Config', 'YAML', 'JSON', 'Markdown', 'Text'}
    lang_totals = defaultdict(float)
    for d in weekly_data.get('data', []):
        for l in d.get('languages', []):
            name = l.get('name')
            if name and name not in ignored_langs:
                lang_totals[name] += l.get('total_seconds', 0)

    total_lang_sec = sum(lang_totals.values())
    languages = []
    if total_lang_sec > 0:
        sorted_langs = sorted(lang_totals.items(), key=lambda x: x[1], reverse=True)
        for name, sec in sorted_langs[:6]:
            pct = round((sec / total_lang_sec) * 100, 1)
            languages.append({'name': name, 'percent': pct})

    # 7-day rollup
    cum_total = weekly_data.get('cumulative_total', {})
    daily_avg = weekly_data.get('daily_average', {})
    rollup_7d = {
        'total': cum_total.get('text', ''),
        'daily_average': daily_avg.get('text', ''),
        'total_seconds': cum_total.get('seconds', 0)
    }

    # Resting status if logged under 30 minutes today
    is_resting = total_seconds < 1800

    payload = {
        'total_today': total_today,
        'total_seconds': total_seconds,
        'is_resting': is_resting,
        'projects': projects,
        'editors': editors,
        'operating_systems': operating_systems,
        'languages': languages,
        'rollup_7d': rollup_7d,
        'last_updated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)

    status_str = f"{total_today} today" if not is_resting else f"{total_today} today (resting, 7d: {rollup_7d['total']})"
    print(f"[wakatime] Updated data/wakatime.json: {status_str} across {len(projects)} projects.")


# ── GitHub Sync ──

def sync_github():
    token = get_github_token()
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'

    out_file = os.path.join(DATA_DIR, 'github.json')

    try:
        events = fetch_json(
            f'https://api.github.com/users/{GH_USER}/events?per_page=30',
            headers
        )
    except Exception as e:
        print(f"[github] Error fetching events: {e}")
        return

    if not isinstance(events, list):
        print("[github] Unexpected events response structure.")
        return

    pushes = [
        ev for ev in events
        if ev.get('type') == 'PushEvent' and ev.get('payload')
    ]
    if not pushes:
        print("[github] No recent PushEvent found.")
        return

    # GitHub Events API is not guaranteed to be strictly chronological.
    # Sort descending by created_at so the newest push is always selected.
    pushes.sort(key=lambda e: e.get('created_at', ''), reverse=True)
    push = pushes[0]

    payload = push.get('payload', {})
    repo_full = push['repo']['name']
    repo_name = repo_full.split('/')[1] if '/' in repo_full else repo_full
    branch = payload.get('ref', '').replace('refs/heads/', '')
    created_at = push.get('created_at')

    # Find HEAD SHA
    head_sha = payload.get('head')
    commits = payload.get('commits', [])
    if not head_sha and commits:
        head_sha = commits[-1].get('sha')

    if not head_sha:
        print("[github] No commit SHA identified in PushEvent.")
        return

    # Find commit message
    commit_msg = None
    commit_date_str = created_at
    if commits:
        commit_msg = commits[-1].get('message')

    # If payload lacked commit message, fetch commit details directly
    if not commit_msg:
        try:
            commit_detail = fetch_json(
                f'https://api.github.com/repos/{repo_full}/commits/{head_sha}',
                headers
            )
            c = commit_detail.get('commit', {})
            commit_msg = c.get('message')
            author_date = c.get('author', {}).get('date')
            if author_date:
                commit_date_str = author_date
        except Exception as e:
            print(f"[github] Notice: commit detail lookup skipped ({e})")
            commit_msg = f"push to {branch or 'main'}"

    # Clean message (first line, strip whitespace, truncate if overly long)
    if commit_msg:
        commit_msg = commit_msg.split('\n')[0].strip()
        if len(commit_msg) > 72:
            commit_msg = commit_msg[:69] + '…'
    else:
        commit_msg = f"push to {branch or 'main'}"

    # Calculate relative time
    dt = None
    relative_time = 'recently'
    if commit_date_str:
        try:
            dt = datetime.fromisoformat(commit_date_str.replace('Z', '+00:00'))
            relative_time = format_relative_time(dt)
        except Exception:
            pass

    short_sha = head_sha[:7] if head_sha else ''
    commit_url = f"https://github.com/{repo_full}/commit/{head_sha}"
    repo_url = f"https://github.com/{repo_full}"

    github_data = {
        'sha': head_sha,
        'short_sha': short_sha,
        'message': commit_msg,
        'repo': repo_full,
        'repo_name': repo_name,
        'branch': branch,
        'date': commit_date_str,
        'relative_time': relative_time,
        'commit_url': commit_url,
        'repo_url': repo_url,
        'last_updated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(github_data, f, indent=2)

    print(f"[github] Updated data/github.json: {repo_name}@{short_sha} ('{commit_msg}') {relative_time}")


# ── Avatar Sync ──

def sync_avatar():
    avatar_file = os.path.join(ROOT_DIR, 'static', 'avatar.jpg')
    url = 'https://avatars.githubusercontent.com/u/93462792?s=160'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': f'{GH_USER}-stats-sync/1.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            new_data = resp.read()

        if os.path.exists(avatar_file):
            with open(avatar_file, 'rb') as f:
                existing = f.read()
            if existing == new_data:
                print("[avatar] static/avatar.jpg is already up to date.")
                return

        with open(avatar_file, 'wb') as f:
            f.write(new_data)
        print(f"[avatar] Updated static/avatar.jpg ({len(new_data)} bytes).")
    except Exception as e:
        print(f"[avatar] Notice: avatar sync skipped ({e})")


if __name__ == '__main__':
    print("── Syncing data for www ──")
    sync_wakatime()
    sync_github()
    sync_avatar()
    print("── Done ──")
