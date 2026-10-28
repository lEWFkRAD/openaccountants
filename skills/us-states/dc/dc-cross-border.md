---
name: dc-cross-border
description: >
  Use this skill whenever asked about District of Columbia
  cross-border taxation for tax year 2026 — DC-source income for
  non-resident individuals (D-40NR), non-resident entity filing
  through mandatory combined reporting, the absence of a DC exit
  tax, P.L. 86-272 scope, non-resident withholding, and the
  special DC rule that DC residents working abroad generally do
  NOT get a foreign-tax credit for income taxed where earned.
  Trigger on "DC non-resident", "DC D-40NR", "District of Columbia
  source income", "DC combined reporting foreign", "DC foreign tax
  credit", "DC P.L. 86-272", "DC exit tax". Source-cited draft;
  OTR pages read 2026-10-27; statutory detail needs-sources.
jurisdiction: US-DC
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - dc-income-tax
  - dc-franchise-tax
---

# District of Columbia cross-border taxation v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. DC cross-border rules: individuals are taxed on **residency** (DC residents: worldwide income on D-40; non-residents: DC-source income on D-40NR); entities are pulled in through **mandatory combined reporting** for unitary groups (OTR Combined Reporting page, fetched 2026-10-27, 200, text read — combination required for TYB ≥ 2011-01-01). DC has **no entity exit tax** regime (confirm — **needs-sources**). **Source status:** the combined-reporting mandate is read from the OTR page; DC-source definitions, D-40NR mechanics, the foreign-tax-credit posture for DC residents working abroad, and P.L. 86-272 administration sit in DC Code Title 47 ch. 18 / OTR individual pages not extracted this run — flagged **needs-sources**.

## 2. Who applies

- **Non-resident individuals** with DC-source income (work performed in DC, DC rents, DC business income) file **D-40NR** (form family confirmed via OTR; thresholds **needs-sources**).
- **Non-resident entities**: any member of a unitary group with DC nexus is swept into the combined return (OTR page, read 2026-10-27) — physical presence is not the only hook once unity + DC nexus exist.
- **P.L. 86-272**: solicitation-only protection for tangible-goods sales (federal statute; DC administration **needs-sources**).
- **DC residents working abroad/overseas**: DC generally taxes worldwide income; the availability of a credit for foreign income taxes is narrow — **needs-sources** (this is a known DC trap for military/diplomatic/expat households).

## 3. Key rules

| Item | Rule | Source |
|---|---|---|
| Entity nexus | unitary-group membership + DC nexus → combined return | OTR page, read 2026-10-27 |
| Water's edge | availability/mechanics **needs-sources** | not extracted |
| Individual non-resident filing | D-40NR on DC-source income; threshold **needs-sources** | OTR form family |
| Exit tax | none identified — confirm | **needs-sources** |
| Foreign tax credit (residents abroad) | narrow/uncertain — **needs-sources** | DC Code §47-1808 et seq. not extracted |

## 4. Deadlines

D-40NR follows the individual calendar (April 15). Entity combined returns follow the franchise calendar (see `dc-franchise-tax`). Federal audit-change reporting window to OTR: **needs-sources**.

## 5. Penalties and interest

DC Code §47-1801.11 penalties (percentages **needs-sources**). Common failure modes: (1) foreign subsidiaries left off the combined return without a confirmed water's-edge position; (2) DC-resident employees seconded abroad assuming the host country's tax relieves DC — it generally does not; (3) non-resident individuals with DC workdays (remote weeks in DC) missing D-40NR; (4) P.L. 86-272 assumed to cover services/SaaS — it does not.

## 6. Worked examples

A non-resident individual worked 40 of 200 workdays in DC, salary $150,000:

```oa-check
name: DC non-resident workday sourcing
inputs:
  dc_days: 40
  total_days: 200
  salary: 150000
steps:
  - ratio: dc_days / total_days
  - dc_source: salary * ratio
expected:
  ratio: 0.20
  dc_source: 30000.00
```

A unitary group with a foreign subsidiary excluded pending water's-edge confirmation; combined income $8,000,000, DC factor 0.10 (illustrative):

```oa-check
name: DC combined foreign-sub exposure
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

## 7. Ask the client

- Foreign subsidiaries: on the combined return or excluded under a documented water's-edge position?
- DC-resident employees working abroad: is DC worldwide taxation modeled in the assignment cost?
- Remote workers with DC workweeks: D-40NR and withholding covered?
- Tangible-goods sellers: is the P.L. 86-272 activity inventory actually solicitation-only?

## Sources

1. OTR Combined Reporting: https://otr.cfo.dc.gov/page/combined-reporting-business-entities (200, text read 2026-10-27)
2. OTR Business Franchise Tax Rates: https://otr.cfo.dc.gov/page/dc-business-franchise-tax-rates (200, read 2026-10-27)
3. DC Code Title 47 ch. 18: https://code.dccouncil.gov/us/dc/council/code/titles/47/chapters/18/ (200; section text not extracted — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for DC cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
