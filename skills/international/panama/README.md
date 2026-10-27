---
jurisdiction: PA
applicable: [IT-CORP, VAT, TP, XB]
covered_by:
  IT-CORP: panama-income-tax
  VAT: panama-itbms
---

# Panama: tax pack

Panama taxes on a territorial source basis: only Panamanian-source income
is taxed, and foreign-source income is reported but not taxed (Fiscal
Code, Ley 8 de 1972, article 705 — text needs-sources; treatment as
published by DGI, read 2026-10-27). Corporations pay 25% on net taxable
income (DGI rate schedule, read), individuals a 0/15/25% graduated
schedule with an 11,000 balboa exempt band (read). Dividends carry a
10% withholding (5% where the paying company's income was exempt —
DGI Form 07 page, read), and payments or credits of Panamanian-source
income to non-residents trigger withholding reported on Form 05 within
10 days (DGI Form 05 page, read). Sales tax is the ITBMS at a 7% general
rate (panama-itbms covers it). Social security and payroll run through
the CSS (panama-social-contributions, panama-payroll). The currency is
the US dollar (balboa at par); the fiscal year is the calendar year
unless DGI authorises a special period (DGI filing-deadlines page, read).
IT-CORP and VAT are covered by existing skills; this pack adds TP and XB
and a corporate-specific skill.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | panama-income-tax | existing (tier-2, DGI-cited) |
| IT-CORP, corporate income tax | panama-income-tax + panama-corporate-income-tax | existing + new corporate skill |
| VAT, ITBMS | panama-itbms | existing (7% general, 10/15% special) |
| SC, social contributions | panama-social-contributions | existing |
| PR, payroll withholding | panama-payroll | existing |
| TP, transfer pricing | panama-transfer-pricing | source-cited draft (thin — needs-sources) |
| XB, cross-border | panama-cross-border | source-cited draft |

## Official sources

- [DGI — ISR rate schedule (Art. 710 Código Fiscal)](https://dgi.mef.gob.pa/DInforme/Tarifa.php) — read 2026-10-27 (individual 0/15/25% bands; corporate 25% from 2011).
- [DGI — filing deadlines and forms (Fecha de Vencimientos)](https://dgi.mef.gob.pa/DInforme/Tab-Decla.php) — read 2026-10-27 (individuals 15 March; companies 31 March; Form 05 within 10 days).
- [DGI — Form 07 dividend withholding](https://dgi.mef.gob.pa/DInforme/Formulario07.php) — read 2026-10-27 (10% Panamanian-source, 5% exempt-source).
- [DGI — Form 05 remesas al exterior](https://dgi.mef.gob.pa/DInforme/Formulario05.php) — read 2026-10-27 (withholding on payments/credits to non-residents; Form 433 for treaty relief).
- [DGI — transfer pricing section (Precios de Transferencia, Informe 930)](https://dgi.mef.gob.pa/PreciosTransferencia/) — read 2026-10-27.
- [DGI — tax treaties (Convenios Tributarios)](https://dgi.mef.gob.pa/ConveniosTributarios/) — read 2026-10-27.
- [Caja de Seguro Social (CSS)](https://www.css.gob.pa/) — reachable but returns 403 to automated fetch; rates needs-sources.

## Source status

The DGI pages above were read directly on 2026-10-27 (the Tarifa page
returned 500 earlier in the day and succeeded on retry). The Fiscal Code
(Ley 8 de 1972) consolidated PDF could not be located on asamblea.gob.pa
(404 on the expected path), so article texts are cited as DGI publishes
them; CSS contribution rates and the transfer-pricing statute (Ley
52-2016 and amendments) are needs-sources.
