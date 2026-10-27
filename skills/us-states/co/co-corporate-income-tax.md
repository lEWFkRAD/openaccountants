---
name: co-corporate-income-tax
description: >
  Use this skill whenever asked about Colorado corporate income tax for
  tax year 2026 — Form DR 0107 filing, the flat 4.4% rate under C.R.S.
  §39-22-101, receipts-factor apportionment under §39-22-303.6, nexus
  and "doing business" standards, estimated payments (DR 0107EC), the
  delinquent-payment penalty (5% + 0.5%/month), and the April 15 /
  October 15 extension mechanics. Trigger on "Colorado corporate income
  tax", "Colorado 4.4 percent", "DR 0107", "Colorado corporation tax
  rate", "Colorado receipts factor", "Colorado estimated tax
  corporation". Source-cited draft; DR 0106 instructions and Book 104
  read 2026-10-27.
jurisdiction: US-CO
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - co-income-tax
---

# Colorado corporate income tax v0.1

## 1. Scope and sources

Covers the Colorado corporate income tax (Form DR 0107), apportionment,
estimated payments, and penalties. Primary verified sources this run:
DR 0106 instructions (2025 edition, PDF text verified 2026-10-27 —
rate, due dates, penalty, estimated-payment thresholds, apportionment
references), Book 104 (2025, PDF verified). The Corporate Income Tax
Guide PDF and C.R.S. pages were 403/404 to this agent on 2026-10-27 —
statute-level cites below are flagged pending verification.

## 2. Who applies

- C corporations with Colorado-source income file DR 0107. "Doing
  business" / nexus standard: C.R.S. §39-22-103 (pending verification;
  economic nexus threshold commonly cited at $100,000 of Colorado
  sales — verify with DOR).
- Partnerships and S corporations file DR 0106 and either file
  composite returns for nonresidents or elect SALT Parity (entity-level
  tax) — see `co-s-corporation-tax`.
- S corporations are pass-throughs for Colorado unless SALT Parity is
  elected (verified DR 0106 text).

## 3. Rates

| Item | Amount | Source |
|---|---|---|
| Corporate income tax | 4.4% flat | C.R.S. §39-22-101(1)(a)(I) (pending); verified on DR 0106 instructions line 20 "Multiply line 19 by 4.4% (0.044)" (2025 form text) |
| Minimum tax | None (Colorado has no corporate minimum tax) | needs-sources — verify with DOR |
| Individual rate (SALT Parity / pass-through) | 4.40% flat | `co-income-tax` skill; Book 104 |

## 4. Base and timing

- Colorado taxable income starts from federal taxable income with
  modifications (state interest add-back, §168(k)/§174 differences,
  C.R.S. §39-22-103 et seq. — pending verification).
- Apportionment: receipts-factor apportionment under C.R.S.
  §39-22-303.6, or direct sourcing at the entity's election for some
  items (verified DR 0106 text referencing §39-22-303.6 and Rule
  39-22-109 sourcing rules).
- Income with no activity outside Colorado is sourced 100% to Colorado
  (verified DR 0106 text).

## 5. Deadlines

| Filing | Calendar-year due date |
|---|---|
| DR 0107 (C corporation) | 15th day of the 4th month after year close — April 15 (verified pattern on DR 0106 instructions; confirm for DR 0107) |
| Extension | Automatic 6-month extension to file (October 15); **no extension of payment** (verified DR 0106 text) |
| Estimated payments | Quarterly; corporations remit via DR 0107EC; individual pattern verified April 15 / June 15 / September 15 / January 15 (DR 0104EP); corporate quarterly dates per Corporate Income Tax Guide Part 9 — needs-sources |

Estimated-payment threshold for entities: partnerships/S corporations
must remit quarterly estimated payments when net Colorado liability
(composite or SALT Parity) exceeds $5,000 (verified DR 0106 text).
C-corporation threshold (commonly $1,000) — needs-sources.

## 6. Penalties and interest

- Delinquent payment penalty: greater of $5 or 5% of additional tax
  due for the first month of delinquency plus 0.5% for each additional
  month; avoided if 90% of tax is paid by the original due date
  (verified DR 0106 text).
- Estimated-tax penalty: computed on form DR 0233 (verified DR 0106
  text); individual analogue DR 0204 (verified DR 0104EP text).
- Interest: accrues on unpaid amounts at the rate under C.R.S.
  §39-21-118 (federal underpayment rate linkage — pending
  verification; Justia 403 this run).

## 7. Cross-border interactions

- Colorado conforms to federal taxable income as the starting point;
  check annual conformity legislation before relying on federal
  international provisions (pending verification).
- Public Law 86-272 protects qualifying solicitation activity from
  net-income tax (federal statute — see `co-cross-border`).
- SALT Parity election (C.R.S. §39-22-101.01 — pending verification):
  entity-level tax at 4.4%, binding election, partners get K-1 credit
  (verified mechanics on DR 0106 text).
- Composite returns: default requirement for nonresident partners
  unless SALT Parity elected (verified DR 0106 text).

## 8. Worked examples

A calendar-year C corporation has $500,000 of Colorado-sourced income
for 2026. Tax:

```oa-check
name: corporate tax on 500000
inputs:
  income: 500000
  rate: 0.044
steps:
  - tax: income * rate
expected:
  tax: 22000.00
```

A multistate corporation has Colorado receipts of $2,500,000 and total
receipts of $10,000,000; total unitary income $1,200,000 (receipts
factor):

```oa-check
name: receipts factor and tax
inputs:
  co_receipts: 2500000
  total_receipts: 10000000
  income: 1200000
  rate: 0.044
steps:
  - factor: co_receipts / total_receipts
  - apportioned: income * factor
  - tax: apportioned * rate
expected:
  factor: 0.25
  apportioned: 300000.00
  tax: 13200.00
```

## 9. Ask the client

- Does the entity have Colorado employees, property, inventory, or
  marketplace sales creating nexus?
- Is the entity a partnership/S corp — has SALT Parity been elected,
  and are composite obligations being met?
- Are estimated payments being made, and is the 90%-by-due-date
  penalty shield being maintained?
- Which apportionment method (receipts factor vs direct sourcing)
  applies to the income streams?

## Sources

1. Colorado DOR — Form DR 0106 instructions (2025): https://tax.colorado.gov/sites/tax/files/documents/DR0106_2025.pdf (200 PDF, 2026-10-27)
2. Colorado DOR — Form DR 0104EP (2025): https://tax.colorado.gov/sites/tax/files/documents/DR0104EP_2025.pdf (200 PDF, 2026-10-27)
3. Colorado DOR — Book 104 (2025): https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf (200 PDF, 2026-10-27)
4. Colorado DOR — Form DR 0107 (2025): https://tax.colorado.gov/sites/tax/files/documents/DR0107_2025.pdf (200 PDF, 2026-10-27)
5. C.R.S. §39-22-101 (income tax rate): https://leg.colorado.gov/sites/default/files/titles/39-22-101.pdf (404 to this agent 2026-10-27 — cite pending verification)
6. C.R.S. §39-22-303.6 (receipts-factor apportionment): https://leg.colorado.gov (403/404 this run — cite pending verification)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Colorado corporate income-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
