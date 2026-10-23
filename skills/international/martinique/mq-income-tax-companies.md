---
name: mq-income-tax-companies
description: >
  Martinique corporate income tax reference for 2026. Martinique companies
  pay French IS: 25% standard, 15% reduced rate on the first EUR 42,500 for
  qualifying small companies, plus overseas investment incentives (CGI Art.
  217 bis / 217 undecies). Covers rates, base, acompte instalments,
  deadlines, penalties and the octroi interface. Source-cited draft; the
  overseas incentive percentages need Legifrance re-verification
  (needs-sources).
jurisdiction: MQ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Martinique corporate income tax

## 1. Scope and sources

French IS applies unchanged in Martinique (CGI Art. 205 ff). Rates carried from the France pack (`fr-business-accounting.md`, official pages read 19 Sep–19 Oct 2026). legifrance 403 on 2026-10-22; the overseas incentive layer (Art. 217 bis/undecies) is needs-sources for current percentages.

## 2. Who is liable

Siège or effective management in Martinique → worldwide profits (Art. 209). Non-residents → Martinique-source profits (PE, real property, farming).

## 3. Rates

| Rate | Applies to | Source |
|---:|---|---|
| 25% | standard IS | France pack, official page read 19 Oct 2026 |
| 15% | first €42,500, Art. 219 I-bis conditions (turnover < €10m, shares fully paid, ≥75% held by individuals) | same |
| Overseas incentives | investment deferrals/exemptions (Art. 217 bis, 217 undecies/duodecies) — **needs-sources** | Legifrance 403 on 2026-10-22 |

## 4. Base

Metropolitan BIC determination rules; overseas incentives reduce or defer the base for qualifying investment — check the eligibility list first.

## 5. Deadlines

- Return (2065 etc.): 3 months after year-end (second working day after 15 May for calendar-year entities).
- Acomptes: 15 February, 15 November, plus 15 August / 15 December balancing instalments (Art. 1668 CGI).

## 6. Penalties and interest

10%/40%/80% late-filing ladder (Art. 1728); interest in arrears (Art. 1727); 5% surcharge on acompte shortfalls (Art. 1731).

## 7. Cross-border points

EU parent-subsidiary / interest-royalty directives apply via France; intra-group goods flows also bear octroi de mer (see `mq-antilles-goods-movements`); transfer pricing per `mq-transfer-pricing`.

## 8. Worked examples

**Example 1 — qualifying small company, profit €100,000.**
42,500 × 15% = 6,375; (100,000 − 42,500) × 25% = 14,375; total 20,750.00.

```oa-check
name: Qualifying small company profit EUR 100,000
inputs:
  profit: 100000
steps:
  - slice1: min(profit, 42500) * 0.15
  - slice2: max(profit - 42500, 0) * 0.25
  - tax: slice1 + slice2
expected:
  tax: 20750.00
```

**Example 2 — November acompte = 25% of prior IS.**
20,750 × 25% = 5,187.50.

```oa-check
name: November acompte on prior IS
inputs:
  prior_is: 20750
steps:
  - acompte: prior_is * 0.25
expected:
  acompte: 5187.50
```

## 9. Ask the client first

1. Art. 219 I-bis eligibility.
2. Overseas incentive files in force (Art. 217 series).
3. Year-end and acompte calendar.
4. Intra-group flows with the metropole or CARICOM counterparties.

## 10. Sources

- France pack `fr-business-accounting.md` (official pages read 19 Sep–19 Oct 2026).
- CGI Art. 205–219, 1668, 217 series — [Legifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069044/) (403 on 2026-10-22; needs-sources).
