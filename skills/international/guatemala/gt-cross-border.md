---
name: gt-cross-border
description: >
  Guatemala cross-border tax reference for 2026. Covers Guatemalan-source
  taxation of non-residents, outbound withholding rates on dividends,
  interest, royalties and technical fees under the Ley de Actualizacion
  Tributaria (Decreto 10-2012), the narrow in-force double-taxation
  treaty network, the no-territorial-exit-tax position, and the
  interaction with the related-party anexo. Trigger on Guatemala
  cross-border, non-resident, withholding, treaty, convenio, no
  residentes, salida. Source-cited draft.
jurisdiction: GT
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Guatemala cross-border

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: SAT's
Acuerdos y Tratados Internacionales page (trade agreements; the
income-tax CDI list is not published there in machine-readable form),
SAT's statute PDF library, and the existing Guatemala corporate and
income skills (withholding figures carried forward with their citations).
Currency is the quetzal (GTQ).

**Source status caveat:** Guatemala publishes no consolidated,
machine-readable register of in-force income-tax conventions on the SAT
portal read this pass. The treaty inventory below is **needs-sources** —
confirm each convention's status and effective date with SAT or the
Ministerio de Relaciones Exteriores before relying on it.

## 2. Who this applies to

- **Non-residents with Guatemalan-source income.** Guatemala taxes
  non-residents on Guatemalan-source income only, generally through
  final withholding (Rentas de No Residentes, Libro I, Decreto 10-2012).
- **Guatemalan residents investing abroad.** Worldwide income applies to
  residents under the general regime; foreign-source dividends, interest
  and capital gains are in the Rentas de Capital category.
- **Payers acting as withholding agents** — Guatemalan companies and
  permanent establishments must withhold and remit through the SAT
  Sistema de Retenciones Web (including the no-residentes module on the
  SAT portal).

## 3. Withholding and outbound payments (rates table)

| Payment to non-residents | Rate | Character | Source |
|---|---|---|---|
| Dividends / profit distributions | 5% | final | Decreto 10-2012, Libro I, Rentas de No Residentes (see gt-corporate-income-tax; some guides cite up to 10% — confirm) |
| Interest | 10% | final | as above |
| Royalties, technical and professional fees | 15% | final | as above |
| Technical assistance / know-how | 10% | final | needs-sources (article-level confirmation) |
| Travel / transport tickets sold in Guatemala | 5% | final | needs-sources |
| Capital gains on Guatemalan assets | 10% on gross (approx) | final | needs-sources |

No withholding arises on payments for services performed wholly outside
Guatemala where no Guatemalan source exists — source rules are
article-level, **needs-sources**.

## 4. Treaty network

- Guatemala's income-tax treaty network is very narrow. A convention
  with Spain is the commonly cited in-force CDI; conventions with Taiwan
  and Chile have been reported as signed/in force at various times. The
  consolidated list: **needs-sources**.
- SAT's Acuerdos y Tratados Internacionales page covers free-trade and
  customs instruments (TLCs, Kyoto Convention, TRIPS), not a CDI
  register — do not read treaty relief from those pages.
- Treaty relief, where available, is applied at source by the Guatemalan
  payer with SAT-issued certification; absent certification the
  domestic rate above applies.

## 5. Exit and departure

- Guatemala imposes **no exit tax / departure tax** on individuals or
  companies ceasing Guatemalan residence — the source-based system
  simply stops taxing after departure (no confirmed statutory exit
  charge; needs-sources for any residual liquidation rules).
- Capital gains on Guatemalan immovables and shares in Guatemalan
  companies remain Guatemalan-source after departure.

## 6. Permanent establishment and residence

- A non-resident operating through a fixed place of business in
  Guatemala is assessed like a resident under the general regime (25%),
  with the branch's after-tax profits subject to the 5% dividend WHT on
  remittance (needs-sources for the remittance trigger mechanics).
- Guatemalan companies are resident where incorporated or where their
  effective management sits in Guatemala (article text needs-sources).

## 7. Interaction with transfer pricing

Related-party payments to non-residents carry both the WHT above and the
Chapter VI valuation rules (see gt-transfer-pricing). Revaluations change
the ISR base but do not refund WHT already borne — with almost no treaty
relief, double charge on mispriced royalties is the default risk.

## 8. Worked examples

**Example 1 — royalty to a foreign affiliate.** A Guatemalan company
pays a GTQ 500,000 royalty to its Canadian parent. Final WHT at 15% =
GTQ 75,000; the affiliate nets GTQ 425,000. No treaty relief assumed
(Canada-Guatemala CDI not confirmed).

```oa-check
name: royalty WHT GTQ 500k
inputs:
  gross: 500000
  rate: 0.15
steps:
  - wht: gross * rate
  - net: gross - wht
expected:
  wht: 75000.00
  net: 425000.00
```

**Example 2 — dividend remittance.** A Guatemalan S.A. distributes GTQ
1,200,000 of after-tax profits to its non-resident shareholder. Final
dividend WHT at 5% = GTQ 60,000.

```oa-check
name: dividend WHT GTQ 1.2m
inputs:
  distribution: 1200000
  rate: 0.05
steps:
  - wht: distribution * rate
expected:
  wht: 60000.00
```

## 9. Ask the client first

1. Is the payment Guatemalan-source — where were the services performed,
   where is the asset located, where is the payer established?
2. Which withholding rate applies to the payment character, and was it
   withheld, remitted, and the receipt (constancia) obtained?
3. Does any in-force CDI cover the counterparty's residence — and is the
   certification in hand before payment?
4. Is the counterparty related — if so, run the transfer-pricing check
   (gt-transfer-pricing) before filing the anexo.

## 10. Sources

- [Portal SAT — Acuerdos y Tratados Internacionales](https://portal.sat.gob.gt/portal/acuerdos-y-tratados-internacionales/) — read 2026-10-23 (trade/customs instruments; CDI register needs-sources).
- [Portal SAT — Legislacion Tributaria](https://portal.sat.gob.gt/portal/biblioteca-en-linea-sat/legislacion-tributaria/) — read 2026-10-23.
- [Codigo Tributario, Decreto 6-91 (SAT PDF)](https://portal.sat.gob.gt/portal/descarga/1899/legislacion-tributaria/18255/codigo-tributario-decreto-numero-6-91) — read 2026-10-23.
- [Portal SAT — home](https://portal.sat.gob.gt/portal/) — read 2026-10-23.
- Existing pack skills `gt-corporate-income-tax` and `guatemala-income-tax` — withholding figures carried forward with their PwC citations pending statute-level confirmation.

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
