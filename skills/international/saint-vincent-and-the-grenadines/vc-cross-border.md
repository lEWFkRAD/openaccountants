---
name: vc-cross-border
description: >
  Saint Vincent and the Grenadines cross-border tax reference for 2026. Covers
  source-based chargeability, non-resident taxation, final withholding on
  payments to non-residents under Income Tax Act Cap. 435 section 66 (20%
  services, 10% rental, 15% CARICOM royalties/interest/management fees), the
  foreign-address presumption, foreign insurance premiums, double-tax-relief
  orders, non-resident employees on PAYE, and the absence of a statutory exit
  tax. Use for SVG inbound/outbound engagements and non-resident payment
  working papers. Independent accountant review pending.
jurisdiction: VC
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Saint Vincent and the Grenadines cross-border v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows; not reviewed for any specific person's facts. Do not file, pay, or take a position on it without review by a qualified SVG professional.

## 1. Scope and sources

SVG taxes income **accruing in or derived from SVG** regardless of the recipient's residence, and taxes residents on income from sources in or out of SVG ([IRD taxes page](https://ird.gov.vc/index.php/taxes), read 2026-10-27: PIT is "charged on income accruing to individuals from sources in or out of St. Vincent and the Grenadines"). Sources: [Income Tax Act Cap. 435 consolidated PDF](https://ird.gov.vc/images/pdf/Cap435.pdf) read 2026-10-27 (ss. 2, 66, 66A, 60; DTR orders list); [IRD taxes page WHT section](https://ird.gov.vc/index.php/taxes) read 2026-10-27. This skill covers non-resident taxation, withholding on outbound payments, treaties, and departure questions. It does not compute resident income tax (`vc-paye-withholding` for employment) or VAT on imported services (`vc-vat`).

## 2. Who applies

- **Non-resident carrying on business in SVG:** taxed on the business profits like a resident (Cap. 435; a non-resident providing independent personal services with WHT liability is the exception).
- **Non-resident with passive SVG income** (interest, rent, annuity, other annual payments, services fees): the income does **not** form part of assessable income — it is charged **final** by withholding under s.66 (Cap. 435 s.10(5) / s.66; IRD WHT table).
- **Resident individuals** remain taxable on worldwide income, including foreign pensions and remittances.
- **Payer side:** every resident person (or their agent) making a payment to a non-resident must withhold (s.66(1)). A payee at an **address outside SVG is presumed non-resident** unless the contrary is proved (s.66(2)).
- **Foreign insurance companies** not registered in SVG: premiums accruing in SVG are deemed income subject to WHT (s.66(4)); s.66A exempts classes of business not available in SVG, prescribed by Ministerial order.

## 3. Rates and base

Withholding on payments to non-residents ([IRD taxes page](https://ird.gov.vc/index.php/taxes), read 2026-10-27; base = gross payment unless stated):

| Payment category | WHT rate |
|---|---|
| Standard rate on services | 20% |
| Rental | 10% |
| Royalties, interest, management fees — payee resident in CARICOM | 15% |
| Withdrawal benefits from approved pension funds | rate in s.65(13) (**needs-sources:** current percentage not retrievable 2026-10-27) |

The Comptroller may direct a **lower** rate where the payee is resident in a treaty country with a lower rate (s.66(3)). Withholding is a **full discharge** for the passive categories — no SVG return for that income.

**Exit tax:** no statutory departure/exit charge was found in Cap. 435 (consolidated PDF read 2026-10-27). **needs-sources:** absence confirmed only against the consolidated text, not against post-2020 amendments on finance.gov.vc (503 on 2026-10-27).

## 4. Deadlines

- **WHT remittance:** file and pay on or before the **15th of the month following** the month of withholding ([IRD taxes page](https://ird.gov.vc/index.php/taxes), read 2026-10-27).
- Non-resident **business** filers follow the ordinary calendar: PIT return 31 March; CIT return 3 months after FY end.
- Failure to pay withheld amounts within the prescribed time is a TAA offence (Cap. 435 penalty provisions; TAA 2019 penalty table on the [IRD non-compliance page](https://ird.gov.vc/index.php/non-compliance), read 2026-10-27).

## 5. Penalties and interest

- Late filing: greater of 5% + 1%/month of tax, or $500 + $100/month, capped $10,000 (TAA s.75).
- Late payment of withheld WHT: 20% (TAA s.76); interest 1.5% monthly.
- The payer — not the non-resident payee — carries the deduction and remittance liability; failure to withhold does not extinguish the payee's tax but exposes the payer to the full amount plus penalties.
- Deduction for the payment is **blocked** until the WHT is paid (Cap. 435 s.13(2)) — see `vc-transfer-pricing`.

## 6. Cross-border (treaties and residence)

Cap. 435's subsidiary-legislation list carries Double Taxation Relief orders for the **United Kingdom, Canada, Sweden, Norway, Denmark, USA, New Zealand and Switzerland** (consolidated PDF, read 2026-10-27). **needs-sources:** in-force status and current articles of each order not verified — several predate 2000; check before relying. Treaty mechanics in the orders follow the PE/attributed-profits pattern (associated-enterprise and arm's-length attribution language appears in the UK order text in the Cap. 435 PDF). CARICOM residents get the reduced 15% on royalties/interest/management fees by domestic law, not treaty. No exit tax; departure from SVG residence has no filing trigger beyond the ordinary 31 March return for the year of departure.

## 7. Worked examples

**Example 1 — non-resident consultant paid by an SVG company.** Gross fee EC$12,000, consultant resident outside CARICOM.

```oa-check
name: services WHT to non-CARICOM consultant
inputs:
  fee: 12000
  wht: 0.20
steps:
  - withheld: fee * wht
  - net_paid: fee - withheld
expected:
  withheld: 2400
  net_paid: 9600
```

The SVG payer remits 2,400 by the 15th of the following month; the consultant owes no further SVG tax (final withholding).

**Example 2 — CARICOM licensor receiving royalties.** Monthly royalty EC$4,000 to a Trinidad resident.

```oa-check
name: CARICOM royalty WHT, one year
inputs:
  monthly: 4000
  months: 12
  wht: 0.15
steps:
  - annual: monthly * months
  - wht_annual: annual * wht
  - net_annual: annual - wht_annual
expected:
  annual: 48000
  wht_annual: 7200
  net_annual: 40800
```

## 8. Ask the client

- Residence and address of every payee — the foreign-address presumption decides withholding.
- Whether the payee is CARICOM-resident (15% category) and can evidence it.
- Whether any treaty rate reduction has been **directed by the Comptroller** — do not self-apply a treaty rate.
- Insurance premiums paid to foreign insurers and whether the class falls under a s.66A order.
- For departing residents: worldwide income continues to be taxable while resident; confirm the departure date and where the new residence taxes the same income.

## 9. Sources

- [Income Tax Act Cap. 435 (consolidated PDF) — ss. 2, 10, 13, 60, 66, 66A, DTR orders](https://ird.gov.vc/images/pdf/Cap435.pdf) — read 2026-10-27
- [IRD — Taxes (WHT categories and rates, deadlines, interest)](https://ird.gov.vc/index.php/taxes) — read 2026-10-27
- [IRD — Non-Compliance (TAA 2019 penalties)](https://ird.gov.vc/index.php/non-compliance) — read 2026-10-27
- [IRD — Legislation](https://ird.gov.vc/index.php/legislation) — read 2026-10-27
- [Finance Act No. 10 of 2023 (PDF)](https://finance.gov.vc/finance/images/PDF/Acts/Finance_Act_No_10_of_2023_30_to_28_tax_rate_001.pdf) — HTTP 503 on 2026-10-27 (source status caveat)

<!-- openaccountants-cta-block -->

**Talk to a verified accountant** — this skill is a source-cited draft (tier 2). For SVG cross-border work under professional review, book time with an OpenAccountants verified accountant: [Calendly](https://www.openaccountants.com).
