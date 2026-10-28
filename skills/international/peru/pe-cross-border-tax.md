---
name: pe-cross-border-tax
description: >
  Peru cross-border tax reference for 2026. Domiciled taxpayers are
  taxed on worldwide income; non-domiciled only on Peruvian-source
  income, defined by the use-economically-in-Peru rules of Income Tax
  Law Arts. 9-10 (technical assistance, royalties, capital placement).
  Non-resident rates: 5% dividends, 5% real-estate capital gains, 5%
  interest (30% when linked or via tax havens), 29.5% branch income,
  deemed branch-profit distribution at the annual-return date. Covers
  domicile tests (Arts. 7-8), source rules, remittance mechanics and
  the treaty position. Trigger on Peru cross-border, no domiciliado,
  dividend withholding Peru, branch profits Peru, fuente peruana.
  Source-cited draft.
jurisdiction: PE
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-28
version: 0.2
---

# Peru cross-border tax

## 1. Who this applies to

- **Domiciled** companies and individuals: worldwide income (Art. 6, TUO chapter PDF read 2026-10-23).
- **Non-domiciled** persons, branches, agencies and permanent establishments of foreign entities: Peruvian-source income only (Art. 6 second paragraph, as amended by D.L. 1424).
- Individuals relocating in or out: domicile is judged at the start of each tax year; mid-year changes take effect the following year, except that a natural person loses domicile on departure when the Art. 7 second-paragraph conditions are met (Arts. 7–8, read 2026-10-23).

## 2. Rates (with sources)

Non-domiciled natural persons and estates on Peruvian-source income (Art. 54, Cap. VII TUO PDF, read 2026-10-23):

| Peruvian-source income | Rate |
|---|---|
| Dividends and other profit distributions | 5% |
| Capital gains from real estate | 5% |
| Interest paid by a domiciled third-category generator | 5% — **30%** when the parties are linked or the payment derives from/via non-cooperative or low-tax jurisdictions (D.L. 1381 text) |

Other cross-border rates:

| Item | Rate | Source |
|---|---|---|
| Domiciled companies (branch-equivalent third-category) | 29.5% | Art. 55 (read 2026-10-23) |
| Non-domiciled companies: dividends and PE profit remittance | 5% | Art. 56 (Cap. VII TUO PDF) |
| Hidden distributions (Art. 24-A(g)) | +5% additional on those sums | Art. 55 final paragraph (read 2026-10-23) |

## 3. Source rules (the base)

Arts. 9–10 (Cap. II TUO PDF, read 2026-10-23) — Peruvian-source rentas regardless of the parties' nationality, domicile, or where the contract is signed:

- Real estate and assets in Peru; rights used in Peru.
- **Technical assistance: source when used economically in the country** (Art. 9(j)).
- **Royalties: source when the underlying goods/rights are used economically in Peru or the payer is domiciled** (Art. 9, Art. 27 link).
- **Capital: interest when the capital is placed or used economically in Peru, or the payer is domiciled** (Art. 9(c)).
- Business activities carried out in national territory (Art. 9(e)); personal work performed in territory (Art. 9(f)) — with a carve-out for non-domiciled natural persons briefly present for pre-investment, supervision, data gathering, hiring, or contract-signing acts.
- Shares in Peruvian-constituted entities (Art. 9(h)); derivatives rules in Art. 10.

## 4. Deadlines and mechanics

- **Branch profits:** a PE of a foreign entity is deemed to distribute profits on the due date of its annual IR return; the distribution base is the branch's net income plus exempt interest and available dividends minus Peruvian tax paid (Art. 55 paragraph, read 2026-10-23). The 5% remittance rate then applies.
- Withholdings on non-resident payments are declared monthly (PLAME) and the annual return reconciles (March–April per SUNAT calendar; **needs-sources:** exact 2026 dates are annual resolutions).
- SUNAT's DTT (convenios) campaign page did not resolve this pass — **needs-sources** for the treaty list and relief procedures.

## 5. Penalties and interest

- Underpaid tax: ITMC interest daily-compounded from due date (Tax Code Art. 176, read 2026-10-23).
- Formal infractions (missing declarations/support): Tax Code Art. 210 graduated fines; base 40% of UIT where no other base applies (read 2026-10-23).
- Coercive collection on exigible debt (Art. 115).

## 6. Cross-border notes

- **Treaties:** Peru's DTT network (Spain, Chile, China, Japan, etc. per secondary sources) — official SUNAT/Ministry list needs-sources; do not apply treaty reductions without confirming the counterparty treaty is in force.
- Temporary-presence carve-out (Art. 9(f)) keeps pre-investment and supervision travel out of Peruvian source — document the purpose of each trip.
- Outbound: domiciled persons pay Peruvian IR on worldwide income; dividends from domiciled companies to domiciled individuals are taxed at 9.3% (2019 onward, Art. 55(e), read 2026-10-23) — foreign-source dividend treatment needs case-by-case analysis.
- Tax-haven and non-cooperative jurisdiction status escalates interest WHT to 30% and interacts with TP rules (see pe-transfer-pricing).

## 7. Worked examples

**Example 1 — dividend to a non-domiciled company.** A Lima S.A.C. distributes S/ 1,000,000 profit to its Chilean parent (no treaty relief assumed).

```oa-check
name: PE dividend WHT non-domiciled company
inputs:
  dividend: 1000000
  rate: 0.05
steps:
  - wht: dividend * rate
  - net: dividend - wht
expected:
  wht: 50000
  net: 950000
```

**Example 2 — branch deemed distribution.** A foreign company's Lima branch has net income S/ 900,000, exempt interest S/ 100,000, available dividends S/ 50,000, and paid Peruvian IR of S/ 296,500. Deemed distribution base, then 5% remittance.

```oa-check
name: PE branch deemed profit distribution
inputs:
  net_income: 900000
  exempt_interest: 100000
  available_dividends: 50000
  tax_paid: 296500
  rate: 0.05
steps:
  - base: net_income + exempt_interest + available_dividends - tax_paid
  - remittance_tax: base * rate
expected:
  base: 753500
  remittance_tax: 37675
```

## 8. Ask the client

- Domicile facts at January 1 of the tax year (Art. 7/8 tests) — nationality, residence, centre of vital interests.
- Where services/assistance are actually used (the use-economically test drives source).
- Whether the counterparty jurisdiction is on Peru's low-tax/non-cooperative list (30% interest rate trigger).
- Treaty status of the counterparty — confirm in-force status before reducing any rate.

## 9. Sources

- [SUNAT — Ley del Impuesto a la Renta, Cap. II (Arts. 6–10 domicile and source)](https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf) — read 2026-10-23.
- [SUNAT — Ley del Impuesto a la Renta, Cap. VII (Arts. 53–56 rates)](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf) — read 2026-10-23 (5% dividends, 5%/30% interest, 29.5%, branch deemed distribution).
- [SUNAT — Código Tributario, Libro segundo](https://www.sunat.gob.pe/legislacion/codigo/libro2/libro.pdf) and [Libro cuarto](https://www.sunat.gob.pe/legislacion/codigo/libro4/libro.pdf) — read 2026-10-23.
- [SUNAT — convenios DTT campaign page](https://www.sunat.gob.pe/campaigns/convenios-para-evitar-la-doble-tributacion/index.html) — did not resolve 2026-10-23 (needs-sources).

**Source status:** source rules, domicile tests, non-resident rates and branch mechanics are official (TUO chapter PDFs). Treaty list and 2026 calendar dates are needs-sources — flagged, not invented.

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
