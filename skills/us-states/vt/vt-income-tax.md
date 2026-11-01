---
name: vt-income-tax
description: "Vermont individual income tax for tax year 2025 (Form IN-111, filed in 2026) for full-year residents, including sole proprietors: starting from federal adjusted gross income, the Vermont standard deduction and $5,300 personal exemption, the 2025 rate schedules (3.35%, 6.60%, 7.60%, 8.75%), the 3% minimum tax when federal AGI exceeds $150,000, the Vermont earned income tax credit and child and dependent care credit, the capital gains exclusion, the April 15 due date, extensions under 32 V.S.A. 5868, and quarterly estimated tax under 32 V.S.A. 5852. Trigger on 'Vermont income tax', 'VT income tax', 'Form IN-111', 'Vermont tax brackets', 'Vermont 8.75%', '32 V.S.A. Chapter 151'."
version: "0.3"
jurisdiction: US-VT
tax_year: 2025
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Vermont individual income tax, 2025

> **Source-cited draft.** Built from the Vermont Department of Taxes 2025 Tax Rate Schedules, the 2025 Form IN-111, Schedule IN-112 and Form IN-153 instructions, the 2026 Form IN-114 instructions, the Department's estimated income tax page, and 32 V.S.A. 5828b, 5828c, 5852, 5857, 5861 and 5868, read on 2026-11-01. No accountant has reviewed it. Do not file from it without review by a qualified professional.

## Who this applies to

- **Vermont filers.** An individual subject to Vermont tax must file a Vermont personal income tax return if required to file a federal return and they earned or received more than $100 of Vermont income, or more than $1,000 of gross income from the sources listed in 32 V.S.A. 5823(b)(1) to (6), or have a Vermont tax liability (32 V.S.A. 5861(a)).
- **Joint filers.** Spouses who file a joint federal return must file a joint Vermont return unless the Commissioner allows otherwise (32 V.S.A. 5861(c)).
- **Self-employed people and sole proprietors.** Business income reaches Vermont through federal adjusted gross income (AGI). The Department says self-employed people "must pay your own estimated income taxes to the Department, usually quarterly" (estimated income tax page).
- This guide covers full-year residents. Part-year residents and nonresidents apply an income adjustment percentage from Schedule IN-113 (IN-111 instructions, Line 15); see Ask the client first.

## Rates, bands and thresholds

**2025 Vermont tax rate schedules** (Department of Taxes, 2025 Vermont Tax Rate Schedules). Taxable income under $75,000 uses the tax tables; the schedules below give the same marginal bands.

| Filing status | 3.35% | 6.60% | 7.60% | 8.75% |
|---|---|---|---|---|
| Single (Schedule X) | $0 to $49,400 | over $49,400 to $119,700 | over $119,700 to $249,700 | over $249,700 |
| Married filing jointly, qualifying widow(er), civil union filing jointly (Schedule Y-1) | $0 to $82,500 | over $82,500 to $199,450 | over $199,450 to $304,000 | over $304,000 |
| Married or civil union filing separately (Schedule Y-2) | $0 to $41,250 | over $41,250 to $99,725 | over $99,725 to $152,000 | over $152,000 |
| Head of household (Schedule Z) | $0 to $66,200 | over $66,200 to $171,000 | over $171,000 to $276,850 | over $276,850 |

Schedule base-tax amounts for incomes of $75,000 or more: Single $3,345.00 at $75,000, $6,295.00 at $119,700, $16,175.00 at $249,700; MFJ $2,513.00 at $75,000, $2,764.00 at $82,500, $10,482.00 at $199,450, $18,428.00 at $304,000.

| Item | 2025 amount | Source |
|---|---|---|
| Standard deduction | Single $7,650; MFJ or qualifying widow(er) $15,300; MFS $7,650; Head of household $11,450 | IN-111 instructions, Line 4 |
| Additional standard deduction (age 65 or blind) | $1,250 per box checked on federal Form 1040 | IN-111 instructions, Line 4 |
| Personal exemption | $5,300 per exemption | IN-111 instructions, Line 5e |
| Minimum tax | if federal AGI exceeds $150,000, tax is the greater of 3% of federal AGI less U.S. obligation interest, or the rate-schedule tax | IN-111 instructions, Line 8 |
| Vermont earned income tax credit | 38% of the federal EITC with one or more qualifying children; 100% of the federal EITC with no qualifying children; refundable | 32 V.S.A. 5828b(a), (b); IN-112 instructions, Line 7 |
| Child and dependent care credit | 72% of the federal child and dependent care credit, refundable, no income limit in the statute | 32 V.S.A. 5828c |
| Capital gains exclusion | flat $5,000 (or actual net adjusted gain if less), or 40% of adjusted net capital gain from qualifying assets held more than three years (gain up to $350,000); either way capped at the lesser of 40% of federal taxable income or $350,000 | IN-153 instructions |
| Charitable contribution credit | 5% of the first $20,000 of charitable contributions, nonrefundable, available whether or not the taxpayer itemizes federally | IN-111 instructions, Line 11 |
| Estimated tax penalty floor | no underpayment penalty or interest if tax due less withholding is under $500 | IN-111 instructions, Line 31; IN-114 instructions |

## The taxable base

Form IN-111 builds Vermont taxable income from federal AGI, not federal taxable income (IN-111 instructions):

1. Line 1: federal adjusted gross income from federal Form 1040.
2. Line 2: net modifications from Schedule IN-112, Part I.
3. Line 3: federal AGI with modifications (Line 1 + Line 2).
4. Line 4: Vermont standard deduction (table above), in place of the federal standard or itemized deduction.
5. Line 5e: personal exemptions x $5,300.
6. Line 7: Vermont taxable income = Line 3 minus Lines 4 and 5e (not below zero).
7. Line 8: tax from the table or rate schedule, subject to the 3% minimum tax when federal AGI exceeds $150,000.

Because the start is federal AGI, the self-employment tax deduction, self-employed health insurance and SEP, SIMPLE or solo 401(k) contributions (all above-the-line federal deductions) carry into Vermont. Deductions taken after AGI federally (itemized deductions, the qualified business income deduction) do not carry into Vermont taxable income. Charitable giving instead earns a nonrefundable credit equal to 5% of the first $20,000 of contributions, whether or not the taxpayer itemizes federally (IN-111 instructions, Line 11).

Schedule IN-112 modifications relevant to sole proprietors (IN-112 instructions):

- **Bonus depreciation:** "Vermont does not recognize the bonus depreciation allowed under federal law." Add back federal bonus depreciation for assets placed in service in 2025 (Line 4); adjust for prior-year bonus property (Line 9).
- **U.S. obligations:** interest from U.S. government obligations is subtracted (Line 7).
- **Capital gains exclusion:** computed on Form IN-153. The percentage exclusion does not apply to a home, depreciable personal property (other than farm or standing timber), or publicly traded stocks, bonds and other instruments, even if held more than three years. Qualified dividends do not qualify. No exclusion is available in a year with a net capital loss (IN-153 instructions; 32 V.S.A. 5811(21)(B)).

## Deadlines and filing

- **Return due date:** the date the federal return is originally due (32 V.S.A. 5861(b)). "The 2025 Vermont Income Tax Return must be filed by April 15, 2026" (IN-111 instructions).
- **Extension:** the Commissioner extends the Vermont filing date to the federal extended date when the taxpayer has a federal automatic or good-cause extension (32 V.S.A. 5868). No separate Vermont extension is needed with a federal extension; a taxpayer making an extension payment files Form IN-151 by April 15, 2026. Extended returns are due Oct. 15, 2026. An extension does not extend the time to pay (32 V.S.A. 5868; IN-111 instructions).
- **Estimated tax:** individuals subject to Vermont tax (other than those receiving at least two-thirds of their income from farming or fishing) must pay estimated tax in installments of 25% of the required annual payment, due April 15, June 15 and September 15 of the tax year and January 15 of the next year (32 V.S.A. 5852(a)). For 2026 estimates: April 15, 2026; June 15, 2026; September 15, 2026; January 15, 2027, with Form IN-114 (IN-114 instructions). Annualized installments are allowed for taxpayers who annualize federally (32 V.S.A. 5852(b)).
- **Safe harbors:** total estimated payments equal to 100% of last year's tax liability or 90% of this year's (IN-111 instructions, Line 31; estimated income tax page).
- **The $500 figure is a penalty floor, not a filing trigger:** if tax due less withholding is under $500 there is no underpayment penalty or interest (IN-111 instructions, Line 31). 32 V.S.A. 5857 refers to "the $500.00 minimum tax requirement" when setting later filing dates for a declaration of estimated tax.

## Penalties and interest

- **Late filing:** a return may be filed up to 60 days after April 15, 2026 without an extension; filing on the 61st day or later brings a $50 late file penalty. With an extension, the $50 penalty applies if the return is not filed by Oct. 15, 2026. The late filing penalty applies even if a refund is due or no tax is due (IN-111 instructions).
- **Late payment:** late payment penalty and interest accrue on tax unpaid after April 15, from April 16 to the date the Department receives payment (IN-111 instructions).
- **Underpayment of estimated tax:** interest and penalty computed on Worksheet IN-152 or IN-152A and reported on IN-111 Line 31 (IN-111 instructions).

## Cross-border points

- **Credit for tax paid to another state or Canadian province:** claimed on Schedule IN-117 and entered on IN-111 Line 17 (IN-111 instructions).
- **Part-year residents and nonresidents:** the EITC and the child and dependent care credit are prorated by the share of income earned or received while a Vermont resident (32 V.S.A. 5828b(a), 5828c).
- **Nonresident business owners:** estimated taxes paid on their behalf by a partnership, LLC or S corporation go on IN-111 Line 26e from Schedule K-1VT (IN-111 instructions).

## Worked examples

### Worked example 1: single sole proprietor

A single full-year resident sole proprietor has federal AGI of $90,000 after the self-employment tax deduction, no IN-112 modifications, and one personal exemption. Federal AGI is under $150,000, so the minimum tax does not apply. Taxable income is $90,000 - $7,650 - $5,300 = $77,050, which uses the Single schedule row over $75,000: $3,345.00 plus 6.60% of the excess over $75,000.

```oa-check
name: VT 2025 single sole proprietor
inputs:
  federal_agi: 90000
  std_deduction: 7650
  exemption: 5300
  base_tax: 3345
  row_floor: 75000
  rate: 0.066
steps:
  - taxable: federal_agi - std_deduction - exemption
  - tax: base_tax + (taxable - row_floor) * rate
expected:
  taxable: 77050.00
  tax: 3480.30
```

Vermont tax is $3,480.30 (IN-111 Line 8, rounded to whole dollars on the return).

### Worked example 2: married couple above the $150,000 minimum-tax line

A married couple filing jointly has federal AGI of $200,000, no modifications, no U.S. obligation interest, and two personal exemptions. Taxable income is $200,000 - $15,300 - $10,600 = $174,100, in the MFJ row over $82,500: $2,764.00 plus 6.60% of the excess. Because federal AGI exceeds $150,000, Line 8 is the greater of that amount and 3% of federal AGI.

```oa-check
name: VT 2025 MFJ with 3 percent minimum tax test
inputs:
  federal_agi: 200000
  std_deduction: 15300
  exemptions: 10600
  base_tax: 2764
  row_floor: 82500
  rate: 0.066
  min_rate: 0.03
steps:
  - taxable: federal_agi - std_deduction - exemptions
  - schedule_tax: base_tax + (taxable - row_floor) * rate
  - minimum_tax: federal_agi * min_rate
  - line8: max(schedule_tax, minimum_tax)
expected:
  taxable: 174100.00
  schedule_tax: 8809.60
  minimum_tax: 6000.00
  line8: 8809.60
```

The rate-schedule tax of $8,809.60 exceeds the $6,000 minimum, so Line 8 is $8,809.60.

## Ask the client first

1. **Were you a Vermont resident all year?** Part-year residents and nonresidents apportion income and prorate credits.
2. **Is your federal AGI over $150,000?** The 3% minimum tax test applies.
3. **Did you claim federal bonus depreciation?** It must be added back on Schedule IN-112.
4. **Did you sell a business, farm, timber or other asset held more than three years at a gain?** Check Form IN-153 for the capital gains exclusion.
5. **Do you claim the federal EITC, and with or without qualifying children?** The Vermont credit is 38% or 100%.
6. **Do at least two-thirds of your gross income come from farming or fishing?** Quarterly estimates are not required.
7. **Did you pay income tax to another state or Canadian province?** Schedule IN-117.

## Sources

| Source | URL | Read on |
|---|---|---|
| Vermont Department of Taxes, 2025 Vermont Tax Rate Schedules | https://tax.vermont.gov/sites/tax/files/documents/TaxRateSched-2025.pdf | 2026-11-01 |
| Vermont Department of Taxes, 2025 Form IN-111 Instructions | https://tax.vermont.gov/sites/tax/files/documents/IN-111-Instr-2025.pdf | 2026-11-01 |
| Vermont Department of Taxes, 2025 Schedule IN-112 Instructions | https://tax.vermont.gov/sites/tax/files/documents/IN-112-Instr-2025.pdf | 2026-11-01 |
| Vermont Department of Taxes, 2025 Form IN-153 Instructions | https://tax.vermont.gov/sites/tax/files/documents/IN-153-Instr-2025.pdf | 2026-11-01 |
| Vermont Department of Taxes, 2026 Form IN-114 Instructions | https://tax.vermont.gov/sites/tax/files/documents/IN-114-Instr-2026.pdf | 2026-11-01 |
| Vermont Department of Taxes, Estimated Income Tax | https://tax.vermont.gov/individuals/estimated-income-tax | 2026-11-01 |
| 32 V.S.A. 5828b, earned income tax credit | https://legislature.vermont.gov/statutes/section/32/151/05828b | 2026-11-01 |
| 32 V.S.A. 5828c, child and dependent care credit | https://legislature.vermont.gov/statutes/section/32/151/05828c | 2026-11-01 |
| 32 V.S.A. 5852, payment of estimated income tax | https://legislature.vermont.gov/statutes/section/32/151/05852 | 2026-11-01 |
| 32 V.S.A. 5857, filing dates | https://legislature.vermont.gov/statutes/section/32/151/05857 | 2026-11-01 |
| 32 V.S.A. 5861, returns by individuals, trusts, and estates | https://legislature.vermont.gov/statutes/section/32/151/05861 | 2026-11-01 |
| 32 V.S.A. 5868, extension of time for filing of returns | https://legislature.vermont.gov/statutes/section/32/151/05868 | 2026-11-01 |

Not yet confirmed: the late payment penalty and interest rates (the IN-111 instructions say they accrue but give no percentages); the 2026 indexed rate schedules, standard deduction and exemption (the 2026 schedule was not archived in readable form); the residency definition (domicile and any day-count test); how the credit for tax paid to another state is computed on Schedule IN-117.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put their name behind the tax answers AI gives people.

> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
