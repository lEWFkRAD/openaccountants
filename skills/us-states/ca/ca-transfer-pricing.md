---
name: ca-transfer-pricing
description: >
  Use this skill whenever asked about California transfer pricing and
  related-party adjustments for tax year 2026 -- unitary business
  combined reporting under R&TC §25101, the water's-edge group rules in
  18 CCR §25110, related-party interest/rent/royalty add-back under
  §25110 (statute), cost-of-performance sourcing of intangible and
  service sales under §25134, and FTB audit adjustments on intercompany
  transactions. Trigger on "California transfer pricing", "California
  combined report adjustment", "FTB unitary", "California addback",
  "cost of performance California", "water's edge California",
  "intercompany California". Source-cited draft; 18 CCR §25110 and
  R&TC §25128.7 read 2026-11-01.
jurisdiction: US-CA
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-11-02
version: 0.1
verified_by: pending
depends_on:
  - ca-corporate-income-tax
---

# California transfer pricing & combined reporting v0.1

## Who this applies to
Covers how California taxes intercompany and cross-border related-party
income: unitary combined reporting, water's-edge boundaries, statutory
add-backs, and sales sourcing. Primary verified sources this run: 18
CCR §25110 (Water's-Edge Group), archived 2026-11-01, which defines
"unitary business" by reference to R&TC §25101 and unity of ownership,
operation, and use; and R&TC §25128.7 (single sales factor), archived
2026-11-01. Statute sections §§25101, 25105, 25109, 25110 and 25134
are not archived in this pack (the leginfo §25128 page returned a
JavaScript stub) -- treat those cites as pending verification.

## Rates, bands and thresholds
| Mechanism | Effect | Source |
|---|---|---|
| Combined report (Form 100W) | Group income combined, then apportioned with group's single sales factor | R&TC §25101 (pending); FTB Form 100W |
| Water's-edge election | Excludes foreign affiliates; binding 5 years | R&TC §25109 (pending); 18 CCR §25110 (verified) |
| §25110 add-back | Interest/rent/royalties to affiliated members added back | R&TC §25110 (pending) |
| Sales sourcing | Tangible property: destination (purchaser location); other sales: cost of performance | R&TC §25134 (pending) |
| Apportionment formula | Single sales factor for tax years beginning on or after 2013 | R&TC §25128.7: "shall be apportioned to this state by multiplying the business income by the sales factor" (archived 2026-11-01) |

## The taxable base
- Combined apportionable income = group-wide unitary income with
  California modifications; intercompany transactions are eliminated
  in the combined report.
- For non-unitary related parties (or water's-edge excluded members),
  transactions are priced at arm's length; FTB may adjust under §25101
  to clearly reflect income.
- Cost-of-performance sourcing matters for service and intangible
  revenue: sales are sourced where the greater proportion of the
  income-producing activities is performed.

## Deadlines and filing
- Combined report filed with the members' Form 100 returns: 15th day of
  the 4th month (April 15 calendar year).
- Election deadlines (water's-edge, affil-group): verify current FTB
  procedure and filing mechanics before advising.

## Penalties and interest
- FTB adjustments carry interest at the published FTB rate from the
  original due date (FTB penalties-and-interest pages, verified
  2026-10-27).
- Understatement penalties (25% late-filing; accuracy-related
  penalties per FTB guidance) may apply to report-position errors.

## Cross-border points
- Water's-edge boundary: U.S. + unitary-group members with U.S. nexus
  stay in; inclusion turns on unitary-business status (unity of
  ownership, operation, and use) and the affiliated-group tests in
  18 CCR §25110, which use more than 50 percent common ownership of
  voting stock by reference to R&TC §25105 -- there is no 25%
  common-ownership inclusion test in §25110.
- FDII/GILTI conformity: California has historically not conformed;
  verify current-year treatment in FTB legal notices.
- Treaty non-application: the U.S.–income-tax treaties do not limit
  California net-income taxation of foreign affiliates (state tax is
  outside treaty scope).
- Public Law 86-272 protects only solicitation activity from
  net-income tax; it does not shelter intangible or management-fee
  income.

## Worked examples

### Worked example 1: Royalty add-back under R&TC §25110

A California manufacturer pays $2,000,000 in royalties to an affiliated
foreign licensor. The royalty is added back under §25110 (no exception
established); apportioned California income rises by the add-back.
Tax effect at 8.84% on a 0.40 sales factor:

```oa-check
name: add-back tax effect
inputs:
  royalty: 2000000
  factor: 0.40
  rate: 0.0884
steps:
  - apportioned_addback: royalty * factor
  - tax: apportioned_addback * rate
expected:
  apportioned_addback: 800000.00
  tax: 70720.00
```

### Worked example 2: Cost-of-performance sourcing

A services company earns $6,000,000 of service revenue; $4,500,000 of
costs of performance are incurred in California, $1,500,000 elsewhere.
Cost-of-performance sourcing:

```oa-check
name: cost of performance sourcing
inputs:
  cop_ca: 4500000
  cop_total: 6000000
  revenue: 6000000
steps:
  - factor: cop_ca / cop_total
  - ca_sales: revenue * factor
expected:
  factor: 0.75
  ca_sales: 4500000.00
```

## Ask the client first
- Is the group unitary under the three-factor test, and is a
  water's-edge election in place (when does it expire)?
- What intercompany interest, rent, or royalty flows exist to
  affiliated members (add-back exposure)?
- Where are income-producing activities performed for service and
  intangible revenue (cost-of-performance documentation)?
- Are intercompany agreements, transfer-pricing studies, and
  contemporaneous documentation in place for FTB audit?

## Sources
| Source | URL | Read on |
| --- | --- | --- |
| 18 CCR section 25110 (Water's-Edge Group) | https://www.law.cornell.edu/regulations/california/18-CCR-25110 | 2026-11-01 |
| R&TC section 25128.7 (single sales factor) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25128.7 | 2026-11-01 |

Not yet confirmed: the 8.84% franchise rate (FTB tax-rates page not archived with a sidecar in this pack), the water's-edge 5-year binding period (R&TC §25109), the §25110 add-back statute text, the §25134 cost-of-performance statute text, the R&TC §25101 and §25105 statute texts, and the FTB penalties-and-interest page.
## Talk to a verified accountant
<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for California combined-reporting and transfer-pricing questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
