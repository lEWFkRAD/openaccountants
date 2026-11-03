---
name: ut-income-tax
description: Use this skill whenever asked about Utah individual income tax, Utah Form TC-40, the Utah flat tax rate, the Utah taxpayer tax credit, Utah exempt taxpayer status, or any Utah personal income tax question for sole proprietors. Trigger on phrases like "Utah income tax", "UT income tax", "Form TC-40", "Utah flat tax", "Utah taxpayer tax credit", or any request involving Utah state individual income tax computation or filing. ALWAYS load us-income-tax first for federal context.
jurisdiction: US-UT
tax_year: 2026
last_updated: 2026-11-03
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UT Income Tax

## Who this applies to

- Full-year Utah residents file the Utah individual income tax return, Form TC-40, with schedule TC-40A for adjustments and credits. Nonresidents and part-year residents use TC-40 plus TC-40B.
- Sole proprietors and single-member LLC owners file the same TC-40; the business profit flows through the federal return and starts in federal adjusted gross income.
- Utah taxes individuals at a single flat rate. There is no bracket schedule.
- A taxpayer whose federal adjusted gross income is less than or equal to the federal standard deduction is a qualified exempt taxpayer and owes no Utah income tax.

## Rates, bands and thresholds

- Tax year 2025: the rate is 4.5 percent (.045) of Utah taxable income (TC-40, line 10).
- Tax year 2026 forward: the rate is 4.45%. Utah Code 59-10-104, effective January 1, 2026, amended by Chapter 250, 2026 General Session (SB0060), sets the tax at 4.45% of state taxable income. The Tax Commission rate page still lists the rate for January 1, 2025 forward as 4.5%; the statute controls for 2026 returns.
- Rate history per the Tax Commission rate page: 4.55% for 2024, 4.65% for 2023, 4.85% for 2022, 4.95% for 2018 through 2021, and 5% for 2008 through 2017.
- Utah personal exemption: $2,111 per dependent (TC-40, line 11).
- Taxpayer tax credit (TC-40, lines 11 through 20): initial credit equals 6 percent of the total of the personal exemption plus the federal standard or itemized deduction (net of state income tax deducted federally). The credit phases out at 1.3 percent of Utah taxable income above the base phase-out amount: $18,213 single, $36,426 married filing jointly, $18,213 married filing separately, $27,320 head of household, $36,426 qualifying surviving spouse.
- Qualified exempt taxpayer thresholds (2025 worksheet): standard deduction amounts of $15,750 single, $23,625 head of household, and $31,500 married filing jointly. If federal adjusted gross income is at or below the taxpayer's standard deduction, Utah tax is zero.
- Retirement credit: up to $450 per individual, or $900 on a joint return, for taxpayers born on or before December 31, 1952, phased out by income. It cannot be combined with the Social Security benefits credit (code AH) or the military retirement credit (code AJ).

## The taxable base

- Utah starts from federal adjusted gross income, not federal taxable income. TC-40, line 4: "Enter your federal adjusted gross income (FAGI) from line 11a of your federal return". Nonresidents and part-year residents also enter their full federal AGI, then apportion on TC-40B.
- Additions (TC-40A, Part 1, TC-40 line 5) include: lump sum distribution, medical savings account addback, my529 addback, child's income excluded from parent's return, municipal bond interest, untaxed income of a resident or nonresident trust, Payroll Protection Program grant or loan addback, equitable adjustments, and tax paid on behalf of a pass-through entity taxpayer.
- Line 7 adds back any state tax refund included on the federal return.
- Subtractions (TC-40A, Part 2, TC-40 line 8) include: interest from Utah municipal bonds and U.S. Government obligations, Native American income, railroad retirement income, equitable adjustments, nonresident active duty military pay, state tax refund distributed to a trust beneficiary, nonresident military spouse income, FDIC premiums, and previously-taxed retirement income.
- Utah taxable income (line 9) is total income minus lines 7 and 8. Tax (line 10) is line 9 times the rate.
- Social Security benefits are not on the subtraction list. Utah instead offers a Social Security benefits credit (code AH) on TC-40A, Part 3.

## Deadlines and filing

- The 2025 return (filed in 2026) is due April 15, 2026.
- Utah does not require quarterly estimated tax payments. Taxpayers may prepay at any time at tap.utah.gov, or by mailing a payment with form TC-546, Individual Income Tax Prepayment Coupon.
- Extension: an automatic extension of up to six months to file, with no extension form to file. All extension returns must be filed by Oct. 15, 2026. The extension is not an extension of time to pay.
- To keep the extension penalty-free, prepay by the original due date: 90 percent of the 2025 tax due (TC-40, line 27 plus line 30), or 100 percent of the 2024 tax liability, or 90 percent of the 2025 tax due if there was no 2024 Utah liability or this is the first year filing.
- Withholding information goes on form TC-40W, attached to the return.

## Penalties and interest

- Penalties apply for not filing by the due date, not paying on time, not prepaying enough on an extension return, and not filing information returns (UCA 59-1-401). Penalties are a percentage of the unpaid tax based on the number of days late.
- The penalty for underpaying an extension prepayment is 2 percent of the unpaid tax per month of the extension period. If the return is not filed by the extension due date, failure to file and pay penalties apply as if the extension had not been granted.
- There is no late filing penalty if no tax is due on the return.
- Interest is in addition to penalties, calculated from the due date (April 15, 2026) to the date paid. The 2026 interest rate is 6 percent.

## Cross-border points

- Nonresidents and part-year residents enter full federal AGI on TC-40, then subtract the non-Utah portion on TC-40B and carry the tax back to TC-40, line 25.
- Utah taxes follow federal AGI definitions, so federal adjustments (for example, the half-of-self-employment-tax deduction) already sit inside the Utah base through AGI.
- Interest from U.S. Government obligations is subtractable in Utah; interest from other states' municipal bonds is an addition.
- Moving out of state mid-year: part-year residents prorate through TC-40B; there is no source-based shortcut at the TC-40 level.

## Worked examples

### Worked example 1: Single filer, 2025 tax year

A single filer with no dependents has federal AGI of $50,000 and takes the $15,750 standard deduction, with no additions or subtractions.

```oa-check
name: Single, FAGI 50000, 2025
inputs:
  utah_taxable: 50000
  fed_deduction: 15750
steps:
  - tax: utah_taxable * 0.045
  - initial_credit: fed_deduction * 0.06
  - phase_income: utah_taxable - 18213
  - phaseout: phase_income * 0.013
  - credit: initial_credit - phaseout
  - net_tax: tax - credit
expected:
  tax: 2250.00
  initial_credit: 945.00
  phaseout: 413.23
  credit: 531.77
  net_tax: 1718.23
```

### Worked example 2: Married couple with two dependents, 2025 tax year

A married couple filing jointly has federal AGI of $100,000, two qualifying dependents, and takes the $31,500 standard deduction. The personal exemption is $2,111 per dependent.

```oa-check
name: MFJ two dependents, FAGI 100000, 2025
inputs:
  utah_taxable: 100000
  dependents: 2
  exemption_each: 2111
  fed_deduction: 31500
steps:
  - exemption: dependents * exemption_each
  - line13: exemption + fed_deduction
  - tax: utah_taxable * 0.045
  - initial_credit: line13 * 0.06
  - phase_income: utah_taxable - 36426
  - phaseout: phase_income * 0.013
  - credit: initial_credit - phaseout
  - net_tax: tax - credit
expected:
  exemption: 4222
  line13: 35722
  tax: 4500.00
  initial_credit: 2143.32
  phaseout: 826.46
  credit: 1316.86
  net_tax: 3183.14
```

### Worked example 3: 2026 rate

For tax year 2026 the statutory rate is 4.45%. A taxpayer with $60,000 of Utah taxable income computes:

```oa-check
name: 2026 rate on 60000
inputs:
  utah_taxable: 60000
steps:
  - tax: utah_taxable * 0.0445
expected:
  tax: 2670.00
```

### Worked example 4: Qualified exempt taxpayer

A single filer with federal AGI of $15,000 and a standard deduction of $15,750 is a qualified exempt taxpayer: AGI is at or below the standard deduction, so Utah income tax is zero.

```oa-check
name: Exempt taxpayer single
inputs:
  agi: 15000
  standard_deduction: 15750
steps:
  - headroom: standard_deduction - agi
  - tax: agi * 0
expected:
  headroom: 750
  tax: 0
```

## Ask the client first

- What is federal adjusted gross income (Form 1040, line 11a)? Utah starts there, not at federal taxable income.
- How many dependents were claimed on the federal return? Each adds $2,111 to the exemption used in the taxpayer tax credit.
- Was the standard or the itemized deduction taken federally, and was state income tax itemized? That feeds TC-40 lines 12 through 15.
- Was there a 2024 Utah liability? That picks the extension prepayment percentage.
- Any my529 contributions, PPP addbacks, out-of-state municipal bond interest, or retirement income? Each touches a specific TC-40A line or credit.
- Is the client a full-year resident, part-year resident, or nonresident with Utah income? TC-40B changes the computation.

## Sources

| Source | URL | Read on |
|---|---|---|
| 2025 Utah TC-40 instructions (Form TC-40, Tax Commission) | https://tax.utah.gov/forms/current/tc-40inst.pdf | 2026-11-01 |
| Utah Code 59-10-104, tax basis, tax rate, exemption (effective January 1, 2026) | https://le.utah.gov/xcode/Title59/Chapter10/59-10-S104.html | 2026-11-01 |
| SB0060, 2026 General Session (rate change to 4.45%) | https://le.utah.gov/~2026/bills/static/SB0060.html | 2026-11-01 |
| Utah State Tax Commission, income tax rates page (rate history table) | https://incometax.utah.gov/paying/tax-rates | 2026-11-02 |

Not yet confirmed: the 2026 TC-40 instructions and the 2026 taxpayer tax credit worksheet amounts (personal exemption, 6 percent factor, and phase-out base amounts may be indexed); the Social Security benefits credit (code AH) amount and phase-out; the retirement credit income phase-out schedule.

## Talk to a verified accountant

This guide is a working paper, not a filing. A Utah-licensed CPA or enrolled agent should review part-year residency, credit eligibility, and any notice or penalty before you rely on these figures.
