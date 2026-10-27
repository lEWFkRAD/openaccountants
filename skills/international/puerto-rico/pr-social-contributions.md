---
name: pr-social-contributions
description: >
  Puerto Rico social contributions reference for 2026. Explains that PR employers and employees pay US federal payroll taxes (FICA 7.65 percent employee plus 7.65 percent employer, FUTA) rather than a local social-security title in the Code, plus local schemes (SUI, government retirement systems) flagged needs-sources. Covers who applies, bases, deadlines and the interaction with PR income withholding. Trigger on Puerto Rico social security, FICA Puerto Rico, SUI PR, unemployment PR. Source-cited draft.
jurisdiction: PR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Puerto Rico social contributions

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026. The Código de Rentas
Internas de Puerto Rico de 2011 (OGP consolidated PDF, rev. 28 May 2026)
was read directly and contains no general private-sector social-security
contribution title — PR old-age and disability cover runs through the US
federal system. The federal FICA/FUTA figures below are standard US
Social Security Administration parameters and are needs-sources for the
2026 wage bases (confirm at ssa.gov/pubs and irs.gov). Local schemes
(Seguro del Empleo, government retirement systems) are needs-sources.

## 2. Who applies

PR private-sector employers and employees pay US federal payroll taxes:
Social Security and Medicare (FICA) withheld by the employer and matched,
and federal unemployment tax (FUTA) on the employer. PR is inside the US
Social Security system; workers qualify for the same federal benefits.
Public employees instead belong to local retirement systems (needs-
sources). PR also operates a local unemployment insurance scheme (Seguro
del Empleo) funded by employer contributions (needs-sources).

## 3. Rates

| Item | Rate | Source |
|---|---|---|
| Social Security (employee + employer) | 6.2% each, on the annual wage base | US FICA — needs-sources for the 2026 base |
| Medicare (employee + employer) | 1.45% each, no cap; 0.9% additional on high earners | US FICA — needs-sources |
| FUTA (employer) | 6.0% gross, effectively 0.6% after credit, on the federal wage base | US FUTA — needs-sources |
| PR unemployment insurance (Seguro del Empleo) | employer contributions, rate schedule needs-sources | local law |
| Government employees' retirement | defined-benefit systems, needs-sources | local law |

## 4. Base and timing

FICA runs on wages as defined federally (the same wage figures PR income
withholding reports on Form 499R-5c/499R-4). PR income-tax withholding
rules live in the Code's Subtítulo A B — see pr-payroll-withholding.
Contribution and tax deposits follow the federal semi-weekly/monthly
deposit schedules (needs-sources for current thresholds).

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| Federal employment tax returns (941) | quarterly, last day of the month after quarter end | US federal — needs-sources |
| Annual wage reports (W-2 / 499R-5c) | 31 January | US/PR joint filing — needs-sources |
| PR unemployment contributions | per local schedule | needs-sources |

## 6. Penalties and interest

Federal employment-tax penalties apply to FICA/FUTA (failure to deposit
2%-15% tiers, needs-sources). For PR income-tax withholding failures the
Code adds 2% of the shortfall per 30-day period up to 24% (§6041.01(a),
read) — that penalty attaches to the withholding side, not FICA.

## 7. Cross-border interactions

US citizens moving to or from PR keep their federal Social Security
coverage unchanged; totalisation agreements do not apply within PR.
Foreign workers on PR assignments follow the same FICA rules as on the
mainland. PR-sourced self-employment income is subject to federal SE
tax (needs-sources).

## 8. Worked examples

PR employer payroll cost adder on USD 80,000 of wages (employer FICA
only, 7.65% — 2026 wage base not binding at this level):

```oa-check
name: employer FICA on 80000 wages
inputs:
  salarios: 80000
  fica: 0.0765
steps:
  - contribucion_patron: salarios * fica
expected:
  contribucion_patron: 6120.00
```

Failure-to-file example for the withholding side: a USD 10,000 PR
withholding return filed 45 days late (§6030.11, read: 5% plus 10% per
additional 30-day period):

```oa-check
name: failure to file penalty 45 days late on 10000 tax
inputs:
  contribucion: 10000
  p30: 0.05
  p30mas: 0.1
steps:
  - penalidad: contribucion * (p30 + p30mas)
expected:
  penalidad: 1500.00
```

## 9. Ask the client / sources

Ask: Is the client filing both federal (941/W-2) and PR (499R) wage
reports? Are PR unemployment contributions current? Any public-sector
employees in a local retirement system? Cross-border assignees keeping
benefit continuity?

Sources: OGP consolidated Code PDF (read 2026-10-27 — no local SSC title).
Needs-sources: 2026 FICA/FUTA wage bases and deposit rules (SSA/IRS),
PR Seguro del Empleo rate schedule, government retirement system rates.

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
