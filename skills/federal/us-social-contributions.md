---
name: us-social-contributions
description: >
  US federal social contributions (FICA and SE tax) reference for 2026.
  Covers Social Security and Medicare rates for employees and
  employers, the self-employment tax computation with the 92.35% net
  earnings adjustment, the additional Medicare tax thresholds, FUTA
  unemployment tax, Form 941/940 filing cadence, and the employment
  tax penalty regime. Trigger on US social security tax, FICA,
  Medicare tax, SE tax, self-employment tax, FUTA, wage base.
  Source-cited draft.
jurisdiction: US
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# US federal social contributions (FICA / SE tax)

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the IRS self-
employment tax page, the IRS employment-taxes page, the About Form 941
and About Form 940 pages, and this repo's hand-authored, CPA-reviewed
`packages/us-federal/rates.2026.json` (payroll_and_se block). Statutes:
IRC §§3101–3128 (FICA), §1401–1403 (SE tax), §3301–3311 (FUTA).

**Source status caveat:** the SSA pages that publish the 2026 Social
Security wage base (ssa.gov COLA/fact-sheet pages) returned 403 to
this drafting environment, and `rates.2026.json` carries the 2026 wage
base as an open TODO. The IRS SE-tax page still quotes the **$168,600
(2025) base**. Every wage-base figure below is therefore flagged:
**2026 wage base needs-sources** — confirm against the SSA annual fact
sheet before relying on it.

## 2. Who the rules apply to

- **Employees and employers.** FICA: Social Security (OASDI) and
  Medicare taxes, imposed in equal shares on wages. The employer
  withholds the employee share and remits both.
- **Self-employed persons.** SE tax is the functional equivalent —
  15.3% on net earnings from self-employment, with a deduction-side
  adjustment instead of an employer share.
- **Employers also pay FUTA**, a federal unemployment tax on the
  employer only, largely offset by the state-unemployment credit.

## 3. Rates table

| Item | Rate / amount | Source |
|---|---|---|
| Social Security — employee | 6.2% of wages up to the wage base | IRC §3101(a); rates.2026.json |
| Social Security — employer | 6.2% (matching) | IRC §3111(a); rates.2026.json |
| Social Security wage base, 2025 | $168,600 | IRS SE-tax page (read 2026-10-24) |
| Social Security wage base, 2026 | **needs-sources** (SSA fact sheet 403 this pass; rates.2026.json TODO) | SSA annual fact sheet |
| Medicare — each side | 1.45%, no wage cap | IRC §§3101(b), 3111(b); rates.2026.json |
| Additional Medicare tax | 0.9% on wages above $200,000 (single) / $250,000 (MFJ) / $125,000 (MFS) — employee only, no employer match | IRC §3101(b)(2); rates.2026.json (statutory, not indexed) |
| SE tax combined | 15.3% = 12.4% OASDI + 2.9% Medicare | IRC §1401; IRS SE-tax page |
| SE net-earnings adjustment | net profit × 92.35% | IRC §1402(a)(12); rates.2026.json |
| SE OASDI cap | 12.4% part stops once wages + SE earnings reach the wage base | IRS SE-tax page |
| SE filing threshold | $400 net earnings from self-employment | IRC §1402(a); rates.2026.json |
| FUTA | 6.0% on first $7,000 per employee, less credit up to 5.4% → 0.6% net in credit states | IRC §§3301, 3302; rates.2026.json |

## 4. Tax base and computation

- **FICA base:** wages as defined in §3121; Social Security stops at
  the annual wage base (per employee, per year), Medicare never stops.
  The additional 0.9% Medicare applies on wages above the filing-
  threshold amounts; employers withhold it above $200,000 but the
  final liability is reconciled on Form 1040 by filing status.
- **SE base:** net earnings = net self-employment profit × 92.35%
  (the deemed employer-equivalent adjustment); the 12.4% part is
  reduced by FICA wages already taxed in the same year. Half of SE tax
  is deductible for income tax (§164(f)).

## 5. Deadlines

- **Form 941** (employer quarterly FICA + income-tax withholding):
  due the last day of the month following each quarter — April 30,
  July 31, October 31, January 31 (About Form 941; deposits follow the
  semi-weekly/monthly schedule on that page).
- **Form 940** (FUTA): annual, due January 31 (February 10 if all
  deposits were timely — About Form 940).
- **SE tax:** computed on Schedule SE with the Form 1040 return;
  paid through quarterly estimated payments (see
  us-quarterly-estimated-tax).

## 6. Penalties and interest

Employment-tax failures stack: failure-to-deposit, failure-to-file
(2–5% escalating), failure-to-pay (0.5%/month), and the federal tax
deposit penalty for late deposits; interest runs on unpaid amounts.
Exact percentage tiers: **needs-sources** (IRS penalties pages did not
resolve this pass — confirm against the employment-taxes page links).
Trust-fund recovery: the unpaid employee-share withholding is
personal to the responsible person.

## 7. Cross-border interaction

Nonresident aliens on US wages pay FICA unless a totalization
agreement or treaty provision applies; US citizens working abroad for
a foreign employer pay US SE tax unless a totalization agreement
exempts them. See us-citizen-moving-abroad-tax and
us-form-941-940-payroll.

## 8. Worked examples

**Example 1 — sole proprietor, SE tax.** Net self-employment profit
$120,000, no wages. Net earnings = 120,000 × 92.35% = $110,820; SE tax
= 110,820 × 15.3% = $16,955.46 (below the wage base, so the full 12.4%
OASDI part applies).

```oa-check
name: SE tax on 120k profit
inputs:
  profit: 120000
  adj: 0.9235
  se_rate: 0.153
steps:
  - net_earnings: profit * adj
  - se_tax: net_earnings * se_rate
expected:
  net_earnings: 110820.00
  se_tax: 16955.46
```

**Example 2 — employer FICA on a $250,000 wage (2025 base).** Social
Security 6.2% capped at the $168,600 base = $10,453.20; Medicare 1.45%
uncapped on $250,000 = $3,625.00; employer total = $14,078.20 (the
0.9% additional Medicare is the employee's, not the employer's).

```oa-check
name: employer FICA 250k wage 2025 base
inputs:
  wage: 250000
  base_2025: 168600
  ss: 0.062
  med: 0.0145
steps:
  - ss_part: min(wage, base_2025) * ss
  - med_part: wage * med
  - total: ss_part + med_part
expected:
  ss_part: 10453.20
  med_part: 3625.00
  total: 14078.20
```

## 9. Ask the client first

1. Any W-2 wages in the same year as SE income — they shrink the 12.4%
   SE part; do you have the wage figures?
2. Household employees, or a spouse/partner draw — FICA still applies;
   is anyone being paid outside payroll?
3. Are wages above $200,000 — additional Medicare withholding and the
   1040 reconciliation need checking.
4. Multi-state or foreign workers — totalization agreements and state
   SUTA credits change the FUTA/SUTA math.

## 10. Sources

- [IRS — Self-employment tax (Social Security and Medicare taxes)](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) — read 2026-10-24 (15.3% rate; $168,600 base quoted).
- [IRS — Employment taxes](https://www.irs.gov/businesses/small-businesses-self-employed/employment-taxes) — read 2026-10-24.
- [IRS — About Form 941](https://www.irs.gov/forms-pubs/about-form-941) — read 2026-10-24.
- [IRS — About Form 940](https://www.irs.gov/forms-pubs/about-form-940) — read 2026-10-24.
- `packages/us-federal/rates.2026.json` — payroll_and_se block (rates.2026.json marks the 2026 wage base as an open TODO pending the SSA fact sheet).
- SSA COLA pages — 403 to this environment 2026-10-24; **2026 wage base needs-sources**.

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
