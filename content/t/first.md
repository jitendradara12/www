+++
date = '2025-12-14T13:02:42+05:30'
title = 'First'
tags = ['random','fake','temp']
+++

hello there,

```python
def fn(a):
  print(fn(a+1))

import random
import string

def generate_random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_random_string(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Generate 200 lines
with open('random_lines.txt', 'w') as f:
    for _ in range(200):
        random_word = generate_random_word(random.randint(4, 10))
        random_string = generate_random_string(40)
        line = f"{random_word}:{random_string}\n"
        f.write(line)
```

This is a very common roadmap hurdle. The mistake most developers make is thinking a personal site needs "articles" like generic Medium posts ("What is an Array?"). You don’t need to do that.

Since you are an engineer, not a journalist, **you should build a "Digital Garden" or a "Wiki," not a blog.**

Here are four content strategies that require **zero creative writing** and focus purely on technical documentation.

### 1. The "TIL" (Today I Learned) Collection

This is the easiest way to fill a site. Instead of writing long essays, you write tiny, 3-sentence snippets about things you figured out that day.

- **Format:** Problem -> Solution.
- **Example Post Title:** _How to quit Vim_
- **Content:** "I got stuck in Vim today. I learned you have to press `:q!` to force quit without saving. Note to self: do not panic next time."
- **Why it works:** It requires 2 minutes to write. Over 6 months, you will have 50+ posts showing a consistent learning curve. Recruiters love seeing "continuous learning."

### 2. The "Cheat Sheet" Strategy

You likely search for the same commands over and over (Git commands, Linux flags, Docker arguments). Turn those into content.

- **Content:** A page called "My Git Cheatsheet" where you just list the commands you actually use.
- **Why it works:** It turns your website into a utility tool for _yourself_. If it’s useful to you, it’s useful to others. It shows you are organized.

### 3. The "Meta" Documentation

Since you have "nothing to show" yet, **this Hugo project IS the thing you show.** Document the process of building it.

- **Post 1:** "Why I chose Hugo over WordPress" (Speed, Go-based, no database).
- **Post 2:** "Setting up the CI/CD pipeline" (How you connected GitHub to your host).
- **Post 3:** "How I customized my theme."
- **Why it works:** It proves you understand the code you just wrote. It fills the site with 3-4 solid technical walkthroughs immediately.

### 4. Configuration & Dotfiles

If you customize your computer (Linux, VS Code, Terminal), post your configs.

- **Content:** Post your config files with short comments explaining _why_ you chose those settings.
- **Example:** "My Terminal Setup" – screenshots of your terminal, your font choice, and your shell aliases.
- **Why it works:** It shows you care about your developer environment and tooling, which is a key trait of productive engineers.

---

### Suggested Taxonomy (Categories)

If you aren't writing "Blog Posts," you shouldn't structure your site like a blog. Structure it like a knowledge base.

In your `content/` folder, create these directories instead of just `posts/`:

```text
content/
├── wiki/         # Detailed notes on languages (e.g., Python, Go)
├── til/          # Quick 2-line snippets of things you learned
├── errors/       # "I got Error X, and here is how I fixed it"
└── projects/     # Placeholders for future projects

```

### Summary

Don't write "articles." **Write documentation for your future self.**

When you solve a bug next week, paste the solution into a markdown file and push it. That is your content.

**Would you like a sample template for a "TIL" (Today I Learned) markdown file to get you started?**
