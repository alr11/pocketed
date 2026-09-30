#!/usr/bin/env python3
"""Write reminders/HH-MM.ics: one repeating daily calendar reminder per half hour.

The app links to these for "Add to Apple Calendar". Times are "floating"
(no time zone), so 8pm means 8pm wherever the phone is. Re-run after changing
the wording or URL:  python3 tools/make-reminders.py
"""
from pathlib import Path

APP_URL = "https://alr11.github.io/pocketed/"
OUT = Path(__file__).resolve().parent.parent / "reminders"


def ics(hh: int, mm: int) -> str:
    end = hh * 60 + mm + 5
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Pocketed//Daily reminder//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "BEGIN:VEVENT",
        f"UID:pocketed-daily-{hh:02d}{mm:02d}@alr11.github.io",
        "DTSTAMP:20261001T000000Z",
        f"DTSTART:20261001T{hh:02d}{mm:02d}00",
        f"DTEND:20261001T{end // 60:02d}{end % 60:02d}00",
        "RRULE:FREQ=DAILY",
        "SUMMARY:Tick off your Pocketed habits",
        f"DESCRIPTION:Open Pocketed and tick today's money habits: {APP_URL}",
        f"URL:{APP_URL}",
        "TRANSP:TRANSPARENT",
        "BEGIN:VALARM",
        "ACTION:DISPLAY",
        "DESCRIPTION:Tick off your Pocketed habits",
        "TRIGGER:PT0M",
        "END:VALARM",
        "END:VEVENT",
        "END:VCALENDAR",
    ]
    return "\r\n".join(lines) + "\r\n"


OUT.mkdir(exist_ok=True)
for minutes in range(6 * 60, 24 * 60, 30):
    hh, mm = divmod(minutes, 60)
    (OUT / f"{hh:02d}-{mm:02d}.ics").write_text(ics(hh, mm), newline="")
print(f"Wrote {len(list(OUT.glob('*.ics')))} files to {OUT}")
