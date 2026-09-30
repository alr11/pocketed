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

## Reminders

Settings → Daily reminder adds a repeating calendar event, so reminders work
on iPhone and Android with no server and no account:

- **Apple Calendar** links to a static file in `reminders/` (one per half hour,
  6:00 to 23:30). Times are "floating", so 8pm means 8pm wherever the phone is.
  Regenerate with `python3 tools/make-reminders.py`.
- **Google Calendar** opens a pre-filled repeating event.

True push notifications need a server with VAPID keys and a scheduler, and on
iPhone they only work once the app is added to the Home Screen (iOS 16.4+).

## Anonymous usage counts (GoatCounter)

Off until you set it up:

1. Sign up at goatcounter.com and pick a site code, e.g. `pocketed`.
2. In `index.html`, set `const GOATCOUNTER_CODE = 'pocketed';` and push.

What's sent: paths only, never names, amounts or IDs.

| Path | Meaning |
| --- | --- |
| `/open` | The app was opened (at most once a day per phone) |
| `/active/week-0` … `/active/week-8-plus` | Opened today, N weeks after this phone started using Pocketed. Compare week-0 with week-2 to see how many people stick with it |
| `/event/habit-added/<template or custom>` | A habit was added |
| `/event/share-card/<design>` | A share card was made |
| `/event/moved-money`, `/event/reminder/<apple or google>` | Features used |
| `/event/plus/opened`, `/checkout`, `/activated` | Plus funnel |

People can turn counts off in Settings, and the Privacy section says what is
sent. Under the Data (Use and Access) Act 2025, analytics used only for
statistics don't need a consent pop-up if they're explained clearly and easy
to turn off. Check the ICO's current guidance before relying on this.
GoatCounter is free for non-commercial use; once Plus is on sale, expect to pay
for a commercial plan or switch provider.

## Pocketed Plus (Lemon Squeezy)

Off until you set it up. While off, everything is free and no Plus screens appear.

1. Create a Lemon Squeezy store and a product "Pocketed Plus" (one-off
   payment, e.g. £4.99) with **license keys** turned on. Set an activation
   limit (e.g. 3 phones).
2. Copy the product's checkout link.
3. In `index.html` set `PLUS_CHECKOUT_URL` to that link, and `PLUS_PRODUCT_ID`
   to the product's ID (so keys for other products are refused). Push.

Plus unlocks unlimited habits (free: 3) and the Midnight and Blush share card
designs. The app checks the key with Lemon Squeezy's licence API when it's
entered and about once a week after (never removing Plus just because the phone
is offline). The unlock is stored on the phone, so a technical person could
bypass it; that's a normal trade-off for a low-price app with no accounts.

## Run locally

```bash
python3 -m http.server 8000
```

## Changing things

- App name: `APP_NAME` in `index.html`, plus `manifest.webmanifest` and the `<title>`.
- Ready-made habits: the `TEMPLATES` list in `index.html`. Amounts are in pence/cents.
- After changing files, bump `VERSION` in `sw.js` so installed copies update.
