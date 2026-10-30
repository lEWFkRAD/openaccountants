---
name: me-transfer-pricing
description: >
  Use this skill whenever asked about Maine transfer pricing and unitary
  business rules for 2026 -- Rule 810 (Maine Unitary Business Taxable
  Income, Combined Reports and Tax Returns), Rule 801 apportionment,
  Rule 808 nexus, and how related-party dealings get policed in Maine
  (combined reporting rather than a standalone TP documentation regime).
  Trigger on "Maine transfer pricing", "Maine combined report", "Maine
  unitary", "Maine Rule 810", "Maine addback". Source-cited draft; rule
  numbers and their subjects verified on the MRS 1120ME page 2026-10-28;
  combined-report scope, addback statutes and documentation requirements
  addback statute not yet confirmed.
jurisdiction: US-ME
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - me-corporate-income-tax
---

# Maine transfer pricing / unitary rules v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

Maine polices related-party pricing mainly through **unitary-business combined reporting (Rule 810)** and **apportionment (Rule 801)** rather than a standalone arm's-length documentation code. **Source status:** the MRS 1120ME page (fetched, verified 2026-10-28) lists **Rule 801 (Apportionment), Rule 808 (Corporate Income Tax Nexus), Rule 810 (Maine Unitary Business Taxable Income, Combined Reports and Tax Returns)** and a Unitary Questionnaire (PDF, updated May 2023). The **operative text of those rules is now verified from the archived rule PDFs (read 2026-10-29)**; any management-fee/royalty addback statute remains not yet confirmed.

## Who this applies to

- Corporations whose income is computed on a **combined basis** because they are part of a unitary business -- the Unitary Questionnaire on the MRS page is the diagnostic form (verified to exist).
- Any filer claiming intercompany charges (management fees, royalties, interest, rents) that shift income out of Maine.

## Rates, bands and thresholds

No standalone TP rate. Exposure runs through the corporate graduated scale (see `me-corporate-income-tax.md`). Combined-report inclusion tests (ownership %, water's-edge): not yet confirmed. Rule 810 "explains standards for determining Maine income tax for unitary businesses and for filing combined reports under 36 M.R.S."; the 1120ME instructions define unitary as "characterized by unity of ownership, functional integration, centralization of management, and economic integration".

## The taxable base

- **Unitary determination:** the questionnaire + Rule 810 factors -- Rule 810 (archived) sets the standards; the 1120ME instructions state the unity-of-ownership/functional-integration/centralization-of-management/economic-integration test.
- **Combined report:** group income combined, then apportioned to Maine under Rule 801 -- "Maine utilizes a single sales factor apportionment formula" (1120ME instructions, archived).
- **Documentation:** no Maine-specific TP file requirement located -- not yet confirmed; federal §482 work is the practical baseline.

## Deadlines and filing

Combined reports ride the 1120ME calendar ("Form 1120ME due date: April 15, 2026", 1120ME instructions, archived). Adjustments attract the same penalty/interest regime as underpaid corporate tax -- estimated-tax penalty 9% compounded monthly for calendar 2026 (1120ME instructions).

## Penalties and interest

Late filing and late payment attract Maine Revenue Services penalties and interest; the published interest rate is "1/1/26 - 12/31/26 9%" (MRS Interest Rates page, read 2026-10-29). Specific penalty percentages: not yet confirmed.

## Cross-border points

Foreign affiliates inside a unitary chain may be swept into the combined report (water's-edge treatment not yet confirmed). Treaty non-relevance: state tax is not treaty-protected -- standing US principle.

## Worked examples

**Worked example 1 -- combined income apportioned to Maine (all facts hypothetical).** Unitary group combined taxable income $2,000,000; Maine apportionment factor 25%:

```oa-check
name: ME combined apportionment
inputs:
  combined: 2000000
  factor: 0.25
steps:
  - me_share: combined * factor
expected:
  me_share: 500000.00
```

**Worked example 2 -- royalty shift exposure (all facts hypothetical).** A $300,000 intercompany royalty moves income from the Maine unitary member to a low-tax affiliate; with a 25% Maine factor the Maine combined base falls by $300,000 × 25% = $75,000, taxed at the 3.5% bottom band if the group is small:

```oa-check
name: ME royalty shift exposure
inputs:
  royalty: 300000
  factor: 0.25
  rate: 0.035
steps:
  - me_base_shift: royalty * factor
  - tax_at_stake: me_base_shift * rate
expected:
  me_base_shift: 75000.00
  tax_at_stake: 2625.00
```

## Ask the client first

- Is the group unitary (common control + operational integration)? Have you completed the MRS Unitary Questionnaire?
- What intercompany fees/royalties/interest run out of Maine entities, and are they supported by arm's-length studies?
- Are foreign affiliates in the chain -- what water's-edge posture does Maine take (not yet confirmed)?

## Sources

| Source | URL | Read on |
|---|---|---|
| MRS Corporate Income Tax (1120ME) page -- Rules 801/808/810 and Unitary/Nexus Questionnaires | https://www.maine.gov/revenue/taxes/income-estate-tax/corporate-income-tax-1120me | 2026-10-29 |
| MRS Rule 801 (combined reporting) | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/Rule%20801%20-%20Clean%20Copy%205-29-25.pdf | 2026-10-29 |
| MRS Rule 810 (unitary business combination) | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/Rule_810_May_2023.pdf | 2026-10-29 |

Not yet confirmed: Rule 801/810 operative-text line-cites beyond the summaries quoted, ownership thresholds, water's-edge posture, addback statutes, documentation requirements.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Maine unitary/TP questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

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
