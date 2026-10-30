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
  "intercompany California". Source-cited draft; 18 CCR §25110 read
  2026-10-27.
jurisdiction: US-CA
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ca-corporate-income-tax
---

# California transfer pricing & combined reporting v0.1

## Who this applies to
Covers how California taxes intercompany and cross-border related-party
income: unitary combined reporting, water's-edge boundaries, statutory
add-backs, and sales sourcing. Primary verified source this run: 18
CCR §25110 (Water's-Edge Group) via Cornell LII (200, 2026-10-27),
which defines "unitary business" by reference to R&TC §25101 and
federal unitary-combination case law. Statute sections cited below
(§§25101, 25110, 25134) returned 403 to this agent from leginfo on
2026-10-27 -- treat as pending verification.

## Rates, bands and thresholds
| Mechanism | Effect | Source |
|---|---|---|
| Combined report (Form 100W) | Group income combined, then apportioned with group's single sales factor | R&TC §25101 (pending); FTB Form 100W |
| Water's-edge election | Excludes foreign affiliates; binding 5 years | R&TC §25109 (pending); 18 CCR §25110 (verified) |
| §25110 add-back | Interest/rent/royalties to affiliated members added back | R&TC §25110 (pending) |
| Sales sourcing | Tangible property: destination (purchaser location); other sales: cost of performance | R&TC §25134 (pending) |
| Apportionment formula | Single sales factor | Prop 66 (2023+); R&TC §25128 (pending) |

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
  stay in; combined-report-unitary and 25% common ownership tests
  determine inclusions (18 CCR §25110 -- verified definitions).
- FDII/GILTI conformity: California has historically not conformed;
  verify current-year treatment in FTB legal notices.
- Treaty non-application: the U.S.–income-tax treaties do not limit
  California net-income taxation of foreign affiliates (state tax is
  outside treaty scope).
- Public Law 86-272 protects only solicitation activity from
  net-income tax; it does not shelter intangible or management-fee
  income.

## Worked examples
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

Not yet confirmed:  FTB -- Corporation Tax Rates | https://www.ftb.ca.gov/file/business/tax-rates.html ;  FTB -- Penalties and Interest | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html ; the 8.84% rate, the 18 CCR §25110 water's-edge text cited from Cornell LII, and the R&TC §§25101, 25109, 25110, 25128 and 25134 statute cites (leginfo 403 on 2026-10-27) are not yet confirmed against archived sources.
## Talk to a verified accountant
<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for California combined-reporting and transfer-pricing questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
