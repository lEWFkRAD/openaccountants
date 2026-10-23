---
name: bz-cross-border
description: >
  Belize cross-border tax reference for 2026. Covers withholding on
  non-resident interest, royalties and management/technical fees under the
  Income and Business Tax Act (Cap. 55), the 3% withholding on gross
  contract payments (s.112), chargeability of non-residents through agents
  and branches (s.25), and the double-tax-treaty relief mechanism —
  extended by the Income and Business Tax (Amendment) Act 2024 to all
  treaty countries, not just Commonwealth countries, with relief capped at
  half the Belize rate. Trigger on Belize cross-border, withholding,
  treaty relief, non-resident, double taxation. Source-cited draft.
jurisdiction: BZ
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Belize cross-border

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the Income and Business
Tax Act Cap. 55 full text (BTS PDF, Revised Edition 2011) and the Income
and Business Tax (Amendment) Act 2024 (Act No. 40 of 2024, gazetted
14 December 2024, BTS PDF). Currency BZD pegged at BZD 2.00 = USD 1.00.

**Source status caveat:** the consolidated statute text read is the 2011
Revised Edition; the 2024 Act amends the Revised Edition 2020. Non-resident
withholding rates on interest/royalties/fees are carried from the existing
bz-corporate-income-tax skill as **approximate (sources vary 15%/25% —
confirm)**; the 2011 text read here does not print a single clean rate
table for them. Belize's DTA counterparty list is **needs-sources** — no
official consolidated register resolved in this pass.

## 2. Who this applies to

- **Non-residents** deriving income from Belize are assessable and
  chargeable in the name of any attorney, factor, agent, receiver, branch
  or manager in Belize (s.25(1)), and in respect of income arising directly
  or indirectly from Belize (s.25(3)).
- **Residents** with foreign-sourced income taxed in a treaty country get
  treaty relief (s.21 as replaced in 2024 — see §5).
- **Payers** of gross contract payments must withhold 3% (s.112 — see
  bz-transfer-pricing).

## 3. Withholding rates (table)

| Flow to non-residents | Rate | Status |
|---|---|---|
| Gross contract payments (works, services, labour, materials) | 3% of gross, creditable against contractor's tax; exempt under BZD 3,000 | Cap. 55 s.112 — verified in statute text |
| Interest to non-residents | ~15% (sources vary 15%/25%) | confirm — carried from bz-corporate-income-tax |
| Royalties to non-residents | ~15% (sources vary 15%/25%) | confirm — carried from bz-corporate-income-tax |
| Management/technical fees, equipment rental | ~25% (confirm) | confirm — carried from bz-corporate-income-tax |
| Dividends | no Belize WHT on dividends paid by IBCs; domestic companies follow Cap. 55 deduction provisions | confirm per entity type |

## 4. Head-office expenditure cap for non-residents

For a non-resident, deductions for head-office expenditure are capped at
**2.5% of gross receipts** (Cap. 55, deductions division) — a standing
cross-border cost-allocation limit that behaves like a transfer-pricing
haircut on group service charges.

## 5. Treaty relief (s.21, replaced by the 2024 Amendment Act)

- The 2024 Act applies double-tax-treaty relief provisions **to all treaty
  countries, not just Commonwealth countries**.
- A person resident in Belize who proves foreign income tax paid in a
  treaty country on the same income gets Belize relief at: (a) the treaty
  country's rate, if that rate does not exceed **one-half** of the Belize
  rate appropriate to the case; otherwise (b) **one-half** of the Belize
  rate.
- Equivalent relief applies to non-residents taxed in Belize who have paid
  treaty-country tax on the same income.
- DTA counterparty list: **needs-sources** (verify with BTS before
  claiming relief).

## 6. Deadlines

- Annual income tax return: 31 March (see bz-income-tax).
- Contract-payment withholding: account and remit within 15 days after
  month end (s.112(5)).
- Business tax: monthly/quarterly per BTS guidance (see
  bz-corporate-income-tax).

## 7. Penalties and interest

- Failure to withhold/account under s.112: the amount becomes a debt to
  the Government plus a penalty of BZD 100 or 10% of the tax due,
  whichever is greater (s.112(5)).
- Late non-delivery of returns: monthly penalty continuing up to 24 months
  plus interest at 1.5% per month or part thereof (Cap. 55, assessments
  division).
- Penalty for evasion (s.116) and general penalty (s.118).

## 8. Worked examples

**Example 1 — treaty relief, low treaty rate.** A Belize resident has
USD 100,000 taxed in a treaty country at 10% (USD 10,000 paid). The Belize
rate appropriate to the case is 25% (USD 25,000). The treaty rate (10%)
does not exceed half the Belize rate (12.5%), so relief is given at the
treaty rate: USD 10,000. Belize payable = USD 15,000.

```oa-check
name: treaty relief low treaty rate USD
inputs:
  income: 100000
  belize_rate: 0.25
  treaty_rate: 0.10
steps:
  - belize_tax: income * belize_rate
  - relief: income * min(treaty_rate, belize_rate / 2)
  - payable: belize_tax - relief
expected:
  payable: 15000.00
```

**Example 2 — treaty relief, high treaty rate (cap bites).** Same income
and Belize rate; treaty country rate 20% (above the 12.5% half-rate cap),
so relief is given at half the Belize rate: USD 12,500. Belize payable =
USD 12,500.

```oa-check
name: treaty relief capped at half Belize rate USD
inputs:
  income: 100000
  belize_rate: 0.25
  treaty_rate: 0.20
steps:
  - belize_tax: income * belize_rate
  - relief: income * min(treaty_rate, belize_rate / 2)
  - payable: belize_tax - relief
expected:
  payable: 12500.00
```

## 9. Ask the client first

1. Is the counterparty in a Belize treaty country at all — and is the
   treaty one Belize actually has? (List needs-sources; verify with BTS.)
2. Are contract payments being withheld at 3% and remitted within 15 days
   of month end?
3. For non-resident businesses operating through Belize: are head-office
   charges within the 2.5% gross-receipts cap?
4. Which entity type is involved (IBC vs domestic) — dividend and
   distribution treatment differs.

## 10. Sources

- [Income and Business Tax Act, Cap. 55 (full text PDF, BTS)](https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf) — s.11 (2.5% head-office cap), s.25 (non-resident chargeability), s.112 (contract withholding), penalties division; read 2026-10-23.
- [Income and Business Tax (Amendment) Act, 2024 (Act No. 40 of 2024, PDF, BTS)](https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf) — long title (treaty relief to all treaty countries; withholding regularization), replacement s.21 relief formula; read 2026-10-23.
- [BTS — Business & Income Tax ACTs list](https://bts.gov.bz/tax_resources/category/business-and-income-tax?type=ACT) — read 2026-10-23.
- [Belize Tax Service](https://bts.gov.bz/) — read 2026-10-23.

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
