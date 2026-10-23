---
name: cw-cross-border
description: >
  Curaçao cross-border tax reference for 2026. Covers residence and the
  worldwide basis for residents versus source basis for non-residents,
  dividend/interest/royalty withholding under the reformed Profit Tax,
  the participation exemption, the 2023 Corporate Tax Reform changes,
  definitive departure (definitief vertrek) for individuals, and the
  treaty position (Kingdom of the Netherlands relations). Trigger on
  Curaçao treaty, non-resident withholding, uitwijken, definitief
  vertrek, participation exemption. Source-cited draft.
jurisdiction: CW
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Curaçao cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: belastingdienst.cw
(homepage HTTP 200; the definitief-vertrek page returned content via
browser-UA but intermittently 403 from this workstation), gobiernu.cw
(HTTP 200), and the pack's tier-2 skills (`cw-tax-overview`,
`cw-corporate-income-tax`, `cw-income-tax`). Core statutes: Landssverordening
winstbelasting (Profit Tax, reformed 2023, effective 2024) and
Landswet inkomstenbelasting (Income Tax). Currency NAg/ANG.

**Source status caveat:** consolidated ordinance texts did not resolve at
stable article paths this pass; outbound withholding rates and the treaty
list are carried from tier-2 pack skills or marked **needs-sources**.

## 2. Charging scope

- **Residents** (individuals and entities) are taxed on worldwide income;
  **non-residents** on Curaçao-source income (carried from `cw-tax-overview`).
- An entity is Curaçao-registered or effectively managed here; the
  2023 reform moved toward place-of-effective-management tests
  (confirm article — needs-sources).
- **Individuals departing:** the tax administration publishes a
  definitive-departure (definitief vertrek) procedure — deregistration
  ends Curaçao liability prospectively; a hidden-gain exit charge on
  substantial interests is **needs-sources** (not confirmed this pass).

## 3. Withholding and outbound flows

| Item | Rate / rule | Source (as_of 2026-10-23) |
|---|---|---|
| Dividends to non-residents | generally 0% under the Profit Tax regime | carried from `cw-corporate-income-tax` (confirm — needs-sources) |
| Interest / royalties to non-residents | no general outbound WHT confirmed | **needs-sources** |
| Participation exemption | dividends/capital gains from qualifying holdings exempt | carried from `cw-corporate-income-tax` |
| Treaty network | Curaçao is part of the Kingdom; the Netherlands DTTs do not automatically apply — Kingdom extensions are treaty-specific | **needs-sources** |
| Pillar Two QDMTT/GIT | 15% for groups EUR 750m+ | carried from `cw-corporate-income-tax` |

## 4. Filings and deadlines

- Non-resident entities with Curaçao-source profit register and file the
  Profit Tax return (6 months after year-end, extendable).
- Individuals on definitive departure file a final Income Tax return up to
  the departure date (procedure page on belastingdienst.cw — intermittently
  403 this pass).

## 5. Penalties and interest

Standard OTB interest on additional assessments; specific cross-border
penalty percentages **needs-sources**.

## 6. Worked examples

**Example 1 — foreign parent dividend out.** A Curaçao group company
(22% regime) distributes NAg 900,000 to its foreign parent. With the
0% dividend withholding carried from the pack, the Curaçao-side cost is
NAg 0.00 — the parent's home-country tax applies separately (confirm the
0% rate against the ordinance before relying on it).

```oa-check
name: Dividend out, 0% WHT NAg 900,000
inputs:
  dividend: 900000
steps:
  - wht: dividend * 0.00
expected:
  wht: 0.00
```

**Example 2 — non-resident branch profit.** A foreign company's Curaçao
activity yields NAg 500,000 taxable profit; Profit Tax at 22% =
110,000.00, and the after-tax remittance faces no confirmed outbound
WHT (needs-sources flag).

```oa-check
name: Non-resident branch profit NAg 500,000
inputs:
  profit: 500000
steps:
  - tax: profit * 0.22
expected:
  tax: 110000.00
```

## 7. Ask the client first

1. Is the entity Curaçao-registered, effectively managed here, or both?
2. Does a Kingdom-of-the-Netherlands treaty extension actually cover
   Curaçao for the counterparty country?
3. Is the individual filing definitive departure — and when?
4. Is there a substantial interest whose gain crystallises on exit?
5. Is the group in Pillar Two scope?

## 8. Sources

- [Belastingdienst Curaçao (tax administration)](https://belastingdienst.cw/) — read 2026-10-23 (homepage HTTP 200; article paths intermittently 403).
- [Gobiernu.cw — wet- en regelgeving](https://gobiernu.cw/nl/themas/wet-regelgeving/) — read 2026-10-23.
- Pack skills carried: `cw-tax-overview`, `cw-corporate-income-tax`, `cw-income-tax` (tier 2, read 2026-07-13).

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
