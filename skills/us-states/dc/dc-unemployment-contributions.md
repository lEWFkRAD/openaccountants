---
name: dc-unemployment-contributions
description: >
  Use this skill whenever asked about District of Columbia employer
  social contributions for tax year 2026 — unemployment insurance
  contributions administered by the Department of Employment Services
  (DOES), the employer-only nature of the UI tax, the DC UI taxable
  wage base and experience rates, DC's paid-family-leave (TFI) and
  temporary- disability insurance (TDI) employer obligations, and
  workers' compensation. Trigger on "DC UI rate", "DC SUTA",
  "District of Columbia unemployment wage base", "DC TDI", "DC TFI",
  "DC employer taxes", "DC DOES UI". Source-cited draft; does.dc.gov
  resolves but is JS-rendered — all figures flagged needs-sources.
jurisdiction: US-DC
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - dc-income-tax
---

# District of Columbia social contributions (UI + TDI/TFI) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. DC employer social contributions: unemployment insurance under DC Code Title 51 ch. 1 administered by the **Department of Employment Services (DOES)**; DC's **Temporary Disability Insurance (TDI)** and **Universal Paid Family Leave (TFI)** programs (DC's distinctive payroll programs, with employer and (for TDI) employee premium splits); federal FICA/FUTA; and mandatory workers' compensation. **Source status:** does.dc.gov/page/unemployment-compensation fetched 2026-10-27 (200) but the page is JavaScript-rendered — the nav confirms "UI Tax for Employers / General UI Information / UI Taxes" sections exist, but no wage-base or rate text was extractable; every figure below is **needs-sources**. TDI/TFI premium splits are well-known in DC practice but were not read from an official page this run — also **needs-sources**.

## 2. Who applies

- Employers covered under DC Code §51-101 et seq. (coverage tests — **needs-sources**). Out-of-state employers with DC employees are covered.
- The UI contribution is **employer-only** — DC employees pay no state UI tax.
- **TDI:** employers withhold/remits a premium split between employer and employee (split **needs-sources**); administered by DC Benefits Bureau.
- **TFI (paid family leave):** employer-paid premium (rate **needs-sources**).
- Workers' compensation: mandatory above the DC threshold (one or more employees — confirm, **needs-sources**).

## 3. Rates and base (2026 — all figures needs-sources)

| Item | 2026 amount | Source |
|---|---|---|
| UI taxable wage base | **needs-sources** (DOES 2026 notice) | DC Code §51-141 — not extracted |
| Experience rate range | **needs-sources** | DC Code §51-142 — not extracted |
| New-employer rate | **needs-sources** | DC Code §51-143 — not extracted |
| TDI premium split | **needs-sources** | DC Benefits Bureau |
| TFI premium rate | **needs-sources** | DC Benefits Bureau |

## 4. Deadlines

- **Quarterly UI return + contribution:** due the last day of the month following each quarter (pattern — confirm, **needs-sources**).
- **Annual reconciliation:** January 31 (pattern — **needs-sources**).
- **TDI/TFI:** quarterly filings with the DC Benefits Bureau (calendar **needs-sources**).

## 5. Penalties and interest

Late UI filings/payments draw Title 51 penalties (percentages **needs-sources**); OTR also publishes a "Notice of Delinquency (TDI)" page (linked from OTR business pages, read 2026-10-27) — TDI delinquency enforcement is real and separate from UI. Common failure modes: (1) multi-state payroll teams missing DC TDI/TFI entirely because no other jurisdiction has analogs; (2) accruing UI on gross payroll instead of the wage base; (3) remote workers performing DC work without a DOES registration.

## 6. Cross-border interactions

- Employers with DC-located employees register with DOES even with no DC office.
- TDI/TFI apply to work performed in DC — telecommuter splits matter (rules **needs-sources**).

## 7. Worked examples

An employer with 4 DC employees each paid $60,000, at an illustrative 3.1% UI rate on a $43,000 wage base (both inputs **needs-sources**):

```oa-check
name: DC UI contribution illustrative
inputs:
  employees: 4
  wage_base: 43000
  rate: 0.031
steps:
  - taxable: employees * wage_base
  - contribution: taxable * rate
expected:
  taxable: 172000.00
  contribution: 5332.00
```

## 8. Ask the client

- Are DC TDI and TFI premiums in the payroll accrual — most multi-state payrolls miss them?
- Has the DOES 2026 rate notice been reconciled to the reserve account?
- Remote workers performing DC work: registered with DOES?
- TDI delinquency notices received (OTR publishes them)?

## Sources

1. DOES Unemployment Compensation: https://does.dc.gov/page/unemployment-compensation (200, read 2026-10-27 — JS-rendered; UI-tax-for-employers sections confirmed)
2. OTR Notice of Delinquency (TDI): https://otr.cfo.dc.gov/page/notice-delinquency-tdi (linked from OTR business nav, read 2026-10-27)
3. DC Code Title 51 ch. 1: https://code.dccouncil.gov/us/dc/council/code/titles/51/chapters/1/ (not extracted this run — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for DC payroll, UI, TDI/TFI questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
