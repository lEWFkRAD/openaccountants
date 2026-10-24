---
jurisdiction: CR
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
---

# Costa Rica: tax pack

Costa Rica taxes income under the territorial principle: Ley del Impuesto
sobre la Renta No. 7092 (LIR) reaches Costa Rica-source income only. The
corporate branch (Título I) taxes company profits — general rate 30% since
the 2019 reform of the income-tax title, with graduated small-company rates
— while employment and self-employed income run on separate schedules
indexed annually by decree. Consumption tax is the IVA (13%) created by
Ley No. 9635 (2018); the same law restructured the income-tax title and
introduced the transfer-pricing rules (LIR arts. 1018–1028). The tax
authority is the Dirección General de Tributación (DGT) under
hacienda.go.cr; filings run through TRIBU-CR. Social security is the CCSS
(Caja), collected on a separate scale.

**Source status:** pgrweb.go.cr resolves and the Ley 9635 VAT-title text was
read 2026-10-24; the SCIJ consolidated-text pages return a JS shell (no
server-rendered statute text), and hacienda.go.cr / sied.hacienda.go.cr did
not resolve from this environment. Corporate-rate and transfer-pricing
article text is therefore **needs-sources** at primary level; figures carry
PwC Tax Summaries citations (read 2026-10-24) and the pre-2019 LIR text
fetched from pgrweb.go.cr for the withholding-title figures.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | costa-rica-income-tax | source-cited draft |
| IT-CORP, corporate income tax | cr-corporate-income-tax | source-cited draft |
| VAT / GST | costa-rica-iva | source-cited draft |
| SC, social contributions | costa-rica-social-contributions | source-cited draft |
| PR, payroll withholding | costa-rica-payroll | source-cited draft |
| TP, transfer pricing | cr-transfer-pricing | source-cited draft |
| XB, cross-border | cr-cross-border | source-cited draft |

## Official sources

- [PGR — Ley 9635 (VAT title text)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML) — read 2026-10-24 (IVA 13% art. 10 verified in text).
- [Ley 7092 LIR (as-enacted PDF, COMEX mirror)](https://www.comex.go.cr/media/1894/ley_7092.pdf) and [MEP mirror](https://www.mep.go.cr/sites/default/files/2024-12/3LeyImpestoRentaN%C2%B07092.pdf) — both verified resolving 2026-10-24 (pre-9635 text; withholding-title rates 15%/25%/30% verified in extracted text).
- [PGR SCIJ — consolidated-text pages](https://pgrweb.go.cr/scij/) — resolve but render via JavaScript; statute text not server-side extractable 2026-10-24; **needs-sources**.
- hacienda.go.cr / sied.hacienda.go.cr — DNS/HTTP failure from this environment 2026-10-24; **needs-sources**.
- [PwC Tax Summaries — Costa Rica corporate income](https://taxsummaries.pwc.com/costa-rica/corporate/taxes-on-corporate-income) and [withholding](https://taxsummaries.pwc.com/costa-rica/corporate/withholding-taxes) — secondary, read 2026-10-24; used where primary text unavailable.
