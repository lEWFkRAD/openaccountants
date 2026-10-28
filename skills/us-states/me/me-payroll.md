---
name: me-payroll
description: >
  Use this skill whenever asked about Maine payroll withholding for 2026 —
  the Income Tax Withholding Quarterly Return (Form 941ME), the
  discontinued W-3ME annual reconciliation (ended after tax year 2023),
  withholding for nonresident partners and shareholders via Form 941P-ME,
  composite returns for nonresident owners, and Rule 803 reports and
  payments. Trigger on "Maine withholding", "941ME", "941P-ME", "Maine
  W-2", "Maine composite return", "Maine nonresident partner". Source-cited
  draft; form IDs, quarterly cadence, W-3ME discontinuation and the PTE
  withholding/composite framework verified on MRS pages 2026-10-28;
  withholding-table figures and deposit thresholds needs-sources.
jurisdiction: US-ME
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - me-income-tax
---

# Maine payroll withholding v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## 1. Scope and sources

Covers Maine income-tax withholding by employers and by pass-through entities. **Source status:** the MRS Employer Withholding page and the MRS Pass-through Entity Withholding page (both fetched and verified 2026-10-28) confirm: **Form 941ME is the Income Tax Withholding Quarterly Return; W-3ME annual reconciliation is no longer required and is discontinued for tax years after 2023; Rule 803 governs withholding reports and payments; Form 941P is required for partnerships and S corporations with Maine-source income that have any nonresident members; entities may withhold, obtain an exemption, or elect composite filing.** Withholding **table figures and payment-frequency thresholds are in Rule 803 / the instructions — needs-sources**.

## 2. Who applies

- **Employers paying Maine wages** (Maine residents and nonresidents working in Maine) — register, withhold per tables, file **941ME quarterly**, furnish W-2s (Maine Tax Portal upload specs verified to exist).
- **Pass-through entities with Maine-apportioned income and any nonresident member** — **941P-ME** withholding on the nonresident's share unless an exemption is obtained or a composite return is filed (verified).
- Real estate withholding (REW) applies to certain Maine real-property sales by nonresidents (nav link verified; thresholds **needs-sources**).

## 3. Rates / tables

Withholding follows the graduated 1040ME schedule (see `me-income-tax.md`, 2026 rate schedules PDF verified there). Exact percentage/method tables: **needs-sources** (Rule 803 text not fetched).

## 4. Base

Wages, pensions, and backup withholding (page title verified: "Wages, Pensions, Backup"). PTE withholding base: the nonresident member's quarterly earnings apportioned to Maine (verified framing).

## 5. Deadlines, penalties, interest

- **941ME: quarterly** (verified). Due dates: last day of the month following each calendar quarter expected — **needs-sources**.
- Annual W-2 reconciliation: W-3ME discontinued after TY2023 (verified) — W-2s still due annually via the portal specs.
- Penalty/interest percentages: **needs-sources**.

## 6. Cross-border notes

Nonresident owners face withholding at the entity level (941P-ME) or a composite return aggregating all nonresidents' Maine-source income on one 1040ME (verified). See `me-cross-border.md`.

## 7. Worked examples

**Example 1 — quarterly remittance.** Q1 Maine wages $120,000, effective withheld rate 5%:

```oa-check
name: ME quarterly withholding
inputs:
  wages: 120000
  eff_rate: 0.05
steps:
  - withheld: wages * eff_rate
expected:
  withheld: 6000.00
```

**Example 2 — PTE withholding on a nonresident member (illustrative rate).** Nonresident member's Maine-apportioned quarterly earnings $50,000, withheld at the 7.95% top marginal rate pending table confirmation:

```oa-check
name: ME 941P illustrative
inputs:
  member_income: 50000
  rate: 0.0795
steps:
  - withheld: member_income * rate
expected:
  withheld: 3975.00
```

## 8. Ask the client

- Any nonresident partners/shareholders? → 941P-ME obligation, exemption certificates, or composite election.
- Are quarterly 941ME filings current, and is the payroll system wired to the Maine Tax Portal upload specs?
- Nonresident selling Maine real property? → REW.

## 9. Sources

1. MRS Employer Withholding: https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding — fetched and verified 2026-10-28 (941ME, ME UC-1, W-3ME discontinued, Rule 803).
2. MRS Pass-through Entity Withholding: https://www.maine.gov/revenue/taxes/income-estate-tax/pass-through-entity-withholding-941p-me-returns — fetched and verified 2026-10-28 (941P, composite filing).
3. Pre-existing `me-income-tax.md` (rate schedules): repo file.

**Needs-sources:** withholding tables/methods, 941ME due dates, penalty/interest percentages, REW thresholds, exemption-certificate form ID.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Maine payroll questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
