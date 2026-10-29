---
name: hi-cross-border
description: >
  Use this skill whenever asked about Hawaii cross-border taxation for tax
  year 2026 — resident vs nonresident base (HRS §235-4), change-of-status
  proration, the §235-4.2 economic-nexus presumption, nonresident real
  property withholding at 7.25% (§235-68), part-year/nonresident filing
  (Form N-15), and military rules (§235-100). Trigger on "Hawaii
  nonresident", "Hawaii part-year", "Hawaii N-15", "moving to Hawaii",
  "Hawaii real property withholding", "HRS 235-4". Source-cited draft;
  statute text read from capitol.hawaii.gov 2026-10-27 and 2026-10-28.
jurisdiction: US-HI
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - hi-income-tax
---

# Hawaii cross-border taxation v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from HRS §§235-4, 235-4.2, 235-68, 235-97 and §231-39, read on capitol.hawaii.gov (runs of 2026-10-27 and 2026-10-28). No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

This skill covers people and entities whose facts straddle Hawaii: moving in/out, part-year residence, nonresident income, and nonresident property dispositions.

## Who this applies to

- **Residents:** §235-4(a) (archived text): "The tax imposed by this chapter applies to the entire income of a resident, computed without regard to source in the State."
- **Nonresidents:** §235-4(b) — the tax applies to the income received or derived from Hawaii property, personal services performed in Hawaii, trade/business carried on in Hawaii, and "any and every other source in the State."
- **Nonresident spouse of a resident filing jointly:** §235-4(b) (archived text): "In the case of a nonresident spouse filing a joint return with a resident spouse, the tax applies to the entire income of the nonresident spouse computed without regard to source in the State." — a joint-return trap.
- **Change of status mid-year:** §235-4(c) (archived text): "when the status of a taxpayer changes during the taxable year from resident to nonresident, or from nonresident to resident, the tax imposed by this chapter applies to the entire income earned during the period of residence ... and during the period of nonresidence the tax shall apply upon the income received or derived as a nonresident"; if it cannot be determined in which period income was received, it is prorated by the ratio of the residence period to the year.
- **Entities lacking physical presence:** the §235-4.2 presumption (archived text): a person that lacks physical presence in the State is presumed to be engaging in business in the State if it "engages in two hundred or more business transactions with persons within the State" or its Hawaii gross income / sales-factor numerator "equals or exceeds $100,000" — see `hi-corporate-income-tax`.

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Resident base | entire income regardless of source | §235-4(a), archived text |
| Nonresident base | Hawaii-source income only | §235-4(b), archived text |
| Change-of-status split | residence-period income worldwide; nonresidence-period income Hawaii-source; otherwise prorated by the residence-period ratio | §235-4(c), archived text |
| Economic-nexus presumption | 200+ transactions or $100,000+ Hawaii gross income / sales-factor numerator | §235-4.2, archived text |
| Real-property exit withholding | §235-68(b) (archived text): "every transferee shall deduct and withhold a tax equal to 7.25 per cent of the amount realized on the disposition of Hawaii real property." | §235-68, archived text |
| Estimated tax on change of status | §235-97 calendar applies to individuals (first voucher "on or before April 20"; June 20, September 20, and the fourth-quarter payment "by January 20 of the year following") | §235-97, archived text |
| Military | §235-100 persons in military service; §235-100.5 abatement on death (section titles from the archived ch. 235 TOC) | ch. 235 TOC |

## The taxable base

- Residents: entire income. Nonresidents: Hawaii-source income (with the joint-return trap above). Part-year: split or prorated per §235-4(c).
- Nonresident sellers of Hawaii realty: 7.25% withheld from the "amount realized" (§235-68); the transferee is made liable for the tax (§235-68, archived text).

## Deadlines and filing

- Part-year/nonresident individuals file Form N-15 instead of the resident Form N-11 (the archived DOTAX rate schedules are stated for both "Form N-11, Line 26 or Form N-15, line 43"); for tax year 2025 the DOTAX tax-year page states the April 20, 2026 filing deadline and automatic 6-month extension for "Form N-11 or N-15". See Not yet confirmed below for the N-15 instruction details.
- Real-property withholding: remitted by the transferee per §235-68 mechanics; final liability is trued-up on the Hawaii return (exemption-certificate mechanics — see Not yet confirmed below).

## Penalties and interest

§231-39 applies (failure-to-file 5%/month capped at 25%; negligence up to 25%; fraud up to 50%; late payment after timely filing up to 20%; interest at two-thirds of one per cent a month — archived §231-39 text; see `hi-corporate-income-tax` for exact quotes). Cross-border failure modes: (1) a resident-spouse joint return silently worldwide-taxes the nonresident spouse; (2) skipping the 7.25% withholding at closing on a nonresident seller — the **transferee** is on the hook ("Every person required to withhold a tax under this section is made liable for the tax", §235-68); (3) assuming no Hawaii filing after moving away while Hawaii-source rents/services continue.

## Cross-border points

- Federal FIRPTA withholding can also apply to nonresident aliens selling U.S. (including Hawaii) realty, in addition to the state 7.25% withholding — see Not yet confirmed below for the federal rate and mechanics.
- No Hawaii estate tax for most estates (see Not yet confirmed below for the current threshold); gift transfers of Hawaii realty still carry conveyance-tax and future-withholding consequences (see Not yet confirmed below for the conveyance-tax rate).
- Treaty benefits do not override the state withholding mechanics; refund comes via the Hawaii return.

## Worked examples

### Example 1: taxpayer moves to Hawaii on July 1 (day 182 of 365); $90,000 income cannot be split by period (hypothetical client facts)

```oa-check
name: HI change-of-status proration
inputs:
  income: 90000
  residence_days: 182
  year_days: 365
steps:
  - hi_attributable: income * residence_days / year_days
expected:
  hi_attributable: 44876.71
```

(The residence-period proration follows the confirmed §235-4(c) rule; the income and dates are hypothetical.)

### Example 2: nonresident (California corporation) sells a Hawaii condo for $600,000 at closing (hypothetical client facts)

```oa-check
name: HI nonresident closing withholding
inputs:
  realized: 600000
  rate: 0.0725
steps:
  - withheld: realized * rate
expected:
  withheld: 43500.00
```

(The 7.25% rate is the confirmed §235-68(b) sentence.)

## Ask the client first

1. Which spouse is the resident — and is the joint-return worldwide-income trap understood (§235-4(b))?
2. Moving in/out mid-year: is income being tracked by period so the §235-4(c) proration isn't needed by default?
3. Buying from or selling as a nonresident: is the 7.25% withholding being handled at closing, with a Hawaii return planned to recover over-withholding?
4. Remote work performed while physically in Hawaii (even on vacation blocks) — Hawaii-source service income follows the body (§235-4(b) source rules)?
5. Any military-service or §235-100.5 abatement situations in the family?

## Sources

| Source | URL | Read on |
|---|---|---|
| HRS §235-4 (residents/nonresidents/change of status) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004.htm | 2026-10-28 |
| HRS §235-4.2 (nexus presumption: 200+ transactions / $100,000) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004_0002.htm | 2026-10-28 |
| HRS §235-68 (7.25% nonresident realty withholding; transferee liability) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0068.htm | 2026-10-28 |
| HRS §235-97 (estimated tax calendar) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0097.htm | 2026-10-28 |
| HRS §231-39 (penalties/interest) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm | 2026-10-28 |
| HRS ch. 235 table of contents (§235-1 definitions; §§235-100/100.5 military) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-.htm | 2026-10-28 |
| DOTAX Tax Rate Schedules (Form N-11 line 26 / Form N-15 line 43 usage) | https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/ | 2026-10-28 |
| DOTAX Tax Year 2025 Information (April 20, 2026 deadline and 6-month extension for Form N-11 or N-15) | https://tax.hawaii.gov/tax-year-information/ | 2026-10-28 |

Not yet confirmed: the §235-1 "resident" definition text (domicile / 540-day rule commonly cited — not extracted this run); Form N-15 instruction details (the tax.hawaii.gov forms page was unreachable this run); the federal FIRPTA withholding rate and mechanics (v0.2 said 15% — a federal figure, not verified against an archived federal source this run); the Hawaii estate-tax threshold; the conveyance-tax rate; the §235-68 exemption certificates and refund forms (v0.2 mentioned HW-8/CR-8 — not verified); and the §235-100 military-rule text beyond the TOC titles. Each was flagged in v0.2 and has not been tied to an archived primary source, so no figure for them is asserted here.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
