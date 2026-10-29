---
name: co-s-corporation-tax
description: >
  Use this skill whenever asked about Colorado taxation of partnerships
  and S corporations for tax year 2026 — Form DR 0106 filing, composite
  returns for nonresident partners, the SALT Parity Act entity-level
  election (form DR 1705), 4.4% entity tax, Colorado K-1s (DR 0106K),
  the $5,000 estimated-payment threshold, receipts-factor apportionment
  for entity income, and withholding on Colorado real estate sales
  (DR 1079). Trigger on "Colorado S corporation", "Colorado composite
  return", "SALT Parity Colorado", "DR 0106", "DR 1705", "Colorado
  composite return", "Colorado K-1", "DR 0106K". Source-cited draft;
  DR 0106 instructions read 2026-10-27.
jurisdiction: US-CO
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - co-corporate-income-tax
---

# Colorado pass-through entities: composite returns & SALT Parity v0.1

## 1. Scope and sources

Covers Colorado obligations of partnerships and S corporations: the
default composite-return regime, the SALT Parity Act entity-level
election, K-1 reporting, and entity estimated payments. Primary
verified source: DR 0106 instructions, 2025 edition (PDF text read
2026-10-27 — all mechanics below are quoted or paraphrased from that
text). Statute cites (C.R.S. §39-22-101.01 etc.) pending verification.

## 2. Who applies

- Every partnership and S corporation required to file DR 0106 that
  does **not** make a SALT Parity election must file a **composite
  return** (DR 0106 Part II) paying tax on behalf of all nonresident
  partners/shareholders (verified text).
- Exceptions to composite inclusion include Colorado residents and
  certain exempt entities (verified text lists Colorado residents and
  other exceptions — read the current instructions for the full list).
- **SALT Parity election:** the entity may elect to be taxed at the
  entity level; the election is binding on all partners/shareholders
  except C-corporation partners (verified text). Election via form DR
  1705 or the SALT Parity box on DR 0106EP filed with an estimated
  payment (verified text).
- Entities making the election must mark the SALT Parity Election box
  on every DR 0106K issued (verified text).

## 3. Rates

| Item | Amount | Source |
|---|---|---|
| Entity tax (SALT Parity) / composite rate | 4.4% (0.044) | Verified DR 0106 line 20 "Multiply line 19 by 4.4% (0.044)" |
| Individual rate for non-electing residents | 4.40% flat | `co-income-tax` |
| Composite payment for nonresidents | 4.4% on each nonresident's share | Verified DR 0106 line 13 (K-1 line 16 sum must equal DR 0106 line 13) |

## 4. Base and timing

- Entity Colorado income: apportioned/allocated under C.R.S.
  §39-22-303.6 receipts-factor apportionment, or direct sourcing;
  ordinary income generally uses receipts-factor apportionment even
  without a full election (verified text).
- No activity outside Colorado → 100% sourced to Colorado (verified
  text).
- SALT Parity entity liability computed with respect to the entity's
  Colorado taxable income (verified text).
- Nonresident partners who are excluded from the composite file their
  own DR 0104 and claim credit for their share of entity-paid tax
  (verified text).

## 5. Deadlines

| Filing | Calendar-year due date |
|---|---|
| DR 0106 | 15th day of the 4th month after year close — April 15 (verified text) |
| Extension | Automatic 6-month filing extension to October 15; **no payment extension** (verified text) |
| Estimated payments (DR 0106EP) | Required quarterly when net Colorado liability (composite or SALT Parity) exceeds $5,000 (verified text) |
| DR 0106K K-1s | Filed with the Department as described in instructions (verified requirement) |

## 6. Penalties and interest

- Delinquent payment penalty: greater of $5 or 5% of additional tax
  due first month + 0.5% per additional month; shielded if 90% of tax
  paid by original due date (verified DR 0106 text).
- Estimated-tax penalty: form DR 0233, attached to the return when due
  (verified text).
- Interest under C.R.S. §39-21-118 (pending verification).

## 7. Cross-border interactions

- Composite regime is Colorado's default answer to nonresident
  partners — plan SALT Parity before year-end; election mechanics and
  binding scope verified above.
- SALT Parity deduction at entity level may interact with the federal
  SALT cap for individuals — coordinate with federal advisor.
- Colorado real-estate closing withholding (DR 1079) credits against
  the entity/partner liability (verified DR 0106 text).
- Listed/reportable transactions must be marked on DR 0106 (verified
  text).

## 8. Worked examples

An S corporation with two nonresident partners elects SALT Parity.
Entity Colorado taxable income $400,000:

```oa-check
name: SALT parity entity tax
inputs:
  income: 400000
  rate: 0.044
steps:
  - tax: income * rate
expected:
  tax: 17600.00
```

A partnership with no SALT Parity election has a nonresident partner
allocated $150,000 of Colorado income; composite tax on that share:

```oa-check
name: composite tax on nonresident share
inputs:
  share: 150000
  rate: 0.044
steps:
  - tax: share * rate
expected:
  tax: 6600.00
```

## 9. Ask the client

- Which partners are nonresidents, and does the entity want SALT
  Parity or composite filing? (Election is binding on most partners.)
- Are DR 0106Ks marked with the SALT Parity box when elected?
- Is net Colorado liability over $5,000 → quarterly DR 0106EP
  payments scheduled?
- Any Colorado real-estate closings with DR 1079 withholding to
  credit?
- Do excluded partners (residents, C corps) know their own filing
  and credit obligations?

## Sources

1. Colorado DOR — Form DR 0106 instructions (2025): https://tax.colorado.gov/sites/tax/files/documents/DR0106_2025.pdf (200 PDF, 2026-10-27)
2. Colorado DOR — Form DR 0104EP (2025): https://tax.colorado.gov/sites/tax/files/documents/DR0104EP_2025.pdf (200 PDF, 2026-10-27)
3. C.R.S. §39-22-101.01 (SALT Parity): https://leg.colorado.gov (403/404 this run — cite pending verification)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Colorado pass-through and SALT Parity questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
