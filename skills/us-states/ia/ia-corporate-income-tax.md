---
name: ia-corporate-income-tax
description: >
  Use this skill whenever asked about Iowa corporate income tax for tax
  year 2026 — Iowa Code ch. 422 subchapter III: graduated rates 5.5%/5.5%/
  9%/9.8% with a statutory receipts-trigger rate adjustment, net income
  computed from federal taxable income with listed bond adjustments,
  combined reporting for affiliated groups, the §422.36 fair-price/
  income-shifting adjustment, and the corporate estimated-tax calendar.
  Trigger on "Iowa corporate income tax", "Iowa Form 4562C", "Iowa
  combined return", "Iowa unitary", "Iowa corporate rates", "422.33",
  "422.35". Source-cited draft; Iowa Code 2026 text read from
  legis.iowa.gov 2026-10-27.
jurisdiction: US-IA
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ia-income-tax
---

# Iowa corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-27. Iowa's corporate income tax lives in Iowa Code ch. 422, subchapter III (§§422.33–422.44). Statute text read directly from the Iowa Code 2026 PDFs at legis.iowa.gov 2026-10-27 (each section fetched and extracted). **Source status:** §§422.33 (rates + receipts trigger), 422.34 (exemptions), 422.35 (net income adjustments), 422.36 (returns + fair-price adjustment) verified from statute text; the combined-reporting section (§422.37) and apportionment sections (§§422.38–422.41) were identified but their full text was not extracted this run — **needs-sources** for combined-group mechanics and the apportionment formula detail. Form identifiers (4562C) from tax.iowa.gov — site returned 404 on guessed paths — **needs-sources**.

## 2. Who applies

- Every corporation "doing business in this state, or deriving income from sources within this state" (§422.33(1)(a), text read 2026-10-27).
- **Exempt:** banks, credit unions, title insurance/trust companies, savings & loans, production credit associations, insurance companies/associations, reciprocal exchanges, fraternal beneficiary associations, and §501 organizations (unless federal exemption denied under §§501–504 IRC) (§422.34, text read 2026-10-27). Financial institutions pay the franchise tax instead (subchapter V, 3.8% for tax years beginning in 2026 — §422.63(2)(e), text read 2026-10-27).
- Affiliated groups file a **combined return** (§422.37 — section exists; text not extracted, **needs-sources** for the unitary/affiliation test).

## 3. Rates and base

| Bracket (taxable income) | Rate (tax years beginning on/after 1 Jan 2021) | Source |
|---|---|---|
| First $25,000 | 5.5% | §422.33(1)(a)(1), text read 2026-10-27 |
| $25,000–$100,000 | 5.5% | §422.33(1)(a)(2), same |
| $100,000–$250,000 | 9% | §422.33(1)(a)(3), same |
| Over $250,000 | 9.8% | §422.33(1)(a)(4), same |

- **Receipts-trigger adjustment:** if net corporate income tax receipts for the preceding fiscal year exceed **$700 million**, the department of revenue must adjust rates downward (first the top rate, floor 5.5%) (§422.33(1)(b), text read 2026-10-27). Current-year applied rates: confirm against the department's annual rate determination — **needs-sources**.
- **Base:** "net income" = federal taxable income under the IRC with adjustments — subtract federal bond interest/dividends; add foreign and (otherwise federally exempt) state/local bond interest with a long list of Iowa-exempt program bonds; plus various Iowa-specific deductions (e.g., 65% wage deduction for certain new hires capped $20,000/individual; 100% exclusion of employee-owner qualified-corporation capital gains for tax years beginning on/after 1 Jan 2025) (§422.35, text read 2026-10-27).
- Iowa conforms to federal with a rolling conformity date — **needs-sources** for the current date.

## 4. Deadlines

- Corporate return: due on or before the end of the **fourth month** following close of the tax year (calendar-year filers: April 30) — §422.16(12)(b)(3) states the general "end of the fourth month following the close of the tax year" rule (text read 2026-10-27); corporate-specific section §422.36 requires a signed return but the date text sits in the general provisions — confirm §422.38 assessment window **needs-sources**.
- **Estimated tax:** required if liability reasonably expected ≥ $1,000; quarterly installments due last day of the 4th, 6th, 9th, and 1st months of the tax year (§422.16(12), text read 2026-10-27).

## 5. Penalties and interest

- Failure-to-file/failure-to-pay and interest run under ch. 421/422 general provisions — **needs-sources** for current percentages (not extracted this run).
- §422.36(2)-(3) give the department power to restate income where a corporation sells to/from a substantially-owned affiliate "at less than the fair price" or where income is "arbitrarily shifted... through price fixing, charges for services, or otherwise" within a commonly-controlled group (text read 2026-10-27) — Iowa's core related-party adjustment authority.
- Franchise-tax filers: §422.11 credit mechanics (text read 2026-10-27).

## 6. Cross-border interactions

- Nonresident/foreign corporations: income sourced within Iowa is taxed; allocation/apportionment under §§422.38–422.41 (existence confirmed via cross-references; text **needs-sources**).
- PTE election: partnerships/S corps may elect entity-level tax at the individual rate under §422.16C (text read 2026-10-27) — relevant to foreign owners avoiding Iowa composite filings.
- Water's-edge / combined-group international issues: **needs-sources**.

## 7. Worked examples

Corporation with $400,000 Iowa-allocated net income, calendar-year filer:

```oa-check
name: IA corporate graduated tax 400k
inputs:
  b1: 25000
  b2: 75000
  b3: 150000
  b4: 150000
  r1: 0.055
  r3: 0.09
  r4: 0.098
steps:
  - t1: b1 * r1
  - t2: b2 * r1
  - t3: b3 * r3
  - t4: b4 * r4
  - total: t1 + t2 + t3 + t4
  - effective: total / (b1 + b2 + b3 + b4)
expected:
  t1: 1375.00
  t2: 4125.00
  t3: 13500.00
  t4: 14700.00
  total: 33700.00
  effective: 0.08
```

(Effective 8.425% — the graduated structure still bites above $250k.)

Same corporation shifts $200,000 of profit to an out-of-State affiliate via an intercompany service fee; department restates under §422.36(3) and the fee is added back to Iowa income at the top marginal rate:

```oa-check
name: IA 422.36 addback at top rate
inputs:
  shifted: 200000
  top_rate: 0.098
steps:
  - extra_tax: shifted * top_rate
expected:
  extra_tax: 19600.00
```

## 8. Ask the client

- Are estimated installments sized to the ≥$1,000 threshold and the 4th/6th/9th/1st-month calendar?
- Is the group affiliated enough to require a combined return — and has the §422.37 test been applied?
- Any intercompany pricing (goods, services, intangibles) that §422.36(2)-(3) could restate?
- Financial institution? The franchise tax (3.8% for 2026) replaces the corporate tax — plus the §422.11 credit mechanics.

## Sources

1. Iowa Code §422.33 (corporate tax imposed; rates; receipts trigger): https://www.legis.iowa.gov/docs/code/422.33.pdf (200, text read 2026-10-27)
2. Iowa Code §422.34 (exempt corporations): https://www.legis.iowa.gov/docs/code/422.34.pdf (200, text read 2026-10-27)
3. Iowa Code §422.35 (net income adjustments): https://www.legis.iowa.gov/docs/code/422.35.pdf (200, text read 2026-10-27)
4. Iowa Code §422.36 (returns; fair-price/income-shifting adjustment): https://www.legis.iowa.gov/docs/code/422.36.pdf (200, text read 2026-10-27)
5. Iowa Code §422.16 (estimated tax calendar): https://www.legis.iowa.gov/docs/code/422.16.pdf (200, text read 2026-10-27)
6. Iowa Code §422.63 (franchise tax rates): https://www.legis.iowa.gov/docs/code/422.63.pdf (200, text read 2026-10-27)
7. Iowa Department of Revenue: https://tax.iowa.gov/ (guessed paths 404 this run — form IDs and current applied rates **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Iowa corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
