---
name: dc-unemployment-contributions
description: >
  Use this skill whenever asked about District of Columbia employer
  social contributions for tax year 2026 -- unemployment insurance
  contributions administered by the Department of Employment Services
  (DOES): the employer-only UI tax on the first $9,000 of wages, the
  2.7% new-employer rate and experience rating, the 0.2% administrative
  assessment, and DC's Universal Paid Family Leave (PFL) 0.62%
  employer-paid contribution. Trigger on "DC UI rate", "DC SUTA",
  "District of Columbia unemployment wage base", "DC paid family
  leave", "DC PFL", "DC employer taxes", "DC DOES UI".
jurisdiction: US-DC
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - dc-income-tax
---

# District of Columbia social contributions (UI + Paid Family Leave), tax year 2026

> **Source-cited draft.** Built from the DOES UI Handbook for Employers, DOES Employer Tax Information and Tax Rate Questions pages, the DOES Paid Family Leave Employer Toolkit, and D.C. Code § 32-541.03(Perm), read on 2026-10-28. No accountant has reviewed it. Do not run a payroll from it without review by a qualified professional.

DC employer social contributions: **unemployment insurance (UI)** under D.C. Code Title 51 ch. 1, administered by the **Department of Employment Services (DOES)**, and the **Universal Paid Leave (PFL)** contribution under D.C. Code § 32-541.03(Perm), administered by the DOES Office of Paid Family Leave. DC has **no temporary disability insurance program**; the OTR "Notice of Delinquency (TDI)" page is a delinquent-**return** notice program (it lists employer withholding tax among the covered tax types), not a disability premium (OTR page, read 2026-10-28). Federal FICA/FUTA sits on top; workers' compensation is separate (see the Not yet confirmed line).

## Who this applies to

- Employers covered under D.C. Code Title 51 ch. 1. "The cost of the unemployment insurance program is financed by employers who pay state and federal taxes on part of the wages paid to each employee" ([DOES Employer Tax Information page](https://does.dc.gov/service/employer-tax-information-unemployment-insurance)). Out-of-state employers with DC employees register with DOES even with no DC office.
- The UI contribution is **employer-only** -- "Employees are not taxed" (DOES Employer Tax Information page).
- **Paid Family Leave:** "All District of Columbia private sector employers must participate in this program"; covered employers "include all DC employers subject to DC Unemployment Insurance (UI) tax and self-employed individuals who choose to opt in" ([DOES PFL Employer Toolkit](https://does.dc.gov/sites/default/files/dc/sites/does/page_content/attachments/DOES_PFL_EmployerToolkit.pdf)). In general, covered workers are those who predominantly work in DC and no more than 50% in another jurisdiction.

## Rates, bands and thresholds

| Item | 2026 amount | Source |
|---|---|---|
| UI taxable wage base | **$9,000** -- "on the first $9,000 of wages paid to each employee" | [DOES Employer Tax Information page](https://does.dc.gov/service/employer-tax-information-unemployment-insurance); [UI Handbook](https://does.dc.gov/sites/default/files/dc/sites/does/publication/attachments/UI%20Employer%20Handbook%20-MASTER2-FINAL.pdf): "payable, at the assigned rate, on the first $9,000 paid to each covered employee during the calendar year" |
| New-employer rate | **2.7% or the average rate paid by all employers the preceding year, whichever is higher** | [UI Handbook](https://does.dc.gov/sites/default/files/dc/sites/does/publication/attachments/UI%20Employer%20Handbook%20-MASTER2-FINAL.pdf); [DOES Tax Rate Questions](https://does.dc.gov/service/tax-rate-questions): "a standard tax rate equal to the average rate of contributions paid by all employers during the preceding year, or 2.7 percent, whichever is higher" |
| Experience rate | Rated on experience after about 36 months of liability; each calendar year one of six tax tables applies, selected by the Trust Fund balance as of the prior 30 September | UI Handbook; DOES Tax Rate Questions |
| Administrative assessment | **0.2%** of taxable wages each quarter, by rated and reimbursable employers alike, "a maximum payment of $18 for each employee" | UI Handbook: "an administrative assessment of two-tenths of one percent (0.2%) on taxable wages reported each quarter" |
| PFL contribution | **0.62%** of each covered employee's wages, **no wage cap** | [D.C. Code § 32-541.03(Perm)](https://code.dccouncil.gov/us/dc/council/code/sections/32-541.03(Perm)): "A covered employer shall contribute an amount equal to 0.62% ... of the wages of each of its covered employees"; PFL Employer Toolkit: "PFL contributions do not have a cap on the amount of wages/earnings subject to the tax" |
| PFL funding split | **100% employer funded**; "employers cannot deduct the contributions from payments to their workers" | PFL Employer Toolkit: "The contributions are 100% employer funded" |

## The taxable base

- **UI:** wages paid to each covered employee during the calendar year, up to $9,000 (UI Handbook). Wages are only taxable once during a year regardless of whether they were reported to another state. The 0.2% administrative assessment is additional and applies to the same first $9,000 (maximum $18 per employee per year).
- **PFL:** the same gross wages reported for quarterly UI filings, but with **no cap** (PFL Employer Toolkit: "the reported wages for their covered workers will be the same gross wages they report for their quarterly Unemployment Insurance (UI) filings"). The 0.62% is employer-paid and cannot be withheld from the worker.

## Deadlines and filing

- **Quarterly UI Contribution and Wage Report (Form UC-30):** due dates are **April 30, July 31, October 31 and January 31** (UI Handbook filing schedule). Household employers may elect annual filing on Form UC-30H.
- **Annual rate notice:** Tax Rate Notices (Form UC-632 or UC-632A) are mailed in December or January; a written application for review must be filed with DOES within 30 days of the notice (UI Handbook).
- **PFL wage reports and contributions:** quarterly; "Wage reports and contributions are due the day after a quarter ends" and are late if not filed "by the last day of the month following the close of a quarter" (PFL Employer Toolkit).

## Penalties and interest

- Late UI filings and payments draw Title 51 penalties and interest (specific percentages are on the DOES notices; see the Not yet confirmed line).
- OTR's "Notice of Delinquency (TDI)" program: OTR "sends a Notice of Delinquency (TDI) when a taxpayer has failed to file a business tax return or extension by the due date", with **Employer Withholding Tax** among the covered tax types ([OTR Notice of Delinquency (TDI) page](https://otr.cfo.dc.gov/page/notice-delinquency-tdi), read 2026-10-28). This is a delinquent-return enforcement notice, not a disability-insurance premium.
- Common failure modes: (1) multi-state payroll teams missing the DC PFL contribution entirely because few other jurisdictions have an analog; (2) accruing UI on gross payroll instead of the $9,000 wage base; (3) remote workers performing DC work without a DOES registration; (4) assuming the employee can be charged the 0.62% -- they cannot.

## Cross-border points

- Employers with DC-located employees register with DOES even with no DC office.
- PFL "applies to work performed in DC"; covered workers are those who predominantly work in DC and no more than 50% in another jurisdiction (PFL Employer Toolkit) -- telecommuter splits matter.
- UI wages are taxable once a year even if already taxed in another state (DOES Tax Rate Questions examples).

## Worked examples

Client facts below are hypothetical; all rates and thresholds are the confirmed figures from the tables above.

**An employer with 4 DC employees each paid $60,000, at the 2.7% new-employer rate on the $9,000 wage base, plus the 0.2% administrative assessment:**

```oa-check
name: DC UI contribution with administrative assessment
inputs:
  employees: 4
  wage_base: 9000
  rate: 0.027
  assessment_rate: 0.002
steps:
  - taxable: employees * wage_base
  - contribution: taxable * rate
  - assessment: taxable * assessment_rate
  - total: contribution + assessment
expected:
  taxable: 36000.00
  contribution: 972.00
  assessment: 72.00
  total: 1044.00
```

**Paid Family Leave on the same payroll (no wage cap):**

```oa-check
name: DC paid family leave contribution
inputs:
  employees: 4
  wages: 60000
  pfl_rate: 0.0062
steps:
  - covered_wages: employees * wages
  - pfl: covered_wages * pfl_rate
expected:
  covered_wages: 240000.00
  pfl: 1488.00
```

## Ask the client first

- Is the DC Paid Family Leave 0.62% in the payroll accrual -- most multi-state payrolls miss it?
- Has the DOES annual rate notice (UC-632) been reconciled to the reserve account?
- Remote workers performing DC work: registered with DOES?
- UI computed on the first $9,000 only, with the 0.2% administrative assessment added?
- Any OTR delinquency notices received for unfiled employer withholding returns?

## Sources

| Source | URL | Read on |
|---|---|---|
| DOES: UI Handbook for Employers (PDF) | https://does.dc.gov/sites/default/files/dc/sites/does/publication/attachments/UI%20Employer%20Handbook%20-MASTER2-FINAL.pdf | 2026-10-28 |
| DOES: Employer Tax Information -- Unemployment Insurance | https://does.dc.gov/service/employer-tax-information-unemployment-insurance | 2026-10-28 |
| DOES: Tax Rate Questions (UI) | https://does.dc.gov/service/tax-rate-questions | 2026-10-28 |
| DOES: Paid Family Leave Employer Toolkit (PDF) | https://does.dc.gov/sites/default/files/dc/sites/does/page_content/attachments/DOES_PFL_EmployerToolkit.pdf | 2026-10-28 |
| D.C. Code § 32-541.03(Perm) (Paid Leave contributions, 0.62%) | https://code.dccouncil.gov/us/dc/council/code/sections/32-541.03(Perm) | 2026-10-28 |
| DOES: Unemployment Compensation | https://does.dc.gov/page/unemployment-compensation | 2026-10-28 |
| OTR: Notice of Delinquency (TDI) | https://otr.cfo.dc.gov/page/notice-delinquency-tdi | 2026-10-28 |

Not yet confirmed: the 2026 experience-rate table in effect (one of six tables is selected each year by the Trust Fund balance; the 2026 table designation was not read from an archived DOES notice); the specific UI late-filing/late-payment penalty percentages under Title 51; the coverage tests and monetary thresholds in D.C. Code Title 51 ch. 1 (section text not archived this run); and the DC workers' compensation coverage threshold.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
