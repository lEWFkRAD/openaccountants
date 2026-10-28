---
name: bh-payroll-social
description: "Source-cited draft: payroll & social contributions for Bahrain (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BH
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahrain Payroll & Social Contributions

## Social insurance (SIO/GOSI) contributions

- **PAYE-equivalent income tax withholding** — None - no income tax is withheld from wages  _(PwC Worldwide Tax Summaries - Bahrain Individual)_
- **Employer contribution - Bahraini nationals (2025)** — 17% of insurable salary %  _([Social Insurance Law (Decree-Law No. 24 of 1976), as amended](https://www.newsofbahrain.com/bahrain/106412.html))_
- **Employee contribution - Bahraini nationals (2025)** — 8% (7% pension/old-age + 1% unemployment insurance) %  _(Social Insurance Law (Decree-Law No. 24 of 1976), as amended)_
- **Scheduled annual increase (Bahraini employers)** — Employer retirement contribution rises 1% per year until reaching 21% in 2028  _([Social Insurance Law (Decree-Law No. 24 of 1976), as amended](https://www.fragomen.com/insights/middle-east-increase-in-insurance-contribution-rates-for-bahraini-nationals-and-their-employers-in-gcc-countries.html))_
- **Employer contribution - non-GCC expatriates** — 3% (work-injury insurance only) %  _(Social Insurance Law (Decree-Law No. 24 of 1976), as amended)_
- **Employee contribution - non-GCC expatriates** — 1% (work-injury insurance only) %  _(Social Insurance Law (Decree-Law No. 24 of 1976), as amended)_
- **GCC nationals working in Bahrain** — Contributions follow the social insurance rules of the worker's home GCC state  _(GCC Unified Insurance Protection Extension scheme)_
- **Insurable salary ceiling** — BHD 4,000 per month BHD  _([Social Insurance Law (Decree-Law No. 24 of 1976), as amended](https://www.zoho.com/en-bh/payroll/help/employer/social-security/gosi.html))_
- **Contribution remittance** — Employer registers with SIO and remits monthly contributions via the SIO portal ((approx - confirm exact monthly due date))  _(Social Insurance Law (Decree-Law No. 24 of 1976), as amended)_
- **Employer registration trigger** — Employers must register with the SIO when hiring employees  _(Social Insurance Law (Decree-Law No. 24 of 1976))_

## Recomputing examples

```oa-check
name: BH GOSI on 1,000 BHD insurable salary: employer 17% + employee 8%
inputs:
  salary: 1000
steps:
  - employer: salary * 0.17
  - employee: salary * 0.08
  - total: employer + employee
expected:
  employer: 170.00
  employee: 80.00
  total: 250.00
```
```oa-check
name: BH expat contributions on 1,000 BHD: employer 3% + employee 1%; 2028 employer 21%
inputs:
  salary: 1000
steps:
  - employer_expat: salary * 0.03
  - employee_expat: salary * 0.01
  - employer_2028: salary * 0.21
expected:
  employer_expat: 30.00
  employee_expat: 10.00
  employer_2028: 210.00
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

- Social Insurance Law (Decree-Law No. 24 of 1976), as amended (Bahrain)

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
