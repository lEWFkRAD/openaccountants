---
name: md-payroll
description: Tier 2 Maryland content skill for employer payroll compliance covering tax year 2025. Includes the MD PIT brackets up to 6.50% state plus county tax 2.25-3.30%, MW507 state W-4, MW-506 filing categories, MD SUI wage base $8,500 with rates 0.30-7.50%, the 24-county + Baltimore City local tax structure (highest rate 3.30% in Dorchester County; 3.20% in most large jurisdictions), Maryland Healthy Working Families Act (Sick & Safe Leave 1 hour per 30 hours), reciprocal agreements with DC/PA/VA/WV exempting non-residents, and ABC contractor classification test.
jurisdiction: US-MD
tax_year: 2025
last_updated: 2026-11-02
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MD Payroll

## Who this applies to

This skill covers Maryland-specific payroll obligations for employers paying Maryland-resident employees or employing nonresidents who perform services in Maryland during tax year 2025. The skill addresses:

- Maryland personal income tax (PIT) withholding under Md. Code Ann., Tax-General §10-901 et seq.
- The stacked local income tax (county tax + Baltimore City) under Md. Code Ann., Tax-General §10-103 and §10-106
- Form MW507 (Employee's Maryland Withholding Exemption Certificate) and MW507M (military spouse)
- Form MW-506 (Employer's Return of Income Tax Withheld) and MW-508 (annual reconciliation)
- Maryland State Unemployment Insurance (SUI) under Md. Code Ann., Labor and Employment §8-101 et seq.
- The Maryland Healthy Working Families Act (Md. Code Ann., L&E §3-1301 et seq.)
- The Maryland Workplace Fraud Act ABC test for worker classification under Md. Code Ann., L&E §3-903
- Reciprocity agreements between Maryland and DC, PA, VA, and WV
- New hire reporting to the Maryland State Directory of New Hires
- Final pay rules under Md. Code Ann., L&E §3-505

OUT OF SCOPE: federal income tax withholding (see us-federal-payroll), federal FUTA, federal FICA, Maryland personal income tax filing for the employee (Form 502), Maryland corporate income tax, Maryland sales and use tax, Maryland Paid Family and Medical Leave Insurance (FAMLI) employer/employee premiums (deferred to a future revision when contributions commence under the current statutory schedule), and household employer special rules.

MUST be loaded alongside us-tax-workflow-base v0.2 or later. Maryland employers and Maryland-source wage income only.

## Rates, bands and thresholds

Maryland imposes a graduated state income tax under Tax-General §10-105. The state brackets for tax year 2025 are:

### Single, Married Filing Separately, Dependent Filer

**Single, Married Filing Separately, Dependent Filer**  _(Tax-General §10-105)_

| Taxable income over | But not over | State rate |
| --- | --- | --- |
| $0 | $1,000 | 2.00% |
| $1,000 | $2,000 | 3.00% |
| $2,000 | $3,000 | 4.00% |
| $3,000 | $100,000 | 4.75% |
| $100,000 | $125,000 | 5.00% |
| $125,000 | $150,000 | 5.25% |
| $150,000 | $250,000 | 5.50% |
| $250,000 | $500,000 | 5.75% |
| $500,000 | $1,000,000 | 6.25% |
| $1,000,000 | -- | 6.50% |

### Married Filing Jointly, Head of Household, Qualifying Surviving Spouse

**Married Filing Jointly, Head of Household, Qualifying Surviving Spouse**  _(Tax-General §10-105)_

| Taxable income over | But not over | State rate |
| --- | --- | --- |
| $0 | $1,000 | 2.00% |
| $1,000 | $2,000 | 3.00% |
| $2,000 | $3,000 | 4.00% |
| $3,000 | $150,000 | 4.75% |
| $150,000 | $175,000 | 5.00% |
| $175,000 | $225,000 | 5.25% |
| $225,000 | $300,000 | 5.50% |
| $300,000 | $600,000 | 5.75% |
| $600,000 | $1,200,000 | 6.25% |
| $1,200,000 | -- | 6.50% |

### Employer withholding tables

- **Employer withholding tables** -- For employer withholding the Comptroller publishes the 2025 Maryland Employer Withholding Guide (revision January 2025). The withholding tables embed both the state rate and the county rate so that an employer applies a single combined withholding rate based on the county entered on the employee's MW507. The 2025 guide also fixes the withholding allowance values: personal exemption $3,200 annually and standard deduction allowance $3,350 annually ($61.54 and $64.42 weekly).  _(2025 Maryland Employer Withholding Guide, archived)_

## The taxable base

Maryland is unusual among US states in that the "local" income tax is administered through the state withholding system and is mandatory in every jurisdiction. Every Maryland resident pays a local tax to one of 24 counties or to Baltimore City, in addition to the state tax. The rate is set annually by each county council and certified to the Comptroller. The local tax piggybacks on the same taxable income base used for the state tax.

### County / Baltimore City Tax Rates for 2025

**County / Baltimore City Tax Rates for 2025**  _(certified county rates 2025)_

| Jurisdiction | 2025 rate |
| --- | --- |
| Allegany County | 3.03% |
| Anne Arundel County | graduated: 2.70% / 2.94% / 3.20% (top rate 3.20%) |
| Baltimore City | 3.20% |
| Baltimore County | 3.20% |
| Calvert County | 3.20% |
| Caroline County | 3.20% |
| Carroll County | 3.03% |
| Cecil County | 2.74% |
| Charles County | 3.03% |
| Dorchester County | 3.30% |
| Frederick County | graduated: top rate 3.20% (3.20% at taxable net income $250,001 or more) |
| Garrett County | 2.65% |
| Harford County | 3.06% |
| Howard County | 3.20% |
| Kent County | 3.20% |
| Montgomery County | 3.20% |
| Prince George's County | 3.20% |
| Queen Anne's County | 3.20% |
| St. Mary's County | 3.20% |
| Somerset County | 3.20% |
| Talbot County | 2.40% |
| Washington County | 2.95% |
| Wicomico County | 3.20% |
| Worcester County | 2.25% |

Source: Comptroller 2025 Resident (Form 502) booklet local tax rate chart, read 2026-11-01.

- **Lowest/highest county rates and graduated brackets** -- The lowest county rate is Worcester at 2.25%; the highest is Dorchester at 3.30%, with 3.20% in most large jurisdictions (Howard, Montgomery, Prince George's, Baltimore City, Baltimore County, Caroline, Calvert, Kent, Queen Anne's, St. Mary's, Somerset, Wicomico and the top brackets of Anne Arundel and Frederick). Anne Arundel County and Frederick County adopted graduated local brackets; for withholding purposes the top marginal local rate is used unless the employee provides the lower-bracket certification on the MW507 worksheet.  _(MW507 worksheet; 2025 county rate chart)_

### Special Nonresident Tax

- **Special Nonresident Tax** -- Under Tax-General §10-106.1, an individual who is subject to the State income tax but not to the county income tax pays a "Special Nonresident Tax" in lieu of the county tax. The statutory rate equals the lowest county income tax rate set by any Maryland county for the year -- 2.25% for 2025 (Worcester County). It applies to wages earned in Maryland by: - Pennsylvania residents earning wages in Maryland (who are exempt from the state portion under reciprocity but remain liable for this local-rate withholding unless they qualify under MW507 Line 6 or Line 7 -- see the MD-PA section below) - Residents of any state with no reciprocity agreement with Maryland  _(Tax-General §10-106.1, archived)_ Residents of DC, Virginia, and West Virginia working in Maryland are exempt from Maryland withholding altogether (state tax and the 2.25% special nonresident tax) under reciprocity, by certifying nonresidence on MW507 Line 4.

> AUDIT FLASH POINT -- missed local/county withholding. The single most common audit finding by the Comptroller of Maryland's Compliance Division is failure to withhold the county component. An employer who treats Maryland income tax as the top state rate only (6.50%) and ignores the 2.25–3.30% local stack under-withholds by roughly a third to a half of the actual liability. The Comptroller assesses the difference against the employer under Tax-General §13-704, plus interest under §13-604 (11.4825% per annum for periods after December 31, 2024, per the Comptroller's 2024 corporate booklet; 10.8133% per annum for 2025 balances paid during 2026, per the 2025 Form 502 booklet) plus a §13-701(a) penalty of up to 10%. Always verify that the withholding table used reflects the county entered on the employee's MW507, not just "Maryland".

> AUDIT FLASH POINT -- wrong county selected. Each employee enters their county of residence (or Baltimore City -- which is NOT part of Baltimore County and must be selected separately) on the MW507 address line; nonresidents enter the Maryland county where employed. An employer that defaults all employees to the employer's county (e.g., Baltimore City because that is where the office sits) when employees actually live in lower-rate counties (e.g., Worcester at 2.25%) overcollects from the employee; the inverse undercollects. The MW507 county entry is the controlling document -- keep the signed original in the employee file for at least 3 years (the guide's record-retention period).

### MW507 -- Employee's Maryland Withholding Exemption Certificate

Form MW507 is the Maryland equivalent of the federal Form W-4. Every new hire must complete it. Per the archived 2025 Form MW507:

- Line 1: total number of personal exemptions claimed. For 2025 the exemption value is $3,200, reduced to $1,600 (single/MFS) for federal AGI $100,000-$125,000 and $800 for $125,000-$150,000, to $0 above $150,000; joint/HOH phase down one step later ($1,600 at $150,000-$175,000, $800 at $175,000-$200,000, $0 above $200,000). Employees expecting AGI over $100,000 (single/MFS) or $150,000 (joint/HOH) must complete the Personal Exemption Worksheet on page 2.
- Line 2: additional withholding amount per pay period.
- Line 3: full exemption from withholding where the employee owed no Maryland tax and was entitled to a full refund last year AND expects the same this year. If claimed, a new certificate is due by February 15 of the following year.
- Line 4: certification of nonresidence for employees domiciled in DC, Virginia, or West Virginia who work in Maryland and do not maintain a place of abode in Maryland for 183 days or more -- full exemption from Maryland withholding.
- Line 5: employees domiciled in Pennsylvania working in Maryland (same 183-day condition) -- exempt from the Maryland STATE portion only; they remain liable for withholding at the rate of the Maryland county where employed unless Line 6 or Line 7 applies.
- Line 6: Pennsylvania residents living in a local Pennsylvania jurisdiction within York or Adams counties -- exempt from Maryland LOCAL tax.
- Line 7: Pennsylvania residents living in a local Pennsylvania jurisdiction that does not impose an earnings or income tax on Maryland residents -- exempt from Maryland LOCAL tax. Employees exempt under Line 6 or 7 also write "EXEMPT" on Line 4.
- Line 8: military-spouse exemption under the Servicemembers Civil Relief Act as amended by MSRRA -- enter state of domicile, attach Form MW507M and a copy of the spousal military identification card.
- Address block: county of residence; nonresidents enter the Maryland county (or Baltimore City) where employed.

Statutory-resident trap: an individual domiciled in DC, Pennsylvania, or Virginia who maintains a place of abode in Maryland for 183 days or more becomes a Maryland statutory resident and is taxed as a resident. An individual domiciled in West Virginia is not required to pay Maryland income tax on wage or salary income regardless of time spent in Maryland.

The employer must forward the certificate to the Compliance Division when the employer has reason to believe it is incorrect, more than 10 exemptions are claimed, the Line 3 no-liability exemption is claimed and wages exceed $200 a week, exemption is claimed on nonresidence, or MSRRA exemption is claimed. A continuing employee who changes county of residence may submit a new MW507 mid-year and the employer must apply the new county rate beginning with the next pay period.

### MW507M -- Military Spouses Residency Relief Act

- **MW507M requirements** -- Form MW507M implements the federal Military Spouses Residency Relief Act (MSRRA) as amended by the Veterans Auto and Education Improvement Act of 2022. A military spouse who is physically present in Maryland solely because of a service member's military orders, and who is a domiciliary of a state other than Maryland, may elect to be exempt from MD income tax withholding by filing MW507M annually with proof of: - the service member's current orders - the spouse's out-of-state driver's license or voter registration (proof of non-MD domicile) - a copy of the service member's most recent LES The 2022 federal amendment allows the spouse to choose the service member's state of legal residence even if the spouse never lived there. The employer keeps MW507M on file; the employee files no Maryland return.  _(50 U.S.C. §4001 (Servicemembers Civil Relief Act -- MSRRA basis); MW507 instructions, archived)_

## Deadlines and filing

Employers report and remit withheld Maryland income tax on Form MW-506. The deposit/return frequency depends on the prior period's withholding total, per the 2025 Employer Withholding Guide:

**Employer filing category table**  _(2025 Employer Withholding Guide, read 2026-11-01)_

| Prior period MD withholding | Deposit frequency | Return due dates |
| --- | --- | --- |
| Less than $250 withheld per calendar year | Annual | Last day of January following the year |
| Less than $700 withheld per quarter | Quarterly | 15th day of the month following each quarter (April 15, July 15, October 15, January 15) |
| More than $700 withheld in any one quarter | Monthly | 15th day of the following month |
| $15,000 or more withheld for the preceding calendar year | Accelerated (remit within 3 business days of any payday with $700 or more accumulated withholding; monthly-waiver available) | per accelerated schedule |
| New employer (first year) | Quarterly default | quarterly |

- **Electronic filing and zero returns** -- MW-506 returns should be filed electronically through the Comptroller's bFile system; even if no tax was withheld in a period, a zero return must be filed.  _(2025 Employer Withholding Guide)_
- **MW-508 annual reconciliation** -- The annual reconciliation, Form MW-508, is due January 31 of the following year and transmits the Form W-2 for each employee with Maryland wages or withholding. For 2025 wages the MW-508 is due January 31, 2026. Employers filing fewer than 25 W-2s/1099s attach MW508CR to the paper MW508; accelerated filers use MW508A.  _(2025 Employer Withholding Guide, archived)_

> AUDIT FLASH POINT -- frequency change not noticed. The Comptroller sets each employer's deposit frequency from the look-back period and notifies the employer; the new frequency takes effect January 1. An employer that crosses the $15,000 threshold and continues to file quarterly into the next year accrues underpayment penalties even if all tax is ultimately paid. Check the Comptroller's frequency notice and update the payroll calendar before January 1.

### Maryland SUI (State Unemployment Insurance)

Maryland Unemployment Insurance is administered by the Maryland Department of Labor, Division of Unemployment Insurance under L&E Title 8.

### 2025 Parameters

- **Taxable wage base** -- $8,500 per employee per calendar year  _(L&E §8-607(b)(1), archived)_
- **Standard contribution rate range** -- 0.30% to 7.50% (Table A, 2025)  _(Maryland DOL 2025 Tax Rate Table, archived)_
- **New employer rate** -- assigned by the Division within a range of 1.0% to 2.6%; the archived 2025 DOL rate table lists 2.60% for new employers  _(Maryland DOL UI tax-rate page and 2025 Tax Rate Table, archived)_
- **No separate construction new-employer rate** -- the 2025 DOL rate table assigns new employers 2.60%; 5.40% is simply the Table A rate for an employer ratio of .0433-.0459, not a new-employer assignment  _(Maryland DOL 2025 Tax Rate Table, archived)_
- **Foreign contractor rate** -- a construction-industry contractor headquartered in another state pays the average rate for the construction industry in Maryland, never lower than the new-employer rate in effect; the 2025 DOL rate table lists the foreign contractor rate at 2.60%  _(Maryland DOL UI tax-rate page and 2025 Tax Rate Table, archived)_
- **Work Sharing program** -- Work Sharing program: available; affects experience rating  _(Md. Code Ann., Labor and Employment Title 8)_
- **Rate table in effect** -- the archived Maryland DOL "Tax Rate Table 2025" is Table A (rates 0.30%-7.50% by employer benefit ratio)  _(Maryland DOL 2025 Tax Rate Table, archived)_

### Reporting

Quarterly wage reports (Form DLLR/DUI 15) and contribution reports (Form DLLR/DUI 16) are filed with contribution payments, which are due:

**Quarterly contribution report due dates**  _(Maryland DOL UI assessment FAQ, archived)_

| Quarter | Wages reported | Due date |
| --- | --- | --- |
| Q1 | January–March | April 30 |
| Q2 | April–June | July 31 |
| Q3 | July–September | October 31 |
| Q4 | October–December | January 31 |

- **Registration thresholds** -- All employers with 1+ employee in 20+ weeks of a calendar year, or who paid $1,500+ in any calendar quarter, must register and file. Domestic employers are subject to a $1,000-per-quarter test. Agricultural employers have the $20,000-per-quarter or 10-employees-in-20-weeks test.  _(Md. Code Ann., Labor and Employment Title 8 -- see Not yet confirmed below)_
- **BEACON portal, late penalties** -- Contribution reports and payments are filed through the Maryland Unemployment Insurance Portal (BEACON) by ACH credit or ACH debit. When quarterly reports and payments are missed, the Division sends a Delinquency Notice; unresolved items become an Assessment Notice with 30 days to pay. Interest accrues at 1.5% per month on the late contribution payment, and penalties are charged at $35 per quarter past due. Interest and penalty waivers and payment plans can be requested in BEACON.  _(Maryland DOL UI assessment FAQ, archived)_

## Penalties and interest

- **Withholding penalties** -- An employer who fails to file returns or remit amounts collected as required is subject to a penalty not to exceed 25% of the unpaid tax; a dishonored payment instrument draws a $30 service charge; willful failure to provide an income tax statement, or a false withholding statement, draws a $50 penalty per violation; willful failure to file, withhold, or pay can be a criminal offense (up to $10,000 and/or 5 years).  _(2025 Employer Withholding Guide, archived)_
- **Failure to pay** -- Tax-General §13-701(a): failure to pay a tax when due draws a penalty not exceeding 10% of the unpaid tax.  _(Tax-General §13-701, archived)_
- **Interest** -- §13-604: 11.4825% per annum for periods after December 31, 2024 (Comptroller 2024 corporate booklet); 10.8133% per annum for 2025 balances paid during 2026 (2025 Form 502 booklet).  _(archived)_
- **UI late reports/payments** -- $35 per quarter past due plus 1.5% per month interest; waivers requestable in BEACON.  _(Maryland DOL UI assessment FAQ, archived)_
- **Misclassification** -- knowing misclassification: civil penalty up to $10,000 per misclassified employee (L&E §3-909(a)); doubled for a prior violation; up to $20,000 per employee after three or more violations (§3-909(e)).  _(L&E §3-909, archived)_
- **New hire reporting** -- written warning for a first violation, then $20 for each month a subsequent violation continues, or $500 where the failure results from a conspiracy between employer and employee (L&E §8-626.1).  _(L&E §8-626.1, archived)_
- **Employer liability for un-withheld tax** -- where a worker is reclassified or withholding was missed, the employer is liable for the under-withheld income tax (Tax-General §10-906) plus the penalties and interest above.

## Cross-border points

Maryland has bilateral wage-tax reciprocity with four neighboring jurisdictions. Under reciprocity an employee who is a resident of one state but works in the other pays income tax only to their state of residence; the employer withholds only for the employee's state of residence.

### MD–DC Reciprocity

- **MD-DC reciprocity terms** -- Under the long-standing administrative agreement between MD and DC: - A Maryland resident working in DC pays only Maryland income tax. The DC employer should not withhold DC tax; the MD employee files a DC Form D-4A and the MD W-2 reflects MD withholding only. - A DC resident working in Maryland pays only DC income tax. The MD employer should withhold DC tax (not MD state tax and not MD county tax). The DC resident completes MW507 Line 4 certifying nonresidence. Note: DC does not have local/county tax, so MD residents working in DC owe only the MD state-plus-county stack to MD.  _(MW507 instructions, archived)_

### MD–PA Reciprocity

- **MD-PA reciprocity terms** -- The MD–PA agreement is the most nuanced of the four because PA's flat 3.07% state tax and PA local Earned Income Tax (EIT) rates interact differently: - A PA resident working in MD completes MW507 Line 5 and is exempt from the Maryland STATE portion, but is still liable for Maryland local withholding at the rate of the Maryland county where employed (the 2.25% special nonresident rate for 2025) -- unless the PA resident lives in a local jurisdiction within York or Adams counties (Line 6) or in a PA local jurisdiction that does not impose an earnings or income tax on Maryland residents (Line 7), in which case the local withholding is also exempt. - A MD resident working in PA: exempt from PA state tax; the PA employer should not withhold PA state tax. The MD resident files PA Form REV-419. The MD resident is still subject to PA local EIT in the PA work location, withheld by the PA employer.  _(MW507 instructions, archived)_

### MD–VA Reciprocity

- **MD-VA reciprocity terms** -- - A VA resident working in MD: exempt from MD state tax and the MD 2.25% special nonresident tax. The employee completes MW507 Line 4 certifying nonresidence (and must not maintain a Maryland abode for 183 days or more, or statutory-residency rules apply). Employer withholds VA tax instead. - A MD resident working in VA: exempt from VA state tax. File VA Form VA-4.  _(MW507 instructions, archived)_

### MD–WV Reciprocity

- **MD-WV reciprocity terms** -- Same structure as MD–VA. A WV resident working in MD completes MW507 Line 4 and the employer withholds WV state tax; a WV domiciliary is not required to pay Maryland income tax on wages regardless of time spent in Maryland. A MD resident working in WV files WV/IT-104R.  _(MW507 instructions, archived)_

### Reciprocity Does Not Override Local Withholding for Residents

- **Residents remain liable for full MD stack** -- Reciprocity only relieves the nonresident from the work-state's tax. A Maryland resident remains liable for the full MD state-plus-county stack on all wages regardless of where earned. An employer with a Maryland resident working remotely from PA must still withhold the MD state tax PLUS the MD county tax for the employee's MD county of residence.

> AUDIT FLASH POINT -- multi-state employee, multi-county allocation. An employee who lives in Howard County (3.20%), works two days a week in the DC office, two days a week in the Tysons Corner VA office, and one day a week remotely from a Pennsylvania family cottage requires very careful sourcing. The full wages are subject to MD state tax plus Howard 3.20% (because the employee is an MD resident); none of those wages are sourced to DC, VA, or PA (because of MD's reciprocal agreements with each). However, if the employee establishes a tax home outside MD or changes residence mid-year, the analysis flips. Keep contemporaneous time-and-location records for any employee who routinely works from more than one state.

### ABC Test for Worker Classification

- **ABC test scope** -- The Maryland Workplace Fraud Act (Md. Code Ann., L&E §3-901 through §3-920) imposes an ABC test for classifying workers in the construction services and landscaping industries. For unemployment insurance purposes statewide (under L&E §8-205), Maryland applies a similar but broader ABC test that resembles California's AB-5 framework.  _(Md. Code Ann., L&E §3-901 through §3-920; L&E §8-205, archived)_
- **Three-prong ABC test** -- A worker is presumed to be an employee unless the putative employer can prove ALL THREE: - (A) the worker is free from control and direction of the hiring entity in connection with the performance of the work, both under the contract and in fact; - (B) the work is outside the usual course of the hiring entity's business OR the work is performed outside all of the hiring entity's places of business; AND - (C) the worker is customarily engaged in an independently established trade, occupation, profession, or business of the same nature as the work performed. Prongs A and C track the common-law right-to-control test and the IRS Section 530 safe harbor. Prong B is the strictest -- it disqualifies most "core function" subcontractors. A software development firm that hires a "contractor" software developer to write code for the firm's product fails prong B because writing code IS the usual course of the firm's business. The worker is an employee under MD unemployment insurance rules regardless of contract language.  _(Md. Code Ann., L&E §3-901 through §3-920; L&E §8-205, archived)_
- **Misclassification penalties** -- a knowing misclassification draws a civil penalty of up to $10,000 per misclassified employee (L&E §3-909(a)); the penalty is doubled for a prior violation, and up to $20,000 per employee may be assessed after three or more violations (§3-909(e)).  _(L&E §3-909, archived)_

### Independent Contractor Affidavit (Construction)

- **Affidavit requirements** -- For construction services only, the Workplace Fraud Act prescribes a specific written form -- the Independent Contractor Affidavit -- that the worker and employer must execute and that the employer must retain for 3 years (L&E §3-906). The affidavit does not by itself satisfy the ABC test; it is documentary evidence that the parties intended an independent contractor relationship but the substantive ABC test still controls.  _(L&E §3-906)_

> AUDIT FLASH POINT -- ABC contractor misclassification. The Maryland DOL Joint Enforcement Task Force on Workplace Fraud cross-references 1099-NEC filings with UI wage records. A 1099-NEC issued by an MD employer to a worker who fails the ABC test triggers an audit with retroactive UI contributions, MD income tax withholding back-assessments (the employer is liable for the under-withheld tax under Tax-General §10-906), workers' compensation premiums, and the L&E §3-909 civil penalty. Never accept "they signed a contractor agreement" as a defense -- the substantive ABC test is dispositive.

### Maryland Healthy Working Families Act (Sick & Safe Leave)

- **General requirement** -- The Maryland Healthy Working Families Act (L&E §3-1301 et seq.) requires nearly every employer to provide earned sick and safe leave to employees who work at a Maryland worksite.  _(Md. Code Ann., L&E §3-1301 et seq., archived)_

### Coverage and Accrual

- **Coverage, accrual, caps, carryover** -- - All employers with 1+ employee must provide leave; the difference is whether the leave is PAID or UNPAID. - Employers with 15 or more employees (counted as the average number of monthly employees in the immediately preceding year, including FT, PT, temporary, and seasonal workers) must provide PAID leave; employers with 14 or fewer employees must provide UNPAID leave (L&E §3-1304(a)). - Accrual rate: at least 1 hour of leave per 30 hours worked (L&E §3-1304(b)). - Annual accrual cap: the employer need not allow more than 40 hours to be earned in a year; annual use cap: 64 hours; total accrual cap: 64 hours at any time (L&E §3-1304(c)). - The employer may front-load the full annual amount at the beginning of the year instead of accruing it (L&E §3-1304(d)). - Leave need not be usable during the employee's first 106 calendar days (L&E §3-1304(c)(4)); unused leave reinstates on rehire within 37 weeks (L&E §3-1304(h)).  _(Md. Code Ann., L&E §3-1304, archived)_

### Eligibility

- **Eligibility criteria** -- - Employees who regularly work at least 12 hours a week (employees regularly working fewer than 12 hours a week are excluded, L&E §3-1302). - The law is worksite-location based: it covers employees working at a Maryland worksite.  _(Md. Code Ann., L&E §3-1302, archived)_

### Permissible Uses

- **Permissible uses of leave** -- - The employee's or family member's mental or physical illness, injury, or condition - Preventive medical care for the employee or a family member - Maternity or paternity leave - Absence due to domestic violence, sexual assault, or stalking against the employee or family member "Family member" is broadly defined to include spouse, child (biological, adopted, foster, step), parent, grandparent, grandchild, sibling, and the spouses of those relations.  _(Md. Code Ann., L&E §3-1305, archived)_

### Excluded Workers

- **Excluded worker categories** -- - Employees who regularly work less than 12 hours per week - Independent contractors (genuine contractors that pass the ABC test) - Workers under 18 - Construction workers covered by a bona fide collective bargaining agreement that expressly waives the act - Certain seasonal/agricultural and as-needed health/human services workers  _(Md. Code Ann., L&E §3-1302, archived)_

### Documentation

- **Documentation requirements** -- - An employer must provide written notice of the policy to employees. - Each pay statement must show the amount of sick and safe leave available. - Records of accrual and use must be kept for at least 3 years.  _(Md. Code Ann., L&E §3-1301 et seq.)_

### Final Pay and Sick Leave Payout

- **Sick leave payout at termination** -- Maryland does NOT require payout of accrued unused sick and safe leave at termination, unlike vacation/PTO, which IS subject to payout under Md. Code Ann., L&E §3-505 if the employer's written policy treats vacation as wages.  _(Md. Code Ann., L&E §3-505)_

### Final Pay Rules

- **Final pay timing and rules** -- Md. Code Ann., L&E §3-505 requires that an employer pay all wages due to a separated employee "on or before the day on which the employee would have been paid the wages if the employment had not been terminated." In practice this is the next regular payday. - Voluntary quit: next regular payday. - Involuntary termination: next regular payday. - Accrued vacation/PTO: payable as wages IF the employer's written policy does not contain a forfeiture clause and IF the employer's practice treats it as earned wages. See Catapult Learning, LLC v. Comptroller (Md. App. 2011) for the leading case. - Accrued sick & safe leave: not payable on separation (statutory carve-out). Late payment of final wages can give rise to treble damages under L&E §3-507.2 if the failure to pay was not the result of a bona fide dispute.  _(Md. Code Ann., L&E §3-505, §3-507.2)_

### New Hire Reporting

- **New hire reporting requirements** -- Under L&E §8-626.1 and Federal PRWORA, Maryland employers must report new hires (and rehires after a 60-day separation) to the Maryland State Directory of New Hires within 20 days of the hire date. - Reporting agency: Maryland State Directory of New Hires (administered by the Maryland Department of Human Services -- DHS -- Child Support Administration; historically referred to as DHR) - Information required: employee name, address, SSN, hire date, employer name, employer FEIN, employer address - Methods: online at MD-newhire.com, electronic file upload, magnetic media, or W-4 facsimile - Penalty: written warning for a first violation, then $20 for each month a subsequent violation continues, or $500 where the failure results from a conspiracy between employer and employee (L&E §8-626.1) Multi-state employers may elect to report all new hires to a single state under 42 U.S.C. §653a -- file the multistate election with the federal Office of Child Support Enforcement.  _(L&E §8-626.1, archived; 42 U.S.C. §653a)_

## Worked examples

### Worked example 1: Baltimore City restaurant, single Maryland-resident employee

Facts: Acme Crab Cakes LLC operates a restaurant in Baltimore City. It hires Jamal, a single Maryland resident living in Baltimore City, in March 2025 at $52,000/year ($1,000/week gross). Jamal files MW507 claiming 1 personal exemption on Line 1 and enters "Baltimore City" as his county. No additional withholding on Line 2.

Annualized estimate of Jamal's 2025 Maryland state plus Baltimore City tax (the Comptroller's weekly withholding table produces a slightly different figure; this shows the mechanics):

```oa-check
name: MD payroll Jamal Baltimore City 2025
inputs:
 wages: 52000
 exemption: 3200
 std: 3350
 local_rate: 0.032
steps:
 - tni: wages - exemption - std
 - state_tax: 90 + 0.0475 * (tni - 3000)
 - local_tax: tni * local_rate
 - total: state_tax + local_tax
 - weekly: round(total / 52 * 100) / 100
expected:
 tni: 45450.00
 state_tax: 2106.38
 local_tax: 1454.40
 total: 3560.78
 weekly: 68.48
```

Step by step: the 2025 withholding allowance values are one personal exemption of $3,200 (federal AGI below the phase-down threshold) and a $3,350 standard deduction allowance, both from the 2025 Employer Withholding Guide. Maryland taxable income = $52,000 − $3,200 − $3,350 = $45,450. State tax = $90 (the 2%/3%/4% brackets on the first $3,000) + 4.75% × $42,450 = $2,106.38. Baltimore City tax = 3.20% × $45,450 = $1,454.40. Total = $3,560.78, about $68.48 per weekly pay period.

Other obligations for Jamal:

1. Federal: handled by federal payroll skill -- outside this scope.
2. SUI: Acme's 2025 new-employer rate is 2.60% (top of the 1.0%-2.6% new-employer range; the DOL 2025 rate table lists 2.60%). Wage base $8,500 means SUI is owed only on the first $8,500 of Jamal's 2025 wages, i.e., $221.00 of SUI for Jamal's first 8.5 weeks; nothing further for the rest of 2025. Reported on DLLR/DUI 15/16 quarterly.
3. Sick & safe leave: Acme has 22 employees so it must provide PAID leave. Jamal accrues 1 hour per 30 hours worked. At 40 hours/week he accrues 40 × (1/30) = 1.333 hours per week, capped at 40 hours earned per year. The pay statement must show available hours.
4. New hire reporting: Acme submits Jamal's data to MD-newhire.com within 20 days of his start date.
5. MW-506: assume Acme is a new employer in 2025 -- quarterly default. First MW-506 covering Q1 2025 is due April 15, 2025 (quarterly returns are due the 15th day of the month following the quarter). Annual MW-508 + W-2s due January 31, 2026.

### Worked example 2: Montgomery County employer with Northern Virginia commuters

Facts: BioWidget Inc., a biotech company headquartered in Bethesda (Montgomery County, MD), employs three workers:

- Priya: lives in Rockville, MD (Montgomery County). Salary $120,000.
- Sam: lives in Arlington, VA. Salary $110,000. Commutes to Bethesda 5 days/week.
- Kavita: lives in Fairfax, VA. Salary $130,000. Hybrid -- 3 days in Bethesda, 2 days remote from her Fairfax home.

Treatment:

Priya -- full MD state + Montgomery County tax. At roughly $113,450 of Maryland taxable income ($120,000 less the $3,200 exemption and $3,350 standard deduction) her marginal state bracket is 5.00% ($100,001-$125,000), so the combined marginal rate is 5.00% + 3.20% = 8.20%; the 5.75% bracket starts only above $250,000 of Maryland taxable income. Standard MW507 with county entry "Montgomery County". Full state and county withholding on all wages.

Sam -- VA resident commuting to MD. MD has full reciprocity with VA. Sam completes MW507 Line 4 certifying Virginia domicile and no Maryland abode of 183+ days, and BioWidget registers as a VA employer to withhold Virginia state tax on Sam's wages. NO MD state tax, NO MD county tax, NO MD 2.25% special nonresident tax.

Kavita -- same as Sam. The two days Kavita works remotely from VA are VA-sourced, and the three days in Bethesda are MD-sourced. Because of MD-VA reciprocity, the MD-sourced wages are STILL exempt from MD tax -- MW507 Line 4 exempts a VA domiciliary's Maryland wages from Maryland withholding entirely. BioWidget withholds 100% VA tax on Kavita's wages just as for Sam. Note: this is different from non-reciprocal multi-state scenarios where day-counting matters; with MD-VA reciprocity it is residency, not work-location-day-count, that controls.

If Kavita establishes residency in MD mid-year (e.g., moves to Bethesda in September), BioWidget must:
- Stop VA withholding effective the move date.
- Begin MD state + Montgomery County withholding effective the move date.
- Obtain an updated MW507 from Kavita with county entry "Montgomery County".
- Issue a 2025 W-2 with VA wages and tax for January–August, plus MD wages and tax for September–December (or, more practically, allocate based on the actual paydays after the move).

> AUDIT FLASH POINT -- multi-county work-day allocations. The trap here is that MD-VA reciprocity makes day-counting irrelevant, but if Kavita instead lived in a non-reciprocal state (say, Delaware) and worked the same 3-MD/2-DE schedule, BioWidget would need to:
> (a) withhold MD state tax + 2.25% MD special nonresident tax on the 3-MD-day portion (60% of wages), and
> (b) withhold Delaware tax on the full wages (because DE taxes residents on worldwide income), with a credit-side reconciliation on Kavita's DE return.
> Always confirm reciprocity status BEFORE setting up withholding; don't generalize from one employee to another.

### Worked example 3: construction contractor "independent contractor" reclassification (ABC test)

Facts: Charm City Builders LLC, an MD construction firm based in Towson (Baltimore County), pays Diego, a drywall installer, $4,500/month on a 1099-NEC. Diego works 40 hours/week exclusively for Charm City for 11 months in 2025. Charm City supplies the tools, sets the work schedule, supplies the materials, and Diego does not advertise his services or have other clients.

Workplace Fraud Act analysis:

- Prong A (free from control): FAILS. Charm City sets schedule, supplies tools, supervises.
- Prong B (outside usual course or outside places of business): FAILS. Drywall is in the usual course of Charm City's business; work is performed at Charm City's jobsites.
- Prong C (independently established trade): FAILS. No other clients, no advertising.

Diego fails all three prongs. He is an EMPLOYEE under MD law regardless of contract language or his preference.

Consequences for Charm City:

1. Retroactive MD income tax withholding liability under Tax-General §10-906 -- Charm City is liable for the under-withheld tax. Assuming Diego is a Baltimore County resident, his marginal rate at this wage level is 4.75% + 3.20% = 7.95% (the 4.75% bracket runs to $100,000 of Maryland taxable income; the 5.75% bracket starts only at $250,001, so 8.95% combined applies far above his wages).
2. Retroactive SUI contributions on Diego's wages up to the $8,500 wage base. At the 2.60% new-employer rate in the DOL 2025 table, the catch-up is $221.00 plus 1.5% per month interest on unpaid contributions.
3. Civil penalty under L&E §3-909(a) of up to $10,000 per misclassified employee for a first knowing violation.
4. Workers' compensation: separate exposure under Md. Code Ann., L&E Title 9 -- Charm City should have been carrying WC coverage for Diego. The Workers' Compensation Commission can assess additional penalties.
5. Federal exposure: 1099-NEC issued in error triggers IRS Section 530 examination and potential FICA, FUTA, and federal income tax under-withholding assessment.
6. Diego's perspective: he can sue for unpaid overtime, sick & safe leave that should have accrued (Charm City has 15+ employees so PAID sick leave), unemployment benefits if separated, and treble damages under L&E §3-507.2 for any unpaid wages.

Remediation: Charm City should reclassify Diego as a W-2 employee going forward, issue corrected payroll records, file Form W-2c if a W-2 was issued for any prior period (none here -- only 1099-NEC), file VCSP (Voluntary Classification Settlement Program) with the IRS, and self-disclose to the Comptroller of Maryland for a potentially reduced penalty. Consider whether other 1099-NEC workers in the same role need the same treatment.

> AUDIT FLASH POINT -- ABC misclassification cascades. Misclassification of a single worker almost never stays isolated. The MD DOL audit team will demand a list of all 1099-NEC payments and apply the ABC test to each. Companies routinely settle MD payroll audits for 5–15× the cost of the original under-withholding because of the layered penalties (UI + income tax + workers' comp + civil penalty + interest).

### Self-Checks Before Sign-Off

Before delivering a Maryland payroll computation or compliance memo to a reviewer, confirm each of the following:

1. Is the employer's MD Central Registration Number (CRN) and FEIN on file for both withholding and UI?
2. Has every employee submitted an MW507 with a county entry (residence, or Maryland county of employment for nonresidents)?
3. Are any MW507 Lines 3/4/5/6/7/8 exemption claims current for the year (annual renewal)?
4. Has the Comptroller's deposit-frequency notice been reviewed for the upcoming calendar year?
5. For employees in PA, VA, WV, or DC: has the corresponding state's withholding form been filed and is the MD-side withholding properly zeroed out (PA: only the state portion)?
6. For employees who moved counties or states mid-year: has the effective-date change been applied at the correct pay period?
7. For any 1099-NEC payments: has each been tested against the three-prong ABC test and documented?
8. Sick & safe leave: is the available balance shown on every pay statement and is the carryover correctly calculated?
9. For a new hire: has the report been transmitted to MD-newhire.com within 20 days?
10. Is the Q4 2025 MW-508 + W-2 reconciliation calendar set for January 31, 2026?

## Ask the client first

- **Refusals list** -- This skill will NOT: - Provide federal income tax, FICA, or FUTA computations (refer to us-federal-payroll). - Compute Maryland income tax for the EMPLOYEE's Form 502 (refer to md-income-tax). - Cover Maryland Paid Family and Medical Leave Insurance (FAMLI) premiums until the contribution schedule is finalized in regulation. - Cover Maryland household employer special rules. - Cover multi-state UI Localization-of-Work analyses where the employee works in 3+ states (refer to a credentialed cross-border payroll specialist). - Substitute for credentialed reviewer sign-off under Circular 230 or under Maryland Board of Individual Tax Preparers oversight.  _(Skill scope definition)_

<!-- openaccountants-cta-block -->

## Common mistakes
- Treating county tax as optional or remitting it to the state alone.
- Treating PA residents as fully exempt from Maryland withholding: Line 5 exempts only the state portion; local withholding at the employment-county rate continues unless Line 6 or Line 7 applies.
- Using MW507 Line 8 (military spouse) for DC/VA/WV commuters -- Line 4 is the nonresidence certification.
- Forgetting the 183-day statutory-residency trap for DC/PA/VA domiciliaries with a Maryland abode.
- Continuing quarterly MW-506 deposits after crossing the $15,000 look-back threshold.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Md. Code, Tax-General § 10-105 (rate schedules) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false | 2026-10-28 |
| Md. Code, Tax-General § 10-106 (county income tax) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-106&enactments=false | 2026-10-28 |
| Md. Code, Tax-General § 10-106.1 (special nonresident tax rate) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-106.1&enactments=false | 2026-11-02 |
| Md. Code, Tax-General § 10-301 (taxable-year definitions) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-301&enactments=false | 2026-10-28 |
| Md. Code, Tax-General § 11-203 (credit for tax paid to other states) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gti&section=11-203&enactments=false | 2026-10-28 |
| Md. Code, Tax-General § 13-701 (failure-to-pay penalty up to 10%) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=13-701&enactments=false | 2026-11-02 |
| Md. Code, Labor & Employment § 3-909 (misclassification penalties) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gle&section=3-909&enactments=false | 2026-11-01 |
| Md. Code, Labor & Employment § 8-607 (UI wage base, foreign contractor) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gle&section=8-607&enactments=false | 2026-11-01 |
| Md. Code, Labor & Employment § 8-626.1 (new hire reporting) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gle&section=8-626.1&enactments=false | 2026-11-01 |
| Md. Code, Labor & Employment § 8-205 (ABC test for UI) | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=le&section=8-205&enactments=false | 2026-11-01 |
| Comptroller, 2025 Maryland Employer Withholding Guide (filing categories, MW508 due date, allowance values, penalties) | https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/instructions/withholding/2025/Withholding-Guide.pdf | 2026-11-01 |
| Comptroller, 2025 Resident (Form 502) booklet (county rate chart, 10.8133% interest) | https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf | 2026-11-01 |
| Comptroller, 2025 Nonresident (Form 505) booklet | https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/nonresident-booklet.pdf | 2026-11-01 |
| Comptroller, 2024 Corporate (Form 500) booklet (11.4825% interest after 12/31/2024) | https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/instructions/2024/Corporate-Booklet.pdf | 2026-11-02 |
| Maryland DOL, UI tax rate page (new employer 1.0%-2.6%, foreign contractor) | https://labor.maryland.gov/unemployment-insurance/employer-agent/tax-rate.shtml | 2026-11-01 |
| Maryland DOL, UI Tax Rate Table 2025 (Table A, new employer 2.60%, foreign contractor 2.60%) | https://labor.maryland.gov/unemployment-insurance/employer-agent/tax-rate-table.shtml | 2026-11-01 |
| Maryland DLS, certified county local income tax rates | https://dls.maryland.gov/pubs/prod/NoPblTabPDF/2026CountyLocalTaxRates.pdf | 2026-11-01 |

Statutes and forms relied on in the body (archived copies on file): Md. Code Ann., Tax-General §10-103 through §10-106.1; §10-901 through §10-913; §13-604, §13-701, §13-704; COMAR 03.04.01.04; Md. Code Ann., Labor and Employment Title 8, §3-505, §3-507.2, §3-901 through §3-920, §3-1301 through §3-1311, §8-626.1; Form MW507 (2025); 42 U.S.C. §653a; 50 U.S.C. §4001.

Not yet confirmed: the $100-per-W-2 / $50,000-annual-cap MW-508 penalty (the Comptroller knowledge base ties W-2 penalties to Tax-General §13-706, not §13-701, and the figures were not found in archived sources); the UI employer coverage/registration tests ($1,500 per quarter, 20 weeks, $1,000 domestic, $20,000/10 workers agricultural); the February 11, 2018 effective date of the Healthy Working Families Act; and BEACON replacing the legacy MABS system. Everything else above -- brackets, county rates, SUI wage base and rates, MW-506 filing categories and dates, MW-508 January 31 due date, MW507 line structure, DLLR/DUI 15/16 quarterly due dates, the $35-per-quarter and 1.5%-per-month UI charges, new-hire and misclassification penalties, and the worked-example arithmetic -- is confirmed by the archived primary and Comptroller/DOL sources in the table (read 2026-10-28 through 2026-11-02).

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
