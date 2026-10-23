---
name: mq-income-tax-individuals
description: >
  Martinique individual income tax reference for 2026. Martinique applies the
  French progressive barème (0–45%, 2025 revenues: bands 11,600 / 29,579 /
  84,577 / 181,917 EUR) with the overseas reduction under CGI Art. 197 B.
  Covers who is liable, the barème, the Art. 197 B reduction, quotient
  familial, filing and PAYE deadlines, penalties. Source-cited draft; the
  Art. 197 B rate and cap need Legifrance re-verification (needs-sources).
jurisdiction: MQ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Martinique individual income tax

## 1. Scope and sources

Martinique is a French department: the Code général des impôts applies as in metropolitan France with the overseas adaptations below. Barème figures read from service-public.fr F1419 on 2026-10-22 (revenus 2025, impôt 2026), matching the France pack (`fr-personal-income-tax.md`, official pages read 19 Sep–19 Oct 2026). legifrance.gouv.fr returned HTTP 403 to this host on 2026-10-22 — Art. 197 B details flagged needs-sources.

## 2. Who is liable

French tax-residence rules (CGI Art. 4 B) apply unchanged: home, centre of economic interests, or professional activity in Martinique. Residents: worldwide income. Non-residents: French-source income only.

## 3. Rates — barème 2026 (revenus 2025)

| Band (per part) | Rate | Source |
|---|---:|---|
| Up to €11,600 | 0% | [service-public.fr F1419](https://www.service-public.fr/particuliers/vosdroits/F1419), read 2026-10-22 |
| €11,601 – 29,579 | 11% | same |
| €29,580 – 84,577 | 30% | same |
| €84,578 – 181,917 | 41% | same |
| Above €181,917 | 45% | same |

## 4. The overseas reduction (CGI Art. 197 B)

Income tax for Martinique-resident households is reduced by a fixed percentage under Art. 197 B CGI, subject to an annual cap. **Needs-sources: current percentage and cap not re-readable from Legifrance on 2026-10-22 (403); the widely applied figure is 40% capped at €6,350 single / €12,700 joint — verify before use.**

## 5. Base and quotient familial

Identical to metropolitan France: 10% employment deduction (minimum and ceiling apply), quotient familial parts, décote. See `fr-personal-income-tax.md`.

## 6. Deadlines

- Annual return (2042): spring online campaign per the DGFiP calendar.
- PAS: monthly withholding at source, rate set from the prior return — see `mq-payroll-withholding`.

## 7. Penalties and interest

Late filing 10% (Art. 1728 CGI), 40% after 30-day notice, 80% for evasion; interest in arrears at the legal rate (Art. 1727).

## 8. Worked examples

**Example 1 — single, net taxable €40,000.**
Band 2: (29,579 − 11,600) × 11% = 1,977.69. Band 3: (40,000 − 29,579) × 30% = 3,126.30. Gross 5,103.99 before Art. 197 B.

```oa-check
name: Single net taxable EUR 40,000 barème 2026
inputs:
  income: 40000
steps:
  - band2: (min(income, 29579) - 11600) * 0.11
  - band3: (income - 29579) * 0.30
  - tax: max(band2, 0) + max(band3, 0)
expected:
  tax: 5103.99
```

**Example 2 — Art. 197 B at the commonly applied 40% (unverified).**
5,103.99 × 40% = 2,041.60; net 3,062.39.

```oa-check
name: Art 197 B at 40 percent rate needs-sources
inputs:
  gross_tax: 5103.99
steps:
  - reduction: gross_tax * 0.40
  - net: gross_tax - reduction
expected:
  net: 3062.39
```

## 9. Ask the client first

1. Residence: Martinique or metropole (Art. 4 B).
2. Household parts.
3. Whether Art. 197 B appears on the prior-year notice (PAS inherits it).
4. Metropole-source income for non-residents.

## 10. Sources

- [service-public.fr F1419](https://www.service-public.fr/particuliers/vosdroits/F1419) — read 2026-10-22.
- France pack `fr-personal-income-tax.md` (official pages read 19 Sep–19 Oct 2026).
- CGI Art. 197 B — [Legifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069044/) (403 on 2026-10-22; needs-sources).
