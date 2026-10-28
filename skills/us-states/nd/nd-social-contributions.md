---
name: nd-social-contributions
description: >-
  Use when an employer needs the 2026 North Dakota answer on state-level
  social contributions: North Dakota has no employee-side social
  contribution, no state disability insurance and no paid-family-leave
  payroll tax — the only state-level social contribution is the
  employer-only unemployment insurance tax administered by Job Service ND
  under N.D.C.C. Ch. 52-8 (quarterly Form SFN 41263 via UI EASY, new
  employer rates 1.02% non-construction / 6.09% construction on the
  2025 $45,100 taxable wage base). Trigger on North Dakota UI tax, ND
  SUTA, new employer rate, Job Service ND, SFN 41263, UI EASY.
  Source-cited draft; 2026 wage base and rates need confirmation.
jurisdiction: US-ND
category: payroll
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.2
---

# North Dakota social contributions (employer-only UI; no employee-side levy)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

Every employer liable for North Dakota unemployment insurance: any person or entity paying wages in North Dakota that meets the coverage tests of N.D.C.C. Ch. 52-8 (Employment Security). North Dakota is an **employer-only** state for social contributions — there is no state-level employee payroll contribution of any kind. Reimbursement-base governmental and certain nonprofit employers elect reimbursement instead of contribution financing (Job Service ND employer's guide).

## 2. Core rules and rates

- **No employee-side social contribution.** No state disability insurance (contrast NY), no paid-family-leave payroll tax (contrast NY, WA), no state retirement contribution. FICA/FUTA are federal and outside this skill. _(N.D.C.C. Ch. 52-8; corroborated by absence of any employee payroll levy in the ND Tax Commissioner materials, read 2026-10-25)_
- **UI taxable wage base.** The base "is determined yearly and equals 70% of the calculated statewide average annual payroll" — Job Service ND, "Determination of Taxable Wage Base," verified 2026-10-25. The **2025 base is $45,100** (corroborated by the existing `nd-payroll` skill, T1-ND-PAY-06); the **2026 base: needs-sources** (Job Service ND rate-notice page not located on 2026-10-25).
- **New employer rates.** Non-construction new employers: **1.02%**; construction new employers: **6.09%** — carried from the existing `nd-payroll` skill with [VERIFY] against the 2025 JSND rate schedules; **2026 schedules: needs-sources**. _(jobsnd.com "Learn About Taxes" confirms new-employer classification mechanics, verified 2026-10-25)_
- **Experience rating.** Rates are re-determined each calendar year based on the employer's history as of the preceding June 30; an employer remains a "new employer" until liable for the period ending the prior June 30 (typically 3 full fiscal years). _(jobsnd.com/unemployment-business-tax/learn-about-taxes, verified 2026-10-25)_
- **Rate range for experience-rated employers:** the existing `nd-payroll` skill carries the schedule with [VERIFY]; the statutory min/max: **needs-sources**.

## 3. Base and adjustments

- Base: each employee's wages up to the calendar-year taxable wage base. Wages follow the Ch. 52-8 definition (remuneration for personal services; exclusions per statute).
- Contributions are computed per employee: taxable wages × assigned rate. No employee withholding, no employee W-2 Box 14 state social line (contrast NY PFL/SDI).
- Voluntary contribution account (VCA) and reimbursement options exist for eligible employers (employer's guide; details **needs-sources**).

## 4. Deadlines

- **Quarterly Form SFN 41263** (Employer's Contribution and Wage Report): due the **last day of the month following the calendar quarter** (Apr 30, Jul 31, Oct 31, Jan 31). Mandatory electronic filing via **UI EASY** for all employers. _(existing `nd-payroll` skill, corroborated by jobsnd.com "File Reports" hub, verified 2026-10-25)_
- Annual rate notices issue in November/December for the following calendar year (existing `nd-payroll` skill; protest window per notice).
- New-employer liability begins with the first quarter in which the coverage test is met; register via Job Service ND.

## 5. Penalties and interest

- Late quarterly reports/contributions: penalty plus interest per Ch. 52-8; the exact 2026 published penalty/interest percentages: **needs-sources** (Ch. 52-8 text at ndlegis.nd.gov unreachable on 2026-10-25 — DNS failure).
- Fraudulent reporting and misclassification (employee vs independent contractor) carry separate Ch. 52-8 sanctions; construction project risk protection rules apply to contractors (jobsnd.com "Comply with Construction Project Risk Protection," verified 2026-10-25).

## 6. Cross-border and federal overlay

- Multi-state employers: ND UI applies to services performed in ND; reciprocal-state wage rules do not affect UI (UI follows the work-location/coverage tests, not income-tax reciprocity).
- Federal FUTA credit reduction interacts with the state UI system; ND's credit-reduction status each year: check the DOL list (federal skill).
- No state PFL/SDI means no interaction with the federal FMLA beyond unpaid-leave protection.

## 7. Worked examples

**Example 1 — two new non-construction employees, 2025 base.** New employer (non-construction), rate 1.02%, 2025 taxable wage base $45,100, two employees each earning over the base.

```oa-check
name: nd ui new employer two employees
inputs:
  base: 45100
  employees: 2
  rate: 0.0102
steps:
  - tax: base * employees * rate
expected:
  tax: 920.04
```

**Example 2 — new construction employer.** Same base, construction new-employer rate 6.09%, one employee over the base.

```oa-check
name: nd ui new construction employer
inputs:
  base: 45100
  rate: 0.0609
steps:
  - tax: base * rate
expected:
  tax: 2746.59
```

(2026 figures will differ once Job Service ND publishes the 2026 base and schedules — recompute before relying.)

## 8. Ask the client first

1. Is the employer construction or non-construction? (Different new-employer rate and project risk-protection rules.)
2. Are workers correctly classified as employees for Ch. 52-8? (Misclassification is the top ND UI audit issue.)
3. Reimbursement or contribution financing — which election is on file?
4. Multi-state: are ND wages being reported to another state's UI system by mistake?
5. Has the 2026 rate notice been reviewed and, if wrong, protested within the notice window?

## 9. Sources

- Job Service ND — Learn About Taxes (taxable wage base formula, new-employer and experience-rating mechanics): <https://www.jobsnd.com/unemployment-business-tax/learn-about-taxes> — 200 with text, 2026-10-25.
- Job Service ND — site root and unemployment-business-tax hub (file reports, employer's guide, construction risk protection): <https://www.jobsnd.com/> — 200, 2026-10-25.
- Existing `nd-payroll` skill (2025 wage base $45,100; SFN 41263 mechanics; new-employer rates with [VERIFY]) — read 2026-10-25.
- N.D.C.C. Ch. 52-8 (Employment Security): **needs-sources** — ndlegis.nd.gov DNS failure on 2026-10-25; statutory min/max rates and penalty percentages unverified.
- 2026 ND UI taxable wage base and rate schedules: **needs-sources** (not published on the pages located 2026-10-25).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
