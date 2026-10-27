---
jurisdiction: MX
applicable: [IT-CORP, SC, PR, XB]
---

# Mexico: tax pack

Mexico taxes corporations under the Ley del Impuesto Sobre la Renta (LISR)
at a flat 30% on the annual fiscal result, with monthly provisional
payments due by the 17th of the following month (LISR Art. 14) and an
annual return in July. Distributions run through the CUFIN/CORE accounts:
dividends are grossed up by the factor 1.4286 and taxed at 30% at the
corporate level (LISR Art. 10), plus a 10% additional tax on distributions
out of post-2014 profits. Social security is IMSS: employer contributions
of roughly 20.6%-31.5% of the salario base de cotizacion depending on the
decreto-prima for occupational risk (LSS Arts. 28, 73), worker
contributions of about 2.375%, plus INFONAVIT at 5% and state payroll
taxes of around 3%. Non-resident income is taxed under LISR Title V with
flat 25% rates on Mexican real-property rent and gains and on services,
withheld at source. The currency is the peso (MXN); the tax year is the
calendar year. VAT (IVA) and individual income tax already have skills in
this pack; this README adds the four missing domains.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-CORP, corporate income tax | mx-corporate-income-tax | source-cited draft |
| SC, social contributions | mx-social-contributions | source-cited draft |
| PR, payroll withholding | mx-payroll-withholding | source-cited draft |
| XB, cross-border | mx-cross-border | source-cited draft |
| IT-IND, individual income tax | mx-income-tax | existing |
| VAT (IVA) | mexico-iva, mx-vat-return | existing |
| TP, transfer pricing | mexico-transfer-pricing | existing |

## Official sources

- [Ley del Impuesto Sobre la Renta (Camara de Diputados PDF, last reform DOF 01-04-2024)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) — read 2026-10-27.
- [Ley del Seguro Social (Camara de Diputados PDF)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) — read 2026-10-27.
- [Ley Federal del Trabajo (Camara de Diputados PDF)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf) — read 2026-10-27.
- [Codigo Fiscal de la Federacion (Camara de Diputados PDF)](https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf) — read 2026-10-27.
- [SAT portal home](https://www.sat.gob.mx/home) — read 2026-10-27.
- [INEGI — UMA (daily reference amount)](https://www.inegi.org.mx/dependencias/cve/uma/) — read 2026-10-27; the 2026 UMA value itself is needs-sources (page is JS-rendered).
- [IMSS](https://www.imss.gob.mx/) — browser-reachable; urllib returned 403 on 2026-10-27, so IMSS circular figures are flagged needs-sources.

## Source status

The LISR and LSS PDFs above were read directly and the statutory rates
and deadlines in these skills cite them article by article. Figures that
come from administrative schedules rather than the statutes — the 2026
UMA and minimum wage, the SAT withholding tariff tables, and the 2026
SBC ceiling — are marked needs-sources and must be confirmed against the
DOF and SAT tariff publications before a tier-1 review.
