---
name: co-s-corporation-tax
description: >
  Use this skill whenever asked about Colorado taxation of partnerships
  and S corporations for tax year 2026 — Form DR 0106 filing (due April 15,
  automatic extension to October 15 with no extension of payment), composite
  returns for nonresident partners, the SALT Parity Act entity-level
  election (form DR 1705 or the DR 0106EP box; C.R.S. §§39-22-340 to 347),
  the 4.4% entity tax, Colorado K-1s (DR 0106K), the $5,000 estimated-payment
  threshold, and withholding on Colorado real estate sales (DR 1079).
  Trigger on "Colorado S corporation", "Colorado composite return",
  "SALT Parity Colorado", "DR 0106", "DR 1705", "Colorado K-1", "DR 0106K".
  DR 0106 instructions (2025) read 2026-10-28.
jurisdiction: US-CO
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
review_status: pending_review
depends_on:
  - co-corporate-income-tax
---

# Colorado pass-through entities: composite returns & SALT Parity, tax year 2026

> **Source-cited draft.** Revised 2026-10-28 against the 2025 DR 0106 instructions and the Colorado Revised Statutes 2026. v0.1 cited the SALT Parity Act as "C.R.S. §39-22-101.01"; in the 2026 statutes the SALT Parity Act is §§39-22-340 to 347, so the citation has been corrected. No accountant has reviewed this draft.

## Who this applies to

- Every partnership and S corporation required to file DR 0106 that does **not** make a SALT Parity election must file a **composite return** (DR 0106 Part II) paying tax on behalf of all nonresident partners and shareholders (DR 0106 instructions).
- A nonresident partner or shareholder who agrees to file their own Colorado return and pay the tax signs form **DR 0107**, the Colorado Nonresident Partner or Shareholder Agreement, delivered to the entity and submitted with the DR 0106 ([DR 0107 (2025)](https://tax.colorado.gov/sites/tax/files/documents/DR0107_2025.pdf)).
- **SALT Parity election:** the entity may elect to be taxed at the entity level; the election is binding on all partners or shareholders, except any partner that is a C corporation unitary with the partnership (DR 0106 instructions; C.R.S. §39-22-343). The election is made by checking box I on DR 0106, by filing form DR 1705, or by marking the SALT Parity Act election box on form DR 0106EP filed with an estimated tax payment.
- Entities making the election must check the SALT Parity Election box on every Colorado K-1 (DR 0106K) issued.

## Rates, bands and thresholds

| Item | Amount | Source |
|---|---|---|
| Entity tax (SALT Parity) / composite rate | 4.4% (0.044) | DR 0106 instructions: "Multiply line 19 by 4.4% (0.044)"; C.R.S. §39-22-344 |
| Composite payment for nonresidents | 4.4% on each nonresident's share; DR 0106 line 13 must equal the sum of line 16 of all nonresidents' DR 0106Ks | DR 0106 instructions |
| Estimated-payment threshold | Required quarterly when net Colorado liability (composite or SALT Parity) exceeds $5,000 | DR 0106 instructions; the 2026 Corporate Income Tax Guide Part 9 confirms the same $5,000 rule for C corporations |
| Individual rate for non-electing owners | 4.4% flat | `co-income-tax`; SB 24-228 (4.40% to 4.25% step, [bill page](https://leg.colorado.gov/bills/sb24-228)) |

## The taxable base

- Entity Colorado income: apportioned and allocated under [C.R.S. §39-22-303.6](https://olls.info/crs/crs2026-title-39.pdf) receipts-factor apportionment, or directly sourced; the ordinary income of a partnership is generally sourced using receipts-factor apportionment even if the partnership does not make a full election (DR 0106 instructions).
- No activity outside Colorado → 100% of income sourced to Colorado (DR 0106 instructions).
- A SALT Parity election applies to the entity's Colorado taxable income computed with respect to all partners or shareholders, including residents and nonresidents, except unitary C-corporation partners (DR 0106 instructions).
- Nonresident partners excluded from the composite file their own DR 0104 and claim credit for their share of entity-paid tax.

## Deadlines and filing

| Filing | Calendar-year due date | Source |
|---|---|---|
| DR 0106 | 15th day of the fourth month after year close — April 15 | DR 0106 instructions |
| Extension | Automatic 6-month filing extension to October 15; **no payment extension**; extension payment via DR 0158-N | DR 0106 instructions |
| Estimated payments (DR 0106EP) | Quarterly when net Colorado liability (composite or SALT Parity) exceeds $5,000 | DR 0106 instructions |
| Colorado K-1 (DR 0106K) | Completed for each partner/shareholder and filed with the Department | DR 0106 instructions |

## Penalties and interest

- Delinquent payment penalty: the greater of $5 or 5% of the additional tax due for the first month of delinquency plus 0.5% for each additional month, up to 12% in total; avoided if 90% of the tax is paid by the original due date (DR 0106 instructions).
- Estimated-tax penalty: computed on form DR 0233 and submitted with the return when due (DR 0106 instructions).
- Interest runs at the rate fixed under C.R.S. §39-21-110.5 (Colorado Revised Statutes 2026; v0.1 cited §39-21-118, which in the 2026 statutes is "Criminal penalties").

## Cross-border points

- The composite regime is Colorado's default answer to nonresident partners; a SALT Parity election is an alternative that is binding on essentially all owners — plan before year-end.
- The SALT Parity Act (C.R.S. §§39-22-340 to 347) exists because state income taxes should be deductible the same way for C corporations, S corporations, and partnerships (§39-22-341, legislative declaration); an entity-level deduction may interact with the federal SALT cap for owners — coordinate with the federal advisor.
- Colorado real-estate closing withholding (DR 1079) is credited by remitting payments with the DR 1079 and submitting the form with the return (DR 0106 instructions).
- Listed or reportable transactions must be marked on DR 0106, with IRS form 8886 or Colorado form DR 1831 attached as applicable (DR 0106 instructions).

## Worked examples

An S corporation elects SALT Parity. Entity Colorado taxable income is $400,000 (hypothetical facts; 4.4% is the confirmed rate):

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

A partnership with no SALT Parity election has a nonresident partner allocated $150,000 of Colorado income (hypothetical facts); composite tax on that share:

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

## Ask the client first

- Which owners are nonresidents, and does the entity want SALT Parity or composite filing? (The election is binding on all owners except unitary C-corporation partners.)
- If elected, is the SALT Parity Election box checked on every DR 0106K?
- Is net Colorado liability over $5,000 → quarterly DR 0106EP payments scheduled?
- Any Colorado real-estate closings with DR 1079 withholding to credit?
- Do excluded owners (residents, C corporations) know their own filing and credit obligations?

## Sources

| Source | URL | Read on |
|---|---|---|
| Colorado DOR — Form DR 0106 instructions (2025), Colorado Partnership and S Corporation Return | https://tax.colorado.gov/sites/tax/files/documents/DR0106_2025.pdf | 2026-10-28 |
| Colorado DOR — Form DR 0107 (2025), Colorado Nonresident Partner or Shareholder Agreement | https://tax.colorado.gov/sites/tax/files/documents/DR0107_2025.pdf | 2026-10-28 |
| Colorado DOR — Colorado Corporate Income Tax Guide (March 2026) | https://tax.colorado.gov/sites/default/files/documents/Corporate_Income_Tax_Guide_Mar_2026_.pdf | 2026-10-28 |
| Colorado OLLS — Colorado Revised Statutes 2026, Title 39 (Taxation) | https://olls.info/crs/crs2026-title-39.pdf | 2026-10-28 |
| Colorado DOR — Colorado Taxes & Fees Due Date Guide | https://tax.colorado.gov/due-date-guide | 2026-10-28 |

Not yet confirmed: the exact quarterly due dates for DR 0106EP estimated payments (the DR 0106 instructions state the quarterly requirement and the $5,000 threshold; the C-corporation dates are April 15, June 15, September 15 and December 15 per the Corporate Income Tax Guide Part 9, and the DR 0106 instructions say the rules for partnerships and S corporations are generally the same as for C corporations, but a pass-through-specific date table was not located in an archived source).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

**Talk to a verified accountant** — for Colorado pass-through and SALT Parity questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
