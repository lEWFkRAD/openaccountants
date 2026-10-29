---
name: mi-transfer-pricing-unitary-combined
description: >-
  Use when a Michigan corporate group has related-party flows and needs the
  2026 answer: mandatory unitary combined reporting under MCL 208.1401, the
  80% common-ownership and unitary-business tests, and how intercompany
  transactions eliminate in the CIT combination. Trigger on Michigan combined
  report, unitary business group Michigan, MCL 208.1401, CIT combined filing.
  Michigan polices connected-party income by forcing combination, not by an
  arm's-length addback statute. Source-cited draft; Treasury unitary page
  verified 2026-10-25.
jurisdiction: US-MI
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---

# Michigan transfer pricing (unitary combined reporting)

## 1. Who this applies to

- Members of a **unitary business group (UBG)** subject to the Michigan Corporate Income Tax (CIT): the group files a combined CIT return (MCL 208.1401 — <https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-208-1401>, 200 on 2026-10-25; Michigan Department of Treasury unitary-business-groups page — <https://www.michigan.gov/taxes/business-taxes/cit/detail/unitary-business-groups>, 200 with content on 2026-10-25).
- Out of scope: stand-alone CIT filers with no unitary affiliates; the individual income tax (no combined reporting there).

## 2. Core rules and rates

- **CIT rate:** 6.0% (mi-corporate-income-tax, read 2026-10-25; the 4.25% figure in that skill is the historical/alternative-rate context — the operative 2026 rate is 6.0%).
- **UBG definition** (MCL 208.1401, 200 on 2026-10-25; Treasury page, 200 on 2026-10-25): a set of linked persons in which one person owns, directly or indirectly, more than 50% of another (or a common owner holds more than 50% of each) **and** they are unitary — a single integrated enterprise, interdependent or mutually interdependent, producing goods or services as an integrated business.
- **Combined filing is mandatory** for UBG members; the group's combined apportioned tax base is taxed at 6.0% (Treasury unitary page, read 2026-10-25).
- **Intercompany elimination:** transactions between UBG members (sales, rents, royalties, interest) eliminate in the combination — Michigan neutralises connected-party shifting through combination rather than an addback schedule (Treasury unitary page, read 2026-10-25).
- **Water's-edge:** the combination includes UBG members' apportionable income with the statutory water's-edge boundary (MCL 208.1401, 200 on 2026-10-25).

## 3. Base and apportionment

- Combined apportioned base = combined CIT base of UBG members, apportioned by the single sales factor (mi-corporate-income-tax, read 2026-10-25).
- The unitary principle pulls the whole group's apportionable income into one base; a member's separate-line claim fails when operations are integrated (Treasury unitary page, read 2026-10-25).

## 4. Deadlines

- Combined CIT return (Form CIT-8 with combined-report schedules): 15th day of the 4th month after year end (calendar year: 15 April); 6-month extension with payment by the original date (mi-corporate-income-tax, read 2026-10-25).

## 5. Penalties and interest

- Failure to file combined when required: the group owes the combined tax plus late-file/late-pay penalties and interest at the CIT statutory rate (MCL 208.1451 et seq. — **unverified**: legislature.mi.gov section pages render via JavaScript and the penalty text was not machine-verified on 2026-10-25; mi-corporate-income-tax corroborates the general penalty/interest framework).

## 6. Cross-border and federal overlay

- P.L. 86-272 solicitation protection applies to the Michigan net-income (CIT) tax but not to other levies; it does not dissolve UBG status for the rest of the group (Treasury CIT pages — unverified for the specific P.L. 86-272 statement).
- Federal §482 adjustments do not automatically flow into the Michigan combination (unverified).
- No state treaty power.

## 7. Worked examples

**Example 1 — combined 6% on apportioned base.** A UBG's combined CIT base is USD 2,500,000; Michigan sales factor 40%. Michigan base: 2,500,000 × 0.40 = 1,000,000. CIT: 1,000,000 × 0.06 = 60,000.

```oa-check
name: mi ubg combined cit
inputs:
  combined_base: 2500000
  mi_factor: 0.40
  rate: 0.06
steps:
  - mi_base: combined_base * mi_factor
  - cit: mi_base * rate
expected:
  mi_base: 1000000.00
  cit: 60000.00
```

**Example 2 — intercompany management fee neutralised.** An in-state manufacturer pays USD 300,000 to its UBG affiliate in another state. Stand-alone the Michigan base would drop by 300,000; combined, the fee and the affiliate's matching income eliminate, so the combined base stays 2,500,000 and the Michigan base stays 1,000,000 — no Michigan tax moves.

```oa-check
name: mi intercompany fee elimination
inputs:
  fee: 300000
  combined_base: 2500000
  mi_factor: 0.40
steps:
  - net_effect: fee - fee
  - combined_after: combined_base + net_effect
  - mi_base: combined_after * mi_factor
expected:
  net_effect: 0.00
  combined_after: 2500000.00
  mi_base: 1000000.00
```

## 8. Ask the client first

- Ownership percentages (the >50% direct/indirect test) and whether a common-owner chain links the entities.
- Whether operations are integrated (shared customers, supply chain, management) — the unitary test.
- Whether any foreign affiliates are inside the water's-edge boundary.

## Sources

- MCL 208.1401 (unitary business groups): <https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-208-1401> — 200 on 2026-10-25.
- Treasury CIT unitary business groups page: <https://www.michigan.gov/taxes/business-taxes/cit/detail/unitary-business-groups> — 200 with content on 2026-10-25.
- `mi-corporate-income-tax` skill (6.0% rate, single sales factor, deadlines) — internal corroboration, read 2026-10-25.

Not yet confirmed: MCL 208.1451 et seq. penalty/interest text (JS-rendered); specific P.L. 86-272 statement; federal §482 interaction with the Michigan combination.
- CIT penalty/interest section text — **unverified** (JS-rendered pages, 2026-10-25).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
