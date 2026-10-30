---
name: ar-transfer-pricing
description: >
  Use this skill whenever asked about Arkansas transfer pricing for
  tax year 2026 -- Arkansas' separate-entity, single-sales-factor
  UDITPA framework as amended by SB 567 / Act 719 of 2025
  (market-based sourcing for services and intangibles, the $250,000
  economic nexus threshold for non-resident entities), the
  affiliated-group adjustment provisions, alternative apportionment,
  and how related-party pricing is policed without mandatory
  combined reporting. Trigger on "Arkansas transfer pricing",
  "Arkansas UDITPA", "Arkansas market based sourcing", "Arkansas
  addback", "Arkansas affiliated group", "Arkansas separate entity
  reporting", "Arkansas alternative apportionment".
jurisdiction: US-AR
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: "0.2"
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - ar-corporate-income-tax
---

# Arkansas transfer pricing, tax year 2026

> **Source-cited draft.** Built from Act 719 of 2025, the DFA Corporation Income Tax page and the DFA Corporate FAQs, read on 2026-10-28. No accountant has reviewed it. Do not take a related-party position from it without review by a qualified Arkansas professional.

Arkansas polices related-party economics through its **UDITPA-based apportionment and affiliated-group provisions**, not through mandatory combined reporting. Arkansas is a separate-entity filing state: each entity computes its own income on its own AR1100CT, even in a consolidated group ("each entity in the Arkansas consolidated group must separately compute its taxable income or loss on a separate form AR1100CT" -- DFA Corporate FAQs). The 2025 reform (**SB 567 / Act 719**, signed 2025-04-16) rewrote the apportionment provisions: **market-based sourcing for sales of services and intangibles** ("based on the location where they are delivered to the customer" -- DFA page) and an **economic nexus filing threshold** for non-resident corporations or partnerships ([Act 719](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf); DFA page).

## Who this applies to

- Every corporation filing Arkansas separately with related-party transactions -- intercompany pricing is tested through the apportionment adjustments on AR-1100ADJ and the affiliated-group provisions.
- Post-Act 719: **non-resident corporations and partnerships with $250,000 or more of Arkansas receipts** and no physical presence are pulled into the filing system from tax year 2026 ("No physical presence is required to establish an income tax filing requirement" -- DFA Corporate FAQs), which makes the sourcing rules the main transfer-pricing lever.
- Unitary groups do **not** automatically combine in Arkansas; each member files separately (DFA Corporate FAQs, consolidated-return requirements). The transfer-pricing risk sits in the sales-factor numerator and in affiliate-expense adjustments.

## Rates, bands and thresholds

| Item | Rule | Tax year | Source |
|---|---|---|---|
| Filing method | separate entity; consolidated only by ACA §26-51-805 election with all Arkansas eligible members consenting | 2026 | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Apportionment factor | single sales factor (Act 822 of 2019, ACA §26-5-101 Art. IV and §§26-51-709–26-51-718) | 2026 | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Services/intangibles sourcing | market-based: receipts are in Arkansas if "the taxpayer's market for the sales is in this state" (Act 719 amending §26-51-717), for tax years beginning on or after January 1, 2026 | 2026 | [Act 719 of 2025](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf) |
| Economic nexus threshold | $250,000 Arkansas gross receipts for nonresident corporations/partnerships with no physical presence, effective January 1, 2026 | 2026 | [DFA Corporate FAQs](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/) |
| Alternative apportionment | available on request (DFA "Request for Alternative Apportionment of Income" link) | 2026 | [DFA Corporation Income Tax page](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/) |
| Affiliate expense adjustments | see Not yet confirmed (the intangible/management-fee addback statute text was not read) | 2026 | -- |

## The taxable base

- **Single sales factor:** since tax years beginning on or after January 1, 2021, all taxpayers with income from sources within and without Arkansas apportion with a single sales factor (DFA Corporate FAQs). Special industries keep their guidance inside the sales factor: private railcar operators, construction contractors, television and radio broadcasting, publishing, pipelines (ACA §26-51-718(c)).
- **Market-based sourcing from 2026:** for services and intangibles, the sales-factor numerator follows where the customer takes delivery -- not where the work is performed (Act 719; DFA page). Nonapportionable (nonbusiness) income is allocated under §§26-51-704–26-51-708 as amended by Act 719.
- **Federal taxable income carries in** with Arkansas modifications (AR-1100ADJ): no Arkansas or federal income tax deduction, no federal bonus depreciation, IRC §179 as in effect on January 1, 2022 (DFA Corporate FAQs).
- **Affiliated-group adjustments:** Arkansas polices related-party pricing through these apportionment and adjustment provisions rather than combined reporting. The specific intangible-expense/affiliate addback statute (Ark. Code Ann. §26-51-904) was not retrieved in this revision -- see Not yet confirmed.

## Deadlines and filing

- Transfer-pricing adjustments ride the AR-1100 (AR1100CT) calendar: April 15 for calendar-year corporations, the 15th day of the 4th month for fiscal-year filers (DFA Corporate FAQs) -- see `ar-corporate-income-tax` for the full deadline and extension table.
- Alternative-apportionment requests are filed with (or before) the return through the DFA "Request for Alternative Apportionment of Income" process (DFA Corporation Income Tax page).

## Penalties and interest

- There is no standalone Arkansas transfer-pricing documentation penalty; exposure runs through the underpayment penalties and interest: 5% per month failure-to-pay penalty and 10% per annum interest, computed daily at .00027397 (DFA Corporate FAQs).
- Common failure modes: (1) keeping place-of-performance sourcing for services after the Act 719 reform; (2) management fees or royalties to a low-tax affiliate with no substance analysis; (3) assuming separate-entity filing means related-party pricing is unexamined -- the sales factor is where DFA looks.

## Cross-border points

- **Market sourcing** makes the customer's location the driver -- align contracts, order-to-cash data, and the sales-factor schedule with where each service/intangible is delivered.
- **Economic nexus** (from 2026) can make a non-resident affiliate with Arkansas-market receipts a filer even without physical presence ($250,000 threshold, DFA Corporate FAQs).
- Federal §1059A-style intangible limitations carry in through federal taxable income; Arkansas-specific affiliate adjustments sit on top (see Not yet confirmed on the addback statute).

## Worked examples

**Example 1: related-party royalty (hypothetical facts).** OpCo (Arkansas operations) pays $300,000 of royalties to AffiliateCo (no Arkansas nexus, arm's-length royalty assumed). Arkansas-apportionable income before the royalty is $1,200,000; the Arkansas sales fraction is 0.60. The royalty reduces apportionable income to $900,000, of which $540,000 is apportioned to Arkansas:

```oa-check
name: AR royalty effect on apportioned income (hypothetical facts)
inputs:
  income_before: 1200000
  royalty: 300000
  factor: 0.60
steps:
  - income_after: income_before - royalty
  - apportioned: income_after * factor
expected:
  income_after: 900000.00
  apportioned: 540000.00
```

**Example 2: market-sourcing fraction after the reform (hypothetical facts).** A services contract books $2,000,000 of revenue, of which $800,000 is delivered to Arkansas customers, with $1,500,000 of apportionable income. Under the single-sales-factor with market sourcing the Arkansas fraction is 0.40:

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

- Are service and intangible revenues now sourced to the customer's market location for tax years beginning on or after January 1, 2026?
- Do affiliate royalty/management-fee arrangements have substance documentation for an affiliate-adjustment review?
- Has the group tested itself against the $250,000 economic-nexus threshold (Arkansas receipts of each non-resident member)?
- Is an alternative-apportionment request a better answer than the statutory single-sales-factor fraction?

## Sources

| Source | URL | Read on |
|---|---|---|
| Act 719 of 2025 (market-based sourcing §§26-51-701–26-51-718, economic nexus, nonapportionable income), Arkansas Legislature | https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf | 2026-10-28 |
| DFA, Corporation Income Tax (Act 719 narrative, alternative apportionment request) | https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/ | 2026-10-28 |
| DFA, Corporate FAQs (separate entity, consolidated election, single sales factor, nexus threshold, penalties) | https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/ | 2026-10-28 |

Not yet confirmed: the text of the affiliated-group / intangible-expense addback statute (Ark. Code Ann. §26-51-901 et seq. and §26-51-904 -- the Arkansas Code site served empty responses, so the addback conditions, exceptions and any disclosure form are not restated here); the current status of the throwback/throwout rule for tangible-property sales after Act 719 (the amended §26-51-716 was not read line by line); whether DFA has issued guidance or rulemaking on the market-based sourcing elections (Act 719 subsection 17(e) references tax years beginning on or after January 1, 2026 for its sourcing provisions, but no DFA rule text was read).

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
