---
name: ms-transfer-pricing
description: >
  Montserrat transfer pricing reference for 2026. There is no dedicated
  transfer-pricing chapter or documentation regime; the arm's-length
  principle is enforced through the Tax Administration Act (Cap. 17.26,
  1 Jan 2025 revision) anti-avoidance section 35, which empowers the
  Comptroller to adjust related-person transactions to arm's-length
  terms and to disregard artificial or mischaracterised schemes, plus
  the Income and Corporation Tax Act non-arm's-length transferee and
  associated-person rules. Covers the adjustment power, interest and
  penalties, and practical documentation posture. Trigger on Montserrat
  transfer pricing, arm's length, related persons, associated persons,
  anti-avoidance, Comptroller adjustment. Source-cited draft.
jurisdiction: MS
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-23
version: 0.1
---

# Montserrat transfer pricing

## 1. Who this applies to

- Companies and bodies filing Montserrat income tax (30% company rate under the Income and Corporation Tax Act Cap. 17.01 s.36) that transact with related persons — parent/subsidiary, common-control groups, director-linked entities.
- Branches and non-resident persons carrying on business in Montserrat.
- There is no statutory documentation obligation (no local file, master file or CbCR filing duty in the revenue laws read this pass), but the Comptroller's adjustment power makes contemporaneous pricing support essential in audit.

## 2. Rates and thresholds

No TP-specific rate or threshold table exists. The relevant money consequence is the underlying tax rate plus statutory interest:

| Item | Amount | Source |
|---|---|---|
| Company income tax rate | 30% of chargeable income | Cap. 17.01 s.36 |
| Interest on underpayment from TP adjustment | 6% simple per annum | Cap. 17.26 ss.56–57 |
| Late-payment fee | 5% of unpaid tax | Cap. 17.26 s.59 |

## 3. The base: the arm's-length adjustment power

Tax Administration Act (Cap. 17.26) section 35 "Anti-avoidance" (read 2026-10-23):

- s.35(1): the Comptroller may **disregard artificial or fictitious transactions or series of transactions**, or treat a mischaracterised transaction according to its **economic substance**.
- s.35(2): in making an assessment the Comptroller may **adjust transactions between related persons to the terms that would have obtained between unrelated persons at arm's length**.
- s.35(3): scheme-based counteraction where a tax benefit arises from a misuse or abuse of a revenue law.

Supporting rules in the Income and Corporation Tax Act (Cap. 17.01): the interest-deduction provisions require the borrowed-capital test (s.13), and s.70 makes a person who received the taxpayer's assets in a **non-arm's-length transaction within one year** before a levy secondarily liable to the extent of the asset value received.

There is no statutory list of OECD-style methods; in practice the Comptroller's "arm's length" standard is applied by comparison to independent pricing, and OECD methods are persuasive rather than enacted.

## 4. Deadlines and mechanics

- Adjustments arise through assessment (Cap. 17.26 Part 4); the Comptroller may issue an assessment where a return is not filed (s.30(3)).
- Objection and appeal rights sit in Part 5 of Cap. 17.26 with stated time limits in the notice of assessment.
- Collection proceedings must start within six years of default (s.61).

## 5. Penalties and interest

- Interest: 6% simple per annum on the shortfall from the original due date of the tax to payment (ss.56–57); variable by Governor's Order.
- Late filing penalty: greater of 5% + 1%/month of tax owing, or $500 + $100/month, capped $100/$1,000/$10,000 (s.58).
- Late payment fee: 5% (s.59).
- Recovery toolkit: tax lien on all property from the due date (s.64), third-party debtor notices (s.68), non-arm's-length transferee liability (Cap. 17.01 s.70).

## 6. Cross-border notes

- Montserrat has no treaty network of its own for income tax; relief claims against UK-administered frameworks need separate analysis (needs-sources: no official treaty list published on gov.ms this pass).
- Remitted branch profits are treated as a separate withholding issue (see ms-nonresident-withholding).
- No CbCR or exchange-of-information statute was located in the Acts read this pass; international tax cooperation obligations flow from UK arrangements — flag as needs-sources.

## 7. Worked examples

**Example 1 — related-party service fee adjustment.** A Montserrat company (tax rate 30%) pays its offshore affiliate XCD 500,000 for management services the Comptroller prices at XCD 350,000 arm's length. The adjustment increases chargeable income by XCD 150,000; interest runs 2 years at 6% simple.

```oa-check
name: TP adjustment tax and interest
inputs:
  paid: 500000
  arm_length: 350000
  rate: 0.30
  interest_rate: 0.06
  years: 2
steps:
  - uplift: paid - arm_length
  - extra_tax: uplift * rate
  - interest: extra_tax * interest_rate * years
  - total: extra_tax + interest
expected:
  uplift: 150000
  extra_tax: 45000
  interest: 5400
  total: 50400
```

**Example 2 — secondary liability of a transferee.** A taxpayer owing XCD 80,000 transfers a property worth XCD 60,000 to a connected entity for XCD 10,000 within the year before levy. The transferee's secondary liability is capped at the value of the assets received.

```oa-check
name: non-arm's-length transferee cap
inputs:
  asset_value: 60000
  price_paid: 10000
  tax_owed: 80000
steps:
  - secondary_liability: min(asset_value, tax_owed)
expected:
  secondary_liability: 60000
```

## 8. Ask the client

- Full related-party transaction inventory (services, loans, IP, management fees, property) with amounts and counterparties.
- Contemporaneous pricing support: quotes, benchmarks, board minutes showing commercial rationale.
- Loan purpose documentation (Cap. 17.01 s.13 interest test).
- Whether any asset transfers occurred in the year before an assessment or levy (s.70 exposure).

## 9. Sources

- [Tax Administration Act, Cap. 17.26 (1 Jan 2025 revision)](https://legislation.gov.ms/wp-content/uploads/2026-02-17.26-Tax-Administration-Act.pdf) — s.35 anti-avoidance, Part 7 interest/penalties; read 2026-10-23.
- [Income and Corporation Tax Act, Cap. 17.01 (1 Jan 2025 revision)](https://legislation.gov.ms/wp-content/uploads/2026-02-17.01-Income-and-Incorporation-Tax-Act.pdf) — s.36 rate, s.13 deductions, s.70 non-arm's-length transferees; read 2026-10-23.
- [MCRS inland revenue page](https://mcrs.ms/inland-revenue/) — read 2026-10-23 (no TP guidance published).

**Source status caveat:** no Montserrat TP guidance note, treaty list, or CbCR statute resolved from official pages on 2026-10-23; those points are marked needs-sources above.

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
