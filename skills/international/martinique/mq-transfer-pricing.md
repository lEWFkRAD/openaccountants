---
name: mq-transfer-pricing
description: >
  Martinique transfer pricing reference for 2026. Martinique companies fall
  under the French regime: the arm's-length rule of CGI Art. 57, master/
  local documentation under LPF Art. L. 13 AA, the 2257-SD annual
  declaration and 2258-SD country-by-country report, and the penalties.
  Covers the rule, thresholds, deadlines, penalties and the DOM angle
  (intra-group goods flows also bear octroi de mer and DOM VAT, and
  customs values are cross-checked). Built on the France pack's verified
  2026 figures.
jurisdiction: MQ
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Martinique transfer pricing

## 1. Scope and sources

The French transfer-pricing regime applies in Martinique without local variation. Figures carried from the France pack (`france-transfer-pricing.md`, all read from official pages 19 Sep–19 Oct 2026: Art. 57 CGI, L. 13 AA documentation, 2257-SD, 2258-SD CbCR, fines).

## 2. The rule

Art. 57 CGI allows correction of declared results where profits are indirectly transferred to related foreign entities via non-arm's-length prices "or by any other means". For accounting years opened from 1 January 2024, departing from the documented method creates a deemed transfer unless the company proves none occurred.

## 3. Documentation and filings

| Obligation | Trigger | Deadline | Source |
|---|---|---|---|
| Master + local file (L. 13 AA) | turnover or assets > €400m | within the 2257-SD window | France pack, verified 2026 |
| 2257-SD declaration | related-party transactions over the threshold (€2m scale) | with the return | same |
| 2258-SD CbCR | groups > €750m consolidated revenue | 12 months after year-end | same |

## 4. Penalties

Failure to file/produce: the France pack's fixed fines (€50,000-scale or 0.5% of reassessed amounts where higher — see the France pack table, read 19 Oct 2026). Art. 57 adjustments carry interest in arrears plus 40%/80% increases in bad-faith cases.

## 5. The DOM angle

Intra-group **goods** between Martinique and the metropole (or third countries) are customs movements bearing octroi de mer and import VAT. A low intra-group price cuts income tax but cuts the octroi/VAT base too — customs and tax cross-check declared values. Inter-island Guadeloupe↔Martinique flows need the monthly dispatch declaration (`mq-antilles-goods-movements`).

## 6. Worked examples

**Example 1 — Art. 57 correction of €50,000.**
Additional IS at 25% = 12,500.00 (before interest).

```oa-check
name: Art 57 adjustment EUR 50,000
inputs:
  adjustment: 50000
steps:
  - is: adjustment * 0.25
expected:
  is: 12500.00
```

**Example 2 — customs consistency on the same uplift (illustrative 13% octroi).**
50,000 × 13% = 6,500.00 additional octroi exposure stacks with the IS adjustment.

```oa-check
name: Octroi consistency EUR 50,000 uplift illustrative
inputs:
  uplift: 50000
steps:
  - octroi: uplift * 0.13
expected:
  octroi: 6500.00
```

## 7. Ask the client first

1. Group revenue vs CbCR/documentation thresholds.
2. TP-file prices vs customs-declared values.
3. Documented method and actual application.
4. Any APAs/rulings covering DOM distribution margins.

## 8. Sources

- France pack `france-transfer-pricing.md` (Art. 57 CGI, L. 13 AA/AB, fines — official pages read 19 Sep–19 Oct 2026, incl. BOI-BIC-BASE-80-10-20).
- [douane.gouv.fr octroi de mer declaration](https://www.douane.gouv.fr/demarche/declarer-votre-octroi-de-mer-interne) — read 2026-10-22.
