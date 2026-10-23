---
name: gt-transfer-pricing
description: >
  Guatemala transfer pricing reference for 2026. Covers the special
  valuation rules between related parties in Libro I, Chapter VI of the
  Ley de Actualizacion Tributaria (Decreto 10-2012), the arm's-length
  methods recognised by SAT, the related-party annex to the annual ISR
  return (Anexo a la Declaracion Jurada Anual del ISR sobre partes
  relacionadas) filed through Agencia Virtual, SAT's technical guide for
  transfer pricing studies, and the interaction with the 25% general
  corporate regime and non-resident withholding. Trigger on Guatemala
  transfer pricing, precios de transferencia, partes relacionadas,
  anexo ISR, valoracion, SAT fiscalizacion. Source-cited draft.
jurisdiction: GT
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Guatemala transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: SAT's Precios de
Transferencia portal page (which states the legal basis and the filing
route), SAT's Legislacion Tributaria PDF library (Codigo Tributario
Decreto 6-91 and the Reglamento del Libro I, Acuerdo Gubernativo 213-2013,
both served as PDFs), and the existing Guatemala corporate-income skill.
Currency is the quetzal (GTQ).

**Source status caveat:** the full in-force text of Decreto 10-2012
Libro I, Chapter VI (Normas Especiales de Valoracion entre Partes
Relacionadas) and the current anexo filing deadline mechanics were not
read at statute level in this pass — SAT's statute library is a
JavaScript-rendered search page. Article numbers, the exact anexo
deadline, and documentation thresholds are therefore **needs-sources**:
confirm against the Decreto 10-2012 PDF and the annual SAT anexo
instructivo before tier-1 promotion.

## 2. Who the rules apply to

- **Related-party transactions of Guatemalan taxpayers.** The rules sit in
  Libro I, Chapter VI of the Ley de Actualizacion Tributaria (Decreto
  10-2012) — "Normas Especiales de Valoracion entre Partes Relacionadas"
  — and apply to transactions between a Guatemalan taxpayer and related
  parties, including non-resident related parties, where Guatemalan
  income tax is affected.
- **Anexo filers.** SAT publishes, inside Agencia Virtual (Servicios de
  Fiscalizacion > Precios de Transferencia > Anexo del ISR), the Anexo a
  la Declaracion Jurada Anual del Impuesto Sobre la Renta, Sobre Partes
  Relacionadas. Taxpayers with covered related-party transactions file it
  with the annual ISR return.
- **No country-by-country reporting regime** has been confirmed in this
  pass — **needs-sources**.

## 3. The rules (methods and documentation table)

| Rule | Content | Source |
|---|---|---|
| Legal basis | Special valuation rules between related parties, Libro I, Chapter VI, Decreto No. 10-2012 del Congreso de la Republica de Guatemala | SAT — Precios de Transferencia page (states the chapter expressly) |
| Arm's-length requirement | Related-party transactions must be valued as between independent parties in comparable circumstances; SAT may revalue and assess the difference | Decreto 10-2012, Libro I, Cap. VI (article text needs-sources) |
| Recognised methods | OECD-aligned methods (comparable uncontrolled price, resale price, cost plus, transactional profit methods) per SAT's Guia Tecnica de Estudios de Precios de Transferencia | SAT — Precios de Transferencia page (Guia Tecnica link) |
| Documentation | Estudio de Precios de Transferencia following SAT's suggested guide; the anexo to the annual ISR return reports related-party transactions | SAT — Precios de Transferencia page |
| Filing route | Agencia Virtual > Servicios de Fiscalizacion > Precios de Transferencia > Anexo del ISR | SAT — Precios de Transferencia page (instructivo) |
| Corporate rate the adjustment feeds | 25% general regime (Regimen Sobre las Utilidades) | Decreto 10-2012, Libro I (see gt-corporate-income-tax) |

## 4. Tax base and computation

A transfer-pricing revaluation enters the general-regime ISR base: SAT
recomputes the Guatemalan taxpayer's income as if the related-party price
had been the arm's-length price, then assesses 25% ISR on the uplift plus
interest for the period (mora plus resarcitorio — see gt-corporate-income-tax
penalties notes). Offsets can arise where the counterparty is a non-resident:
Guatemala may deny the deduction or revalue the outbound payment.

## 5. Deadlines

- **Annual ISR return (general regime):** 31 March following a 31 December
  year-end (see gt-corporate-income-tax).
- **Related-party anexo:** filed with the annual ISR return through
  Agencia Virtual; the exact anexo deadline for the current tax year is
  set by SAT each cycle — **needs-sources**.
- **Estudio:** contemporaneous documentation expected on request during
  fiscalizacion; no confirmed statutory preparation deadline —
  **needs-sources**.

## 6. Penalties and interest

Under the Codigo Tributario (Decreto 6-91, PDF in SAT's library):
under-assessment from a revaluation attracts interest (0.005 per day mora
plus the resarcitorio rate on unpaid tax, per the existing Guatemala
skills), and specific fines apply for failure to file informative
declarations. Exact anexo-specific fine amounts: **needs-sources**.

## 7. Cross-border interaction

Most Guatemalan transfer-pricing exposure pairs with the non-resident
withholding regime: royalties and technical fees paid to related
non-residents carry 15% final WHT, interest 10%, dividends 5% (see
gt-cross-border). A revaluation of an inbound royalty therefore changes
both the ISR base and the WHT already withheld. Guatemala's narrow treaty
network rarely relieves the double charge.

## 8. Worked examples

**Example 1 — inbound goods underpricing.** A Guatemalan distributor buys
from its US parent at GTQ 1,400,000 when the arm's-length price is GTQ
2,000,000. SAT revalues the cost base down by GTQ 600,000; additional ISR
at 25% = GTQ 150,000.

```oa-check
name: revaluation uplift GTQ 600k
inputs:
  arm_length: 2000000
  price: 1400000
steps:
  - uplift: arm_length - price
  - isr: uplift * 0.25
expected:
  isr: 150000.00
```

**Example 2 — outbound royalty overpricing.** A Guatemalan licensee pays
its foreign affiliate a GTQ 800,000 royalty; SAT accepts only GTQ
500,000 as arm's length. The GTQ 300,000 excess is non-deductible; ISR
uplift at 25% = GTQ 75,000 (the 15% WHT already withheld on the full
royalty is a separate final charge).

```oa-check
name: royalty disallowance GTQ 300k
inputs:
  royalty_paid: 800000
  arm_length: 500000
steps:
  - disallowed: royalty_paid - arm_length
  - isr: disallowed * 0.25
expected:
  isr: 75000.00
```

## 9. Ask the client first

1. Which related-party transactions (goods, services, royalties,
   financing) crossed the border in the tax year?
2. Is a current estudio on hand following SAT's Guia Tecnica, and was
   the anexo filed with the ISR return through Agencia Virtual?
3. Are the two sides of each transaction recorded at the same amount and
   price in both countries?
4. Was WHT (10%/15%/5%) withheld and paid on the related-party payments —
   receipts available for SAT?

## 10. Sources

- [Portal SAT — Precios de Transferencia](https://portal.sat.gob.gt/portal/precios-de-transferencia/) — legal basis (Libro I, Cap. VI, Decreto 10-2012), anexo filing route, Guia Tecnica; read 2026-10-23.
- [Portal SAT — Legislacion Tributaria](https://portal.sat.gob.gt/portal/biblioteca-en-linea-sat/legislacion-tributaria/) — statute PDF library; read 2026-10-23.
- [Codigo Tributario, Decreto 6-91 (SAT PDF)](https://portal.sat.gob.gt/portal/descarga/1899/legislacion-tributaria/18255/codigo-tributario-decreto-numero-6-91) — read 2026-10-23.
- [Reglamento del Libro I, AG 213-2013 (SAT PDF)](https://portal.sat.gob.gt/portal/descarga/1899/legislacion-tributaria/18250/acuerdo-gubernativo-numero-213-2013-reglamento-del-libro-i-de-la-ley-de-actualizacion-tributaria-decreto-numero-10-2012-del-congreso-de-la-republica-de-guatemala-que-establece-el-impuesto-sobre-la-r) — read 2026-10-23.
- [Portal SAT — home](https://portal.sat.gob.gt/portal/) — read 2026-10-23.

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
