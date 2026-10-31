---
name: il-cross-border
description: >
  Use this skill whenever asked about Illinois cross-border taxation
  for tax year 2026 -- corporate and individual nexus, the single
  sales factor and throwback/throw-out, PL 86-272 solicitation
  protection, nonresident taxation of Illinois-source income at the
  4.95% flat rate plus surtax, part-year residency, and credits for
  taxes paid to other states. Trigger on "Illinois nexus", "Illinois
  nonresident", "part-year Illinois", "PL 86-272 Illinois",
  "Illinois credit for taxes paid", "Illinois-source income".
  Source-cited draft; IL-1120 instructions PDF read 2026-10-27.
jurisdiction: US-IL
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - il-income-tax
---

# Illinois cross-border (nexus, non-residents, other-state taxes) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 27 October 2026. Illinois reaches non-resident individuals and out-of-state corporations through source-based and factor-based rules: individuals pay the flat 4.95% (plus 3%/2% surtax tiers) on Illinois-source income; corporations apportion by a single sales factor with throwback/throw-out, and unitary groups combine under Schedule UB. **Source status:** the IL-1120 instructions PDF was text-read 2026-10-27 (nexus triggers for corporations, Finnigan/throwback note, pass-through attribution rule all read from it). The individual nonresident rules (IL-1040NR/IL-1040, credit for other taxes) sit in 35 ILCS 5 -- JS-rendered on ILGA, so individual-side specifics carry  flags.

### Who this applies to

- **Corporations**: Illinois nexus exists if the corporation does business in Illinois, derives Illinois-source income, **or** is qualified to do business and files federally -- regardless of income or loss (IL-1120 instructions, read 2026-10-27).
- **Nonresident individuals**: taxed on Illinois-source income (wages for Illinois work, Illinois business income, Illinois rents) -- IL-1040 (nonresident section) mechanics: .
- **Part-year residents**: full-year taxation of worldwide income for the resident period, source-only for the nonresident period (confirm current IL-1040NR instructions: ).
- **Remote workers**: wages for services performed in Illinois are Illinois-source even for nonresidents; telework from another state generally shifts source out (confirm current guidance: ).

## Rates, bands and thresholds

| Item | Amount / rule | Source |
|---|---|---|
| Individual flat rate | 4.95% | 35 ILCS 5 (section text ; rate corroborated by existing `il-income-tax.md` in this pack) |
| Surtax | 3%/2% tiers on taxable income above statutory thresholds (not yet confirmed: 35 ILCS 5/201 text not archived; see il-income-tax.md) | 35 ILCS 5/201(b) |
| Corporate combined rate | 9.5% on apportioned net income | IL-1120 PDF, read 2026-10-27 |
| Corporate apportionment | single sales factor; throwback/throw-out; Finnigan for unitary groups from TYE 2025-12-31 | IL-1120 instructions, read 2026-10-27 |
| Pass-through attribution | gains/losses from S corps/partnerships attributable to Illinois if the entity is taxable in Illinois | IL-1120 instructions, read 2026-10-27 |
| Credit for taxes paid to other states | available against IL tax per statute (mechanics ) | 35 ILCS 5/304(a) --  |

## The taxable base

The base follows the federal starting point with Illinois modifications; see Rates, bands and thresholds above and the archived IL-1040/IL-1120 instructions in Sources.

## Deadlines and filing

- IL-1120 follows the federal due date (April 15 calendar-year; instructions read 2026-10-27).
- Individual IL-1040 follows the federal due date (confirm: ).
- No Illinois entry/exit filing for individuals; withholding (IL-W-4/IW-4) is the compliance hook for nonresident employees (see `il-payroll`).

## Penalties and interest

Corporate penalties ride the IL-2220/IDOR regime (see `il-corporate-income-tax`); percentages . Common failure modes: (1) nonresident teleworkers assuming no IL source for occasional Illinois days; (2) corporations with Illinois property/payroll but no Illinois sales triggering throwback; (3) double taxation where the work state and residence state both tax -- the credit analysis must be run both ways; (4) PL 86-272 overreach into services/digital.

## Cross-border points

- **PL 86-272** (15 U.S.C. §381) bars a net-income tax on pure solicitation of tangible-goods orders shipped from outside Illinois; services, digital, and in-state fulfillment are unprotected.
- **Reciprocity**: Illinois has **no** income-tax reciprocity with neighboring states (Indiana/Kentucky/Missouri/Wisconsin each tax nonresident work income; Wisconsin reciprocity is Wisconsin-side only) -- confirm current list: .
- **PTE election**: out-of-state owners of Illinois partnerships/S corps can take Illinois PTE credits via K-1-P/K-1-T (credits verified on IL-1120 Lines 61c–61d; individual-side credit mechanics ).
- **Foreign parents**: no Illinois-specific treaty provisions; federal ECI/treaty analysis governs, Illinois conforms to federal starting point.

## Worked examples

A Missouri resident works 100% remotely from Missouri for an Illinois company (no Illinois work days):

```oa-check
name: no IL source for MO telework
inputs:
  wages: 120000
  il_days: 0
  total_days: 250
  rate: 0.0495
steps:
  - src_frac: il_days / total_days
  - il_tax: wages * src_frac * rate
expected:
  src_frac: 0.00
  il_tax: 0.00
```

A Wisconsin resident works 60 of 250 workdays in Chicago at $150,000 wages:

```oa-check
name: WI resident 60 IL workdays
inputs:
  wages: 150000
  il_days: 60
  total_days: 250
  rate: 0.0495
steps:
  - src_frac: il_days / total_days
  - il_tax: wages * src_frac * rate
expected:
  src_frac: 0.24
  il_tax: 1782.00
```

## Ask the client first

- Where is work physically performed -- how many Illinois workdays per employee?
- For corporations: property, payroll, sales footprint and whether throwback applies; is the group unitary (Schedule UB)?
- Is the residence state offering a credit for Illinois tax, and at what rate?
- Is the activity PL 86-272-protected tangible-goods solicitation?

## Sources

| Source | URL | Read on |
|---|---|---|
| IL-1120 instructions (nexus, Finnigan, pass-through attribution) | https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/business/corporate/il-1120-instr.pdf | 2026-10-27 |
| Form IL-1120 | https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/business/corporate/il-1120.pdf | 2026-10-27 |
| 15 U.S.C. 381 (PL 86-272) | https://www.law.cornell.edu/uscode/text/15/381 | 2026-10-27 |

Not yet confirmed: 35 ILCS 5 article text (JS-rendered), nonresident credit computations
## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
