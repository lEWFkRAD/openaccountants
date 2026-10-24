---
name: us-transfer-pricing
description: >
  US federal transfer pricing reference for 2026. Covers IRC §482 and
  the §482 regulations (controlled transactions, specified methods for
  goods, intangibles, services and loans, the best-method rule), the
  §6662(e)/(h) substantial and gross valuation-misstatement penalties
  with the transactional and net-adjustment thresholds, contemporaneous
  documentation, and country-by-country reporting (Form 8975, §6038).
  Trigger on US transfer pricing, §482, arm's length, CPM, CUP, profit
  split, Form 8975, valuation misstatement penalty. Source-cited draft.
jurisdiction: US
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# US transfer pricing (§482)

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the IRS transfer-
pricing page, eCFR 26 CFR §§1.482-1 (framework and best-method rule),
1.482-3 (tangible property), 1.482-4 (intangibles), 1.482-5
(comparable profits method), and 1.6662-6 (penalties), plus the About
Form 8975 page. Statutes: IRC §482, §6662(e)–(h), §6038. Currency:
USD; tax year is the taxable year of the filer.

## 2. Who the rules apply to

- **Controlled taxpayers.** §482 reaches "any two or more persons…
  owned or controlled directly or indirectly by the same interests" —
  the regulations' control presumption is 50% ownership, and control
  can also be de facto (§1.482-1(d)).
- **Both directions:** US inbounds (foreign parent selling into a US
  subsidiary) and US outbounds (US parent licensing to a foreign
  affiliate) are equally in scope.
- **Country-by-country reporting:** US ultimate parent entities of
  MNE groups with $850m+ consolidated revenue file Form 8975 (§6038;
  threshold stated on the Form 8975 page — confirm current indexed
  amount, needs-sources).

## 3. Methods and rules table

| Rule | Content | Source |
|---|---|---|
| Arm's-length standard | The IRS may allocate income/deductions among controlled taxpayers to reflect arm's-length results | IRC §482; 26 CFR 1.482-1 |
| Best-method rule | Select the method providing the most reliable measure given comparability and data quality | 1.482-1(c) |
| Tangible property | CUP, resale price, cost plus, CPM, profit split | 1.482-3(a) |
| Intangibles | CUP, profit split, unspecified methods (CUT method in regulations) | 1.482-4(c) |
| Services | Services cost method, CUP, cost of services plus, CPM, profit split | 1.482-9 (page not re-read this pass — needs-sources for exact list) |
| Loans | Safe-haven interest rates (Applicable Federal Rate ±) | 1.482-2(a) (needs-sources for current bands) |
| Advance pricing agreements | Prospective APA with IRS (and foreign competent authority) | Rev. Proc. 2015-41 (needs-sources) |
| Transactional penalty | 20% of the underpayment for a substantial valuation misstatement (transfer price ≤50% or ≥200% of arm's length); 40% for gross (≤25% or ≥400%) | §6662(e),(h); 1.6662-6 |
| Net-adjustment penalty | 20% if net §482 adjustments exceed $5m or 10% of gross receipts; 40% if over $20m or 20% of gross receipts | §6662(e),(h); 1.6662-6 |
| Contemporaneous documentation | Required to be in existence when the return is filed; penalty relief if reasonably complete | 1.6662-6(d) |
| CbCR | Form 8975 for $850m+ MNE groups | §6038; About Form 8975 |

## 4. Tax base and computation

A §482 adjustment reallocates income between the controlled parties,
changing the US taxable base. Interaction with the 2026 corporate
layer (rates.2026.json): the 21% C-corp rate, the 15% CAMT for AFSI
over $1bn average, BEAT at 12.5% from 2026 (base-erosion payments to
foreign associates are the classic BEAT trigger — see
us-gilti-fdii-beat), and §163(j) 30% ATI limits on related-party
interest.

## 5. Deadlines

- **Documentation:** contemporaneous documentation must exist when the
  US return is filed (1120: 15 April for calendar-year filers; six-
  month extension available).
- **Form 8975 (CbCR):** with the US parent's annual return (Form
  8975 page).
- **APA:** filed before the covered transactions, generally.

## 6. Penalties and interest

The §6662(e)/(h) regime above (20%/40%), with the transactional test
per adjustment and the net-adjustment test per year ($5m/$20m or
10%/20% of gross receipts — 1.6662-6, read 2026-10-24). Adequate
contemporaneous documentation is the main shield. Interest runs on the
underpayment from the original due date.

## 7. Cross-border interaction

Mirror adjustments in the counterparty country require the treaty MAP
article (competent-authority relief); the US competent-authority
function sits with the IRS Advance Pricing & Agreements team. BEAT
(12.5% in 2026) taxes base erosion via deductible payments to foreign
related parties where the ratio test is met — a §482 uplift on inbound
payments can shrink BEAT exposure, and vice versa. See
us-gilti-fdii-beat, us-form-5472-foreign-owned-us.

## 8. Worked examples

**Example 1 — transactional penalty.** The IRS adjusts a US
distributor's transfer price so its profit is understated by $4,000,000
(a substantial valuation misstatement). Underpayment at the 21%
corporate rate = $840,000; transactional penalty at 20% = $168,000.

```oa-check
name: transactional penalty 4m adjustment
inputs:
  adjustment: 4000000
  cit: 0.21
  penalty: 0.20
steps:
  - underpayment: adjustment * cit
  - penalty_amount: underpayment * penalty
expected:
  underpayment: 840000.00
  penalty_amount: 168000.00
```

**Example 2 — gross misstatement, net-adjustment test.** Net §482
adjustments of $25,000,000 (over the $20m net threshold) on gross
receipts of $150,000,000: the net-adjustment penalty applies at 40%.
Underpayment at 21% = $5,250,000; penalty = $2,100,000.

```oa-check
name: net adjustment penalty 25m
inputs:
  adjustment: 25000000
  gross_receipts: 150000000
  cit: 0.21
  penalty: 0.40
steps:
  - underpayment: adjustment * cit
  - penalty_amount: underpayment * penalty
  - over_net_threshold: adjustment - 20000000
  - over_gross_pct: pct(gross_receipts, 20)
expected:
  underpayment: 5250000.00
  penalty_amount: 2100000.00
  over_net_threshold: 5000000.00
  over_gross_pct: 30000000.00
```

## 9. Ask the client first

1. Which controlled transactions ran in the year — goods, services,
   intangibles, loans, cost shares?
2. Does contemporaneous documentation exist as of the filing date?
3. Are inbound payments to foreign associates large enough to trip
   BEAT (12.5% in 2026) or §163(j)?
4. Group revenue near $850m — is a Form 8975 CbCR obligation live,
   and do the CbCR numbers match the US returns?

## 10. Sources

- [IRS — Transfer pricing](https://www.irs.gov/businesses/international-businesses/transfer-pricing) — read 2026-10-24.
- [eCFR 26 CFR 1.482-1](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-D/part-1/section-1.482-1) — read 2026-10-24.
- [eCFR 26 CFR 1.482-3](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-D/part-1/section-1.482-3) — read 2026-10-24.
- [eCFR 26 CFR 1.482-4](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-D/part-1/section-1.482-4) — read 2026-10-24.
- [eCFR 26 CFR 1.482-5](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-D/part-1/section-1.482-5) — read 2026-10-24.
- [eCFR 26 CFR 1.6662-6](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.6662-6) — read 2026-10-24 (20%/40% penalties; $5m/$20m and 10%/20% thresholds).
- [IRS — About Form 8975, Country by Country Report](https://www.irs.gov/forms-pubs/about-form-8975) — read 2026-10-24.
- `packages/us-federal/rates.2026.json` — 2026 corporate layer (BEAT 12.5%, §250 deductions).

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
