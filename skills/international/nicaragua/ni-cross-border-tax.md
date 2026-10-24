---
name: ni-cross-border-tax
description: >
  Nicaragua cross-border tax reference for 2026. Territorial system
  ("renta territorial reforzada" under Law 822): only Nicaraguan-source
  income is taxed, non-residents are taxed con o sin establecimiento
  permanente via definitive withholding (20% general, 3%
  insurance/transport/telecom, 1.5% reinsurance), no income-tax
  treaties in force, and special incentive regimes for migrants and
  pensioners (Laws 535 and 694). Covers source rules, withholding
  mechanics and deadlines, inbound and outbound posture, and the
  treaty position. Trigger on Nicaragua cross-border, territorial
  tax, non-resident withholding Nicaragua, source rules, pensioner
  regime Nicaragua. Source-cited draft.
jurisdiction: NI
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-23
version: 0.1
---

# Nicaragua cross-border tax

## 1. Who this applies to

- Non-resident individuals and companies earning Nicaraguan-source income (services used or producing effects in Nicaragua, local assets, local activities) — taxed definitively at source through resident withholding agents, "con o sin establecimiento permanente".
- Resident companies and individuals on worldwide accounting but territorial taxation: foreign-source income is outside the IR base.
- Migrants returning under Law 535 and resident pensioners/rentiers under Law 694 — import and income incentives (see §6).

## 2. Rates (with sources)

Definitive withholding on Nicaraguan-source payments to non-residents (DGI Ley 822 primer, read 2026-10-23):

| Income type | Rate |
|---|---|
| General economic-activity income (services, royalties, technical assistance, other business payments) | 20% |
| Insurance/surety premiums; maritime, air and international land passenger/cargo transport; international telephone and internet communications | 3% |
| Reinsurance | 1.5% |
| Directors' fees (dietas) | 25% (12.5% municipal councillors) |
| Severance under Art. 19(3) Law 822 | 15% |

Resident labour income: progressive rentas-del-trabajo scale to 30% top rate (see nicaragua-income-tax). Corporate: 30% net or 1%–3% minimum on gross (see ni-corporate-income-tax).

## 3. Source rules (the base)

- Law 822 applies a reinforced territorial model: Nicaraguan-source rentas are those derived from goods, services, assets, rights and any activity in Nicaraguan territory, "aun cuando dicha renta se devengue o se perciba en el exterior" — even when earned or received abroad — and regardless of physical presence.
- Donations, gratuitous transfers and debt forgiveness to a non-resident beneficiary: the resident donor/transferor withholds.
- Diplomatic and consular missions are withholding agents where no reciprocity exempts them.

## 4. Deadlines and mechanics

- Withholdings must be liquidated, declared and paid in the first five business days of the month after payment (DGI primer, 2026-10-23).
- Non-residents subject only to definitive withholding do not file an annual reconciliation for the withheld amounts.
- Resident annual returns: labour income within 45 days after year-end; corporate IR within three months of the (calendar) year-end unless an authorised alternate year-end.

## 5. Penalties and interest

- The withholding agent is the debtor if withholding is omitted or short.
- **needs-sources:** Código Tributario (Law 820) fine and interest tables did not resolve from an official PDF this pass — confirm current amounts with a Nicaraguan CPA before quoting figures.

## 6. Cross-border notes

- **Treaties:** no income-tax treaties in force per the pack overview (PwC-cited); statutory rates cannot be reduced by treaty. Official DGI/asamblea treaty list: needs-sources.
- **Law 535** (incentivos migratorios para nicaragüenses residentes en el extranjero) and **Law 694** (promoción de ingreso de residentes pensionados y rentistas): named in the Law 822 IVA import-exemption list (DGI primer) — household goods and qualifying imports exempt; income-side incentives need regime-specific review.
- Outbound: foreign-source income is not taxed; foreign tax credits are therefore largely moot — flag any foreign-branch profits for source analysis instead.
- Free-trade-zone (puertos libres) purchases: IVA-exempt under the customs regime (Law 822 Art. 127 list, via DGI primer).

## 7. Worked examples

**Example 1 — foreign consultant invoicing a Managua company.** A Costa Rican consultant invoices C$ 25,000 for services used in Nicaragua.

```oa-check
name: NI source-based WHT on consultant
inputs:
  invoice: 25000
  rate: 0.20
steps:
  - wht: invoice * rate
  - net: invoice - wht
expected:
  wht: 5000
  net: 20000
```

The consultant has no NI annual filing for this; the payer declares the C$ 5,000 within the first five business days of the next month.

**Example 2 — international telecom operator.** A foreign carrier bills a Nicaraguan company C$ 60,000 for international connectivity (3% band).

```oa-check
name: NI telecom 3% definitive WHT
inputs:
  bill: 60000
  rate: 0.03
steps:
  - wht: bill * rate
  - net: bill - wht
expected:
  wht: 1800
  net: 58200
```

## 8. Ask the client

- Residence and source facts: where the service is used, where the asset sits, where the contract is performed.
- Characterisation of each payment (service vs royalty vs transport vs insurance) — the rate band depends on it.
- Whether the client qualifies under Law 535/694 (pensioner/migrant regimes) and can document it.
- Whether any treaty the client assumes exists actually applies (answer: none in force — needs-sources caveat).

## 9. Sources

- [DGI — Dirección General de Ingresos](https://www.dgi.gob.ni) — read 2026-10-23.
- [DGI official Ley 822 primer PDF](https://www.dgi.gob.ni/pdfArchivo/22) — read 2026-10-23; territoriality language, withholding bands, deadlines, Law 535/694 and puertos libres references quoted from this document.
- [asamblea.gob.ni](https://www.asamblea.gob.ni/) — reachable 2026-10-23; consolidated Law 822 PDF 404 on known path.
- Pack skills: ni-tax-overview, ni-corporate-income-tax, nicaragua-income-tax (PwC-cited, consistent with the DGI primer).

**Source status:** rates, source rules and deadlines are official (DGI primer). Treaty list and penalty tables are needs-sources — flagged, not invented.

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
