---
name: kn-value-added-tax
description: >
  Saint Kitts and Nevis value added tax reference for 2026. Covers the 17%
  standard rate, monthly tax periods, the EC$150,000 registration threshold,
  input-tax deduction, filing and payment deadlines, the 1.25%-per-month
  interest charge and registration offences. Uses the official Law Commission
  consolidation of the Value Added Tax Act (Cap. 18.47). Post-2017 amendment
  reconciliation and accountant review remain open; source-cited draft.
jurisdiction: KN
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Saint Kitts and Nevis value added tax

## 1. Scope and sources

Source-cited draft checked 22 October 2026 from the Value Added Tax Act, Cap. 18.47 (official consolidation, revision date 31 December 2017), read in full from the Law Commission site. Amounts are East Caribbean dollars. **Caveat: not a complete post-2017 amendment audit — verify the threshold and rate against current IRD guidance before filing.**

## 2. Who is charged

- Every **taxable person** making taxable supplies in the Federation, and every **importer** of goods; the recipient of imported services (s.26).
- A person carrying on a taxable activity must register within 14 days of exceeding (or expecting to exceed) **EC$150,000** of taxable supplies in a 12-month / 365-day window (s.13(4)).
- Supplying without registration is an offence: fine up to EC$30,000 or two years' imprisonment or both (s.13(3)).

## 3. Rates

| Source | All rates below | [Value Added Tax Act, Cap. 18.47, s.27](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_47-Value-Added-Tax-Act.pdf) |
|---|---:|---|
| Standard rate on taxable supplies and imports | 17% | |
| Zero-rated supplies | 0% | Second Schedule (exports, supplies of a going concern, others listed) |
| Exempt supplies | — | First Schedule (financial services, education, health, others listed) |

## 4. Base and input tax

Tax is charged on the value of the supply (supply value rules, s.28 ff). Registered persons deduct input tax on acquisitions used in making taxable supplies, subject to the allocation and disallowance rules (ss.40–42). Tax invoices are required for supplies to registered recipients (s.44).

## 5. Deadlines

- **Tax period: the calendar month** (s.46).
- Return due within **15 calendar days** after the end of the tax period, whether or not tax is payable (s.47).
- Payment due by the return due date (s.51).

## 6. Penalties and interest

- Interest on unpaid VAT: **1.25% per month** (or part) from the due date (s.43; alterable by Order).
- Late filing under the Tax Administration and Procedures Act, Cap. 20.52 s.37: 5% of tax owing plus EC$100 per month of continuing failure.
- Failure to register: offence penalty above (s.13(3)).

## 7. Cross-border points

- Exports of goods and most services to outside the Federation are zero-rated (Second Schedule) — verify the item against the Schedule.
- Imported services: the local recipient accounts for VAT (reverse charge, s.26(2)(c)).
- Registration applies to non-residents making taxable supplies; the registration test for a person not resident in the Federation is modified by s.13(5).

## 8. Worked examples

**Example 1 — registered retailer, EC$84,000 gross takings in a month, EC$4,500 input tax.**
Output tax = 84,000 × 17/117 = 12,205.13. Net payable = 12,205.13 − 4,500 = 7,705.13.

```oa-check
name: Retailer gross takings EC$84,000
inputs:
  gross: 84000
  input_tax: 4500
steps:
  - output: gross * 0.17 / 1.17
  - payable: output - input_tax
expected:
  payable: 7705.13
```

**Example 2 — the same EC$7,705.13 paid three months late.**
Interest = 7,705.13 × 1.25% × 3 = 288.94. Late-filing penalty = 7,705.13 × 5% = 385.26. Total additional = 674.20; total cost 8,379.33.

```oa-check
name: Late VAT EC$7,705.13, three months
inputs:
  due: 7705.13
steps:
  - interest: due * 0.0125 * 3
  - penalty: due * 0.05
  - total: due + interest + penalty
expected:
  total: 8379.33
```

## 9. Ask the client first

1. Are annual taxable supplies near or above EC$150,000 (registration trigger)?
2. Which supplies are exempt or zero-rated — classify against the Schedules.
3. Are imported services being received (reverse charge)?
4. Are tax invoices being issued and retained for input claims?

## 10. Sources

- [Value Added Tax Act, Cap. 18.47](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_47-Value-Added-Tax-Act.pdf) — read 2026-10-22.
- [Tax Administration and Procedures Act, Cap. 20.52](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf) — read 2026-10-22.
