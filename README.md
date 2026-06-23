# A-Share Trading Skills

A Codex / WorkBuddy skill collection for A-share trading workflows.

## Skills

- `a-stock-news`: Aggregates A-share and financial news from multiple public sources.
- `a-stock-hot`: Tracks A-share hot sectors, capital flows, market sentiment, limit-up themes, and leading stocks.

## Install

Install one skill:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Jettison928/a-share-trading-skills --path skills/a-stock-news
```

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Jettison928/a-share-trading-skills --path skills/a-stock-hot
```

Install both:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Jettison928/a-share-trading-skills --path skills/a-stock-news skills/a-stock-hot
```

Restart Codex after installing new skills.

## Notes

These skills are designed for short-term A-share market monitoring and decision support. They are not financial advice.
