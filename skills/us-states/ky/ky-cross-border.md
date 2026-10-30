---
name: ky-cross-border
description: >
  Use this skill whenever asked about Kentucky cross-border taxation for tax year 2026 -- corporate nexus and P.L. 86-272 protection, the unitary combined mandate's reach over out-of-state affiliates, nonresident individual taxation of Kentucky-source income, nonresident withholding by pass-through entities (Form 740NP-WH), the LLET credit for out-of-state LLC members, and credits for taxes paid to other states. Trigger on "Kentucky nexus", "Kentucky nonresident", "Kentucky LLET credit out of state", "nonresident withholding Kentucky", "moving to Kentucky taxes", "Kentucky credit for taxes paid". ALWAYS load us-tax-workflow-base first.
version: 0.3
jurisdiction: US-KY
category: cross-border
tax_year: 2026
last_updated: 2026-10-28
tier: 2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - ky-income-tax
---

# Kentucky cross-border (nexus, non-residents, other-state taxes), tax year 2026

> **Source-cited draft.** Built from KRS 141.020, 141.070, 141.0401, 141.202, 15 U.S.C. §381, and DOR pages, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

- **Out-of-state corporations** inside a Kentucky unitary group: combined filing is mandatory for tax years beginning on or after 1 January 2019 (KRS 141.202; DOR corporate page) -- membership, not physical presence, drives the exposure.
- **Corporations with Kentucky activity** outside a unitary group: separate-entity filing with Kentucky-source apportionment (KRS 141.120), subject to P.L. 86-272 (15 U.S.C. §381) for solicitation-only activity.
- **Nonresident individuals** and **nonresident partners/members of Kentucky pass-through entities**: taxed on Kentucky-source income; the entity may have a withholding obligation (see below).
- **Out-of-state members of Kentucky LLCs**: the entity pays the LLET; members take the entity-level credit on their Kentucky returns (KRS 141.0401).

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Corporate rate | Flat 5% on apportioned Kentucky income (TYB on/after 2018) | KRS 141.040(2) |
| Individual rate | Flat income tax: 4% for 2025, 3.5% for 2026 | KRS 141.020(2)(e)–(f) |
| Nonresident individual base | Kentucky-source income only (Form 740-NP); residents taxed "upon his or her entire net income" | KRS 141.020(1), (4) |
| Nonresident withholding by PTEs | Required on each nonresident individual partner/member/shareholder's distributive share at "the maximum rate provided in KRS 141.020"; Form 740NP-WH filed "by the 15th day of the fourth month following the close of the tax year" | KRS 141.206(5)(a) per DOR Nonresident Withholding page |
| LLET | $175 minimum; $0.095 per $100 of Kentucky gross receipts above the brackets; credited against income tax | KRS 141.0401 |
| Credit for taxes paid to other states | Resident credit: lesser of Kentucky tax on the double-taxed income and the other state's tax | KRS 141.070(1) |

## The taxable base

Residents are taxed on entire net income wherever earned (KRS 141.020(1)). Nonresidents are taxed only on Kentucky-source income; KRS 141.020(4) provides that for nonresidents, "The remainder of the income received by the nonresident shall be deemed nontaxable by this state." Corporations apportion by a receipts-only fraction (KRS 141.120(9)). Nonresident C-corporations that are partners or members of pass-through entities are not subject to PTE withholding "but still have a Kentucky filing obligation under the doing business standard of KRS 141.010(13)" (DOR Nonresident Withholding page).

## Deadlines and filing

- Form 720 (combined or separate): April 15 for calendar-year filers; estimated installments 25% x 4 (DOR corporate page).
- Federal audit final determination: amended Kentucky return within 180 days (DOR corporate page).
- Nonresident withholding: Form 740NP-WH (with copy A of PTE-WH for each nonresident) by the 15th day of the fourth month after year end (DOR Nonresident Withholding page).
- Individual 740 / 740-NP follow the April 15 due date (2025 Form 740 instructions).

## Penalties and interest

Late payment/filing: 2% per 30 days or fraction, capped at 20%, $10 minimum (DOR Penalties, Interest and Fees page). Interest on unpaid tax: 10% for 2025, 9% for 2026 (DOR interest notices under KRS 131.183(2)(a)2). Common failure modes: (1) an out-of-state parent assuming no Kentucky exposure while a unitary member operates there; (2) a Kentucky PTE skipping nonresident withholding on distributive shares; (3) LLC members missing the LLET credit on their own returns; (4) double taxation where the work state and residence state both tax -- run the KRS 141.070 credit analysis in both directions.

## Cross-border points

- **P.L. 86-272** (15 U.S.C. §381): "No State ... shall have power to impose ... a net income tax on the income derived within such State by any person from interstate commerce if the only business activities within such State ... are either, or both, of the following: (1) the solicitation of orders ... for sales of tangible personal property, which orders are sent outside the State for approval or rejection, and, if approved, are filled by shipment or delivery from a point outside the State." Services, digital goods, and in-state fulfillment are unprotected.
- **Unitary reach**: combined group is corporations with more than 50% common voting-stock ownership in a unitary business, filed waters-edge (KRS 141.202) -- map every affiliate before assuming exposure.
- **Reciprocity**: Kentucky has reciprocal individual income tax agreements with neighboring states; a nonresident employee claims exemption by filing the certificate of non-residence (Form 42A809) with the Kentucky employer, and the employer then withholds the home state's tax. Confirm the current reciprocal-state list and the form against DOR guidance before relying on it (see Not yet confirmed).
- **Foreign parents**: no Kentucky-specific treaty provisions; federal ECI/treaty analysis governs.

## Worked examples

### Example 1: nonresident Kentucky-source wages (hypothetical facts)

An Indiana resident works 40 of 240 workdays at a Louisville client site on $120,000 of wages. Kentucky-source fraction 40/240 = 1/6; Kentucky nonresident tax on the Kentucky-source portion at the 2026 rate of 3.5%: $120,000 × 1/6 × 3.5% = $700.

```oa-check
name: IN resident 40 KY workdays, 2026 rate
inputs:
  wages: 120000
  ky_days: 40
  total_days: 240
  rate: 0.035
steps:
  - src_frac: ky_days / total_days
  - ky_wages: wages * src_frac
  - ky_tax: ky_wages * rate
expected:
  src_frac: 0.16666667
  ky_tax: 700.00
```

### Example 2: LLET credit at member level (hypothetical facts)

A Texas-owned LLC with Kentucky gross receipts of $8,000,000 pays LLET of $8,000,000 / 100 × $0.095 = $7,600. The entity-level credit flows to its two members' Kentucky income tax positions.

```oa-check
name: LLET credit at member level
inputs:
  receipts: 8000000
  per_hundred: 0.095
  members: 2
steps:
  - llet: receipts / 100 * per_hundred
  - per_member: llet / members
  - credit_total: per_member * members
expected:
  llet: 7600.00
  per_member: 3800.00
  credit_total: 7600.00
```

## Ask the client first

- Which affiliates sit inside the Kentucky unitary group -- and has anyone checked the 50% voting-stock test and the exceptions?
- How many workdays do remote/cross-border employees actually spend in Kentucky?
- For Kentucky PTEs: are nonresident members' distributive shares being withheld on (Form 740NP-WH/PTE-WH)?
- For LLC members: is the LLET credit being claimed on their own returns?
- Does the residence state credit Kentucky tax, and at what rate (KRS 141.070 both directions)?

## Sources

| Source | URL | Read on |
|---|---|---|
| KRS 141.020 (resident/nonresident base; 4% 2025, 3.5% 2026 rates) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.020 | 2026-10-28 |
| KRS 141.070 (credit for tax paid to other states) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.070 | 2026-10-28 |
| KRS 141.0401 (LLET; entity-level credit for members) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.0401 | 2026-10-28 |
| KRS 141.202 (unitary combined report; waters-edge) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.202 | 2026-10-28 |
| KRS 141.120 (receipts-only apportionment; market sourcing) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.120 | 2026-10-28 |
| 15 U.S.C. §381 (P.L. 86-272 solicitation protection) | https://www.law.cornell.edu/uscode/text/15/381 | 2026-10-28 |
| DOR Nonresident Withholding Tax page (KRS 141.206(5)(a); Form 740NP-WH; maximum-rate withholding) | https://revenue.ky.gov/Business/Nonresident-Withholding-Tax/Pages/default.aspx | 2026-10-28 |
| DOR Corporation Income & LLET page (combined filing; 180 days; LLET) | https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx | 2026-10-28 |
| Form 720 (Corporation Income Tax and LLET return, PDF) | https://revenue.ky.gov/Forms/720.pdf | 2026-10-28 |
| DOR Penalties, Interest and Fees page | https://revenue.ky.gov/Collections/Pages/Penalties-Interest-and-Fees.aspx | 2026-10-28 |
| DOR 2025 Form 740 instruction packet (individual due date) | https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf | 2026-10-28 |

Not yet confirmed: the current list of reciprocal states and the mechanics of Form 42A809 (v0.1 asserted six reciprocal states and Ohio Rev. Code and KRS citations; neither the reciprocal agreements nor Form 42A809's instructions were archived this run -- verify on the DOR withholding page before applying an exemption); the DOR "doing business" standard in KRS 141.010(13) beyond the quoted reference (KRS 141.010 is archived, but the subsection was not re-read for this note); local occupational tax treatment of cross-border workers (local ordinances not archived; see `ky-payroll` Not yet confirmed).

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
