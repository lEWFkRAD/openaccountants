---
name: dc-cross-border
description: >
  Use this skill whenever asked about District of Columbia
  cross-border taxation for tax year 2026 — the Home Rule bar on
  taxing non-resident individuals' income (commuter refunds on Form
  D-40B), non-resident entity filing through mandatory combined
  reporting, P.L. 86-272 scope, and the position of DC residents
  working abroad. Trigger on "DC non-resident", "DC D-40B",
  "District of Columbia source income", "DC combined reporting
  foreign", "DC P.L. 86-272", "DC commuter tax".
jurisdiction: US-DC
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - dc-income-tax
  - dc-franchise-tax
---

# District of Columbia cross-border taxation, tax year 2026

> **Source-cited draft.** Built from D.C. Code §§ 1-206.02, 47-1807.02, 47-1808.03 and 47-1810.02, the OTR Combined Reporting and Business Franchise Tax Rates pages, and the OTR 2025 Form D-40B, read on 2026-10-28. No accountant has reviewed it. Do not take a position from it without review by a qualified professional.

DC's cross-border posture is unusual: **individuals are taxed only on residency**, while **entities are pulled in through mandatory combined reporting** for unitary groups.

## Who this applies to

- **Non-resident individuals.** The Home Rule Act bars the Council from imposing "any tax on the whole or any portion of the personal income ... of any individual not a resident of the District" ([D.C. Code § 1-206.02](https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02)). A commuter who lives in Maryland or Virginia and works in DC files no DC income-tax return; there is no DC non-resident individual return. DC tax withheld in error from a non-resident's wages is recovered on **Form D-40B, Nonresident Request for Refund** ([2025 D-40B](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40B_Form_012026.pdf)).
- **Part-year residents** file the D-40 for the DC-domicile period only, with prorated deduction and credits (see `dc-income-tax`).
- **Non-resident entities:** any member of a unitary group with DC nexus is swept into the combined franchise return — "For tax years beginning on or after January 1, 2011, a corporation or unincorporated business entity subject to tax and engaged in a unitary business with one or more corporations or unincorporated business entities" must report on a combined basis ([OTR Combined Reporting page](https://otr.cfo.dc.gov/page/combined-reporting-business-entities), read 2026-10-28). Physical presence is not the only hook once unity and DC nexus exist.
- **DC residents working abroad:** DC taxes residents on worldwide income; the availability of a credit for foreign income taxes paid by a resident is not confirmed in the archived sources (see the Not yet confirmed line).

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Non-resident individual income tax | **Barred** — no tax on any portion of a non-resident's personal income | [D.C. Code § 1-206.02](https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02) |
| Commuter withholding refund | Form D-40B, available to a non-resident "who did not maintain a place of abode in DC for a total of 183 days or more" whose only DC-source income was wages | [2025 D-40B](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40B_Form_012026.pdf) |
| Entity nexus | Unitary-group membership + DC nexus → combined return, TYB ≥ 1 January 2011 | [OTR Combined Reporting page](https://otr.cfo.dc.gov/page/combined-reporting-business-entities) |
| Combined-group rate | 8.25% on DC-apportioned taxable income; $250/$1,000 minimum tax | [D.C. Code § 47-1807.02](https://code.dccouncil.gov/us/dc/council/code/sections/47-1807.02); [§ 47-1808.03](https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.03) |
| Apportionment of business income | Single sales factor | [D.C. Code § 47-1810.02(d-2)](https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02) |

## The taxable base

- **Individuals:** residency, not source. Residents report worldwide income; non-residents report nothing (subject only to erroneous withholding, recovered on D-40B with the W-2s and, from tax year 2025, a copy of the home state's return attached).
- **Entities:** the unitary group's combined taxable income, apportioned to DC by the sales factor alone ([§ 47-1810.02(d-2)](https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02)); intragroup transactions are eliminated in combination.

## Deadlines and filing

- **D-40B** follows the individual calendar (15 April; the 2025 form can be filed on MyTax.DC.gov from tax year 2025).
- **Entity combined returns** follow the franchise-tax calendar — estimated payments 15 April, 15 June, 15 September, 15 December with the 110% prior-year safe harbor (see `dc-franchise-tax`).

## Penalties and interest

- Failure-to-file/failure-to-pay additions of 5% a month up to 25%, and 10%-a-year interest compounded daily, apply to DC returns generally ([D.C. Code § 47-4213](https://code.dccouncil.gov/us/dc/council/code/sections/47-4213); [§ 47-4201](https://code.dccouncil.gov/us/dc/council/code/sections/47-4201), both archived 2026-10-28).
- Common failure modes: (1) foreign subsidiaries left off the combined return without a confirmed water's-edge position; (2) DC-resident employees seconded abroad assuming the host country's tax relieves DC — DC taxes residents on worldwide income; (3) non-resident individuals with DC tax withheld in error never filing the D-40B refund claim; (4) P.L. 86-272 assumed to cover services or software — the federal statute protects only solicitation of orders for tangible personal property.

## Cross-border points

- **Combined reporting** pulls out-of-District unitary affiliates into the DC computation; foreign affiliates' water's-edge treatment is not confirmed in the archived sources (see the Not yet confirmed line).
- **P.L. 86-272** (federal statute): solicitation-only protection for tangible-goods sellers; DC's administration of it was not read from an archived source this run.
- **Remote workers:** an out-of-state employer whose employee performs services in DC has DC withholding and DOES registration duties (see `dc-payroll-withholding`, `dc-unemployment-contributions`); the non-resident employee still owes no DC income tax.
- **No DC entity exit-tax regime** is described in the archived sources.

## Worked examples

Client facts below are hypothetical; all rates are the confirmed figures from the tables above.

**A unitary group with $8,000,000 combined net income and a DC sales-factor share of 0.10:**

```oa-check
name: DC combined group apportioned tax
inputs:
  combined_income: 8000000
  factor: 0.10
  rate: 0.0825
steps:
  - dc_base: combined_income * factor
  - tax: dc_base * rate
expected:
  dc_base: 800000.00
  tax: 66000.00
```

**A commuter's refund:** a Maryland resident, never maintaining a DC abode for 183 days or more, had $2,000 of DC tax withheld from DC wages in 2025. The client files Form D-40B with the W-2s and a copy of the Maryland return, and recovers the full $2,000 — no DC income tax applies to a non-resident's wages ([D.C. Code § 1-206.02](https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02); [2025 D-40B](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40B_Form_012026.pdf)).

## Ask the client first

- Foreign subsidiaries: on the combined return or excluded under a documented water's-edge position?
- DC-resident employees working abroad: is DC worldwide taxation modeled in the assignment cost?
- Commuters with DC withholding: D-40B refund claims filed (with the home-state return attached)?
- Tangible-goods sellers: is the P.L. 86-272 activity inventory actually solicitation-only?
- Entity nexus: is every unitary member on the combined return?

## Sources

| Source | URL | Read on |
|---|---|---|
| D.C. Code § 1-206.02 (Home Rule bar on taxing nonresident income) | https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02 | 2026-10-28 |
| D.C. Code § 47-1807.02 (corporate rate and minimum tax) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1807.02 | 2026-10-28 |
| D.C. Code § 47-1808.03 (unincorporated business rate and minimum tax) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.03 | 2026-10-28 |
| D.C. Code § 47-1810.02 (apportionment; single sales factor) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02 | 2026-10-28 |
| D.C. Code § 47-4213 (failure-to-file/pay additions) | https://code.dccouncil.gov/us/dc/council/code/sections/47-4213 | 2026-10-28 |
| D.C. Code § 47-4201 (interest, 10% compounded daily) | https://code.dccouncil.gov/us/dc/council/code/sections/47-4201 | 2026-10-28 |
| OTR: Combined Reporting of Business Entities | https://otr.cfo.dc.gov/page/combined-reporting-business-entities | 2026-10-28 |
| OTR: DC Business Franchise Tax Rates | https://otr.cfo.dc.gov/page/dc-business-franchise-tax-rates | 2026-10-28 |
| OTR 2025 Form D-40B (PDF) | https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40B_Form_012026.pdf | 2026-10-28 |

Not yet confirmed: the water's-edge treatment of foreign affiliates in a DC combined report; DC's administration of P.L. 86-272 (the federal statute protects solicitation-only sales of tangible personal property, but DC-side guidance was not archived this run); the availability of a DC foreign-tax credit for residents working abroad; and the federal audit-change reporting window to OTR.

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
