---
name: hi-sales-tax
description: Use this skill whenever asked about Hawaii General Excise Tax (GET). Trigger on phrases like "Hawaii GET", "General Excise Tax", "HI sales tax", "HRS 237", "Hawaii excise tax". Hawaii has a GET on the SELLER, not a traditional sales tax. The DOTAX-published rates are 4.5% on Oahu (including a 0.5% county surcharge), 0.50% for wholesale activities, and 0.15% for insurance commissions; economic nexus at $100,000 gross income or 200+ transactions.
version: "2.2"
jurisdiction: US-HI
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# HI Sales Tax (General Excise Tax) v2.2

> **Source-cited draft.** Built from the Hawaii Department of Taxation General Excise Tax page (tax.hawaii.gov/get/, read 2026-10-28). No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**CRITICAL: GET is imposed on the SELLER, not the buyer.** GET is a tax on the seller's gross income, applies to virtually all business activity including services, and pyramids (cascades) at every supply-chain level. It is NOT a traditional sales tax.

## Who this applies to

Every person engaging in business activities in Hawaii, anyone with physical nexus (office, employees, inventory, or services performed in Hawaii), and any remote business meeting the economic-nexus threshold. Registration: "An individual, business, or other legal entity must register for a GET license if they are: engaging in business activities in Hawaii, have physical nexus, or meet/exceed the economic nexus threshold." (DOTAX GET page)

## Rates, bands and thresholds

**Published rates (DOTAX General Excise Tax page, read 2026-10-28):**

| Activity | Rate |
| --- | --- |
| "Selling retail goods and services, renting, leasing real property, construction contracting, earning commissions, all others" | 4.5%* (per the DOTAX GET page footnote, "This 4.5% rate includes a 0.5% county surcharge"; the surcharge applies only in counties that have enacted it) |
| "Wholesaling goods, producing, providing wholesale services, business activities of disabled people" | 0.50% |
| "Insurance Commissions" | 0.15% |

\* "*This 4.5% rate includes a 0.5% county surcharge. The county surcharge does not apply to activities taxed at the 0.5% rate (for example selling wholesale goods) or insurance commissions." (DOTAX GET page)

**Economic nexus:** "If the business has gross income or receipts of $100,000 or more, or has 200 or more transactions in the current or preceding calendar year, economic nexus is established." (DOTAX GET page)

| Field | Value |
| --- | --- |
| Tax type | General Excise Tax (GET) -- tax on the SELLER's gross income, not a traditional sales tax |
| Tax authority | Hawaii Department of Taxation (DoTax) |
| Portal | https://tax.hawaii.gov |
| SST member | No |
| Sourcing | Not stated on the archived DOTAX page; see Not yet confirmed below |

## The taxable base

"All gross receipts from these activities are subject to GET unless a specific exemption applies. Certain types of income may be exempt or subject to deduction under Hawaii law." (DOTAX GET page, which links the Schedules of GET, Use Tax, and County Surcharge exemptions and deductions.)

### Transaction pattern library

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE at the general rate | "Sales of goods and services" are listed taxable activities |
| ALL services (including professional) | TAXABLE | "Services and professional fees" are listed taxable activities |
| Wholesale sales | TAXABLE at 0.50% | Lower wholesale rate |
| Resale | 0.50% wholesale rate | Not fully exempt; taxed at the wholesale rate |
| Rentals and commissions | TAXABLE | "Rental income from property", "Commissions and fees", "Construction contracts" are listed taxable activities |
| Business interest and other income earned | TAXABLE | Listed taxable activity on the DOTAX page |

Specific category exemptions (e.g., prescription drugs, groceries as a category) are governed by the Schedules of GET Exemptions and Deductions; see Not yet confirmed below.

### GET pyramiding

GET pyramids: the tax cascades at every supply-chain level. A manufacturer pays 0.50% on wholesale sales, the wholesaler pays 0.50%, and the retailer pays the general rate; amounts passed on to the buyer are additional gross income subject to GET again. (Follows from the seller-side gross-income base and the rate table above.)

## Deadlines and filing

Registration and filing are through Hawaii Tax Online (https://tax.hawaii.gov). The archived DOTAX page does not state the current periodic-return due dates; see Not yet confirmed below.

## Penalties and interest

GET underpayments draw the HRS §231-39 penalty and interest regime (see `hi-corporate-income-tax` for the confirmed amounts). Specific GET penalty provisions were not extracted this run; see Not yet confirmed below.

## Cross-border points

- Remote sellers with no physical presence are captured by the economic-nexus threshold ($100,000 gross income/receipts or 200+ transactions).
- GET on interstate/foreign-source gross income and the use-tax (ch. 238) offset rules were not extracted this run; see Not yet confirmed below.

## Worked examples

The DOTAX page does not publish worked computation rules, and GET computation on gross income is a fill-in exercise on the periodic returns. Per the pack convention, no arithmetic example is asserted beyond the confirmed rate table above; the rates in any client computation must come from the confirmed table in this skill.

## Ask the client first

1. Is the client registered for a GET license -- and does it meet/exceed the $100,000 / 200-transaction economic-nexus threshold even without physical presence?
2. Which activity codes apply -- general, wholesale (0.50%), or insurance commissions (0.15%)?
3. Is the client on Oahu (0.5% county surcharge baked into the 4.5% rate)?
4. Is GET being passed through to customers, and if so is the pass-through being recognized as additional gross income subject to GET again?
5. Are exemptions being claimed only where the Schedules of GET Exemptions and Deductions actually provide them?

## Sources

| Source | URL | Read on |
|---|---|---|
| Hawaii Department of Taxation -- General Excise Tax (rates, county surcharge, wholesale and insurance-commission rates, economic nexus) | https://tax.hawaii.gov/get/ | 2026-10-28 |
| HRS §231-39 (penalties; ⅔%/month interest) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm | 2026-10-28 |

Not yet confirmed: the HRS ch. 237 statutory rate section text (capitol.hawaii.gov rate-limited the ch. 237 pages this run, so rates are cited to the DOTAX tax-authority page); the destination-based sourcing statement (v0.2 asserted destination sourcing -- not stated on the archived page); the ~4.166% effective pass-through rate (arithmetic, not published); specific category exemptions such as prescription drugs or groceries (governed by the Schedules of GET Exemptions and Deductions, not extracted this run); the current periodic-return due dates and the SST (Streamlined Sales Tax) non-membership statement (v0.2 assertion); and specific GET penalty provisions. None of these is asserted in the body because none could be tied to an archived primary source this run.

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
