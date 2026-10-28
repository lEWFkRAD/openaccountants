---
name: ne-corporate-income-tax
description: >
  Use this skill whenever asked about Nebraska corporate income tax for
  tax year 2026 — the Revenue Act Chapter 77 corporation tax, Form
  4-1120C, the pass-through entity (PTE) tax election, and filing
  mechanics. Trigger on "Nebraska corporate income tax", "4-1120C",
  "Nebraska corporation tax", "Nebraska PTE tax". Source-cited draft;
  Chapter 77 structure, the withholding statute rail (§ 77-3513) and the
  official PTE-tax page verified 2026-10-28; the rate table, Form
  4-1120C identity and deadlines needs-sources (official rate page not
  reached this run).
jurisdiction: US-NE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ne-income-tax
---

# Nebraska corporate income tax v0.1

> **General reference only.** General tax reference for AI-assisted workflows; not reviewed for any specific client's facts. Do not file, pay, or take a position on this alone — use a qualified Nebraska practitioner.

## 1. Scope and sources

Nebraska corporation income tax under the Revenue Act, Chapter 77. **Source status:** the Legislature's Chapter 77 index and § 77-3513 (withholding) were fetched and verified reachable 2026-10-28, and the DOR's **PTE tax page** (https://revenue.nebraska.gov/tax-credits/nebraska-pass-through-entity-tax-ptet) is verified. The **corporate rate table (commonly cited as 5% up to $100,000 and 5.5% above), Form 4-1120C identity, due dates and estimate thresholds were not on a page this run could fetch — needs-sources**.

## 2. Who applies

- Corporations (and entities taxed as corporations) with Nebraska-source income — Chapter 77 (structure verified).
- **Pass-through entities may elect the Nebraska PTE tax** at the entity level (official page verified); members then get a credit — mechanics/rate **needs-sources**.
- Nebraska imposes **no separate franchise tax** on general corporations (verify — **needs-sources**).

## 3. Rates (tax year 2026)

| Nebraska taxable income | Rate | Source status |
|---|---|---|
| Up to $100,000 (approx.) | 5% | **needs-sources** |
| Over $100,000 (approx.) | 5.5% | **needs-sources** |

Treat 5.5% as the planning default above $100,000 pending source confirmation.

## 4. Base and apportionment

Federal taxable income with Nebraska modifications (additions include certain interest/dividends from related affiliates — confirm, **needs-sources**). Nebraska is a **separate-company state with a single sales factor expected** — combined-reporting posture **needs-sources**.

## 5. Deadlines, estimates, penalties

- Return due: expected April 15 (conformity) — **needs-sources**.
- Estimates: expected 100% prior-year / 90% current-year safe harbors — **needs-sources**.
- Penalty/interest percentages: **needs-sources**.

## 6. Cross-border notes

Nexus: Chapter 77 income-tax nexus provisions + P.L. 86-272 (detail **needs-sources**). Nonresident member taxation and PTE withholding rails: see `ne-payroll.md` / `ne-cross-border.md`.

## 7. Worked examples

**Example 1 — $400,000 Nebraska taxable income at 5.5% (rate needs-sources):**

```oa-check
name: NE corporate 5.5 percent
inputs:
  income: 400000
  rate: 0.055
steps:
  - tax: income * rate
expected:
  tax: 22000.00
```

**Example 2 — PTE election comparison (illustrative).** Pass-through income $200,000 all Nebraska-source; entity-level tax at 5.5% vs member-level at an assumed 4.5% individual effective rate (both rates needs-sources):

```oa-check
name: NE PTE vs member level
inputs:
  income: 200000
  pte_rate: 0.055
  member_eff: 0.045
steps:
  - pte_tax: income * pte_rate
  - member_tax: income * member_eff
  - delta: pte_tax - member_tax
expected:
  pte_tax: 11000.00
  member_tax: 9000.00
  delta: 2000.00
```

## 8. Ask the client

- Is the entity considering the PTE election (SALT-cap workaround posture)? Compare entity vs member rates.
- Related-party interest/dividend payments that trigger Nebraska addbacks?
- Factor presence (payroll, sales, property) creating Chapter 77 nexus?

## 9. Sources

1. Revenue Act Ch. 77 index: https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=77 — fetched 2026-10-28.
2. § 77-3513 (withholding): https://nebraskalegislature.gov/laws/statutes.php?statute=77-3513 — fetched 2026-10-28.
3. DOR PTE tax: https://revenue.nebraska.gov/tax-credits/nebraska-pass-through-entity-tax-ptet — verified 2026-10-28.
4. DOR businesses landing: https://revenue.nebraska.gov/businesses — resolves; corporate rate page not reached.

**Needs-sources:** rate bands, Form 4-1120C, due dates, estimate safe harbors, penalties/interest, addback statutes, apportionment factor mix, PTE rate/credit mechanics.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Nebraska corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
