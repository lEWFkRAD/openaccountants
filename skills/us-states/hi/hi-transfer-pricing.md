---
name: hi-transfer-pricing
description: >
  Use this skill whenever asked about Hawaii transfer pricing and
  related-party income allocation for tax year 2026 -- three-factor
  apportionment (HRS §235-29), nonbusiness-income allocation (§235-24),
  the patent/copyright/trade-secret royalty exclusion (§235-7.3), and the
  §235-4.2 nexus presumption. Trigger on "Hawaii transfer pricing",
  "Hawaii apportionment factor", "Hawaii unitary", "Hawaii royalty
  exclusion", "HRS 235-29", "HRS 235-7.3". Source-cited draft; statute text
  read from capitol.hawaii.gov 2026-10-27 and 2026-10-28.
jurisdiction: US-HI
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - hi-corporate-income-tax
---

# Hawaii transfer pricing v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from HRS §§235-24, 235-29, 235-7.3, 235-4.2 and §231-39, read on capitol.hawaii.gov (runs of 2026-10-27 and 2026-10-28). No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

Hawaii has **no standalone transfer-pricing documentation statute**; related-party economics are policed through the **UDITPA apportionment machinery** (HRS ch. 235 part II) plus targeted royalty rules.

## Who this applies to

- Any corporation (or §235-4.2 presumed-nexus person) with unitary business income earned inside and outside Hawaii must apportion under §235-29 (archived text): "All business income shall be apportioned to this State by multiplying the income by a fraction, the numerator of which is the property factor plus the payroll factor plus the sales factor, and the denominator of which is three."
- Groups shifting intangible income: §235-7.3 (archived text) excludes "amounts received by an individual or a qualified high technology business as royalties and other income derived from any patents, copyrights, and trade secrets" that are "owned by" and "arising out of" the qualified high technology business -- a Hawaii-specific lever that changes where royalty income is worth booking.
- Nonbusiness income: §235-24 (archived text) -- "Rents and royalties from real or tangible personal property, capital gains, interest, dividends, or patent or copyright" royalties of a nonbusiness character are allocated (not apportioned), per the situs rules in §§235-25 to 235-27.

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Formula | (property + payroll + sales) ÷ 3, applied to all business income | §235-29, archived text |
| Property factor | property-factor component of the §235-29 formula; factor sections §§235-30 to 235-32 per the archived ch. 235 TOC | §235-29 + ch. 235 TOC |
| Nonbusiness income | allocated by situs rules in §§235-25 to 235-27 | §235-24, archived text |
| Royalty exclusion | royalties from patents/copyrights/trade secrets owned by and arising out of a qualified high technology business are excluded from gross income | §235-7.3, archived text |
| Nexus presumption | 200+ transactions or $100,000+ Hawaii gross income / sales-factor numerator | §235-4.2, archived text |

The §235-30 property-factor computation details and §§235-31/235-32 payroll/sales-factor sourcing details were not extractable this run (see Not yet confirmed below); the three-factor structure itself is confirmed by §235-29.

## The taxable base

- Business income: apportioned under §235-29. Nonbusiness income: allocated under §§235-24 to 235-27.
- §235-7.3-excluded royalties leave the base entirely when the qualified-high-technology-business conditions are met (the definition of "qualified high technology business" is in §235-1 -- see Not yet confirmed below).
- Combined reporting: not found in the statute text read; Hawaii files on a separate-entity + apportionment basis (see Not yet confirmed below on current administrative practice).

## Deadlines and filing

TP positions ride the corporate return calendar (Form N-30; estimated tax 4/20, 6/20, 9/20, 1/20 per the confirmed §235-97 calendar -- see `hi-corporate-income-tax`). Assessment/adjustment windows under HRS ch. 231: see Not yet confirmed below.

## Penalties and interest

No TP-specific penalty statute was found in the text read. Underpayments from factor or allocation errors draw the §231-39 regime (failure-to-file 5%/month capped at 25%; negligence up to 25%; fraud up to 50%; late payment after timely filing up to 20%; interest at two-thirds of one per cent a month -- archived §231-39 text; see `hi-corporate-income-tax` for exact quotes). Common failure modes: (1) assuming single-sales-factor apportionment -- Hawaii is three-factor, so moving payroll/property matters; (2) booking royalties into a Hawaii holding company without qualifying under §235-7.3 and getting them apportioned in anyway; (3) missing the §235-4.2 presumption when restructuring away physical presence.

## Cross-border points

- Foreign groups: apportionment applies to the Hawaii share of unitary business income; water's-edge/combined issues -- see Not yet confirmed below.
- §235-7.3 exclusion interacts with federal §1202/§250 and GILTI planning; decoupling detail -- see Not yet confirmed below.
- The 7.25% nonresident realty withholding (§235-68(b), archived text: "every transferee shall deduct and withhold a tax equal to 7.25 per cent of the amount realized on the disposition of Hawaii real property") can catch cross-border property exits.

## Worked examples

### Example 1: unitary group, $8,000,000 business income; hypothetical factors 0.20 property, 0.24 payroll, 0.40 sales

```oa-check
name: HI three-factor apportionment
inputs:
  income: 8000000
  property_factor: 0.20
  payroll_factor: 0.24
  sales_factor: 0.40
steps:
  - factor: (property_factor + payroll_factor + sales_factor) / 3
  - hi_share: income * factor
expected:
  factor: 0.28
  hi_share: 2240000.00
```

(The ÷3 formula is the confirmed §235-29 sentence; the factor values are hypothetical client facts.)

### Example 2: same group books $1,200,000 trade-secret royalties (hypothetical client facts) through a Hawaii entity qualifying under §235-7.3 -- the royalties leave the apportioned base

```oa-check
name: HI 235-7.3 royalty exclusion effect
inputs:
  royalties: 1200000
  factor: 0.28
steps:
  - taxed_without_exclusion: royalties * factor
  - taxed_with_exclusion: 0
  - saving_base: taxed_without_exclusion - taxed_with_exclusion
expected:
  taxed_without_exclusion: 336000.00
  taxed_with_exclusion: 0.00
  saving_base: 336000.00
```

(The exclusion effect follows the confirmed §235-7.3 sentence; the royalty amount and factor are hypothetical.)

## Ask the client first

1. Are property and payroll footprints being modeled -- Hawaii's three-factor formula rewards them unlike single-sales-factor States?
2. Any royalty structures aimed at Hawaii: does the entity meet the §235-7.3 "qualified high technology business" conditions (definition in §235-1 -- see Not yet confirmed below)?
3. Is the nonbusiness vs business character of intangible income documented (allocation vs apportionment changes the answer)?
4. Post-restructuring: does the §235-4.2 presumption still pull the group in (200+ transactions / $100,000)?

## Sources

| Source | URL | Read on |
|---|---|---|
| HRS §235-29 (three-factor formula) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0029.htm | 2026-10-28 |
| HRS §235-24 (nonbusiness income allocation) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0024.htm | 2026-10-28 |
| HRS §235-7.3 (royalty exclusion) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0007_0003.htm | 2026-10-28 |
| HRS §235-4.2 (nexus presumption) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004_0002.htm | 2026-10-28 |
| HRS §231-39 (penalties/interest) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm | 2026-10-28 |
| HRS ch. 235 table of contents (§§235-25 to 235-32 factor/allocation section map) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-.htm | 2026-10-28 |

Not yet confirmed: the §235-30/31/32 factor computation details (the capitol.hawaii.gov server rate-limited those section pages this run, so only their TOC titles are cited); the §235-1 "qualified high technology business" definition text; combined-reporting / water's-edge administrative practice; addback rules and substance tests for related-party intangibles (none found in the text read); and the HRS ch. 231 assessment windows. Each was flagged in v0.2 and has not been tied to an archived primary source, so no figure for them is asserted here.

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
