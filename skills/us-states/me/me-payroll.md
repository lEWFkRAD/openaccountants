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
  withholding-table method detail not line-cited.
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

Covers Maine income-tax withholding by employers and by pass-through entities. **Source status:** the MRS Employer Withholding page and the MRS Pass-through Entity Withholding page (both fetched and verified 2026-10-28) confirm: **Form 941ME is the Income Tax Withholding Quarterly Return; W-3ME annual reconciliation is no longer required and is discontinued for tax years after 2023; Rule 803 governs withholding reports and payments; Form 941P is required for partnerships and S corporations with Maine-source income that have any nonresident members; entities may withhold, obtain an exemption, or elect composite filing.** Withholding **methods and payment dates are verified from MRS Rule 803 (Chapter 803, "Income Tax Withholding Reports and Payments", archived, read 2026-10-29)**.

## Who this applies to

- **Employers paying Maine wages** (Maine residents and nonresidents working in Maine) — register, withhold per tables, file **941ME quarterly**, furnish W-2s (Maine Tax Portal upload specs verified to exist).
- **Pass-through entities with Maine-apportioned income and any nonresident member** — **941P-ME** withholding on the nonresident's share unless an exemption is obtained or a composite return is filed (verified).
- Real estate withholding (REW): "The amount to be withheld is equal to 2.5% of the sale price" and applies "to sales of property only when the consideration paid" meets the statutory threshold (MRS Real Estate Withholding page, read 2026-10-29; filed on form REW-1).

## Rates, bands and thresholds

Withholding follows the graduated 1040ME schedule (see `me-income-tax.md`, 2026 rate schedules PDF verified there). Rule 803 prescribes the methods — "1. Percentage method. The amount of tax to be deducted and withheld under the percentage method of withholding is determined using the applicable percentage method tax rate schedule" (Rule 803, archived).

## The taxable base

Wages, pensions, and backup withholding (page title verified: "Wages, Pensions, Backup"). PTE withholding base: the nonresident member's quarterly earnings apportioned to Maine (verified framing).

## Deadlines and filing

- **941ME: quarterly** (verified). Rule 803: quarterly withholding payments "are due on or before the following dates: April 30, July 31, October 31, and January 31 of the following year"; the MRS due-dates page lists 941ME on the same dates.
- Annual W-2 reconciliation: W-3ME discontinued after TY2023 (verified) — W-2s still due annually via the portal specs.
- Penalty/interest percentages: not yet confirmed (MRS interest table: 9% for 2026 — see `me-corporate-income-tax.md`; withholding-specific penalty percentages not line-cited).

## Penalties and interest

Late filing and late payment attract Maine Revenue Services penalties and interest; the published interest rate is "1/1/26 - 12/31/26 9%" (MRS Interest Rates page, read 2026-10-29). Specific penalty percentages: not yet confirmed.

## Cross-border points

Nonresident owners face withholding at the entity level (941P-ME) or a composite return aggregating all nonresidents' Maine-source income on one 1040ME (verified). See `me-cross-border.md`.

## Worked examples

**Worked example 1 — quarterly remittance (hypothetical).** Q1 Maine wages $120,000, effective withheld rate 5%:

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

**Worked example 2 — PTE withholding on a nonresident member (hypothetical).** Nonresident member's Maine-apportioned quarterly earnings $50,000, withheld at the 7.95% top marginal rate (per Rule 803 PTE amounts use "the actual income of the payee for a particular quarter or 25% of the payee's annual income"):

```oa-check
name: ME 941P hypothetical
inputs:
  member_income: 50000
  rate: 0.0795
steps:
  - withheld: member_income * rate
expected:
  withheld: 3975.00
```

## Ask the client first

- Any nonresident partners/shareholders? → 941P-ME obligation, exemption certificates, or composite election.
- Are quarterly 941ME filings current, and is the payroll system wired to the Maine Tax Portal upload specs?
- Nonresident selling Maine real property? → REW.

## Sources

| Source | URL | Read on |
|---|---|---|
| MRS Employer Withholding (941ME, ME UC-1, W-3ME discontinued, Rule 803) | https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding | 2026-10-29 |
| MRS Pass-through Entity Withholding (941P-ME, composite) | https://www.maine.gov/revenue/taxes/income-estate-tax/pass-through-entity-withholding-941p-me-returns | 2026-10-29 |
| MRS 2026 Income Tax Withholding Tables | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf | 2026-10-29 |
| MRS Rule 803 (Chap. 301) withholds on nonresident partners/shareholders | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/Rule%20803_May_2024.pdf | 2026-10-29 |

Not yet confirmed: withholding-table method details, penalty percentages for late 941ME, the exact REW consideration threshold wording, exemption-certificate form ID.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Maine payroll questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

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
