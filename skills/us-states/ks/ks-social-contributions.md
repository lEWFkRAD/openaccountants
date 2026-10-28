---
name: ks-social-contributions
description: >
  Use this skill whenever asked about Kansas employer social contributions
  for tax year 2026 — state unemployment insurance (UI) contributions, the
  UI-only nature of Kansas employer social cost (no state disability, no
  paid-family-leave, no state health mandate), and the interaction with
  federal FUTA. Trigger on "Kansas unemployment insurance", "Kansas UI
  rate", "Kansas employer contributions", "K.S.A. 79-27", "KW-3 UI".
  Source-cited draft; the 2026 wage base, rate ranges and filing calendar
  are not yet confirmed (dol.ks.gov returned 403 to plain HTTP this run).
jurisdiction: US-KS
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
depends_on:
  - ks-income-tax
---

# Kansas social contributions, tax year 2026

> **Source-cited draft.** Built from the KDOR business pages and 26 U.S.C. §§ 3301 and 3302, read on 2026-10-28. The Kansas UI program pages (dol.ks.gov) returned 403 Forbidden to plain HTTP and the statute page tried served a JS shell, so no Kansas UI figure is confirmed yet: see the Not yet confirmed line. No accountant has reviewed it. Do not rely on it without review by a qualified Kansas professional.

Tax year: the calendar year. Currency: US dollars. Kansas has **no state-run social insurance beyond unemployment insurance**: no state disability insurance, no paid family and medical leave program, no individual health-coverage mandate. Employer social cost above federal FICA / FUTA is **UI contributions only**.

See also: `ks-payroll`, `ks-income-tax`.

## Who this applies to

- **Covered employers:** employers paying Kansas wages must register and pay Kansas UI contributions, with quarterly wage reporting (the coverage threshold is listed under Not yet confirmed).
- **Federal layer:** FUTA applies at 6.0% of FUTA wages, with credit for state contributions capped at 90% of that tax, i.e. 5.4% (26 U.S.C. §§ 3301, 3302(c)(1)).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| FUTA gross rate | 6.0% | 2026 | [26 U.S.C. § 3301](https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleC-chap23-sec3301.htm) |
| Maximum credit for state contributions | 90% of the FUTA tax (5.4% of FUTA wages) | 2026 | [26 U.S.C. § 3302(c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleC-chap23-sec3302.htm) |

No Kansas UI figure for 2026 — taxable wage base, experience-rated schedule, new-employer rate, any employee share or any surcharge — is confirmed yet; each is listed on the Not yet confirmed line.

## The taxable base

Kansas UI contributions are charged on each employee's Kansas wages up to an annual per-employee taxable wage base; the 2026 base itself is listed under Not yet confirmed. Multi-state employers apply the Kansas base and rate to Kansas wages only; other states' bases differ, so file per state.

## Deadlines and filing

No Kansas UI filing calendar is confirmed in this skill. The quarterly report and payment dates, the annual rate notice and its protest window, and the annual wage report for experience rating are listed under Not yet confirmed.

## Penalties and interest

- Misclassifying employees as independent contractors triggers back contributions. KDOR publishes Misclassification Statistics and Employment Tax Delinquencies pages ([KDOR business navigation](https://www.ksrevenue.gov/business.html)).
- Late-report and late-payment penalty and interest percentages, and misclassification penalty tiers, are listed under Not yet confirmed.

## Cross-border points

- Multi-state employers: Kansas base and rate apply to Kansas wages; other states' bases differ — file per state.
- No Kansas portability issue for Social Security / Medicare — federal only.
- How Kansas localizes the work of remote employees is listed under Not yet confirmed.

## Worked examples

The base and rate in these examples are **illustrative placeholders**, not the confirmed Kansas 2026 figures (see Not yet confirmed). They show the mechanics: contributions run on wages up to the per-employee base, times the employer's rate.

### Example 1: single-employee UI cost

One employee earns $180,000 of Kansas wages. With an illustrative base of $15,000 and an illustrative experience rate of 2.1%, taxable wages are capped at $15,000 and the UI contribution is $315.

```oa-check
name: KS UI employer contribution (illustrative)
inputs:
  wages: 180000
  base: 15000
  rate: 0.021
steps:
  - taxable: min(wages, base)
  - ui: taxable * rate
expected:
  taxable: 15000
  ui: 315
```

### Example 2: two-employee small employer

Same facts, two employees each above the base: the cost doubles to $630, because the base applies per employee.

```oa-check
name: KS UI two employees
inputs:
  per_employee_ui: 315
  employees: 2
steps:
  - total: per_employee_ui * employees
expected:
  total: 630
```

## Ask the client first

1. **Kansas payroll footprint and headcount?** Which states' bases apply.
2. **Experience-rating history and successor-ownership changes?** They drive the rate.
3. **Worker classification posture (W-2 vs 1099)?** KDOR misclassification exposure.
4. **Does FUTA credit-reduction status affect 2026 federal cost?**

## Sources

| Source | URL | Read on |
|---|---|---|
| KDOR business navigation (Misclassification Statistics; Employment Tax Delinquencies) | https://www.ksrevenue.gov/business.html | 2026-10-28 |
| 26 U.S.C. § 3301 (FUTA rate 6.0%) | https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleC-chap23-sec3301.htm | 2026-10-28 |
| 26 U.S.C. § 3302 (credit cap 90% of the tax) | https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleC-chap23-sec3302.htm | 2026-10-28 |

Not yet confirmed: the 2026 Kansas UI taxable wage base (recent years were described in v0.1 as in the $15,000 range); the experience-rated contribution schedule and the new-employer rate for the first coverage years; that Kansas imposes no employee UI premium; any suspense or financing surcharge (historically added in years with a federal loan balance); the coverage threshold for registration; aggregation of successors and common-owner groups for experience rating; FUTA credit-reduction status for 2026; the quarterly UI report and payment due dates (v0.1: last day of the month after each quarter); the annual rate notice and its protest window; the annual wage report for experience rating with the Q4 filing; late-report and late-payment penalty and interest percentages and misclassification penalty tiers; Kansas adoption of the federal four-part localization-of-work tests for remote workers; which agency administers Kansas UI (v0.1 said the Labor Services division of KDOR, but KDOR's business page does not show it and the UI program pages are on dol.ks.gov); and the statutory citation (v0.1 cited K.S.A. 79-27 and 79-27-105, whose kslegislature.org page served only a JS shell; the Kansas Employment Security Law in K.S.A. chapter 44 should be checked).

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
