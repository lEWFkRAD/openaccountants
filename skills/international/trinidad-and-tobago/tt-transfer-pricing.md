---
name: tt-transfer-pricing
description: >
  Trinidad and Tobago transfer pricing reference for 2026. Covers the
  associated-person arm's-length rules inside the Income Tax Act
  (Chap. 75:01), the 30%/35% corporation tax rates the adjustments feed,
  the 0.6% Business Levy and 0.3% Green Fund Levy gross-receipt
  overlays, withholding rates on cross-border associate payments, and
  the IRD Mutual Agreement Procedure route under the fifteen listed
  treaties. Trigger on Trinidad and Tobago transfer pricing, arm's
  length, associated persons, IRD revaluation. Source-cited draft.
jurisdiction: TT
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Trinidad and Tobago transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the Inland Revenue
Division (IRD) home, legislation, withholding-tax, double-taxation-
treaties and MAP-guidelines pages; the Ministry of Finance income-tax
services page; and the existing TT pack skills (figures carried forward
with their citations). Currency is the Trinidad and Tobago dollar
(TTD).

**Source status caveat:** the consolidated Income Tax Act (Chap. 75:01)
text in the Digital Legislative Library (laws.gov.tt) was not
machine-readable this pass, and the IRD publishes no standalone
transfer-pricing guide. The section numbers of the associated-person /
revaluation provisions and any statutory documentation deadline are
therefore **needs-sources** — confirm against the Act before tier-1
promotion.

## 2. Who the rules apply to

- **Transactions between associated persons.** The Income Tax Act
  (Chap. 75:01) contains associated-person provisions allowing the
  Board of Inland Revenue to recompute income where a transaction
  between associated persons is not at arm's length and reduces a TT
  tax base. Section numbers: **needs-sources.**
- **Cross-border payments to non-resident associates** additionally run
  through the withholding regime (dividends 10%, interest 10%/8%,
  royalties 15% non-treaty — see tt-corporate-income-tax); the charges
  stack.
- **No published standalone TP documentation code** (no local-file /
  master-file / CbCR triplet confirmed) — the IRD requests records
  through its audit powers. **needs-sources.**

## 3. The rules (revaluation table)

| Rule | Content | Source |
|---|---|---|
| Arm's-length revaluation | The Board may recompute where an associated-person transaction departs from arm's length and understates the TT base | Income Tax Act (Chap. 75:01), associated-person provisions (sections needs-sources) |
| Standard corporation tax rate | 30% of chargeable profits | Corporation Tax Act (Chap. 75:02) — tt-corporate-income-tax |
| Banks / petrochemicals rate | 35% | Corporation Tax Act (Chap. 75:02) — tt-corporate-income-tax |
| Petroleum production | 50% standard; 30% deep-sea | Petroleum Taxes Act (Chap. 75:04) — tt-corporate-income-tax |
| Business Levy overlay | 0.6% of gross revenue/receipts (exempt below TTD 360,000), payable where it exceeds the corporation tax liability | Corporation Tax Act (Chap. 75:02) — tt-corporate-income-tax |
| Green Fund Levy overlay | 0.3% of gross income, non-deductible, quarterly | Miscellaneous Taxes Act (Chap. 77:01) — tt-corporate-income-tax |
| WHT overlay | Dividends 10%; interest 10% (individuals) / 8% (companies); royalties 15% — non-treaty, reduced or 0% under treaties | Income Tax Act (Chap. 75:01) — tt-corporate-income-tax |
| Documentation | No standalone statutory TP-file regime confirmed; records on request | needs-sources |

## 4. Tax base and computation

A revaluation feeds chargeable profits for the Corporation Tax Act
computation. Two gross-receipt overlays matter on an uplift: the
Business Levy (0.6% of gross revenue) and the Green Fund Levy (0.3% of
gross income) both key on **gross** amounts, so an arm's-length uplift
that raises TT gross receipts raises the levies even where the
corporation-tax margin effect is small. Compute all three charges on
any adjustment.

## 5. Deadlines

- **Corporation tax return:** 30 April following the end of the income
  year; quarterly instalments 31 March / 30 June / 30 September /
  31 December (see tt-corporate-income-tax).
- **PAYE / WHT remittance:** by the 15th of the following month (see
  tt-payroll-social).
- **TP documentation:** no statutory preparation deadline confirmed —
  **needs-sources**.

## 6. Penalties and interest

Assessment and collection run through the Income Tax Act / Corporation
Tax Act: the Board may assess under-declared amounts with penalties and
interest on late or incorrect returns (section-level amounts
**needs-sources**). Treaty-based disputes go to the IRD's published MAP
guidelines page.

## 7. Cross-border interaction

TT's treaty network is real and listed by the IRD (fifteen instruments
including the USA 1971, UK 1983, CARICOM 1994, China 2004, Spain 2009 —
see tt-cross-border). A revaluation of a cross-border associate payment
can be challenged through MAP under the treaty's associated-articles;
the IRD publishes MAP guidelines. Intra-CARICOM dividends are 0% under
the CARICOM treaty (see tt-corporate-income-tax).

## 8. Worked examples

**Example 1 — service fee undercharge by a TT associate.** A TT company
provides back-office services to its foreign parent for TTD 400,000
when the arm's-length fee is TTD 1,200,000. The Board recomputes TT
profits up by TTD 800,000; additional corporation tax at the 30%
standard rate = TTD 240,000.

```oa-check
name: service fee uplift TTD 800k
inputs:
  arm_length: 1200000
  price: 400000
  cit_rate: 30
steps:
  - uplift: arm_length - price
  - cit: uplift * pct(1, cit_rate)
expected:
  cit: 240000.00
```

**Example 2 — royalty overcharge, stacked charges.** A TT licensee pays
its foreign associate a TTD 1,000,000 royalty; the Board accepts TTD
500,000 as arm's length. The TTD 500,000 excess is disallowed for
corporation tax (30% = TTD 150,000 more tax), and the 15% non-treaty
royalty WHT already borne on the gross royalty (TTD 150,000) is
separate and final.

```oa-check
name: royalty disallowance TTD 500k
inputs:
  royalty_paid: 1000000
  arm_length: 500000
  cit_rate: 30
  wht_rate: 15
steps:
  - disallowed: royalty_paid - arm_length
  - extra_cit: disallowed * pct(1, cit_rate)
  - wht_on_gross: royalty_paid * pct(1, wht_rate)
expected:
  extra_cit: 150000.00
  wht_on_gross: 150000.00
```

## 9. Ask the client first

1. Which transactions crossed borders with associated persons in the
   year — goods, services, royalties, management fees, loans?
2. Are both sides of each transaction recorded at the same price in
   both countries?
3. Was withholding filed and remitted by the 15th on every cross-
   border associate payment, at the correct treaty or non-treaty rate?
4. Has the Business Levy and Green Fund Levy exposure been recomputed
   on gross receipts after any uplift?

## 10. Sources

- [Inland Revenue Division — home](https://www.ird.gov.tt/) — read 2026-10-24.
- [IRD — Legislation and Tax Laws](https://www.ird.gov.tt/law-policy/legislation) — read 2026-10-24.
- [IRD — Withholding Tax](https://www.ird.gov.tt/withholding-tax) — read 2026-10-24.
- [IRD — Double Taxation Treaties](https://www.ird.gov.tt/law-policy/double-taxation-treaties) — read 2026-10-24.
- [IRD — Guidelines for Mutual Agreement Procedure](https://www.ird.gov.tt/law-policy/map-guidelines) — read 2026-10-24.
- [Ministry of Finance — Income Tax services](https://www.finance.gov.tt/services/income-tax/) — read 2026-10-24.
- Existing pack skill `tt-corporate-income-tax` — Corporation Tax Act, Petroleum Taxes Act, levy and withholding figures carried forward with their PwC citations pending statute-level confirmation.

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
