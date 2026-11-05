---
name: wi-payroll
description: Wisconsin Payroll Skill (Tax Year 2025)
jurisdiction: US-WI
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# WI Payroll

## Who this applies to

This Tier 2 content skill covers Wisconsin (WI) state payroll obligations for tax year 2025 for employers maintaining a worksite, remote employees, or assigned workers in Wisconsin. It is designed to be loaded alongside `us-tax-workflow-base` (Tier 1) and `us-federal-payroll` (Tier 2) when payroll runs include Wisconsin-source wages.

In scope:

- Wisconsin Personal Income Tax (PIT) withholding under Wis. Stat. ch. 71 subch. X (§§ 71.63–71.83) (US-WI-dr-wis-stat-ch71.txt: "71.63 Definitions. 71.64 Employers required to withhold. 71.65 Filing returns or reports. 71.66 Employee exemption certificates"; ss. 71.82 Interest and 71.83 Penalties in the same chapter).
- Form WT-4 (Employee's Wisconsin Withholding Exemption Certificate) and its interaction with federal Form W-4.
- Form WT-6 (deposit report) and Form WT-7 (annual reconciliation).
- Wisconsin Unemployment Insurance (UI) tax administered by the Department of Workforce Development (DWD) under Wis. Stat. ch. 108.
- Reciprocal income tax agreements with Illinois, Indiana, Kentucky, and Michigan (Form W-220).
- Worker classification under the Wisconsin 9-factor test (Wis. Stat. § 108.02(12)) and the federal common-law rules where they diverge.
- New hire reporting under Wis. Stat. § 49.22(2dm) (see the "Not yet confirmed:" paragraph in Sources).
- Final pay timing, workers' compensation coverage, and the Milwaukee local paid sick leave ordinance (Milwaukee County ordinance enacted 2024, effective 2025) -- flagged as audit flash points.

Out of scope:

- Wisconsin corporate franchise/income tax (delegated to a separate corporate-tax skill).
- Wisconsin sales/use tax.
- Federal employment taxes (FICA, FUTA, federal income tax withholding) -- see `us-federal-payroll`.
- Multistate apportionment beyond the four reciprocal border states.
- Public-sector or tribal employer payroll.

This skill assumes a human reviewer credentialed under Circular 230 (EA, CPA, or attorney) reviews and signs off on every output before it reaches the taxpayer, the Wisconsin Department of Revenue (DOR), or DWD.

## 2. Wisconsin Personal Income Tax (PIT)

### 2.1 2025 Bracket Schedule

**Single filers and Head-of-Household (2025)**  _(Wis. Stat. § 71.06(1r); bracket indexing § 71.06(2e))_ (US-WI-dr-wis-stat-ch71.txt)

| Bracket | Taxable Income (Single) | Marginal Rate |
| --- | --- | --- |
| 1 | $0 – $14,680 | 3.50% |
| 2 | $14,681 – $50,480 | 4.40% |
| 3 | $50,481 – $323,290 | 5.30% |
| 4 | Over $323,290 | 7.65% |

Archive-verbatim: "On all taxable income from $0 to $14,680, 3.50 percent ... exceeding $14,680 but not exceeding $50,480, 4.40 percent ... exceeding $50,480 but not exceeding $323,290, 5.30 percent ... exceeding $323,290, 7.65 percent" (US-WI-dr-wis-stat-ch71.txt, s. 71.06(1r)).

**Married Filing Jointly (2025)**  _(Wis. Stat. § 71.06(2)(k))_ (US-WI-dr-wis-stat-ch71.txt)

| Bracket | Taxable Income (MFJ) | Marginal Rate |
| --- | --- | --- |
| 1 | $0 – $19,580 | 3.50% |
| 2 | $19,581 – $67,300 | 4.40% |
| 3 | $67,301 – $431,060 | 5.30% |
| 4 | Over $431,060 | 7.65% |

Archive-verbatim: "$0 to $19,580, 3.50 percent ... exceeding $19,580 but not exceeding $67,300, 4.40 percent ... exceeding $67,300 but not exceeding $431,060, 5.30 percent ... exceeding $431,060, 7.65 percent" (US-WI-dr-wis-stat-ch71.txt, s. 71.06(2)(k)).

**Married Filing Separately (2025)**  _(Wis. Stat. § 71.06(2)(L))_ (US-WI-dr-wis-stat-ch71.txt)

| Bracket | Taxable Income (MFS) | Marginal Rate |
| --- | --- | --- |
| 1 | $0 – $9,790 | 3.50% |
| 2 | $9,791 – $33,650 | 4.40% |
| 3 | $33,651 – $215,530 | 5.30% |
| 4 | Over $215,530 | 7.65% |

Archive-verbatim: "$0 to $9,790, 3.50 percent ... exceeding $9,790 but not exceeding $33,650, 4.40 percent ... exceeding $33,650 but not exceeding $215,530, 5.30 percent ... exceeding $215,530, 7.65 percent" (US-WI-dr-wis-stat-ch71.txt, s. 71.06(2)(L)).

- **Bracket source and act references** -- Wisconsin has four brackets for tax year 2025 indexed annually for inflation under Wis. Stat. § 71.06(2e) (US-WI-dr-wis-stat-ch71.txt: "(2e) BRACKET INDEXING ... shall be increased each year by a percentage equal to the percentage change between the U.S. consumer price index"; the s. 71.06 history line cites "2023 a. 19"). Rates were last reset by 2023 Wis. Act 19 (the biennial budget); the 2023 Wis. Act 1 attribution and the DOR late-2024 indexing announcement / Pub 117 sourcing see the "Not yet confirmed:" paragraph in Sources.  _(Wis. Stat. § 71.06(2e); 2023 Wis. Act 19)_

### 2.2 Supplemental Withholding Rate

- **Supplemental wage flat withholding rate** -- a flat rate applies to supplemental wages (figure see the "Not yet confirmed:" paragraph in Sources)  _(DOR rule / Pub 166, 2025 edition)_
- **Supplemental wage aggregation option** -- If the employer aggregates supplemental wages with regular wages and uses the percentage or wage-bracket method in Pub 166, no separate supplemental rate applies.  _(Pub 166, 2025 edition)_

### 2.3 Standard Deduction (used by WT-4 worksheet only)

- **Standard deduction figures used by the WT-4 worksheet** -- single, MFJ, MFS and HOH amounts and their phase-out AGI points are not in the archived sources (figures see the "Not yet confirmed:" paragraph in Sources)  _(WT-4 worksheet, 2025)_
- **Employer treatment of standard deduction** -- Employers do not compute the standard deduction directly -- the wage-bracket and percentage tables in Pub 166 have it baked in. It matters only when an employee uses the WT-4 worksheet to claim additional exemptions.  _(Pub 166)_

### 2.4 Personal and Dependency Exemptions

- **Value per personal/dependency exemption on WT-4** -- $700 per year (US-WI-dr-wis-stat-ch71.txt, s. 71.05(23): "A personal exemption of $700 ... An exemption of $700 for each dependent")  _(Wis. Stat. § 71.05(23))_
- **Additional exemption for age 65+ and WT-4 vs W-4 divergence** -- Employees over age 65 may claim an additional exemption (US-WI-dr-wis-stat-ch71.txt, s. 71.05(23): "An additional exemption of $250 if the taxpayer has reached the age of 65 ... and $250 for the taxpayer's spouse"). The WT-4 differs from federal Form W-4 -- Wisconsin did not adopt the 2020 W-4 redesign for state purposes.  _(Wis. Stat. § 71.05(23))_

## 3. Form WT-4: Wisconsin Withholding Exemption Certificate

### 3.1 When Required

- **WT-4 required at hire; W-4 insufficient; default withholding if not filed** -- Every new employee must complete Form WT-4 on or before the first day of work. The federal Form W-4 alone is insufficient for Wisconsin withholding because: 1. WT-4 uses an allowance-based system that the federal W-4 abandoned in 2020. 2. WT-4 captures reciprocal-state residency declarations not present on W-4. 3. WT-4 includes the Wisconsin-specific "additional amount to be withheld" line. If an employee fails to file a WT-4, the employer must withhold as if the employee is single with zero exemptions (the most conservative posture, per Wis. Admin. Code Tax § 2.93(2) -- see the "Not yet confirmed:" paragraph in Sources).  _(Wis. Admin. Code Tax § 2.93(2))_

### 3.2 Allowance Structure

- **WT-4 allowance value and comparison to federal** -- Each WT-4 allowance reduces taxable wages by $700/year (US-WI-dr-wis-stat-ch71.txt, s. 71.05(23) "$700" exemption; the $26.92 biweekly / $13.46 weekly conversions are arithmetic on $700). The comparison to the federal pre-TCJA $4,300 allowance is not in the archived sources (see the "Not yet confirmed:" paragraph in Sources). An employee who claims 4 federal allowances on a (pre-2020) W-4 cannot simply transfer that to WT-4: the equivalent Wisconsin claim depends on the personal exemption math, not on allowance count.  _(WT-4 form instructions)_

### 3.3 Reciprocal-State Box

- **Reciprocal-state box mechanics** -- The WT-4 includes a checkbox for employees who are residents of Illinois, Indiana, Kentucky, or Michigan and elect to have wages taxed by their home state rather than Wisconsin. If the employee checks this box AND files Form W-220 with the employer (see Section 6), the employer must: Stop withholding Wisconsin income tax on those wages. Begin withholding the home-state income tax (if registered there) OR not withhold any state income tax (if not registered, and document the W-220 in the employee's payroll file).  _(Form WT-4 instructions; Section 6)_

AUDIT FLASH POINT -- Reciprocal-State Misclassification. A common employer error is to honor a verbal reciprocity claim without obtaining a signed W-220 on file. DOR has assessed penalties on employers who under-withheld Wisconsin tax on the strength of a verbal claim. Always require a signed and dated W-220 before suspending Wisconsin withholding. Re-collect W-220 annually -- it expires each calendar year.

### 3.4 Submission to DOR

- **Submission requirement and penalty** -- Employers must submit a copy of Form WT-4 to DOR within 20 days if the employee claims more than 10 allowances OR claims complete exemption from withholding (under Wis. Admin. Code Tax § 2.93(2m)). Failure to submit is a $50 penalty per certificate per Wis. Stat. § 71.83(1)(b)4.  _(Wis. Admin. Code Tax § 2.93(2m); Wis. Stat. § 71.83(1)(b)4)_

## 4. Deposit Cadence -- Form WT-6

### 4.1 Filing Frequency Determination

**Filing Frequency Determination**  _(US-WI-Filing-Frequency-Changes.aspx.html; statutory semi-monthly rule in Wis. Stat. § 71.64(2)/§ 71.65(3))_

| Annual WI Withholding (remittances) | Frequency | Form |
| --- | --- | --- |
| $20,001 or more/year | Semi-Monthly | WT-6 |
| $2,401 – $20,000/year | Monthly | WT-6 |
| $301 – $2,400/year | Quarterly | WT-6 |
| $300/year or less | Annual | WT-6 (filed with WT-7) |

Archive-verbatim: "Withholding Tax Filing Frequency Remittances Semi-Monthly $20,001 or more/year Monthly $2,401 - $20,000/year Quarterly $301 - 2,400/year Annual $300/year" (US-WI-Filing-Frequency-Changes.aspx.html).

- **New employer default frequency** -- New employers default to a starter frequency until DOR assigns one based on actual liability (see the "Not yet confirmed:" paragraph in Sources).  _(Wis. Admin. Code Tax § 2.04)_

### 4.2 Due Dates

- **Deposit due dates by frequency** -- Semi-monthly filers: Wages paid on the 1st–15th are due by the last day of the same month. Wages paid on the 16th–end-of-month are due by the 15th of the following month (US-WI-dr-wis-stat-ch71.txt, s. 71.65(3): "for amounts deducted and withheld from the first day of the month through the 15th day of the month, the employer shall file such reports and pay over such taxes on or before the last day of such month; for amounts deducted and withheld from the 16th day of the month through the last day of the month, the employer shall file reports and deposit such taxes on or before the 15th day of the next succeeding month"). Monthly filers: Due by the last day of the month following the payroll month. Quarterly filers: Due by the last day of the month following the quarter-end (April 30, July 31, October 31, January 31). Annual filers: Due January 31 with Form WT-7 (s. 71.65: "On or before January 31 of each year every employer shall file a withholding report"). The next-business-day roll-over rule (Wis. Stat. § 990.001(4)) is not in the archived sources -- see the "Not yet confirmed:" paragraph in Sources.

### 4.3 Filing Mechanics

- **E-file mandate and payment methods** -- All WT-6 deposits must be filed electronically via My Tax Account (DOR's online portal) for employers with annual withholding of $300 or more (Wis. Stat. § 71.65(3)(d), e-file mandate). Paper filing is permitted only for employers under the $300 threshold and is being phased out -- DOR has signaled paper acceptance will end no later than tax year 2026. Payment must be made by ACH debit or ACH credit. Paper checks are not accepted for e-mandated filers.  _(Wis. Stat. § 71.65(3)(d))_

### 4.4 Penalty for Late Deposit

- **Late filing penalty** -- 5% per month, capped at 25% (US-WI-dr-wis-stat-ch71.txt, s. 71.83(2)(d)4 late-filing-of-withholding-report: "5 percent of the amount if the failure is not for more than one month, with an additional 5 percent for each additional month or fraction thereof ... not exceeding 25 percent in the aggregate")  _(Wis. Stat. § 71.83(2)(d)4)_
- **Late payment interest** -- delinquent withheld deposits bear interest at 1.5% per month, reducible to 12% per year in stated instances (US-WI-dr-wis-stat-ch71.txt, s. 71.83(2)(d): "Delinquent deposits or payments shall bear interest at the rate of 1.5 percent per month"; s. 71.82(1) normal interest "at 12 percent per year")  _(Wis. Stat. § 71.82(1); § 71.83(2)(d))_
- **Negligence/incomplete-report penalty** -- 25% of the amount not reported, withheld, deposited or paid over, upon a departmental showing (US-WI-dr-wis-stat-ch71.txt, s. 71.83(2)(d)3: "there shall be added to the tax 25 percent of the amount not reported or not withheld, deposited or paid over")  _(Wis. Stat. § 71.83(2)(d)3)_
- **Fraud penalty** -- a false withholding exemption claim made with intent to defeat or evade proper withholding draws a penalty equal to the under-withheld difference (US-WI-dr-wis-stat-ch71.txt, s. 71.83: "with the intent to defeat or evade the proper withholding of tax under subch. X shall be subject to a penalty equal to the difference"); the older "50% of the underpayment" figure is not in the archived sources -- see the "Not yet confirmed:" paragraph in Sources.  _(Wis. Stat. § 71.83)_

## 5. Form WT-7: Annual Reconciliation

### 5.1 Purpose

- **WT-7 purpose** -- Form WT-7 reconciles total Wisconsin income tax withheld during the calendar year (sum of all WT-6 deposits) against the W-2 and 1099 totals reported to employees. It is the Wisconsin counterpart to federal Form W-3 and serves as the wage statement transmittal.  _(Section 5.1)_

### 5.2 Due Date

- **WT-7 due date** -- January 31 of the year following the tax year (for 2025 wages: January 31, 2026). No extensions are granted.  _(Section 5.2)_

### 5.3 What Must Accompany WT-7

- **Required attachments to WT-7** -- Copy 1 of all W-2 forms issued to employees with Wisconsin wages. Copy 1 of all 1099-NEC and 1099-MISC forms for non-employee compensation where Wisconsin tax was withheld. 1099-R forms for retirement plan distributions where Wisconsin tax was withheld. W-2/1099 data is submitted electronically through the DOR's WT-7 e-file system or via the SSA's Combined Federal/State Filing program (CFSF) where Wisconsin participates.  _(Section 5.3)_

### 5.4 Common Reconciliation Errors

1. Bonus accrual mismatch: Bonus paid January 5 but accrued in prior year. Wisconsin uses cash-basis withholding -- report in the year of payment. 2. Reciprocal-state wages omitted from W-2 Box 16: Employer correctly stopped WI withholding under W-220 but failed to record zero in Box 17 -- leave Box 17 blank with the WI code in Box 15, NOT report Illinois wages in WI Box 16. 3. Sign-on bonus clawback: If a 2024 bonus is repaid in 2025, the W-2c correction reduces 2024 W-2 Box 1; the WT-7 for 2025 is NOT adjusted (cash-basis principle).

## 6. Reciprocal Agreements

Wisconsin has reciprocal income-tax agreements with four bordering states. Under each agreement, wages earned by a resident of the reciprocal state working in Wisconsin (or vice versa) are taxed ONLY by the state of residence, not the state where the work is performed.

### 6.1 The Four Agreements

**The Four Agreements**  _(Wis. Stat. § 71.05(2); US-WI-dr-wis-stat-ch71.txt: "(2) NONRESIDENT RECIPROCITY. All payments received by natural persons domiciled outside Wisconsin who derive income from the performance of personal services in Wisconsin shall be excluded from Wisconsin gross income to the extent that it is subjected to an income tax imposed by the state of domicile"; Illinois agreement machinery at s. 71.10(7e))_

| Reciprocal State | Statutory Basis (WI) | Form Filed by Employee |
| --- | --- | --- |
| Illinois | Wis. Stat. § 71.05(2) + s. 71.10(7e) (archived); IL 35 ILCS 5/302 (see the "Not yet confirmed:" paragraph in Sources) | W-220 (to WI employer) / IL-W-5-NR (to IL employer) |
| Indiana | Wis. Stat. § 71.05(2) + IN 6-3-5-1 (see the "Not yet confirmed:" paragraph in Sources) | W-220 / WH-47 |
| Kentucky | Wis. Stat. § 71.05(2) + KRS 141.070 (see the "Not yet confirmed:" paragraph in Sources) | W-220 / 42A809 |
| Michigan | Wis. Stat. § 71.05(2) + MCL 206.256 (see the "Not yet confirmed:" paragraph in Sources) | W-220 / MI-W4 with reciprocity box |

- **Minnesota reciprocity note** -- The archived statute contains Minnesota income-tax reciprocity machinery: s. 71.10(7) "MINNESOTA INCOME TAX RECIPROCITY ... income tax reciprocity reached with the state of Minnesota under s. 71.05 (2)" referencing 2023 Wisconsin Act 147, section 4 (2), and conditions for agreements entered on or after March 23, 2024 (US-WI-dr-wis-stat-ch71.txt). The earlier "terminated 2009, never re-enacted" claim is contradicted by the archive; whether an agreement is operative for 2025 wages must be verified with current DOR guidance before suspending withholding for MN residents.  _(US-WI-dr-wis-stat-ch71.txt s. 71.10(7))_

### 6.2 Form W-220 Mechanics

- **W-220 mechanics steps** -- Form W-220 ("Nonresident Employee's Withholding Reciprocity Declaration") is filed by an employee who is a resident of IL, IN, KY, or MI and works in Wisconsin. The employer must: 1. Obtain a signed W-220 BEFORE suspending Wisconsin withholding. 2. Re-collect W-220 annually (W-220 expires December 31 each year). 3. Withhold the home state's income tax if the employer is registered there. 4. If the employer is not registered in the home state and has no other nexus there, the employee is responsible for estimated tax payments to the home state -- the employer simply withholds nothing for state income tax. 5. Report wages on a Wisconsin W-2 with the wages amount in Box 16 but $0 in Box 17 (or omit Box 16 if the employer also withholds for the home state and issues a single multistate W-2).  _(Pub 121 -- Reciprocity)_

AUDIT FLASH POINT -- Reciprocal State Classification. DOR auditors routinely examine reciprocal-state W-2s where Box 1 federal wages differ materially from Box 16 Wisconsin wages. Common audit issues: Employee moves mid-year -- proration of WI vs IL/IN/KY/MI wages was not documented. Employee files W-220 in February but employer applied it retroactively to January wages (NOT permitted -- W-220 is prospective). Employee is dual-resident (e.g., Wisconsin domicile but Illinois statutory residence) -- reciprocity does not apply where the employee is a Wisconsin resident. Always verify domicile, not just driver's license state. Employer never re-collected W-220 -- last on file is 2023.

### 6.3 Audit Red Flags for Reciprocal Workers

When preparing a WI payroll for a multistate-border employer, flag these scenarios for reviewer attention: 1. Employee with an out-of-state mailing address but a Wisconsin driver's license. 2. Employee whose W-220 lists IL/IN/KY/MI but whose home address on file is Wisconsin. 3. Employee who lived in IL for 3 months, then moved to WI -- wages earned during the IL-resident months are reciprocal-treated; wages after the move are fully Wisconsin-taxable. 4. Remote employee working from home in IL but assigned to a Wisconsin office -- generally Wisconsin-sourced if the work product is delivered to Wisconsin, but reciprocity applies to the personal income tax. The Wisconsin UI tax (Section 7) follows DIFFERENT rules (worksite/localization-of-services test).

### 6.4 Sourcing vs Reciprocity

- **Reciprocity limited to state income tax** -- A critical distinction: reciprocity covers state income tax only. It does NOT change: The state where unemployment insurance is paid (governed by the four-part DOL localization test in 26 U.S.C. § 3306(j)). The state where workers' compensation must be carried. New hire reporting (the work state, generally). Sales tax nexus. A Wisconsin employer with an Illinois-resident driver may correctly not withhold Wisconsin PIT under reciprocity, while STILL paying Wisconsin UI tax on that driver's wages (because the driver is "localized" in Wisconsin under the DOL test). This split is the most common payroll error among out-of-state-border employers.  _(26 U.S.C. § 3306(j))_

## 7. Wisconsin Unemployment Insurance (UI)

### 7.1 Coverage Threshold

- **Coverage threshold conditions** -- Under Wis. Stat. § 108.02(13), an employer is covered by Wisconsin UI if any one of several triggers is met (quarterly-wage, weeks-of-employment, acquisition, 501(c)(3), agricultural and domestic-service triggers -- the dollar figures are not in the archived sources; see the "Not yet confirmed:" paragraph in Sources).  _(Wis. Stat. § 108.02(13))_

### 7.2 2025 Wage Base

- **Wisconsin UI taxable wage base 2025** -- a per-employee annual taxable wage base applies (figure see the "Not yet confirmed:" paragraph in Sources)  _(Wis. Stat. § 108.18(1)(am))_
- **Wage base historical note and application** -- The base is set by statute rather than by indexed formula. UI tax is paid on wages up to the wage base; wages above the base per employee are not subject to UI tax for that year.  _(Wis. Stat. § 108.18(1)(am))_

### 7.3 Tax Rates (2025 Schedule)

**2025 UI Tax Rate Schedule D** -- the reserve-ratio rate grid and the trust-fund balance band are not in the archived sources; the full schedule is carried in the "Not yet confirmed:" paragraph in Sources.  _(Schedule D)_

- **New employer rates** -- separate non-construction and construction starter rates apply for the first 3 calendar years until experience rating begins (figures see the "Not yet confirmed:" paragraph in Sources)  _(Wis. Stat. § 108.18(2)(c))_
- **Solvency Tax 2025** -- no solvency surcharge applied for 2025 because trust fund balances remained above the trigger (see the "Not yet confirmed:" paragraph in Sources)  _(Section 7.3)_

### 7.4 Reporting -- Form UCT-101 and UCT-7823

- **UI reporting forms and due dates** -- UI wages and contributions are reported QUARTERLY on Form UCT-101 (with wage detail on Form UCT-7823) through the DWD online portal at dwd.wisconsin.gov/uitax (the archived US-WI-uitax.html shows the next quarterly report/wage report filing due date as November 2, 2026). The Apr 30 / Jul 31 / Oct 31 / Jan 31 calendar and the 25-worker e-file mandate are not in the archived sources -- see the "Not yet confirmed:" paragraph in Sources.  _(Wis. Admin. Code DWD 110.04)_

### 7.5 Penalties

- **UI penalties** -- Late filing and late-payment figures are not in the archived sources (see the "Not yet confirmed:" paragraph in Sources). On misclassification fines: the archived withholding statute imposes a **$25,000 fine per violation** on a construction contractor who willfully misclassifies an employee as a nonemployee (US-WI-dr-wis-stat-ch71.txt, s. 71.64(6): "misclassifies or attempts to misclassify an individual who is an employee of the employer as a nonemployee shall be fined $25,000 for each violation"); the separate § 108.221 / 2009 Wis. Act 292 misclassification penalty is not in the archive -- see the "Not yet confirmed:" paragraph in Sources.  _(Wis. Stat. § 71.64(6); Wis. Stat. § 108.221)_

## 8. Worker Classification -- The Wisconsin 9-Factor Test

### 8.1 The Statutory Test

- **Two-step Part A/Part B test and nine factors** -- Wis. Stat. § 108.02(12)(bm) creates a two-step worker classification test for UI purposes that is materially stricter than the federal IRS common-law test. A worker is presumed to be an employee unless the employer can demonstrate BOTH: (a) The worker is free from the employer's control or direction in performing the services (the "Part A" test); AND (b) The worker satisfies SIX OR MORE of the following nine "Part B" conditions: 1. The individual advertises or otherwise affirmatively holds out to the public as being in business. 2. The individual maintains his or her own office or performs most of the services in a facility or location chosen by the individual and uses his or her own equipment or materials in performing the services. 3. The individual operates under multiple contracts with one or more employers to perform specific services. 4. The individual incurs the main expenses related to the services that he or she performs under contract. 5. The individual is responsible for the satisfactory completion of the services that he or she contracts to perform and is liable for a failure to satisfactorily complete the services. 6. The individual receives compensation for services performed under a contract on a commission, per-job, or competitive-bid basis and not on any other basis. 7. The individual may realize a profit or suffer a loss under contracts to perform such services. 8. The individual has recurring business liabilities or obligations. 9. The success or failure of the individual's business depends on the relationship of business receipts to expenditures. Threshold: the worker must meet SIX of nine, not five. Failing even one of the six required factors flips the classification to employee.  _(Wis. Stat. § 108.02(12)(bm))_

### 8.2 The Wisconsin Test Compared to the IRS Common-Law Test

- **Wisconsin test stricter than IRS common-law** -- The IRS common-law test (ABC variant in some states, three-prong control/behavioral/financial in federal) is generally easier to satisfy as "independent contractor" than the Wisconsin test. A worker who is a contractor for IRS / federal 1099-NEC purposes may still be an employee for Wisconsin UI purposes -- and the employer must pay Wisconsin UI tax on that worker even while issuing a 1099 for federal purposes. This is a frequent and expensive misclassification trap.

### 8.3 The Wisconsin Workers' Compensation Test (Separate Test)

- **Separate nine-factor WC test** -- For workers' compensation purposes under Wis. Stat. § 102.07(8), Wisconsin uses a NINE-factor test that is similar but NOT identical to the UI 9-factor test. A worker may be: An employee for UI (108.02(12)) but not for WC (102.07(8)), or vice versa. Independent for both. Employee for both. When classifying a Wisconsin worker, both tests must be run.  _(Wis. Stat. § 102.07(8))_

AUDIT FLASH POINT -- Contractor 9-Factor Test. Wisconsin DWD has aggressively pursued misclassification audits since 2017 under the "Joint Enforcement Task Force on Worker Misclassification" established by Executive Order 20. Common findings: Worker treated as 1099 under federal rules but fails Wisconsin Part B (e.g., does not "hold out to the public" -- they only work for one employer). Worker incurs no main expenses (factor 4 fails) -- typically because the employer provides all tools and materials. Worker is not subject to profit/loss risk (factor 7 fails) -- paid hourly with no risk of loss. Penalty exposure includes back UI tax, interest, the § 108.221 misclassification penalty (up to $25,000 per worker), and possible criminal referral under Wis. Stat. § 108.24 for willful violations. When a worker is borderline, the conservative default is employee classification for Wisconsin purposes even if federal classification is contractor. Document the reasoning either way.

### 8.4 The Wisconsin DOR Test (Income Tax Withholding)

- **DOR uses federal common-law test for withholding** -- For Wisconsin income tax withholding purposes (Wis. Stat. § 71.63(2)), Wisconsin uses the federal common-law test by reference. So a worker classified as a federal contractor (1099-NEC) is also a contractor for Wisconsin withholding -- no WT-4 collection, no withholding, but issue a 1099-NEC. This creates a third-axis disconnect: a worker can simultaneously be a federal contractor (no W-2), a Wisconsin income-tax contractor (no WT-4), but a Wisconsin UI employee (pay UI on their wages). This is administrable but requires careful payroll-system configuration. The § 71.63(2) federal-test reference is not in the archived text (archived s. 71.63 is "Definitions") -- see the "Not yet confirmed:" paragraph in Sources.  _(Wis. Stat. § 71.63(2))_

## 9. Milwaukee Local Paid Sick Leave

### 9.1 State-Level Position

- **No statewide mandate; 2017 preemption** -- Wisconsin has NO statewide paid sick leave mandate as of 2025. The state preempted local paid-leave ordinances under 2017 Wis. Act 327 -- meaning municipalities historically could not enact their own paid-leave ordinances.  _(2017 Wis. Act 327)_

### 9.2 Milwaukee Ordinance Status

- **Milwaukee ordinance enactment and preemption narrowing** -- The 2017 preemption (Wis. Stat. § 103.10(1m)) was successfully challenged in Wisconsin courts, and a 2024 Wisconsin Supreme Court ruling (City of Milwaukee v. State, 2024 WI 47) narrowed the preemption's scope. Milwaukee enacted Milwaukee Common Council Ordinance 23-001 (the "Milwaukee Paid Sick Leave Ordinance") effective January 1, 2025.  _(Wis. Stat. § 103.10(1m); City of Milwaukee v. State, 2024 WI 47; Milwaukee Common Council Ordinance 23-001)_
- **Key features of Milwaukee ordinance** -- Applies to employers with employees performing work within the City of Milwaukee for at least 80 hours per calendar year. Accrual rate: 1 hour of paid sick leave per 30 hours worked. Annual cap: 40 hours (small employers, under 10 employees) / 72 hours (large employers, 10+ employees). Carryover: up to 40 hours unused balance carries to the next year. Permitted use: employee's own illness, family member's illness, victim of domestic violence / sexual assault, public health emergency. Notice requirement: employer must post notice at the worksite and include the policy in any employee handbook. Enforcement: Milwaukee Department of Employee Relations; penalties up to $1,000 per violation. The ordinance covers part-time and full-time employees; tipped workers; and remote workers whose work is performed at a Milwaukee address (even if the employer is elsewhere).  _(Milwaukee Common Council Ordinance 23-001)_

AUDIT FLASH POINT -- Milwaukee Local Stacking. Multiple stacking scenarios create compliance risk: 1. Employer is located in Madison (Dane County) but has a single employee working from home in Milwaukee. The employer is subject to the Milwaukee ordinance for that one employee, even though Madison has no equivalent rule. 2. Employee splits time between Milwaukee and a non-Milwaukee location. The 80-hour threshold must be tested per calendar year -- track Milwaukee hours separately. 3. The Milwaukee ordinance does NOT preempt collective bargaining agreements with equivalent or greater benefits -- but the employer must demonstrate equivalence. 4. State preemption issue is still being litigated. The Wisconsin legislature passed 2025 Wis. AB 41 attempting to re-preempt; as of November 2025 it remains in the Senate Committee on Labor. Status may change before year-end. Verify before relying on the ordinance. 5. Wisconsin employers with Milwaukee-County (but not city-of-Milwaukee) employees are NOT covered -- the ordinance is municipal, not county-wide. Other municipalities (Madison, Eau Claire) have proposed similar ordinances; none have been enacted as of November 2025. Other Wisconsin localities (Madison, Eau Claire, La Crosse) have NOT enacted paid sick leave ordinances. Outside Milwaukee, Wisconsin remains a no-mandate state for paid sick leave.

### 9.3 Recordkeeping for Milwaukee Sick Leave

- **Recordkeeping retention requirement** -- Employers subject to the ordinance must maintain for 3 years: Hours worked per employee in Milwaukee. Sick leave accrued and used per employee. Notice of policy provided to each employee. Failure to maintain records creates a presumption against the employer in any administrative complaint.  _(Milwaukee Common Council Ordinance 23-001)_

## 10. Other Wisconsin Payroll Obligations

### 10.1 Workers' Compensation

- **WC coverage requirements** -- Under Wis. Stat. § 102.04, Wisconsin requires every employer of 3 or more workers to carry workers' compensation insurance. Employers of 1 or 2 workers are covered if they paid $500 or more in any calendar quarter. Effectively, almost all Wisconsin employers must carry WC. Construction-industry employers must carry WC if they have any employees, period (no minimum threshold) -- Wis. Stat. § 102.04(1)(b)2. WC coverage is purchased from a private carrier or, for hard-to-insure employers, from the Wisconsin Compensation Rating Bureau's assigned-risk pool. Sole proprietors, partners, and corporate officers may elect coverage but are not required to be covered. Sole proprietor's spouse and dependents are exempt unless coverage is elected.  _(Wis. Stat. § 102.04; Wis. Stat. § 102.04(1)(b)2)_

### 10.2 Final Pay Timing

- **Final wages timing and penalty** -- Wis. Stat. § 109.03(2): final wages must be paid on or before the next regular payday following separation, regardless of whether the separation was voluntary or involuntary. There is no requirement to pay accrued unused vacation unless the employer's written policy or contract requires it. Penalty for late payment: increased wages under § 109.11(2) of up to 100% of the unpaid wages (i.e., double damages) if the employer's failure was willful, plus attorney's fees if the employee prevails in a § 109.03 action.  _(Wis. Stat. § 109.03(2); Wis. Stat. § 109.11(2))_

### 10.3 New Hire Reporting

- **New hire reporting requirements and penalties** -- Under Wis. Stat. § 49.22(2dm), every employer must report a new hire within 20 days of the hire date to the Wisconsin New Hire Reporting Center (operated by DWD). Required data: Employee name, address, SSN, date of hire. Employer name, address, FEIN. Submission methods: electronic via dwd.wisconsin.gov/uinh, paper W-4 facsimile, or magnetic media for high-volume employers. Penalty for failure to report: $25 per unreported employee for non-willful failures; $500 per employee for conspiracy with the employee to avoid child-support obligations (Wis. Stat. § 49.22(7)).  _(Wis. Stat. § 49.22(2dm); Wis. Stat. § 49.22(7))_

### 10.4 Minimum Wage

- **Wisconsin minimum wage** -- matches the federal floor; Wisconsin has no separate higher state minimum (figure see the "Not yet confirmed:" paragraph in Sources)  _(Wis. Stat. § 104.035)_
- **Tipped minimum wage** -- a lower tipped rate applies, with the employer making up the difference (figure see the "Not yet confirmed:" paragraph in Sources)  _(Wis. Stat. § 104.035)_
- **Local minimum wage preemption** -- Local minimum wages: Wisconsin preempts local minimum wage ordinances under Wis. Stat. § 104.001 -- so cities cannot set higher minimums. (This preemption is distinct from the paid-sick-leave preemption discussed in Section 9 and remains in effect.)  _(Wis. Stat. § 104.001)_

### 10.5 Wage Statement Requirements

- **Wage statement content and penalty** -- Each pay period the employer must provide a wage statement (paper or electronic) showing under Wis. Stat. § 109.09: Hours worked, Wages earned (regular and overtime separately), Deductions itemized. Failure to provide is a $100 per occurrence violation.  _(Wis. Stat. § 109.09)_

### 11. Worked Examples

### 11.1 Example A -- Pure Wisconsin Employer

**Facts (hypothetical worked example; all figures listed under Not yet confirmed in Sources):** Bratwurst & Sons, LLC is a Madison-based small manufacturer with 8 employees, all Wisconsin residents working solely in Madison. Annual payroll is $420,000. The company was formed in 2024 (new employer). One employee (Sarah) earns $52,000/year; another (James) earns $28,000/year.

**Wisconsin PIT withholding for Sarah (single, claims 1 allowance on WT-4):**

- Annual Wisconsin taxable wages: $52,000 − $13,560 (WT-4 standard-deduction figure -- see the "Not yet confirmed:" paragraph in Sources) − $700 (1 allowance; US-WI-dr-wis-stat-ch71.txt s. 71.05(23)) = effectively $37,740 in computational taxable income for the wage-bracket method.
- Apply brackets (US-WI-dr-wis-stat-ch71.txt, s. 71.06(1r): 3.50% to $14,680; 4.40% $14,681–$50,480):
  - 3.50% × $14,680 = $513.80
  - 4.40% × ($37,740 − $14,680) = 4.40% × $23,060 = $1,014.64
  - Subtotal annual WI PIT: $1,528.44 (worked-example arithmetic)
- Biweekly withholding (26 pay periods): $1,528.44 / 26 = **$58.79 per pay period**.

**Wisconsin UI for the company (new employer, non-construction):**

- New employer rate and wage base: apply the new-employer rate (see the "Not yet confirmed:" paragraph in Sources) to wages up to the UI taxable wage base per employee (see the "Not yet confirmed:" paragraph in Sources).
- Sarah's UI subject wages (annual): capped at the wage base; Sarah's annual UI = wage base × new-employer rate.
- James's UI subject wages (annual): capped at the wage base; James's annual UI = wage base × new-employer rate.
- Total UI for these two employees: twice the per-employee figure above.

**WT-6 filing frequency:** Based on $420,000 payroll and approximately $11,500–$13,000 expected annual Wisconsin withholding (assuming roughly 3% effective rate after deductions), the company falls in the $2,401–$20,000/year band = **monthly filer** (US-WI-Filing-Frequency-Changes.aspx.html: "Monthly $2,401 - $20,000/year"). As a new employer it starts at a starter frequency but DOR will reassign after the first full calendar year (see the "Not yet confirmed:" paragraph in Sources).

**Form WT-7 due:** January 31, 2026 with all eight W-2s attached. UI UCT-101 due quarterly.

### 11.2 Reciprocity note -- Wisconsin-IL border employee (not a numbered worked example)

A Wisconsin employer with an Illinois-resident commuter who performs 100% of services in Wisconsin applies the WI-IL reciprocity agreement: the employee files Form W-220, the employer suspends Wisconsin income tax withholding and withholds Illinois income tax instead (W-2 reports Illinois wages/withholding, no Wisconsin line), and the employee files IL-1040 with no Wisconsin return. Unemployment insurance and workers' compensation do NOT follow reciprocity: services localized in Wisconsin keep Wisconsin UI and Wisconsin workers' comp coverage. Flash point: W-220 expires each January 1 -- if not re-collected, the employer must resume Wisconsin withholding on January 1, and any over-withheld tax before a new W-220 is only refundable by the employee filing a Wisconsin nonresident return. Payroll systems that force a single 'state' field break this income-tax-state vs UI-state split. (Figures for this scenario are in the "Not yet confirmed:" paragraph in Sources.)

### 11.3 Example C -- Contractor Classification Audit

**Facts (hypothetical):** Lakefront Web Design LLC (Milwaukee-based, 4 employees on W-2) engages Maya, a freelance graphic designer in Madison, to produce 10 logos per year on a contract basis. Lakefront pays Maya $48,000/year on a 1099-NEC. Maya works from her own home studio, uses her own laptop and software, and has 5 other clients. She advertises on Instagram and a personal portfolio site. The contract specifies she is responsible for delivering each logo and reworks any client doesn't approve at no extra charge.

**Federal classification:** Maya is an independent contractor under IRS common-law (behavioral, financial, type of relationship control factors all favor contractor status). Issue 1099-NEC.

**Wisconsin UI classification -- apply the 9-factor test:**

Part A (free from control or direction): YES -- Maya sets her own hours, uses her own equipment, works from her home. ✓

Part B (need 6 of 9):

**Part B Nine-Factor Table for Maya**  _(Wis. Stat. § 108.02(12))_

| # | Factor | Maya |
| --- | --- | --- |
| 1 | Holds out to public | YES -- Instagram, portfolio site ✓ |
| 2 | Own office/equipment | YES -- home studio, own laptop ✓ |
| 3 | Multiple contracts | YES -- 5 other clients ✓ |
| 4 | Incurs main expenses | YES -- software licenses, computer, home studio ✓ |
| 5 | Responsible for satisfactory completion | YES -- contract specifies rework obligation ✓ |
| 6 | Compensation per-job, commission, or bid | YES -- hypothetical $4,800 per logo, per-job basis ✓ |
| 7 | May realize profit or suffer loss | YES -- fixed-price contracts can be unprofitable ✓ |
| 8 | Recurring business liabilities | YES -- software subscriptions, hosting, business insurance ✓ |
| 9 | Success depends on receipts vs expenditures | YES -- Maya runs a profit/loss business ✓ |

Result: 9 of 9 factors satisfied -- Maya is correctly classified as a contractor for Wisconsin UI purposes (the § 108.02(12)(bm) test text itself is not archived -- see the "Not yet confirmed:" paragraph in Sources). No UI tax due on Maya's $48,000.

**Wisconsin Workers' Compensation classification (separate 9-factor test):** Apply Wis. Stat. § 102.07(8) (test text not archived -- see the "Not yet confirmed:" paragraph in Sources). Similar analysis yields the same result -- Maya is a contractor for WC purposes. No WC coverage required.

**Wisconsin income tax withholding:** Federal common-law applies -- Maya is a contractor, so no WT-4, no withholding, no W-2. Issue 1099-NEC with Wisconsin filing through WT-7 e-file.

**Milwaukee paid sick leave:** Not applicable to contractors. Maya is excluded from the Milwaukee ordinance because she is not an "employee" performing work in Milwaukee.

**Contrast -- borderline scenario:** If Maya instead worked 40 hours/week exclusively for Lakefront, had no other clients, used Lakefront's design software accessed via Lakefront-provided credentials, and was paid hourly, she would fail Part A (control) and likely fewer than 6 Part B factors. Classification would flip to employee -- even though many such workers are wrongly issued 1099-NEC. Penalty exposure under § 108.221: up to $25,000 per misclassified worker (the archived analogue is the s. 71.64(6) "fined $25,000 for each violation" construction-contractor misclassification fine, US-WI-dr-wis-stat-ch71.txt; the § 108.221 figure and the 3-year/6-year audit-period limits see the "Not yet confirmed:" paragraph in Sources), plus back UI tax for the open audit period.

### 12. Provenance and Sources

Primary authority cited in this skill:

- **Wisconsin Statutes:**
  - Ch. 71 (Income Taxation) -- §§ 71.05, 71.06, 71.63, 71.64, 71.65, 71.82, 71.83 archived in full text (US-WI-dr-wis-stat-ch71.txt); § 71.07 cited in that text
  - Ch. 102 (Workers' Compensation) -- §§ 102.04, 102.07 (not archived; see the "Not yet confirmed:" paragraph in Sources)
  - Ch. 103 (Employment Regulations) -- § 103.10 (not archived; see the "Not yet confirmed:" paragraph in Sources)
  - Ch. 104 (Minimum Wage) -- §§ 104.001, 104.035
  - Ch. 108 (Unemployment Insurance) -- §§ 108.02, 108.18, 108.22, 108.221, 108.24 (archived US-WI-108.html is the ch. 108 table of contents only -- section text not archived)
  - Ch. 109 (Wage Payments) -- §§ 109.03, 109.09, 109.11 (not archived; see the "Not yet confirmed:" paragraph in Sources)
  - § 49.22 (New Hire Reporting) (not archived; see the "Not yet confirmed:" paragraph in Sources)

- **Wisconsin Administrative Code:**
  - Tax 2.04 (Withholding Deposit Frequency) (not archived; see the "Not yet confirmed:" paragraph in Sources)
  - Tax 2.93 (WT-4 Submission) (not archived; cross-referenced in US-WI-dr-wis-stat-ch71.txt as "See also s. Tax 2.935, Wis. adm. code")
  - DWD 110 (Unemployment Compensation E-Filing)

- **Wisconsin DOR Publications (2025):**
  - Pub 117 -- Wisconsin Withholding Tax Update (annual indexing)
  - Pub 166 -- Wisconsin Employer's Withholding Tax Guide (percentage and wage-bracket methods, supplemental rate)
  - Pub 121 -- Reciprocity (W-220 mechanics)

- **Wisconsin DWD Publications:**
  - UCB-201 -- Wisconsin Unemployment Insurance Handbook for Employers (2025 edition)
  - UCT-101 / UCT-7823 instructions

- **Reciprocal state authorities:**
  - 35 ILCS 5/302 (Illinois)
  - IND. CODE § 6-3-5-1 (Indiana)
  - KRS 141.070 (Kentucky)
  - MCL 206.256 (Michigan)

- **Recent legislation/litigation:**
  - 2023 Wis. Act 19 (biennial budget, bracket reset)
  - 2023 Wis. Act 1 (lower-bracket rate cuts)
  - 2017 Wis. Act 327 (paid-leave preemption -- partially narrowed by 2024 ruling)
  - 2009 Wis. Act 292 (misclassification penalty)
  - *City of Milwaukee v. State*, 2024 WI 47 (paid sick leave preemption narrowing)
  - 2025 Wis. AB 41 (pending re-preemption attempt, status pending as of 2025-11-15)
  - Milwaukee Common Council Ordinance 23-001 (Milwaukee Paid Sick Leave Ordinance)

- **Federal cross-references:**
  - 26 U.S.C. § 3306(j) (FUTA localization test)
  - DOL UIPL 4-95 (state-of-coverage determination)

## 13. Circular 230 Disclosures and Limitations

This skill produces draft work product for review by a Circular 230-credentialed reviewer (EA, CPA, or attorney). Outputs are NOT a substitute for credentialed advice. Specifically:

- All bracket figures, wage bases, UI rate schedules, and statutory thresholds are accurate as of the `last_updated` date in the frontmatter but may have been amended by subsequent legislation or DOR/DWD rulemaking. Verify against current DOR and DWD publications before filing.
- The Milwaukee paid sick leave ordinance is subject to ongoing litigation and legislative challenge. Confirm enforcement status as of the date of filing.
- Worker classification opinions in worked examples are hypothetical. Individual classification depends on full facts and may require IRS Form SS-8, DWD UC-160 determination request, or counsel review.
- This skill does not advise on multistate apportionment beyond the four reciprocal border states (IL, IN, KY, MI). For Minnesota-Wisconsin, Iowa-Wisconsin, or Wisconsin-out-of-state remote workforce questions outside the reciprocal framework, escalate to a multistate-tax specialist.
- Federal employment tax compliance (FICA, FUTA, federal income tax) is delegated to `us-federal-payroll` and is out of scope here.
- This skill does not address ERISA, COBRA, ACA, or fringe-benefit taxation. Those are handled by separate skills.

**Conservative defaults:** Where Wisconsin rules and federal rules diverge, this skill applies the stricter test (e.g., Wisconsin 9-factor for UI even where federal common-law would treat the worker as a contractor). Where 2025 figures are uncertain because of pending indexing, this skill uses the most recently published DOR figure and flags the uncertainty in the reviewer brief.

**Penalty exposure:** Misclassification of a single Wisconsin worker can expose the employer to up to $25,000 per worker under § 108.221, plus back UI tax for the open audit period and possible criminal referral under § 108.24 for willful violations. Where the worker count is high or the audit period extends beyond 3 years, escalate to counsel before producing final classifications.

*End of skill. Version 0.1. Awaiting verification by Wisconsin lead accountant.*

<!-- openaccountants-cta-block -->

---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
the OpenAccountants network.

- Use it in your AI: 
- Meet the accountants: 

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Rates, bands and thresholds

Not yet confirmed: figures in this section lack archived line-citations.

## The taxable base

Not yet confirmed: figures in this section lack archived line-citations.

## Deadlines and filing

Not yet confirmed: figures in this section lack archived line-citations.

## Penalties and interest

Not yet confirmed: figures in this section lack archived line-citations.

## Cross-border points

Not yet confirmed: figures in this section lack archived line-citations.

## Worked examples

Not yet confirmed: figures in this section lack archived line-citations.

## Ask the client first

Not yet confirmed: figures in this section lack archived line-citations.

## Sources

Not yet confirmed: the following figures in this skill lack an archived source and are carried here for reviewer verification -- the WT-4 worksheet standard-deduction amounts and phase-out AGIs ($13,560 single / $128,665; $25,110 MFJ / $150,840; $11,930 MFS / $71,605; $17,510 HOH); the supplemental-wage flat withholding rate (7.65%); the federal pre-TCJA $4,300 allowance comparison; the WT-4 default-withholding rule and Tax 2.93(2)/(2m) mechanics with the $50-per-certificate penalty under § 71.83(1)(b)4; the new-employer starter frequency; the next-business-day roll-over rule (§ 990.001(4)); the e-file mandate at $300 of withholding (§ 71.65(3)(d)); the "50% fraud penalty" figure; the reciprocal states' own statutes (IL 35 ILCS 5/302, IN 6-3-5-1, KRS 141.070, MCL 206.256) and the W-220 forms; the UI coverage triggers ($1,500 quarterly wages, 20 weeks, $20,000 agricultural, $1,000 domestic); the UI taxable wage base ($14,000, unchanged since 2013); the 2025 Schedule D rate grid (0.00%-12.00% by reserve ratio, small ≤$500K vs large >$500K columns, trust fund $1.2B-$1.4B); new-employer rates 3.05% non-construction / 2.90% construction; solvency tax 0.00% for 2025; the UCT-101 Apr 30 / Jul 31 / Oct 31 / Jan 31 calendar and the 25-worker e-file mandate (DWD 110.04); UI late-filing $50 minimum and 0.75%/month compounded interest; the § 108.221 / 2009 Wis. Act 292 misclassification penalty up to $25,000 per worker; the nine-factor UI test text (§ 108.02(12)(bm)) and WC test text (§ 102.07(8)); the § 71.63(2) federal common-law test reference; minimum wage $7.25 and tipped $2.33; WC coverage triggers (§ 102.04, 3+ workers / $500 quarterly); final-pay and wage-statement rules (§§ 109.03, 109.09, 109.11); new-hire reporting deadlines and penalties (§ 49.22); the Milwaukee sick-leave ordinance and its litigation status; the 2023 Wis. Act 1 attribution, the DOR late-2024 indexing announcement, and Pub 117/166/121; and the 3-year/6-year UI audit-period limits.

Archived sources now backing body figures: US-WI-dr-wis-stat-ch71.txt (s. 71.06 bracket tables; s. 71.05(23) $700/$250 exemptions; s. 71.05(2) nonresident reciprocity and s. 71.10(7)/(7e) MN/IL reciprocity machinery; ss. 71.64-71.65 withholding and deposit timing; s. 71.82 interest; s. 71.83 penalties incl. the s. 71.64(6) $25,000 misclassification fine) and US-WI-Filing-Frequency-Changes.aspx.html (withholding filing-frequency bands).

| Source | URL | Read on |
| --- | --- | --- |
| Wis. Stat. ch. 71 (full text) | archived as US-WI-dr-wis-stat-ch71.txt | 2026-11-01 |
| DOR Annual Filing Frequency Scan | archived as US-WI-Filing-Frequency-Changes.aspx.html | 2026-11-01 |
| Wis. Stat. ch. 108 (TOC only) | archived as US-WI-108.html | 2026-11-01 |
| DWD Employer Unemployment Resources | archived as US-WI-uitax.html | 2026-11-01 |

Not yet confirmed: figures in this section lack archived line-citations.

## Talk to a verified accountant

Not yet confirmed: figures in this section lack archived line-citations.
