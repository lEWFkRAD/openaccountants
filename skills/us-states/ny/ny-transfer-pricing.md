---
name: ny-transfer-pricing
description: >-
  Use when a corporate group with New York nexus needs the 2026 answer on
  Article 9-A connected-party and unitary rules: combined filing on Form
  CT-3-A with related corporations (verified from tax.ny.gov Article 9-A
  page), the business-income base taxed at up to 7.25% (rate table
  verified in the CT-3-A instructions PDF), the highest-of-three-bases
  rule (business income / capital / net income), market-based receipts
  sourcing, and intercompany royalty/management-fee planning under the
  combined return. Trigger on NY combined return CT-3-A, Article 9-A
  combined, NY 7.25 percent, NY related corporation, NY receipts factor.
  Source-cited draft; statute text (Tax Law 210-A et seq.) not fetched
  this run.
jurisdiction: US-NY
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---

# New York transfer pricing (Article 9-A combined reporting, receipts, intangibles)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

C corporations and other general business corporations taxable under Tax Law Article 9-A that are related to, or unitary with, other corporations — especially groups routing intangibles, financing, or services through low-tax affiliates. New York taxes Article 9-A corporations on the **highest of three bases** (business income base, capital base, tax on net income) plus the MTA surcharge where applicable, and requires **combined filing on Form CT-3-A** for related corporations. _(tax.ny.gov/bus/ct/article9a.htm, 200 with text, 2026-10-25.)_

## Rates, bands and thresholds

- **Combined return.** "General business corporations that file on a combined basis with related corporations file Form CT-3-A, General Business Corporation Combined Franchise Tax Return." Standalone filers use Form CT-3. The CT-3-A instructions define combined-group membership and the designated-agent filing mechanics. _(article9a.htm verified 200, 2026-10-25; CT-3-A PDF verified 200 with combined-group lines, 2026-10-25.)_
- **Business income base top rate: 7.25%.** The CT-3-A instructions rate table carries tax factors 0.04875 and **0.0725** (plus the 2% ENI rate and fixed-dollar minimums on the return). _(CT-3-A instructions PDF, tax.ny.gov/pdf/current_forms/ct/ct3ai.pdf, 200, 2026-10-25. The graduated business-base brackets and the $5M/200M thresholds: confirm against the CT-3/CT-3-A instructions before relying — Tax Law §§ 210-A/210-B statute text not fetched 2026-10-25: **not yet confirmed**.)_
- **Highest-of-three-bases.** The franchise tax is the highest of: business income base × rate, capital base × rate, or a tax on net income — plus MTA surcharge in the MCTD. _(article9a.htm, verified 2026-10-25.)_
- **Receipts factor.** Article 9-A apportionment uses a receipts factor with market-based sourcing (customer location / benefit tests); the DTF page "Deriving combined group receipts" governs combined-group receipts. _(article9a_deriving_receipts.htm linked from article9a.htm, verified 2026-10-25; the § 210-A receipts text itself: **not yet confirmed**.)_
- **No water's-edge surtax** (contrast ND): NY's combined group scope is defined by taxability/unitary tests in the CT-3-A instructions — the precise current membership test: **not yet confirmed** (instructions PDF text extraction partial).

## The taxable base

1. Start from federal taxable income with NY modifications (combined, if CT-3-A).
2. Intercompany transactions within the combined group are eliminated on the combined return — royalty/fee stripping between combined members does not move group NY tax; stripping to **non-combined** affiliates (e.g., a member excluded from the NY combined group, or a foreign affiliate outside the group) does reduce the business income base and is the planning pressure point DTF audits.
3. Apportion by the receipts factor (market sourcing), combined-group receipts per the DTF guidance.
4. Compute all three bases; the highest controls. MTA surcharge applies separately in the MCTD (see `ny-mctmt`).

## Deadlines and filing

- CT-3 / CT-3-A: 15th day of the 4th month after year end (Apr 15 calendar filers); extension follows the federal extension.
- Estimated payments: quarterly on Form CT-4 (installment percentages per instructions; exact 2026 percentages: **not yet confirmed**).
- Combined groups file through a designated agent; membership changes must be reflected in the first combined return of the group.

## Penalties and interest

- Underpaid estimates: interest from each installment date (Tax Law Ch. 9 mechanics; 2026 rate: **not yet confirmed**).
- Late filing: Ch. 9 penalties (5%/month to 25% historically — confirm current: **not yet confirmed**).
- DTF audit themes: intangible transfers to non-combined affiliates, management-fee stripping, and receipts-factor manipulation (alternative apportionment authority under § 210-a(6): **not yet confirmed**).

## Cross-border points

- Foreign affiliates outside the combined group: royalty/interest flows to them are the classic NY stripping structure; federal §267/§163(j) and BEPS/Pillar-Two considerations are federal (federal skills).
- Combined-group membership interacts with other states' combined regimes (NY Joyce/Finnigan treatment of non-taxable members: **not yet confirmed** — confirm in CT-3-A instructions).
- MCTD surcharge stacks on top of the 9-A tax for MCTD business (see `ny-mctmt`).

## Worked examples

**Example 1 — receipts-factor apportionment, standalone CT-3.** Group NY receipts $9M of $20M total; combined business income base $4M (all at the 7.25% top rate for simplicity).

```oa-check
name: ny 9a receipts apportionment
inputs:
  sn: 9000000
  st: 20000000
  ci: 4000000
steps:
  - f: sn / st
  - base: ci * f
  - tax: base * 0.0725
expected:
  f: 0.45
  base: 1800000.00
  tax: 130500.00
```

**Example 2 — royalty stripping to a non-combined affiliate.** Same group pays an $800,000 royalty to an affiliate excluded from the NY combined group; the royalty reduces the pre-allocation base by $800,000 × 0.45 receipts.

```oa-check
name: ny royalty stripping noncombined
inputs:
  pre: 1800000
  roy: 800000
  f: 0.45
steps:
  - cut: roy * f
  - base: pre - cut
  - tax: base * 0.0725
expected:
  cut: 360000.00
  base: 1440000.00
  tax: 104400.00
```

(The $26,100 saving is the DTF's audit target: if the royalty is recharacterized or the affiliate pulled into the combined group, it disappears.)

## Ask the client first

1. Which members are taxable in NY, and is the group filing CT-3-A through a designated agent?
2. Where do the IP, debt, and service functions sit relative to the NY combined group?
3. Are intercompany royalty/fee rates documented and arm's-length?
4. Do receipts reflect the market-sourcing tests (customer location, benefit receipt)?
5. Is the capital base or ENI base ever the highest of the three — is the 7.25% business-base assumption even the controlling one?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| NYS DOL — Unemployment Insurance rate information | https://dol.ny.gov/unemployment-insurance-rate-information | 2026-10-28 |

Not yet confirmed: figures below the Sources heading lack archived line-citations.

- NYS DTF — Article 9-A overview (three bases, CT-3 vs CT-3-A combined filing, MTA surcharge): <https://www.tax.ny.gov/bus/ct/article9a.htm> — 200 with text, 2026-10-25.
- NYS DTF — Form CT-3-A instructions (7.25% rate factor 0.0725 in the rate table; combined-group lines): <https://www.tax.ny.gov/pdf/current_forms/ct/ct3ai.pdf> — 200 PDF, 2026-10-25.
- NYS DTF — Form CT-3-A (combined return form): <https://www.tax.ny.gov/pdf/current_forms/ct/ct3a.pdf> — 200 PDF, 2026-10-25.
- NYS DTF — Deriving combined group receipts: <https://www.tax.ny.gov/bus/ct/article9a_deriving_receipts.htm> — linked from the Article 9-A page, 2026-10-25.
- Tax Law §§ 210-A, 210-B, 210-C, 251 statute text; 2026 CT-4 installment percentages; penalty schedule: **not yet confirmed** — not fetched 2026-10-25.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min

## Talk to a verified accountant


This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
