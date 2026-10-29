---
name: ar-transfer-pricing
description: >
  Use this skill whenever asked about Arkansas transfer pricing for
  tax year 2026 — Arkansas' separate-entity UDITPA framework as
  amended by SB 567 / Act 719 of 2025 (market-based sourcing for
  services and intangibles, economic nexus for non-resident
  entities), the affiliated-group adjustment provisions, and how
  related-party pricing is policed without mandatory combined
  reporting. Trigger on "Arkansas transfer pricing", "Arkansas
  UDITPA", "Arkansas market based sourcing", "Arkansas addback",
  "Arkansas affiliated group", "Arkansas separate entity reporting".
  Source-cited draft; DFA corporate page read 2026-10-27; statute
  text needs-sources.
jurisdiction: US-AR
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ar-corporate-income-tax
---

# Arkansas transfer pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Arkansas polices related-party economics through its **UDITPA-based apportionment and affiliated-group provisions**, not through mandatory combined reporting: Arkansas has historically been a **separate-entity filing state** (confirm current status — **needs-sources**). The 2025 reform (**SB 567 / Act 719**, signed 2025-04-16) amended the UDITPA adoption to add **market-based sourcing for sales of services and intangibles** (location where delivered to the customer) and an **economic nexus filing threshold for non-resident corporations or partnerships** (all read from the DFA Corporation Income Tax page, fetched 2026-10-27). **Source status:** the reform narrative is read from the DFA page; the affiliated-group adjustment statute (Ark. Code Ann. §26-51-904 — intangible-expense/affiliate adjustments; cite and text **needs-sources**) and the unitary-combination status were not retrievable from this host this run.

## 2. Who applies

- Every corporation filing Arkansas separately with related-party transactions — intercompany pricing is tested through the UDITPA adjustments on AR-1100ADJ and the affiliated-group provisions (text **needs-sources**).
- Post-Act 719: **non-resident corporations and partnerships over the economic-nexus threshold** (amount **needs-sources**) are pulled into the filing system, making sourcing rules the main TP lever.
- Groups that are unitary do NOT automatically combine in Arkansas (separate-entity state — confirm, **needs-sources**); the risk sits in the sales-factor numerator and affiliate-expense adjustments.

## 3. Mechanics

| Item | Rule | Source |
|---|---|---|
| Filing method | separate-entity (confirm) | UDITPA as adopted — **needs-sources** |
| Services/intangibles sourcing | market-based: customer delivery location (Act 719) | DFA page, read 2026-10-27 |
| Affiliate expense adjustments | intangible/management-fee addback provisions | Ark. Code §26-51-904 — **needs-sources** |
| Alternative apportionment | available on request (DFA "Request for Alternative Apportionment" link, read 2026-10-27) | DFA page |
| Throwback/throwout | confirm post-Act 719 | **needs-sources** |

## 4. Deadlines

TP adjustments ride the AR-1100 calendar (see `ar-corporate-income-tax`). Alternative-apportionment requests are filed with (or before) the return (procedure **needs-sources**).

## 5. Penalties and interest

No standalone TP documentation penalty; exposure runs through underpayment penalties/interest (§26-18-403 — percentages **needs-sources**). Common failure modes: (1) keeping place-of-performance sourcing for services after Act 719; (2) management fees to a low-tax affiliate with no substance analysis under the affiliate-adjustment provisions; (3) assuming separate-entity filing means related-party pricing is unexamined — the sales factor is where DFA looks.

## 6. Cross-border interactions

- Market sourcing makes the customer's location the driver — align contracts, order-to-cash data, and the sales-factor schedule (see `ar-cross-border`).
- Federal §1059A-style intangible limitations carry in through federal taxable income; Arkansas-specific affiliate adjustments are separate (**needs-sources**).

## 7. Worked examples

Related-party royalty: OpCo (Arkansas operations) pays $300,000 in royalties to AffiliateCo (no Arkansas nexus). Arkansas-apportionable income before the royalty is $1,200,000; Arkansas sales fraction 0.60:

```oa-check
name: AR royalty effect on apportioned income
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

If DFA adjusts the royalty out under the affiliate provisions (illustrative full addback):

```oa-check
name: AR addback delta illustrative
inputs:
  apportioned_after: 540000
  royalty: 300000
  factor: 0.60
  rate: 0.01
steps:
  - addback_effect: royalty * factor
  - extra_tax: addback_effect * rate
expected:
  addback_effect: 180000.00
  extra_tax: 1800.00
```

## 8. Ask the client

- Are service and intangible revenues now sourced to the customer-delivery location for post-2025 years?
- Do affiliate royalty/management-fee arrangements have substance documentation for a §26-51-904 review?
- Has anyone tested the group against the Act 719 economic-nexus threshold?
- Is an alternative-apportionment request a better answer than the statutory fraction?

## Sources

1. DFA Corporation Income Tax page: https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/ (200, text read 2026-10-27 — Act 719 market-based sourcing, economic nexus, alternative apportionment request link)
2. Ark. Code Ann. §26-51-901 et seq. (UDITPA as adopted): https://www.arkleg.state.ar.us/Code (empty/500 from this host — **needs-sources**)
3. Act 719 of 2025: https://www.arkleg.state.ar.us/Acts/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf (200 but 0 bytes from this host — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Arkansas related-party and sourcing questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
