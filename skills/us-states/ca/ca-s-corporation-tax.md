---
name: ca-s-corporation-tax
description: >
  Use this skill whenever asked about California S-corporation taxation
  for tax year 2026 — Form 100S filing, the 1.5% entity-level tax and
  $800 minimum franchise tax under R&TC §23803, shareholder K-1 (Form
  100S Schedule K-1) reporting on Form 540, the QSSS election, estimated
  tax for S corporations, and the interaction with the FTB minimum
  franchise tax. Trigger on "California S corporation tax", "Form 100S",
  "1.5 percent S corp California", "California QSSS", "FTB S corp
  minimum tax", "California K-1". Source-cited draft; Form 100S read
  2026-10-27.
jurisdiction: US-CA
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ca-corporate-income-tax
---

# California S-corporation tax (Form 100S) v0.1

## Who this applies to
Covers the California entity-level tax on S corporations (Form 100S),
shareholder-level pass-through reporting, and the QSSS election. Does
not cover C-corporation franchise tax (see `ca-corporate-income-tax`)
or LLCs taxed as S corporations (Form 568 overlay may apply — verify
with FTB). Primary sources: FTB Form 100S (2025 edition, PDF verified
2026-10-27); R&TC §23803 (leginfo returned 403 to this agent — cite
pending verification).

## Rates, bands and thresholds
| Item | Amount | Source |
|---|---|---|
| Entity-level tax | 1.5% of California net income | R&TC §23803 (cite pending verification — leginfo 403 2026-10-27) |
| Minimum franchise tax | $800 | R&TC §23153 (cite pending verification); FTB Form 100S line 21 "at least minimum franchise tax, if applicable" (verified form text) |
| Shareholder-level | Ordinary CA rates (1–13.3%) on K-1 income | `ca-income-tax` skill | (not yet confirmed)

Form 100S line 21 reads "Tax. ____% × line 20 (at least minimum
franchise tax, if applicable)" — the rate itself is printed in the
instructions, not on the form face (verified 2025 form text).

## The taxable base
- California S-corporation net income starts from federal ordinary
  business income with state modifications (state interest add-backs,
  NOL differences).
- Apportionment follows the same single sales factor rules as
  corporations (R&TC §§25128–25129; see `ca-corporate-income-tax` §4).
- Distributions of previously taxed income are generally not taxed
  again at shareholder level; reasonable-compensation analysis is
  federal but affects CA wages on Form 540 withholding.

## Deadlines and filing
| Filing | Calendar-year due date |
|---|---|
| Form 100S | 15th day of the 3rd month after year close — March 15 |
| Form 7004 extension | 6-month extension to file (September 15); payment not extended |
| Estimated tax (Form 3539) | April 15, June 15, September 15, December 15 (S corporations pay CA estimated tax — verify current safe-harbor percentages in Form 100S instructions) |

## Penalties and interest
- Same FTB penalty/interest regime as corporations: 25% late-filing
  penalty on unpaid tax, interest at the published FTB rate (FTB
  penalties-and-interest pages, verified 2026-10-27).
- Estimated-tax underpayment penalty applies; computed per FTB
  instructions.

## Cross-border points
- QSSS election: a qualifying S corporation subsidiary of an S parent
  is disregarded for California franchise purposes; QSub income flows
  to the parent's Form 540 (FTB Form 100S instructions — verify current
  mechanics).
- Nonresident shareholders pay CA tax on their share of CA-source
  K-1 income; composite/withholding mechanics exist via Forms 592/593
  (referenced on verified Form 100S text).
- Other states' PTE (pass-through entity) elective taxes do not have a
  California analogue as of this run — verify before advising.

## Worked examples
A calendar-year S corporation has $300,000 of California net income for
2026. Entity tax:

```oa-check
name: S corp entity tax on 300000
inputs:
  income: 300000
  rate: 0.015
  minimum: 800
steps:
  - tax: income * rate
  - due: max(minimum, tax)
expected:
  tax: 4500.00
  due: 4500.00
```

The same S corporation has $50,000 of California net income:

```oa-check
name: S corp minimum franchise tax floor
inputs:
  income: 50000
  rate: 0.015
  minimum: 800
steps:
  - tax: income * rate
  - due: max(minimum, tax)
expected:
  tax: 750.00
  due: 800.00
```

## Ask the client first
- Has FTB recorded the S election, and is the entity in good standing
  with the Secretary of State?
- Is the entity an LLC that elected S status federally? Which FTB form
  governs?
- Are nonresident shareholders aware of CA filing obligations on K-1
  income (and Forms 592/593 withholding)?
- Is a QSSS/QSub structure in place, and does it still qualify?
- Are estimated payments being made on the corporate schedule?

## Sources
| Source | URL | Read on |
| --- | --- | --- |
| FTB — Form 100S (2025) | https://www.ftb.ca.gov/forms/2025/2025-100S.pdf | 2026-10-28 |
| FTB — Corporation Tax Rates | https://www.ftb.ca.gov/file/business/tax-rates.html | 2026-10-28 |
| FTB — Penalties and Interest | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html | 2026-10-28 |

Not yet confirmed: the 1.5% entity-level tax rate, $800 minimum franchise tax, shareholder rates (1–13.3%), Form 7004 extension dates, estimated-tax schedule and safe-harbor percentages, and the R&TC §§23803 and 23153 statute cites (leginfo 403 on 2026-10-27) are not yet confirmed against archived sources.

## Talk to a verified accountant
<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for California S-corporation questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
