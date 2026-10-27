---
name: aw-transfer-pricing
description: >-
  Use for Aruba transfer pricing and cross-border profit allocation:
  arm's-length expectations for related-party dealings with the 22%
  winstbelasting backdrop, the 15% nominal-tax recipient condition on
  related-party interest, the DGA excessive-debt deemed dividend, BEPS
  infrastructure at DIMP (CbC reporting, Mutual Agreement Procedure),
  and adjustment worked examples. Trigger on Aruba transfer pricing,
  Aruba related party, Aruba CbC, winstbelasting arm's length.
  Source-cited draft; DIMP BEPS pages verified 2026-10-27; statutory
  arm's-length article needs-sources.
jurisdiction: AW
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-27
version: 0.1
---

# Aruba transfer pricing

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status (2026-10-27):** DIMP pages verified HTTP 200 with real content: <https://www.impuesto.aw/beps> (BEPS hub: CbC, MAP) and <https://www.impuesto.aw/internationaal> (BEPS/CbC/MAP/CRS structure), plus <https://www.impuesto.aw/belastingplan_2023> (15% nominal-tax recipient rule on interest, DGA deemed-dividend rule, 22% rate). **needs-sources:** the statutory arm's-length article of the Landsverordening winstbelasting (Aruba's codified TP rules are limited; the arm's-length principle is applied through profit-determination case law and DIMP practice), CbC threshold/local-filing mechanics, and the treaty network position (Kingdom treaties generally apply to the European part only — confirm per treaty).

## 1. Who this applies to

- **Aruba winstbelasting subjects trading with related parties** — cross-border and domestic groups, holding/financing structures, management-fee and service arrangements.
- **Financing arms:** interest deductions run into the 15% nominal-tax recipient condition (see §2).
- **Multinationals with Aruba entities:** BEPS tools at DIMP — Country-by-Country Reporting and the Mutual Agreement Procedure (DIMP internationaal page, verified 2026-10-27).
- **DGAs** with excessive private debt to their company — deemed-dividend rule (see §6).

## 2. Rates and key rules

| Item | Value | Source |
|---|---|---|
| Corporate rate backdrop | 22% winstbelasting | DIMP belastingplan_2023, verified 2026-10-27 |
| Related-party interest deduction | Recipient must be subject to **nominal tax ≥15%** | DIMP belastingplan_2023, verified 2026-10-27 |
| DGA excessive private debt | > Afl. 500,000 → fictitious dividend | DIMP belastingplan_2023, verified 2026-10-27 |
| Statutory arm's-length article | **needs-sources** (codification limited; principle applied in profit determination) | — |
| CbC reporting | Exists at DIMP (BEPS hub) | DIMP /beps, verified 2026-10-27 |
| MAP | Available at DIMP | DIMP /beps, verified 2026-10-27 |

## 3. Base and mechanics

- **Profit determination:** winstbelasting taxes the whole profits of the company; DIMP re-allocates profits where related-party pricing shifts profit out of Aruba. Document pricing against comparables (CUP, cost-plus, TNMM) even though Aruba's codified TP chapter is thin (**needs-sources**).
- **Interest anti-abuse:** before deducting related-party interest, confirm the recipient's nominal tax position ≥15% — a zero/low-tax holding company breaks the deduction (DIMP belastingplan_2023, verified 2026-10-27).
- **Service fees and royalties:** no withholding-tax gate was verified for royalties this run (**needs-sources**); the profit-determination test still applies.

## 4. Deadlines and filings

- TP documentation rides with the corporate return; no separate Aruba TP filing was verified (**needs-sources**).
- CbC notification/filing calendar: **needs-sources** (DIMP /beps hub verified; mechanics page not resolved this run).

## 5. Penalties and interest

- Re-allocation assessments carry the standard winstbelasting machinery; surcharge/interest percentages **needs-sources**.
- Objection window on a self-assessed dividendbelasting return is 2 months from payment (DIMP dividendbelasting-home, verified 2026-10-27) — indicative of DIMP's general objection posture.

## 6. Cross-border notes

- **Treaty coverage:** Kingdom of the Netherlands treaties do not automatically extend to Aruba — check each treaty's territorial clause before relying on treaty rates or MAP (**needs-sources**).
- **DGA deemed dividend:** private debt above Afl. 500,000 becomes a fictitious distribution; prior deemed amounts uprate the threshold; pre-2023 loans had a transition to 31 Dec 2024 (DIMP belastingplan_2023, verified 2026-10-27).
- **CRS:** Aruba participates in the Common Reporting Standard (DIMP internationaal page, verified 2026-10-27) — account data flows to DIMP/foreign authorities.

## 7. Worked examples

**Example 1 — sales price re-allocation.** An Aruba distributor sells to its foreign parent at Afl. 1,000,000 for goods whose arm's-length price is Afl. 800,000 (CUP evidence). DIMP re-allocates the Afl. 200,000 excess profit to Aruba at 22%.

```oa-check
name: aw tp sales adjustment
inputs:
  charged: 1000000
  arm_len: 800000
  rate: 0.22
steps:
  - adjustment: charged - arm_len
  - extra_tax: rate * adjustment
expected:
  adjustment: 200000.00
  extra_tax: 44000.00
```

**Example 2 — cost-plus service fee.** An Aruba service centre incurs Afl. 200,000 and charges its foreign affiliate Afl. 190,000 (below cost). The arm's-length cost-plus margin is 7% → price Afl. 214,000.

```oa-check
name: aw tp cost plus service
inputs:
  cost: 200000
  charged: 190000
  margin: 0.07
  rate: 0.22
steps:
  - arm_len_price: cost * (1 + margin)
  - adjustment: arm_len_price - charged
  - extra_tax: rate * adjustment
expected:
  arm_len_price: 214000.00
  adjustment: 24000.00
  extra_tax: 5280.00
```

## 8. Ask the client first

1. What related-party flows cross the Aruba border — goods, services, financing, royalties, IP?
2. Who is the counterparty and what nominal tax does it face (the 15% interest condition)?
3. Is there contemporaneous pricing evidence (comparables) for each flow?
4. Is the group CbC-relevant — does an Aruba entity file or notify?
5. Is a DGA privately indebted to the company above Afl. 500,000?

## 9. Sources

- DIMP — BEPS hub (CbC, MAP): <https://www.impuesto.aw/beps> — verified 200 with text 2026-10-27.
- DIMP — Internationaal (BEPS/CbC/MAP/CRS): <https://www.impuesto.aw/internationaal> — verified 200 with text 2026-10-27.
- DIMP — Belastingplan 2023 (15% recipient rule, DGA debt rule, 22% rate): <https://www.impuesto.aw/belastingplan_2023> — verified 200 with text 2026-10-27.
- DIMP — Dividendbelasting (2-month objection term): <https://www.impuesto.aw/dividendbelasting-home> — verified 200 with text 2026-10-27.
- Landsverordening winstbelasting — statutory arm's-length basis **needs-sources** this run.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
