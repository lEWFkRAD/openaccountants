---
name: kn-transfer-pricing
description: >
  Saint Kitts and Nevis transfer pricing reference for 2026. Covers the
  Comptroller's arm's-length reallocation power over related/associated
  persons (Income Tax Act s.5), the associated-company control tests,
  re-characterisation and substance powers, branch allocation, and the 15%
  non-resident withholding that captures group charges. No statutory
  documentation regime exists. Uses the official Law Commission
  consolidation of the Income Tax Act (Cap. 18.22); source-cited draft.
jurisdiction: KN
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Saint Kitts and Nevis transfer pricing

## 1. Scope and sources

Source-cited draft checked 22 October 2026 from the Income Tax Act, Cap. 18.22 (consolidation, revision date 31 December 2017), read in full from the Law Commission site. Amounts are East Caribbean dollars.

## 2. The rule

Section 5(1): in any arrangement, transaction or group of transactions between **related or associated persons**, the Comptroller may by notice —

- (a) distribute, apportion or allocate amounts of income and deductions **as necessary to reflect the chargeable income or tax that would have arisen at arm's length**;
- (b) **re-characterise** the source and type of income or payment where the form does not reflect the substance, or where the arrangement is an avoidance arrangement;
- (c) **disregard** arrangements without substantial economic effect or classified as avoidance arrangements.

There is **no statutory transfer-pricing documentation regime** (no master file / local file obligation) and no statutory penalty specific to transfer pricing — adjustments flow through assessments with the general interest and penalty regime (TAP Act ss.22, 37–38).

## 3. Who is associated

Section 5(2): two companies are associated in a tax year if at any time in the year one controls the other; both are controlled by the same person or group; control sits with related persons each owning at least 25% of any class of shares; or related groups control each with overlapping members owning at least 25%. Control is direct or indirect "in any manner" — de facto control counts.

Branch/head-office allocation: where branch activities cannot be accounted for separately, the Comptroller may allocate between them on arm's-length lines (s.5 as applied to branches; see the branch-allocation provision in Part II).

## 4. Practical base

- The scheduled DTA Orders (Canada, UK, USA, etc.) carry OECD-style associated-enterprise articles; treaty-based adjustments can run in parallel with s.5 (verify which Orders are in force).
- Every cross-border group charge (management fees, service fees, recharges, interest) also triggers **15% withholding under s.40** — see `kn-payroll-withholding`. Under-pricing a charge does not avoid withholding; the withholding base is the gross amount paid.

## 5. Deadlines and procedure

No annual filing. Adjustments arise on audit/assessment: assessed tax is due within one month of the notice (s.66); interest runs at 12% per annum from the original due date (TAP Act s.22(4)); the 25% underpayment penalty applies where the pricing position was negligent or intentional (TAP Act s.38).

## 6. Cross-border points

- Thin-capitalisation: no statutory thin-cap rule; excessive interest is policed through s.5 re-characterisation.
- Repatriation of an adjustment: the corresponding foreign-side relief depends on the counterparty's domestic law and any in-force DTA Order.

## 7. Worked examples

**Example 1 — under-priced management service.** A KN distributor pays an affiliate for services that arm's-length comparables price at EC$200,000; the invoice charged EC$140,000. The Comptroller reallocates the difference: adjustment 60,000, additional company tax 60,000 × 33% = 19,800.00 (before interest).

```oa-check
name: Under-priced service adjustment
inputs:
  arm_length: 200000
  charged: 140000
steps:
  - adjustment: arm_length - charged
  - tax: adjustment * 0.33
expected:
  tax: 19800.00
```

**Example 2 — off-market intra-group loan.** A KN borrower pays 12% on an EC$2,000,000 note; the arm's-length rate is 7%. Disallowed interest = 2,000,000 × (12% − 7%) = 100,000; additional KN tax = 100,000 × 33% = 33,000.00. The lender's receipt also bore 15% s.40 withholding on the gross interest.

```oa-check
name: Off-market loan EC$2,000,000
inputs:
  principal: 2000000
steps:
  - disallowed: principal * (0.12 - 0.07)
  - tax: disallowed * 0.33
expected:
  tax: 33000.00
```

## 8. Ask the client first

1. Which entities are associated under the s.5(2) control tests (including de facto control)?
2. What comparables support the pricing of each cross-border charge?
3. Was 15% s.40 withholding applied to every non-resident group charge?
4. Is the counterparty in a territory with an in-force DTA Order?

## 9. Sources

- [Income Tax Act, Cap. 18.22, s.5 and scheduled DTA Orders](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_22-Income-Tax-Act.pdf) — read 2026-10-22.
- [Tax Administration and Procedures Act, Cap. 20.52](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf) — read 2026-10-22.
