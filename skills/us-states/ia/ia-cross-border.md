---
name: ia-cross-border
description: >
  Use this skill whenever asked about Iowa cross-border personal tax
  situations for tax year 2026 — nonresident taxation of Iowa-source income
  (§422.19 receipt-basis rule), the flat 3.8% rate for residents and
  nonresidents alike, part-year filing, the §422.17 no-withholding
  certificate, PTE election vs. composite returns for out-of-state owners,
  and the absence of neighbor reciprocity in the statute read. Trigger on
  "Iowa nonresident", "Iowa part-year", "Iowa commuter", "Iowa-source
  income", "422.19", "Iowa composite return", "Iowa PTE". Source-cited
  draft; Iowa Code 2026 text read from legis.iowa.gov 2026-10-27.
jurisdiction: US-IA
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - ia-income-tax
---

# Iowa cross-border v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-27. Iowa's individual income tax is a **flat 3.8%** for tax years beginning on/after Jan 1, 2025 (SF 2442 (2024) completed the reform; §422.5 as amended — amendment text read 2026-10-27). **Source status:** §422.19 (nonresident scope), §422.17 (no-withholding certificate), §422.16C (PTE election), §422.16(2) (nonresident withholding) verified from statute text; **residency-domicile definition, part-year proration mechanics, and Form IA 1040 nonresident schedule (IA 1040NR) line mechanics** — **needs-sources** (not extracted this run).

## 2. Who applies

- **Iowa residents:** worldwide income, flat 3.8% (§422.5 as amended, text read 2026-10-27).
- **Nonresidents:** Iowa-source income only; the tax applies to income **actually received** in the year regardless of when earned — accrual filers: when it first became demandable (§422.19, text read 2026-10-27).
- **Part-year residents:** both resident and nonresident periods in the year — proration mechanics **needs-sources**.
- **Withholding agents** paying Iowa-source income to nonresidents: withhold under §422.16(2)(b) at the same rate unless a §422.17 certificate is produced (text read 2026-10-27).

## 3. Mechanics

- **Nonresident withholding:** agents withhold on nonresident Iowa income; the nonresident can obtain a **certificate authorizing payment without withholding** by paying the entire estimated Iowa tax on or before the **last day of the fourth month** of their tax year (§422.17, text read 2026-10-27). If actual payments exceed the certificate estimate, the agent must withhold (§422.17, text read 2026-10-27).
- **PTE election (§422.16C, text read 2026-10-27):** partnerships/S corps elect annual entity-level tax at 3.8%; out-of-state owners avoid Iowa individual/composite filings; election irrevocable for the year. Composite-return alternative under §422.16B — mechanics **needs-sources**.
- **Iowa-source income** for individuals: services performed in Iowa, Iowa real/tangible property, Iowa business (§422.16(2)(a)(1) sweep; individual sourcing detail **needs-sources**).
- **Reciprocity:** no neighbor-reciprocity exemption appears in the §422.16 text read — IL/MN/NE/WI commuters should be treated as taxable in Iowa absent contrary guidance — **needs-sources** confirmation.

## 4. Deadlines

- IA 1040/1040NR: April 30 (Iowa conforms to federal extensions — **needs-sources** for extension mechanics).
- Estimated tax: installments at the last day of the 4th, 6th, 9th, and 1st months when liability ≥ $1,000 (§422.16(12), text read 2026-10-27).
- §422.17 certificate: estimated payment by the last day of the fourth month of the tax year (§422.17, text read 2026-10-27).

## 5. Penalties and interest

- Underpaid nonresident tax: withholding-agent liability runs to the agent personally (§422.16(5), text read 2026-10-27); taxpayer penalties/interest under ch. 421 — rates **needs-sources**.
- Overwithheld amounts ≥ $1 refunded with interest (§422.16(10), text read 2026-10-27) — a common commuter recovery path.

## 6. Cross-border interactions

- Moving to/from Iowa: mid-year moves create part-year status; the §422.19 receipt rule can pull Iowa income into the nonresident year even when earned earlier.
- Remote workers: physical presence in Iowa for services creates Iowa-source wages regardless of employer location (see ia-social-contributions for the UI mirror).
- Foreign owners of Iowa flow-throughs: PTE election substitutes entity-level tax; otherwise withholding + §422.17 certificate route.

## 7. Worked examples

Wisconsin resident works 120 of 250 Iowa job-site days, wages $90,000, agent withholds nothing:

```oa-check
name: IA nonresident sourced wages
inputs:
  wages: 90000
  iowa_days: 120
  work_days: 250
  rate: 0.038
steps:
  - sourced: wages * (iowa_days / work_days)
  - tax: sourced * rate
expected:
  sourced: 43200.00
  tax: 1641.60
```

(Day-count sourcing is illustrative — confirm IA 1040NR allocation mechanics, **needs-sources**.)

Same taxpayer obtains a §422.17 certificate by paying $1,641.60 estimated tax by April 30:

```oa-check
name: IA 422.17 certificate funding check
inputs:
  estimated_tax: 1641.60
  threshold: 1000
steps:
  - above_estimated_threshold: estimated_tax - threshold
expected:
  above_estimated_threshold: 641.60
```

## 8. Ask the client

- Commuter or remote worker: is Iowa withholding happening, or is a §422.17 certificate in place?
- Mid-year move: part-year proration and the §422.19 receipt rule reviewed?
- Out-of-state owners of Iowa partnerships: PTE election vs. composite vs. individual filings — which is cheaper at 3.8% flat?
- Overwithheld commuters: refund claim with interest available under §422.16(10).

## Sources

1. Iowa Code §422.19 (scope of nonresident tax): https://www.legis.iowa.gov/docs/code/422.19.pdf (200, text read 2026-10-27)
2. Iowa Code §422.17 (no-withholding certificate): https://www.legis.iowa.gov/docs/code/422.17.pdf (200, text read 2026-10-27)
3. Iowa Code §422.16 (withholding; estimated tax; refunds): https://www.legis.iowa.gov/docs/code/422.16.pdf (200, text read 2026-10-27)
4. Iowa Code §422.16C (PTE election): https://www.legis.iowa.gov/docs/code/422.16C.pdf (200, text read 2026-10-27)
5. Iowa Code §422.5 (flat 3.8% individual rate as amended): https://www.legis.iowa.gov/docs/code/422.5.pdf (200, text read 2026-10-27)
6. Iowa Department of Revenue: https://tax.iowa.gov/ (guessed paths 404 this run — IA 1040NR mechanics **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Iowa cross-border personal questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
