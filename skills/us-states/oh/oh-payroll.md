---
name: oh-payroll
description: Tier 2 Ohio content skill for employer payroll compliance covering tax year 2025. Includes OH PIT withholding, IT 941 annual reconciliation with IT 501 deposits, OH SUI (wage base $9,000), the municipal income tax system collected via RITA (Regional Income Tax Agency) and CCA (Central Collection Agency) with direct-file cities like Cincinnati/Columbus/Dayton/Toledo, the work-in-municipality 20-day threshold (ORC 718.011) triggering non-resident withholding, and BWC mandatory state-fund workers' compensation.
jurisdiction: US-OH
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# OH Payroll

## Ohio Payroll -- Tier 2 Content Skill

## Who this applies to

This skill governs **Ohio employer payroll compliance for tax year 2025** for businesses with employees physically working in Ohio (resident or non-resident of Ohio), including remote workers whose home office is in an Ohio municipality. It covers:

- **Ohio Personal Income Tax (PIT) withholding** -- Form IT 4 (employee certificate), IT 501 (monthly deposit), IT 941 (quarterly/annual return), IT 3 (W-2 transmittal reconciliation)
- **Ohio State Unemployment Insurance (SUI)** -- Ohio Department of Job and Family Services (ODJFS), Form JFS-20125 quarterly contribution + wage report
- **Ohio Municipal Income Tax** -- the single most complex U.S. state-local payroll obligation, with **600+ taxing municipalities**, three collection regimes (RITA, CCA, direct-file), and the post-SB 22 (2021) **20-day work-in-municipality threshold**
- **Bureau of Workers' Compensation (BWC)** -- mandatory state-fund workers' comp (Ohio is a monopolistic state)
- **Worker classification** -- Ohio uses the 20-factor IRS common-law test plus statutory carve-outs

**Out of scope:** Ohio Commercial Activity Tax (see `oh-commercial-activity-tax.md`), Ohio personal income tax return preparation for individuals (see `oh-income-tax.md`), school district income tax (separate withholding obligation handled in a future companion skill), federal payroll (Form 941, FUTA, FICA -- federal skill), and household employees (Schedule H -- federal skill).

**Reviewer assumption:** every output of this skill must be reviewed and signed off by a credentialed payroll professional (CPP, CPA, or Ohio-registered tax preparer) before payroll is run or returns are filed.

## 2. Ohio Personal Income Tax Withholding

### 2.1 2025 brackets and the phase-down

**2025 Ohio PIT brackets**  _(HB 33 (2023); HB 96 (2025 budget bill))_

| Taxable income (OH AGI less exemptions) | 2025 marginal rate |
| --- | --- |
| $0 -- $26,050 | 0.00% (US-OH-dr-it1040-2025-booklet-ty2025.txt: "0.000% of Ohio taxable nonbusiness income") |
| $26,051 -- $100,000 | 2.75% |
| $100,001 and above | 3.125% (US-OH-dr-it1040-2025-booklet-ty2025.txt: "$2,394.32 plus 3.125% of the amount in excess of $100,000") |

- **Phase-down trajectory** -- 2023: top rate 3.99% (four brackets); 2024: top rate 3.50%, three brackets (consolidated); 2025: top rate 3.125% (US-OH-dr-it1040-2025-booklet-ty2025.txt: "For 2025, Ohio has lowered the tax rate applied to taxable nonbusiness income above $100,000 to 3.125%"); 2026: top rate 3.125% (HB 96 sets a glide path; see Not yet confirmed: in Sources); 2027 target: flat 2.75% if revenue triggers are met (see Not yet confirmed: in Sources)  _(HB 33 (2023), archived US-OH-dr-lsc-hb33-greenbook.txt; HB 96 (2025))_
- **Withholding tables method** -- The Ohio Department of Taxation publishes withholding tables under O.A.C. 5703-7-10. The 2025 tables continue to compute withholding using a simplified two-tier method approximating the 2.75% / 3.50% structure, after applying the personal exemption amounts ($2,400 / $2,150 / $1,900 tiered by federal AGI under R.C. 5747.025; amounts per US-OH-dr-it1040-2025-booklet-ty2025.txt; statute archived at US-OH-dr-orc-5747-025.txt).  _(O.A.C. 5703-7-10; R.C. 5747.025)_

### 2.2 Supplemental wage withholding

- **Supplemental wage withholding methods** -- Ohio does not publish a separate statutory supplemental rate. The Department's withholding guidelines (Employer's Withholding Tax Guide, rev. 1/2025) instruct employers to: Aggregate method -- combine supplemental wages with regular wages and withhold using normal tables, OR Flat method -- withhold at 3.5% on supplemental payments (bonuses, commissions, severance) -- this approximates the top marginal rate. Most payroll systems default to the 3.5% flat method for bonuses paid separately. This is acceptable to the Department and is the practical industry standard.  _(Ohio Department of Taxation, Employer's Withholding Tax Guide, rev. 1/2025; see Not yet confirmed: in Sources)_

**AUDIT FLASH POINT:** Some payroll providers still use legacy withholding rates. The 2025 top marginal is 3.125% (US-OH-dr-it1040-2025-booklet-ty2025.txt) -- verify your provider has updated, and confirm whether they apply a flat rate to severance (which Ohio treats as supplemental wages, not regular wages, for withholding; see Not yet confirmed: in Sources).

### 2.3 Form IT 4 -- Employee's Withholding Exemption Certificate

- **Form IT 4 contents** -- Every Ohio employee must file Form IT 4 (the state W-4 equivalent) on hire and any time their exemption status changes. IT 4 captures: Personal exemptions claimed (line 1); Dependent exemptions (line 2); Residence school district number (line 4) -- this is the trigger for school district income tax withholding if the district has an income tax; Resident municipality (line 5) -- used to determine the "courtesy withholding" obligation; Additional Ohio withholding requested (line 6)
- **Default withholding if no IT 4 filed** -- If an employee fails to file IT 4, the employer must withhold as if zero exemptions are claimed and the employee is single.  _(R.C. 5747.06(A))_
- **IT 4 retention** -- IT 4 must be retained by the employer for at least 4 years. It is not filed with the Department, but is producible on audit.

### 2.4 Deposit frequency -- IT 501 vs. IT 941 quarterly

**Deposit frequency table**  _(O.A.C. 5703-7-04)_

| Prior 12-month OH withholding | Frequency | Form | Due date |
| --- | --- | --- | --- |
| Look-back $2,000 or less | Quarterly | IT 501 (quarterly return) | Last day of month after quarter end (US-OH-dr-wh-guidelines-2026.txt: "look-back period is $2,000 or less. The IT 501 and payment are due by the last day of the month following the end of each calendar quarter") |
| $2,000 – $84,000 | Monthly | IT 501 | 15th of month after month end (US-OH-dr-wh-guidelines-2026.txt: "greater than $2,000 but less than $84,000. The IT 501 and payment are due within 15 days following the end of each month") |
| $84,000 or more | Partial-weekly | IT 501 + EFT | EFT within three banking days from the end of each partial-week period (US-OH-dr-wh-guidelines-2026.txt: "$84,000 or more. The payments must be made by electronic funds transfer (EFT) within three banking days") |

- **Annual return** -- Annual return: IT 941 is the annual reconciliation filed by January 31 following the calendar year (US-OH-dr-wh-guidelines-2026.txt: "Employers are required to file by January 31st of the following tax year"). The IT 3 transmittal accompanies the W-2 copies (US-OH-dr-wh-guidelines-2026.txt: W-2/1099 information due "by the due date of January 31st"; the OH|TAX Upload Statement "creates an IT 3 from the W-2/1099 information submitted").
- **Quarterly filer treatment** -- Quarterly filers (look-back $2,000 or less) remit with the quarterly IT 501; the IT 941 is the separate annual reconciliation (US-OH-dr-wh-guidelines-2026.txt: "The IT 501 and payment are due by the last day of the month following the end of each calendar quarter").
- **E-file mandate** -- Employers are required to electronically file and pay Ohio withholding taxes through OH|TAX eServices (the archived Employer's Withholding Tax Guide states the requirement for employers generally, not only above $84,000/250 W-2s -- see Not yet confirmed: in Sources).  _(O.A.C. 5703-7-19; US-OH-dr-wh-guidelines-2026.txt: "Employers are required to electronically file and pay Ohio employer and school district withholding taxes")_

### 2.5 Penalties

- **Late filing penalty** -- greater of $50/month or 5% of tax due per month, capped at 50% of tax  _(R.C. 5747.15)_
- **Late deposit penalty** -- 50% of underpayment -- Ohio is unusually harsh here; the federal trust fund recovery analog is 100% but is only assessed against responsible persons. Ohio's 50% is automatic on the entity.  _(R.C. 5747.071)_
- **Failure to file IT 3 / W-2s penalty** -- $50 per W-2 not transmitted, capped at $25,000.

**AUDIT FLASH POINT:** Ohio's 50% late-deposit penalty is automatic and assessed even if the tax is paid one day late. Set deposit reminders. Abatement requires a written showing of reasonable cause, and the Department's abatement rate is low.

## 3. Ohio State Unemployment Insurance (SUI)

### 3.1 Wage base and rates

- **Taxable wage base 2025** -- $9,000 USD per employee per year (US-OH-dr-odjfs-2025-rates.txt: "Taxable Wage Base $9,000"; US-OH-dr-orc-4141-01(G): wages exclude remuneration "in excess of nine thousand dollars on and after January 1, 2020"); 2026 base also $9,000 (US-OH-dr-odjfs-2026-rates.txt: "Base $9,000")
- **SUI rate range 2025** -- experience/MSL rates 0.3% – 10.1% across rate classes 1-40, plus surcharge and fees (US-OH-dr-odjfs-2025-rates.txt rate-class table)
- **New employer rate -- non-construction** -- 2.70%  _(US-OH-dr-odjfs-2025-rates.txt: "NB Rate 2.7%"; US-OH-dr-nfib-uc-handbook-2025.txt: "New Employer Rate (except Construction Industry): 2.7%")_
- **New employer rate -- construction** -- 5.60% for 2025, 5.70% for 2026  _(US-OH-dr-odjfs-2025-rates.txt: "NB Construction Rate 5.6%"; US-OH-dr-odjfs-2026-rates.txt: "NB Construction Rate 5.7%")_
- **Mutualized account rate add-on 2025** -- 0.0% (the trust fund is solvent; the mutualized add-on was zeroed out in late 2024 by the Unemployment Compensation Advisory Council) (US-OH-dr-odjfs-2025-rates.txt and US-OH-dr-odjfs-2026-rates.txt: Mutual Rate 0.0% for all rate classes)

### 3.2 Reporting and payment

- **SUI reporting mechanism** -- SUI is reported via Form JFS-20125 (Quarterly Contribution and Wage Report) through ODJFS's ERIC (Employer Resource Information Center) portal.

**SUI quarterly due dates**

| Quarter | Due date |
| --- | --- |
| Q1 (Jan-Mar) | April 30 (US-OH-dr-orc-4141-20.txt: "the quarterly report shall be filed not later than the last day of the first month following the close of the calendar quarter") |
| Q2 (Apr-Jun) | July 31 |
| Q3 (Jul-Sep) | October 31 |
| Q4 (Oct-Dec) | January 31 (US-OH-dr-orc-4141-20.txt: same last-day-of-following-month rule) |

- **SUTA dumping prohibition** -- SUTA dumping (transferring employees to a lower-rated entity) is prohibited with criminal penalties and rate reassignment going back to the date of transfer.  _(R.C. 4141.244)_

### 3.3 Coverage

- **Coverage thresholds** -- see Not yet confirmed: in Sources.
- **Agricultural employer coverage threshold** -- see Not yet confirmed: in Sources.
- **Nonprofit reimbursement election** -- Nonprofit 501(c)(3) employers with 4+ employees may elect reimbursement instead of contributions -- they pay back the trust fund dollar-for-dollar for actual UI claims paid to former employees.  _(R.C. 4141.241)_

## 4. Municipal Income Tax -- The Painful Center of Ohio Payroll

Ohio is the only U.S. state where municipal income tax is the dominant local payroll complexity. There are 600+ taxing municipalities (cities and villages), each with its own: Rate (range 1.00% – 3.00%, most cluster between 2.0% and 2.5%; see Not yet confirmed: in Sources); Credit for taxes paid to other municipalities (range 0% to 100% of the resident rate); Filing forms (though three centralized agencies handle most of them); Definition of "taxable income" (largely conformed by HB 5 (2014) but not entirely). Ohio Revised Code Chapter 718 governs the uniform municipal income tax framework (archived US-OH-dr-orc-718-011.txt). HB 5 (2014) imposed uniform definitions and the 20-day rule. SB 22 (2021) rewrote the 20-day rule to the form discussed below.

### 4.1 The three collection regimes

#### 4.1.1 RITA -- Regional Income Tax Agency

- **RITA overview** -- Collects for ~330 Ohio municipalities (the largest network; see Not yet confirmed: in Sources). Members include most Cleveland-area suburbs (excluding Cleveland itself), Akron-area, much of Dayton suburban ring, Toledo suburbs, and many central-Ohio villages. Single combined return: Form 11 / Form 17 for individual; Form 27 (employer year-end withholding reconciliation); Form 11A or online portal for monthly/quarterly remittance. Withholding remittance frequency: monthly if prior-quarter withholding exceeded $2,399; quarterly otherwise (the parallel CCA rule is archived: "Employers must remit monthly if withholding in the previous calendar year exceeded $2,399 or if the amount required to be withheld during any month of the previous calendar quarter exceeded $200" -- US-OH-dr-cca-faq-business.txt; see Not yet confirmed: in Sources for the RITA-specific threshold). Annual reconciliation Form 11 due by February 28 following the tax year (see Not yet confirmed: in Sources).

RITA members are searchable at ritaohio.com. The employer is responsible for verifying every workplace and resident municipality against the current member list -- RITA's coverage changes (cities occasionally leave or join).

#### 4.1.2 CCA -- Central Collection Agency (Division of Taxation, City of Cleveland)

- **CCA overview** -- Collects for ~50 Ohio municipalities (see Not yet confirmed: in Sources), including Cleveland and Akron (both in US-OH-dr-cca-members.txt), Parma Heights (rate 3.00% in US-OH-dr-cca-rates.txt), and others (note: Akron historically self-administered; recent membership changes apply -- confirm against current CCA member roster). Form CCA-W3 is the annual withholding reconciliation. Monthly remittance if withholding exceeds $200 per month ("Employers which withhold more than $200.00 per month must file monthly"; monthly filings "due by the 15th day of the month following the end of the withholding period" -- US-OH-dr-cca-102.txt). The Annual Reconciliation (W-3) and W-2s are due on the last day of February (US-OH-dr-cca-faq-business.txt). CCA is operated by the City of Cleveland Division of Taxation -- its rules can deviate slightly from RITA's, particularly around courtesy withholding for residents.

#### 4.1.3 Direct-file cities

- **Direct-file cities list** -- These cities administer their own income tax and do not use RITA or CCA: Columbus (Division of Income Tax); Cincinnati (Income Tax Division); Dayton (Division of Tax & Accounting Administration); Toledo (Division of Taxation); Lakewood (a notable Cleveland-area exception); Several smaller villages. Each direct-file city has its own forms, portals, and deposit schedules. Columbus uses Form IT-11 for employer reconciliation; Cincinnati uses Form W-3; Dayton uses Form D-W3; Toledo uses Form W-3.

**AUDIT FLASH POINT:** Misrouting withholding (sending Cleveland-resident withholding to RITA instead of CCA, or sending Columbus withholding to RITA) is a high-frequency error. RITA and CCA generally do not forward misrouted funds -- the employer must reclaim from the wrong agency and re-remit to the correct one, while penalties accrue at the correct municipality. Always validate routing using the official municipality lookup tools each year.

### 4.2 The withholding rule -- workplace municipality

- **Workplace withholding determination steps** -- For each pay period, the employer must: 1. Determine where the employee physically performed services (the "principal place of work" by day count for that pay period) 2. Withhold at the workplace municipality's resident/non-resident rate on wages earned while physically in that municipality 3. If the workplace municipality is different from the employee's resident municipality, courtesy withholding to the resident municipality is optional but common (and frequently required by collective bargaining agreements or municipal ordinance for resident-rate employers). Wages earned outside any taxing municipality (e.g., at a worksite in an unincorporated township, or in another state) are not subject to Ohio municipal withholding, but may still be subject to OH state withholding.

### 4.3 The 20-day work-in-municipality threshold (post-SB 22)

- **20-day rule** -- An employer is not required to withhold municipal income tax on qualifying wages for services performed in a municipal corporation "on twenty or fewer days in a calendar year" unless an exception applies (principal place of work, worksite, resident request, athlete/entertainer). Once the threshold is exceeded, the employer must withhold and remit "for any subsequent days in that calendar year"; the employer MAY elect to also withhold for the first twenty days, in which case the principal-place-of-work tax paid for those days is refundable to the employee.  _(R.C. 718.011(B)(1), (D)(1)-(2), archived US-OH-dr-orc-718-011.txt)_
- **Key mechanics** -- "Day" = any portion of a day spent performing services in the municipality (a part-day counts as a full day); Counted by calendar year, resetting each January 1; Small employer exception: employers with prior-year total revenue under $500,000 are exempt from the 20-day non-resident withholding obligation entirely -- they withhold only for the principal place of work; Trigger is retroactive: once day 21 hits, withholding is owed on days 1–20 as well, requiring a catch-up remittance (and possibly amended W-2 municipal lines if year-end is approaching); Telework cleanup: SB 22 also rolled back the pandemic-era H.B. 197 §29 fiction that treated remote work as occurring at the principal place of work. From 2022 forward, remote-work days are sourced to the employee's actual physical location, which for most home-office employees is their resident municipality.  _(R.C. 718.011(A)(1); R.C. 718.011(D))_

#### Worked example (hypothetical scenario; figures listed under Not yet confirmed in Sources)

> A Cleveland-resident employee normally works at the employer's Independence office (RITA member, 2.0% -- US-OH-dr-rita-rates.txt: "Independence | 390 | 2.000%"). On August 15, the employee starts a 60-day project at the customer site in Westlake (RITA member, 1.5% -- US-OH-dr-rita-rates.txt: "Westlake | 840 | 1.500%"). The employee works in Westlake Monday–Thursday and returns to Independence Friday.
>
> Through October 14 (Day 21 of Westlake work), the employer was withholding only for Independence. On October 14, the employer must (US-OH-dr-orc-718-011.txt (D)(1)):
> 1. Begin withholding for Westlake at 1.5% on Westlake-day wages for subsequent days
> 2. Optionally elect to withhold for the first twenty Westlake days, in which case the Independence tax paid for those days is refundable to the employee (US-OH-dr-orc-718-011.txt (D)(2)-(3))
> 3. Refund or credit back to the employee (or to Independence withholding) the Independence withholding that was over-collected on those 20 Westlake days, only if the employer had been withholding the Independence rate on Westlake-day wages (which it was, under the under-20-day default)
> 4. Issue W-2 Box 18/19/20 lines reflecting both Independence and Westlake correctly at year end

**AUDIT FLASH POINT:** Missed 20-day catch-up withholding is the single most common Ohio municipal payroll audit finding. Employers with project-based remote-employee deployments (consultants, engineers, sales reps, IT installers) must maintain a day-by-day workplace log per employee per municipality and have a triggering report that fires at day 21. Many payroll providers do not natively support this -- it requires manual oversight.

### 4.4 Resident municipality "courtesy" withholding

- **Courtesy withholding mechanics** -- When an employee works in Municipality A but resides in Municipality B: Municipality A withholding is mandatory at A's non-resident rate (subject to the 20-day rule); Municipality B withholding is optional courtesy withholding -- most large employers do it as a service to the employee; If Municipality B is provided a credit for tax paid to Municipality A, B's withholding obligation may be zero or partial (computed at B's resident rate less the credit allowed). The credit percentage varies dramatically: Cleveland Heights grants a 50% credit factor (US-OH-dr-rita-rates.txt: "Cleveland Heights | 210 | 2.250% | 50.000% | 1.000%"), Brecksville and Independence grant 100% (same table), East Cleveland grants 0% (same table); Cincinnati's credit policy (see Not yet confirmed: in Sources).

The employee's IT 4 (line 5 residence municipality) plus the employer's own knowledge of the workplace municipality drives the courtesy withholding determination. Best practice: collect a separate employer-internal "municipal residency certification" at hire, distinct from IT 4, capturing the precise street address (RITA/CCA/direct-file city lookup tools resolve by address, not ZIP).

### 4.5 Multi-municipality remote workers

The post-2022 remote-work environment has produced a new high-audit-risk pattern: the employee who works partially at home (resident municipality), partially at the employer's office (workplace municipality), and partially at customer sites (third municipalities).

- **Allocation rule** -- Withholding must be allocated to each municipality based on actual days worked there, with the 20-day non-resident threshold applied separately to each non-principal-place-of-work municipality.

> Employee resides in Dublin (direct-file with Columbus suburbs -- Dublin is actually a separate direct-file city, 2.0% -- US-OH-dr-dublin-income.txt: "The local income tax rate is 2.0%"). The employer's office is in Columbus (direct-file, 2.5% -- US-OH-dr-columbus-ir25-instructions.txt: "2.5%"). The employee works 3 days per week at home in Dublin, 2 days per week at the Columbus office.
>
> - **Dublin** is the employee's resident municipality and (for telework days) the workplace. The 20-day rule does not protect the employer here because Dublin is exceeded almost immediately (3 days/week × any number of weeks > 20 days quickly). The employer must withhold for Dublin on the telework-day wages at Dublin's rate. Because Dublin is also the resident municipality, no credit issue arises.
> - **Columbus** is the workplace for in-office days. The employer must withhold for Columbus on those days at Columbus's non-resident rate (2.5% -- US-OH-dr-columbus-ir25-instructions.txt). Columbus's credit treatment for tax paid to other municipalities (see Not yet confirmed: in Sources); the employer's allocation is based on actual days, so no credit-side issue arises at the employer level.
> - Both withholdings go to direct-file cities (Dublin and Columbus). The employer files separate withholding returns with each.
>
> **W-2 reporting:** Box 18 (local wages) and Box 19 (local tax) appear **twice** -- one line for Dublin, one for Columbus. Box 20 holds the municipality name. The state tax (Boxes 15-17) is reported once for Ohio.

**AUDIT FLASH POINT:** Misallocated remote work is the second-most-common Ohio municipal audit finding (after missed 20-day triggers). Employers must require employees to attest to their work location and maintain logs. The Ohio Tax Department and many municipalities have indicated they will rely on employer records first; absence of records leads to assessment at the workplace municipality rate for all wages (worst-case outcome).

### 4.6 W-2 reporting to municipalities

- **W-2 municipal transmittal** -- Every Ohio W-2 with municipal withholding must be transmitted to each municipality (or to RITA/CCA on its behalf) by the federal W-2 due date (January 31) (see Not yet confirmed: in Sources; CCA's own rule: "The Annual Reconciliation (W-3) and W-2s are due on the last day of the February" -- US-OH-dr-cca-faq-business.txt). The transmittal is: RITA: Form 17, submitted electronically through RITA's eFiling portal; CCA: Form CCA-W3, submitted via the CCA portal; Direct-file cities: each city's annual reconciliation form (Columbus IT-13, Cincinnati W-2, etc.)
- **E-file mandate for municipal W-2s** -- RITA, CCA, Columbus, Cincinnati, Dayton, and Toledo all require electronic W-2 transmittal for any employer issuing 10+ municipally-taxable W-2s (some thresholds vary).

## 5. Bureau of Workers' Compensation (BWC)

### 5.1 Monopolistic state -- no private market

- **Monopolistic state status** -- Ohio is one of four monopolistic states (along with North Dakota, Washington, Wyoming) where workers' compensation insurance must be purchased through the state-run BWC fund. Private workers' comp insurance is not available for the primary policy.
- **Self-insurance exception** -- The administrator may grant self-insuring status to employers "of sufficient financial ability to render certain the payment of compensation"; factors include at least two years operating in Ohio, sufficiency of Ohio assets, and CPA-certified financial records, and a surety bond is required. The "$5M+ net assets" rule of thumb (see Not yet confirmed: in Sources).  _(R.C. 4123.35(B), archived US-OH-dr-orc-4123-35.txt)_
- **Federal program exclusions** -- Federal employees, railroad workers, and longshoremen are covered by federal programs, not BWC.

### 5.2 Coverage requirement

- **BWC coverage requirement** -- Every Ohio employer with at least one employee (full-time, part-time, or seasonal) must have BWC coverage. Independent contractors are not covered unless the employer elects to cover them.

### 5.3 Premium computation

- **BWC premium formula** -- BWC premium = (manual rate per $100 of payroll) × (payroll subject to BWC) × (experience modifier) × (any program discounts).
- **Manual classifications** -- BWC uses NCCI-style class codes (e.g., 8810 clerical, 5403 carpentry) with Ohio-specific rates
- **Maximum reportable wage per employee, policy year 2024-2025** -- $35,800 (policy year July 1, 2024 – June 30, 2025)
- **Maximum reportable wage per employee, policy year 2025-2026** -- $38,300 (policy year July 1, 2025 – June 30, 2026)
- **Minimum premium** -- $120 per policy year per employer (see Not yet confirmed: in Sources)

### 5.4 Reporting

- **True-up report due date** -- True-up report: due August 15 following the policy-year end (June 30). Reports actual payroll for the prior policy year. Failure to file true-up triggers loss of all program discounts and a non-compliance flag.
- **Installment payments** -- BWC requires monthly, bi-monthly, quarterly, semi-annual, or annual installments based on premium size. Default is bi-monthly for new employers.

### 5.5 Penalties

- **Failure to maintain coverage penalty** -- BWC can assess back premium plus interest plus a penalty, and an employer without coverage loses statutory immunity from employee injury lawsuits  _(R.C. 4123.74, archived US-OH-dr-orc-4123-74.txt; the 100% penalty figure -- see Not yet confirmed: in Sources)_
- **Late true-up penalty** -- forfeiture of discounts averaging 4-15% of annual premium

## 6. Worker Classification

- **20-factor common-law test adoption** -- Ohio R.C. 4141.01 and R.C. 4123.01(A)(1) use common-law employee/contractor distinctions (archived US-OH-dr-orc-4141-01.txt; US-OH-dr-orc-4123-01.txt); the specific adoption of the 20-factor IRS test (Rev. Rul. 87-41) and its three categories (see Not yet confirmed: in Sources).  _(R.C. 4141.01; R.C. 4123.01(A)(1); IRS Rev. Rul. 87-41)_
- **Behavioral control factors (1-11)** -- 1. Instructions -- employer's right to direct how, when, where work is done 2. Training -- employer-provided training suggests employee 3. Integration -- services integrated into business operations 4. Services rendered personally -- must the worker do the work themselves? 5. Hiring assistants -- does the worker hire and pay helpers? 6. Continuing relationship -- recurring engagement suggests employee 7. Set hours of work -- fixed hours suggest employee 8. Full-time required -- full-time exclusivity suggests employee 9. Doing work on employer's premises 10. Order or sequence set -- employer directing sequence suggests employee 11. Reports -- required oral or written reports suggest employee  _(IRS Rev. Rul. 87-41)_
- **Financial control factors (12-15)** -- 12. Payment by hour, week, or month (vs. by job) -- periodic pay suggests employee 13. Payment of business and travel expenses -- reimbursement suggests employee 14. Furnishing tools and materials -- employer-furnished suggests employee 15. Significant investment -- worker's substantial investment in own equipment suggests contractor  _(IRS Rev. Rul. 87-41)_
- **Relationship of the parties factors (16-20)** -- 16. Realization of profit or loss -- bearing financial risk suggests contractor 17. Working for more than one firm at a time 18. Making services available to general public 19. Right to discharge -- at-will termination suggests employee 20. Right to terminate -- worker's right to walk away without breach suggests contractor  _(IRS Rev. Rul. 87-41)_
- **Ohio-specific statutory presumptions** -- Construction industry: a person performing labor under a construction contract is an employee "if at least ten of the following criteria apply" (instructions, training, integration, personal performance, supervision, continuing relationship, set hours, full time, on-premises, order of work -- US-OH-dr-orc-4123-01.txt (A)(1)(c)). Real estate agents and direct sellers (see Not yet confirmed: in Sources).  _(R.C. 4123.01(A)(1)(c); IRC §3508)_

**AUDIT FLASH POINT:** Ohio BWC audits independent contractor relationships aggressively, particularly in construction, delivery, and gig economy contexts. A reclassification finding triggers:
1. Retroactive BWC premium for all reclassified workers (4-6 years lookback)
2. Retroactive SUI contributions (subject to ODJFS's 3-year SOL)
3. Retroactive OH withholding under R.C. 5747.06
4. Loss of statutory employer immunity from injury suits for those workers
5. Potential 1099-to-W-2 reclassification at the IRS level (which often follows once ODJFS reports)

## 7. Healthy Families and Workplaces Act -- Status

- **Paid sick leave status in Ohio** -- The Ohio "Healthy Families and Workplaces Act" (variously proposed in HB 22, HB 230, and recurring iterations) would mandate employer-provided paid sick leave. As of November 2025, no version has been enacted into law. Ohio currently has no state-mandated paid sick leave. Some Ohio cities (notably Columbus, which considered but did not pass a 2024 ordinance) have proposed local paid leave; none has been enacted as of 2025. The state preemption statute prohibits local minimum-wage and benefits mandates from being inconsistent with state law, which has chilled municipal action.  _(R.C. 4113.85, archived US-OH-dr-orc-4113-85.txt)_
- **Mandatory leave categories** -- Employers are not required to provide paid sick leave by Ohio law. Federal FMLA (50+ employees) and federal CARES/FFCRA leave (expired) are the only mandatory leave categories for most Ohio employers.

## 8. IT 3 Annual Reconciliation and W-2 Transmittal

- **Form IT 3 contents and due date** -- Form IT 3 is Ohio's W-2 transmittal form, due January 31 following the calendar year (US-OH-dr-wh-guidelines-2026.txt: W-2/1099 information due "by the due date of January 31st"; OH|TAX upload "creates an IT 3 from the W-2/1099 information submitted"), accompanying the W-2 copies. IT 3 reports: Total Ohio wages paid; Total Ohio income tax withheld; Total Ohio school district income tax withheld; Count of W-2s issued (reported items -- see Not yet confirmed: in Sources).
- **E-filing requirement for IT 3** -- the archived Employer's Withholding Tax Guide requires electronic filing and payment for employers generally (US-OH-dr-wh-guidelines-2026.txt); the 250+ W-2 / $84,000 thresholds (see Not yet confirmed: in Sources).
- **W-2 box requirements** -- The W-2 must include: Box 15: OH; Box 16: Ohio wages (generally matches federal Box 1, subject to limited Ohio-specific add-backs/subtractions); Box 17: Ohio income tax withheld; Box 18, 19, 20: each municipality with withholding (multiple lines if multi-municipality); Box 19 must also include any school district income tax withholding, with Box 20 showing the 4-digit district number (this is a parallel system to municipal -- out of scope for this skill).

### 9. Worked Examples

### Example 1: Cleveland employer with RITA suburbs

**Facts:** ABC Manufacturing, Inc. has its office in **Independence, Ohio** (RITA member, workplace rate 2.0%). It has 40 employees, all working at the Independence office. Employees live across multiple cities: Cleveland (CCA, resident rate 2.5%, 100% credit for tax paid elsewhere -- US-OH-dr-cca-rates.txt), Parma (CCA, 2.5%, 100% credit -- Parma Heights 3.00% in US-OH-dr-cca-rates.txt; Parma city rate see Not yet confirmed: in Sources), Brecksville (RITA, 2.0%, 100% credit -- US-OH-dr-rita-rate-table.txt: "Brecksville | 130 | 2.000% | 100.000%"), Independence (RITA, 2.0% -- same as workplace, no credit issue; US-OH-dr-rita-rates.txt), Lakewood (direct-file, 1.5%, 100% credit; see Not yet confirmed: in Sources).

**Withholding strategy:**

1. **Workplace withholding (mandatory):** all 40 employees, withhold Independence 2.0% non-resident rate on 100% of wages (US-OH-dr-rita-rates.txt: "Independence | 390 | 2.000%") → remit to **RITA** monthly via **RITA Form 11** (the archived 2026 Form 11 instructions, US-OH-dr-rita-form11.txt, describe eFiling Form 11 withholding returns through ritaohio.com).

2. **Courtesy withholding (resident-side) -- optional but recommended:**
   - **Cleveland residents** (3 employees): Cleveland resident rate is 2.5%, credit 100% up to resident rate. Since Independence rate (2.0%) < Cleveland rate (2.5%), Cleveland residents owe Cleveland an additional 0.5% on Independence-earned wages. Many employers withhold this 0.5% as courtesy. **Routes to CCA** (Cleveland is a CCA member -- US-OH-dr-cca-members.txt).
   - **Parma residents** (2 employees): same analysis -- Parma 2.5%, credit 100%, owe 0.5%. **Routes to CCA** (Parma Heights rate 3.00% in US-OH-dr-cca-rates.txt; Parma city rate see Not yet confirmed: in Sources).
   - **Brecksville residents** (5 employees): Brecksville 2.0%, credit 100% (US-OH-dr-rita-rate-table.txt: "Brecksville | 130 | 2.000% | 100.000%"), owe 0%. No courtesy needed.
   - **Independence residents** (12 employees): workplace = residence, single withholding only.
   - **Lakewood residents** (3 employees): Lakewood 1.5% (see Not yet confirmed: in Sources), credit 100% on 1.5% of Independence wage, owe 0% (Lakewood rate ≤ Independence rate). No courtesy needed.

3. **Quarterly filings:**
   - **RITA Form 11** annual + monthly remittances for all Independence withholding + Brecksville-courtesy (zero) + Lakewood (zero)
   - **CCA Form CCA-117** monthly for Cleveland and Parma courtesy 0.5% (CCA monthly filing rule archived in US-OH-dr-cca-102.txt; the CCA-117 form number -- see Not yet confirmed: in Sources)
   - **Note:** Even though Independence is RITA, the Cleveland and Parma courtesy withholding must be remitted to **CCA**, not RITA, because Cleveland and Parma are CCA members.

4. **Year-end W-2 boxes** for a Cleveland-resident employee:
   - Box 18: Independence wages, Box 19: Independence tax, Box 20: "INDEPENDENCE"
   - Box 18: Cleveland wages, Box 19: Cleveland courtesy tax (0.5%), Box 20: "CLEVELAND" (W-2 box usage -- see Not yet confirmed: in Sources; per IRS Form W-2 instructions the standard layout is Box 18 = locality name, Box 19 = local wages, Box 20 = local income tax)

5. **IT 3 / IT 941** reconciliation: filed with Ohio Department of Taxation for the state-level withholding (top rate 3.125% for 2025 -- US-OH-dr-it1040-2025-booklet-ty2025.txt), separate from the municipal filings.

**AUDIT FLASH POINT:** A common error is to send the Cleveland courtesy withholding to RITA (because the employer is "primarily a RITA filer"). RITA will accept the funds and book them to Cleveland... wait, no -- RITA does not collect for Cleveland (Cleveland is CCA). RITA will reject or hold the funds, and Cleveland's claim against the employer accrues penalties. **Always route by destination municipality, not by employer's primary agency.**

### Example 2: Columbus direct-file employer

**Facts:** XYZ Tech LLC has its office in **Columbus, Ohio** (direct-file, 2.5%). It has 25 employees, all working at the Columbus office. Employees live in Columbus (15), Dublin (4, direct-file, 2.0%, 100% credit up to 2.0% for tax paid to the workplace municipality -- US-OH-dr-dublin-income.txt), Worthington (3, RITA, 2.5%, 100% credit -- US-OH-dr-rita-rate-table.txt), Westerville (2, RITA, 2.0%, 100% credit; Westerville rate see Not yet confirmed: in Sources), and Bexley (1, direct-file, 2.5%, 65% credit factor -- US-OH-dr-rita-rate-table.txt: "Bexley | 104 | 2.500% | 65.000%").

**Withholding strategy:**

1. **Workplace withholding (mandatory):** all 25 employees, withhold Columbus 2.5% non-resident rate on 100% of wages (US-OH-dr-columbus-ir25-instructions.txt: "2.5%") → remit to **City of Columbus Division of Income Tax** monthly via Columbus's CRISP portal (crisp.columbus.gov -- US-OH-dr-columbus-ir25-instructions.txt). Use Columbus's own monthly deposit form.

2. **Courtesy withholding:**
   - **Columbus residents** (15): workplace = residence, single withholding only.
   - **Dublin residents** (4): Dublin 2.0% with a 100% credit up to 2.0% for taxes withheld or paid to the workplace municipality (US-OH-dr-dublin-income.txt: "The City of Dublin provides 100% credit up to 2.0% for taxes withheld or paid to the workplace municipality"). Columbus 2.5% > Dublin 2.0%, so the Dublin credit fully offsets -- owe 0%. Courtesy withholding to Dublin is optional. **Routes to City of Dublin** (direct-file).
   - **Worthington residents** (3): 2.5%, 100% credit (US-OH-dr-rita-rate-table.txt). Columbus 2.5% credit covers full Worthington 2.5%. Owe 0%. No courtesy.
   - **Westerville residents** (2): 2.0%, 100% credit (rate see Not yet confirmed: in Sources). Columbus 2.5% > Westerville 2.0%, so Westerville credit fully offsets. Owe 0%. No courtesy.
   - **Bexley residents** (1): 2.5% with a 65% credit factor (US-OH-dr-rita-rate-table.txt: "Bexley | 104 | 2.500% | 65.000%"). The Columbus credit offsets only 65% of Bexley tax, so the employee owes roughly 0.875% to Bexley at filing. Courtesy withholding may be appropriate.

3. **Filings:**
   - **Columbus IT-11** annual reconciliation + monthly remittances
   - **Dublin Form IT-13** annual + monthly remittances for the Dublin courtesy
   - **No RITA filings** (Worthington and Westerville withholdings are zero; nothing to remit, but employer must still register if it ever has courtesy withholding to those cities)

4. **Annotation for the Dublin case:** Dublin grants a 100% credit up to 2.0% for workplace-municipality tax (US-OH-dr-dublin-income.txt), so Dublin residents working in Columbus owe no additional Dublin tax -- the earlier draft's "no credit" assumption was wrong. Employees should still register/file with Dublin (all Dublin residents 18+ must file regardless of where income is earned -- US-OH-dr-dublin-income.txt).

**AUDIT FLASH POINT:** Credit policies vary by city and by credit factor -- e.g., Bexley applies only a 65% credit factor (US-OH-dr-rita-rate-table.txt) and East Cleveland 0% (same table). The no- or low-credit cities must be tracked individually (Cincinnati's policy -- see Not yet confirmed: in Sources). **Always look up credit policy by destination, never assume.**

### Example 3: Multi-municipality remote worker triggering 20-day rule

**Facts:** Delta Consulting LLC has its office in **Akron** (CCA member -- US-OH-dr-cca-members.txt; workplace rate 2.5% -- US-OH-dr-akron-indiv-filers.txt; prior-year revenue $3.2M so the small-employer exception -- "total revenue of less than five hundred thousand dollars during the preceding taxable year", R.C. 718.01(TT), US-OH-dr-orc-718-01.txt -- does NOT apply). Sarah is a consultant who lives in **Hudson** (RITA, resident rate 2.0%, 100% credit -- US-OH-dr-rita-rate-table.txt: "Hudson\t378\t2.000%\t100.000%"). Sarah's pattern in 2025:

- Jan 1 – Jun 30: works 4 days/week at the Akron office, 1 day/week telework from Hudson (26 weeks × 1 day = 26 Hudson telework days; well above 20)
- Jul 1 – Aug 31: works 3 days/week at a customer site in **Beachwood** (RITA, 2.0%) and 2 days/week at Akron. Total Beachwood days through Aug 31: ~26 days (above 20)
- Sep 1 – Dec 31: returns to Akron full-time (5 days/week)

**Withholding analysis:**

**Hudson (resident municipality, also telework workplace):**
- The 1-day-per-week telework allocates 26 days to Hudson for the first half of the year, exceeding the 20-day threshold by approximately Day 21 (~late May). HOWEVER, Hudson is Sarah's resident municipality, and the 20-day rule under R.C. 718.011 only protects against non-resident municipal withholding. Because Hudson is Sarah's residence, the resident-municipality rules apply, and Hudson-rate withholding on Hudson telework days is appropriate from Day 1 (subject to credit for Akron tax withheld on Akron days).
- Practical result: employer should set up resident courtesy withholding for Hudson from Day 1, with Hudson credit for Akron tax = full 2.0% Hudson rate (because Akron's 2.5% withheld exceeds Hudson's 2.0% rate). Net Hudson withholding owed on Akron-day wages = 0. Net Hudson withholding owed on Hudson telework-day wages = 2.0% (no credit because no other municipality is taxing those wages). (Hudson rate/credit per US-OH-dr-rita-rate-table.txt: "Hudson | 378 | 2.000% | 100.000%")
- **Route:** Hudson is a RITA member → remit to RITA.

**Akron (workplace municipality, principal place of work):**
- Akron is the principal place of work. Withhold 2.5% on all Akron-day wages from Day 1 (US-OH-dr-akron-indiv-filers.txt) → remit to CCA (Akron appears in US-OH-dr-cca-members.txt).
- No 20-day issue (principal place of work is always subject to withholding from Day 1).

**Beachwood (non-resident, non-principal-place-of-work municipality):**
- Sarah starts Beachwood work July 1. The employer should NOT withhold Beachwood tax for the first 20 Beachwood-days under R.C. 718.011.
- Approximately Day 21 hits in early August (July 1, 2, 3 = 3 days week 1; 3 days/week for ~7 weeks → Day 21 hits around Aug 12).
- **On Day 21 trigger:** the employer must:
  - Begin withholding Beachwood 2.0% non-resident rate on Beachwood-day wages for subsequent days (US-OH-dr-orc-718-011.txt (D)(1); Beachwood rate/credit per US-OH-dr-rita-rate-table.txt: "Beachwood | 050 | 2.000% | 100.000%")
  - Optionally elect to withhold for the first 20 Beachwood-days, in which case the Akron tax paid for those days is refundable to Sarah (US-OH-dr-orc-718-011.txt (D)(2)-(3)); remit any catch-up to RITA (Beachwood is RITA)
  - Adjust Akron withholding: the employer had been (incorrectly, but per the 20-day default) withholding Akron 2.5% on Beachwood-day wages during Days 1-20 (because under 20-day rule, the wages were sourced to principal place of work). The CCA position on whether Akron tax was correctly withheld on those Beachwood days is nuanced -- best practice is to leave Akron withholding alone for the under-20 days (since Akron tax was legitimately owed under the default sourcing) and not apply a Beachwood credit to it; the catch-up to Beachwood is incremental. (US-OH-dr-orc-718-011.txt (D)(1)-(3))

> **Important interpretive note:** R.C. 718.011 and the 2021-2025 guidance from the Ohio Department of Taxation are not fully settled on whether the Day-21 catch-up to Beachwood is an *addition* to Akron tax already withheld, or a *reallocation* (with Akron refund and Beachwood payment). The conservative, dominant practice is reallocation -- Akron withholding on those 20 days is refunded/credited back via amended Akron filing, and Beachwood withholding is remitted fresh. Confirm with the relevant municipalities for any large-dollar case.

**Year-end W-2 lines for Sarah:**
- Box 18/19/20: Akron -- wages and tax for all Akron days (4 days/week Jan-Jun + 2 days/week Jul-Aug + 5 days/week Sep-Dec)
- Box 18/19/20: Hudson -- wages and tax for Hudson telework days (1 day/week Jan-Jun)
- Box 18/19/20: Beachwood -- wages and tax for Beachwood days post-Day-21 catch-up (3 days/week Jul-Aug, all days)

**AUDIT FLASH POINT:** This pattern is the canonical Ohio payroll audit nightmare: three municipalities (Akron-CCA, Hudson-RITA, Beachwood-RITA), 20-day rule triggering mid-year, courtesy withholding for resident, and a remote-work component. Documentation requirements:
- Daily timesheet showing physical work location (employer-maintained, employee-attested)
- Monthly summary log per employee per municipality with day-count
- Day-21 trigger alert system (manual or in payroll software)
- Year-end reconciliation cross-checking each municipality's withholding remittances to the W-2 lines

### 10. Provenance & Citations

**Statutes (Ohio Revised Code):**
- R.C. 5747 (Ohio Income Tax) -- entire chapter
- R.C. 5747.06 -- Employer withholding obligation
- R.C. 5747.07 -- Annual reconciliation (IT 3) (archived US-OH-dr-orc-5747-07-9-30-2025.txt)
- R.C. 5747.071 -- Late payment penalty (50%)
- R.C. 5747.15 -- General penalties (archived US-OH-dr-orc-5747-15.txt)
- R.C. 718 (Municipal Income Tax) -- entire chapter
- R.C. 718.011 -- 20-day rule (as rewritten by SB 22, 2021)
- R.C. 718.03 -- Employer withholding for municipalities (archived US-OH-dr-orc-718-03.txt)
- R.C. 4141 (Unemployment Compensation) -- entire chapter
- R.C. 4141.241 -- Reimbursing employer election
- R.C. 4141.244 -- SUTA dumping prohibition
- R.C. 4123 (Workers' Compensation) -- entire chapter
- R.C. 4123.01 -- Definitions including employee/contractor (archived US-OH-dr-orc-4123-01.txt)
- R.C. 4123.35 -- Self-insurance (archived US-OH-dr-orc-4123-35.txt)
- Statutory immunity for workers' compensation carriers (archived US-OH-dr-orc-4123-74.txt)
- Local benefits-treaty preemption for employees (archived US-OH-dr-orc-4113-85.txt)

**Administrative Code (Ohio Administrative Code):**
- O.A.C. 5703-7-04 -- Withholding deposit frequency
- O.A.C. 5703-7-10 -- Withholding tables
- O.A.C. 5703-7-19 -- E-file mandate
- O.A.C. 4141-9-04 -- New employer SUI rates

**Session laws:**
- HB 5 (2014) -- Municipal income tax uniformity
- HB 110 (2021) -- Budget bill confirming SB 22 changes
- SB 22 (2021) -- 20-day rule rewrite; rollback of pandemic telework fiction
- HB 33 (2023) -- Income tax phase-down (archived US-OH-dr-lsc-hb33-greenbook.txt; the enacted top-rate path is reflected in US-OH-dr-it1040-2025-booklet-ty2025.txt: 3.125% top rate for 2025)
- HB 96 (2025) -- Continued phase-down (3.125% top rate in effect for 2025 per US-OH-dr-it1040-2025-booklet-ty2025.txt; 2026 path see Not yet confirmed: in Sources)

**Federal guidance referenced:**
- IRS Rev. Rul. 87-41 -- 20-factor common-law worker classification
- IRC §3508 -- Direct sellers statutory non-employee
- IRC Subtitle C (Federal Employment Taxes) -- federal payroll baseline; deferred to federal payroll skill

**Agency publications:**
- Ohio Department of Taxation, *Employer's Withholding Tax Guide*, revised January 2025
- RITA, *Employer Withholding Tax Guide*, current edition (rita.ohioregional.gov)
- CCA, *Employer Tax Guidelines*, current edition (ccatax.ci.cleveland.oh.us)
- City of Columbus, *Income Tax Employer's Guide*, current edition
- City of Cincinnati, *Income Tax Withholding Manual*, current edition
- ODJFS, *Employer Resource Information Center (ERIC) User Guide*, 2025
- Ohio BWC, *Employer Compliance Reference Guide*, policy year 2025-2026

**Version history:**
- v0.1 (2025-11-15): Initial drafting. Reviewer status: pending. Awaiting credentialed Ohio payroll-professional sign-off before use on live filings.

**Reviewer to-do (before promoting to verified):**
1. Confirm current CCA member roster (Akron status in particular, given recent transitions)
2. Confirm BWC maximum reportable wage for policy year July 1, 2025 – June 30, 2026 at $38,300 against published BWC rate manual
3. Confirm RITA member count (~330 cited) against current RITA published list
4. Cross-check direct-file city list (Cincinnati, Columbus, Dayton, Toledo, Lakewood, Dublin) against current ODT bulletin
5. Verify the 50% late-deposit penalty under R.C. 5747.071 is still automatic and not subject to recent legislative amendment
6. Verify supplemental wage 3.5% flat-rate guidance is still endorsed by ODT's 2025 Withholding Tax Guide (see Not yet confirmed: in Sources)

## End of skill.

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

## The taxable base

## Deadlines and filing

## Penalties and interest

## Cross-border points

## Worked examples

## Ask the client first

## Sources

Not yet confirmed: the following figures/claims lack archived line-citations -- 2026 top-rate glide path and 2027 flat-2.75% target under HB 96; the 3.5% flat supplemental-wage method and severance-as-supplemental treatment in ODT's Employer's Withholding Tax Guide; the e-file thresholds (250+ W-2s / prior-year withholding over $84,000); SUI coverage thresholds ($1,500 in a quarter or 20 different weeks) and the agricultural coverage threshold; the count of 600+ taxing municipalities and the 1.00%-3.00% rate range; RITA member count (~330), RITA's $2,399 monthly-remittance threshold, Form 11 February 28 due date, and Form 11A/17/27 numbering; CCA member count (~50) and CCA-W3/CCA-117/CCA-119 form numbering; Cincinnati's resident-credit policy; the January 31 municipal W-2 transmittal date; BWC self-insurance "$5M+ net worth" rule of thumb; the $120 minimum premium; the 100% no-coverage penalty; adoption of the IRS 20-factor test (Rev. Rul. 87-41) for SUI/BWC; the real-estate-agent and direct-seller statutory classifications; Parma city rate (2.5%), Lakewood (1.5%) and Westerville (2.0%) rates; the W-2 Box 18/19/20 municipal mapping used in the examples; Columbus's credit treatment for tax paid to other municipalities; and the Ohio paid-sick-leave legislative status.


| Source | URL | Read on |
| --- | --- | --- |
| Ohio Dept of Taxation | https://tax.ohio.gov/ | 2026-10-28 |

## Talk to a verified accountant

### Sources


### Talk to a verified accountant

