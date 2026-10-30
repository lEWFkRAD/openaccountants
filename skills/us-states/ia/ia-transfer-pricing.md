---
name: ia-transfer-pricing
description: >
  Use this skill whenever asked about Iowa related-party pricing,
  consolidated returns, and income allocation for tax year 2026 -- Iowa
  Code §422.36 fair-price and income-shifting adjustments, §422.37
  consolidated returns for IRC §1504(a) affiliated groups, §422.32
  business-income and commercial-domicile definitions, and the §422.17
  no-withholding certificate for nonresidents. Trigger on "Iowa transfer
  pricing", "Iowa consolidated return", "Iowa affiliated group", "422.36",
  "422.37", "Iowa fair price", "Iowa income shifting". Corrected 2026-10-28
  against archived Iowa Code 2026 statute text.
jurisdiction: US-IA
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - ia-corporate-income-tax
---

# Iowa transfer pricing, tax year 2026

> **Source-cited draft.** Built from Iowa Code §§422.32, 422.33, 422.36, 422.37, 422.39, 422.40 and 422.17 (Iowa Legislature, Iowa Code 2026), read on 2026-10-28. No accountant has reviewed it. Do not file, pay, amend, or take a tax position from it without review by a qualified Iowa professional.

Tax year: the corporation's federal tax year. Authority: Iowa Department of Revenue. Currency: US dollars. Covers related-party restatement, consolidated returns, and allocation definitions. Iowa has no separate transfer-pricing statute; the toolkit is §422.36(2)-(3) plus the §422.37 consolidated return.

See also: `ia-corporate-income-tax`, `ia-cross-border`.

## Who this applies to

- Any corporation taxable under §422.33 that transacts with a substantially-owned related party or is part of a commonly-controlled group (§422.36(2)-(3)).
- **Affiliated group** = "an affiliated group of corporations as defined in section 1504(a) of the Internal Revenue Code" (§422.32(1)(a)); such a group "may, not later than the due date for filing its return for the taxable year, including any extensions thereof, ... elect, and upon demand of the director shall be required, to make a consolidated return" (§422.37).

## Rates, bands and thresholds

- Restated or reallocated income carries the confirmed corporate graduated rates (5.5%/5.5%/9%/9.8% for tax years beginning on or after January 1, 2021 -- §422.33(1)(a); see `ia-corporate-income-tax`).
- The 90-day non-filing trigger: after "ninety days after the time prescribed in this subchapter for making such report or return, or for paying such tax or fee, the director may certify such fact to the secretary of state" (§422.40(1)), who may cancel a domestic corporation's articles or a foreign corporation's certificate of authority (§422.40(1)).

## The taxable base

- **Fair-price adjustment (§422.36(2)):** where a corporation liable under subchapter III sells its products "at less than the fair price which might be obtained therefor" to benefit members, stockholders or interested persons, or a substantially-owned corporation disposes of products "in such a manner as to create a loss or improper net income", "the department may determine the amount of taxable income of either or any of such corporations ... having due regard to the reasonable profits which, but for such arrangement or understanding, might or could have been obtained".
- **Income-shifting adjustment (§422.36(3)):** where a business distorts its "true net income and the net income properly attributable to the state, whether by the arbitrary shifting of income, through price fixing, charges for services, or otherwise" so that income is "arbitrarily assigned to one or another unit in a group of taxpayers carrying on business under a substantially common control", the director shall determine the proper net income "having regard to the fair profits which would normally arise from the conduct of the trade or business".
- **Business income / commercial domicile (§422.32(1)):** "'Commercial domicile' means the principal place from which the trade or business of the taxpayer is directed or managed." (§422.32(1)(c)).
- Consolidated-return conditions (§422.37): the group "shall file a consolidated return for federal income tax purposes for the same taxable year"; corporations exempt under §422.34 are excluded; the §29C.24 exception applies (§422.36(7)).

## Deadlines and filing

- Consolidated-return election: "not later than the due date for filing its return for the taxable year, including any extensions thereof" (§422.37).
- Corporate tax is due "on or before the end of the fourth month following the close of the tax year"; estimated installments run on the §422.16(12) calendar (see `ia-corporate-income-tax`).

## Penalties and interest

- Restated income carries the graduated rates plus interest; the current ch. 421 interest rate is listed under Not yet confirmed.
- **90-day cancellation:** §422.40(1) lets the director certify non-filing/non-payment (90 days or more) to the secretary of state, who may cancel articles of incorporation or the certificate of authority; exercising corporate privileges after cancellation is an offense (§422.40).
- §422.39 imports "sections 422.24 through 422.27" assessment/collection machinery, including pass-through-entity assessment under §422.25A. (not yet confirmed)

## Cross-border points

- Out-of-state corporations: Iowa taxes corporations "deriving income from sources within this state" (§422.33(1)(a)).
- Nonresident individuals/entities receiving Iowa income: withholding under §422.16(2)(b) unless the department issues a no-withholding certificate after the nonresident "pays the entire amount of tax properly estimated on or before the last day of the fourth month of the nonresident's tax year" (§422.17).
- No Iowa addback statute specific to royalties paid to related parties in zero-tax jurisdictions was located in the archived subchapter III text; absence is not confirmed from a comprehensive search.

## Worked examples

Hypothetical domestic parent sells goods to its wholly-owned out-of-state subsidiary at $60/unit where the fair price is $85/unit; 40,000 units:

```oa-check
name: IA 422.36(2) fair-price restatement
inputs:
  units: 40000
  charged: 60
  fair: 85
  top_rate: 0.098
steps:
  - understatement: (fair - charged) * units
  - extra_tax: understatement * top_rate
expected:
  understatement: 1000000.00
  extra_tax: 98000.00
```

(Client facts are hypothetical; the 9.8% top rate is the confirmed §422.33(1)(a)(4) figure for tax years beginning on or after January 1, 2021, and the restatement authority is the confirmed §422.36(2) fair-price rule.)

Hypothetical commonly-controlled group shifts $350,000 of Iowa-earning income to an affiliate via management charges; the director reallocates under §422.36(3):

```oa-check
name: IA 422.36(3) reallocation
inputs:
  shifted: 350000
  top_rate: 0.098
  saved_rate: 0.055
steps:
  - extra_tax: shifted * top_rate
  - affiliate_relief: shifted * saved_rate
  - net_effect: extra_tax - affiliate_relief
expected:
  extra_tax: 34300.00
  affiliate_relief: 19250.00
  net_effect: 15050.00
```

(Hypothetical arithmetic at the confirmed 9.8% and 5.5% bracket rates.)

## Ask the client first

- Is the group an IRC §1504(a) affiliated group -- and has the director ever demanded a consolidated Iowa return (§422.37)?
- Intercompany goods/services/intangibles: is pricing documentation defensible against the §422.36(2)-(3) restatement powers?
- Are all group members filing on the same consolidated basis for federal and Iowa (§422.37)?
- Ninety days late on any corporate filing risks charter/authority cancellation under §422.40 -- are filings current?

## Sources

| Source | URL | Read on |
|---|---|---|
| Iowa Code §422.36 (returns; fair-price and income-shifting adjustments) | https://www.legis.iowa.gov/docs/code/422.36.pdf | 2026-10-28 |
| Iowa Code §422.37 (consolidated returns) | https://www.legis.iowa.gov/docs/code/422.37.pdf | 2026-10-28 |
| Iowa Code §422.32 (definitions: affiliated group, commercial domicile) | https://www.legis.iowa.gov/docs/code/422.32.pdf | 2026-10-28 |
| Iowa Code §422.33 (corporate rates) | https://www.legis.iowa.gov/docs/code/422.33.pdf | 2026-10-28 |
| Iowa Code §422.40 (cancellation of authority for non-filing) | https://www.legis.iowa.gov/docs/code/422.40.pdf | 2026-10-28 |
| Iowa Code §422.39 (imported assessment/collection provisions) | https://www.legis.iowa.gov/docs/code/422.39.pdf | 2026-10-28 |
| Iowa Code §422.17 (no-withholding certificate) | https://www.legis.iowa.gov/docs/code/422.17.pdf | 2026-10-28 |

Not yet confirmed: Iowa's apportionment formula (property/payroll/sales factors, single-sales-factor status) and the §§422.38–422.41 allocation detail (not archived this run); the current ch. 421 interest rate on restated assessments; whether Iowa imposes any related-party royalty addback.

<!-- openaccountants-cta-block -->

---

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
