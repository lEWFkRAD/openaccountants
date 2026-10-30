---
name: ar-corporate-income-tax
description: >
  Use this skill whenever asked about Arkansas corporate income tax
  for tax year 2026 -- the graduated 1% to 4.3% rate (4.1% from 2027),
  the SB 567 / Act 719 of 2025 corporate-tax modernization
  (market-based sourcing for services and intangibles, the $250,000
  economic nexus threshold for non-resident entities), Form AR-1100
  (AR1100CT) / AR-1100ADJ mechanics, the pass-through entity tax, and
  estimated tax. Trigger on "Arkansas corporate tax", "Arkansas
  AR-1100", "Arkansas SB 567", "Arkansas Act 719", "Arkansas market
  based sourcing", "Arkansas pass-through entity tax".
jurisdiction: US-AR
category: corporate
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: "0.3"
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - ar-income-tax
---

# Arkansas corporate income tax, tax year 2026

> **Source-cited draft.** Built from Act 719 of 2025, Act 1 of the 2026 First Extraordinary Session, the DFA fiscal impact statement for SB1, the DFA Corporation Income Tax page and the DFA Corporate FAQs, read on 2026-10-28. No accountant has reviewed it. Do not file from it without review by a qualified Arkansas professional.

Arkansas taxes C corporations on Arkansas-apportioned income. DFA's Corporation Income Tax Section processes and audits Partnership, LLC, C-corporation and Sub-S income tax returns ([DFA Corporation Income Tax page](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/)). In 2025 the state layered a major reform: "On April 16, 2025, Arkansas Gov. Sarah Huckabee Sanders signed Senate Bill 567 into law as Act 719 of 2025, modernizing the state's corporate income tax" -- it amends Arkansas' adoption of the Multistate Tax Compact / UDITPA, adopts market-based sourcing for sales of services and intangibles, and establishes an economic nexus filing threshold for non-resident corporations or partnerships (DFA page, read 2026-10-28).

## Who this applies to

- **C corporations** doing business in Arkansas, filing Form AR1100CT with a copy of the federal return attached (DFA Corporate FAQs).
- **Non-resident corporations and partnerships over the economic nexus threshold:** "Effective January 1, 2026, Arkansas established a corporate economic nexus threshold of $250,000 in gross receipts for nonresident corporations or partnerships with no physical presence. No physical presence is required to establish an income tax filing requirement" (DFA Corporate FAQs, citing ACA §26-51-702 & 26 CAR §130-136). Act 719 itself: a nonresident is not subject to the chapter's filing requirement unless Arkansas receipts under §§26-51-701–26-51-718 "exceed two hundred fifty thousand dollars ($250,000)" for the current or preceding taxable year.
- A non-resident corporation or partnership **with a physical presence** in Arkansas engaging in unprotected activities still establishes nexus and a filing requirement even below the threshold (DFA Corporate FAQs).
- **S corporations** file AR-1100S; partnerships/LLCs file the partnership return and members pay individually, unless the entity elects the **pass-through entity tax (PET)** (DFA Corporation Income Tax page).
- The AR-1100ADJ adjustment schedule carries the state modifications to federal taxable income.

## Rates, bands and thresholds

| Item | Rate / amount | Tax year | Source |
|---|---|---|---|
| Corporate income tax, first $3,000 of net income | 1.0% | 2024 to 2026 | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Second $3,000 of net income | 2.0% | 2024 to 2026 | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Next $5,000 of net income | 3.0% | 2024 to 2026 | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| All net income exceeding $11,000 (top rate) | 4.3% | 2024 to 2026 | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Top rate (first $3,000 / next $3,000 / next $5,000 / above $11,000) | 1% / 2% / 3% / 4.1% | 2027 and following | [Act 1 of 2026 First Extraordinary Session](https://www.arkleg.state.ar.us/Home/FTPDocument?path=/ACTS/2026S1/Public/ACT1.pdf); [DFA fiscal impact, SB1](https://arkleg.state.ar.us/Home/FTPDocument?path=%2FAssembly%2F2025%2F2026S1%2FFiscal+Impacts%2FSB1-DFA1.pdf) |
| Economic nexus threshold (nonresident corporations/partnerships, no physical presence) | $250,000 gross receipts | from 2026-01-01 | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/); [Act 719 of 2025](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf) |
| EFT mandate for estimated quarterly payments | quarterly liability of $20,000 or more | current | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Apportionment | single sales factor (Act 822 of 2019), market-based sourcing for services and intangibles from 2026 (Act 719) | 2026 | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/); [Act 719 of 2025](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf) |
| NOL carryforward | 5 tax years (pre-2020 losses), 8 tax years (losses from 2020), 10 tax years (losses from 2021); carrybacks not allowed | current | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Base | federal taxable income with Arkansas modifications (AR-1100ADJ); Arkansas or federal income tax not deductible; no bonus depreciation; IRC §179 as in effect on 1 January 2022 | current | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |

Act 1 (SB1) and Act 4 (HB1001) of the Second Extraordinary Session of 2024 reduced the top corporate income tax rate to 4.3% for tax years beginning on or after January 1, 2024; Act 1/Act 2 of the 2026 First Extraordinary Session reduce the top rate to 4.1% "for tax years beginning on or after January 1, 2027" (DFA Corporate FAQs; Act 1 of 2026). Arkansas has no corporate minimum tax stated on these DFA pages -- see Not yet confirmed.

## The taxable base

- Federal taxable income, modified on Form AR-1100ADJ. Arkansas does not allow Arkansas or federal income tax as a deduction (ACA §26-51-416, DFA Corporate FAQs).
- **Depreciation:** "No bonus depreciation is allowed for Arkansas income tax purposes." IRC §§167 and 168(a)–(j) are adopted as in effect on January 1, 2019; IRC §179 as in effect on January 1, 2022 (DFA Corporate FAQs).
- **Apportionment:** since tax years beginning on or after January 1, 2021, "all taxpayers with income from sources within and without Arkansas must use a single sales factor to apportion income from Arkansas" (DFA Corporate FAQs, citing Act 822 of 2019 amending ACA §26-5-101 Article IV and §§26-51-709–26-51-718). Act 719 of 2025 rewrites the sales-sourcing rules inside those sections: receipts from services and intangibles are in Arkansas if "the taxpayer's market for the sales is in this state" (Act 719, amending §26-51-717), for tax years beginning on and after January 1, 2026.
- **Consolidated returns:** ACA §26-51-805 -- all federal eligible members must be part of the federal consolidated return, only members with Arkansas income may join, all Arkansas eligible members must consent before the last day for filing, and each entity separately computes its taxable income or loss on its own AR1100CT before consolidating (DFA Corporate FAQs).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| AR1100CT, calendar year | "on or before April 15 for the preceding calendar year" (ACA §26-51-806) | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| AR1100CT, fiscal year | on or before the 15th day of the 4th month after the close of the tax year | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Estimated installment 1 (Voucher 1) | on or before the 15th day of the fourth month of the tax year (ACA §26-51-913) | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Estimated installment 2 (Voucher 2) | on or before the 15th day of the sixth month of the tax year | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Estimated installment 3 (Voucher 3) | on or before the 15th day of the ninth month of the tax year | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Estimated installment 4 (Voucher 4) | on or before the 15th day of the twelfth month of the tax year | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Federal extension (Form 7004) | recognized for the Arkansas return until the federal extended due date; Act 629 of 2021 adds one month after the federal extended due date for tax years beginning on or after January 1, 2021 when a federal extension is requested | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Arkansas extension beyond the federal one | form AR1155, 60 days beyond the federal extended due date for good cause (ACA §26-18-505) | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Report an IRS change (RAR) | within 180 days of the IRS notice and demand (ACA §26-18-306(b)) | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Amended return | within 3 years of the original filing date or 2 years from payment, whichever is later (ACA §26-18-306(i)) | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |

Payments may be made by EFT (ACH debit or credit), ATAP, check, or in person; the Corporation Income Tax Section does not accept credit cards or wire transfers. Corporations with an estimated quarterly income tax liability of $20,000 or more must pay by EFT (ACA §26-19-106, DFA Corporate FAQs).

## Penalties and interest

- **Interest:** 10% per annum on tax not paid by the original due date, "computed on a daily rate of .00027397 (.027397%)" (DFA Corporate FAQs).
- **Failure to pay:** "failure to pay penalties at 5% per month will be assessed on all taxes unpaid after the original due date" (DFA Corporate FAQs, ACA §26-18-208).
- **EFT non-compliance:** a 5% penalty on the taxes due for a corporation required to pay by EFT that does not (ACA §26-19-107).
- **Extension is not an extension to pay:** "All tax payments are due on the original return due date" (DFA Corporate FAQs).
- Common failure modes: (1) ignoring the economic nexus threshold for non-resident corporations/partnerships from 2026; (2) sourcing services/intangibles by place-of-performance after the 2025 reform instead of the customer's market; (3) forgetting corporate (Sub-S) withholding obligations (see `ar-payroll-withholding`).

## Cross-border points

- **Market-based sourcing:** Act 719 moves the sales-factor numerator for services and intangibles to where the customer receives delivery -- see `ar-transfer-pricing`.
- **Economic nexus:** a non-resident corporation or partnership with $250,000 or more of Arkansas receipts and no physical presence must file from tax year 2026 (DFA Corporate FAQs; Act 719).
- **Special industry apportionment** still applies within the single sales factor: private railcar operators (26 CAR §130-114), construction contractors (§130-144(a)), television and radio broadcasting (§130-144(b)), publishing (§130-144(c)), pipelines (§130-144(f)) -- ACA §26-51-718(c), DFA Corporate FAQs.
- Multistate individuals (part-year residents, nonresidents, other-state credits) are handled in `ar-income-tax`.

## Worked examples

**Example 1: C corporation, calendar year 2026.** A corporation with $1,500,000 of net income apportioned to Arkansas at the 2026 graduated rates (1% on the first $3,000, 2% on the next $3,000, 3% on the next $5,000, 4.3% on the excess over $11,000):

```oa-check
name: AR corporate tax, 1,500,000 apportioned income, 2026 graduated rates (hypothetical facts)
inputs:
  apportioned: 1500000
steps:
  - tax: 3000 * 0.01 + 3000 * 0.02 + 5000 * 0.03 + (apportioned - 11000) * 0.043
expected:
  tax: 64267.00
```

**Example 2: market-based sourcing of a services contract (2026).** $2,000,000 of total service revenue, of which $800,000 is delivered to Arkansas customers, and $1,500,000 of apportionable income before sourcing. Under single-sales-factor apportionment with market sourcing:

```oa-check
name: AR market sourcing services fraction (hypothetical facts)
inputs:
  ar_market: 800000
  total: 2000000
  income: 1500000
steps:
  - factor: ar_market / total
  - apportioned: income * factor
expected:
  factor: 0.40
  apportioned: 600000.00
```

## Ask the client first

- Has the nexus model been re-run against the $250,000 economic-nexus threshold for non-resident entities, effective January 1, 2026?
- Are services/intangible revenues sourced to the customer's market location for tax years beginning on or after January 1, 2026?
- Is the entity considering the pass-through entity tax election -- and what is the member-savings math?
- Is the corporation above the $20,000 quarterly EFT threshold and paying electronically?
- Does the group file consolidated (ACA §26-51-805 consent filed before the due date), or separately?

## Sources

| Source | URL | Read on |
|---|---|---|
| DFA, Corporation Income Tax (Act 719 narrative, ATAP, alternative apportionment request link) | https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/ | 2026-10-28 |
| DFA, Corporate FAQs (rates, nexus threshold, deadlines, EFT, extensions, penalties, apportionment, depreciation, NOL) | https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/ | 2026-10-28 |
| Act 719 of 2025 (market-based sourcing, §§26-51-701–26-51-718, $250,000 nexus), Arkansas Legislature | https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf | 2026-10-28 |
| Act 1 of 2026 First Extraordinary Session (corporate top rate 4.1% for tax years beginning on or after January 1, 2027) | https://www.arkleg.state.ar.us/Home/FTPDocument?path=/ACTS/2026S1/Public/ACT1.pdf | 2026-10-28 |
| DFA fiscal impact statement for SB1 of 2026 First Extraordinary Session (2026 individual tables; corporate 4.1% from 2027) | https://arkleg.state.ar.us/Home/FTPDocument?path=%2FAssembly%2F2025%2F2026S1%2FFiscal+Impacts%2FSB1-DFA1.pdf | 2026-10-28 |
| DFA, Withholding Tax Branch (annual reconciliation, W-2/1099 transmittals) | https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/withholding-tax-branch/ | 2026-10-28 |

Not yet confirmed: the pass-through entity tax (PET) election rate and mechanics (the DFA pages list the PET program and forms but state no rate -- pull the PET forms/instructions before quoting a member-savings figure); the AR-1100ADJ line detail (the 2026 revision of the form was located via DFA search but its line-by-line content was not read); whether Arkansas imposes a corporate minimum tax; the AR-1100S (S corporation) due date for calendar-year 2026 (March 16 is the federal S-corp date, but no Arkansas source stating the AR-1100S date was read); the estimated-tax safe-harbor percentage for corporations; the current status of the throwback/throwout rule for tangible-property sales after Act 719 (the Act's amended §26-51-716 was not read line by line for throwback language).

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
