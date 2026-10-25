---
name: Haiti social contributions
description: Use when a Haiti employer needs to identify 2026 ONA and OFATMA registration, payroll-base, remittance, evidence, or audit requirements and source current rates safely.
jurisdiction: HT
category: payroll
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Haiti social contributions

## 1. Who this applies to

Haiti employers must determine whether workers are covered by the Office National d'Assurance-Vieillesse (ONA) pension system and the Office d'Assurance Accidents du Travail, Maladie et Maternité (OFATMA). Coverage and contribution treatment depend on the worker relationship, insurable remuneration, employer activity and the institution's current registration rules.

Do not treat independent-contractor wording as conclusive. Test supervision, integration, economic dependence, tools, risk and actual working conditions.

## 2. Rates and ceilings — source status

| Contribution | Institution | 2026 rate/ceiling status |
|---|---|---|
| Old-age/pension insurance | ONA | `needs-sources` — obtain the current official employer circular, contribution schedule or institution-certified assessment |
| Work-accident insurance | OFATMA | `needs-sources` — rate may depend on risk classification; obtain current official classification and schedule |
| Sickness/maternity coverage | OFATMA | `needs-sources` — confirm covered population, base and current split directly with OFATMA |

The official ONA and OFATMA pages verified the institutions and programs but did not expose a complete, current 2026 rate-and-ceiling table. Historic rates from secondary summaries are not reproduced here.

## 3. Contribution base

Build the payroll base from each employee's cash pay, allowances, bonuses, benefits and other remuneration, then map each component to the institution's current definition of insurable earnings. Reconcile the contribution base to payroll, general ledger and wage-withholding returns. Document exclusions with the specific current rule rather than custom or software defaults.

## 4. Registration, returns and deadlines

Register the employer and covered workers with the appropriate institution, maintain employee identifiers and risk classification, file the current return, and remit by the institution's deadline. Obtain written confirmation from ONA and OFATMA for the 2026 filing frequency, return format, deadline, payment account and correction process.

**Source status:** current 2026 rates, ceilings and remittance deadlines are `needs-sources`. This guide is a control framework, not a rate table.

## 5. Arrears, penalties and evidence

Late or missing registration, declarations or payments may lead to arrears, surcharges, collection and benefit-record problems. Before quantifying exposure, obtain an institution statement and the current legal rate of surcharge. Keep enrollment evidence, payroll detail, filed returns, bank proof and employee account confirmations.

**AUDIT FLASH POINT** — A payroll system can compute consistently using a stale rate. Reconcile every rate and ceiling to a dated ONA or OFATMA primary document before accepting the calculation.

## 6. Cross-border and mobile workers

For an expatriate, secondee or remote worker, determine who is the legal and economic employer, where the work is performed, whether Haiti coverage is mandatory and whether any social-security coordination instrument applies. Do not assume foreign coverage removes Haiti registration without a documented exemption.

## 7. Worked example — payroll-base reconciliation

An employer's payroll has HTG 60,000 regular pay and HTG 40,000 other remuneration subject to confirmation. The candidate contribution base is HTG 100,000 before applying a verified institution rate.

```oa-check
name: haiti candidate social contribution base
inputs:
  regular_pay: 60000
  other_remuneration: 40000
steps:
  - candidate_base: regular_pay + other_remuneration
expected:
  candidate_base: 100000.00
```

## 8. Worked example — remittance control

A ledger shows HTG 7,000 credited to ONA and HTG 3,000 credited to OFATMA for a period. The payroll-control total is HTG 10,000; compare it to returns and bank proof without assuming either amount is correct.

```oa-check
name: haiti social remittance control total
inputs:
  ona_ledger: 7000
  ofatma_ledger: 3000
steps:
  - control_total: ona_ledger + ofatma_ledger
expected:
  control_total: 10000.00
```

## 9. Ask the client first

1. Are the employer and every worker registered with ONA and OFATMA?
2. What dated official schedule supports each rate, ceiling and risk class used in payroll?
3. Which pay components are included or excluded, and why?
4. Do filed returns, institution statements, payroll and bank payments reconcile?
5. Are there contractors, expatriates, secondees or remote workers needing classification review?

## 10. Sources

- [ONA — official site](https://ona.ht/) — institution and pension-program access point; accessed 2026-10-24.
- [OFATMA — official site](https://ofatma.gouv.ht/) — workplace-accident, sickness and maternity institution; accessed 2026-10-24.
- [DGI — Code Général des Impôts, official PDF](https://dgi.gouv.ht/wp-content/uploads/2026/10/Code-Fiscal.pdf) — Article 71 confirms deductibility framework for employer pension and employee sickness/accident contributions but does not supply the contribution schedule; opened 2026-10-24.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
