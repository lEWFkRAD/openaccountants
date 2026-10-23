---
name: bz-transfer-pricing
description: >
  Belize transfer pricing reference for 2026. Covers the absence of a
  general transfer-pricing code in the Income and Business Tax Act (Cap.
  55) — business tax is charged on gross receipts, which limits
  profit-shifting — the statutory arm's-length deeming rules for petroleum
  operations contractors (Cap. 55 Part IV, ss.101–102), the 3% withholding
  tax on gross contract payments (s.112, regularized by the Income and
  Business Tax (Amendment) Act 2024), and the Belize Tax Service AEOI/BEPS
  framework. Trigger on Belize transfer pricing, arm's length, petroleum
  operations, gross contract payments, CbCR, AEOI. Source-cited draft.
jurisdiction: BZ
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Belize transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the full text of the
Income and Business Tax Act, Cap. 55 (Revised Edition 2011 PDF published by
the Belize Tax Service) and the Income and Business Tax (Amendment) Act,
2024 (Act No. 40 of 2024, gazetted 14 December 2024, BTS PDF), plus the BTS
Business & Income Tax resources pages. Currency is the Belize dollar (BZD),
pegged at BZD 2.00 = USD 1.00.

**Source status caveat:** the BTS statute library posts the 2011 revision
plus amendment Acts as separate PDFs; intermediate consolidations (Revised
Edition 2020 is referenced by the 2024 Act) were not all read. Country-
by-country reporting: Belize appears in BTS "AEOI & BEPS" resources, but no
CbCR regulation text was read in this pass — **needs-sources** before
asserting a CbCR threshold or deadline. No Pillar Two / minimum-tax
legislation was found on the BTS site — treat as not enacted as of the read
date, and re-verify.

## 2. Who the rules apply to

- **No general TP code.** Cap. 55 contains no general arm's-length or
  associated-enterprises rule for ordinary companies. The structural
  reason: most business tax is charged on **gross receipts** (rates by
  activity — see bz-corporate-income-tax), so intra-group pricing cannot
  shift taxable profit the way it does under net-basis regimes.
- **Petroleum operations contractors.** Part IV (petroleum agreements)
  carries express arm's-length rules: s.101 values petroleum sold to third
  parties at the net realised price at the Delivery Point, and crude oil
  sold to other than third parties by the weighted-average unit price of
  third-party sales in the preceding 90 days (adjusted for quality, grade
  and gravity), with "third party sales" defined as arm's-length sales to
  purchasers that are not affiliated companies of the Contractor
  (s.101(4)); and s.102(4) deems **all transactions giving rise to
  revenues, costs or expenses** to have been conducted at arm's length (or
  on a basis assuring third-party competitive results) for tax purposes
  unless the Government agrees otherwise in writing.
- **Contract-payment withholding** (s.112) applies to self-employed
  persons, professionals and entities paid under contracts — see §5.

## 3. Rates and key parameters

| Item | Value | Source |
|---|---|---|
| General transfer-pricing code | None (gross-receipts business tax) | Cap. 55 structure; read 2026-10-23 |
| Petroleum arm's-length deeming | All revenue/cost/expense transactions deemed arm's length unless Government agrees otherwise | Cap. 55, s.102(4) |
| Petroleum third-party sales pricing | Market-referenced; affiliated-company sales excluded from "third party sales" | Cap. 55, s.101(4) |
| Withholding on gross contract payments | 3% of the gross contract price, creditable against the contractor's tax; not applied where the payment is under BZD 3,000 | Cap. 55, s.112 |
| 2024 amendment effect on withholding | "Regularize" withholding of tax on gross contract payments | Amendment Act 2024, long title |
| CbCR / Pillar Two | needs-sources (AEOI & BEPS resources exist; no text read) | BTS resources |

## 4. Tax base and computation

For in-scope petroleum operations, taxable income is a net computation
(petroleum income tax 25% of net income — see bz-corporate-income-tax),
and the arm's-length deeming in s.102(4) is the transfer-pricing control:
revenues, costs and expenses are recomputed to third-party competitive
levels. For everyone else, the gross-receipts base makes mispricing of
intra-group charges largely tax-neutral on the Belize side — but the
counterparty jurisdiction's own TP rules still apply to the same flows.

## 5. Withholding on contract payments (s.112)

- 3% levied on **gross contract payments** (total contract price without
  deduction) to self-employed persons, professionals or entities under
  contracts for works, services, labour or materials (plus Gazette-
  prescribed categories).
- Operates as a **credit** against the contractor's tax.
- Payments under BZD 3,000 are outside the section.
- Every payer is obliged to withhold and remit.

## 6. Deadlines

- Business tax returns and income tax filing: see bz-corporate-income-tax
  and bz-income-tax (annual income tax return 31 March; business tax
  monthly/quarterly per BTS guidance).
- Withheld contract tax: every payer must render an account and remit the
  deducted amount **within fifteen days following the end of every month**
  (s.112(5)); failure to deduct or account makes the amount a debt owing
  to the Government, recoverable with a penalty of BZD 100 or 10% of the
  tax due, whichever is greater (s.112(5)).

## 7. Penalties and interest

Cap. 55 penalties: penalty for evasion (s.116), general penalty (s.118),
and arrears recovery against purchasers of businesses (s.117). Interest
provisions for late payment follow the collection division (Part VI).
Exact current rates are set in the Act's penalty sections — confirm
against the BTS guides before quoting amounts.

## 8. Worked examples

**Example 1 — petroleum arm's-length recomputation.** A petroleum
contractor books drilling services from an affiliate at USD 8,000,000 when
the third-party competitive price is USD 6,500,000. Under s.102(4) the
deductible cost is deemed at arm's length: disallowed excess USD 1,500,000;
at the 25% petroleum income tax rate the adjustment raises tax by USD
375,000.

```oa-check
name: petroleum arm's length cost uplift USD
inputs:
  affiliate_cost: 8000000
  arm_length: 6500000
steps:
  - disallowed: affiliate_cost - arm_length
  - tax_uplift: disallowed * 0.25
expected:
  tax_uplift: 375000.00
```

**Example 2 — contract-payment withholding.** A company pays a Belize
consultancy a gross contract price of BZD 200,000. Withholding = 3% = BZD
6,000, creditable against the consultancy's tax; the payment exceeds the
BZD 3,000 floor so s.112 applies.

```oa-check
name: s.112 contract withholding BZD
inputs:
  contract_price: 200000
steps:
  - wht: contract_price * 0.03
  - net: contract_price - wht
expected:
  wht: 6000.00
  net: 194000.00
```

## 9. Ask the client first

1. Is the client a petroleum-operations contractor (Part IV arm's-length
   rules bite) or an ordinary business (gross-receipts base)?
2. Are there gross contract payments being made — is 3% withholding being
   applied and credited correctly?
3. What does the counterparty jurisdiction's TP regime require for the
   same intra-group flows?
4. Any CbCR or substance filings expected by BTS under AEOI/BEPS?

## 10. Sources

- [Income and Business Tax Act, Cap. 55 (full text PDF, BTS)](https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf) — ss.101–102 (petroleum arm's length), s.112 (contract withholding), Part VI penalties; read 2026-10-23.
- [Income and Business Tax (Amendment) Act, 2024 (Act No. 40 of 2024, PDF, BTS)](https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf) — long title (withholding regularization, treaty relief extension); read 2026-10-23.
- [BTS — Business & Income Tax ACTs list](https://bts.gov.bz/tax_resources/category/business-and-income-tax?type=ACT) — read 2026-10-23.
- [BTS — AEOI & BEPS resources](https://bts.gov.bz/tax_resources/category/aeoi-and-beps) — read 2026-10-23 (contents needs-sources).

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
