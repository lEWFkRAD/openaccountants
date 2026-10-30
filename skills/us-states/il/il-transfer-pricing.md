---
name: il-transfer-pricing
description: >
  Use this skill whenever asked about Illinois transfer pricing and
  unitary combined reporting for tax year 2026 -- mandatory combined
  reporting for unitary business groups via Illinois Schedule UB, the
  Schedule 80/20 related-party expense addback, the 2026 Finnigan
  apportionment change for unitary groups, and the absence of a
  standalone state documentation regime. Trigger on "Illinois unitary",
  "Schedule UB", "Illinois combined reporting", "Schedule 80/20",
  "Illinois addback", "Finnigan Illinois", "Illinois transfer
  pricing". Source-cited draft; IL-1120 instructions PDF read
  2026-10-27.
jurisdiction: US-IL
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - il-corporate-income-tax
---

# Illinois transfer pricing / unitary combined reporting v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 27 October 2026. Illinois is a **mandatory combined-reporting** state: members of a unitary business group combine on Illinois Schedule UB (Combined Apportionment for Unitary Business Group). Related-party base erosion is policed by **Schedule 80/20** (addback of interest, intangible-expense, and service-fee payments to related affiliates, with statutory exemptions). Illinois has no separate transfer-pricing documentation statute. **Source status:** the IL-1120 instructions PDF (24 pages) was text-read 2026-10-27 -- the unitary-filer mechanics, Schedule UB/80/20 references, and the **Finnigan** apportionment change effective for tax years ending on/after 2025-12-31 are read from that PDF. Statute-level text (35 ILCS 5 Art. III-bis unitary definitions; Art. IV 80/20) is JS-rendered on ILGA --  for definitional tests.

### Who this applies to

- **Unitary business group members**: a group of corporations affiliated through common ownership and operating as a unitary business (income/loss combined on Schedule UB). The affiliation and unitarity tests sit in 35 ILCS 5 Art. III-bis --  for the current ownership-percentage and factor-based tests.
- **Non-unitary filers** still face Schedule 80/20 addbacks on related-party payments (IL-1120 Step 1 Line M; instructions read 2026-10-27).
- Combined groups file one IL-1120 marked "Unitary Filer" with Schedule UB attached; the form **prohibits** unitary filers from using the non-unitary "income derived inside Illinois only" shortcut.

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Combined tax rate | 7.0% income + 2.5% replacement = 9.5% on combined Illinois net income | IL-1120 PDF, read 2026-10-27 |
| Combined apportionment | one sales-factor fraction for the group via Schedule UB | IL-1120 instructions, read 2026-10-27 |
| Finnigan method | for TYE on/after 2025-12-31, unitary groups include all Illinois income/loss from all group members in the sales-factor numerator; throwback/throw-out applied per Finnigan | IL-1120 instructions, read 2026-10-27 |
| 80/20 addback | interest + intangible expenses + service fees paid to related affiliates added back; exemptions (e.g., unitary-group exception, conduit) per statute | instructions read 2026-10-27; exemption text  |
| Documentation regime | none standalone | absence noted |

## The taxable base

The base follows the federal starting point with Illinois modifications; see Rates, bands and thresholds above and the archived IL-1040/IL-1120 instructions in Sources.

## Deadlines and filing

- Schedule UB and Schedule 80/20 attach to the IL-1120 -- same due dates as the return (15th day of 4th month; April 15 calendar-year).
- Estimated payments at the 9.5% combined worksheet rate (IL-1120-V) quarterly.
- No separate TP documentation deadline.

## Penalties and interest

Underpayment rides the IL-2220 estimated-penalty regime (see `il-corporate-income-tax`); percentage penalty/interest rates . Common failure modes: (1) assuming federal consolidated ≠ Illinois unitary -- the tests differ; (2) missing the 2026 Finnigan numerator change for unitary groups; (3) paying related-party royalties/management fees without running the 80/20 exemption analysis; (4) double-counting intercompany sales in the combined numerator.

## Cross-border points

- **Water's-edge**: Illinois combined reporting follows its unitary definition; whether foreign members are included turns on the Art. III-bis affiliation tests --  (confirm current water's-edge treatment before structuring).
- 80/20 applies to payments to related foreign affiliates as well (instructions describe related-party expenses generally; foreign-specific carve-outs ).
- PTE and pass-through income inside a unitary group flow through the combined computation (K-1-P/K-1-T credits on IL-1120 Lines 61c–61d verified on form).

## Worked examples

A unitary group's combined Illinois sales factor is 0.30 on $10,000,000 combined net income:

```oa-check
name: IL combined tax unitary group
inputs:
  combined_ni: 10000000
  factor: 0.30
  rate: 0.095
steps:
  - il_income: combined_ni * factor
  - tax: il_income * rate
expected:
  il_income: 3000000.00
  tax: 285000.00
```

A non-unitary filer pays $500,000 of related-party management fees added back under 80/20, apportioned at 20%:

```oa-check
name: 80/20 addback effect
inputs:
  addback: 500000
  app: 0.20
  rate: 0.095
steps:
  - il_added: addback * app
  - tax_up: il_added * rate
expected:
  il_added: 100000.00
  tax_up: 9500.00
```

## Ask the client first

- Is the group unitary under Illinois tests (not just federally consolidated)? Pull the Art. III-bis affiliation analysis.
- Have intercompany interest, royalties, and service fees been run through Schedule 80/20 exemptions?
- Is the 2026 Finnigan sales-factor numerator change reflected in the UB computation?
- Any foreign affiliates -- what is the water's-edge position?

## Sources

| Source | URL | Read on |
|---|---|---|
| IL-1120 instructions (unitary, Schedule UB, 80/20, Finnigan) | https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/business/corporate/il-1120-instr.pdf | 2026-10-27 |
| Form IL-1120 (Unitary Filer box, Schedule UB/80/20) | https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/business/corporate/il-1120.pdf | 2026-10-27 |

Not yet confirmed: 35 ILCS 5 Art. III-bis definitional tests (JS-rendered)
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
