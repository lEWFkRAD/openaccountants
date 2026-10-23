---
name: cw-transfer-pricing
description: >
  Curaçao transfer pricing reference for 2026. Covers the arm's-length
  principle in the Profit Tax (Landssverordening winstbelasting), the
  2023 Corporate Tax Reform documentation duties, the related-party
  definition, the 2024 Pillar Two minimum tax (15% QDMTT/GIT for groups
  EUR 750m+), and the OTB assessment powers. Trigger on Curaçao transfer
  pricing, winstbelasting related party, groepsbedrijf, minimumbelasting.
  Source-cited draft.
jurisdiction: CW
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Curaçao transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the Curaçao tax
administration (belastingdienst.cw — homepage and theme pages HTTP 200 via
browser-UA; deeper article paths intermittently 403 from this
workstation), the government legislation portal (gobiernu.cw, HTTP 200),
and the pack's existing tier-2 skills (`cw-corporate-income-tax`,
`cw-tax-overview`). Core statute: Landssverordening winstbelasting (Profit
Tax Ordinance) as replaced by the 2023 Corporate Tax Reform (effective
2024). Currency Netherlands Antillean guilder (NAg/ANG, pegged 1.79/USD).

**Source status caveat:** the consolidated PTO text and the Pillar Two
ordinance (Landssverordening minimumbelasting) did not resolve at stable
article paths this pass; documentation thresholds and penalty percentages
are marked **needs-sources** rather than invented.

## 2. Who the rules apply to

- **Groepsbedrijf (group company) test.** Under the reformed Profit Tax,
  a Curaçao entity is a group company when a related party holds ≥50% or
  exercises decisive influence; group companies owe the arm's-length
  standard and documentation duties (carried from `cw-corporate-income-tax`,
  tier 2).
- **Related-party transactions** — goods, services, financing, royalties,
  cost allocations between a Curaçao taxpayer and foreign or domestic
  related parties — must be priced as independent parties would.
- **Pillar Two layer:** groups with consolidated revenue ≥ EUR 750m in at
  least two of four years face the 15% minimum tax (QDMTT/GIT) from 2025
  (carried from `cw-corporate-income-tax`; confirm ordinance number —
  needs-sources).

## 3. Rates and thresholds

| Item | Rate / threshold | Source (as_of 2026-10-23) |
|---|---|---|
| Profit Tax base the TP adjustment hits | 22% standard / 15% small (<NAg 5m) | carried from `cw-corporate-income-tax` (2024 reform) |
| Group-company related-party test | 50% holding / decisive influence | carried from `cw-corporate-income-tax` |
| Master/local file thresholds | not confirmed at official path | **needs-sources** |
| Pillar Two group threshold | EUR 750,000,000 | carried from `cw-corporate-income-tax` (confirm ordinance) |

## 4. Filings and deadlines

- Profit Tax return (winstbelasting aangifte) is due within 6 months of
  year-end, extendable; transfer documentation must be available on
  request (exact statutory deadline **needs-sources**).
- Pillar Two returns follow the GloBE model timelines for in-scope groups
  (confirm — needs-sources).

## 5. Penalties and interest

The OTB (Ontvanger Belastingen) can assess additional Profit Tax plus
interest for understated related-party pricing; late-supply of
documentation can draw fines. Specific percentages are **needs-sources** —
do not quote a Curaçao TP penalty figure without the ordinance text.

## 6. Worked examples

**Example 1 — related-party service fee understated.** A Curaçao group
company (22% regime) charges its foreign parent for management services
at NAg 400,000; the arm's-length fee is NAg 650,000. The OTB restates
profit upward by 250,000; additional Profit Tax = 250,000 × 22% =
55,000.00.

```oa-check
name: Service fee restatement NAg 250,000
inputs:
  arm_length: 650000
  charged: 400000
steps:
  - uplift: arm_length - charged
  - tax: uplift * 0.22
expected:
  tax: 55000.00
```

**Example 2 — small-regime financing adjustment.** A small company (15%
regime) pays a related-party loan interest of NAg 120,000 where the
arm's-length rate supports only NAg 70,000; disallowed 50,000 × 15% =
7,500.00 additional tax.

```oa-check
name: Interest disallowance small regime NAg 50,000
inputs:
  paid: 120000
  arm_length: 70000
steps:
  - disallowed: paid - arm_length
  - tax: disallowed * 0.15
expected:
  tax: 7500.00
```

## 7. Ask the client first

1. Is the entity a group company under the 50%/decisive-influence test?
2. Which Profit Tax regime applies — 22% standard or 15% small (<NAg 5m)?
3. Is the group in Pillar Two scope (EUR 750m+ revenue)?
4. What transfer documentation exists today, and in what language?
5. Are intra-group financings documented with rates and terms?

## 8. Sources

- [Belastingdienst Curaçao (tax administration)](https://belastingdienst.cw/) — read 2026-10-23 (homepage HTTP 200; article paths intermittently 403).
- [Gobiernu.cw — wet- en regelgeving](https://gobiernu.cw/nl/themas/wet-regelgeving/) — read 2026-10-23.
- Pack skills carried: `cw-corporate-income-tax`, `cw-tax-overview` (tier 2, read 2026-07-13).

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
