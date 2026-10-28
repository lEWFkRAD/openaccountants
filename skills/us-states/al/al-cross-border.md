---
name: al-cross-border
description: >
  Use this skill whenever asked about Alabama cross-border taxation
  for tax year 2026 — nexus standards for out-of-state corporations,
  single-sales-factor market sourcing, non-resident individuals with
  Alabama income, part-year residency, composite returns for
  non-resident pass-through members, and the absence of an Alabama
  exit tax. Trigger on "Alabama nexus", "Alabama economic nexus",
  "Alabama non-resident income tax", "Alabama part-year resident",
  "Alabama composite return", "Alabama exit tax", "Alabama remote
  seller". Source-cited draft; ALDOR corporate page read 2026-10-27;
  nexus-threshold text needs-sources.
jurisdiction: US-AL
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - al-income-tax
  - al-corporate-income-tax
---

# Alabama cross-border taxation v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Alabama's cross-border surface: (1) corporate taxation of foreign corporations limited to **Alabama-source income** (Amendment 212 language read from the ALDOR Corporate Income Tax page, 2026-10-27); (2) **single sales factor** market sourcing (ALDOR page, read 2026-10-27); (3) individual taxation of non-residents on Alabama-source income and residents on worldwide income; (4) composite/pass-through withholding for non-resident members (see `al-payroll-withholding`). **Source status:** the source-based limitation and single-factor rule are read from the ALDOR page; P.L. 86-272 protection scope, economic-nexus thresholds, non-resident filing thresholds, and the part-year proration mechanics sit in statute/regulation text not retrievable from this host this run — flagged **needs-sources**.

## 2. Who applies

- **Out-of-state corporations:** Alabama income tax attaches to income derived from sources within Alabama (ALDOR page, read 2026-10-27). Physical presence, employees, or economic activity above statutory thresholds create filing duties (thresholds **needs-sources**); P.L. 86-272 shields purely solicitation activity (application detail **needs-sources**).
- **Remote sellers:** sales-tax economic nexus (see `al-sales-tax`) — the Retail Tax Collection Act applies to remote sellers over the statutory thresholds (amounts **needs-sources**).
- **Non-resident individuals:** file Alabama Form 40 NR when Alabama-source income exceeds the filing threshold (amount **needs-sources**); non-resident tax-exempt status is available only if the home state grants the same exemption to Alabama residents (reciprocity-of-exemption rule — confirm, **needs-sources**).
- **Part-year residents:** prorate the standard deduction and exemptions by resident days (mechanics **needs-sources**).

## 3. Key rules

| Item | Rule | Source |
|---|---|---|
| Foreign corporation base | Alabama-source income only | ALDOR page (Amendment 212), read 2026-10-27 |
| Apportionment | single sales factor, market sourcing (TYB ≥ 2021) | ALDOR page, read 2026-10-27 |
| Exit tax | **none** — Alabama does not tax departing residents on deferred gains | confirm — **needs-sources** |
| In-state capital gains sourcing | situs rules for intangibles | §40-18-166 — **needs-sources** |
| Composite return | available for non-resident members of pass-throughs | Ala. Code §40-18-411 — **needs-sources** |

## 4. Deadlines

Non-resident and part-year individual returns follow the same April 15 calendar as residents. Corporations must notify Alabama of federal changes within the statutory window (days **needs-sources**).

## 5. Penalties and interest

Standard §40-2A-1 penalties (percentages **needs-sources**). Common failure modes: (1) assuming no Alabama filing because the entity has no office — employees or market sales can create nexus; (2) sourcing services to the wrong state after the 2021 single-factor switch; (3) non-resident members of an LLC ignoring composite withholding and filing nothing.

## 6. Worked examples

A Georgia company with $3,000,000 total sales, $450,000 delivered to Alabama customers, $700,000 Alabama-apportionable base after the federal-tax deduction:

```oa-check
name: AL non-resident corporate apportionment
inputs:
  al_sales: 450000
  total_sales: 3000000
  base: 700000
  rate: 0.065
steps:
  - factor: al_sales / total_sales
  - apportioned: base * factor
  - tax: apportioned * rate
expected:
  factor: 0.15
  apportioned: 105000.00
  tax: 6825.00
```

Non-resident individual with $120,000 total income, $30,000 Alabama-source wages:

```oa-check
name: AL non-resident income ratio
inputs:
  al_income: 30000
  total_income: 120000
steps:
  - ratio: al_income / total_income
expected:
  ratio: 0.25
```

## 7. Ask the client

- Does anyone live or work in Alabama, or are goods/services delivered there — has nexus been re-tested since the 2021 single-factor switch?
- For moving individuals: Alabama has no exit tax, but deferred comp earned while resident can still source to Alabama — is the sourcing documented?
- Non-resident LLC members: is the composite election or A-6 withholding being used?

## Sources

1. ALDOR Corporate Income Tax page: https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ (200, text read 2026-10-27 — source-based limitation, single sales factor)
2. ALDOR Withholding page: https://revenue.alabama.gov/taxes-fees/withholding/ (200, read 2026-10-27 — A-3/A-6 vehicles)
3. Ala. Code Title 40 ch. 18 art. 14 (non-residents): https://law.justia.com/codes/alabama/title-40/ (not fetched — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Alabama nexus and non-resident questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
