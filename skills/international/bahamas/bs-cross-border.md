---
name: bs-cross-border
description: >
  Bahamas cross-border tax reference for 2026. Covers the absence of
  withholding tax on dividends, interest and royalties, the absence of a
  double-tax-treaty network (information exchange runs on TIEAs, FATCA,
  CRS and the Common Reporting Standard rather than DTAs), the
  Corporate Economic and Social Reporting Act (CESRA) substance reporting
  administered by the Department of Inland Revenue, and how the Domestic
  Minimum Top-Up Tax 2024 interacts with inbound and outbound group
  structures. Trigger on Bahamas cross-border, withholding, treaty, TIEA,
  CESRA substance, exchange of information. Source-cited draft.
jurisdiction: BS
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Bahamas cross-border

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the DIR site
structure (DMTT pages, CESRA substance-reporting section), the OPM Pillar
Two portal and DMTT Act 2024 text. The TIEA inventory is **needs-sources**
(see caveat) — no consolidated Bahamian treaty register resolved in this
pass.

**Source status caveat:** legislation.gov.bs and laws.bahamas.gov.bs did not
resolve to usable statute text from this environment; the DMTT Act PDF was
read from the OPM portal instead. The list of Bahamian Tax Information
Exchange Agreements (TIEAs) was not verified against an official register —
confirm before asserting a specific counterparty.

## 2. Who this applies to

- Any Bahamian entity paying or receiving cross-border flows — the
  withholding picture below is structural (there is no income tax to
  withhold).
- In-scope MNE groups with Bahamian constituent entities (DMTT — see
  bs-transfer-pricing).
- Entities carrying on "economic and other activity" in The Bahamas:
  substance reporting under CESRA, administered by DIR (the DIR site runs
  a Substance Reporting (CESRA) section with legal forms and FAQs).

## 3. Withholding and outbound payments (rates table)

| Item | Position | Source |
|---|---|---|
| Dividends, interest, royalties to non-residents | No withholding tax | bs-corporate-income-tax (no income tax); DIR tax-type index shows no WHT tax type |
| Business licence tax | Annual turnover-based licence tax (covered in bs-payroll-social / overview), not a cross-border charge | DIR Business Licence section |
| DMTT (in-scope groups) | 15% minimum on Bahamian GloBE ETR | DMTT Act 2024 |

## 4. Treaty and information-exchange network

- The Bahamas has **no double-tax-treaty (DTA) network** in the classic
  sense; there is no treaty relief to claim because there is no income tax
  to relieve.
- Information exchange runs through Tax Information Exchange Agreements
  (TIEAs) and the multilateral instruments: FATCA (US), the Common
  Reporting Standard (CRS), and automatic-exchange regulations. The DIR
  and OPM portals administer the reporting rails. Exact TIEA partner
  list: **needs-sources**.
- Practical consequence for groups: no treaty interest/royalty reductions
  apply on Bahamian legs; the Pillar Two DMTT, not treaties, is the
  cross-border tax lever.

## 5. Substance reporting (CESRA)

The Corporate Economic and Social Reporting Act regime requires in-scope
entities to report economic activity in The Bahamas to DIR (registration,
annual reporting; the DIR site carries the legal forms, FAQs and
enforcement notices). Substance facts feed the GloBE substance-based
income exclusion for in-scope groups. Exact thresholds and filing dates:
confirm on the DIR CESRA pages — **needs-sources** for the current
calendar.

## 6. Deadlines

- DMTT notification at fiscal-year start; return and payment 15 months
  after fiscal year end (DMTT Act ss.5–6).
- CESRA reporting: DIR calendar — needs-sources.
- Business licence renewals: annual, DIR calendar (see overview skills).

## 7. Worked examples

**Example 1 — outbound royalty with no Bahamian withholding.** A Bahamian
licensee pays a royalty of USD 1,000,000 to a foreign parent. Bahamian
withholding = 0; the parent's jurisdiction may tax the receipt under its
own rules.

```oa-check
name: no Bahamian WHT on royalty USD
inputs:
  royalty: 1000000
  wht_rate: 0
steps:
  - wht: royalty * wht_rate
  - net: royalty - wht
expected:
  net: 1000000.00
```

**Example 2 — group ETR floor check.** An in-scope group's Bahamian
entities pay business licence tax of BSD 200,000 on GloBE income BSD
4,000,000 (ETR 5%). DMTT top-up = 4,000,000 × 15% − 200,000 = BSD
400,000.

```oa-check
name: DMTT floor with BL tax credit BSD
inputs:
  income: 4000000
  covered_tax: 200000
steps:
  - topup: income * 0.15 - covered_tax
expected:
  topup: 400000.00
```

## 8. Ask the client first

1. Is the counterparty expecting treaty relief? (There is none — no DTA
   network, no income tax.)
2. Is the group in DMTT scope, and are CESRA substance reports current?
3. Where will the counterparty jurisdiction tax the flow on its own side?
4. Are FATCA/CRS registrations in place with DIR?

## 9. Sources

- [DIR — D.M.T.T. page](https://inlandrevenue.finance.gov.bs/dmtt/) — read 2026-10-23.
- [DIR site — Substance Reporting (CESRA) section](https://inlandrevenue.finance.gov.bs/) — read 2026-10-23.
- [OPM — Bahamas CIT / Pillar Two portal](https://opm.gov.bs/bahamascitpillar2/) — read 2026-10-23.
- [Domestic Minimum Top-Up Tax Bill/Act 2024 — full text (OPM PDF)](https://opm.gov.bs/wp-content/uploads/2024/08/Domestic-Minimum-Top-Up-Tax-Bill-2024.pdf) — read 2026-10-23.

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
