---
name: az-income-tax
description: Use this skill whenever asked about Arizona individual income tax for self-employed individuals or sole proprietors — filing Form 140, AZ estimated tax (Form 140ES), Arizona flat tax rate, Arizona standard deduction, or any query involving Arizona state income tax compliance. Trigger on phrases like "Arizona income tax", "AZ income tax", "Form 140", "Arizona estimated tax", "Arizona self-employed tax", "AZDOR income tax", "Arizona flat tax", or "ARS §43".
jurisdiction: US-AZ
tier: 2
last_updated: 2026-10-28
version: "0.3"
validation_status: ai-drafted-q3
---

# Arizona Individual Income Tax — Self-Employed / Sole Proprietor

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Scope.** This skill covers Arizona individual income tax for self-employed individuals and sole proprietors filing Form 140. It addresses tax computation, deductions, estimated payments, and form mapping.
> **Quality tier.** Q3 — AI-drafted with citations; not independently verified by a licensed professional.

## Who this applies to

Self-employed individuals and sole proprietors who are Arizona residents filing Form 140, plus individuals who need the Arizona estimated-payment rules. Part-year residents and nonresidents file Form 140NR — see `az-cross-border`.

**At a glance**

| Field | Value |
|---|---|
| Jurisdiction | Arizona, United States |
| Jurisdiction code | US-AZ |
| Tax authority | Arizona Department of Revenue (AZDOR) |
| Filing portal | https://www.aztaxes.gov |
| Legislation citation | Arizona Revised Statutes Title 43 (Taxation of Income) |
| Primary form | Form 140 — Arizona Resident Personal Income Tax |
| Filing deadline | April 15 (follows federal deadline) |
| Version | 0.3 |
| Generated | 2026-10-28 |
| Validation status | AI-drafted — Q3 |

## Rates, bands and thresholds

### Tax rate

Arizona imposes a **flat income tax rate of 2.5%** on all taxable income, regardless of filing status or income level. AZDOR's Individual Income Tax Highlights page (read 2026-10-28) confirms the "2025 New Tax Rate of 2.5% for All Income Levels and Filing Status" and that "The Optional Tax Table and the X and Y Tax Table are now obsolete."

| Filing status | Rate | Applies to |
|---|---|---|
| All statuses | 2.5% | All Arizona taxable income |

### Standard deduction (TY 2025)

| Filing status | Standard deduction |
|---|---|
| Single | $15,750 |
| Married Filing Jointly | $31,500 |
| Married Filing Separately | $15,750 |
| Head of Household | $23,625 |

Source: AZDOR Individual Income Tax Highlights (read 2026-10-28): "The 2025 Arizona standard deduction amounts are: $15,750 for a single taxpayer or a married taxpayer filing a separate return; $31,500 for a married couple filing a joint return; and $23,625 for individuals filing a head of household return."

Arizona also allows a **Standard Deduction Increase** equal to 34% of qualifying charitable contributions (TY 2025), calculated on page 3 of Form 140. Source (read 2026-10-28): "For tax year 2025, the allowable portion of your charitable contributions used to compute your Standard Deduction Increased was increased from 33% to 34% of the qualified charitable contributions made during the tax year."

### Personal exemptions

Arizona does not use personal exemptions in the traditional sense. The standard deduction effectively replaces the exemption for most filers.

## The taxable base

### How this skill works with the federal return

1. **Starting point:** Arizona begins with **federal adjusted gross income** (federal Form 1040, Line 11).
2. **Arizona additions:** Add back amounts deducted federally but not recognized by Arizona (e.g., other states' municipal bond interest).
3. **Arizona subtractions:** Subtract Arizona-exempt income (e.g., Social Security benefits, U.S. government interest, Arizona-specific exclusions).
4. **Arizona AGI:** Federal AGI ± additions/subtractions.
5. **Deductions:** Subtract standard deduction or Arizona itemized deductions.
6. **Result:** Arizona taxable income × 2.5% = tax liability.

### Self-employed specific rules

**Federal conformity**
- Arizona generally conforms to the Internal Revenue Code as of a specific date (rolling conformity with some exceptions).
- Schedule C business income and deductions flow through federal AGI into Arizona's computation.

**QBI deduction (§199A)**
- The federal QBI deduction reduces federal taxable income but does **not** directly apply to Arizona's computation since Arizona starts from federal AGI (above the line).
- However, Arizona allows its own subtraction for certain small business income (see the Not yet confirmed line).

**SE health insurance deduction**
- Flows through federal AGI (above-the-line deduction) and is automatically reflected in Arizona's starting point.

**Retirement contributions**
- SEP-IRA and Solo 401(k) contributions reduce federal AGI and therefore reduce Arizona starting income.

**Home office deduction**
- Federal home office deduction (simplified or actual) flows through Schedule C and is reflected in federal AGI.

### Tier 1 rules — deterministic

| # | Rule | Logic |
|---|---|---|
| T1-01 | Apply 2.5% flat rate to Arizona taxable income | Single rate × taxable income |
| T1-02 | Standard deduction by filing status | Fixed amounts: $15,750 / $31,500 / $23,625 |
| T1-03 | Social Security benefits fully exempt | Subtract from AZ computation |
| T1-04 | U.S. government bond interest exempt | Subtract from AZ income |
| T1-05 | Estimated tax threshold | Gross income > $75,000 (single) or $150,000 (MFJ) |
| T1-06 | Standard deduction increase | Add 34% of qualifying charitable contributions |

### Tier 2 rules — requires judgment

| # | Rule | Why judgment needed |
|---|---|---|
| T2-01 | Standard deduction vs. itemized | Taxpayer must compare both methods |
| T2-02 | IRC conformity date issues | Some federal provisions may not be adopted; requires checking current conformity |
| T2-03 | Part-year resident allocation | Requires apportionment of income to AZ residency period |
| T2-04 | Small Business Income Tax election | Taxpayer may elect to pay the flat rate separately on business income — requires evaluation of benefit (see the Not yet confirmed line) |
| T2-05 | Credit for taxes paid to other states | Requires analysis of multistate income sourcing (Form 309) |
| T2-06 | Charitable contribution substantiation | Standard deduction increase requires documentation of qualified contributions |

## Deadlines and filing

- **Form 140 (calendar year):** due April 15, following the federal deadline (AZDOR highlights page, read 2026-10-28: "Your 2025 individual income tax return is due by midnight on April 15, 2026").
- **Estimated tax payments (Form 140ES):**
  - **Required if:** your Arizona gross income exceeds $75,000 (single/MFS/HOH) or $150,000 (MFJ) for the current or prior year. AZDOR's estimated-payments page (read 2026-10-28): "You must make Arizona estimated income tax payments during 2026 if: ... Single $75,000 $75,000; Married Filing Joint $150,000 $150,000 ... Head of Household $75,000 $75,000" (prior-year and current-year gross income both above the threshold).
  - **Safe harbor:** total estimated payments + withholding must equal the lesser of 90% of current year tax or 100% of prior year tax. AZDOR (read 2026-10-28): "your payments, when added to your Arizona withholding, must total either 90% of the tax due for the current calendar year, or 100% of the tax due for the prior calendar year."
  - **Due dates:** April 15, June 15, September 15, January 15. AZDOR (read 2026-10-28): "Estimated tax payments are due April 15, June 15, September 15, 2026, and January 15, 2027."
  - **Payment methods:** online via AZTaxes.gov or mail Form 140ES to AZDOR.
  - **Small business variant:** Form 140ES-SBI for those electing the small business income tax (see the Not yet confirmed line).

### Form mapping

| Computed value | Form 140 line |
|---|---|
| Federal AGI | Line 12 |
| Arizona additions | Line 13 |
| Arizona subtractions | Line 15 |
| Arizona adjusted gross income | Line 16 |
| Standard or itemized deduction | Line 18 |
| Arizona taxable income | Line 19 |
| Tax (2.5% × Line 19) | Line 20 |
| Credits | Lines 21–30 |
| Estimated payments + withholding | Lines 40–43 |
| Balance due / refund | Lines 52–56 |

### Supplier pattern library

| Pattern on bank/CC statement | Likely meaning |
|---|---|
| `AZ DEPT OF REVENUE` / `AZDOR` | Arizona income tax payment (estimated or balance due) |
| `AZTAXES.GOV` | Electronic payment via AZTaxes portal |
| `STATE OF AZ TAX` | State tax payment |
| `ARIZONA DOR` | Department of Revenue payment |

## Penalties and interest

Interest on under- and overpayments tracks the federal short-term rate plus three percentage points, compounded annually (AZDOR interest-rate page, read 2026-10-28: "that rate of interest for both overpayments and underpayments for all taxpayers is the federal short-term rate, determined by the IRC, plus three percentage points"; 2026 quarterly table rows: first quarter 7%, second quarter 6%, third and fourth quarters 7%). Late-filing and underpayment penalty percentages are not tied out this run — see the Not yet confirmed line.

## Cross-border points

- Multistate business activity requiring apportionment: refuse and escalate (R-01); see `az-cross-border` for the nonresident/part-year rules.
- Part-year residents (Form 140PY/140NR) with complex sourcing: escalate (R-02).
- Credit for income taxes paid to another state: Form 309 — requires multistate sourcing analysis (see the Not yet confirmed line).
- Reciprocal-agreement treatment of wages earned across state lines: Arizona has no reciprocal agreement treatment tied out this run — see the Not yet confirmed line.

## Worked examples

### Example 1: single filer, Arizona taxable income $60,000 (client facts hypothetical)

```oa-check
name: single filer 60000 at 2.5 percent
inputs:
  taxable_income: 60000
  rate: 0.025
steps:
  - tax: taxable_income * rate
expected:
  tax: 1500.00
```

### Example 2: standard deduction and the charitable-contribution increase (client facts hypothetical)

A single filer with federal AGI $70,000, no Arizona additions/subtractions, and $2,000 of qualifying charitable contributions:

```oa-check
name: standard deduction increase at 34 percent
inputs:
  agi: 70000
  std_deduction: 15750
  contributions: 2000
  increase_share: 0.34
  rate: 0.025
steps:
  - increase: contributions * increase_share
  - taxable: max(0, agi - std_deduction - increase)
  - tax: taxable * rate
expected:
  increase: 680.00
  taxable: 53570.00
  tax: 1339.25
```

## Ask the client first

- Filing status, and any mid-year residency change (Form 140 vs 140PY/140NR)?
- Arizona additions or subtractions (municipal-bond interest from other states, Social Security, U.S. government interest)?
- Qualifying charitable contributions for the standard-deduction increase (documentation per T2-06)?
- Expected liability — does the estimated-payment threshold apply (T1-05)?
- Considering the Small Business Income Tax election or Form 309 credit? Escalate (R-03/T2-05).

### Refusal catalogue

This skill must refuse and recommend professional review when:

| # | Condition |
|---|---|
| R-01 | Taxpayer has multistate business activity requiring apportionment |
| R-02 | Taxpayer is a part-year resident (Form 140PY) with complex sourcing |
| R-03 | Taxpayer is considering the Small Business Income Tax election and needs cost-benefit analysis |
| R-04 | Issues involving Arizona tax credits (solar, research, qualified facilities, etc.) |
| R-05 | Taxpayer has Arizona net operating loss carryforward |
| R-06 | Questions about TPT (Transaction Privilege Tax) nexus or classification |
| R-07 | Audit representation or controversy matters |
| R-08 | Any question about tax fraud, evasion, or aggressive positions |

### Prohibitions

- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the model.
- NEVER apply a graduated rate table -- Arizona's individual rate is flat (the optional tax tables are obsolete per AZDOR).
- NEVER treat out-of-state municipal-bond interest as Arizona-exempt -- it is an addition.
- NEVER advise on multistate apportionment, the SBI election, or credits without escalation (R-01..R-05).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| AZDOR — Individual Income Tax Highlights | https://azdor.gov/forms/individual-income-tax-highlights | 2026-10-28 |
| AZDOR — Individual Estimated Tax Payments | https://azdor.gov/individuals/individual-estimated-tax-payments | 2026-10-28 |
| AZDOR — Individual Forms hub (Form 140) | https://azdor.gov/forms/individual | 2026-10-28 |
| AZDOR — Interest Rates | https://azdor.gov/business/interest-rates | 2026-10-28 |

Not yet confirmed: Arizona itemized-deduction rules and the IRC conformity date; late-filing and underpayment penalty percentages; the Small Business Income Tax (SBI) election mechanics and Form 140ES-SBI details; the credit for taxes paid to other states (Form 309) mechanics; whether Arizona wages earned across state lines receive any reciprocal-agreement treatment; 2026 standard-deduction amounts (the highlights page states 2025 amounts); Form 140 line numbers for tax years after 2025.

## Talk to a verified accountant

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
