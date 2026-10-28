---
name: cg-payroll-social
description: "Source-cited draft: payroll & social contributions for Republic of Congo (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: CG
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Republic of Congo Payroll & Social Contributions

## Payroll, social security and salary taxes

- **Employee old-age pension (CNSS)** — 4% of gross salary percent  _(Code de Sécurité Sociale; CNSS regulations — https://taxsummaries.pwc.com/republic-of-congo/individual/other-taxes)_
- **Employer old-age / invalidity / death insurance (CNSS)** — 8% of gross salary, capped at XAF 14,400,000 annually percent  _(Code de Sécurité Sociale; CNSS regulations — https://taxsummaries.pwc.com/republic-of-congo/corporate/other-taxes)_
- **Employer family allowance contribution** — 10.035% of gross salary, capped at XAF 7,200,000 annually percent  _(Code de Sécurité Sociale; CNSS regulations — https://taxsummaries.pwc.com/republic-of-congo/corporate/other-taxes)_
- **Employer work-accident contribution** — 2.25% of gross salary, capped at XAF 7,200,000 annually percent  _(Code de Sécurité Sociale; CNSS regulations — https://taxsummaries.pwc.com/republic-of-congo/corporate/other-taxes)_
- **Single Tax on Remuneration (employer)** — 7.5% for resident employees; 6% for non-resident non-seafarers; 2.5% for oil companies percent  _(Code Général des Impôts (CGI) — Taxe Unique sur les Salaires — https://taxsummaries.pwc.com/republic-of-congo/corporate/other-taxes)_
- **Pension contribution wage ceiling** — Approximately XAF 14,400,000 per year (old-age/invalidity/death branch) XAF  _(Code de Sécurité Sociale; CNSS regulations — https://taxsummaries.pwc.com/republic-of-congo/corporate/other-taxes)_
- **Salary tax withholding (PAYE-equivalent)** — IRPP and the Single Tax on Remuneration are withheld monthly by the employer at source  _(Code Général des Impôts (CGI))_
- **Payroll tax / contribution remittance deadline** — By the 20th of the month following the payroll period (CNSS monthly/quarterly per employer size) ((approx — confirm))  _(Code Général des Impôts (CGI); CNSS regulations)_
- **Departmental (local) tax** — Flat XAF 2,000 per individual per year XAF  _(Code Général des Impôts (CGI) — https://taxsummaries.pwc.com/republic-of-congo/individual/other-taxes)_

## Recomputing examples

```oa-check
name: CG CNSS on 1,000,000 XAF monthly gross (employee 4%, employer 8%)
inputs:
  gross: 1000000
steps:
  - employee: gross * 0.04
  - employer: gross * 0.08
expected:
  employee: 40000.00
  employer: 80000.00
```
```oa-check
name: CG Taxe Unique sur les Salaires 7.5% on 10,000,000 XAF payroll
inputs:
  payroll: 10000000
steps:
  - tus: payroll * 0.075
expected:
  tus: 750000.00
```

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

## Sources

- Code de Sécurité Sociale (Republic of Congo); CNSS regulations
- Code Général des Impôts (CGI) (Republic of Congo), Taxe Unique sur les Salaires

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
