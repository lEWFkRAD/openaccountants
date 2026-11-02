---
name: ca-540-individual-return
description: Tier 2 content skill for preparing California Form 540 (Resident Income Tax Return) for US sole proprietors and single-member LLCs who are California residents. Covers tax year 2025 California personal income tax including the Schedule CA (540) decoupling adjustments from federal AGI, California's non-conformity with OBBBA bonus depreciation and section 179 expensing, the nine-bracket rate structure (1% through 12.3% plus the 1% Behavioral Health Services Tax surcharge above $1,000,000), standard and itemized deductions, California tax credits (renter's credit, CalEITC, young child tax credit), SDI treatment, and California's own AMT. Defers estimated tax to ca-estimated-tax-540es, SMLLC franchise tax to ca-smllc-form-568, and health coverage mandate to ca-form-3853-coverage. MUST be loaded alongside us-tax-workflow-base v0.1 or later and us-federal-return-assembly. California full-year residents only.
version: 0.3
jurisdiction: US-CA
tier: 2
last_updated: 2026-11-02
---

# CA 540 Individual Return Skill v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

### What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It provides the California personal income tax computation rules for a full-year California resident sole proprietor or single-member LLC owner for tax year 2025. It does not provide workflow architecture -- that comes from the base. It does not compute California estimated tax (ca-estimated-tax-540es), SMLLC franchise tax (ca-smllc-form-568), or the individual mandate penalty (ca-form-3853-coverage) -- those are separate content skills.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (November 2026). California conforms to the Internal Revenue Code as of January 1, 2025 for taxable years beginning on or after January 1, 2025 (R&TC section 17024.5(a)(1)(Q), as amended by SB 1435, Stats. 2026, Ch. 236). California has NOT conformed to the One Big Beautiful Bill Act (OBBBA, P.L. 119-21, approved July 4, 2025) for the key provisions listed in "The taxable base" below; FTB Publication 1001 (2025) states the R&TC does not conform to those changes. For tax years before 2025, the skill must not be used without explicit verification. For tax years after 2025, bracket thresholds and standard deduction amounts will need updating.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer (Enrolled Agent, CPA, or attorney under Circular 230) reviews and signs the return.

---

## Who this applies to

This skill covers California Form 540 (Resident Income Tax Return) for tax year 2025 for taxpayers who are:

- Full-year California residents, AND
- Sole proprietors filing federal Schedule C, OR single-member LLCs disregarded for federal tax

For the following kinds of work:

- Computing California adjusted gross income (CA AGI) from federal AGI using Schedule CA (540)
- Identifying California additions (add-backs) and subtractions from federal AGI
- Applying the nine-bracket California tax rate schedule
- Applying the 1% Behavioral Health Services Tax (formerly Mental Health Services Tax) on taxable income above $1,000,000
- Determining standard deduction vs. itemized deductions (California-specific rules)
- Computing California tax credits (renter's credit, CalEITC, young child tax credit, and others)
- Computing California Alternative Minimum Tax (AMT) where applicable
- Producing the Form 540 worksheet for the reviewer

This skill does NOT cover:

- California estimated tax payments -- handled by `ca-estimated-tax-540es`
- Form 568 SMLLC return -- handled by `ca-smllc-form-568`
- Health coverage individual mandate -- handled by `ca-form-3853-coverage`
- Part-year residents or nonresidents (Form 540NR)
- Multi-state apportionment
- Community property adjustments for RDP/same-sex couples (flag for reviewer)
- Any federal computation -- those are upstream

---

## Rates, bands and thresholds

**Tax year covered:** 2025 (California returns due April 15, 2026, or October 15, 2026 with extension).

**Currency date:** November 2026.

**Legislation and sources reflected:**
- California Revenue and Taxation Code (R&TC) as in force for tax year 2025
- R&TC section 17024.5(a)(1)(Q): for taxable years beginning on or after January 1, 2025, California conforms to the IRC as of **January 1, 2025** (amended by Stats. 2026, Ch. 236 (SB 1435), effective September 14, 2026)
- FTB 2025 Personal Income Tax Booklet (Form 540 instructions, tax rate schedules X and Y)
- FTB Schedule CA (540) Instructions (2025), FTB Schedule P (540) and instructions (2025)
- FTB Publication 1001 (2025) -- Adjustments to Income (federal acts California does not conform to)
- FTB CalEITC and Young Child Tax Credit pages (2025 figures)
- EDD Rates and Withholding (SDI 2025)
- P.L. 119-21 (OBBBA) as enacted

**Conformity note:** The FTB 2025 booklet states: "In general, for taxable years beginning on or after January 1, 2025, California law conforms to the Internal Revenue Code (IRC) as of January 1, 2025. However, there are continuing differences between California and federal law."

### Tax rate schedule -- Single, Head of Household, Married Filing Separately (2025, Schedule X)

| Bracket | Taxable income range | Rate |
|---|---|---|
| 1 | $0 -- $11,079 | 1% |
| 2 | $11,079 -- $26,264 | 2% |
| 3 | $26,264 -- $41,452 | 4% |
| 4 | $41,452 -- $57,542 | 6% |
| 5 | $57,542 -- $72,724 | 8% |
| 6 | $72,724 -- $371,479 | 9.3% |
| 7 | $371,479 -- $445,771 | 10.3% |
| 8 | $445,771 -- $742,953 | 11.3% |
| 9 | $742,953 and over | 12.3% |

**Note:** Married Filing Jointly / Qualifying Surviving Spouse brackets (Schedule Y) are double the single brackets (first bracket $0 -- $22,158 at 1%, second bracket starts at $22,158). The $1,000,000 Behavioral Health Services Tax threshold is statutory at one million dollars regardless of filing status (R&TC section 17043(a)) and is NOT doubled for MFJ.

### Behavioral Health Services Tax (renamed from Mental Health Services Tax for taxable years beginning on or after January 1, 2025)

- Additional tax of 1 percent on the portion of taxable income in excess of $1,000,000 (R&TC section 17043(a)).
- The $1,000,000 threshold is not indexed and is not doubled for MFJ; it applies to the return's joint taxable income.
- Reported on Form 540, line 62.

### Standard deduction (2025)

| Filing status | Standard deduction |
|---|---|
| Single / MFS | $5,706 |
| MFJ / QSS / HOH | $11,412 |

### California personal exemption credit (2025, Form 540 lines 7-10)

| Item | Credit |
|---|---|
| Personal exemption (line 7) | $153 each (MFJ/QSS enter 2, i.e. $306 combined) |
| Blind exemption (line 8) | $153 each |
| 65-or-older exemption (line 9) | $153 each |
| Each dependent (line 10) | $475 |

### Renter's credit (2025, nonrefundable, Form 540 line 46)

| Filing status | Credit amount | CA AGI limit (Form 540 line 17) |
|---|---|---|
| Single | $60 | $53,994 or less |
| MFS | $60 each if both qualify and lived together (or one claims $120); $60 if lived apart all year | $53,994 or less |
| HOH / QSS | $120 | $107,988 or less |
| MFJ | $120 | $107,988 or less |

Requires paying rent for at least half of 2025 on a California principal residence; a taxpayer who can be claimed as a dependent by another person does not qualify.

### CalEITC (2025)

| Figure | Value |
|---|---|
| Maximum earned income to qualify | $32,900 |
| Maximum credit, 0 qualifying children | $302 |
| Maximum credit, 1 qualifying child | $2,016 |
| Maximum credit, 2 qualifying children | $3,339 |
| Maximum credit, 3 or more qualifying children | $3,756 |

CalEITC may provide cash back or reduce tax owed (refundable). ITIN holders are eligible.

### Young Child Tax Credit (YCTC) (2025)

| Figure | Value |
|---|---|
| Maximum credit per eligible tax return (child under 6) | $1,189 |
| Earned income limit | $32,900 or less (CalEITC-linked) |

### California AMT (Schedule P (540))

| Figure | Value |
|---|---|
| AMT rate | 7.0% of AMT income less exemption (Schedule P line 24) |
| Exemption, single or HOH | $92,749 |
| Exemption, MFJ / QSS | $123,667 |
| Exemption, MFS | $61,830 |
| Exemption phaseout | 25% of excess AMTI |

The booklet flags AMT as possible when total income exceeds the exemption amounts above. AMT is reported on Form 540 line 61.

### SDI / VPDI (2025)

| Figure | Value |
|---|---|
| SDI withholding rate 2025 | 1.2% |
| SDI taxable wage limit | None -- SB 951 removed the taxable wage limit and maximum withholdings effective January 1, 2024 |
| SDI deductibility on CA return | NOT deductible on the California return (see "The taxable base") |

---

## The taxable base

This is the critical section. California starts with federal AGI and adjusts it on Schedule CA (540): Part I adjusts income to CA AGI (column A is the federal amount, column B is a CA addition, column C is a CA subtraction); Part II re-figures itemized deductions under California law. Use Schedule CA (540) to make adjustments to your federal adjusted gross income and to your federal itemized deductions using California law.

### California non-conformity with OBBBA (P.L. 119-21)

FTB Publication 1001 (2025) states that in general the R&TC does not conform to the changes under the federal acts listed in that publication, including the OBBBA items below. Because California's IRC conformity date for 2025 is January 1, 2025 (R&TC 17024.5(a)(1)(Q)) and OBBBA was approved July 4, 2025, these provisions are not conformed to absent separate California legislation.

| Federal OBBBA provision | CA treatment | Schedule CA column |
|---|---|---|
| 100% bonus depreciation for certain qualified property acquired and placed in service after January 19, 2025 (IRC 168(k)) | California does not conform. California allows no bonus depreciation; figure CA depreciation under California law and enter the excess of federal over CA depreciation on Part I line 12, column B. Track CA basis for future years (form FTB 3885A figures the adjustment). | Column B addition |
| 100% depreciation election for qualified production property (IRC 168(n)) | California does not conform. | Column B addition |
| Full expensing of domestic research and experimental expenditures | California does not conform; CA follows its own R&E treatment. | Column B addition |
| Expansion of qualified small business stock gain exclusion | California does not conform to the expanded exclusion. | Column B addition |
| Section 179 expensing | California allows a section 179 expense election up to $25,000, with a phaseout starting at $200,000 of property placed in service (Pub 1001). Add back the excess of federal section 179 over the CA amount. | Column B addition |
| Federal SALT cap raised to $40,000 for 2025 ($40,400 for 2026) (IRC 164(b)(6)) | The federal cap only affects the federal itemized deduction. California itemizes under its own rules (below); no CA add-back of the federal cap itself. | n/a |

### QBI (IRC 199A) -- no add-back needed, but never apply it in CA

The federal qualified business income deduction is a below-the-line deduction: it reduces federal taxable income, not federal AGI. Because Schedule CA starts from federal AGI, the QBI deduction never enters the CA computation and no add-back line is required. The CA error to avoid is applying a QBI-style deduction on the CA return -- California allows none.

### Pre-OBBBA non-conformity items (ongoing, per Pub 1001 and Schedule CA instructions)

| Federal item | CA treatment |
|---|---|
| HSA (IRC 223) | California does not recognize HSAs. Employer HSA contributions (W-2 box 12 code W) are added on Part I line 1h column C; the federal HSA contribution deduction (Schedule 1 line 13) is added back on Part I line 13 column B; HSA interest/earnings are taxable in the year earned; a tax-free federal HSA distribution for qualified medical expenses is added back (line 8f column B area) and qualified expenses over 7.5% of federal AGI may go to Part II line 4 column C. |
| Educator expenses | Federal law allows the deduction; California does not conform. Add back on Part I line 11 column B. |
| Moving expenses | California does not conform to the TCJA suspension for non-military taxpayers; non-military movers complete form FTB 3913 and subtract on Part I line 14 column C. |
| Bonus depreciation (pre-OBBBA phase-down too) | California does not conform to the IRC 168(k) additional first-year deduction; enter the federal-over-CA depreciation difference on Part I line 12 column B. |
| Section 179 excess over CA limit ($25,000, phaseout at $200,000) | Add back the difference on Part I line 12 column B. |
| Net operating loss | California suspended the NOL carryover deduction for taxable years beginning on or after January 1, 2024 and before January 1, 2027; NOLs may still be computed and carried over. Taxpayers with net business income or modified AGI under $1,000,000, or with disaster loss carryovers, are not affected by the suspension. |
| Mortgage interest | Federal acquisition-debt limit is $750,000 ($375,000 MFS); California does not conform and keeps the $1,000,000 ($500,000 MFS) limit. If the federal deduction was limited, enter the amount over the federal limit on Part II line 8 column C. |
| Alimony | For agreements executed after December 31, 2025 (or modified after that date), California conforms to the federal repeal of IRC 71/215; no adjustment for those. |

### Common subtractions (federal income CA excludes)

| Item | CA treatment |
|---|---|
| Social Security benefits and Tier 1 railroad retirement | Excluded by California. Enter the taxable amount from federal AGI on Schedule CA Part I line 6 column B. |
| California lottery winnings | Excluded; enter on Part I line 8b column B. Lottery winnings from other states ARE taxable by California. California lottery losses are not deductible (Part II line 16 column B). |
| PFL (Paid Family Leave / Family Temporary Disability) benefits | Excluded; enter the 1099-G amount on Part I line 7 column B. |
| Military pay | Servicemembers domiciled outside California (and spouses/RDPs) may exclude military compensation when computing the tax rate on nonmilitary income; military pay is not CA source income when permanently stationed outside California. See FTB Pub. 1032 -- flag for reviewer. |

### Itemized deduction differences from federal (Schedule CA Part II)

| Deduction | Federal rule | CA rule |
|---|---|---|
| State and local income tax | Deductible up to the federal SALT cap ($40,000 for 2025 under OBBBA) | NOT deductible on the CA return -- California disallows state and local income tax (including other states' income taxes), SDI/VPDI, and state and local general sales tax; enter the federal amount on Part II line 5a column B |
| Property tax | Within the federal SALT cap | Deductible under CA rules (the CA disallowance above covers income, SDI, and general sales taxes, not property tax) |
| Mortgage interest | $750,000 acquisition debt limit | $1,000,000 acquisition debt limit; excess-over-federal amount is a subtraction (line 8 column C) |
| Charitable contributions | Up to 60% of AGI for cash to public charities | California limits the deduction to 50% of federal AGI; enter the difference on Part II line 11/12 column B. Conservation easements: CA limit 30% of federal AGI; CA carryover period 5 years vs federal 15 |
| Medical expenses | Over 7.5% of AGI | Over 7.5% of federal AGI |
| Casualty losses | Federally declared disasters | CA-declared disaster losses also allowed |
| Miscellaneous itemized (2% floor) | Suspended federally | California does NOT conform to the suspension -- job expenses and certain miscellaneous deductions subject to the 2% floor are deductible (Part II lines 19-22) |
| Gambling losses | Limited to winnings | Same, except California lottery losses are not deductible |

### Standard vs. itemized election

The taxpayer may choose independently for California. A taxpayer who takes the federal standard deduction may itemize on the CA return, and vice versa. CA standard deduction for 2025 is $5,706 (single/MFS) or $11,412 (MFJ/QSS/HOH) -- far below the federal amount -- so self-employed taxpayers with mortgage interest, property tax, charitable gifts, or CA-allowed miscellaneous deductions usually benefit from CA itemizing.

### Tax credits

1. **Nonrefundable credits** (reduce tax, not below zero): personal/blind/elderly exemption credits ($153 each; $475 per dependent), renter's credit ($60/$120 within the AGI limits above), child and dependent care credit, and others.
2. **Refundable credits** (can generate a refund): CalEITC, Young Child Tax Credit, Foster Youth Tax Credit.

CalEITC notes: available for wages or self-employment income; must file a CA return to claim even if no CA tax is owed; ITIN filers are eligible.

### SDI / VPDI treatment

- SDI/VPDI withheld from wages is NOT deductible on the California return. If the taxpayer deducted state and local taxes (which include SDI) federally, the Schedule CA Part II line 5a column B addition removes that deduction for CA.
- If the taxpayer takes the CA standard deduction, no separate SDI deduction arises.

### Prohibitions

**P-540-1.** NEVER apply a QBI-style deduction on the California return. California allows none; the federal QBI deduction needs no add-back only because it never enters federal AGI.

**P-540-2.** NEVER use federal bonus depreciation on the California return. California allows no bonus depreciation and caps section 179 at $25,000 with a phaseout starting at $200,000.

**P-540-3.** NEVER assume California conforms to OBBBA. Pub 1001 lists the non-conformed provisions; every OBBBA-specific federal deduction or exclusion must be evaluated for a CA add-back.

**P-540-4.** NEVER deduct state or local income tax (CA or other states'), SDI, or state and local general sales tax on the California return (Schedule CA line 5a column B).

**P-540-5.** NEVER double the $1,000,000 Behavioral Health Services Tax threshold for MFJ filers.

**P-540-6.** NEVER exclude HSA contributions or earnings from California income.

**P-540-7.** NEVER carry the federal SALT cap onto the California return; CA itemizes under CA rules.

**P-540-8.** NEVER skip the Schedule CA reconciliation. Every federal-to-California adjustment must be documented and traced.

**P-540-9.** NEVER compute CA AMT using the federal AMT rates. California AMT is 7.0%.

**P-540-10.** NEVER leave taxable Social Security in CA income. Subtract it on Schedule CA line 6 column B.

### Self-checks

**Check 200.** Schedule CA Part I starts from federal AGI -- verify the column A starting figure ties to the federal return.

**Check 201.** Every OBBBA provision used federally has a corresponding Schedule CA addition where required.

**Check 202.** HSA add-backs present if applicable (line 1h column C, line 13 column B).

**Check 203.** Behavioral Health Services Tax of 1% on taxable income over $1,000,000 computed (Form 540 line 62).

**Check 204.** Standard vs. itemized deduction is optimal on the CA return.

**Check 205.** Social Security subtracted on line 6 column B if included in federal AGI.

**Check 206.** Section 179 / depreciation differences added back and CA basis tracked (FTB 3885A).

**Check 207.** CalEITC and YCTC evaluated when earned income is $32,900 or less.

**Check 208.** Schedule P (540) completed when AMT triggers exist (large depreciation differences, ISO exercises, private activity bond interest).

**Check 209.** CA filing status matches federal filing status (limited RDP exceptions).

---

## Deadlines and filing

- Form 540 for tax year 2025 is due **April 15, 2026**.
- With an extension, the last day to file or e-file the 2025 return without the late-filing penalty is **October 15, 2026**; interest still runs from April 15, 2026.
- Different dates apply to taxpayers living or traveling outside the United States (form FTB 3519).
- The renter's credit can be claimed using CalFile; the Nonrefundable Renter's Credit Qualification Record is in the booklet.

## Penalties and interest

- **Delinquent filing penalty (individuals):** 5% of the amount due (after payments/credits made by the original due date) for each month or part of a month the return is late and unpaid, maximum 25% (R&TC 19131). If the balance due is $540 or less, the penalty is the lesser of $135 or 100% of the amount due.
- **Late payment penalty:** 0.5% of unpaid tax per month or part of a month, not to exceed 40 months.
- **Interest:** 7% for personal income tax under- and overpayments for 07/01/2025 - 06/30/2026 and 07/01/2026 - 12/31/2026 (8% for 01/01/2025 - 06/30/2025).
- **Estimated tax penalty** and **demand penalty** also apply (see FTB penalties page); estimated tax detail is in `ca-estimated-tax-540es`.

## Cross-border points

- Other states' income taxes are NOT deductible on the California return (Schedule CA line 5a column B disallows state and local income tax generally) -- unlike many states, CA gives no credit-style deduction for another state's income tax at the itemized level.
- The federal SALT cap ($40,000 for 2025, $40,400 for 2026) affects only the federal itemized deduction; CA itemizing ignores it.
- Part-year residents and nonresidents file Form 540NR (out of scope here); the booklet says to stop and file 540NR if applicable.
- Moving business property into California: depreciation methods and useful lives must be acceptable to California; if a pre-move method was unacceptable, use straight-line to compute basis (Pub 1001).
- Community property / RDP computations use combined federal AGI for limitation purposes; flag RDP allocation for the reviewer.

## Worked examples

### Worked example 1: Single filer, CA taxable income $79,294 (2025)

Single full-year resident, CA AGI $85,000, no adjustments, CA standard deduction $5,706, taxable income $79,294. Regular tax by brackets, then the $153 personal exemption credit.

```oa-check
name: Single, taxable income 79294, 2025 Schedule X
inputs:
  ti: 79294
steps:
  - b1: min(ti, 11079) * 0.01
  - b2: (min(ti, 26264) - 11079) * 0.02
  - b3: (min(ti, 41452) - 26264) * 0.04
  - b4: (min(ti, 57542) - 41452) * 0.06
  - b5: (min(ti, 72724) - 57542) * 0.08
  - b6: (ti - 72724) * 0.093
  - tax: b1 + b2 + b3 + b4 + b5 + b6
  - after_credit: tax - 153
expected:
  tax: 3812.98
  after_credit: 3659.98
```

Cross-check against the booklet's Schedule X formula for the 9.3% bracket: $3,201.97 + 9.30% of the amount over $72,724 = $3,201.97 + $611.01 = $3,812.98.

### Worked example 2: High-income freelancer triggers the Behavioral Health Services Tax

Single filer, CA taxable income $1,200,000. Regular tax uses the 12.3% bracket over $742,953; the 1% surcharge applies to the excess over $1,000,000.

```oa-check
name: Single, taxable income 1200000, BHST
inputs:
  ti: 1200000
steps:
  - reg: 72219.84 + (ti - 742953) * 0.123
  - bhst: (ti - 1000000) * 0.01
  - total: reg + bhst
expected:
  reg: 128436.62
  bhst: 2000
  total: 130436.62
```

The marginal rate on income above $1,000,000 is 12.3% plus the 1% surcharge.

### Worked example 3: MFJ couple just over the $1,000,000 threshold

MFJ with combined CA taxable income of $1,050,000 (one spouse $900,000, the other $150,000). The surcharge is based on the JOINT taxable income; the threshold is not doubled and not measured per spouse.

```oa-check
name: MFJ joint taxable income 1050000, BHST
inputs:
  ti: 1050000
steps:
  - bhst: (ti - 1000000) * 0.01
expected:
  bhst: 500
```

### Worked example 4: OBBBA bonus depreciation add-back

Sole proprietor placed $200,000 of equipment in service March 1, 2025 and claimed 100% federal bonus ($200,000). California allows no bonus depreciation; assume the CA MACRS year-one deduction is $40,000 (verify with FTB 3885A). The Schedule CA Part I line 12 column B addition is the federal-over-CA difference, and the remaining CA basis carries forward.

```oa-check
name: Bonus add-back, 200000 equipment
inputs:
  fed_dep: 200000
  ca_dep: 40000
steps:
  - addback: fed_dep - ca_dep
  - ca_basis_forward: 200000 - ca_dep
expected:
  addback: 160000
  ca_basis_forward: 160000
```

### Worked example 5: Section 179 phaseout in California

Same taxpayer claimed $500,000 of federal section 179. CA maximum is $25,000, phased out dollar-for-dollar past $200,000 of property placed in service: the $300,000 excess wipes out the CA allowance entirely, so CA section 179 is $0 and the full $500,000 is added back (then depreciated under CA MACRS going forward).

```oa-check
name: CA 179 phaseout, 500000 placed in service
inputs:
  cost: 500000
  fed179: 500000
steps:
  - phaseout: max(0, cost - 200000)
  - ca179: max(0, min(25000, 25000 - phaseout))
  - addback: fed179 - ca179
expected:
  ca179: 0
  addback: 500000
```

### Worked example 6: Federal standard deduction, CA itemized

Single filer, federal AGI $95,000, takes the federal standard deduction. Property tax $9,000, mortgage interest $7,000, charitable $3,000. CA itemized beats the CA standard deduction by a wide margin; the elections are independent.

```oa-check
name: CA itemized vs standard, single
inputs:
  prop: 9000
  mort: 7000
  char: 3000
steps:
  - ca_itemized: prop + mort + char
  - advantage: ca_itemized - 5706
expected:
  ca_itemized: 19000
  advantage: 13294
```

### Worked example 7: 2% miscellaneous itemized deductions (CA allows, federal does not)

Taxpayer has $3,000 unreimbursed employee business expenses and $1,500 tax preparation fees; federal AGI $80,000. Federal deduction is $0 (suspended). CA applies the 2% floor and allows the excess as a Part II lines 19-22 subtraction.

```oa-check
name: CA 2% misc deduction
inputs:
  agi: 80000
  misc: 4500
steps:
  - floor_amt: agi * 0.02
  - ded: misc - floor_amt
expected:
  floor_amt: 1600
  ded: 2900
```

### Worked example 8: Social Security recipient with self-employment income

Taxpayer receives $18,000 of Social Security, of which $15,300 (85%) is in federal AGI, plus $50,000 Schedule C net profit. California excludes Social Security entirely: subtract $15,300 on Schedule CA Part I line 6 column B.

```oa-check
name: SS subtraction, 18000 benefits
inputs:
  ss: 18000
steps:
  - subtract: ss * 0.85
expected:
  subtract: 15300
```

### Worked example 9: Mortgage interest difference ($750K federal vs $1M CA)

$900,000 acquisition mortgage. Federal deduction is limited to interest on $750,000; California allows interest on the full $900,000 (under its $1,000,000 limit). The interest allocable to the $150,000 excess is a CA subtraction on Part II line 8 column C. Flag the pro-rata allocation for the reviewer.

### Worked example 10: Low-income sole proprietor, CalEITC + YCTC

Single ITIN filer, net self-employment income $22,000 (all earned income), one child age 4. Earned income is within the $32,900 limit, so CalEITC (maximum $2,016 for one child) and YCTC ($1,189) apply; both can produce cash back even with zero CA tax.

```oa-check
name: CalEITC plus YCTC maxima, one child
inputs:
  cal_eitc_max: 2016
  yctc: 1189
steps:
  - combined: cal_eitc_max + yctc
expected:
  combined: 3205
```

The actual CalEITC at $22,000 of earned income is below the maximum; compute from the FTB table.

## Ask the client first

- Where did you live and work all year? (Full-year CA resident vs 540NR territory.)
- What depreciation did you claim federally -- bonus, section 179, R&E expensing? (Drives the largest Schedule CA additions.)
- Do you have an HSA? (Add-backs and CA-taxable earnings.)
- Did you receive Social Security, California lottery winnings, or PFL benefits? (Subtractions.)
- Did you pay rent in California for at least half the year, and what is your CA AGI? (Renter's credit.)
- Do you have children under 6, and is earned income $32,900 or less? (CalEITC/YCTC.)
- Any ISO exercises, private activity bond interest, or large depreciation differences? (Schedule P AMT screen.)
- Military domicile or stationing outside California? (Pub 1032 rules.)

### Known gaps

1. Part-year and nonresident returns (Form 540NR) are not supported.
2. Community property rules for RDP/same-sex couples require reviewer judgment.
3. California NOL carryforward/carryback mechanics beyond the 2024-2026 suspension are not detailed.
4. Specific CA disaster loss rules beyond the general casualty difference are not covered.
5. California's legislative response to OBBBA may change; monitor FTB conformity updates.

### Cross-skill references

**Inputs from:** `us-federal-return-assembly`, `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, `us-qbi-deduction` (for information only -- no CA add-back), `us-self-employed-health-insurance`, `us-self-employed-retirement`.

**Outputs to:** `ca-estimated-tax-540es`, `ca-form-3853-coverage`, `us-ca-return-assembly`.

### Change log
- **v0.1 (April 2026):** Stub.
- **v0.2 (April 2026):** Full content skill with Schedule CA adjustments, OBBBA decoupling, brackets, credits, AMT, edge cases, and test suite.
- **v0.3 (November 2026):** Deep-review corrections against archived FTB/EDD/leginfo sources: 2025 brackets, standard deduction, exemption credits, renter's credit, CalEITC/YCTC, AMT, SDI, conformity date, bonus/179 treatment, SALT and itemized rules; edge cases and tests rebuilt as worked examples.

### End of skill

---

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| FTB 2025 Personal Income Tax Booklet (Form 540 instructions, Schedules X/Y) | https://www.ftb.ca.gov/forms/2025/2025-540-booklet.html | 2026-11-01 |
| FTB Schedule CA (540) Instructions 2025 | https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html | 2026-11-01 |
| FTB Form 540 (2025) | https://www.ftb.ca.gov/forms/2025/2025-540.pdf | 2026-11-01 |
| FTB Schedule P (540) instructions 2025 | https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html | 2026-11-01 |
| FTB Schedule P (540) (2025) | https://www.ftb.ca.gov/forms/2025/2025-540-p.pdf | 2026-11-01 |
| R&TC section 17024.5 (IRC conformity date) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17024.5 | 2026-11-01 |
| R&TC section 17043 (1% tax over $1,000,000) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043 | 2026-11-01 |
| FTB CalEITC eligibility and credit information (2025) | https://www.ftb.ca.gov/file/personal/credits/caleitc/eligibility-and-credit-information.html | 2026-11-01 |
| FTB Young Child Tax Credit (2025) | https://www.ftb.ca.gov/file/personal/credits/young-child-tax-credit.html | 2026-11-01 |
| EDD Rates and Withholding (SDI 2025) | https://www.edd.ca.gov/Payroll_Taxes/Rates_and_Withholding.htm | 2026-11-01 |
| FTB Penalties and Interest | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html | 2026-11-01 |
| FTB Interest and Estimate Penalty Rates | https://www.ftb.ca.gov/pay/penalties-and-interest/interest-and-estimate-penalty-rates.html | 2026-10-31 |
| P.L. 119-21 (OBBBA) full text | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-01 |

Not yet confirmed: the federal standard deduction for 2025 (commonly cited as $15,750) and the federal section 179 dollar limit for 2025 (commonly cited as $2,500,000) -- no archived federal-inflation source in this pack; the Schedule CA line number that carries total federal AGI (the instructions text archived here does not show it); FTB Publication 1001 (2025) was read from an archived copy that has no sidecar, so it is cited in the body but not listed above.

## Talk to a verified accountant

This skill is general reference for AI-assisted preparation. A credentialed professional (CPA, EA, or attorney under Circular 230) must review and sign any California return prepared with it, especially where OBBBA add-backs, CA basis tracking, AMT, or RDP/community property issues appear.
