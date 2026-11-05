---
name: or-payroll
description: Tier 2 Oregon content skill for employer payroll compliance covering tax year 2026. Includes the OR PIT brackets up to 9.9%, supplemental wage rate 8.0%, OR-W-4 state withholding form, Form OQ quarterly combined withholding/UI return, OR UI wage base $54,300 for 2025 (highest in the US) with rates 0.9%-5.4%, the Statewide Transit Tax 0.1% on all wages (no cap), TriMet 0.8237% employer payroll tax for Portland area, Lane Transit 0.80% for Eugene, the OR Paid Leave program 1.0% total split between employer (0.4%) and employee (0.6%), and WBF Workers' Benefit Fund assessment 1.8 cents per hour (2026).
jurisdiction: US-OR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# OR Payroll

### Oregon Payroll Compliance -- Tier 2 Content Skill

### 1. Scope

This skill is the authoritative Tier 2 content layer for Oregon employer payroll compliance for tax year 2026. It is consumed by upstream workflow skills (`us-tax-workflow-base`, `us-federal-return-assembly`) when an employer has Oregon-source wages, an Oregon resident employee, or any employee performing services within Oregon transit district boundaries.

### 1.1 What this skill covers

- Oregon Personal Income Tax (PIT) withholding from wages -- brackets, supplemental wage rate, OR-W-4 employee certificate, Form OQ filing
- Oregon Unemployment Insurance (UI) -- wage base $54,300 (the highest taxable UI wage base in the United States for 2025), rates 0.9%–5.4%, new-employer rate 2.4%
- Statewide Transit Tax (STT) -- 0.1% of all Oregon wages, no wage base cap, applied to Oregon residents working anywhere and to non-residents performing services in Oregon (US-OR-dr-stt.txt: one-tenth of 1 percent or .001, enacted by HB 2017 (2017), ORS 320.550)
- Local transit district employer payroll taxes:
  - TriMet (Portland metropolitan area) -- 0.8237% employer (US-OR-dr-trimet-taxinfo.txt); employee 0.13% (see Not yet confirmed: list in Sources)
  - Lane Transit District (Eugene/Springfield) -- 0.80% employer (US-OR-dr-oq-2026.txt: 'Lane Transit District (LTD) tax rate is 0.0080')
  - Salem Area Mass Transit District / Cherriots -- employer payroll tax proposed from 2027 (US-OR-dr-cherriots-se.txt); the 0.36% rate is listed under Not-yet-confirmed in Sources
- Oregon Paid Leave (Paid Leave Oregon) -- 1.0% total contribution, split 40/60 employer/employee for employers with 25+ employees, up to 12 weeks of paid family/medical/safe leave benefits (US-OR-dr-paidleave.txt: 'The total contribution rate for 2026 is 1% of gross wages up to $184,500'; US-OR-dr-lro-basic-facts-2026.pdf: up to 12 weeks in a 52-week period)
- Workers' Benefit Fund (WBF) assessment -- 1.8 cents per hour worked (2026), listed under Not yet confirmed in Sources for the 2025 split rate (US-OR-dr-wbf.txt: 'In 2026, the WBF assessment is 1.8 cents per hour worked'); the 2025 0.66¢/0.66¢ split is listed under Not-yet-confirmed in Sources
- Final-pay rule -- by end of next business day after termination by employer
- Independent contractor classification -- the Oregon ABC test, codified by case law and adopted statutorily post-2020
- Federal interactions -- Family and Medical Leave Act parity, Pay Equity Act 2019 implications for payroll

### 1.2 What this skill does NOT cover

- Oregon Corporate Activity Tax (CAT) -- see `or-corporate-activity-tax`
- Oregon individual income tax return preparation -- see `or-income-tax`
- Federal payroll (FICA, FUTA, federal income tax withholding, Form 941, Form 940) -- outside scope; covered elsewhere
- Multistate apportionment for employers outside Oregon with zero Oregon nexus
- Self-employed sole proprietor own-wage treatment -- sole proprietors do not pay themselves W-2 wages and do not owe employer payroll taxes on owner draws
- Tribal employers and federally-recognized tribal sovereignty exemptions
- Agricultural labor exemptions under ORS 657.045 (limited scope; refer)

### 1.3 Conservative defaults

- **Default: worker classification** -- Treat worker as W-2 employee unless ABC test affirmatively fails (i.e., default to employee classification)
- **Default: STT applicability** -- Apply Statewide Transit Tax to all wages until exemption is documented
- **Default: transit district application** -- Apply TriMet/Lane/Cherriots to all hours worked inside the district unless employer has documented evidence of work performed entirely outside
- **Default: OR-W-4 missing** -- Use the standard OR-W-4 default (single, zero allowances) when no signed OR-W-4 is on file
- **Default: Paid Leave Oregon employee count** -- For Paid Leave Oregon employee count, count all employees nationwide, not just Oregon (per OED rule)

## Who this applies to

Oregon employers (and out-of-state employers with Oregon-source wages,
Oregon-resident remote employees, or employees performing services inside
Oregon transit district boundaries) with payroll obligations for tax year
2025: PIT withholding, UI, Statewide Transit Tax, transit district taxes,
Paid Leave Oregon, and the Workers' Benefit Fund. Sole proprietors paying
themselves no W-2 wages are out of scope (see ### 1.2).

## Rates, bands and thresholds

### 2.1 2026 brackets (single filer; married/HOH/QSS chart thresholds differ as shown)

**2026 Oregon PIT rate chart, single or married filing separately (OR-ESTIMATE 2026, Chart S)**

| Taxable income (single) | Marginal rate |
| --- | --- |
| $0 – $4,550 | 4.75% |
| $4,551 – $11,400 | 6.75% |
| $11,401 – $125,000 | 8.75% |
| Over $125,000 | 9.90% |

- **Married filing jointly / head of household / qualifying surviving spouse (Chart J)** -- 4.75% to $9,100; 6.75% over $9,100 to $22,800; 8.75% over $22,800 to $250,000; 9.9% over $250,000 (OR-ESTIMATE 2026).

The 9.9% top rate has been in place since 2013 and remains the third-highest top state PIT rate in the United States after California (13.3%) and Hawaii (11.0%).

### 2.2 Supplemental wage rate

- **Oregon supplemental wage withholding rate (2025)** -- 8.0%

This rate applies to bonuses, commissions, severance, equity vesting events, retroactive pay, and other supplemental wages identified under IRS Pub 15 (which Oregon incorporates by reference for definitional purposes but applies its own rate to).

Employers may use the supplemental flat rate **or** the aggregate method that combines the supplemental wage with the most recent regular pay period and applies the standard withholding tables. The flat method is strongly preferred for one-time large payments (bonuses, RSU vests) because the aggregate method can produce mechanical over-withholding when the supplemental payment is large relative to the regular paycheck.

### 2.3 OR-W-4 state withholding certificate

- **OR-W-4** -- Oregon decoupled from the federal Form W-4 in 2020 when the IRS eliminated withholding allowances. Employers must obtain a Form OR-W-4 from every Oregon employee. The OR-W-4 still uses an allowances system and does not mirror the federal W-4 structure.
- **Default rule when no OR-W-4 is on file** -- withhold as single with zero allowances. This is the most conservative default and the explicit DOR rule.
- **OR-W-4 retention** -- retain for at least four years following the last calendar year the certificate was in effect. Submit to DOR only when requested or when the employee claims more than 10 allowances (mandatory submission trigger under OAR 150-316-0290).  _(OAR 150-316-0290)_

### 2.4 Form OQ -- Quarterly Oregon Combined Tax Report

- **Form OQ** -- Form OQ is Oregon's unified quarterly return that consolidates four employer obligations into a single filing: 1. Oregon income tax withholding 2. Oregon UI tax (Schedule B) 3. Statewide Transit Tax (Schedule STT) 4. TriMet or Lane Transit tax (Schedule TM or LTD) if applicable
- **Form OQ due dates and e-filing** -- Due dates: April 30, July 31, October 31, January 31. Electronic filing via Frances Online (Oregon Frances Online portal, which replaced OTTER) is mandatory for employers with 250+ W-2s and strongly encouraged otherwise.
- **Form OR-WR Annual Withholding Reconciliation** -- Form OR-WR (Annual Withholding Reconciliation) is due January 31 of the following year and reconciles the four quarterly OQs to the W-2/W-3 filed with DOR.

> **AUDIT FLASH POINT:** Form OQ filers commonly forget to attach Schedule STT or Schedule TM/LTD when the employer has Oregon wages but no employees in the transit district. The schedules must be filed with **zeros** rather than omitted -- omission triggers a non-filer notice and a $50 penalty per schedule per quarter under ORS 314.400.

## The taxable base

### 3.0 What wages are in the base

- **Withholding base** -- Oregon PIT withholding applies to all Oregon-source wages under the OR-W-4 tables (see ## Rates, bands and thresholds).
- **UI base** -- taxable wages capped at the annual wage base (### 3.1), per employer per year.
- **STT base** -- every dollar of covered wages, no cap (### 4.1).
- **Transit district base** -- wages for services performed inside the district boundary (### 5.5).
- **Paid Leave base** -- wages up to the Social Security wage base cap (### 6.3).
- **WBF base** -- hours worked, not dollars (### 7.1).

### 3.1 Wage base $54,300 for 2025

- **Oregon 2025 taxable UI wage base** -- $54,300  _(ORS 657.435)_ (US-OR-dr-ui-2026-pr.pdf: 'from $54,300 per employee in 2025 to $56,700'; US-OR-dr-lro-basic-facts-2026.pdf: 'the first $54,300 of wages paid to each employee')

Oregon's 2025 taxable UI wage base is **$54,300**, the highest of any state. The wage base is set annually as 80% of the state average annual wage under ORS 657.435 (US-OR-dr-ors657.txt: wages exclude amounts 'in excess of an amount obtained by multiplying the average annual wage for the second preceding calendar year by 0.80'). For comparison:

- Oregon: $54,300 (US-OR-dr-ui-2026-pr.pdf)
- Washington: $72,800 for 2025, rising to $78,200 for 2026 (US-OR-dr-wa-ui-base.txt; note: WA's 2026 base exceeds Oregon's $56,700 2026 base)
- Idaho: $55,300 (US-OR-dr-id-ui-report-2025.pdf: 'the taxable wage base for 2025 is $55,300')
- Most other states: $7,000 – $20,000

Implications:
- Annual UI tax cost per employee is materially higher in Oregon than in most jurisdictions
- For high-earning employees, the employer reaches the wage cap by mid-year; for lower-earning employees, the employer pays UI tax on essentially every dollar
- Multistate employers must apply the **localization of work** test under ORS 657.030 to determine which state's wage base applies

### 3.2 Rates 0.0% – 5.4%; new employer 2.4%

- **Oregon UI experience rate range 2025** -- 0.9% – 5.4% (US-OR-dr-ui-rates.txt: 'Taxable minimum rate: 0.9% Taxable maximum rate: 5.4%')
- **Oregon UI new-employer rate 2025** -- 2.4% (US-OR-dr-ui-rates.txt: 'Taxable base tax rate: 2.4% (new employer rate)')

Oregon uses an experience-rated system with rates ranging from 0.9% to 5.4% in 2025 (US-OR-dr-ui-rates.txt). The new-employer rate for 2025 is 2.4%. Rates are assigned annually based on the employer's reserve ratio (cumulative contributions minus benefits charged, divided by average annual taxable payroll).

Schedule D applies for 2025 (Oregon has eight rate schedules A–H; D is the midpoint). The schedule is set by the OED based on the trust fund balance ratio.

### 3.3 Employee count and Form OQ Schedule B

- **Schedule B taxable/excess wage reporting** -- Schedule B of Form OQ reports each employee's wages, broken down between taxable (capped at $54,300 YTD) and excess (above the cap). UI tax is owed only on the taxable portion (US-OR-dr-oq-2026.txt: 'Excess wages are wages ... above the taxable wage base for the year'; 'Taxable wages. Enter box 13a minus box 14a').

> **AUDIT FLASH POINT:** Employers commonly miscompute the taxable/excess split when an employee changes employers mid-year. The $54,300 wage base is per-employer per-year, not per-employee per-year across employers. A new hire whose YTD wages with the prior employer already exceeded $54,300 still owes UI tax on the first $54,300 paid by the new employer (US-OR-dr-ors657.txt: the wage-base exclusion applies to remuneration received 'from each employer' per calendar year).

### 4. Statewide Transit Tax -- 0.1% with no cap

### 4.1 Mechanics

- **Statewide Transit Tax rate** -- 0.1%  _(HB 2017 (2017); ORS 320.550)_ (US-OR-dr-stt.txt: 'one-tenth of 1 percent or .001')
- **STT wage base cap** -- There is no wage base cap. The 0.1% applies to every dollar of covered wages.  _(ORS 320.550)_ (US-OR-dr-stt.txt: the tax is calculated on the employee's wages as defined in ORS 316.162, with no cap stated)

The Statewide Transit Tax (STT), enacted under HB 2017 (2017) and codified at ORS 320.550, is a 0.1% payroll tax on (US-OR-dr-stt.txt):

- All wages paid to Oregon residents (regardless of where work is performed)
- All wages paid to non-residents for services performed **in** Oregon

### 4.2 Who pays

- **STT liability** -- The STT is an employee-paid tax that the employer is required to withhold and remit. The employer does not bear the economic burden but bears full liability for collection and remittance.

### 4.3 Filing and remittance

- **STT filing and W-2 reporting** -- STT is reported on Schedule STT of Form OQ each quarter. Annual reconciliation on Form OR-STT-A is due January 31. The STT is also reported in W-2 Box 14 with the code "ORSTT W/H" (DOR-prescribed code).

### 4.4 Common pitfalls

> **AUDIT FLASH POINT:** Out-of-state employers with even one Oregon-resident remote worker frequently miss STT registration entirely. The 0.1% feels trivial per paycheck (e.g., $1 on a $1,000 weekly check) but compounded across years with no wage cap, an out-of-state employer with five Oregon remote employees earning $100,000 each owes $500/year STT -- small in dollars but a 100% audit certainty given OED's data-share with DOR. The non-filing penalty under ORS 314.400 is the larger exposure.

> **AUDIT FLASH POINT:** The STT applies to non-resident remote workers physically in Oregon. A consultant living in Vancouver, WA who crosses the river to work at a Portland client site has STT-covered wages for those days. The day-by-day allocation must be tracked.

### 5. Local transit district employer payroll taxes

### 5.1 TriMet -- 0.8237% employer + 0.13% employee (Portland)

- **TriMet employer rate (2025)** -- 0.8237% (US-OR-dr-trimet-taxinfo.txt: 'The transit tax rate is 0.8237%'; US-OR-dr-transit-211-503.pdf rate table: 0.008237 for 1/1/25-12/31/25 and 1/1/26 and beyond)
- **TriMet employee rate (2025)** -- 0.13%  _(OAR 150-267-0020)_ (see Not yet confirmed: list in Sources)

The TriMet (Tri-County Metropolitan Transportation District of Oregon) employer payroll tax applies to wages paid for services performed within the TriMet district, which encompasses most of Multnomah County, the urban portions of Washington County, and the urban portions of Clackamas County.

- Employer rate (2025): 0.8237% of subject wages (US-OR-dr-trimet-taxinfo.txt)
- Employee rate (2025): 0.13% (this is the separate TriMet employee assessment; Note: some references treat the 0.13% as part of OR Paid Leave employee share -- treat as separate per OAR 150-267-0020 unless guidance updates; see Not yet confirmed: list in Sources -- the archived TriMet page describes only the employer transit tax and the statewide 0.1% employee tax)
- No wage base cap
- Reported on Schedule TM of Form OQ

The TriMet rate is statutorily increased by 0.0001 (1 basis point) per year through 2026 under ORS 267.385, then capped.

### 5.2 Lane Transit District (LTD) -- 0.79% employer (Eugene/Springfield)

- **Lane Transit District employer rate (2026)** -- 0.80% (US-OR-dr-oq-2026.txt: 'Lane Transit District (LTD) tax rate is 0.0080'); the 2025 rate of 0.79% is listed under Not-yet-confirmed in Sources

The Lane Transit District employer payroll tax applies to wages paid for services performed within the LTD boundary, which covers most of Lane County including Eugene, Springfield, and surrounding communities.

- Employer rate (2026): 0.80% of subject wages (US-OR-dr-oq-2026.txt)
- No wage base cap
- Reported on Schedule LTD of Form OQ
- Similar 0.0001 annual increase through 2026 under ORS 267.385

### 5.3 Salem Area Mass Transit District (Cherriots) -- 0.36%

- **Cherriots employer rate** -- 0.36% (0.0036) (see Not yet confirmed: list in Sources; US-OR-dr-cherriots-se.txt describes an employer payroll tax starting in 2027 but gives no rate)
- **Cherriots administration** -- Unlike TriMet and LTD, the Cherriots tax is administered locally rather than through Form OQ; the employer registers with and remits to Cherriots directly.

### 5.4 Sandy / Canby / South Clackamas / others

Several smaller cities and special districts impose narrow employer payroll taxes (typically 0.5%–0.7%; see Not yet confirmed: list in Sources) for local transit. These are jurisdiction-by-jurisdiction and require boundary verification using the DOR's transit district lookup tool.

### 5.5 District boundary determination

- **Boundary determination steps** -- Determining whether a wage is "subject" to TriMet or LTD requires: 1. Geocoding the work location (not the employee's residence) 2. Cross-referencing the geocoded coordinates against the official transit district map (published annually by each district) 3. For remote workers, applying the principal-place-of-services test under OAR 150-267-0030: the location where the employee performs the majority of work in the quarter  _(OAR 150-267-0030)_

> **AUDIT FLASH POINT:** The single most common Oregon payroll audit finding is misallocation between TriMet, Lane, and "no transit district." Employers often default all Oregon wages to TriMet because Portland is the largest metro, or default everything to "no district" because the employer is headquartered outside Oregon. Both are wrong. Each employee's work-location geocoding must be documented and refreshed annually, and remote-work reallocations during 2020–2024 created retroactive exposure that the OED began aggressively auditing in 2024.

### 6. Paid Leave Oregon -- 0.6% combined, 12 weeks of benefits

### 6.1 Program overview

- **Paid Leave Oregon program overview** -- Paid Leave Oregon, created by the 2019 Oregon Legislature (US-OR-dr-lro-basic-facts-2026.pdf: 'The 2019 Oregon Legislature created the Paid Leave Oregon (PLO) program'), provides up to 12 weeks of paid leave per benefit year, with an additional 2 weeks in some situations for a pregnant employee (US-OR-dr-lro-basic-facts-2026.pdf), for family, medical, or safe leave (same source: 'up to 12 weeks, in a 52-week period, for family, medical, or safe leave'). Benefits are wage-replacement limited to a maximum of 120% of the state average weekly wage (US-OR-dr-lro-basic-facts-2026.pdf). The September 3, 2023 benefits effective date, the 16-week combined leave ceiling, and the approximately $1,568.60 maximum weekly benefit for 2025 are listed under Not-yet-confirmed in Sources.

### 6.2 Contribution mechanics -- 0.6% total, split 40/60

- **Paid Leave Oregon combined contribution rate (2025)** -- 1.0% (US-OR-dr-lro-basic-facts-2026.pdf: 'For 2025, the tax rate was set at 1%'; US-OR-dr-paidleave.txt: 2026 rate also 1%)
- **25+ employees nationwide split** -- For employers with 25 or more employees nationwide: Employer share: 40% of the total (0.4% of wages); Employee share: 60% of the total (0.6% of wages, withheld from paychecks)
- **Fewer than 25 employees nationwide** -- For employers with fewer than 25 employees nationwide: Employer share: $0 (exempt from employer portion); Employee share: 0.6% of wages (still withheld); Small employers may opt in to employer-portion participation to qualify for assistance grants (US-OR-dr-paidleave.txt: small employers 'don't pay the employer contribution to Paid Leave Oregon'; assistance grants for employers with fewer than 25 employees on average)
- **25-employee count basis** -- The 25-employee count is a nationwide headcount, not Oregon-only. A California company with 30 employees and one Oregon remote worker is a "25+" employer for Paid Leave Oregon purposes.

### 6.3 Wage base cap

- **Paid Leave Oregon contribution wage base cap** -- $176,100 for 2025, $184,500 for 2026 (US-OR-dr-lro-basic-facts-2026.pdf: 'the wage limit was set at $176,100'; US-OR-dr-paidleave.txt: '1% of gross wages up to $184,500' for 2026)
- **Wages above SS cap** -- Wages above the SS cap are not subject to Paid Leave contributions.

### 6.4 Filing

- **Paid Leave Oregon filing schedule** -- Paid Leave Oregon contributions are reported on Schedule P of Form OQ quarterly. The schedule is filed with both employer and employee shares combined and remitted with Form OQ.

### 6.5 Equivalent plans

- **Equivalent private plans** -- Employers may apply to OED for approval of an equivalent private plan that provides benefits and protections at least equal to the state plan. Approved equivalent plans exempt the employer (and its employees) from state contributions.

> **AUDIT FLASH POINT:** The employer/employee 40/60 split is the most commonly mis-coded line item in Oregon payroll. Many payroll providers default to 50/50 or to "employer pays all" which produces an over-payment by the employer and an under-withholding from the employee -- and creates a constructive bonus to the employee that should have been included in federal Box 1 wages. The 40/60 must be coded explicitly.

> **AUDIT FLASH POINT:** Employers using the small-employer (<25) exemption often miscount by limiting to Oregon employees. OED counts nationwide. Misclassification as small triggers a back-assessment of employer contributions plus interest from program inception.

### 7. Workers' Benefit Fund Assessment

### 7.1 Mechanics

- **WBF assessment (2026)** -- 1.8 cents per hour worked  _(ORS 656.506)_ (US-OR-dr-wbf.txt: 'In 2026, the WBF assessment is 1.8 cents per hour worked')
- **WBF employer rate (2025)** -- $0.0066 per hour worked (0.66¢)  _(ORS 656.506)_ (see Not yet confirmed: list in Sources)
- **WBF employee rate (2025)** -- $0.0066 per hour worked (0.66¢)  _(ORS 656.506)_ (see Not yet confirmed: list in Sources)
- **WBF combined rate (2025)** -- $0.0132 per hour worked (1.32¢)  _(ORS 656.506)_ (see Not yet confirmed: list in Sources)
- **WBF hours basis for salaried/part-time** -- Salaried employees: use 40 hours per week (or actual hours if tracked). Part-time employees: use actual hours.

### 7.2 Filing

- **WBF filing** -- WBF assessment is reported on Form OQ alongside withholding, UI, and STT.

> **AUDIT FLASH POINT (worked example figures; hypothetical):** WBF is computed per-hour, not per-dollar. A common mistake is to apply a 0.0066% rate to wages, which dramatically under-reports. The correct base is hours worked × the per-hour assessment (US-OR-dr-wbf.txt: assessment is 'per hour worked'; US-OR-dr-oq-2026.txt: 'Determining WBF hours worked').

### 8. ABC test for independent contractor classification

- **Oregon independent contractor ABC test** -- Oregon does not have a single statutory ABC test analog to California AB5. However, ORS 670.600 (the "independent contractor" definition for OED and DOR purposes) operates as a de-facto ABC test and has been strengthened by case law and by 2020+ administrative guidance. A worker is an independent contractor only if all of the following are true: A. The worker is free from direction and control over the means and manner of providing services, subject only to the right of the contracting person to specify the desired results. B. The worker is customarily engaged in an independently established business of the same nature as the services contracted for. Three of the following five factors must be met: 1. Maintains a business location separate from the contracting person 2. Bears the risk of loss 3. Provides contracted services for two or more different customers within a 12-month period, or routinely engages in business advertising or solicitation 4. Makes a significant investment in the business through tools, equipment, or premises 5. Has the authority to hire and fire employees to perform the contracted services C. The worker is licensed under ORS 671 or 701 if such license is required for the services performed. Failure on any of A, B, or C reclassifies the worker as a W-2 employee for Oregon withholding, UI, STT, transit district, Paid Leave, and WBF purposes.  _(ORS 670.600)_

> **AUDIT FLASH POINT:** Software developers, designers, and other "professional" contractors frequently fail Prong B because they only have one client and do not advertise. Even with a Form 1099-NEC issued, OED can reclassify and impose retroactive UI, STT, transit, and Paid Leave taxes plus penalties under ORS 657.471.

### 9. Final pay rule

- **Final pay rule under ORS 652.140** -- Under ORS 652.140: - Employer-initiated termination (firing/layoff): all wages due by the end of the next business day after termination - Employee-initiated termination (quit) with 48+ hours notice: all wages due on the last day worked - Employee-initiated termination without 48 hours notice: all wages due within five business days or the next regular payday, whichever is earlier  _(ORS 652.140)_
- **Penalty wages under ORS 652.150** -- Violation triggers penalty wages under ORS 652.150 equal to the employee's regular daily wage rate for each day the wages remain unpaid, up to 30 days. Penalty wages are owed even if the underpayment is minor.  _(ORS 652.150)_

## Deadlines and filing

- **Form OQ quarterly combined return** -- Oregon withholding, UI (Schedule B), Statewide Transit Tax (Schedule STT), and TriMet/Lane Transit (Schedule TM/LTD) are consolidated on Form OQ, due April 30, July 31, October 31, and January 31; schedules must be filed with zeros rather than omitted.
- **Form OQ e-filing** -- Electronic filing via Frances Online (Oregon Frances Online portal, which replaced OTTER) is mandatory for employers with 250+ W-2s and strongly encouraged otherwise.
- **Annual reconciliations** -- Form OR-WR (withholding) and Form OR-STT-A (Statewide Transit Tax) are each due January 31 of the following year.
- **Registration** -- Register with DOR for withholding and OED for UI/Paid Leave before the first Oregon payroll.

## Penalties and interest

- **Penalty wages under ORS 652.150** -- failure to pay final wages in full timely triggers penalty wages (detailed under Final pay rules above).
- **Late filing/payment penalties** -- Oregon imposes a 5 percent late-payment penalty on tax not paid by the original due date, a 20 percent late-filing penalty if the return is filed more than three months late (25 percent combined), and a 100 percent penalty if you do not file after notice  _(ORS 314.400; ORS 657.471)_ (US-OR-dr-dor-penalties.txt).
## Cross-border points

### 10.1 Family and Medical Leave Act parity

- **FMLA and Paid Leave Oregon concurrency** -- Paid Leave Oregon runs concurrently with federal FMLA leave when both apply. An employer covered by both must coordinate the leave designation; treating them as sequential (rather than concurrent) is a violation under both OED rule and DOL guidance.

### 10.2 Oregon Pay Equity Act 2019

- **Oregon Pay Equity Act requirements** -- The Oregon Pay Equity Act (ORS 652.220) prohibits pay discrimination based on protected class and requires equal pay for work of "comparable character." For payroll purposes: - Salary history inquiries are prohibited - Pay decisions must be defensible against an "affirmative defense" requiring a documented equal-pay analysis within the prior three years - Posting of salary ranges in job postings is required under separate amendments Payroll system implications: maintain documented job-evaluation factors and ensure compensation changes carry justification metadata.  _(ORS 652.220)_

## Worked examples

### 11.1 Example A -- Portland TriMet-area employer, single employee (hypothetical facts)

- Employer: Acme Software LLC, located in Portland (Multnomah County, within TriMet district)
- Employee: J. Smith, Oregon resident, lives and works in Portland
- 2025 gross wages: $120,000 salaried, 2,080 hours
- No bonuses

**Example A computation**

| Tax | Base | Rate | Amount |
| --- | --- | --- | --- |
| Oregon UI (employer) | $54,300 (capped) | 2.4% (new emp.) | $1,303.20 |
| Statewide Transit Tax (EE) | $120,000 | 0.1% | $120.00 |
| TriMet (employer) | $120,000 | 0.8237% | $988.44 |
| Paid Leave Oregon (employer) | $120,000 | 0.4% (40% of 1%) | $480.00 |
| Paid Leave Oregon (employee) | $120,000 | 0.6% (60% of 1%) | $720.00 |
| WBF (employer) | 2,080 hours | $0.0066/hr | $13.73 |
| WBF (employee) | 2,080 hours | $0.0066/hr | $13.73 |

WBF rows use the 2025 $0.0066/hour split rate (listed under Not yet confirmed in Sources); the 2026 assessment is 1.8 cents per hour (US-OR-dr-wbf.txt).

Employer total (Oregon-specific, excluding federal): approximately $2,785.37 (worked-example arithmetic; hypothetical facts)
Employee withholding (Oregon-specific, excluding federal & PIT): approximately $853.73 plus Oregon PIT withholding from OR-W-4 table (worked-example arithmetic; hypothetical facts)

### 11.2 Example B -- Eugene Lane Transit employer (hypothetical facts)

- Employer: Willamette Designs Inc., located in Eugene (Lane County, within LTD)
- Employee: M. Garcia, Oregon resident
- 2025 gross wages: $75,000 salaried, 2,080 hours
- Employer has 30 employees nationwide

**Example B computation**

| Tax | Base | Rate | Amount |
| --- | --- | --- | --- |
| Oregon UI (employer) | $54,300 (capped) | 1.8% (assumed) | $977.40 |
| Statewide Transit Tax (EE) | $75,000 | 0.1% | $75.00 |
| Lane Transit (employer) | $75,000 | 0.79% | $592.50 |
| Paid Leave Oregon (employer) | $75,000 | 0.4% | $300.00 |
| Paid Leave Oregon (employee) | $75,000 | 0.6% | $450.00 |
| WBF (employer) | 2,080 hours | $0.0066/hr | $13.73 |
| WBF (employee) | 2,080 hours | $0.0066/hr | $13.73 |

The Lane Transit row uses the 2025 0.79% rate (see Not yet confirmed: list in Sources; the archived 2026 rate is 0.80%, US-OR-dr-oq-2026.txt); WBF rows use the 2025 $0.0066/hour split rate (see Not yet confirmed: list in Sources).

Employer total: approximately $1,897.36
Note: Because the work is in Eugene (LTD), TriMet does not apply. A common error is to dual-allocate; only the district covering the work location applies.

### 11.3 Example C -- Multistate employer, Oregon-resident remote worker (hypothetical facts)

- Employer: TechCorp Inc., headquartered in Austin, Texas
- Employee: K. Nguyen, lives in Bend, Oregon (Deschutes County -- outside TriMet, LTD, and Cherriots boundaries)
- 2025 gross wages: $150,000 salaried, fully remote, 2,080 hours
- Employer has 200 employees nationwide

**Example C Oregon obligations**

| Tax | Base | Rate | Amount |
| --- | --- | --- | --- |
| Oregon withholding | per OR-W-4 | bracket-based | varies |
| Oregon UI (employer) | $54,300 | 2.4% (new to OR) | $1,303.20 |
| Statewide Transit Tax (EE) | $150,000 | 0.1% | $150.00 |
| TriMet | n/a | -- | $0 |
| Lane Transit | n/a | -- | $0 |
| Cherriots | n/a | -- | $0 |
| Paid Leave Oregon (employer) | $150,000 capped at SS | 0.4% | $600.00 |
| Paid Leave Oregon (employee) | $150,000 capped at SS | 0.6% | $900.00 |
| WBF (employer) | 2,080 hours | $0.0066/hr | $13.73 |
| WBF (employee) | 2,080 hours | $0.0066/hr | $13.73 |

WBF rows use the 2025 $0.0066/hour split rate (see Not yet confirmed: list in Sources).

- TechCorp must register with Oregon DOR for withholding, OED for UI and Paid Leave, and DCBS for WBF -- even with a single Oregon employee
- No transit district tax because Bend is outside all three districts
- The $1,500+ Paid Leave employee + employer combined is a non-trivial annual cost for a single remote hire

### 11.4 Example D -- Portland employee, mid-year wage cap (hypothetical facts)

**Facts:**
- Employer: Acme Software LLC (same as Example A), new hire in Q2
- Employee: D. Park, hired April 1, 2025, $200,000 annualized salary
- Prior employer (Jan–March): paid $50,000 with $50,000 in UI taxable wages

**Acme's UI obligation on Park:**
- Acme's $54,300 wage base is not reduced by Park's prior-employer wages (US-OR-dr-ors657.txt: the exclusion applies per 'each employer' per calendar year)
- Acme owes UI on the first $54,300 paid to Park during 2025
- Park reaches $54,300 in Acme wages around mid-June (3 months × $16,667/mo)
- UI tax on Park (assume 2.4% new-employer): $54,300 × 2.4% = $1,303.20

This is the classic "double-count" problem unique to high-base UI states like Oregon and Washington.

## Ask the client first

Before signing off on an Oregon payroll filing, the credentialed reviewer must verify:

1. Form OQ Schedule STT filed: even if zero
2. Form OQ Schedule TM/LTD filed: correct district per work-location geocoding
3. Paid Leave Oregon 40/60 split: employer at 0.4%, employee at 0.6% (US-OR-dr-paidleave.txt: large employers pay 40% and employees 60% of the 1% rate)
4. UI wage base $54,300 (2025; $56,700 for 2026, US-OR-dr-ui-2026-pr.pdf): not the federal FUTA $7,000 base
5. STT applied with no cap: including high earners
6. WBF on hours, not dollars
7. OR-W-4 on file for every employee: default single/zero if missing
8. Transit district boundary geocoded: for each work location, not based on employer HQ
9. ABC test documented: for every 1099-NEC contractor
10. Final-pay rule timeline: next business day for terminations

## Sources

Not yet confirmed: the TriMet employee 0.13% rate, the Cherriots 0.36%
employer rate, the 0.5%–0.7% range for smaller transit districts, the 2025
Lane Transit 0.79% rate (the archived 2026 rate is 0.80%), the 2025 WBF
$0.0066/hour employer/employee split (the archived 2026 assessment is 1.8
cents per hour), the Paid Leave September 3, 2023 benefits effective date,
the 16-week combined leave ceiling, the approximately $1,568.60 maximum
weekly benefit for 2025, and the worked-example totals are not tied to an
archived capture; the archived captures now also cover the 8.0% supplemental
flat rate, the $54,300/$56,700 UI wage bases, the 0.9%–5.4% UI rate range
and 2.4% new-employer rate, the 0.1% Statewide Transit Tax, the TriMet
0.8237% and Lane Transit 0.80% employer rates, Paid Leave 1.0% total with
40/60 split and the $176,100/$184,500 wage base caps, the WBF 1.8 cents per
hour 2026 assessment, and the 2026 OR-ESTIMATE rate charts.

| Source | URL | Read on |
| --- | --- | --- |
| Oregon Department of Revenue (home) | https://www.oregon.gov/dor | 2026-10-28 |
| Oregon Department of Revenue -- Personal Income Tax | https://www.oregon.gov/dor/programs/individuals/Pages/PIT.aspx | 2026-10-28 |
| Oregon Legislative Assembly -- ORS Chapter 316 | https://www.oregonlegislature.gov/bills_laws/ors/ors316.html | 2026-10-28 |
| Oregon DOR -- 2026 Publication OR-ESTIMATE (Chart S/J 2026 rate charts: single 4.75% to $4,550, 6.75% to $11,400, 8.75% to $125,000, 9.9% above; MFJ/HOH/QSS $9,100/$22,800/$250,000) | https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf | 2026-10-31 |
| OED press release -- 2026 UI tax rate (2025 base $54,300, 2026 base $56,700; Paid Leave 1%/$176,100 2025, $184,500 2026) | https://www.oregon.gov/employ/NewsAndMedia/Documents/2025-11-18_Tax_Rate_2026_Press_Release.pdf | 2026-11-04 |
| OED Current Tax Rate page (min 0.9%, max 5.4%, new-employer 2.4%) | https://www.oregon.gov/employ/Businesses/Pages/Current-Tax-Rate.aspx | 2026-11-04 |
| ORS Chapter 657 (wage base = 0.80 x average annual wage, per each employer) | https://www.oregonlegislature.gov/bills_laws/ors/ors657.html | 2026-11-04 |
| WA ESD UI tax rates (2025 base $72,800; 2026 $78,200) | https://esd.wa.gov/employer-requirements/unemployment-taxes/how-we-determine-tax-rates | 2026-11-04 |
| Idaho UI annual report 2025 (2025 base $55,300) | https://labor.idaho.gov | 2026-11-04 |
| Oregon DOR -- Statewide Transit Tax page (0.1%, HB 2017, ORS 320.550) | https://www.oregon.gov/dor/programs/businesses/pages/statewide-transit-tax.aspx | 2026-11-04 |
| TriMet tax information page (employer transit tax 0.8237%) | https://trimet.org/taxinfo/ | 2026-11-04 |
| DOR Publication 211-503 -- TriMet/Lane transit payroll taxes (rate table) | https://www.oregon.gov/dor/forms/formspubs/transit-payroll-taxes_211-503.pdf | 2026-11-04 |
| Form OQ 2026 combined payroll tax report instructions (TM 0.008237, LTD 0.0080, STT 0.001; WBF hours) | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll-tax-report_150-211-155.pdf | 2026-11-04 |
| Paid Leave Oregon employer overview (2026 rate 1% up to $184,500; 40/60 split; small-employer exemption) | https://paidleave.oregon.gov/employers-overview/ | 2026-11-04 |
| DCBS Workers' Benefit Fund page (2026 assessment 1.8 cents per hour) | https://www.oregon.gov/dcbs/wbf/Pages/index.aspx | 2026-11-04 |
| Oregon LRO Basic Facts 2026 (PLO 1%/$176,100 for 2025; 12 weeks + 2; 120% max; EIC 9%/12%) | https://www.oregonlegislature.gov/lro/Documents/Basic%20Facts%202026.pdf | 2026-11-04 |
| DOR Withholding Tax Formulas 2025 (8 percent flat rate for supplemental wages; OR-W-4) | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2025.pdf | 2026-11-04 |
| DOR Penalties and interest page (5% late-payment, 20% late-filing, 100% non-filer) | https://www.oregon.gov/DOR/programs/individuals/Pages/penalties.aspx | 2026-11-04 |
| Cherriots service-enhancements page (employer payroll tax starting 2027) | https://www.cherriots.org/service-enhancements/ | 2026-11-04 |

Unconfirmed against archived sources: the ORS/OAR citations, Frances
Online portal, and DCBS/OED notices listed below have no archived captures
and are therefore not confirmed sources.

- ORS Chapter 316 -- Personal Income Tax (withholding)
- ORS 657.435 -- new-employer base rate (chapter text archived; section note not)
- ORS 267.385 -- TriMet and LTD employer payroll tax escalator
- ORS 657B -- Paid Leave Oregon
- ORS 656.506 -- Workers' Benefit Fund
- ORS 670.600 -- Independent contractor definition
- ORS 652.140, 652.150 -- Final pay and penalty wages
- ORS 652.220 -- Pay Equity Act
- OAR 150-267-0020, 150-267-0030 -- TriMet/LTD allocation
- OAR 150-316-0290 -- OR-W-4 submission triggers
- OAR 471-070 -- Paid Leave Oregon implementation
- OED Frances Online portal -- replacement for OTTER (effective 2022)
- DCBS WBF assessment notice -- annual publication

### 14. Refusals

- **Public employer (PERS-covered)** -- The taxpayer is an Oregon public employer (PERS-covered) -- different regime
- **Agricultural employer ORS 657.045 exemption** -- The taxpayer is an agricultural employer seeking the ORS 657.045 exemption analysis without documented seasonal-worker facts  _(ORS 657.045)_
- **Tribal entity** -- The taxpayer is a federally-recognized tribal entity -- sovereignty defenses outside scope
- **Railroad employees** -- The request concerns railroad employees (federal RRA preempts state UI)
- **Maritime employees** -- The request concerns maritime employees on navigable waters
- **Multistate apportionment OR/WA dispute** -- The request concerns a multistate apportionment analysis where the primary work state is contested between Oregon and Washington under ORS 657.030 localization-of-work -- refer to multistate workflow  _(ORS 657.030)_

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
