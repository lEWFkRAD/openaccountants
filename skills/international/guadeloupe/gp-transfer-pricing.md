---
name: gp-transfer-pricing
description: >
  Guadeloupe transfer pricing reference for 2026. Guadeloupe companies fall
  under the French regime: the arm's-length rule of CGI Art. 57, the master/
  local documentation file under LPF Art. L. 13 AA, the 2257-SD annual
  declaration, the 2258-SD country-by-country report, and the penalties for
  each. Covers the rule, thresholds, deadlines, penalties and the DOM angle
  (intra-group goods flows also bear octroi de mer and DOM VAT). Built on
  the France pack's verified 2026 figures.
jurisdiction: GP
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Guadeloupe transfer pricing

## 1. Scope and sources

The French transfer-pricing regime applies in Guadeloupe without local variation. All figures carried from the France pack (`france-transfer-pricing.md`, every figure read from official pages 19 Sep–19 Oct 2026: Art. 57 CGI arm's-length rule, L. 13 AA documentation, 2257-SD, 2258-SD CbCR, fines).

## 2. The rule

Art. 57 CGI lets the administration correct declared results where profits are indirectly transferred to related foreign entities through non-arm's-length prices "or by any other means". For accounting years opened from 1 January 2024, departing from the documented method creates a deemed transfer unless the company proves none occurred (burden on the company).

## 3. Documentation and filings

| Obligation | Trigger | Deadline | Source |
|---|---|---|---|
| Master + local file (L. 13 AA) | turnover or assets > €400m (higher thresholds apply; see France pack Section on thresholds) | within the 2257-SD filing window | France pack, verified 2026 |
| 2257-SD declaration | related-party transactions > €2m (or the reduced threshold) | with the return | same |
| 2258-SD CbCR | groups > €750m consolidated revenue | 12 months after year-end | same |

## 4. Penalties

Failure to file 2257-SD or produce the file: the France pack's fixed fines (€50,000-scale, or 0.5% of the reassessed amounts where higher — verify the current figure in the France pack table, read 19 Oct 2026). Art. 57 adjustments carry interest in arrears plus the bad-faith or 40%/80% increases where applicable.

## 5. The DOM angle

Intra-group **goods** movements between Guadeloupe and the metropole or third countries are customs movements: they bear octroi de mer and import VAT on top of the income-tax treatment (see `gp-producer-octroi-compliance`, `gp-value-added-tax`). Transfer-pricing policy must be consistent with the customs values declared — a low intra-group price raises income tax but lowers the octroi/VAT base, and customs and tax administrations cross-check.

## 6. Worked examples

**Example 1 — profit transfer corrected.** A Guadeloupe distributor buys from the group's mainland parent at above-market prices; the administration re-establishes €50,000 of profit: additional IS at 25% = 12,500.00 (before interest).

```oa-check
name: Art 57 adjustment EUR 50,000
inputs:
  adjustment: 50000
steps:
  - is: adjustment * 0.25
expected:
  is: 12500.00
```

**Example 2 — consistency check with customs.** The same €50,000 price uplift had reduced the import value; at the illustrative 13% octroi rate the group had also underpaid octroi of 50,000 × 13% = 6,500.00 — the two administrations' adjustments stack.

```oa-check
name: Octroi consistency on EUR 50,000 uplift illustrative
inputs:
  uplift: 50000
steps:
  - octroi: uplift * 0.13
expected:
  octroi: 6500.00
```

## 7. Ask the client first

1. Group revenue vs the CbCR and documentation thresholds.
2. Are intra-group goods prices consistent between the TP file and customs declarations?
3. Which method is documented and actually applied?
4. Any APAs or advance rulings covering DOM distribution margins.

## 8. Sources

- France pack `france-transfer-pricing.md` (Art. 57 CGI, L. 13 AA/L. 13 AB, fines — official pages read 19 Sep–19 Oct 2026, incl. BOI-BIC-BASE-80-10-20).
- [douane.gouv.fr octroi de mer declaration](https://www.douane.gouv.fr/demarche/declarer-votre-octroi-de-mer-interne) — read 2026-10-22.
