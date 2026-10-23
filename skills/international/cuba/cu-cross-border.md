---
name: cu-cross-border
description: >
  Cuba cross-border tax reference for 2026. Covers residence and the
  worldwide-versus-source charging basis under Law No. 113 of 2012,
  non-resident taxation on Cuban-source income, withholding on dividends,
  interest and royalties to non-residents, the Ley 118 foreign-investment
  regime (15% rate, exemption periods), the absence of a published exit
  tax, and the double-tax-treaty position. Trigger on Cuba treaty,
  non-resident, withholding, expatriate, Ley 118. Source-cited draft.
jurisdiction: CU
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Cuba cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: Gaceta Oficial portal
(HTTP 200), mep.gob.cu (HTTP 200), MINJUS registry page (HTTP 200), and
the pack's existing tier-2 skills (`cu-tax-overview`,
`cu-corporate-income-tax`, `cu-income-tax`). Core statute: Ley No. 113 of
2012 (Ley del Sistema Tributario) as amended by the 2021 Tax Codes (DL 34)
and the annual State Budget Law. Currency CUP.

**Source status caveat:** the consolidated Ley 113 text and the official
in-force DTT list did not resolve from this workstation this pass
(gacetaoficial article paths 404; onat.gob.cu refused). Residence tests,
treaty partners, and outbound WHT rates are carried from the pack's tier-2
skills or marked **needs-sources** — never quote a Cuba treaty rate without
confirming the specific DTT.

## 2. Charging scope

- **Residents** are taxed on worldwide income; **non-residents** on
  Cuban-source income (carried from `cu-tax-overview`, approx — confirm
  against Ley 113 ss. on residencia).
- Cuban-source income for a non-resident includes income from Cuban
  economic activity, Cuban real property, and payments by Cuban payers for
  services used in Cuba (general pattern; article numbers **needs-sources**).
- **No exit tax** is published in the pack sources — treat as none, but
  confirm (needs-sources).

## 3. Withholding and the foreign-investment layer

| Item | Rate / rule | Source (as_of 2026-10-23) |
|---|---|---|
| Dividends to MIPYME partners | taxed in personal income tax (max marginal ~20%) | carried from `cu-corporate-income-tax` |
| Dividend WHT to foreign shareholders | not confirmed | **needs-sources** |
| Interest / royalties to non-residents | WHT may apply; rate unconfirmed | **needs-sources** |
| Foreign-investment entities | 15% Impuesto sobre Utilidades; exemption period commonly cited as 8 years | Ley 118, carried from `cu-corporate-income-tax` (approx — confirm) |
| Natural resources | up to 50% | carried from `cu-corporate-income-tax` (approx — confirm) |
| Territorial contribution for local development | 1% of gross income | carried from `cu-corporate-income-tax` (Granma, 2025) |
| DTT network | treaties exist (e.g. Spain, UK, Canada, China commonly cited) — in-force list not published at a stable official path | **needs-sources** |

## 4. Filings and deadlines

- Non-resident payers: Cuban payers withhold at source where a WHT rule
  applies; the non-resident generally has no annual Cuban return unless
  registered (confirm — needs-sources).
- Resident individuals abroad: Cuba's treatment of dual residents and the
  2-year presence style tests are **needs-sources** — the 2021 Tax Codes
  amended residence rules and the text did not resolve this pass.

## 5. Penalties and interest

General Ley 113 infractions; figures **needs-sources** (see
`cu-transfer-pricing` §5).

## 6. Worked examples

**Example 1 — foreign royalty into a Cuban JV.** A Cuban joint venture
(15% regime) pays a foreign licensor a royalty of CUP 500,000. With the
royalty deductible in Cuba and no confirmed outbound WHT, the worked figure
shows only the Cuban-side deduction effect at 15%: 500,000 × 15% =
75,000.00 of Cuban tax saved — the licensor's home-country tax must be
added once the WHT rate is confirmed (**needs-sources** flag stands).

```oa-check
name: JV royalty deduction effect CUP 500,000
inputs:
  royalty: 500000
steps:
  - cuban_saving: royalty * 0.15
expected:
  cuban_saving: 75000.00
```

**Example 2 — MIPYME partner dividend into personal tax.** A MIPYME
distributes CUP 120,000 to its resident partner; the partner's personal
income tax tops out at the ~20% marginal band cited in the pack:
120,000 × 20% = 24,000.00 (illustrative top-band figure; the progressive
scale in `cu-income-tax` governs).

```oa-check
name: Partner dividend top-band CUP 120,000
inputs:
  dividend: 120000
steps:
  - tax: dividend * 0.20
expected:
  tax: 24000.00
```

## 7. Ask the client first

1. Is the individual or entity a Cuban tax resident — and under which test
   year (2021 Tax Codes amended the rules)?
2. Is the payer a state enterprise, Ley 118 joint venture, or MIPYME?
3. Does a double tax treaty actually apply to the counterparty country —
   confirm the in-force list first.
4. Are remittables being moved at the official or the MLC exchange rate —
   the CUP conversion changes every figure.
5. Is the 1% territorial contribution being filed on the gross income that
   the cross-border flows run through?

## 8. Sources

- [Gaceta Oficial de la República de Cuba (portal)](http://www.gacetaoficial.gob.cu/) — read 2026-10-23 (HTTP 200; statute article paths 404 — needs-sources).
- [Ministerio de Economía y Planificación](https://www.mep.gob.cu/) — read 2026-10-23.
- [MINJUS — Registro Mercantil](https://www.minjus.gob.cu/es/servicios/registro-mercantil) — read 2026-10-23.
- Pack skills carried: `cu-tax-overview`, `cu-corporate-income-tax`, `cu-income-tax` (tier 2, read 2026-07-13).

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
