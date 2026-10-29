---
name: co-corporate-income-tax
description: >
  Use this skill whenever asked about Colorado corporate income tax for
  tax year 2026 — Form DR 0112 filing (due May 15, extension to November 15),
  the flat 4.4% rate, receipts-factor apportionment under C.R.S. §39-22-303.6,
  "doing business" and substantial-nexus standards, quarterly estimated
  payments (DR 0112EP, no penalty if net liability is under $5,000), the
  delinquent-payment penalty (greater of $5 or 5%, plus 0.5% a month), and
  combined reporting. Trigger on "Colorado corporate income tax",
  "Colorado C corporation tax", "DR 0112", "Colorado receipts factor",
  "Colorado corporate estimated tax". Corporate Income Tax Guide (March
  2026) and C.R.S. Title 39 (2026) read 2026-10-28.
jurisdiction: US-CO
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
review_status: pending_review
depends_on:
  - co-income-tax
---

# Colorado corporate income tax (C corporations), tax year 2026

> **Source-cited draft.** Revised 2026-10-28 against the Colorado Corporate Income Tax Guide (March 2026), the 2025 DR 0112 form and instructions, and the Colorado Revised Statutes 2026. v0.1 incorrectly treated "DR 0107" as the C-corporation return (DR 0107 is the Nonresident Partner or Shareholder Agreement; the C-corporation return is DR 0112) and carried April 15/October 15 dates that belong to the pass-through (DR 0106) calendar. No accountant has reviewed this draft.

## Who this applies to

- Every domestic C corporation, and every foreign C corporation doing business in Colorado, pays Colorado corporate income tax on its Colorado net income ([Corporate Income Tax Guide, Part 1](https://tax.colorado.gov/sites/default/files/documents/Corporate_Income_Tax_Guide_Mar_2026_.pdf)).
- A C corporation is "doing business in Colorado" whenever the minimum standards of Public Law 86-272 are exceeded and the corporation has substantial nexus with Colorado (Corporate Income Tax Guide, Part 1; Department Rule 39-22-301(1)).
- **Substantial nexus thresholds** (Corporate Income Tax Guide, Part 1): a foreign C corporation organized or commercially domiciled in Colorado has nexus; otherwise nexus exists if Colorado property or payroll exceeds $50,000, or Colorado sales exceed $500,000, or 25% or more of the corporation's total property, payroll or sales are in Colorado. v0.1's "$100,000 of Colorado sales" economic-nexus figure matched the sales-and-use-tax rule, not the income-tax rule, and has been removed.
- Partnerships and S corporations file DR 0106 and either include nonresident owners in a composite return or elect the SALT Parity Act entity-level tax — see `co-s-corporation-tax`.
- Organizations with IRS tax-exempt status are generally exempt; an exempt entity claiming only a refundable or transferable credit files DR 0990 instead ([DR 0112 page, DOR](https://tax.colorado.gov/sites/default/files/documents/DR0112_2025.pdf)).

## Rates, bands and thresholds

| Item | Amount | Source |
|---|---|---|
| Corporate income tax | 4.4% of Colorado taxable net income (2025; 2024 was 4.25%) | [Corporate Income Tax Guide, Part 3](https://tax.colorado.gov/sites/default/files/documents/Corporate_Income_Tax_Guide_Mar_2026_.pdf); DR 0106 instructions line 20 "Multiply line 19 by 4.4% (0.044)" |
| SALT Parity entity-level rate (pass-throughs) | 4.4% | DR 0106 instructions line 20; C.R.S. §39-22-344 (SALT Parity Act, §§39-22-340 to 347) |
| Combined-reporting unity | A combined return must include each affiliate meeting at least three of the six tests of unity for the current and two preceding years | Corporate Income Tax Guide, Part 2 |
| Estimated tax penalty exemption | No estimated tax penalty if net tax liability for the year is under $5,000 | Corporate Income Tax Guide, Part 9 |

Colorado has one flat corporate rate; there are no brackets and no separate corporate minimum tax in the archived March 2026 guide (the absence of a minimum tax is not affirmatively stated in a primary source — see Not yet confirmed).

## The taxable base

- Colorado corporate taxable income starts from federal taxable income with modifications: additions (for example, non-Colorado state and local bond interest; net operating loss deductions for losses incurred outside Colorado) and subtractions (for example, income exempt from federal tax) — Corporate Income Tax Guide, Parts 4 and 5.
- A C corporation with income from business activity outside Colorado apportioned and allocated that income; receipts-factor apportionment is under [C.R.S. §39-22-303.6](https://olls.info/crs/crs2026-title-39.pdf), and the DR 0106 instructions confirm ordinary income of a pass-through is generally sourced using receipts-factor apportionment even without a full election.
- Income with no activity outside Colorado is sourced 100% to Colorado (DR 0106 instructions).
- **Related-party adjustments:** where C corporations are owned or controlled directly or indirectly by the same interests, the executive director may, to avoid abuse, on a fair and impartial basis, distribute or allocate gross income and deductions between or among them to clearly reflect income (C.R.S. §39-22-304(6), Colorado Revised Statutes 2026). v0.1 cited "C.R.S. §39-22-503" for this; in the 2026 statutes §39-22-503 is "Taxation of real estate investment trusts", so that citation has been corrected.
- **Combined reporting for listed jurisdictions:** C.R.S. §39-22-304(8) and (8.5) govern combined reports, including when members incorporated in a "listed jurisdiction" for tax avoidance must be included; a water's-edge election is binding for the election year and the following nine years (Colorado Revised Statutes 2026). v0.1 cited "C.R.S. §39-22-5303" for tax-haven combined reporting; that section does not exist in the 2026 statutes under that number, so the citation has been corrected.

## Deadlines and filing

| Filing | Calendar-year due date | Source |
|---|---|---|
| DR 0112 (C corporation return) | 15th day of the fifth month after year close — May 15 | [DR 0112 (2025) form instructions](https://tax.colorado.gov/sites/default/files/documents/DR0112_2025.pdf) |
| Extension | Automatic 6-month extension to November 15; **no extension of payment**; extension payment via DR 0158-C | DR 0112 (2025) form instructions |
| Estimated payments (DR 0112EP) | Quarterly: April 15, June 15, September 15 and December 15 | [Corporate Income Tax Guide, Part 9](https://tax.colorado.gov/sites/default/files/documents/Corporate_Income_Tax_Guide_Mar_2026_.pdf) |

A C corporation must remit estimated payments if its net Colorado tax liability for the year exceeds $5,000; payments go through Revenue Online, EFT, or by check with form DR 0112EP (Corporate Income Tax Guide, Part 9). Affiliated C corporations filing a consolidated return use DR 0112 with the consolidated-return box checked, filed by the due date including extensions; the consolidated election is binding for four years (Corporate Income Tax Guide, Part 2).

## Penalties and interest

- **Delinquent payment penalty** (DR 0106 instructions, same rulebook standard the corporate guide cross-references): the greater of $5 or 5% of the additional tax due for the first month of delinquency, plus 0.5% for each additional month, up to 12% in total; avoided if 90% of the tax is paid by the original due date.
- **Estimated tax penalty:** computed on [Form DR 0205](https://tax.colorado.gov/sites/default/files/documents/Corporate_Income_Tax_Guide_Mar_2026_.pdf) (Computation of Penalty Due Based on Underpayment of Colorado Corporate Estimated Tax), charged as interest (Corporate Income Tax Guide, Part 9).
- **Interest:** the corporate estimated-tax interest rates published by the Department are 12% for 2025 and 11% for 2026 (Corporate Income Tax Guide, Part 9). The general interest-rate statute is C.R.S. §39-21-110.5 ("Rate of interest to be fixed", Colorado Revised Statutes 2026). v0.1 cited §39-21-118 for the interest rate; in the 2026 statutes §39-21-118 is "Criminal penalties", so the citation has been corrected.

## Cross-border points

- **Public Law 86-272** (15 U.S.C. §381) bars a net-income tax where the only in-state activity is solicitation of orders for tangible personal property approved and filled outside the state; the Corporate Income Tax Guide applies the "doing business" test only when those federal minimum standards are exceeded — see `co-cross-border`.
- Dividends a C corporation includible in a combined report receives from another includible member are excluded from taxable income (Corporate Income Tax Guide, Part 3).
- HB 25B-1002 (2025 special session) adds, for C corporations only and from 1 January 2026, an addback of the federal foreign-derived intangible income deduction and new listed tax-haven jurisdictions — see [HB 25B-1002](https://leg.colorado.gov/bills/hb25b-1002).
- Foreign corporations should confirm the current listed-jurisdiction list and water's-edge election mechanics with the Department before filing a combined return.

## Worked examples

A calendar-year C corporation has $500,000 of Colorado net income for 2026 (hypothetical facts). Tax:

```oa-check
name: corporate tax on 500000
inputs:
  income: 500000
  rate: 0.044
steps:
  - tax: income * rate
expected:
  tax: 22000.00
```

A multistate corporation has Colorado receipts of $2,500,000 and total receipts of $10,000,000; total unitary income $1,200,000 (hypothetical facts; receipts factor per C.R.S. §39-22-303.6):

```oa-check
name: receipts factor and tax
inputs:
  co_receipts: 2500000
  total_receipts: 10000000
  income: 1200000
  rate: 0.044
steps:
  - factor: co_receipts / total_receipts
  - apportioned: income * factor
  - tax: apportioned * rate
expected:
  factor: 0.25
  apportioned: 300000.00
  tax: 13200.00
```

## Ask the client first

- Does the entity have Colorado property or payroll over $50,000, Colorado sales over $500,000, or 25% of its factors in Colorado (or is it organized/domiciled in Colorado)?
- Is the entity a partnership or S corporation — has a SALT Parity election been made, and are composite obligations being met?
- Are quarterly DR 0112EP payments scheduled, and is the 90%-by-due-date penalty shield being maintained?
- Which apportionment method (receipts factor vs direct sourcing) applies to each income stream, and is any affiliate in a listed jurisdiction (combined-reporting exposure)?
- Is an extension payment (DR 0158-C) needed by May 15?

## Sources

| Source | URL | Read on |
|---|---|---|
| Colorado DOR — Colorado Corporate Income Tax Guide (March 2026) | https://tax.colorado.gov/sites/default/files/documents/Corporate_Income_Tax_Guide_Mar_2026_.pdf | 2026-10-28 |
| Colorado DOR — Form DR 0112 (2025), Colorado C Corporation Income Tax Return and instructions | https://tax.colorado.gov/sites/default/files/documents/DR0112_2025.pdf | 2026-10-28 |
| Colorado DOR — Form DR 0106 instructions (2025), Colorado Partnership and S Corporation Return | https://tax.colorado.gov/sites/tax/files/documents/DR0106_2025.pdf | 2026-10-28 |
| Colorado DOR — Corporate Income Tax Guide (web page) | https://tax.colorado.gov/corporate-income-tax-guide | 2026-10-28 |
| Colorado DOR — Colorado Taxes & Fees Due Date Guide | https://tax.colorado.gov/due-date-guide | 2026-10-28 |
| Colorado OLLS — Colorado Revised Statutes 2026, Title 39 (Taxation) | https://olls.info/crs/crs2026-title-39.pdf | 2026-10-28 |
| Colorado General Assembly — HB 25B-1002 (2025 special session) | https://leg.colorado.gov/bills/hb25b-1002 | 2026-10-28 |
| Cornell Law LII — 15 U.S.C. §381 (Public Law 86-272) | https://www.law.cornell.edu/uscode/text/15/381 | 2026-10-28 |

Not yet confirmed: whether Colorado has any corporate minimum tax or alternative minimum tax (v0.1 asserted "None"; the March 2026 Corporate Income Tax Guide does not mention one, but absence from a guide is not statutory confirmation); the current-year corporate interest rate for late payments (the guide's 11% figure for 2026 is stated for estimated-tax purposes); the statute citation for the delinquent-payment penalty applied to C corporations specifically (the $5 / 5% / 0.5% / 12% figures are confirmed from the DR 0106 instructions, which state the rule for that return).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

**Talk to a verified accountant** — for Colorado corporate income-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
