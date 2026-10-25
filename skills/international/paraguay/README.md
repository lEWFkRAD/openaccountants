---
jurisdiction: PY
applicable: [IT-IND, IT-CORP, SC, PR, TP, XB]
not_applicable:
  VAT: covered by the existing `paraguay-iva` skill (10% standard / 5% reduced IVA) already in this pack
---

# Paraguay (PY): tax pack

Paraguay taxes on a **territorial** basis: only Paraguay-source income is taxed, in guaraníes (PYG), on a calendar fiscal year. The tax authority is the Dirección Nacional de Ingresos Tributarios (DNIT, formerly SET) at set.gov.py. Individuals pay IRP (progressive 8/9/10% personal services; flat 8% capital); businesses pay the 10% Impuesto a la Renta Empresarial (IRE, Ley 72/2023) with simplified regimes IRE SIMPLE (prior-year income ≤ PYG 2bn) and RESIMPLE (gross ≤ PYG 80m). There is no separate payroll tax — payroll withholding is IRP on dependent work plus IPS social-security withholding (9% employee / 16.5% employer general). IVA is 10% standard, 5% reduced.

**Source status:** the DNIT portal (set.gov.py) and the IPS portal resolve; the BACN statute mirror returned 523 and the Ley 72/2023 gazette PDF did not resolve from the drafting environment on 2026-10-24, so IRE statutory citations are **needs-sources** (figures corroborated by PwC Worldwide Tax Summaries, Paraguay pages, last reviewed 19 October 2026, read 2026-10-24).

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | paraguay-income-tax | source-cited draft |
| IT-CORP, corporate income tax | py-corporate-income-tax | source-cited draft |
| VAT / GST | paraguay-iva (see not_applicable) | source-cited draft |
| SC, social contributions | paraguay-social-contributions | source-cited draft |
| PR, payroll withholding | paraguay-payroll | source-cited draft |
| TP, transfer pricing | py-transfer-pricing | source-cited draft |
| XB, cross-border | py-cross-border-tax | source-cited draft |

## Official sources

- DNIT (tax authority) portal: <https://www.set.gov.py/> — read 2026-10-24 (HTTP 200).
- Ley 6380/2019 mirror (BACN): <https://www.bacn.gov.py/archivos/9332/Ley+6380.pdf> — PDF 200 on 2026-10-24; site root returned 523 (flaky).
- IPS (social security): <http://www.ips.gov.py/> — read 2026-10-24 (HTTP 200).
- PwC Worldwide Tax Summaries, Paraguay (corporate CIT / administration / other taxes; individual other taxes) — read 2026-10-24; PwC "last reviewed 19 October 2026".
- Ley 72/2023 (IRE) official gazette text — **needs-sources** (not reachable from the drafting environment 2026-10-24).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
