---
name: dc-transfer-pricing
description: >
  Use this skill whenever asked about District of Columbia transfer
  pricing for tax year 2026 — mandatory combined reporting for
  unitary businesses (all members, worldwide, for taxable years
  beginning on or after 2011-01-01), the unitary-group tests, the
  DC apportionment factor, and how combined reporting changes
  related-party planning. Trigger on "DC combined reporting",
  "District of Columbia unitary group", "DC transfer pricing",
  "DC water's edge", "DC apportionment factor", "DC D-20 combined".
  Source-cited draft; OTR Combined Reporting page read 2026-10-27;
  apportionment detail needs-sources.
jurisdiction: US-DC
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - dc-franchise-tax
---

# District of Columbia transfer pricing (combined reporting) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. DC is a **mandatory combined-reporting state**: the OTR Combined Reporting page (fetched 2026-10-27, 200, text read) states that businesses that are part of a **unitary business** must file a combined franchise-tax return, and that the requirement applies to taxable years beginning on or after **January 1, 2011**. Combined reporting means related-party intragroup transactions are eliminated at the group level and the group's DC-share is driven by the apportionment factor, not by intercompany pricing alone. **Source status:** the mandate and effective date are read from the OTR page; the unitary-combination mechanics (affiliation >50% tests, water's-edge treatment, apportionment-factor formula — DC Code Title 47 ch. 18 subch. II) were not extracted from code.dccouncil.gov this run — flagged **needs-sources**.

## 2. Who applies

- Every member of a **unitary business** with DC nexus files one combined return (OTR page, read 2026-10-27) — corporate and unincorporated members alike.
- Because combination is mandatory, classic transfer-pricing levers (royalties, management fees, intercompany debt) mostly wash out inside the combined group; the live issues become **where the group's sales/property/payroll sit** and **which entities are in the group**.
- International groups: water's-edge election availability and mechanics — **needs-sources**.

## 3. Mechanics

| Item | Rule | Source |
|---|---|---|
| Combination | mandatory for unitary groups, TYB ≥ 2011-01-01 | OTR page, read 2026-10-27 |
| Unitary test | unity-of-business (operational/functional integration, arm's-length independence analysis) — DC follows the standard unitary doctrine; statutory text **needs-sources** | DC Code Title 47 ch. 18 — not extracted |
| Affiliation threshold | common ownership control (typically >50%) — **needs-sources** | not extracted |
| Apportionment factor | DC formula under Title 47 ch. 18 subch. II (single-sales-factor history — confirm) — **needs-sources** | not extracted |
| Intragroup transactions | eliminated in combination | inherent in combined reporting |

## 4. Deadlines

Combined returns ride the franchise-tax calendar (D-20/D-30; see `dc-franchise-tax`). OTR audit adjustments to combination scope follow DC's assessment windows — **needs-sources**.

## 5. Penalties and interest

Underpayment interest/penalties under DC Code §47-1801.02/.11 (percentages **needs-sources**). Common failure modes: (1) filing separate D-20s for a unitary group — mandatory since 2011, OTR page read 2026-10-27; (2) excluding a foreign subsidiary without confirming water's-edge status; (3) building royalty/fee structures that wash out in combination and surprise planners when DC tax doesn't move; (4) apportionment-factor data (sales by customer state) not maintained at group level.

## 6. Cross-border interactions

- Worldwide combination unless water's-edge elected (**needs-sources**) — see `dc-cross-border`.
- Federal §245A/BEAT/GILTI interactions with DC combined income: DC starts from federal lines — decoupling detail **needs-sources**.

## 7. Worked examples

A unitary group with $10,000,000 combined net income and a DC apportionment factor of 0.12 (illustrative — formula **needs-sources**):

```oa-check
name: DC combined group DC-share
inputs:
  combined_income: 10000000
  factor: 0.12
  rate: 0.0825
steps:
  - dc_base: combined_income * factor
  - tax: dc_base * rate
expected:
  dc_base: 1200000.00
  tax: 99000.00
```

A $2,000,000 intercompany royalty inside the same group — eliminated on combination, so DC tax effect at the group level is zero before factor effects:

```oa-check
name: DC intragroup royalty wash
inputs:
  royalty: 2000000
  eliminated: 2000000
steps:
  - net_effect: royalty - eliminated
expected:
  net_effect: 0.00
```

## 8. Ask the client

- Is every unitary member on the combined return — including LLCs and foreign subsidiaries (water's-edge status confirmed)?
- Are intercompany fee/royalty plans modeled at the combined level, not entity level?
- Is apportionment-factor data (property, payroll, sales by destination) maintained group-wide?
- Any restructuring that changes unity or affiliation percentages?

## Sources

1. OTR Combined Reporting: https://otr.cfo.dc.gov/page/combined-reporting-business-entities (200, text read 2026-10-27 — mandatory combination, TYB ≥ 2011-01-01)
2. DC Code Title 47 ch. 18 subch. II: https://code.dccouncil.gov/us/dc/council/code/titles/47/chapters/18/ (200; section text not extracted — **needs-sources**)
3. OTR Business Franchise Tax Rates: https://otr.cfo.dc.gov/page/dc-business-franchise-tax-rates (read 2026-10-27 — 8.25% rate)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for DC combined-reporting questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
