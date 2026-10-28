---
name: hi-transfer-pricing
description: >
  Use this skill whenever asked about Hawaii transfer pricing and
  related-party income allocation for tax year 2026 — three-factor
  apportionment (HRS §235-29), property/payroll/sales factor mechanics
  (§§235-30 to 235-32), nonbusiness-income allocation (§§235-24 to 235-28),
  the patent/copyright/trade-secret royalty exclusion (§235-7.3), and the
  §235-4.2 nexus presumption. Trigger on "Hawaii transfer pricing", "Hawaii
  apportionment factor", "Hawaii unitary", "Hawaii royalty exclusion",
  "HRS 235-29", "HRS 235-7.3". Source-cited draft; statute text read from
  capitol.hawaii.gov 2026-10-27.
jurisdiction: US-HI
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - hi-corporate-income-tax
---

# Hawaii transfer pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Hawaii has **no standalone transfer-pricing documentation statute**; related-party economics are policed through the **UDITPA apportionment machinery** (HRS ch. 235 part II) plus targeted royalty rules. Statute text read from the HRS mirror at capitol.hawaii.gov 2026-10-27. **Source status:** §235-29 (three-factor formula), §235-30 (property factor), §235-24 (nonbusiness income allocation), §235-7.3 (royalty exclusion), and §235-4.2 (nexus presumption) verified from statute; unitary-combination doctrine, addback rules for related-party intangibles, and the sales-factor sourcing details (§235-32) were not extracted this run — **needs-sources**.

## 2. Who applies

- Any corporation (or §235-4.2 presumed-nexus person) with **unitary business income** earned inside and outside Hawaii must apportion under §235-29.
- Groups shifting intangible income: §235-7.3 can **exclude patent/copyright/trade-secret royalties from the base entirely** when the royalties are owned by, and arise out of, a "qualified high technology business" — a Hawaii-specific lever that changes where royalty income is worth booking.
- Nonbusiness income (rents, royalties, capital gains, interest, dividends, patent/copyright royalties that are nonbusiness in character) is **allocated, not apportioned** (§235-24, text read 2026-10-27, pointing to §§235-25 to 235-27).

## 3. Mechanics

| Item | Rule | Source |
|---|---|---|
| Formula | (property + payroll + sales) ÷ 3, applied to all business income | §235-29, text read 2026-10-27 |
| Property factor | average value of real/tangible property owned or rented **and used in Hawaii** ÷ all such property everywhere | §235-30, text read 2026-10-27 |
| Payroll / sales factors | §§235-31/235-32 (TOC read 2026-10-27); sourcing detail **needs-sources** | partial |
| Nonbusiness income | allocated by situs rules in §§235-25 to 235-27 | §235-24, text read 2026-10-27 |
| Royalty exclusion | royalties from patents/copyrights/trade secrets owned by and arising out of a **qualified high technology business** are excluded from gross/taxable income | §235-7.3, text read 2026-10-27 ("qualified high technology business" definition in §235-1 — **needs-sources**) |
| Combined reporting | not found in the statute text read; Hawaii files on a separate-entity + apportionment basis — confirm current administrative practice **needs-sources** | — |
| Addbacks / substance tests for related-party intangibles | not found in text read | **needs-sources** |

## 4. Deadlines

TP positions ride the corporate return calendar (Form N-30; estimated 4/20, 6/20, 9/20, 1/20 — see `hi-corporate-income-tax`). Assessment/adjustment windows under HRS ch. 231 — **needs-sources**.

## 5. Penalties and interest

No TP-specific penalty statute read. Underpayments from factor or allocation errors draw the §231-39 regime (5%/month FTF to 25%; negligence ≤25%; fraud ≤50%; interest ⅔%/month — text read 2026-10-27). Common failure modes: (1) assuming single-sales-factor apportionment — Hawaii is three-factor, so moving payroll/property matters; (2) booking royalties into a Hawaii holding company without qualifying under §235-7.3 and getting them apportioned in anyway; (3) missing the §235-4.2 presumption when restructuring away physical presence.

## 6. Cross-border interactions

- Foreign groups: apportionment applies to the Hawaii share of unitary business income; water's-edge/combined issues — **needs-sources**.
- §235-7.3 exclusion interacts with federal §1202/§250 and GILTI planning — decoupling detail **needs-sources**.
- The 7.25% nonresident realty withholding (§235-68) can catch cross-border property exits — see `hi-payroll-withholding`.

## 7. Worked examples

Unitary group, $8,000,000 business income; factors 0.20 property, 0.24 payroll, 0.40 sales:

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

Same group books $1,200,000 trade-secret royalties through a Hawaii entity that qualifies under §235-7.3 — the royalties leave the apportioned base:

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

## 8. Ask the client

- Are property and payroll footprints being modeled — Hawaii's three-factor formula rewards them unlike single-sales-factor States?
- Any royalty structures aimed at Hawaii: does the entity meet the §235-7.3 "qualified high technology business" conditions?
- Is nonbusiness vs business character of intangible income documented (allocation vs apportionment changes the answer)?
- Post-restructuring: does the §235-4.2 presumption still pull the group in?

## Sources

1. HRS §235-29 (three-factor formula): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0029.htm (200, text read 2026-10-27)
2. HRS §235-30 (property factor): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0030.htm (200, text read 2026-10-27)
3. HRS §235-24 (nonbusiness income allocation): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0024.htm (200, text read 2026-10-27)
4. HRS §235-7.3 (royalty exclusion): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0007_0003.htm (200, text read 2026-10-27)
5. HRS §235-4.2 (nexus presumption): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004_0002.htm (200, text read 2026-10-27)
6. HRS §231-39 (penalties/interest): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm (200, text read 2026-10-27)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Hawaii related-party and apportionment questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
