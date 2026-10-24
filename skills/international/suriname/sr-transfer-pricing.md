---
name: sr-transfer-pricing
description: >
  Suriname transfer pricing reference for 2026. Covers the absence of a
  published standalone transfer-pricing code, the arm's-length revaluation
  route through the Income Tax Act 1922 (Inkomstenbelasting 1922) general
  provisions, the 36% corporate rate the adjustments feed, dividend
  withholding interaction under the Dividendbelasting, and the narrow
  treaty network (Netherlands, Curaçao). Trigger on Suriname transfer
  pricing, arm's length, associated enterprises, related party, SRD
  revaluation. Source-cited draft.
jurisdiction: SR
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Suriname transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026. **Source status
caveat:** the Surinamese tax administration portal
(belastingkantoor.sr) and statute portal (surinamewetten.sr) did not
resolve from this drafting environment — only gov.sr and the Ministry of
Finance and Planning pages under it did. Every statute-level section
reference below is therefore **needs-sources**: the rules are stated at
the level the earlier source-cited drafts (sr-income-tax,
sr-corporate-income-tax) support, and no figure here is invented.
Confirm against the Income Tax Act 1922 (Inkomstenbelasting 1922) and
current DRIOT/Ministry practice before tier-1 promotion. Currency is the
Surinamese dollar (SRD).

## 2. Who the rules apply to

- **Transactions between related parties.** Suriname has no published
  standalone transfer-pricing regulations (no local-file / master-file /
  country-by-country triplet confirmed). The arm's-length principle is
  applied through the general provisions of the Income Tax Act 1922:
  the tax administration may disregard amounts that do not reflect
  arm's-length dealing between related parties and recompute the
  Suriname tax base. Section numbers: **needs-sources.**
- **Cross-border payments to foreign associates** (interest, royalties,
  management fees, rent) are additionally screened through the
  withholding and deduction-allowance rules in sr-corporate-income-tax;
  note the existing draft records **no general domestic withholding on
  interest or royalties** (approx — confirm), so the primary Suriname
  charge on a mispriced inbound payment is the corporate-income-tax
  disallowance, not WHT.
- **Dividends** to a foreign parent run through the separate Dividend
  Withholding Tax Act (Dividendbelasting) — see sr-cross-border.

## 3. The rules (revaluation table)

| Rule | Content | Source |
|---|---|---|
| Arm's-length revaluation | The administration may recompute profits where a related-party transaction understates the Suriname base; no standalone TP code | Income Tax Act 1922, general provisions (sections needs-sources) |
| Corporate rate the adjustment feeds | 36% flat on net taxable profit (resident companies, worldwide base) | Income Tax Act 1922 — see sr-corporate-income-tax |
| Interest / royalty WHT | No general domestic withholding confirmed (approx — confirm) | Income Tax Act 1922 — see sr-corporate-income-tax |
| Dividend WHT overlay | 25% domestic; treaty reductions (NL 7.5%; Curaçao 5%/10%) | Dividendbelasting + treaties — see sr-cross-border |
| Documentation | No statutory TP-file regime confirmed; records on request under assessment powers | needs-sources |
| Loss carryforward the adjustment can absorb | 7 years generally; indefinite for losses of the first 3 years of operation | Income Tax Act 1922 — see sr-corporate-income-tax |

## 4. Tax base and computation

A revaluation feeds the 36% corporate computation on net taxable
profit. Because resident companies are taxed on their **worldwide**
profit, an uplift on a Suriname entity's margin cannot be netted
against a foreign affiliate's offsetting loss for Suriname purposes
unless a treaty MAP route exists — and Suriname's network is narrow
(Netherlands, Curaçao). Offsets available in-country are the ordinary
loss carryforward (7 years; indefinite for first-3-year losses).

## 5. Deadlines

- **Corporate return:** filed after year-end on the schedule set by the
  tax administration; provisional/advance payments during the year
  (exact calendar: approx — confirm, see sr-corporate-income-tax).
- **TP documentation:** no statutory preparation deadline confirmed —
  **needs-sources**; keep contemporaneous records anyway, because the
  revaluation power runs with the assessment window.

## 6. Penalties and interest

Under-declaration found on revaluation is assessed with the ordinary
penalty and interest regime of the income-tax laws (amounts
**needs-sources** — the Suriname statute portals did not resolve this
pass). Objection practice follows the Ministry/gov.sr service routes.

## 7. Cross-border interaction

Treaty relief on a revaluation is only realistic with the Netherlands
or Curaçao counterparties; both instruments carry MAP articles
(article-level citations **needs-sources**). For all other
counterparties, double exposure on an uplift is not eliminated —
price at arm's length up front. See sr-cross-border.

## 8. Worked examples

**Example 1 — cheap loan from the parent.** A Suriname company borrows
SRD 5,000,000 from its foreign parent at 2% when the arm's-length rate
is 12%. The administration disallows the interest shortfall:
SRD 500,000 of extra profit at the 36% corporate rate = SRD 180,000
(no interest WHT overlay, per the no-general-interest-WHT position —
approx — confirm).

```oa-check
name: interest shortfall SRD 5m loan
inputs:
  principal: 5000000
  arm_rate: 12
  paid_rate: 2
steps:
  - shortfall: principal * (pct(1, arm_rate) - pct(1, paid_rate))
  - cit: shortfall * 0.36
expected:
  cit: 180000.00
```

**Example 2 — underpriced sale to a foreign affiliate.** A Suriname
manufacturer sells goods to its foreign affiliate for SRD 4,000,000;
the arm's-length price is SRD 5,500,000. The SRD 1,500,000 uplift is
taxed at 36% = SRD 540,000.

```oa-check
name: goods uplift SRD 1.5m
inputs:
  arm_price: 5500000
  charged: 4000000
steps:
  - uplift: arm_price - charged
  - cit: uplift * 0.36
expected:
  cit: 540000.00
```

## 9. Ask the client first

1. Which related-party transactions crossed the border — goods,
   services, loans, royalties, cost allocations?
2. Do the Suriname books and the counterparty's books record the same
   price in both countries?
3. Is the counterparty in the Netherlands or Curaçao (the only treaty
   MAP routes), or elsewhere (no treaty relief)?
4. Are there loss carryforwards that could absorb an uplift — within
   the 7-year window, or first-3-year indefinite losses?

## 10. Sources

- [Republiek van Suriname — portaal](https://gov.sr/) — read 2026-10-24.
- [Ministerie van Financiën en Planning](https://gov.sr/ministeries/ministerie-van-financien-en-planning/) — read 2026-10-24.
- Existing pack skills `sr-corporate-income-tax`, `sr-income-tax` — Income Tax Act 1922 and Dividendbelasting figures carried forward with their citations.
- Tax administration / statute portals (belastingkantoor.sr, surinamewetten.sr) — DNS unresolved 2026-10-24; **needs-sources**.

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
