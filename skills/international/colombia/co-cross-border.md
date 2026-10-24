---
name: co-cross-border
description: >
  Use this skill whenever asked about Colombia cross-border taxation — tax residence, source rules, dividend/interest/royalty withholding to non-residents, the treaty network, CFC rules, exchange-control (declaración cambiaria) interaction, and outbound remittances. Trigger on phrases like "remesas Colombia", "convenio doble tributación Colombia", "CDI Colombia", "dividendo a no residente retención", "residencia fiscal Colombia", "CFC Colombia", "control cambiario DIAN", "cross-border Colombia". Tax year 2026 draft; treaty article rates are instrument-specific and flagged for verification per treaty.
jurisdiction: CO
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Colombia cross-border taxation

## 1. Who applies

- **Colombian tax residents** — taxed on worldwide income (natural persons: 183+ days in a 365-day window; entities: management place or main place of business in Colombia, ET art. 10).
- **Non-residents** — taxed on Colombian-source income only, largely through withholding.
- **Colombian companies with foreign affiliates** — CFC rules (ET arts. 871 et seq.) attribute passive income of controlled foreign entities.

## 2. Rates and thresholds

Statutory withholding on outbound payments (ET arts. 245, 408; treaties override — always check the instrument):

| Payment to non-resident | Domestic statutory rate |
|---|---|
| Dividends from taxed profits | 20% (art. 245) |
| Dividends from untaxed profits | 48% then 20% on remainder |
| Royalties, technical services, software | 20% |
| Interest | 15%–20% (5% qualifying long infrastructure loans) |

Treaty network: DIAN publishes the instruments at its [convenios tributarios internacionales page](https://www.dian.gov.co/normatividad/convenios/paginas/conveniostributariosinternacionales.aspx) (37 treaties/accord PDFs listed; Canada-2012, UK-2019, Mexico-2013 PDFs verified resolving 2026-10-24). Treaty WHT rates are instrument-specific — **verify per treaty before quoting a reduced rate**.

## 3. Base

- Source rules for services: rendered in Colombia (art. 20); royalties/intangibles: used in Colombia.
- Non-residents: no deductions on the withholding base (gross), except the taxed-dividend regime.
- Residents: worldwide base with the cédula general system (see `co-income-tax`).

## 4. Deadlines

- Withholding remittance: monthly Form 350, DIAN calendar staggered by NIT.
- Form 1042 (treaty relief request): filed before applying a reduced rate.
- Exchange-control declarations (banco de la República, inbound/outbound FX) run alongside DIAN filings — separate regime, verify current resolutions.

## 5. Penalties and interest

- Under-withheld remittances: ET arts. 667/651 penalties plus art. 635 interest (see `co-payroll-withholding`).
- Exchange-control breaches: separate fines under the external-accounting regime.

## 6. Cross-border

- MAP: available under each published treaty; DIAN administers.
- CFC: passive-income attribution where control + low-taxed entity in listed jurisdictions.
- Treaty access requires certificate of tax residence + Form 1042; without them, statutory rates apply.

## 7. Worked examples

**Example 1 — dividend to a non-resident from taxed profits.**

```oa-check
name: Dividend 500,000,000 COP, 20% WHT (no treaty claim)
inputs:
  dividend: 500000000
steps:
  - wht: dividend * 0.20
  - net: dividend - wht
expected:
  wht: 100000000
  net: 400000000
```

**Example 2 — royalty to a non-resident licensor.**

```oa-check
name: Royalty 200,000,000 COP at 20%
inputs:
  royalty: 200000000
steps:
  - wht: royalty * 0.20
expected:
  wht: 40000000
```

## 8. Ask the client

1. Residence of the recipient and treaty eligibility (certificate of residence)?
2. Characterisation of the payment — dividend, interest, royalty, service fee?
3. Was the paying company's profit taxed in Colombia (dividend regime split)?
4. Form 1042 filed before applying a treaty rate?
5. FX flows compliant with the exchange-control regime?

## 9. Sources

- [DIAN — Convenios tributarios internacionales](https://www.dian.gov.co/normatividad/convenios/paginas/conveniostributariosinternacionales.aspx) — read 2026-10-24.
- [DIAN — Convenios bilaterales](https://www.dian.gov.co/normatividad/convenios/Paginas/ConveniosBilaterales.aspx) — read 2026-10-24.
- Treaty PDFs verified resolving: [Canada 2012](https://www.dian.gov.co/normatividad/convenios/Convenios_Tributarios_Internacionales/Canada-2012.PDF), [UK 2019](https://www.dian.gov.co/normatividad/convenios/Convenios_Tributarios_Internacionales/Reino-Unido-2019.PDF), [Mexico 2013](https://www.dian.gov.co/normatividad/convenios/Convenios_Tributarios_Internacionales/Mexico-2013.PDF) — read 2026-10-24.
- ET arts. 10, 20, 245, 408, 871 — gazette text **needs-sources** (pgn.gov.co unresolved 2026-10-24); figures carried from the existing `co-corporate-income-tax` draft's citations.

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
