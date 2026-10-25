---
name: ma-transfer-pricing-combined-reporting
description: >-
  Use when a Massachusetts corporate group has related-party flows and needs
  the 2026 combined-reporting answer: when an affiliated group must file on a
  combined unitary basis, the 80%/55% ownership and unitary-business tests,
  and how intercompany transactions disappear in the combination. Trigger on
  Massachusetts combined reporting, 830 CMR 63.03, M.G.L. c.63 s.33A,
  unitary group Massachusetts, water's-edge. Massachusetts has no OECD-style
  method statute; it polices connected-party income by forcing combination.
  Source-cited draft with needs-sources caveat on statute/reg text.
jurisdiction: US-MA
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---

# Massachusetts transfer pricing (combined reporting)

## 1. Who this applies to

- C corporations and corporate groups doing business in Massachusetts where an affiliated group meets the ownership and unitary-business tests (M.G.L. c.63 §33A; 830 CMR 63.03 — **needs-sources**: malegislature.gov and the mass.gov regulation page returned 404 site-wide from the drafting environment on 2026-10-25; rule statements below are corroborated by the existing `ma-corporate-excise` skill, which describes combined unitary reporting).
- Out-of-scope: standalone corporations with no unitary affiliates (they file Form 355 on a stand-alone basis); non-corporate entities (the excise regime is corporate).

## 2. Core rules and rates

- **Excise rate:** 8.25% of federal taxable income with modifications (ma-corporate-excise, read 2026-10-25).
- **Combined reporting is mandatory** when the group qualifies: the reporting corporation files Form 355 on a combined basis, not each member separately (830 CMR 63.03 — needs-sources).
- **Affiliated-group tests** (830 CMR 63.03 — needs-sources): more than 50% common ownership, and the group conducts a unitary business (integration, interdependence, or mutual interdependence across members).
- **Water's-edge:** the combination is limited to unitary-group members' income, with the standard water's-edge boundary for foreign affiliates (830 CMR 63.03 — needs-sources).
- **Intercompany elimination:** in a proper combination, intercompany dividends, interest, rents, and royalties between unitary members are eliminated — Massachusetts does not run an arm's-length addback regime because the combination itself neutralises most connected-party planning (ma-corporate-excise, read 2026-10-25).

## 3. Base and apportionment

- Combined apportionable income = the unitary group's combined federal taxable income with Massachusetts modifications, apportioned to Massachusetts by the single sales factor (ma-corporate-excise, read 2026-10-25).
- The unitary-business principle pulls the entire group's income into the apportionment base when a member's business is part of a unitary business (830 CMR 63.03 — needs-sources).

## 4. Deadlines

- Form 355 combined return: 15th day of the 4th month after year end (calendar year: 15 April); extensions to 15 November with payment by the original date (ma-corporate-excise, read 2026-10-25).
- Combined groups file one Form 355 for the reporting member; members are jointly liable for the combined tax (830 CMR 63.03 — needs-sources).

## 5. Penalties and interest

- Failure to file combined when required exposes the group to the excise difference plus late-filing/late-payment penalties and interest at the federal underpayment rate plus add-on (M.G.L. c.65C — **needs-sources**, 404 on 2026-10-25). Treat the exact rate as unverified until re-checked.

## 6. Cross-border and federal overlay

- P.L. 86-272 protects solicitation-only activity from net-income excise but does not change the combined-reporting analysis for the rest of the group (needs-sources).
- No state treaty power; US treaties can touch nonresident-member income but not the corporate combination itself.
- Federal §482 adjustments do not automatically flow into the Massachusetts combination — the combination is computed under Massachusetts rules (needs-sources).

## 7. Worked examples

**Example 1 — combined apportionment.** A unitary group's combined apportionable income is USD 4,000,000; the Massachusetts sales factor is 25%. Combined Massachusetts-basis income: 4,000,000 × 0.25 = 1,000,000. Excise at 8.25%: 1,000,000 × 0.0825 = 82,500.

```oa-check
name: ma combined apportionment
inputs:
  combined_income: 4000000
  ma_factor: 0.25
  rate: 0.0825
steps:
  - ma_base: combined_income * ma_factor
  - excise: ma_base * rate
expected:
  ma_base: 1000000.00
  excise: 82500.00
```

**Example 2 — intercompany royalty neutralised.** A Massachusetts manufacturer pays a royalty of USD 600,000 to its 100%-owned out-of-state licensor inside the same unitary group. Stand-alone, the MA entity would deduct 600,000; combined, the royalty and the licensor's matching income eliminate, so the group's combined apportionable income is unchanged at USD 4,000,000 and the Massachusetts-basis income stays 1,000,000 — the royalty moves no Massachusetts tax.

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

## 8. Ask the client first

- Ownership chain percentages between members (the >50% common-ownership test).
- Whether operations are integrated/interdependent (the unitary test) or truly separate lines of business.
- Whether any foreign affiliates are in the group (water's-edge boundary).

## 9. Sources

- M.G.L. c.63 §33A (affiliated groups): <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter63/Section33A> — **needs-sources** (404 site-wide on 2026-10-25).
- 830 CMR 63.03 unitary combined reporting: <https://www.mass.gov/regulations/830-cmr-6303-unitary-combined-reporting> — **needs-sources** (404 on 2026-10-25).
- `ma-corporate-excise` skill (8.25% rate, combined unitary reporting, single sales factor) — internal corroboration, read 2026-10-25.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
