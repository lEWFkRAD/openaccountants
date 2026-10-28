---
name: ms-social-contributions
description: >
  Use this skill whenever asked about Mississippi employer social
  contributions for 2026 — unemployment insurance administered by the
  Mississippi Department of Employment Security (MDES), employer quarterly
  wage and contribution reporting, and the interaction with federal
  FUTA/SUTA credits. Trigger on "Mississippi unemployment", "MDES",
  "Mississippi SUTA", "Mississippi employer contributions". Source-cited
  draft; MDES administration and employer reporting rails verified on
  mdes.ms.gov 2026-10-28; wage base and experience-rate tables
  needs-sources.
jurisdiction: US-MS
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ms-income-tax
---

# Mississippi social contributions (employer side) v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## 1. Scope and sources

Employer social costs for Mississippi employment: state UI plus the federal rails. **Source status:** MDES (https://www.mdes.ms.gov/) and its employer reporting-and-filing section resolve and were fetched 2026-10-28 — **MDES administers Mississippi UI; employers file quarterly wage and contribution reports (Form UI-2 is the conventional report ID — confirm, needs-sources)**. The **2026 taxable wage base, new-employer rate and experience schedule — needs-sources** (tables not extracted this run).

## 2. Who applies

Mississippi employers (including out-of-state employers with Mississippi employees). Mississippi has **no state disability, family-leave, or state-mandated retirement contribution** for private employers beyond federal FICA/FUTA.

## 3. Rates and wage base

| Item | 2026 figure | Source status |
|---|---|---|
| MS UI taxable wage base | not fetched | **needs-sources** |
| Experience rates | schedule not fetched | **needs-sources** |
| New-employer rate | not fetched | **needs-sources** |
| FUTA (context) | 6.0% on first $7,000; credit up to 5.4% for timely SUTA | federal standing rule |

## 4. Base and mechanics

- Quarterly gross-wage + contribution report to MDES (verified rails); online account filing standard.
- Timely SUTA payment preserves the 5.4% FUTA credit (federal rule).

## 5. Deadlines, penalties, interest

Quarterly reports due last day of the month following each quarter (convention — **needs-sources** for MS-specific dates/penalties).

## 6. Cross-border notes

Multi-state employers: localize employees under the interstate reciprocal coverage agreement tests (verify — **needs-sources**); Mississippi income-tax withholding is separate (see `ms-payroll.md`).

## 7. Worked examples

**Example 1 — FUTA net per employee (federal context):**

```oa-check
name: FUTA net 0.6 percent
inputs:
  wage_base: 7000
  net_rate: 0.006
steps:
  - futa: wage_base * net_rate
expected:
  futa: 42.00
```

**Example 2 — illustrative MS UI (figures assumed, needs-sources).** Base $9,500, new-employer-style rate 1.0%:

```oa-check
name: MS UI illustrative
inputs:
  wage_base: 9500
  rate: 0.01
steps:
  - ui: wage_base * rate
expected:
  ui: 95.00
```

## 8. Ask the client

- Are MDES quarterly filings current (experience rating depends on them)?
- Multi-state workforce — is Mississippi the localization state?
- Successor-employer or rate-transfer events on account purchases?

## 9. Sources

1. MDES employer reporting: https://www.mdes.ms.gov/ — fetched 2026-10-28 (administration + reporting rails).
2. Pre-existing `ms-income-tax.md` for the income-tax side.

**Needs-sources:** wage base, rate schedule, new-employer rate, UI-2 form ID confirmation, due dates, penalties.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Mississippi payroll/social-cost questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
