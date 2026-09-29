# Pocketed: money habits

A money-habits tracker for iPhone and Android. Each habit has a price, the
money you'd usually spend. Every day you keep it, Pocketed adds that amount
to your "saved so far" total.

It's an installable web app (PWA) with no build step, no account and no
server. Data stays on the phone.

## Features

- **Money habits** with an amount, e.g. "No takeaways" saves £12, "Coffee at home" saves £3.50.
- **Goes up each time** mode for the 1p saving challenge (£667.95 over a year) and the 52-week challenge (£1,378).
- **Saved so far** total with this week, this month and an overall streak of days you kept every habit.
- **Savings goal** with a progress bar that shows both what you've saved and what you've actually moved to savings.
- **"I moved money"**: log transfers into a savings account or pot, so the total is real money rather than an estimate.
- **Payday months**: count the month from payday to payday (any day, or the last working day). Weekend paydays move to the Friday before; bank holidays aren't counted.
- **Help to Save tip** (GBP only): points people on Universal Credit to the government's 50% bonus scheme on GOV.UK. Can be hidden.
- **Share card**: a 1080×1920 image of your total, streak and top habits, ready for TikTok or Instagram Stories.
  Uses the phone's share sheet where available; otherwise press and hold the image to save it.
- 8 ready-made habits (no-spend day, no takeaways, pack lunch, 1p challenge, …) plus custom ones.
- Per-habit schedules, streaks, 30-day completion rate and a 16-week history grid.
- Currency picker (GBP, EUR, USD, CAD, AUD, NZD, INR, ZAR, NGN).
- JSON backup export/import, light and dark mode, works offline.

The total is an estimate of money not spent. The app isn't connected to a bank
account and says so in Settings.

## Hosting

`.github/workflows/pages.yml` publishes the app to GitHub Pages on every push
to `main`: `https://alr11.github.io/pocketed/`. In the repo's **Settings →
Pages**, set **Source** to **GitHub Actions** once.

## Run locally

```bash
python3 -m http.server 8000
```

## Changing things

- App name: `APP_NAME` in `index.html`, plus `manifest.webmanifest` and the `<title>`.
- Ready-made habits: the `TEMPLATES` list in `index.html`. Amounts are in pence/cents.
- After changing files, bump `VERSION` in `sw.js` so installed copies update.
