---
name: ca-s-corporation-tax
description: >
  Use this skill whenever asked about California S-corporation taxation
  for tax year 2026 -- Form 100S filing, the 1.5% entity-level tax and
  $800 minimum franchise tax under R&TC §23802(b)(1) and §23153, shareholder K-1 (Form
  100S Schedule K-1) reporting on Form 540, the QSSS election, estimated
  tax for S corporations, and the interaction with the FTB minimum
  franchise tax. Trigger on "California S corporation tax", "Form 100S",
  "1.5 percent S corp California", "California QSSS", "FTB S corp
  minimum tax", "California K-1". Source-cited draft; 2025 Form 100S
  booklet and R&TC §§23802/23803/23153 read 2026-11-01.
jurisdiction: US-CA
category: state-tax
tax_year: 2025
tier: 2
last_updated: 2026-11-02
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
or LLCs taxed as S corporations (Form 568 overlay may apply -- verify
with FTB). Primary sources: FTB 2025 Form 100S booklet and FTB Form
100S (2025 edition); R&TC §23802 (S-corp tax rate), §23803 (S election
and consent -- not the tax-rate section), and §23153 (minimum
franchise tax), all archived from leginfo 2026-11-01.

## Rates, bands and thresholds
| Item | Amount | Source |
|---|---|---|
| Entity-level tax | 1.5% of California net income | R&TC §23802(b)(1): "The tax imposed under Section 23151 or 23501 shall be imposed at a rate of 11/2 percent rather than the rate specified in those sections" |
| Minimum franchise tax | $800 | R&TC §23153(d)(1) ("a minimum franchise tax of eight hundred dollars ($800)"); FTB Form 100S line 21 "at least minimum franchise tax, if applicable" |
| Shareholder-level | Ordinary CA rates (1% to 13.3% top bracket incl. 1% behavioral health surcharge) on K-1 income | `ca-income-tax` skill (2025 Form 540 booklet, archived) |

Form 100S line 21 reads "Tax. ____% × line 20 (at least minimum
franchise tax, if applicable)" -- the rate itself is printed in the
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
| Form 100S | 15th day of the 3rd month after year close -- March 15 |
| Automatic filing extension | 6 months (to September 15 for calendar-year filers); no application required -- "No application is required for an extension to file" (FTB extension-to-file page). Payment is NOT extended: pay the balance with FTB 3539 by the original due date |
| Estimated tax | Four installments: 15th day of the 4th, 6th, 9th, and 12th months of the tax year (April 15, June 15, September 15, December 15 calendar year); the 1st payment may not be less than the minimum franchise tax plus QSub annual tax, if applicable (2025 Form 100S booklet) |

## Penalties and interest
- Same FTB penalty/interest regime as corporations: 25% late-filing
  penalty on unpaid tax, interest at the published FTB rate (FTB
  penalties-and-interest pages, verified 2026-10-27).
- Estimated-tax underpayment penalty applies; computed per FTB
  instructions.

## Cross-border points
- QSSS election: a qualifying S corporation subsidiary of an S parent
  is disregarded for California franchise purposes; QSub income flows
  to the parent's Form 540 (FTB Form 100S instructions -- verify current
  mechanics).
- Nonresident shareholders pay CA tax on their share of CA-source
  K-1 income; composite/withholding mechanics exist via Forms 592/593
  (referenced on verified Form 100S text).
- Other states' PTE (pass-through entity) elective taxes do not have a
  California analogue as of this run -- verify before advising.

## Worked examples

### Worked example 1: Entity tax on $300,000 of CA net income

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

### Worked example 2: Minimum franchise tax floor

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
| R&TC section 23802 (S corporation tax rate) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23802 | 2026-11-01 |
| R&TC section 23803 (S election and consent) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23803 | 2026-11-01 |
| R&TC section 23153 (minimum franchise tax) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153. | 2026-11-01 |
| FTB 2025 Form 100S Booklet | https://www.ftb.ca.gov/forms/2025/2025-100S-booklet.pdf | 2026-11-01 |
| FTB Payment for Automatic Extension (FTB 3539, 2025) | https://www.ftb.ca.gov/forms/2025/2025-3539.pdf | 2026-11-01 |
| FTB Extension to File | https://www.ftb.ca.gov/file/when-to-file/extension-to-file.html | 2026-11-01 |

Not yet confirmed: the QSSS/QSub California mechanics beyond the 100S booklet text, the Forms 592/593 withholding details, the estimated-tax safe-harbor percentages (100% of prior year vs 110%), and whether an LLC that elected S status files Form 100S or Form 568 with an S overlay.
## Talk to a verified accountant
<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for California S-corporation questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
