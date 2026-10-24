---
name: ni-transfer-pricing
description: >
  Nicaragua transfer pricing reference for 2026. Law 822 (Ley de
  Concertación Tributaria) has no dedicated transfer-pricing chapter or
  documentation regime; pricing between related parties is policed
  through the market-value and substance rules of the Código Tributario
  (Law 820), the withholding schedule that applies definitive rates to
  non-residents, and DGI audit powers. Covers the withholding rates
  that bite on cross-border related-party charges (20% general
  non-resident rate, 3% insurance/transport/telecom, 1.5%
  reinsurance), withholding-on-account rates, payment deadlines, and
  the DGI's assessment toolkit. Trigger on Nicaragua transfer
  pricing, partes vinculadas, precio de transferencia, DGI
  related-party, retención no residente. Source-cited draft.
jurisdiction: NI
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-23
version: 0.1
---

# Nicaragua transfer pricing

## 1. Who this applies to

- Resident companies (IR de rentas de actividades económicas, 30% rate or 1%–3% definitive minimum tax on gross) that buy from or sell to non-resident affiliates — management fees, royalties, interest, goods transfers.
- Non-residents receiving Nicaraguan-source income: the withholding agent (resident payer) applies definitive rates; there is no separate TP filing, so related-party pricing risk lands on the resident payer's deductibility and the non-resident's definitive WHT.
- Law 822 taxes non-residents "con o sin establecimiento permanente" (with or without a permanent establishment) — the PE label does not change the WHT exposure.

## 2. Rates (with sources)

Definitive withholding on payments to non-residents (read from the DGI's official Ley 822 primer, 2026-10-23):

| Payment to non-resident | Rate |
|---|---|
| General economic-activity payments (services, royalties, technical assistance) | 20% |
| Reinsurance | 1.5% |
| Insurance and surety premiums; maritime/air cargo and passenger transport, international land passenger transport; international telephone and internet communications | 3% |
| Directors' fees (dietas) | 25% (12.5% municipal councillors) |
| Severance under Art. 19(3) Law 822 | 15% |

Withholding on account (a cuenta, creditable) — resident-to-resident: 1.5% card-payment sales; 3% agricultural purchases; 5% per cubic metre of logs; 10% professional/technical services and occasional imports above US$2,000; minimum C$1,000 per invoice.

Corporate rate context: 30% net or 1%–3% minimum tax on gross (see ni-corporate-income-tax).

## 3. The base: no statutory TP methods list

- Law 822 as read in the DGI primer contains no dedicated transfer-pricing article or OECD-methods list; the DGI polices related-party pricing through general valuation and substance rules (Código Tributario, Law 820) and audit adjustments to market value.
- **needs-sources:** the exact Ley 822 / Law 820 article numbers for the market-value rule did not resolve from an official PDF this pass (asamblea.gob.ni 404s, Normaweb Lotus database timed out from this network). Do not cite an article number until a CPA confirms it.
- Practical posture: document prices with independent comparables; the 20% definitive WHT on services/royalties/interest to affiliates is the first-line collection mechanism and the DGI's audit lever.

## 4. Deadlines and mechanics

- Withholdings (definitive and on account) must be liquidated, declared and paid in the **first five business days of the month following** the payment (DGI primer, read 2026-10-23).
- Monthly IR advance declarations for economic-activity income; annual corporate return within three months of year-end (calendar year; alternate year-ends by authorisation — see ni-tax-overview).
- Annual labour-income return: within 45 days after year-end.

## 5. Penalties and interest

- **needs-sources:** the Código Tributario (Law 820) penalty and interest table did not resolve from an official source this pass. DGI practice applies statutory interest on underpayments and fines for undeclared/underpaid amounts; confirm current figures with a Nicaraguan CPA before quoting.
- Withholding agents who fail to withhold remain liable for the tax as debtor.

## 6. Cross-border notes

- Territorial system ("renta territorial reforzada"): only Nicaraguan-source income is taxed; source is where the good/service produces effects in Nicaragua, even if paid abroad.
- No income-tax treaties in force per the pack's existing overview (PwC-sourced; official list needs-sources) — statutory WHT rates cannot be reduced by treaty.
- Diplomatic/consular missions pay withholding unless reciprocity exempts.

## 7. Worked examples

**Example 1 — management fee to non-resident parent.** A Managua company pays its Guatemalan parent C$ 40,000 for administrative services. Definitive WHT 20%.

```oa-check
name: NI non-resident services WHT
inputs:
  fee: 40000
  rate: 0.20
steps:
  - wht: fee * rate
  - net: fee - wht
expected:
  wht: 8000
  net: 32000
```

The C$ 8,000 is due in the first five business days of the following month.

**Example 2 — related-party goods sale, withholding on account.** A distributor buys goods from a linked importer for C$ 50,000 invoiced; the transaction carries the 10% professional/technical on-account rate analogue the DGI applies to service-heavy invoices above the C$ 1,000 minimum.

```oa-check
name: NI on-account withholding credit
inputs:
  invoice: 50000
  rate: 0.10
steps:
  - withheld: invoice * rate
expected:
  withheld: 5000
```

The C$ 5,000 is creditable against the buyer's monthly IR advances — track it, it is not definitive.

## 8. Ask the client

- Full list of payments to non-resident affiliates with amounts, nature (service, royalty, interest, transport, insurance) — the rate band depends on characterisation.
- Whether the affiliate has a PE in Nicaragua (does not change WHT but changes filing duties).
- Comparables for intercompany prices: quotes, benchmarking, contracts showing substance.
- Whether withholding was actually paid on time (agent liability if not).

## 9. Sources

- [DGI — Dirección General de Ingresos](https://www.dgi.gob.ni) — read 2026-10-23 (JS portal; statute PDFs not directly linkable this pass).
- [DGI official Ley 822 primer PDF](https://www.dgi.gob.ni/pdfArchivo/22) — read 2026-10-23; withholding tables, deadlines, territoriality language quoted from this document.
- [asamblea.gob.ni](https://www.asamblea.gob.ni/) — reachable 2026-10-23; Ley 822 consolidated PDF did not resolve (404 on known path; Normaweb database timed out).
- Existing pack skills: ni-corporate-income-tax, ni-tax-overview (PwC-cited rates, consistent with the DGI primer).

**Source status:** withholding rates and deadlines are official (DGI primer). TP article numbers and penalty/interest figures are needs-sources — flagged above, not invented.

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
