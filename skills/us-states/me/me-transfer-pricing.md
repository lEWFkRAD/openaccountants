---
name: me-transfer-pricing
description: >
  Use this skill whenever asked about Maine transfer pricing and unitary
  business rules for 2026 — Rule 810 (Maine Unitary Business Taxable
  Income, Combined Reports and Tax Returns), Rule 801 apportionment,
  Rule 808 nexus, and how related-party dealings get policed in Maine
  (combined reporting rather than a standalone TP documentation regime).
  Trigger on "Maine transfer pricing", "Maine combined report", "Maine
  unitary", "Maine Rule 810", "Maine addback". Source-cited draft; rule
  numbers and their subjects verified on the MRS 1120ME page 2026-10-28;
  combined-report scope, addback statutes and documentation requirements
  needs-sources.
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

## 1. Scope and sources

Maine polices related-party pricing mainly through **unitary-business combined reporting (Rule 810)** and **apportionment (Rule 801)** rather than a standalone arm's-length documentation code. **Source status:** the MRS 1120ME page (fetched, verified 2026-10-28) lists **Rule 801 (Apportionment), Rule 808 (Corporate Income Tax Nexus), Rule 810 (Maine Unitary Business Taxable Income, Combined Reports and Tax Returns)** and a Unitary Questionnaire (PDF, updated May 2023). The **operative text of those rules and any management-fee/royalty addback statute — needs-sources** (rule text not fetched this run).

## 2. Who applies

- Corporations whose income is computed on a **combined basis** because they are part of a unitary business — the Unitary Questionnaire on the MRS page is the diagnostic form (verified to exist).
- Any filer claiming intercompany charges (management fees, royalties, interest, rents) that shift income out of Maine.

## 3. Rates / thresholds

No standalone TP rate. Exposure runs through the corporate graduated scale (see `me-corporate-income-tax.md`). Combined-report inclusion tests (ownership %, water's-edge): **needs-sources**.

## 4. Base and mechanics

- **Unitary determination:** the questionnaire + Rule 810 factors (integration, unity of ownership, economies of scale) — text **needs-sources**.
- **Combined report:** group income combined, then apportioned to Maine under Rule 801 — factor mix **needs-sources**.
- **Documentation:** no Maine-specific TP file requirement located — **needs-sources**; federal §482 work is the practical baseline.

## 5. Deadlines, penalties, interest

Combined reports ride the 1120ME calendar (due date itself **needs-sources**). Adjustments attract the same penalty/interest regime as underpaid corporate tax — percentages **needs-sources**.

## 6. Cross-border notes

Foreign affiliates inside a unitary chain may be swept into the combined report (water's-edge treatment **needs-sources**). Treaty non-relevance: state tax is not treaty-protected — standing US principle.

## 7. Worked examples

**Example 1 — combined income apportioned to Maine.** Unitary group combined taxable income $2,000,000; Maine apportionment factor 25%:

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

**Example 2 — royalty shift exposure.** A $300,000 intercompany royalty moves income from the Maine unitary member to a low-tax affiliate; with a 25% Maine factor the Maine combined base falls by $300,000 × 25% = $75,000, taxed at the 3.5% bottom band if the group is small:

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

## 8. Ask the client

- Is the group unitary (common control + operational integration)? Have you completed the MRS Unitary Questionnaire?
- What intercompany fees/royalties/interest run out of Maine entities, and are they supported by arm's-length studies?
- Are foreign affiliates in the chain — what water's-edge posture does Maine take (**needs-sources**)?

## 9. Sources

1. MRS Corporate Income Tax (1120ME) page — Rules 801/808/810 and Unitary/Nexus Questionnaires: https://www.maine.gov/revenue/taxes/income-estate-tax/corporate-income-tax-1120me — fetched and verified 2026-10-28.
2. Pre-existing `me-corporate-income-tax.md` (this pack) for rates.

**Needs-sources:** Rule 801/810 operative text, ownership thresholds, water's-edge posture, addback statutes, documentation requirements, penalty percentages.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Maine unitary/TP questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
