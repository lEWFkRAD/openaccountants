---
name: NAME
description: >
  DESC
jurisdiction: JUR
category: CAT
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Puerto Rico cross-border (Chapter 10, non-residents)

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: the OGP consolidated
PDF of the Código de Rentas Internas de Puerto Rico de 2011 (rev. 28 May
2026) was read directly; §§1091.01 and 1092.01 are quoted from that text.
US income-tax-treaty application to PR-source income is needs-sources
(the US treaties generally cover PR income, but PR's own Code taxes
independently — the interaction must be confirmed per treaty).

## 2. Who applies

Non-resident aliens not engaged in a PR trade or business pay Chapter 10
on PR-source amounts received (§1091.01(a)(1)(A), read). Foreign
corporations not engaged in a PR business pay the parallel charge
(§1092.01(a)(1)(A), read). US-mainland persons are "non-resident" for PR
income-tax purposes; a US citizen resident in PR is taxed like a PR
resident on PR-source income (see pr-federal-residence-and-filing).

## 3. Rates

| Payee / income | Rate | Source |
|---|---|---|
| NRA: rents, royalties, salaries, annuities, related-party interest, partnership allocations, capital gains, other fixed determinable income | 29% | §1091.01(a)(1)(A)(i) (read) |
| NRA: dividends | 15% | §1091.01(a)(1)(A)(ii) (read) |
| NRA: S-corporation (corporación de individuos) allocable income | 33% | §1091.01(a)(1)(A)(iii) (read) |
| Foreign corporation: fixed determinable PR-source income incl. related-party interest | 29% | §1092.01(a)(1)(A)(i) (read) |
| Foreign corporation: dividends | 10% | §1092.01(a)(1)(A)(ii) (read) |
| Portfolio interest to unrelated payers | exempt/10% by category | §1023.04-1023.05 area (needs-sources current text) |

International insurers and their holding companies are carved out of the
charge for specified flows (§1091.01(a)(1)(B), read).

## 4. Base and timing

Chapter 10 taxes the amount received ("monto recibido, o implícitamente
recibido") with no deductions for the flat categories (read). Capital
gains are netted only within PR sources and without capital-loss carryover
benefits (§1091.01(a)(2), read). "Related person" definitions drive the
29% vs portfolio split (§1091.01(a)(3), §1010.05, read). A foreign
corporation may elect to be taxed on net income as if engaged in a PR
business (§1092.01(d) election referenced in §1022.03(a), read).

## 5. Deadlines

Withholding by the PR payer rides the Subtítulo A B deposit rules (see
pr-payroll-withholding). Self-filing by the non-resident: annual return
15 April calendar-year (§1061.16, read) with the 3-month automatic
extension (read).

## 6. Penalties and interest

10% annual interest on deficiencies (§6030.01, read); failure-to-file 5%
plus 10% per 30-day period (§6030.11, read); failure to deposit withheld
tax 2% per 30-day period capped at 24% (§6041.01, read).

## 7. Cross-border interactions

PR-source rules mirror the old US IRC sourcing (the Code was modelled on
the Internal Revenue Code): services are PR-source where performed,
rents where the property sits, interest by the payer's residence. US
federal law then exempts most PR-source income of PR residents from US
federal tax, but non-residents of PR face both the PR Chapter 10 charge
and US federal tax on US-source flows — treaty relief, where available,
is a US-federal question (needs-sources). Act 138-2022 / Act 60-2019
decree companies operate inside this net with decree-specific conditions
(needs-sources).

## 8. Worked examples

A foreign (non-PR) corporation receives USD 120,000 of dividends from a
PR corporation, with no PR business (§1092.01(a)(1)(A)(ii), 10%):

```oa-check
name: non-resident corporation dividend withholding 10 percent
inputs:
  dividendo: 120000
  tasa: 0.1
steps:
  - contribucion: dividendo * tasa
expected:
  contribucion: 12000.00
```

A non-resident alien individual receives PR-source rent of USD 60,000
(29% under §1091.01(a)(1)(A)(i), read):

```oa-check
name: non-resident alien PR rent 29 percent on 60000
inputs:
  renta: 60000
  tasa: 0.29
steps:
  - contribucion: renta * tasa
expected:
  contribucion: 17400.00
```

## 9. Ask the client / sources

Ask: Which payees are non-residents of PR for PR tax purposes (mainland
US persons included)? Are payers screening service and rent flows for
Chapter 10 vs §1062.03 overlap? Any §1092.01(d) net-income elections?
Related-party interest reclassified at 29%? Decree companies keeping
their decree conditions and Chapter 10 filings straight?

Sources: OGP consolidated Code PDF (read 2026-10-27). Needs-sources:
treaty interaction with PR-source income, portfolio-interest current
text (§§1023.04-1023.05), decree (Act 138-2022) conditions.

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
