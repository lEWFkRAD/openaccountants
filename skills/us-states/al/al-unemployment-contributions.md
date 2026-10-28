---
name: al-unemployment-contributions
description: >
  Use this skill whenever asked about Alabama employer social
  contributions for tax year 2026 — unemployment insurance
  contributions administered by the Alabama Department of Labor
  (labor.alabama.gov / adol.alabama.gov), the employer-only nature of
  the UI tax, the Alabama taxable wage base, experience rating, and
  the absence of state disability or paid-leave payroll taxes.
  Trigger on "Alabama UI rate", "Alabama SUTA", "Alabama unemployment
  wage base", "Alabama employer taxes", "Alabama reemployment tax".
  Source-cited draft; labor.alabama.gov resolves but UI figures were
  not extractable this run — all amounts flagged needs-sources.
jurisdiction: US-AL
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - al-income-tax
---

# Alabama social contributions (UI) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Alabama's employer social contributions are: unemployment insurance ("reemployment tax") contributions under Ala. Code Title 25 administered by the Alabama Department of Labor (ADOL), federal FICA/FUTA, and (for construction and similar industries) mandatory workers' compensation insurance. Alabama has **no** state disability insurance, **no** paid family/medical leave contribution, and **no** state-mandated retirement contribution for private employers. **Source status:** labor.alabama.gov fetched 2026-10-27 (200) and links the unemployment-compensation division at adol.alabama.gov (including employer partial-contribution filing guidance); the UI taxable wage base, 2026 experience-rate range, and new-employer rate were **not extractable this run** — every figure below is **needs-sources**. Do not publish numbers until ADOL's current rate notice is pulled.

## 2. Who applies

- Employers covered under Ala. Code Title 25 ch. 1 (coverage tests — statutory text **needs-sources**). Out-of-state employers with Alabama employees are covered on the same basis.
- The UI contribution is **employer-only** — Alabama employees pay no state UI tax.
- Workers' compensation insurance is mandatory for employers with the statutory number of employees (threshold **needs-sources**); it is an insurance mandate, not a tax.

## 3. Rates and base (2026 — all figures needs-sources)

| Item | 2026 amount | Source |
|---|---|---|
| UI taxable wage base | **needs-sources** (pull ADOL 2026 rate notice) | Ala. Code §25-4-41 — not fetched |
| Experience rate range (min/max) | **needs-sources** | Ala. Code §25-4-43 — not fetched |
| New-employer assigned rate | **needs-sources** | Ala. Code §25-4-44 — not fetched |
| Solvency/add-on surtaxes | **needs-sources** (check ADOL annual notice) | ADOL rate notices |
| FUTA credit reduction | none typical — verify current-year DOL list | US DOL |

## 4. Deadlines

- **Quarterly contribution return (Form A-4):** due the last day of the month following each quarter (April 30, July 31, October 31, January 31) — pattern **needs-sources** confirmation from ADOL.
- **Annual reconciliation (Form A-5):** due January 31 — **needs-sources**.
- **2026 rate notices:** issued to employers late in the prior year (ADOL employer portal) — date **needs-sources**.

## 5. Penalties and interest

Late contribution returns and payments draw penalties/interest under Title 25 (percentages **needs-sources**). Common failure modes: (1) reporting wages above the wage base — the base is per-employee per-year, not gross payroll; (2) missing the solvency surtax line on the A-4 in years it applies; (3) new employers assuming the assigned rate is negotiable — it is assigned, with appeal rights.

## 6. Cross-border interactions

- Multi-state employers register in Alabama when they have Alabama employees or localizable work; the wage base applies per employee per state.
- Leasing companies / PEOs file under ADOL's leasing-company rules (**needs-sources**).
- No Alabama counterpart to EU-style social security totalization; interstate only.

## 7. Worked examples

An employer with 10 Alabama employees each paid $30,000 in 2026, at an assumed experience rate of 2.7% on a $8,000 wage base (illustrative inputs — both figures **needs-sources**):

```oa-check
name: AL UI contribution illustrative
inputs:
  employees: 10
  wage_base: 8000
  rate: 0.027
steps:
  - taxable: employees * wage_base
  - contribution: taxable * rate
expected:
  taxable: 80000.00
  contribution: 2160.00
```

## 8. Ask the client

- Has the 2026 ADOL rate notice been received and the experience rate verified against the reserve account?
- Are wages reported capped at the wage base per employee, with multi-state employees allocated correctly?
- Is the solvency surtax (if any for 2026) included in accruals?
- Construction/trades: is workers' compensation coverage current and classified correctly?

## Sources

1. Alabama Department of Labor: https://labor.alabama.gov/ (200, read 2026-10-27; links unemployment-compensation division)
2. ADOL unemployment-compensation division: https://adol.alabama.gov/divisions/unemployment-compensation/ (linked from labor.alabama.gov 2026-10-27)
3. ADOL employer partial-contribution filings: https://adol.alabama.gov/employers/unemployment-compensation-partials/ (linked 2026-10-27)
4. Ala. Code Title 25 ch. 1: https://law.justia.com/codes/alabama/title-25/ (not fetched this run — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Alabama payroll and UI questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
