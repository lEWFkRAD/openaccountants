---
name: gp-income-tax-companies
description: >
  Guadeloupe corporate income tax reference for 2026. Guadeloupe companies
  pay French IS: 25% standard, 15% reduced rate on the first EUR 42,500 for
  qualifying small companies, plus the overseas investment-deferral and
  exemption incentives (CGI Art. 217 bis etc.). Covers rates, the base,
  instalments (acomptes), deadlines, penalties and the octroi/VAT interface.
  Source-cited draft; the overseas incentive percentages need Legifrance
  re-verification (needs-sources).
jurisdiction: GP
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Guadeloupe corporate income tax

## 1. Scope and sources

French IS applies unchanged in Guadeloupe (CGI Art. 205 ff). Rate figures carried from the France pack (`fr-business-accounting.md`, official pages read 19 Sep–19 Oct 2026: 25% standard, 15% reduced on the first €42,500). legifrance.gouv.fr 403 on 2026-10-22; the overseas incentive layer (Art. 217 bis/217 undecies, deferral regimes) is flagged needs-sources for current percentages.

## 2. Who is liable

Companies with their siège or effective management in Guadeloupe are taxable on worldwide profits (Art. 209); non-resident companies on Guadeloupe-source profits (permanent establishment, real property, farming income).

## 3. Rates

| Rate | Applies to | Source |
|---:|---|---|
| 25% | standard IS, all profits above the reduced-rate slice | France pack, official page read 19 Oct 2026 |
| 15% | first €42,500 of profit, companies meeting the Art. 219 I-bis conditions (turnover < €10m, fully paid-up shares, held ≥75% by individuals) | same |
| Overseas incentives | deferrals/exemptions for qualifying investment (Art. 217 bis, 217 undecies/duodecies) — **needs-sources** | Legifrance 403 on 2026-10-22 |

## 4. Base

Same determination rules as metropolitan France (BIC schedules, deductibility, carry-forward of deficits). Overseas investment incentives reduce the base or defer recognition — classify the asset against the incentive's eligibility list before applying.

## 5. Deadlines

- Return (2065 etc.): within 3 months of the accounting year-end (second working day after 15 May for calendar-year entities).
- **Acomptes**: payments on 15 February, 15 November, plus 15 August and 15 December balancing instalments (Art. 1668 CGI); first-year entities exempt from the February acompte.

## 6. Penalties and interest

Late filing 10%/40%/80% ladder (Art. 1728 CGI); interest in arrears at the legal rate (Art. 1727); insufficient acomptes attract a 5% interest surcharge on the shortfall (Art. 1731).

## 7. Cross-border points

- EU parent-subsidiary and interest-royalty directives apply to Guadeloupe entities (France is the reporting Member State; check the directive's ORA notes).
- Transfer pricing on dealings with the mainland or third countries: see `gp-transfer-pricing`.
- Octroi de mer is a goods tax, not deductible against IS in the same way as VAT — see `gp-producer-octroi-compliance`.

## 8. Worked examples

**Example 1 — qualifying small company, profit €100,000.**
Slice 1: 42,500 × 15% = 6,375. Slice 2: (100,000 − 42,500) × 25% = 14,375. Total 20,750.00.

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

**Example 2 — same company, November acompte.**
The 15 November acompte is 25% of the prior-year IS: 20,750 × 25% = 5,187.50.

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

1. Does the company meet the Art. 219 I-bis reduced-rate conditions?
2. Any overseas investment-incentive file (Art. 217 series) in force?
3. Accounting year-end and acompte calendar.
4. Intra-group flows with mainland France or third countries.

## 10. Sources

- France pack `fr-business-accounting.md` (IS rates, official pages read 19 Sep–19 Oct 2026).
- CGI Art. 205–219, 1668, 217 bis — [Legifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069044/) (403 on 2026-10-22; incentive layer needs-sources).
