---
name: gp-income-tax-individuals
description: >
  Guadeloupe individual income tax reference for 2026. Guadeloupe applies the
  French progressive barème (0–45%, 2025 revenues: bands 11,600 / 29,579 /
  84,577 / 181,917 EUR) with the overseas reduction under CGI Art. 197 B.
  Covers who is liable, the barème, the Art. 197 B reduction, quotient
  familial, filing and PAYE deadlines, penalties, and the interface with the
  France pack. Source-cited draft; the Art. 197 B rate and cap need
  Legifrance re-verification (needs-sources).
jurisdiction: GP
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Guadeloupe individual income tax

## 1. Scope and sources

Guadeloupe is a French department: the same Code général des impôts (CGI) applies as in metropolitan France, with the overseas adaptations below. The barème figures were read from service-public.fr F1419 on 2026-10-22 (revenus 2025,impôt 2026) and match the France pack (`fr-personal-income-tax.md`, official pages read 19 Sep–19 Oct 2026). legifrance.gouv.fr returned HTTP 403 to this host on 2026-10-22 — the Art. 197 B reduction details are flagged needs-sources.

## 2. Who is liable

French tax-residence rules (CGI Art. 4 B) apply unchanged: home or main place of abode in Guadeloupe, centre of economic interests, or majority of professional activity. Residents are taxable on worldwide income; non-residents on French-source income only (Art. 4 B II list).

## 3. Rates — barème 2026 (revenus 2025)

| Band (per part) | Rate | Source |
|---|---:|---|
| Up to €11,600 | 0% | [service-public.fr F1419](https://www.service-public.fr/particuliers/vosdroits/F1419), read 2026-10-22 |
| €11,601 – 29,579 | 11% | same |
| €29,580 – 84,577 | 30% | same |
| €84,578 – 181,917 | 41% | same |
| Above €181,917 | 45% | same |

## 4. The overseas reduction (CGI Art. 197 B)

Income tax on Guadeloupe-resident households is reduced by a fixed percentage under Art. 197 B CGI (the "réduction d'impôt outre-mer"), subject to an annual cap per single/married status. **Needs-sources: the current percentage and cap could not be re-read from Legifrance on 2026-10-22 (403); the widely applied figure is 40% capped at €6,350 single / €12,700 joint — verify before use.** The reduction applies to the computed barème tax (after quotient familial), not to the 45% CEHR-type surcharges.

## 5. Base and quotient familial

Same as metropolitan France: net taxable income after the 10% employment deduction (with minimum and ceiling), then quotient familial (parts; single = 1). See `fr-personal-income-tax.md` for the full sequence, décote and caps.

## 6. Deadlines

- Annual return (2042): online in the spring campaign per the DGFiP calendar; paper where not eligible.
- Prélèvement à la source (PAS): monthly withholding at source on current-year income, rate set from the prior return — see `gp-payroll-withholding`.
- Balance adjustments settle July–September per the DGFiP schedule.

## 7. Penalties and interest

- Late filing: 10% increase (Art. 1728 CGI), 40% after 30 days of formal notice, 80% for deliberate evasion.
- Interest in arrears: current legal rate on the unpaid balance (Art. 1727 CGI).

## 8. Worked examples

**Example 1 — single, net taxable €40,000 (before Art. 197 B).**
Band 2: (29,579 − 11,600) × 11% = 1,977.69. Band 3: (40,000 − 29,579) × 30% = 3,126.30. Gross tax 5,103.99. The Art. 197 B reduction then applies (rate/cap needs-sources).

```oa-check
name: Single, net taxable EUR 40,000, barème 2026
inputs:
  income: 40000
steps:
  - band2: (min(income, 29579) - 11600) * 0.11
  - band3: (income - 29579) * 0.30
  - tax: max(band2, 0) + max(band3, 0)
expected:
  tax: 5103.99
```

**Example 2 — same taxpayer, Art. 197 B at the commonly applied 40% (unverified cap).**
Reduction 5,103.99 × 40% = 2,041.60 (below any plausible cap); net 3,062.39.

```oa-check
name: Art 197 B reduction at 40 percent (rate needs-sources)
inputs:
  gross_tax: 5103.99
steps:
  - reduction: gross_tax * 0.40
  - net: gross_tax - reduction
expected:
  net: 3062.39
```

## 9. Ask the client first

1. Tax residence: Guadeloupe or metropolitan France (Art. 4 B tests).
2. Household parts and any overseas-specific dependants.
3. Whether Art. 197 B was applied on the prior-year notice (PAS rate inherits it).
4. Local-source vs metropolitan-source income mix for non-residents.

## 10. Sources

- [service-public.fr F1419 — barème](https://www.service-public.fr/particuliers/vosdroits/F1419) — read 2026-10-22.
- France pack `fr-personal-income-tax.md` (official pages read 19 Sep–19 Oct 2026).
- CGI Art. 197 B — [Legifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069044/) (403 on 2026-10-22; needs-sources).
