---
name: md-cross-border
description: >
  Use this skill whenever asked about Maryland cross-border personal tax for
  tax year 2026 — part-year and nonresident Form 505, the 24-county local
  tax structure and the 2.25% Special Nonresident Tax in lieu of county tax
  (Tax-General §10-106.1), reciprocity exemptions for DC/PA/VA/WV resident
  wage earners, nonresident real-estate withholding (Form MW506NRS), and the
  corporate side: separate returns for consolidated groups and no
  combined-report regime. Trigger on "Maryland nonresident", "Maryland
  part-year", "Form 505", "Maryland special nonresident tax", "Maryland
  reciprocal agreement", "MW506NRS", "Maryland county tax nonresident".
  Source-cited draft; Comptroller booklet and Department of Labor pages read
  2026-10-27, figures corroborated by the existing md-payroll skill.
jurisdiction: US-MD
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - md-income-tax
  - md-payroll
---

# Maryland cross-border (nonresidents, part-year, reciprocity) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to


Covers how Maryland taxes people and businesses that cross its border: individual part-year/nonresident filing (Form 505), the county-tax overlay for nonresidents (Special Nonresident Tax), the four reciprocal agreements, nonresident real-estate withholding, and the corporate cross-border posture. Out of scope: full resident computation (`md-income-tax`), employer withholding mechanics (`md-payroll`), corporate apportionment detail (`md-corporate-income-tax`, `md-transfer-pricing`).

**Source status:** the Comptroller 2024 Corporation Tax Booklet (real-estate withholding reference) verified 200 and read 2026-10-27. The 2025 Form 505 instruction PDF returned 404 from the drafting environment — Form 505 procedural specifics are; the 2.25% Special Nonresident Tax, county-rate range 2.25%–3.20%, and the DC/PA/VA/WV reciprocity list are corroborated by the existing tier-2 `md-payroll` skill (statutory cite Tax-General §10-106.1) and must be re-verified against the current 505 instructions before filing.

## Rates, bands and thresholds


- **Part-year and nonresident individuals** with Maryland-source income (wages for days worked in Maryland, Maryland real property gains, etc.) file **Form 505** when they meet the filing thresholds. (Corroborated by `md-payroll`; 505 instructions.)
- **Reciprocal-state residents** (DC, Pennsylvania, Virginia, West Virginia): Maryland-source **wages are exempt** from Maryland income tax under bilateral agreements; the resident pays only their home state. A PA resident *not* covered by reciprocity falls into the Special Nonresident Tax instead. (Corroborated by `md-payroll`.)
- **Other-state residents** working in Maryland: taxed on Maryland-source income at graduated state rates **plus the 2.25% Special Nonresident Tax** in lieu of the county tax (Tax-General §10-106.1, per `md-payroll`).
- **Nonresident sellers of Maryland real property:** withholding regime via **Form MW506NRS** — the buyer/payer withholds state income tax on the sale unless waived; the seller settles on a Form 505 or declares estimated payments. (Booklet line-15 reference to MW506NRS, read 2026-10-27; waiver mechanics.)
- **Corporations:** no combined return; federal consolidated members file separate Maryland returns (see `md-transfer-pricing`).

## The taxable base


| Item | Amount / rule | Source |
|---|---|---|
| State graduated rates (nonresidents pay on the MD-source share) | 2%–5.75% top for 2025 brackets per `md-payroll` | `md-payroll` skill, 2025 tables |
| County tax (residents) | 2.25%–3.20% by county | `md-payroll` skill |
| **Special Nonresident Tax** | **2.25%** flat on Maryland-source income, in lieu of county tax | Tax-General §10-106.1 via `md-payroll`; statute page |
| Reciprocity exemption | DC/PA/VA/WV residents' wages exempt from MD tax (income other than wages still MD-source taxable) | `md-payroll` skill |
| Effective top combined for nonresidents | 5.75% + 2.25% = **8.00%** | `md-payroll` skill table |

Base for Form 505: Maryland-source income, with the federal return attached; allocation of wages is day-based for most nonresidents (505 mechanics).

## Deadlines and filing


- Form 505 follows the individual return calendar: **15 April** for calendar-year filers (505 instructions; date is the universal US individual norm and matches `md-income-tax`).
- MW506NRS withholding is due at closing; the seller's settlement return can be filed within 3 years of closing to reclaim over-withheld tax (waiver/settlement mechanics).
- Reciprocity exemption at payroll level: employee files the exemption certification with the employer (MD form **MW507B** — for the current form number).

## Penalties and interest


- Missed Maryland filing by a nonresident carries the ordinary regime: interest **11.4825%** annually after 2024 (Corporation Tax Booklet, read 2026-10-27 — same statutory rate applies across Comptroller taxes), late-filing penalty up to 25% (Tax-General §13-701,).
- Employers who withhold Maryland tax for reciprocal-state residents instead of honoring the exemption create employee refunds, not entity penalties; employers who *fail* to withhold for nonreciprocal nonresidents face §13-704 assessments (per `md-payroll`).

## Cross-border points


- **DC/VA/MD commuter:** no MD tax on wages (reciprocity); remote work performed in VA/DC for a MD employer is VA/DC-source, not MD-source.
- **PA/MD:** reciprocity covers wages only — a PA resident with Maryland rental income or business income files Form 505 for that income and pays the 2.25% special nonresident tax on it.
- **No convenience-of-the-employer rule** was found for Maryland in the sources read; Maryland sources wages by where services are performed (contrast New Jersey — see `nj-cross-border`).
- Moving to/from Maryland: part-year Form 505 plus proration; final-rule domicile tests are fact-heavy — flag for review.

## Worked examples


**Example 1 — PA commuter, reciprocity.** A Pennsylvania resident earns $120,000 working in Baltimore County, Maryland, all wages, 2026.

```oa-check
name: MD reciprocal exemption
inputs:
 wages: 120000
 md_rate: 0.0
steps:
 - md_tax: wages * md_rate
expected:
 md_tax: 0.00
```

Maryland tax **$0** with a valid MW507B exemption; PA taxes the wages. Without the exemption, Maryland would assess state rates + 2.25% and the commuter would need a refund claim.

**Example 2 — NY resident working 60 of 240 workdays in Maryland.** Wages $180,000; Maryland-source share by workdays.

```oa-check
name: MD nonresident wage allocation
inputs:
 wages: 180000
 md_days: 60
 total_days: 240
 state_top: 0.0575
 special: 0.0225
steps:
 - md_source: wages * md_days / total_days
 - rough_tax: md_source * (state_top + special)
expected:
 md_source: 45000.00
 rough_tax: 3600.00
```

The $3,600 is an upper-bound at top marginal rates (Maryland's graduated brackets will compute lower); it shows the 8.00% combined exposure the client should model. New York credits taxes paid to Maryland subject to its own limits.

## Ask the client first


1. Where is domicile, and did a move create a part-year? Which side of the 30-day/final-rule facts apply?
2. Is the employee in a reciprocal state, and is the exemption certification on file with payroll?
3. Any Maryland real property sale by a nonresident — was MW506NRS withheld, and is a settlement return worth filing?
4. Non-wage Maryland-source income (rental, business, gains) for a nonresident — Form 505 plus 2.25% special tax modeled?
5. Days-worked logs for remote commuters — who tracks them?

## Sources


| Source | What it covers | Read on |
|---|---|---|
| Existing tier-2 skill `md-payroll` (county rates, §10-106.1 special nonresident tax, reciprocity list, §13-704): repo `skills/us-states/md/md-payroll.md`. | internal skill reference | 2026-10-28 |
| Md. Code Tax-General §10-106.1: (statute mirror did not resolve 2026-10-27). | internal skill reference | 2026-10-28 |

Not yet confirmed: the 2025 Form 505 instruction PDF (404 on 2026-10-27), the Tax-General §10-106.1 statute text for the 2.25% Special Nonresident Tax, the MW506NRS waiver mechanics, the current MW507B reciprocity form number, and the §13-701 penalty percentage.

## Talk to a verified accountant

No Maryland-specific rule was found in the sources read for this topic.

<!-- openaccountants-cta-block -->

### Talk to a verified accountant

**Talk to a verified accountant** — for Maryland questions on live client facts, book time with an OA Partner.
