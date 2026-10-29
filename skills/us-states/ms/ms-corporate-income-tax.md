---
name: ms-corporate-income-tax
description: >
  Use this skill whenever asked about Mississippi corporate income tax for
  tax year 2026 — the Title 27 Chapter 7 Article 1 income tax, the
  combined-report regime (Form 83-310 on the Form 83-105 face), the
  90%-of-current-year estimated-payment rule, and the separate franchise
  tax (Title 27 Chapter 13). Trigger on "Mississippi corporate income tax",
  "83-100", "83-105", "83-310", "Mississippi combined report", "Mississippi
  franchise tax". Corrected 2026-10-29 against archived MSDOR Form 83-100
  instructions (rate table, due dates, penalties, franchise rate) and the
  DOR combined-income-filing page.
jurisdiction: US-MS
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.2
depends_on:
  - ms-income-tax
---

# Mississippi corporate income tax, tax year 2026

> **Source-cited draft.** Built from the MSDOR 2025 Corporate Income and Franchise Tax Instructions (Form 83-100, rev. 01/2026) and the DOR Combined Income Filing page, read on 2026-10-28/29. No accountant has reviewed it. Do not file from it without review by a qualified Mississippi professional.

## Who this applies to

- Every corporation, other than a QSSS (qualified subchapter "S" subsidiary), "either registered to do business in Mississippi or otherwise doing business in the state must file a combination income and franchise tax return" (DOR Combined Income Filing page).
- **Combined groups:** an "affiliated group" of corporations "may elect to file on a combined basis for purposes of the income tax provided the requirements of Title 35, Part III, Subpart 08, Chapter 07 are met" (DOR Combined Income Filing page).
- Financial institutions and certain entities also face the **franchise tax** (Title 27 Ch. 13; rate in Rates below).

## Rates, bands and thresholds

| Mississippi taxable income | Rate | Source |
|---|---|---|
| First $5,000 | 0% | [2025 Form 83-100 instructions](https://www.dor.ms.gov/sites/default/files/tax-forms/business/2025%20CIT%20INSTRUCTIONS%2083-100%20-%20Final%20%2001.14.2026.pdf) |
| Next $5,000 | 4% | 2025 Form 83-100 instructions |
| Over $10,000 | 5% | 2025 Form 83-100 instructions |

The instructions state: "Income Tax: 0% on the first $5,000 of taxable income and 4% on the next $5,000 of taxable income and 5% on all taxable income in excess of $10,000." Treat 5% as the planning default for income above $10,000.

Franchise tax: "$0.75 per $1,000 of capital, or fractional part thereof, of capital surplus, undivided profits and true reserves employed in Mississippi in excess of $100,000 (minimum tax of $25)" (2025 Form 83-100 instructions).

Estimated tax: "Every corporate taxpayer with an annual income tax liability in excess of $200 must make estimated tax payments. At least 90% of the current income tax liability must be paid by submitting quarterly payments" (2025 Form 83-100 instructions).

## The taxable base

Federal taxable income with Mississippi modifications; the instructions list Mississippi-specific differences (e.g. Mississippi "has not adopted federal provisions related to Extraterritorial Income Exclusion"). Multistate business income is apportioned "in accordance with the formulas prescribed by Title 35, Part III, Subpart 08, Chapter 06 of the Miss. Admin. Code"; the taxpayer completes Form 83-125 (multistate contractors: Form 83-124) (2025 Form 83-100 instructions). Combined-group income is summed on Form 83-310 and entered on line 4 of the reporting corporation's Form 83-105 (DOR Combined Income Filing page).

## Deadlines and filing

- "The Mississippi combination return of corporate income and franchise tax must be filed on or before the 15th day of the 4th month following the close of the accounting year" (2025 Form 83-100 instructions).
- Extension: "Mississippi will follow federal return filing and extended due dates"; tax due must be remitted with Form 83-180 by the original due date (2025 Form 83-100 instructions).
- Quarterly estimates due the 15th day of the 4th, 6th, 9th and 12th months after year end; combined groups pay estimates through the reporting corporation (2025 Form 83-100 instructions; DOR Combined Income Filing page).

## Penalties and interest

- Late payment: "The penalty imposed for failure to pay the tax when due is 1/2% per month not to exceed 25% in the aggregate"; interest "computed at 1/2 of 1% per month" (2025 Form 83-100 instructions).
- Late or non-filer: "The penalty is 5% per month not to exceed 25% in the aggregate. The penalty shall not be less than $100 for income tax for failure to file a return" (2025 Form 83-100 instructions).
- Incomplete returns: "$25 per required attachment or schedule up to a maximum of $500 per return" (2025 Form 83-100 instructions).
- Failure to file electronically: "a penalty of twenty-five dollars ($25.00) for the first instance of noncompliance and five hundred dollars ($500.00) for each additional instance" (2025 Form 83-100 instructions).
- Underestimated estimates: Form 83-305 computes interest and penalty (2025 Form 83-100 instructions).

## Cross-border points

Nexus thresholds and P.L. 86-272 protection scope are not confirmed in the archived sources (see Not yet confirmed). Mississippi taxes the Mississippi-apportioned share via the Form 83-125 factor (2025 Form 83-100 instructions).

## Worked examples

**Example 1 — $500,000 Mississippi taxable income (hypothetical client facts), using the 2025 rate table from the skill's own table above:**

```oa-check
name: MS corporate graduated 500k
inputs:
  income: 500000
steps:
  - band1: 5000 * 0.00
  - band2: 5000 * 0.04
  - band3: (income - 10000) * 0.05
  - tax: band1 + band2 + band3
expected:
  tax: 24700.00
```

**Example 2 — combined-group estimate floor (hypothetical projected current-year liability $120,000; the 90% rule is from the skill's own confirmed threshold):**

```oa-check
name: MS combined 90 percent estimates
inputs:
  projected: 120000
  pct: 0.90
steps:
  - required_estimates: projected * pct
expected:
  required_estimates: 108000.00
```

## Ask the client first

- Is the group an affiliated group that has elected combined reporting? → Form 83-310 filed with the reporting corporation's Form 83-105.
- Are intercompany fees (management fees, royalties, interest, rents) shifting income out of Mississippi inside the group?
- Any franchise-tax-applicable entity (banks, certain LLCs)? Franchise estimates are not required, but the franchise tax is due by the return due date.

## Sources

| Source | URL | Read on |
|---|---|---|
| MSDOR 2025 Corporate Income & Franchise Tax Instructions (Form 83-100, rev. 01/2026) — rate table, $200/$90% estimate rule, due dates, penalties/interest, franchise rate, e-file penalty | https://www.dor.ms.gov/sites/default/files/tax-forms/business/2025%20CIT%20INSTRUCTIONS%2083-100%20-%20Final%20%2001.14.2026.pdf | 2026-10-29 |
| DOR Combined Income Filing — combination return requirement, affiliated-group election, Form 83-310 on Form 83-105 line 4, 90% quarterly estimates via Form 83-300 | https://www.dor.ms.gov/business/corporate-income-franchise-tax/combined-income-filing | 2026-10-28 |

Not yet confirmed: nexus thresholds and P.L. 86-272 protection scope; combined-group ownership/membership tests beyond the Title 35, Part III, Subpart 08, Chapter 07 reference; intercompany addback detail and water's-edge posture; the apportionment factor mix inside the Title 35, Part III, Subpart 08, Chapter 06 formulas; whether the 2026 tax-year rate table changes from the 2025 table archived here.

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
