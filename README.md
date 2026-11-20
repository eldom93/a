# Store Numbers — Daily Tracker & Money Finder

A simple, **zero-install** tool for a Subway (or any quick-service) store. Open `index.html`
in any browser — phone or computer — and go. All data stays on your device (`localStorage`);
nothing is uploaded anywhere.

## What it does

- **Today** — enter your end-of-day numbers (sales, guests, drink sales, food cost %, labor
  hours, wage) and instantly see your average ticket, guests per labor hour, drink %, and
  labor % of sales, with plain-English flags (e.g. an impossible 200% food cost = a data error).
- **Cash Count** — reconcile your drawer the way the register does and get your over/short,
  with guidance on what to check.
- **Shift Log** — a timestamped record of every drawer handoff: opening/closing counts, your
  sales rung, drops, who you took the drawer from and handed it to, an optional witness, and
  notes. It auto-computes over/short per shift and exports to CSV so you always have your own
  dated receipts if a discrepancy ever gets pinned on the wrong person.
- **History** — every saved day in one table, with bad data flagged so it stands out. Export to CSV.
- **Money Finder** — the three biggest money levers (average ticket, drink attachment, labor),
  with sliders that show the **yearly dollar impact** using your store's real numbers.
- **My Pitch** — generates a numbers-first script you can read to the owner to ask for a raise
  or a performance bonus, pre-filled with your Money Finder total.

## Run it

Just open the file:

```bash
# double-click index.html, or:
python3 -m http.server 8000   # then visit http://localhost:8000
```

No dependencies, no build step, no accounts.

## Note

The Money Finder uses industry-typical assumptions (e.g. ~$2.19 average drink, ~75% drink
margin, 12% payroll tax on labor). Adjust the inputs to match your store — the math updates live.
These are planning estimates, not accounting figures.
