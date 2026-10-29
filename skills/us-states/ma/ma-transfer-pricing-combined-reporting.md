---
name: ma-transfer-pricing-combined-reporting
description: >-
  Use when a Massachusetts corporate group has related-party flows and needs
  the 2026 combined-reporting answer: when an affiliated group must file on a
  combined unitary basis, the more-than-50% common-ownership and unitary-business
  tests, and how intercompany transactions disappear in the combination. Trigger
  on Massachusetts combined reporting, 830 CMR 63.32B.2, M.G.L. c.63 s.32B,
  unitary group Massachusetts, water's-edge. Massachusetts has no OECD-style
  method statute; it polices connected-party income by forcing combination.
jurisdiction: US-MA
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-29
version: 0.2
---

# Massachusetts transfer pricing (combined reporting)

## Who this applies to

- C corporations and corporate groups doing business in Massachusetts where corporations under common ownership conduct a unitary business (M.G.L. c.63 §32B; 830 CMR 63.32B.2 — statute and regulation text archived 2026-10-28).
- Out of scope: standalone corporations with no unitary affiliates (they file Form 355 on a stand-alone basis); non-corporate entities (the excise regime is corporate).

## Rates, bands and thresholds

- **Excise rate:** 8.0% of net income determined to be taxable in accordance with the chapter, for tax years beginning on or after January 1, 2012 (G.L. c.63 §39(a)(2)(iv), archived 2026-10-28).
- **Combined reporting is mandatory** when a corporation subject to tax under c.63 is engaged in a unitary business with one or more corporations subject to combination: it calculates its taxable net income as its share, attributable to the commonwealth, of the apportionable income or loss of the combined group, determined in accordance with a combined report (G.L. c.63 §32B(a), archived 2026-10-28).
- **Common ownership test:** "more than 50 per cent of the voting control of each member of the group is directly or indirectly owned by a common owner or owners" (G.L. c.63 §32B(b)(2), archived 2026-10-28).
- **Unitary business test:** "the activities of a group of 2 or more corporations under common ownership that are sufficiently interdependent, integrated or interrelated through their activities so as to provide mutual benefit and produce a significant sharing or exchange of value among them or a significant flow of value between the separate parts" (G.L. c.63 §32B(b)(1), archived 2026-10-28).
- **Intercompany elimination:** "items of income, deductions and receipts from transactions between or among members of the combined group, including but not limited to the payment of dividends, shall be eliminated" (G.L. c.63 §32B(a), archived 2026-10-28). Massachusetts does not run an arm's-length addback regime because the combination itself neutralises most connected-party planning.
- **Joint and several liability:** "Every member of the combined group shall be jointly and severally liable for the tax due from any taxpayer member under this chapter, including any interest and penalties" (G.L. c.63 §32B(e), archived 2026-10-28).

## The taxable base

- Combined apportionable income = the unitary group's combined taxable net income with Massachusetts modifications, apportioned to Massachusetts by the single sales factor (G.L. c.63 §38(c)-(d), archived 2026-10-28; see the `ma-corporate-excise` skill).
- The unitary-business principle pulls the entire group's income into the apportionment base when a member's business is part of a unitary business (G.L. c.63 §32B(a), (b)(1), archived 2026-10-28).

## Deadlines and filing

- Form 355 combined return: 15th day of the 4th month after year end (calendar year: 15 April); extensions to 15 November with payment by the original date (see `ma-corporate-excise` skill).
- Combined groups file one combined report attached to the reporting member's return; members are jointly and severally liable for the combined tax (G.L. c.63 §32B(e), archived 2026-10-28).

## Penalties and interest

- Failure to file combined when required exposes the group to the excise difference plus late-filing/late-payment penalties and interest; the exact rate schedule is listed under Not yet confirmed below.

## Cross-border points

- P.L. 86-272 protects solicitation-only activity from net-income excise but does not change the combined-reporting analysis for the rest of the group.
- No state treaty power; US treaties can touch nonresident-member income but not the corporate combination itself.
- Federal §482 adjustments do not automatically flow into the Massachusetts combination — the combination is computed under Massachusetts rules (G.L. c.63 §32B(a): items from intercompany transactions "shall be eliminated, subject to regulations as may be adopted" under §32B(f)).
- Water's-edge treatment of foreign affiliates: see Not yet confirmed below.

## Worked examples

Client facts (group income, sales factor) are hypothetical; the 8.0% rate is the confirmed §39 figure above.

**Example 1 — combined apportionment.** A unitary group's combined apportionable income is USD 4,000,000; the Massachusetts sales factor is 25%. Combined Massachusetts-basis income: 4,000,000 × 0.25 = 1,000,000. Excise at 8.0%: 1,000,000 × 0.08 = 80,000.

```oa-check
name: ma combined apportionment
inputs:
  combined_income: 4000000
  ma_factor: 0.25
  rate: 0.08
steps:
  - ma_base: combined_income * ma_factor
  - excise: ma_base * rate
expected:
  ma_base: 1000000.00
  excise: 80000.00
```

**Example 2 — intercompany royalty neutralised.** A Massachusetts manufacturer pays a royalty of USD 600,000 to its 100%-owned out-of-state licensor inside the same unitary group. Stand-alone, the MA entity would deduct 600,000; combined, the royalty and the licensor's matching income eliminate (§32B(a)), so the group's combined apportionable income is unchanged at USD 4,000,000 and the Massachusetts-basis income stays 1,000,000 — the royalty moves no Massachusetts tax.

```oa-check
name: ma intercompany royalty elimination
inputs:
  royalty: 600000
  combined_income: 4000000
  ma_factor: 0.25
steps:
  - net_effect: royalty - royalty
  - combined_after: combined_income + net_effect
  - ma_base: combined_after * ma_factor
expected:
  net_effect: 0.00
  combined_after: 4000000.00
  ma_base: 1000000.00
```

## Ask the client first

- Ownership chain percentages between members (the more-than-50% voting-control test).
- Whether operations are integrated/interdependent (the unitary test) or truly separate lines of business.
- Whether any foreign affiliates are in the group (water's-edge boundary).

## Sources

| Source | URL | Read on |
|---|---|---|
| M.G.L. c.63 §32B — Combined reporting; corporations subject to combination; apportionment of income; joint and several liability | <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section32B> | 2026-10-28 |
| M.G.L. c.63 §39 — Tax rate (8.0% income measure for tax years beginning on or after Jan 1, 2012) | <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section39> | 2026-10-28 |
| M.G.L. c.63 §38 — Determination of net income derived from business carried on within commonwealth (sales factor) | <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section38> | 2026-10-28 |
| 830 CMR 63.00 (DOR regulations, incl. 63.32B.2 Combined Reporting) — Secretary of the Commonwealth regulation publication PDF | <https://www.sec.state.ma.us/reg_pub/pdf/800/830063.pdf> | 2026-10-28 |

Not yet confirmed: the water's-edge boundary for foreign affiliates in the Massachusetts combination (830 CMR 63.32B.2 text not fully read from the archived PDF); the exact penalty and interest rate schedule for failure to file a combined return when required (M.G.L. c.63 penalty provisions not archived); whether federal §482 adjustments flow into the combined report in any circumstance.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
