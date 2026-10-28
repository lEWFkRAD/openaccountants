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
  statute text read from capitol.hawaii.gov 2026-10-27.
jurisdiction: US-HI
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - hi-income-tax
---

# Hawaii cross-border taxation v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-27. This skill covers people and entities whose facts straddle Hawaii: moving in/out, part-year residence, nonresident income, and nonresident property dispositions. Statute text read from the HRS mirror at capitol.hawaii.gov 2026-10-27. **Source status:** §§235-4, 235-4.2, 235-68, 235-97, 231-39 verified from statute; the §235-1 "resident" definition text (domicile / 540-day rule commonly cited) was not extracted this run — **needs-sources**; Form N-15 instructions (tax.hawaii.gov) returned 429 — **needs-sources**.

## 2. Who applies

- **Residents:** taxed on **entire income wherever sourced** (HRS §235-4(a), text read 2026-10-27).
- **Nonresidents:** taxed only on income from Hawaii property, personal services performed in Hawaii, trade/business carried on in Hawaii, and "any and every other source in the State" (§235-4(b), text read 2026-10-27).
- **Nonresident spouse of a resident filing jointly:** the nonresident spouse's **entire** income becomes taxable (§235-4(b) — a joint-return trap; text read 2026-10-27).
- **Change of status mid-year:** income is split — residence period taxed on worldwide income, nonresidence period on Hawaii-source only; if the split can't be determined, income is prorated by the ratio of residence days to the year (§235-4(c), text read 2026-10-27).
- **Entities lacking physical presence:** §235-4.2 presumption (200+ transactions or $100,000+ Hawaii gross income/sales-factor numerator) — see `hi-corporate-income-tax`.

## 3. Mechanics and rates

| Item | Rule | Source |
|---|---|---|
| Residency test | §235-1 definitions (domicile / statutory-day test) — text not extracted | **needs-sources** |
| Part-year / nonresident return | Form N-15 (N-11 is full-year resident) | form role from `hi-income-tax` pack context; instructions **needs-sources** |
| Real property exit withholding | transferee withholds **7.25% of amount realized** on Hawaii realty sold by a "nonresident person" (§235-68(b), text read 2026-10-27); "resident person" includes Hawaii-incorporated corporations, Hawaii-formed LLCs/partnerships, resident trusts/estates (§235-68(a), text read 2026-10-27) | verified |
| Withholding exemptions/refund mechanics | later §235-68 subsections (certificates, final-return true-up) | **needs-sources** |
| Estimated tax on change of status | §235-97 calendar (4/20, 6/20, 9/20, 1/20) applies to individuals too | text read 2026-10-27 |
| Military | §235-100 persons in military service; §235-100.5 abatement on death (TOC read 2026-10-27) | section titles only |

## 4. Deadlines

- Part-year/nonresident return: same annual date as the N-11 (customarily April 20 for Hawaii individual returns per the §235-97 estimated calendar; confirm N-15 instruction — **needs-sources**).
- Real-property withholding: remitted by the transferee at/around closing per §235-68 mechanics; final liability trued-up on the Hawaii return (form HW-8/CR-8 — **needs-sources**).

## 5. Penalties and interest

§231-39 applies (5%/month failure-to-file to 25%; negligence ≤25%; fraud ≤50%; late-pay ≤20%; interest ⅔%/month — text read 2026-10-27). Cross-border failure modes: (1) resident-spouse joint return silently worldwide-taxes the nonresident spouse; (2) skipping the 7.25% withholding at closing on a nonresident seller — the **transferee** is on the hook; (3) assuming no Hawaii filing after moving away while Hawaii-source rents/services continue.

## 6. Cross-border interactions

- Federal: nonresident aliens selling Hawaii realty face federal FIRPTA 15% **on top of** the 7.25% state withholding — both are credited/refunded on the respective returns.
- No Hawaii estate tax for most estates (confirm current threshold — **needs-sources**); gift transfers of Hawaii realty still carry the conveyance-tax and future-withholding consequences.
- Treaty benefits do not override the state withholding mechanics; refund comes via the Hawaii return.

## 7. Worked examples

A taxpayer moves to Hawaii on July 1 (day 182 of 365); $90,000 income cannot be split by period:

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

A nonresident (California corporation) sells Hawaii condo for $600,000 at closing:

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

## 8. Ask the client

- Which spouse is the resident — and is the joint-return worldwide-income trap understood?
- Moving in/out mid-year: is income being tracked by period so the §235-4(c) proration isn't needed by default?
- Buying from or selling as a nonresident: is the 7.25% withholding being handled at closing, with a Hawaii return planned to recover over-withholding?
- Remote work performed while physically in Hawaii (even on vacation blocks) — Hawaii-source service income follows the body.

## Sources

1. HRS §235-4 (residents/nonresidents/change of status): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004.htm (200, text read 2026-10-27)
2. HRS §235-4.2 (nexus presumption): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004_0002.htm (200, text read 2026-10-27)
3. HRS §235-68 (7.25% nonresident realty withholding, definitions): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0068.htm (200, text read 2026-10-27)
4. HRS §235-97 (estimated tax calendar): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0097.htm (200, text read 2026-10-27)
5. HRS §231-39 (penalties/interest): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm (200, text read 2026-10-27)
6. HRS ch. 235 TOC (§235-1 definitions, §§235-100/100.5 military): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-.htm (200, read 2026-10-27)
7. Hawaii Form N-15 instructions: https://tax.hawaii.gov/forms/n-15/ (404/429 this run — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Hawaii moving/part-year/nonresident questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
