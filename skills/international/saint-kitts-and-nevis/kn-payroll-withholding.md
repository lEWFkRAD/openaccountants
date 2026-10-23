---
name: kn-payroll-withholding
description: >
  Saint Kitts and Nevis payroll withholding reference for 2026. Covers PAYE
  deduction on emoluments under Income Tax Act s.69, the non-resident payment
  withholding at 15% under s.40, remittance duties, the 10% non-remittance
  penalty, and how PAYE interacts with social security and the housing levy.
  Uses the official Law Commission consolidation of the Income Tax Act
  (Cap. 18.22). Employer remittance deadlines under the Income Tax Rules
  need IRD confirmation; source-cited draft.
jurisdiction: KN
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Saint Kitts and Nevis payroll withholding

## 1. Scope and sources

Source-cited draft checked 22 October 2026 from the Income Tax Act, Cap. 18.22 (consolidation, revision date 31 December 2017), read in full from the Law Commission site. Companion payroll levies are covered in `kn-social-security-contributions` and `kn-housing-social-development-levy`. Amounts are East Caribbean dollars.

## 2. Who withholds

- **Employers** paying emoluments (s.69, with s.70 definitions): PAYE must be deducted on each payment of emoluments arising in or received in the State, under the Income Tax Rules made under s.40, using the Tax Tables (s.71), whether or not an assessment exists.
- **Payers to non-residents** (s.40, as amended by Act 2 of 2016): withholding at **15%** on a long list of payments — rents, interest, insurance premiums, service and management fees, professional fees, expense recharges, other periodic payments — irrespective of whether the payment produces income in the recipient's hands.

## 3. Rates and mechanics

| Item | Rate / rule | Basis |
|---|---|---|
| PAYE on emoluments | Tax Tables rates (same progressive schedule as `kn-income-tax-individuals`), via employee declaration under s.68 | s.69, s.71 |
| Withholding on payments to non-residents | 15% of the gross payment | s.40(1) (Act 2 of 2016) |
| Non-resident withholding return + payment | quarterly, on or before 15 March / June / September / December for the preceding quarter | s.40(2)(b) (Act 3 of 2014) |
| Certificate to the non-resident | required, stating amount and tax withheld | s.40(2)(a) |

PAYE remittance timing follows the Income Tax Rules made under s.40; the consolidated Act does not print the day-count. **Confirm the current remittance cycle with the IRD before setting payroll calendars (needs-sources).**

## 4. Employee side

An employee whose emoluments are subject to PAYE is relieved from instalments on that part of income (s.67(5)); where withheld emoluments are at least three-quarters of total income, the remainder of estimated tax is payable by **1 July** following the year (s.67(6)).

## 5. Penalties

- Failure to remit deducted/withheld amounts: penalty of **10% of the unremitted amount or EC$10, whichever is greater**, plus the amount itself, plus **5% per annum interest** (s.69(3)).
- Directors' personal liability for unwithheld amounts: Tax Administration and Procedures Act s.39.

## 6. Cross-border points

- The 15% s.40 withholding is the main tool for services, rents and fees paid to non-residents — it applies even to expense recharges and shared costs within groups (see `kn-transfer-pricing`).
- Double-taxation relief for a non-resident recipient is only available where an in-force DTA Order applies (verify against the scheduled Orders; see `kn-cross-border`).

## 7. Worked examples

**Example 1 — PAYE shortfall.** An employee's year-end self-assessment shows total tax of EC$11,587.50; employer PAYE deducted EC$10,800. The employee pays the difference of 787.50 by 1 July (s.67(6)).

```oa-check
name: PAYE shortfall
inputs:
  total_tax: 11587.50
  paye: 10800
steps:
  - balance: total_tax - paye
expected:
  balance: 787.50
```

**Example 2 — EC$50,000 management fee to a non-resident affiliate, not withheld.**
Withholding due = 50,000 × 15% = 7,500. Employer failed to withhold: it still owes the amount, plus the greater of 10% (7,500 × 10% = 750) or EC$10 → 750, plus 5% interest on 7,500 = 375. Total employer cost = 50,000 + 7,500 + 750 + 375 = 58,625.00 (interest runs to payment date; example assumes one year).

```oa-check
name: Unwithheld non-resident fee EC$50,000
inputs:
  fee: 50000
steps:
  - wh: fee * 0.15
  - penalty: max(wh * 0.10, 10)
  - interest: wh * 0.05
  - total: fee + wh + penalty + interest
expected:
  total: 58625.00
```

## 8. Ask the client first

1. Is the payee a non-resident — does s.40 withholding apply to this payment type?
2. Has the employee filed a s.68 declaration (affects PAYE calculation)?
3. Current IRD remittance cycle for PAYE (confirm before calendar setup).
4. Are group cost recharges being paid cross-border (15% applies)?

## 9. Sources

- [Income Tax Act, Cap. 18.22](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_22-Income-Tax-Act.pdf) — read 2026-10-22.
- [Tax Administration and Procedures Act, Cap. 20.52](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf) — read 2026-10-22.
