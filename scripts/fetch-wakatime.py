#!/usr/bin/env python3
"""Fetch daily WakaTime stats and save to data/wakatime.json for Hugo."""
import configparser
import urllib.request
import json
import base64
import os
from datetime import datetime, timezone

cfg_path = os.path.expanduser('~/.wakatime.cfg')
api_key = os.environ.get('WAKATIME_API_KEY')

if not api_key and os.path.exists(cfg_path):
    c = configparser.ConfigParser()
    c.read(cfg_path)
    if c.has_option('settings', 'api_key'):
        api_key = c.get('settings', 'api_key').strip()

if not api_key:
    print("No WakaTime API key found in ~/.wakatime.cfg or WAKATIME_API_KEY env var.")
    exit(0)

b64 = base64.b64encode(api_key.encode()).decode()
url = 'https://wakatime.com/api/v1/users/current/summaries?range=today'
req = urllib.request.Request(url, headers={'Authorization': f'Basic {b64}'})

try:
    with urllib.request.urlopen(req) as resp:
        raw = json.loads(resp.read().decode())
except Exception as e:
    print(f"Error fetching WakaTime summaries: {e}")
    exit(0)

if not raw.get('data'):
    print("No summary data returned from WakaTime.")
    exit(0)

day = raw['data'][0]
data = {
    'total_today': day['grand_total']['text'],
    'total_seconds': day['grand_total']['total_seconds'],
    'projects': [
        {'name': p['name'], 'text': p['text'], 'percent': round(p['percent'], 1)}
        for p in day.get('projects', [])
        if p.get('name') != 'Unknown Project'
    ],
    'editors': [
        {'name': e['name'], 'text': e['text'], 'percent': round(e['percent'], 1)}
        for e in day.get('editors', [])
        if e.get('name') != 'Unknown Editor'
    ],
    'operating_systems': [
        {'name': o['name'], 'text': o['text'], 'percent': round(o['percent'], 1)}
        for o in day.get('operating_systems', [])
    ],
    'last_updated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
}

os.makedirs('data', exist_ok=True)
with open('data/wakatime.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Updated data/wakatime.json: {data['total_today']} today across {len(data['projects'])} projects.")
