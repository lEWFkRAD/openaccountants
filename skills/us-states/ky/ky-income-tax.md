---
name: ky-income-tax
description: Use this skill whenever asked about Kentucky individual income tax. Trigger on phrases like "Kentucky income tax", "KY income tax", "Form 740", "KRS 141", "Kentucky flat tax". Kentucky has a flat 3.5% rate for TY2026 (was 4% for TY2025). ALWAYS load us-tax-workflow-base first.
version: "0.4"
jurisdiction: US-KY
tax_year: 2026
last_updated: 2026-10-28
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kentucky individual income tax (Form 740), tax year 2026

> **Source-cited draft.** Built from KRS 141.020, 141.081, 141.066, 141.069, 141.305, the DOR 2025 Form 740 instruction packet, and DOR news releases, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

This skill covers the Kentucky individual income tax return for **full-year Kentucky residents** (Form 740), including sole proprietors and owners of single-member LLCs that are disregarded for federal purposes. It is written for **tax year 2026** (returns due in 2027), with a dated section for **2025 returns**, which are still being filed on extension until 15 October 2026.

| Field | Value |
| --- | --- |
| Jurisdiction | Kentucky (US-KY) |
| Tax authority | [Kentucky Department of Revenue (DOR)](https://revenue.ky.gov/) |
| Legislation | KRS Chapter 141 |
| Primary form | Form 740 (Individual Income Tax Return) + Schedules M, ITC, P |
| Filing deadline | April 15, 2027 (for tax year 2026) |

Out of scope, refer instead:

- Part-year residents and nonresidents: they file Form 740-NP, not Form 740.
- Residents of Illinois, Indiana, Michigan, Ohio, Virginia, West Virginia or Wisconsin who only had Kentucky wages withheld: Form 740-NP-R.
- Corporations, the limited liability entity tax (LLET) and pass-through entity returns (see `ky-corporate-income-tax`).
- Local occupational license taxes (see When to refuse or refer). They are separate local taxes, not part of Form 740.

## Who this applies to

Full-year Kentucky residents filing Form 740, including sole proprietors and single-member LLC owners whose Schedule C income flows through federal AGI. Self-employed persons must file a Kentucky return even below the Chart B AGI amounts if gross receipts from self-employment exceed the Chart A amount for their family size. Nonresidents and part-year residents file Form 740-NP (see `ky-cross-border`).

## Rates, bands and thresholds

| Item | 2025 returns | 2026 returns | Source |
| --- | --- | --- | --- |
| Flat rate | 4% | 3.5% | [KRS 141.020](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.020); DOR Employer Payroll Withholding page |
| Standard deduction (per return; per spouse on a combined separate return) | $3,270 | $3,360 | 2025 Form 740 instructions; [DOR 2026 standard deduction news release](https://revenue.ky.gov/News/Pages/Kentucky-DOR-Announces-2026-Standard-Deduction.aspx) |
| Pension income exclusion (per taxpayer) | $31,110 | Not yet published on a 2026 form | 2025 Form 740 instructions |
| Personal tax credits | $40 each for age 65+ and for blindness; $20 Kentucky National Guard | Same credits (DOR individual income tax page, current) | [DOR individual income tax page](https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx) |
| Family size tax credit ceiling on MGI (family of four or more, 2025 table) | $42,760 | 2026 table not yet published | 2025 Form 740 instructions |
| Filing threshold (Chart A, MGI, 2025) | $15,650 (one), $21,150 (two), $26,650 (three), $32,150 (four or more) | 2026 amounts not yet published | 2025 Form 740 instructions |

KRS 141.020(2)(d)–(f) states the rate history: "For taxable years beginning on or after January 1, 2023, but prior to January 1, 2024, the tax shall be four and one-half percent (4.5%) of net income. For taxable years beginning on or after January 1, 2024, but before January 1, 2026, the tax shall be four percent (4%) of net income. For taxable years beginning on or after January 1, 2026, the tax shall be three and one-half percent (3.5%) of net income." Future reductions require an act of the General Assembly; the department maintains the paragraph (f) rate unless the General Assembly acts.

## The taxable base

1. **Starting point.** Form 740, line 5 starts from **federal adjusted gross income** (Form 1040 line 11), not federal taxable income.
2. **Schedule M modifications.**
   - Additions: interest on securities of other states and their political subdivisions (Kentucky municipal bond interest is exempt); resident adjustments from Kentucky Schedule K-1; federal depreciation differences (see below).
   - Subtractions: taxable state income tax refund included in federal income (line 7); U.S. government bond and securities interest (line 8 -- Fannie Mae, Ginnie Mae and Freddie Mac interest is NOT exempt, per the instructions); pension exclusion (line 9, see below); Social Security and railroad retirement benefits (lines 10–11); military pay of active duty Armed Forces members (line 13, exempt under KRS 141.019(l), which "Exclude[s] all military pay received by members of the Armed Forces while on active duty").
3. **Pension income exclusion (Schedule M line 9).** For 2025: "The 2025 exclusion amount is 100 percent of taxable retirement benefits or $31,110, whichever is less." It covers pensions, annuities, IRA accounts, 401(k) plans and similar written-plan retirement income. It is **per taxpayer**. If total retirement income exceeds $31,110 and any of it is from the federal government, the Commonwealth of Kentucky or a Kentucky local government, or is supplemental U.S. Railroad Retirement Board benefits, Schedule P must be completed.
4. **Standard deduction.** KRS 141.081 allows an optional standard deduction, inflation-adjusted under KRS 141.081(2). The 2025 Form 740 instructions state: "For 2025, the standard deduction is $3,270." The DOR 2026 news release states: "After adjusting for inflation, the standard deduction for 2026 is $3,360, an increase of $90." On a joint return only one standard deduction is allowed; married filing separately on a combined return (Filing Status 2) enters it in both columns. A taxpayer may instead itemize Kentucky deductions, which exclude medical expenses, state and local income taxes, real estate and personal property taxes, and casualty losses.
5. **Depreciation and Section 179 (permanent decoupling).** Per the 2025 Form 740 instructions: "taxpayers who placed property into service after September 10, 2001, are required to compute Kentucky depreciation under IRC Section 168 according to the provisions in effect on December 31, 2001," and property placed in service on or after 1 January 2020 computes the IRC Section 179 expense deduction under the provisions in effect on 1 January 2020. Recompute on a Kentucky Form 4562, adding back federal depreciation on Schedule M line 3 and subtracting Kentucky depreciation on line 12.
6. **Federal conformity.** Kentucky uses the Internal Revenue Code as of a fixed date. The 2025 instructions state that KRS 141.010(21) was updated to 31 December 2024 and that recent federal changes "do not apply to Kentucky returns," citing qualified tips, overtime income and car loan interest. The federal QBI deduction is taken after federal AGI, so it never reaches Form 740. Self-employed health insurance, the deductible half of self-employment tax, and SEP/SIMPLE/solo 401(k) deductions reduce federal AGI and flow through. A home office deduction sits on Schedule C and is already inside federal AGI.
7. **Credits.** Nonrefundable credits: personal tax credits (Schedule ITC), family size tax credit, education tuition tax credit (Form 8863-K), child and dependent care credit, business incentive credits and the credit for tax paid to other states (KRS 141.070: the lesser of the Kentucky tax on the double-taxed income and the other state's tax).
8. **Payments and balance.** Kentucky withholding from Schedule KW-2, estimated and extension payments, refundable credits, then penalties and interest (line 34) and the amount owed or refunded.

### Family size tax credit (KRS 141.066)

A nonrefundable percentage of tax for low incomes. The 2025 instructions state the credit "provides benefits to individuals and families at incomes up to 133 percent of the threshold amount based on the federal poverty level. The 2025 threshold amount is $15,650 for a family size of one, $21,150 for a family of two, $26,650 for a family of three, and $32,150 for a family of four or more." Modified gross income is the greater of federal AGI (plus non-Kentucky municipal bond interest and lump-sum distributions) or Kentucky AGI (plus those distributions). The percentage is read from the Family Size Tax Table on Schedule ITC; the instructions' example confirms: "This taxpayer has a family size of two and would be entitled to a family size tax credit of 80% (.80)" (MGI $22,650).

### Personal tax credits

The DOR individual income tax page states: "A $40 tax credit is allowed for each individual reported on the return who is age 65 or over. Also, a $40 tax credit is allowed if an individual is legally blind. Persons who are both age 65 or older and legally blind are eligible for both tax credits for a total of $80 per person. Members of the Kentucky National Guard may claim a tax credit of $20; military reserve members are not eligible." These are nonrefundable.

### Education tuition tax credit (KRS 141.069)

KRS 141.069(2) allows a nonrefundable credit of "twenty-five percent (25%)" of the federal credit for undergraduate tuition at an eligible Kentucky institution. The 2025 instructions cap the American Opportunity portion at "$625 for each qualifying student" and the Lifetime Learning portion at "a maximum allowed of $500 per return." Nonrefundable, with a carryforward; Form 8863-K required. Graduate tuition and out-of-state institutions do not qualify.

### Child and dependent care credit (line 24)

For 2025 returns: the credit is 20% of the federal credit from Form 2441, line 11 -- the instructions state "Multiply this amount by 20 percent (.20), and enter result on line 24." It is also available to a person with no federal filing requirement who would have qualified (write "did not meet federal filing requirements" on Form 2441). For 2026, the federal credit base may have changed after Kentucky's conformity date; check the 2026 Form 740 line 24 instructions before applying 20% (see Not yet confirmed).

## Deadlines and filing

- **Due dates.** The 2025 instructions state the calendar-year 2025 return "must be postmarked or submitted electronically no later than April 15, 2026." The same rule puts the 2026 return on 15 April 2027; confirm on the 2026 packet.
- **Extensions.** Kentucky extensions "are limited to six months" (an extended 2025 return is due 15 October 2026). A federal automatic extension is honoured if a copy is enclosed; alternatively Form 740EXT may be filed, which "must state a reasonable cause for the inability to file. Inability to pay is not an acceptable reason." An extension is not an extension to pay; interest runs from the original due date.
- **Estimated tax (KRS 141.305).** KRS 141.305(1) applies where "Gross income from sources other than wages upon which Kentucky income tax will be withheld can reasonably be expected to exceed five thousand dollars ($5,000) for the taxable year," and KRS 141.305(2) states "No estimated tax shall be required if the estimated tax liability can reasonably be expected to be five hundred dollars ($500) or less." Otherwise pay the smaller of 90% of the current-year tax or 100% of the prior-year tax from a 12-month return; taxpayers whose prior-year Kentucky AGI exceeded $150,000 ($75,000 if married filing separately) use 110% of the prior year instead (per the Form 2210-K instructions in the 2025 packet, which test the prior year's income). Farmers and fishermen: the instructions state "substitute 66 2/3% for 90% in (1) above," and the 110% rule does not apply. Installments for 2026 are due 15 April, 15 June and 15 September 2026 and 15 January 2027. The annualized income method (Form 2210-K) is available.
- **Amended returns and federal audits.** Amended returns must be filed within four years ("amended returns must be filed within the statute of limitations period; four years from the due date"). A taxpayer must report a final federal audit determination "within 180 days of its conclusion."

## Penalties and interest

| Item | Rule | Source |
| --- | --- | --- |
| Underpaid estimated tax | May apply if the amount owed is more than $500; computed on Form 2210-K, line 34(a) | 2025 Form 740 instructions |
| Late payment | 2% of the tax due per 30 days or fraction thereof, capped at 20%, minimum $10; the instructions add "if the amount timely paid is 75 percent of the tax determined due," the late-payment penalty is not assessed | 2025 Form 740 instructions; DOR Penalties, Interest and Fees page |
| Late filing | 2% of the tax due per 30 days or fraction thereof, capped at 20%, minimum $10 ($100 after a jeopardy assessment) | DOR Penalties, Interest and Fees page |
| Interest on unpaid tax | 10% for calendar year 2025 and 9% for calendar year 2026 under KRS 131.183(2)(a)2 | DOR news releases for 01-01-25 and 01-01-26; DOR Penalties, Interest and Fees page |
| Waiver | Penalties, but not interest, may be reduced or waived for reasonable cause | DOR Penalties, Interest and Fees page |

The DOR 2025 interest notice states that taxes not paid "will accrue interest at the rate of 10 % pursuant to KRS 131.183(2)(a)2"; the 2026 notice states the rate "will accrue interest at the rate of 9 % pursuant to KRS 131.183(2)(a)2."

## Cross-border points

- Nonresidents and part-year residents file Form 740-NP (see `ky-cross-border`).
- Kentucky residents pay tax on their entire net income regardless of where earned and may claim a credit for income tax paid to another state under KRS 141.070 (the lesser of the Kentucky tax on the double-taxed income and the other state's tax).
- Interest from another state's municipal bonds is added back; U.S. government obligations are subtracted.
- Local occupational license taxes are not Kentucky income tax and must not be included on Form 740 line 31(a).

## Worked examples

### Example 1: 2026, single, self-employed (hypothetical facts)

Federal AGI $60,000, all Schedule C, no Kentucky modifications, standard deduction. Taxable income $60,000 − $3,360 = $56,640. Tax $56,640 × 3.5% = $1,982.40.

```oa-check
name: KY 2026 single, AGI 60000, std deduction 3360, rate 3.5 percent
inputs:
  agi: 60000
  std: 3360
  rate: 0.035
steps:
  - ti: agi - std
  - tax: ti * rate
expected:
  ti: 56640.00
  tax: 1982.40
```

### Example 2: the same hypothetical facts on a 2025 return

$60,000 − $3,270 = $56,730. Tax $56,730 × 4% = $2,269.20.

```oa-check
name: KY 2025 single, AGI 60000, std deduction 3270, rate 4 percent
inputs:
  agi: 60000
  std: 3270
  rate: 0.04
steps:
  - ti: agi - std
  - tax: ti * rate
expected:
  ti: 56730.00
  tax: 2269.20
```

### Example 3: 2025, single retiree aged 67 (hypothetical facts)

Private pension $40,000 and taxable Social Security $17,000; federal AGI $57,000. Subtract the pension exclusion $31,110 and Social Security $17,000: Kentucky AGI $8,890. Less $3,270 = $5,620 taxable. Tax $5,620 × 4% = $224.80, less the $40 age credit = $184.80. MGI is the greater of federal AGI ($57,000) and Kentucky AGI, so no family size credit.

```oa-check
name: KY 2025 retiree, pension exclusion 31110
inputs:
  agi: 57000
  pension_excl: 31110
  socsec: 17000
  std: 3270
  rate: 0.04
  age_credit: 40
steps:
  - kyagi: agi - pension_excl - socsec
  - ti: kyagi - std
  - tax_gross: ti * rate
  - tax: tax_gross - age_credit
expected:
  kyagi: 8890.00
  ti: 5620.00
  tax: 184.80
```

### Example 4: 2025, family size credit (hypothetical facts)

Married couple, family size two, filing jointly; MGI and Kentucky AGI $22,650. Taxable $22,650 − $3,270 = $19,380. Tax $19,380 × 4% = $775.20. Per the instructions' example, a family of two with MGI $22,650 is entitled to an 80% credit: $775.20 × 80% = $620.16. Tax after the credit is $155.04.

```oa-check
name: KY 2025 family size credit 80 percent
inputs:
  mgi: 22650
  std: 3270
  rate: 0.04
  credit_pct: 0.80
steps:
  - ti: mgi - std
  - tax_gross: ti * rate
  - credit: tax_gross * credit_pct
  - tax: tax_gross - credit
expected:
  ti: 19380.00
  tax: 155.04
```

### Example 5: 2025 education credit (hypothetical facts)

Federal American Opportunity credit of $2,500 for an undergraduate at a Kentucky university. Kentucky credit 25% = $625, which equals the per-student cap. Nonrefundable: limited to tax on line 22, excess carries forward.

```oa-check
name: KY education credit 25 percent capped at 625
inputs:
  fed_aoc: 2500
  pct: 0.25
  cap: 625
steps:
  - tentative: fed_aoc * pct
  - credit: min(tentative, cap)
expected:
  tentative: 625.00
  credit: 625.00
```

### Example 6: 2026 estimated tax (hypothetical facts)

Example 1's taxpayer has no withholding and owed $2,269.20 for 2025 (a full 12-month return). The 2026 estimate is $1,982.40, which exceeds $500, so payments are required. The required annual payment is the smaller of 90% × $1,982.40 = $1,784.16 and 100% of the 2025 tax ($2,269.20): $1,784.16, or $446.04 per quarterly installment.

```oa-check
name: KY 2026 required annual installment
inputs:
  est_2026: 1982.40
  tax_2025: 2269.20
  pct: 0.90
steps:
  - req: min(est_2026 * pct, tax_2025)
  - per_q: req / 4
expected:
  req: 1784.16
  per_q: 446.04
```

## Ask the client first

- Which tax year is this: 2025 or 2026? The rate and standard deduction differ.
- Was the person a Kentucky resident for the **whole** year? If not, stop: Form 740-NP.
- Filing status on the federal return, and, if married, did both spouses have income? (Kentucky lets spouses file separately on one combined return, which "usually results in a lower tax than Filing Status 3" per the instructions.)
- Federal AGI (Form 1040 line 11), and whether any federal return was filed at all.
- Age 65 or over, legally blind, or a Kentucky National Guard member on 31 December?
- Family size and modified gross income (for the filing test and the family size tax credit).
- Pension, IRA, 401(k) or annuity income? Any of it from the federal government, the Commonwealth of Kentucky or a Kentucky local government?
- Social Security or railroad retirement benefits in federal AGI?
- Interest from US government obligations, or from other states' municipal bonds?
- Bonus depreciation or Section 179 amounts in the federal return?

## When to refuse or refer

- Part-year or nonresident: Form 740-NP.
- Schedule P cases (government pension with service before 1998), lump-sum 10-year averaging (Form 4972-K) or farm income averaging.
- Business incentive credits, pass-through entity tax credits, the LLET or Kentucky Schedule K-1 adjustments.
- Schedule C or E amounts shaped by post-2024 federal changes where the year's Schedule M instructions give no line to reverse them.
- Kentucky net operating loss, excess business loss (Form 461-K) or passive loss (Form 8582-K) recomputations.
- **Local occupational license taxes.** Many Kentucky cities and counties levy their own occupational license tax. They are administered locally, not by DOR; the instructions state "Local government occupational, license or income tax must not be included on line 31(a)." Send the person to the city or county tax office where the work is done. Do not quote local rates from memory.
- Any 2027 rate question until DOR publishes 2027 forms.

## Sources

| Source | URL | Read on |
|---|---|---|
| KRS 141.020 (individual income tax rates; 4.5% 2023, 4% 2024-2025, 3.5% 2026; nonresident source rules) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.020 | 2026-10-28 |
| KRS 141.081 (optional standard deduction; inflation adjustment) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.081 | 2026-10-28 |
| KRS 141.066 (family size tax credit) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.066 | 2026-10-28 |
| KRS 141.069 (education tuition credit, 25% of federal) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.069 | 2026-10-28 |
| KRS 141.305 (estimated tax; $5,000 income and $500 liability thresholds) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.305 | 2026-10-28 |
| KRS 141.070 (credit for tax paid to other states) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.070 | 2026-10-28 |
| KRS 141.019 (exclusions incl. military pay) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.019 | 2026-10-28 |
| DOR 2025 Form 740 instruction packet (filing thresholds, $3,270, $31,110, $42,760, credits, penalties, extensions, 66 2/3%, $150,000/$75,000, depreciation) | https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf | 2026-10-28 |
| DOR individual income tax page (personal credits $40/$80/$20; child and dependent care credit 20%) | https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx | 2026-10-28 |
| DOR news release: 2026 standard deduction $3,360 | https://revenue.ky.gov/News/Pages/Kentucky-DOR-Announces-2026-Standard-Deduction.aspx | 2026-10-28 |
| DOR news release: 2027 standard deduction $3,470 | https://revenue.ky.gov/News/Pages/Kentucky-DOR-Announces-2027-Standard-Deduction.aspx | 2026-10-28 |
| DOR news release: interest rate update for 01-01-25 (10% on unpaid tax) | https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-25.aspx | 2026-10-28 |
| DOR news release: interest rate update for 01-01-26 (9% on unpaid tax) | https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-26.aspx | 2026-10-28 |
| DOR Penalties, Interest and Fees page (late payment/filing 2% per 30 days, 20% cap, $10 minimum; interest rates table) | https://revenue.ky.gov/Collections/Pages/Penalties-Interest-and-Fees.aspx | 2026-10-28 |
| DOR Employer Payroll Withholding page ("The Kentucky Withholding Tax rate will be 3.5% for tax year 2026") | https://revenue.ky.gov/Business/Pages/Employer-Payroll-Withholding.aspx | 2026-10-28 |

Not yet confirmed: the 2026 pension income exclusion amount (DOR pages still show the 2025 $31,110 figure; the 2026 Form 740 packet was not yet published at read time); the 2026 family size tax credit table and thresholds (the 2025 table is archived; the 2026 table appears on Schedule ITC, not yet published); whether the 2026 child and dependent care credit base is the pre-2026 or post-P.L. 119-21 federal credit (check the 2026 Form 740 line 24 instructions before applying 20%); the 2027 individual income tax rate (reductions require General Assembly action; no 2027 act confirmed -- the 2027 standard deduction of $3,470 per the DOR news release is for planning only).

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
