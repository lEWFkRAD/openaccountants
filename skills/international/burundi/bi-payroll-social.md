---
name: bi-payroll-social
description: "Source-cited draft: payroll & social contributions for Burundi (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BI
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burundi Payroll & Social Contributions

## Payroll and social security (INSS)

Employers operate PAYE-style withholding on salaries and pay social-security contributions to the Institut National de Sécurité Sociale (INSS) plus health insurance. Reported rates differ between sources, so the figures below should be confirmed against current INSS and OBR schedules.

- **Payroll income tax withholding** — Employers withhold income tax on salaries at the progressive 0% / 20% / 30% scale (PAYE-equivalent)  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Employer INSS old-age/pension contribution** — 6% of gross wages % (approx — confirm; sources conflict)  _([Code de la sécurité sociale (INSS)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Employee INSS old-age/pension contribution** — 4% of gross wages % (approx — confirm; sources conflict)  _([Code de la sécurité sociale (INSS)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Monthly earnings cap for INSS pension contributions** — BIF 450,000 per month BIF (approx — confirm)  _([Code de la sécurité sociale (INSS)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Employer occupational risk / work injury contribution** — 3% (capped at BIF 80,000 per month) % (approx — confirm)  _([Code de la sécurité sociale (INSS)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Employee national health insurance contribution** — 3% of gross wages % (approx — confirm)  _([Régime d'assurance maladie (national health insurance)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Employee national health insurance contribution** — 3% of gross wages % (approx — confirm)  _([Régime d'assurance maladie (national health insurance)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Employer employment / vocational training levy** — 1% of gross wages % (approx — confirm)  _([Code de la sécurité sociale (INSS)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Approximate total employer social contributions** — About 13% of gross wages (pension + health + work injury + training, subject to caps) % (approx — confirm; sources conflict)  _([Code de la sécurité sociale (INSS)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Approximate total employee social contributions** — About 8% of gross wages (pension + health, subject to caps) % (approx — confirm; sources conflict)  _([Code de la sécurité sociale (INSS)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Payroll tax and INSS contribution remittance deadline** — 15th of the month following the payroll month  _([OBR / INSS monthly declaration rules](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Annual employer declaration** — Employers file an annual return summarising gross pay and tax/contributions withheld per employee  _([OBR filing rules under the General Tax Code](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_

## Worked examples

```oa-check
name: BI employee contributions on BIF 300,000 gross (INSS 4% + health 3%)
inputs:
  gross: 300000
  pension_cap: 450000
steps:
  - inss_employee: min(gross, pension_cap) * 0.04
  - health_employee: gross * 0.03
  - total_employee: inss_employee + health_employee
expected:
  inss_employee: 12000.00
  health_employee: 9000.00
  total_employee: 21000.00
```

```oa-check
name: BI employer contributions on BIF 300,000 gross (pension 6% + risk 3% capped 80,000 + training 1%)
inputs:
  gross: 300000
  pension_cap: 450000
  risk_cap: 80000
steps:
  - pension: min(gross, pension_cap) * 0.06
  - risk: min(gross, risk_cap) * 0.03
  - training: gross * 0.01
  - total_employer: pension + risk + training
expected:
  pension: 18000.00
  risk: 2400.00
  training: 3000.00
  total_employer: 23400.00
```

## Sources

| Source | URL | as_of |
|---|---|---|
| Code de la securite sociale (INSS) (cited inline) | https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/ | 2026-10-28 |
| Law No. 1/02 of 24 January 2013 (income tax law) (cited inline) | https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/ | 2026-10-28 |

Sources are the statutes/agencies already cited inline in this guide, listed as_of 2026-10-28 and **unverified against archived evidence**.

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
