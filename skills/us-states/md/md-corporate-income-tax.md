---
name: md-corporate-income-tax
description: >
  Use this skill whenever asked about Maryland corporate income tax for tax
  year 2026 -- the flat 8.25% rate on Maryland taxable income (Form 500),
  separate-return requirement for federal consolidated groups, single
  receipts-factor apportionment for tax years beginning after 2021, special
  apportionment formulas for rental/leasing, financial institutions,
  transportation and worldwide-unitary-headquartered companies, Form 500D
  estimated tax (four 25% installments, 90%/110% safe harbors), Form 500E
  extension (max 7 months), and the 11.4825% post-2024 interest rate.
  Trigger on "Maryland corporate income tax", "Form 500", "Maryland CBT",
  "Maryland corporation apportionment", "Form 500D", "Form 500E".
  Source-cited draft; Comptroller 2024 Corporation Tax Booklet read 2026-10-27.
jurisdiction: US-MD
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: "0.2"
verified_by: pending
depends_on:
  - md-income-tax
---

# Maryland corporate income tax (Form 500) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to


Covers Maryland corporation income tax on C corporations and other entities taxed as corporations (Form 500), including nexus, apportionment, estimated tax, extensions, penalties and interest. Out of scope: federal tax, Maryland personal income tax (`md-income-tax`), payroll withholding (`md-payroll`), sales/use tax (`md-sales-tax`), the digital advertising tax (separate regime, returns due April 15), S corporations (Form 510 pass-through level), and fiduciary returns (Form 504). (not yet confirmed)

**Source status:** the Comptroller's Corporation Income Tax Return Booklet (2024 edition, latest located) was fetched and read in full on 2026-10-27 (HTTP 200, PDF text extracted). Statute-section citations (Tax-General §7-204 rate, §13-701 penalty percentages) did **not** resolve from the drafting environment -- those specifics are flagged; the 8.25% rate, interest rate, due dates, estimated-tax mechanics and extension cap are all quoted from the booklet itself. The 8.25% rate is independently confirmed by the archived statute text: Tax-General § 10-106(b)(1) (archived 2026-10-28): "The State income tax rate for a corporation is 8.25% of Maryland taxable income."

## Rates, bands and thresholds


- Every corporation subject to the Maryland income tax law -- multistate corporations operating in Maryland as a **unitary business** outside P.L. 86-272 protection, and unistate corporations operating only in Maryland (or whose other-state activity is within P.L. 86-272 protection). (Booklet, "Multistate and Unistate Corporations", read 2026-10-27.)
- **Affiliated corporations that file consolidated federal returns must file separate Maryland returns** for each member, reporting taxable income or loss on a separate basis without regard to consolidation; NOLs and special deductions are computed on separate federal taxable income. (Booklet, "Special Requirements for Certain Organizations", read 2026-10-27.)
- A multistate corporation with Maryland operations but not subject to the tax law need not file, though a zero-factor return may be filed for record purposes; letters in lieu of filing are not accepted. (Booklet, read 2026-10-27.)
- All financial institutions are subject to the tax with special apportionment rules (COMAR 03.04.08). (Booklet, read 2026-10-27.)

## The taxable base


| Item | Amount / rule | Source |
|---|---|---|
| Corporate income tax rate | **8.25%** flat on Maryland taxable income (Form 500 line 14) | Corporation Tax Booklet, "Tax, Interest and Penalty" + line 14 instruction, read 2026-10-27 |
| Statutory citation for the rate | Tax-General §7-204 | (statute page not fetched this run; rate itself verified in booklet) |
| Base | Federal taxable income with statutory addition/subtraction modifications, × apportionment factor for multistate corporations | Booklet, read 2026-10-27 |
| Apportionment | **Single receipts factor** for tax years beginning after 31 December 2021; rental/leasing companies, financial institutions, transportation companies and worldwide-unitary-headquartered companies must use a Special Apportionment Formula unless the Comptroller accepts an Alternative Apportionment Formula | Booklet, "Single Sales Factor Apportionment", read 2026-10-27 |
| Separate accounting | Allowed only with prior approval of the Revenue Administration Division, for nonunitary in-state activity | Booklet, read 2026-10-27 |
| Minimum tax | None found in the booklet for Form 500 | booklet read 2026-10-27; absence noted, confirm before relying |

There is no Maryland surtax or franchise tax on top of the 8.25% for ordinary C corporations (pack README: no franchise/gross-receipts tax).

## Deadlines and filing


- **Return:** Form 500 due the **15th day of the 4th month** after year-end (15 April for calendar-year filers). (Booklet, "When and Where to File", read 2026-10-27.) (not yet confirmed)
- **Extension:** Form 500E; extension of time to file only, **never more than 7 months** beyond the original due date; payment is still due at the original date. (Booklet, "Extension of Time to File", read 2026-10-27.)
- **Estimated tax (Form 500D):** required if the corporation reasonably expects a Maryland tax over **$1,000**; four installments due the **4th, 6th, 9th and 12th months** of the year, at least **25% each**; total must be at least **90% of current-year tax or 110% of prior-year tax**. (Booklet, "Estimated Income Tax", read 2026-10-27.)
- **Amended returns:** Form 500X has been combined with Form 500 -- check the amended box and refile the full return. IRS final determination increasing Maryland income: amend within **90 days**. (Booklet, read 2026-10-27.)
- **Refund claims:** 3 years from filing / 2 years from payment, with statutory limitations. (Booklet, read 2026-10-27.)

## Penalties and interest


- **Interest:** annual rate **11.4825%** for periods after 31 December 2024 (10.0075% for 2024). (Booklet, "Tax, Interest and Penalty", read 2026-10-27.) (not yet confirmed)
- **Late filing / late payment:** a penalty applies; false, fraudulent or frivolous returns carry additional penalties, civil and criminal. The booklet does not print the percentage -- the statutory penalty (Tax-General §13-701, commonly up to 25% of tax due) is this run. (not yet confirmed)
- **Estimated-tax underpayment:** additions apply when installments miss the 90%/110% safe harbor (Form 500D mechanics). (Booklet, read 2026-10-27.) (not yet confirmed)

## Cross-border points


- Unitary-business apportionment via Schedule A receipts factor; goods generally sourced to delivery destination, services to where the benefit is received (booklet Schedule A instructions, read 2026-10-27).
- P.L. 86-272 protects solicitation of orders for tangible personal property only; exceeding it creates filing exposure.
- Maryland has **no corporate combined/unitary group return** -- federal consolidated groups file separate Maryland returns (see §2). Combined-reporting questions route to `md-transfer-pricing`.
- Nonresident individuals working in Maryland: see `md-cross-border` (reciprocity, special nonresident tax).

## Worked examples


**Example 1 -- unistate C corporation.** A Maryland-only manufacturer has federal taxable income of $2,000,000 and no modifications. (not yet confirmed)

```oa-check
name: MD unistate corp tax
inputs:
 income: 2000000
 rate: 0.0825
steps:
 - tax: income * rate
expected:
 tax: 165000.00
```

Maryland tax: **$165,000**, due 15 April with Form 500D installments already made. (not yet confirmed)

**Example 2 -- multistate corporation, single receipts factor.** A multistate seller has $5,000,000 modified income and a Maryland receipts factor of 0.125 ($10,000,000 Maryland receipts ÷ $80,000,000 total). (not yet confirmed)

```oa-check
name: MD apportioned tax
inputs:
 receipts_md: 10000000
 receipts_total: 80000000
 income: 5000000
 rate: 0.0825
steps:
 - factor: receipts_md / receipts_total
 - md_income: income * factor
 - tax: md_income * rate
expected:
 factor: 0.1250
 md_income: 625000.00
 tax: 51562.50
```

**Example 3 -- estimated installments.** Expected Maryland tax $100,000:

```oa-check
name: MD estimated installments
inputs:
 tax: 100000
 n: 4
steps:
 - each: tax / n
expected:
 each: 25000.00
```

Four payments of **$25,000** (Form 500D) at the 4th/6th/9th/12th-month dates. (not yet confirmed)

## Ask the client first


1. Is the entity part of a federal consolidated group? (Maryland still requires separate returns -- which members have Maryland nexus?)
2. What apportionment method is in use -- single receipts factor, Special Apportionment Formula (rental/leasing, financial, transportation, worldwide HQ), or an approved Alternative formula?
3. Are Form 500D installments tracking 90% of current year or 110% of prior year? (not yet confirmed)
4. Any P.L. 86-272 claim, and does the activity stay inside it?
5. Any IRS examination closing that started the 90-day amended-return clock?

## Sources


| Source | What it covers | Read on |
|---|---|---|
| Md. Code, Tax-General §7-204 (rate) and §13-701 (penalty): -- statute pages did not resolve from the drafting environment on 2026-10-27. | internal skill reference | 2026-10-28 |
| Form 500 / 500D / 500E instructions: referenced inside the booklet above (same fetch). | internal skill reference | 2026-10-28 |

Not yet confirmed: the statute text behind Tax-General §7-204 (corporate rate citation) and §13-701 (late-filing penalty percentage) -- the 8.25% rate itself is confirmed in the archived Tax-General §10-106(b)(1) and the 2024 Corporation Tax Booklet.

## Talk to a verified accountant

No Maryland-specific rule was found in the sources read for this topic.

<!-- openaccountants-cta-block -->

### Talk to a verified accountant

**Talk to a verified accountant** -- for Maryland questions on live client facts, book time with an OA Partner.
