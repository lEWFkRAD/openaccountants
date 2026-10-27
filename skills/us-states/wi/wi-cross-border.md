---
name: wi-cross-border
description: >
  Use this skill whenever asked about Wisconsin cross-border personal tax for
  tax year 2026 — Form 1NPR for nonresidents and part-year residents, the
  four reciprocal states (IL, IN, KY, MI — wages exempt from WI tax for their
  full-year residents), the critical fact that Minnesota and Wisconsin have
  NO reciprocal agreement since 2009 (MN-WI commuters file both states),
  Wisconsin-source income rules (services where performed, property where
  located), the credit for tax paid to another state, and the residency
  domicile questionnaire when moving out. Wisconsin has no exit tax. Trigger
  on "Wisconsin nonresident", "1NPR", "Wisconsin reciprocity", "Minnesota
  Wisconsin reciprocity", "credit for tax paid to another state Wisconsin",
  "Wisconsin source income", "part-year Wisconsin", "work in Wisconsin live
  in Illinois".
  Source-cited draft; 2025 Form 1NPR instructions PDF read 2026-10-27
  (source-income list, reciprocity exceptions, credit section); MN
  non-reciprocity and the UI-vs-PIT localization split carried from tier-2
  wi-payroll (read 2026-07-13).
jurisdiction: US-WI
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - wi-income-tax
  - wi-payroll
---

# Wisconsin cross-border (nonresidents, reciprocity, credits) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Wisconsin professional.

## 1. Scope and sources

How Wisconsin taxes people crossing its borders: **Form 1NPR** (nonresident/part-year), the **four reciprocal states (IL, IN, KY, MI)**, the famous **Minnesota exception** (no agreement since 2009), the **credit for tax paid to another state**, and the residency/domicile mechanics. Entity cross-border (Form 4 nexus, P.L. 86-272, water's edge) sits in `wi-corporate-income-tax` and `wi-transfer-pricing`. Wisconsin has **no exit tax**.

**Source status (as_of 2026-10-27):** [2025 Form 1NPR instructions](https://www.revenue.wi.gov/TaxForms2025/2025-Form1NPR-inst.pdf) fetched as PDF and read — WI-source income list, the IL/IN/KY/MI line-1 exceptions, part-year rules, and the credit-for-tax-paid section are quoted from it. MN non-reciprocity (terminated 2009) and the UI localization split carried from tier-2 `wi-payroll` (read 2026-07-13). 2026 1NPR instructions not published at read time — figures are 2025 unless flagged.

## 2. Who applies

- **Full-year residents:** taxed on all sources (Form 1, `wi-income-tax`).
- **Nonresidents:** Wisconsin taxes **only Wisconsin-source income** — file 1NPR.
- **Part-year residents:** all sources during the WI-residency period; WI sources only otherwise. Certain credits (homestead, EIT) are **not** available to part-year residents or nonresidents.
- **Reciprocal-state residents (IL, IN, KY, MI):** full-year residents of those states working in WI are exempt from WI tax on **wages** (1NPR line-1 exceptions) — but any other WI-source income (rents, business income) still triggers a 1NPR.
- **Minnesota residents working in WI: NO reciprocity.** The MN-WI agreement was terminated in 2009 and never re-enacted — file both states, claim credits both ways (`wi-payroll` §6.1).
- **Movers out of Wisconsin:** complete the Legal Residence (Domicile) Questionnaire (1NPR instructions p. 60) — domicile drives the part-year split.

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| WI rates | Graduated 3.5%–**7.65%** (2025 worksheet: $215,530+ flat 7.65%) | 1NPR instructions, read 2026-10-27 |
| Reciprocal states | **IL, IN, KY, MI** — wages exempt for their full-year residents | 1NPR instructions, read 2026-10-27 |
| Minnesota | **No agreement since 2009** — both-state filing | `wi-payroll` (2026-07-13) |
| WI-source income | Services where performed; rents/royalties/gains from WI real or tangible property; business/farm conducted in WI | 1NPR instructions, read 2026-10-27 |
| Credit for tax paid to another state | WI residents taxed by another state claim the credit (1NPR p. 126 section) | 1NPR instructions, read 2026-10-27 |
| Nonresident credits | Homestead credit and EIT unavailable to nonresidents/part-year | 1NPR instructions, read 2026-10-27 |
| Retirement subtraction (2025) | Age 67+: up to $24,000 retirement income subtraction | 1NPR instructions, read 2026-10-27 |
| Exit tax | **None** | no WI statute imposes one |

## 4. Deadlines

| Filing | Due |
|---|---|
| 1NPR | April 15 (calendar year); federal extension carries over |
| Domicile questionnaire | With the return when moving out |
| Estimated tax (Form 1-ES) | Quarterly if 2026 liability ≥ $1,000 (threshold needs-sources) |
| Legal residence change notice | DOR Form MV300 with DMV when moving — needs-sources |

## 5. Penalties and interest

- 1NPR underpayment: WI interest on balance due (rate per return instructions — needs-sources exact 2026 rate); failure-to-file penalties per ch. 71.
- Reciprocity misuse: IL-resident claiming the wage exemption while actually a WI domiciliary is a top audit flag (`wi-payroll` §6.3 red flags: out-of-state address + WI driver's license; W-220 mismatch).
- MN commuters who skip the WI return get DOR matching notices.

## 6. Cross-border

- **Services are WI-source where performed** — telework days from an IL home are IL-source; the work-location log decides the split.
- **Reciprocity ≠ everything:** IL/IN/KY/MI residents with WI rentals, farm income, or a WI business file 1NPR for those items; the exemption is wages-only.
- **UI follows localization, not reciprocity:** an IL-resident driver localized to a WI office has no WI PIT withholding but **does** generate WI UI tax (26 U.S.C. § 3306(j) via `wi-payroll` §6.2) — the most common border-employer payroll error.
- **MN residents:** full two-state compliance; WI credit for MN tax on the same wages and vice versa.
- **Entities:** P.L. 86-272 and water's edge in `wi-corporate-income-tax` / `wi-transfer-pricing`.

## 7. Worked examples

**Example A — Illinois resident commuting to Milwaukee.**

```oa-check
name: Reciprocity zeroes WI tax on wages for IL resident
inputs:
  wi_wages: 80000
  wi_tax_if_not_reciprocal: 80000 * 0.0627
  il_tax_on_wages: 4400
steps:
  - wi_tax_due: 0
  - il_tax_due: il_tax_on_wages
expected:
  wi_tax_if_not_reciprocal: 5016.00
  wi_tax_due: 0
  il_tax_due: 4400
```

The 6.27% is an illustrative blended WI rate for the bracket range (top 7.65%, graduated) — reciprocity waives it on wages; IL taxes the full amount. Any Milwaukee rental income would still force a 1NPR.

**Example B — Minnesota resident, no reciprocity, credit both ways.**

```oa-check
name: MN commuter pays both states with WI credit for MN tax
inputs:
  wi_wages: 95000
  wi_tax_before_credit: 6200
  mn_tax_on_wi_wages: 5700
steps:
  - wi_credit: min(wi_tax_before_credit, mn_tax_on_wi_wages)
  - wi_due_after_credit: wi_tax_before_credit - wi_credit
expected:
  wi_credit: 5700
  wi_due_after_credit: 500
```

No treaty-like waiver exists with MN: the commuter files WI 1NPR, credits the MN tax on the same wages (capped at the WI figure), and owes the 500 differential to Wisconsin.

## 8. Ask the client

- Domicile on January 1 and December 31 — any move mid-year triggers part-year status and the questionnaire.
- Driver's license, vehicle registration, homestead, voter registration — the domicile evidence DOR weighs.
- Reciprocal-state resident: any WI income beyond wages? That breaks the exemption.
- MN commuters: both returns filed? Credits claimed both directions?
- Payroll: UI localization documented separately from PIT reciprocity?
- Telework calendar: how many WI work-days for a nonresident?

## 9. Sources

- [2025 Form 1NPR instructions](https://www.revenue.wi.gov/TaxForms2025/2025-Form1NPR-inst.pdf) — PDF read 2026-10-27 (source-income list, IL/IN/KY/MI exceptions, credit for tax paid to another state, part-year rules, 7.65% worksheet)
- `wi-payroll` (tier 2, read 2026-07-13) — MN non-reciprocity (terminated 2009), UI localization split, audit red flags
- `wi-income-tax` (tier 2) — resident rates and brackets
- **needs-sources:** 2026 1NPR instructions; exact 2026 bracket table; estimated-tax threshold; WI interest rate for 2026.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Wisconsin nonresident, reciprocity and MN-commuter questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
