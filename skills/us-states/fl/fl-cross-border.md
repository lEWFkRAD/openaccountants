---
name: fl-cross-border
description: >
  Use this skill whenever asked about Florida cross-border taxation for tax
  year 2026 -- the corporate nexus standard under Ch. 220 ("conducting
  business, earning or receiving income in this state", s. 220.11), Public
  Law 86-272 solicitation protection, the absence of a Florida individual
  income tax and what that means for nonresidents and departing residents,
  the state income tax addback under s. 220.13, and reemployment-tax nexus
  for remote employers. Trigger on "Florida nexus", "PL 86-272 Florida",
  "Florida nonresident", "moving to Florida taxes", "Florida credit for
  taxes paid", "Florida corporate tax other state". ALWAYS load
  us-tax-workflow-base first.
version: 0.2
jurisdiction: US-FL
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - fl-corporate-income-tax
---

# Florida cross-border (nexus, non-residents, other-state taxes), tax year 2026

> **Source-cited draft.** Built from ss. 220.11, 220.13, 220.15 and 220.21 Fla. Stat. (2026), P.L. 86-272 (73 Stat. 555), and Florida Department of Revenue guidance pages, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

**Out-of-state C-corporations with Florida nexus.** Florida's statutory hook is broad: the corporate income tax is "imposed on every taxpayer for each taxable year for the privilege of conducting business, earning or receiving income in this state, or being a resident or citizen of this state" (s. 220.11(1), Fla. Stat.). There is no bright-line economic-nexus dollar threshold in the statute text; the department applies the statutory standard plus factor-based apportionment under s. 220.15. Corporations, including entities that are taxed federally as corporations, are subject to the tax (FDOR corporate income tax page).

**Foreign (non-US) corporations** face the same Ch. 220 reach; federal taxable income is the starting point, modified by Florida adjustments under s. 220.13. Treaty relief operates at the federal level only -- Florida has no state treaty provisions beyond its conformity to the federal base.

**Individuals moving to or from Florida.** Florida imposes no individual income tax, so "non-resident" questions for individuals collapse to corporate and payroll questions: the old residence state may still tax a part-year resident, while Florida itself will not (see `fl-moving-to-florida-domicile`).

**Remote employers.** Florida reemployment tax attaches to Florida employment regardless of where the employer sits; an out-of-state employer with Florida employees must register (see `fl-social-contributions`).

## Rates, bands and thresholds

| Item | Amount / rule | Source |
|---|---|---|
| Corporate income tax rate | 5.5% of net income for taxable years beginning on or after 1/1/2022 | s. 220.11(2)(a): "an amount equal to 5 1/2 percent of the taxpayer's net income for the taxable year"; FDOR corporate income tax page rate table: "On or After 1/1/2022 ... 5.5%" |
| Alternative rate for taxpayers computing income under s. 220.13(2)(k) | 3.3% of net income | s. 220.11(3): "shall be an amount equal to 3.3 percent of the taxpayer's net income for the taxable year" |
| Apportionment fraction | Sales factor 50%, property factor 25%, payroll factor 25% | s. 220.15(1): "an apportionment fraction composed of a sales factor representing 50 percent of the fraction, a property factor representing 25 percent of the fraction, and a payroll factor representing 25 percent of the fraction" |
| Individual nonresident income tax | None -- Florida imposes no individual income tax | No Florida personal income tax statute exists; the tax in Ch. 220 is measured by net income of taxpayers as defined in s. 220.03 |
| State income tax addback | State/local income taxes deducted federally are added back to compute adjusted federal income | s. 220.13(1)(a)1.a.: "The amount of any tax upon or measured by income ... paid or accrued as a liability to the District of Columbia or any state of the United States which is deductible from gross income in the computation of taxable income" shall be added |
| PL 86-272 protection | No state may impose a net income tax where the only in-state activity is solicitation of orders for tangible personal property filled from outside the state | P.L. 86-272, s. 101(a): "No State ... shall have power to impose ... a net income tax on the income derived within such State by any person from interstate commerce if the only business activities within such State ... are ... the solicitation of orders ... for sales of tangible personal property, which orders are sent outside the State for approval or rejection, and, if approved, are filled by shipment or delivery from a point outside the State" |

## The taxable base

Only Florida-apportioned adjusted federal income is taxed. The base starts from federal taxable income, adjusted under s. 220.13 (including the addback of other states' income taxes), apportioned to Florida by the sales/property/payroll fraction in s. 220.15. A company with nexus but no Florida property or payroll can therefore land at a zero or near-zero apportionment percentage on its property and payroll factors, with the sales factor carrying 50% of the fraction.

A company claiming PL 86-272 protection must stay inside the statute: orders solicited in Florida for sales of tangible personal property, sent outside Florida for approval, and filled by shipment from a point outside the state (P.L. 86-272 s. 101(a)). In-state inventory, fulfillment, services, and digital goods exceed the protection. Independent contractors whose in-state activities consist solely of making sales or soliciting orders for tangible personal property do not create business activities either (P.L. 86-272 s. 101(c)).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Florida Form F-1120 | Generally the later of: the 1st day of the 5th month after the tax year end (May 1 for a calendar year), or the 15th day following the federal return due date without extension | FDOR corporate income tax page: "Generally, Florida Form F-1120 is due the later of ... the 1st day of the 5th month following the close of the tax year ... or The 15th day following the due date, without extension, for the filing of the related federal return" |
| F-1120 with no tax due | Must still be filed | FDOR corporate income tax page: "Corporations must file Florida Form F-1120 each year, even if no tax is due." |
| Electronic filing | Required where the taxpayer must file its federal return electronically | s. 220.21(2): "A taxpayer who is required to file its federal income tax return by electronic means ... shall file returns required by this chapter by electronic means." |
| Reemployment tax return (RT-6) for employers with Florida employees | Quarterly, by the last day of the month following each quarter (4/30, 7/31, 10/31, 1/31) | FDOR reemployment tax page due-date table |

## Penalties and interest

Late corporate returns draw a penalty of 10% of any unpaid tax due with the return for each month or fraction of a month the return is late, up to a total penalty of 50% of the unpaid tax (FDOR corporate income tax page). A floating rate of interest applies to underpayments and late payments (FDOR corporate income tax page; s. 213.235 sets the floating deficiency-interest rate).

Common cross-border failure modes: (1) an out-of-state company assuming no Florida exposure while its Florida sales factor grows -- Florida nexus is statutory-conduct based, not threshold based; (2) claiming PL 86-272 for services, digital goods, or in-state fulfillment, which exceed "solicitation of orders of tangible personal property"; (3) departing residents assuming their old state's tax disappears automatically -- it does not; (4) remote employers missing the Florida reemployment duty for Florida-based staff.

## Cross-border points

- **PL 86-272** protects only solicitation of orders for tangible personal property shipped from outside Florida; it does not shield services, digital goods, or in-state inventory fulfillment (P.L. 86-272 s. 101(a)).
- **Other-state pass-through entity taxes:** where an entity pays another state's PTE tax, a Florida member has no Florida credit to claim against a Florida individual income tax because no such tax exists; the federal SALT-cap analysis governs instead.
- **Combined-reporting states:** a group combined elsewhere still files Florida on the entity/statutory-fraction basis unless it elects Florida consolidation under s. 220.131 (see `fl-transfer-pricing`).
- **Reemployment tax for remote employers:** an out-of-state employer with a Florida employee is a liable employer once it meets the coverage tests (FDOR reemployment tax page; see `fl-social-contributions`).

## Worked examples

All client facts in the examples are hypothetical.

A Texas corporation (no Florida property or payroll) has $3,000,000 of Florida-apportioned adjusted federal income for 2026. Florida tax at the confirmed 5.5% rate:

```oa-check
name: FL corporate tax on apportioned income
inputs:
  apportioned: 3000000
  rate: 0.055
steps:
  - tax: apportioned * rate
expected:
  tax: 165000.00
```

The same company's only Florida activity is soliciting tangible-goods orders shipped from Texas, so P.L. 86-272 bars a net income tax on the Florida income:

```oa-check
name: PL 86-272 protected activity
inputs:
  apportioned: 3000000
  rate: 0.055
  protected: 1
steps:
  - tax: apportioned * rate * (1 - protected)
expected:
  tax: 0.00
```

## Ask the client first

- What Florida contacts exist -- employees, agents, inventory, fulfillment, trade shows -- and do they cross "conducting business, earning or receiving income in this state" (s. 220.11(1))?
- Is the activity pure tangible-goods solicitation (PL 86-272) or services/digital/fulfillment?
- For inbound movers: has the old state been formally exited (domicile, statutory-day rules), since Florida itself will not tax them?
- For remote employers: are Florida-based employees registered for Florida reemployment tax?
- Are other states' income taxes deducted federally tracked for the s. 220.13(1)(a)1.a. addback?

## Sources

| Source | URL | Read on |
|---|---|---|
| s. 220.11 Fla. Stat. (2026) -- tax imposed; 5.5% and 3.3% rates; nexus language | https://www.flsenate.gov/Laws/Statutes/2026/220.11 | 2026-10-28 |
| s. 220.13 Fla. Stat. (2026) -- adjusted federal income; state income tax addback | https://www.flsenate.gov/Laws/Statutes/2026/220.13 | 2026-10-28 |
| s. 220.15 Fla. Stat. (2026) -- apportionment fraction (sales 50%, property 25%, payroll 25%) | https://www.flsenate.gov/Laws/Statutes/2026/220.15 | 2026-10-28 |
| s. 220.21 Fla. Stat. (2026) -- returns; electronic filing requirement | https://www.flsenate.gov/Laws/Statutes/2026/220.21 | 2026-10-28 |
| P.L. 86-272, 73 Stat. 555 -- limitation on state net income taxes (15 U.S.C. 381), act text | https://www.govinfo.gov/content/pkg/STATUTE-73/pdf/STATUTE-73-Pg555.pdf | 2026-10-28 |
| Florida Department of Revenue -- Corporate Income Tax page (rates table, F-1120 due date, penalties) | https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx | 2026-10-28 |
| Florida Department of Revenue -- Reemployment Tax page (coverage tests, RT-6 due dates) | https://floridarevenue.com/taxes/taxesfees/Pages/reemployment.aspx | 2026-10-28 |

Not yet confirmed: the current DOR nexus guidance pages beyond the statute text (the department's "doing business" facts-and-circumstances guidance was not archived this run); whether the department has published any post-2022 rate table revisions affecting the 5.5%/3.3% rates (the 2026 statute text read this run shows both rates unchanged).

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
