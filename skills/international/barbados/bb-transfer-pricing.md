---
name: bb-transfer-pricing
description: >
  Barbados transfer pricing reference for 2026. Covers the arm's-length and
  artificial-transaction rules of the Income Tax Act Cap. 73 (s.29, with the
  related-party unpaid-deduction clawback in the deductions division), the
  absence of a master/local documentation file in the LRO 2007 consolidation,
  country-by-country reporting under the Income Tax (Country-by-Country
  Reporting) Act 2021-27 (USD 850 million threshold), and the Pillar Two
  Corporation Top-Up Tax Act 2024-16 QDMTT (15% ETR, EUR 750 million).
  Trigger on Barbados transfer pricing, associated enterprises, CbCR, GloBE,
  QDMTT. Source-cited draft.
jurisdiction: BB
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Barbados transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 22 October 2026: the full text of the Income
Tax Act, Cap. 73 (L.R.O. 2007 consolidation, PDF from the Barbados Revenue
Authority legislation page), the BRA's Income Tax (Country-by-Country
Reporting) Act 2021-27 summary page, and the BRA's Corporation Top-Up Tax Act
2024-16 summary page. Currency is the Barbados dollar (BBD), pegged at
BBD 2.00 = USD 1.00.

**Source status caveat:** the consolidation on the BRA site is the L.R.O. 2007
text; amendment Acts run to 2025-31 and are posted as separate PDFs that were
not all read in this pass. If a post-2020 amendment introduced a formal
master/local file documentation requirement, it is not reflected here —
**needs-sources** before tier-1 promotion.

## 2. Who the rules apply to

Barbados has no standalone transfer-pricing code. The arm's-length principle
is applied through the Income Tax Act:

- **s.29 (Artificial transactions).** Where a purchase-and-sale transaction
  involving a person carrying on business in Barbados is between parties where
  one controls the other, or the purchaser (or spouse) is a relative of the
  vendor (or spouse), with the effect that the transaction is not at arm's
  length and the price is other than fair market value, the transaction is
  **deemed to have taken place at fair market value** in computing assessable
  income. s.29(2) reaches transactions whose **main purpose is the artificial
  reduction of assessable income**.
- **Related-party deduction clawback.** A deducted amount owing to a person
  in a non-arm's-length transaction (within the meaning of s.29) or to an
  associated/related company is added back if unpaid within **one year** after
  the income year of the deduction (two years for arm's-length/non-associated
  parties).
- **Company residence and source.** Resident companies are taxed on worldwide
  income, non-residents on Barbados-source income (see `bb-cross-border`), so
  cross-border intra-group pricing directly moves the Barbados base.

## 3. Rates and the top-up layer

| Item | Rate / threshold | Source (as_of 2026-10-22) |
|---|---|---|
| General corporation tax | 9% | Income Tax Act Cap. 73; carried from `bb-corporate-income-tax` (PwC, reviewed 11 Jan 2026) |
| QDMTT (Pillar Two) | 15% minimum effective tax rate; MNE groups ≥ EUR 750m consolidated revenue in at least two of the last four fiscal years; applies to fiscal years beginning on or after 31 Dec 2023 | Corporation Top-Up Tax Act 2024-16, BRA legislation page |
| CbCR | MNE groups with consolidated group revenue ≥ USD 850m (≈ BBD 1.72bn) in the previous fiscal year, constituent entities in 2+ jurisdictions; Barbados-resident ultimate parent files | Income Tax (Country-by-Country Reporting) Act 2021-27, in force 31 Dec 2021, BRA page |

## 4. Filings and deadlines

- **CbC report:** filed by the Barbados-resident ultimate parent entity (or a
  surrogate/local constituent where the UPE is not required to file in its
  jurisdiction) — filing window per the Act and BRA guidance notes; confirm
  the current-year deadline on the BRA Tax Calendar before filing
  (needs-sources).
- **No separate TP return** exists in the LRO 2007 consolidation; related-party
  terms are disclosed within the corporation tax return and exposed on audit.
- **Corporation tax prepayments:** monthly 1/12 prepayments from income year
  2025 (see `bb-corporate-income-tax`).

## 5. Penalties and interest

From the Income Tax Act (LRO 2007 text, read 2026-10-22):

- Late/failed return by a company: penalty of **$100**, plus, where the tax
  was unpaid at the time of default, a further penalty of **5% of the tax
  assessed** for that income year.
- Failure to deduct/withhold/pay an amount required by the prepayment and
  withholding sections: **10% of the amount not withheld or $10, whichever is
  greater**.
- s.29 adjustments raise additional tax; interest on unpaid tax follows the
  Act's payment division. Confirm current interest practice with the BRA
  (needs-sources).

## 6. Worked examples

**Example 1 — non-arm's-length sale corrected to FMV.** A Barbados trading
company sells a warehouse to a company it controls for BBD 300,000 when the
fair market value is BBD 450,000. Under s.29 the transaction is deemed to have
taken place at FMV: additional assessable income 450,000 − 300,000 = 150,000;
corporation tax at 9% = 13,500.00 (before penalties/interest).

```oa-check
name: s.29 FMV adjustment BBD 150,000
inputs:
  fmv: 450000
  price: 300000
steps:
  - uplift: fmv - price
  - tax: uplift * 0.09
expected:
  tax: 13500.00
```

**Example 2 — QDMTT top-up on a low-ETR group.** An in-scope MNE group's
Barbados constituent entities have GloBE income of BBD 1,000,000 and Barbados
covered taxes of BBD 90,000 (ETR 9%). The QDMTT tops up to the 15% minimum:
1,000,000 × (15% − 9%) = 60,000.00.

```oa-check
name: QDMTT top-up BBD
inputs:
  income: 1000000
  covered_tax: 90000
steps:
  - etr: covered_tax / income
  - topup: income * 0.15 - covered_tax
expected:
  topup: 60000.00
```

## 7. Ask the client first

1. Is the group an MNE over EUR 750m (QDMTT) or USD 850m (CbCR)?
2. Which intra-group transactions are purchase-and-sale transfers between
  controlling/relative parties (s.29 reach) versus service fees?
3. Are related-party payables outstanding beyond one year (deduction clawback)?
4. What is the Barbados ETR once the 9% rate and any incentives are applied —
  is a QDMTT top-up due?

## 8. Sources

- [Income Tax Act, Cap. 73 (full text PDF, L.R.O. 2007)](https://bra.gov.bb/attachment?file=Attachments%2fIncome+Tax+Act%2c+Cap.+73.pdf&name=Income+Tax+Act%2c+Cap.+73) — s.29, deductions clawback, penalties division; read 2026-10-22.
- [Income Tax (Country-by-Country Reporting) Act, 2021-27](https://bra.gov.bb/About/Legislation-Regulations/Income-Tax-Country-by-Country-Repo) — read 2026-10-22.
- [Corporation Top-Up Tax Act, 2024-16](https://bra.gov.bb/About/Legislation-Regulations/Corporation-Top-up-Tax-Act-2024-16) — read 2026-10-22.
- [BRA Legislation & Regulations index](https://bra.gov.bb/About/Legislation-Regulations) — read 2026-10-22.

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
