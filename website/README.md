# Learning Dashboard

Minimal React + Vite frontend for the coding revision dashboard.

## Planned data flow

The website will consume generated repository data:

- `leetcode-stats.json`
- `.leetcode-metadata.json`
- `leetcode-topics/*.md`
- future `deepml-solutions/` data
- future platform indexes

The repository remains the source of truth. GitHub Actions can regenerate the data whenever a new solution is added.

## Run locally

```bash
cd website
npm install
npm run dev
```
