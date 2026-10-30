---
name: nj-transfer-pricing
description: >
  Use this skill whenever asked about New Jersey transfer pricing and
  related-party rules for tax year 2026 -- New Jersey has no standalone TP
  documentation statute; related-party economics are handled inside
  mandatory unitary combined reporting (CBT-100U): intercompany
  transactions are eliminated, the group apportions on a single sales
  factor with the Finnigan method, water's-edge / world-wide / affiliated
  group elections bind six years, captive foreign insurers are pulled into
  the water's-edge group, and the dividend exclusion (100%/50% with a 5%
  clawback) plus the §250 disallowance govern cross-border payments.
  Trigger on "New Jersey transfer pricing", "NJ combined reporting",
  "CBT-100U", "Finnigan", "water's-edge election", "world-wide unitary",
  "NJ captive insurer", "NCTI dividend exclusion".
  Source-cited draft; Division pages read 2026-10-27; mechanics corroborated
  by the existing tier-2 nj-cbt-and-bait skill (2025 CBT-100/100U
  instructions, TB-86(R), TB-88, TB-89, TB-95(R), TB-102(R), TB-109,
  TB-110(R)).
jurisdiction: US-NJ
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - nj-cbt-and-bait
---

# New Jersey transfer pricing / combined-reporting overlay v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

New Jersey has **no standalone transfer-pricing documentation requirement and no related-party addback statute** in the Maryland/Missouri sense. Because combined reporting is **mandatory** for commonly-owned unitary groups (privilege periods ending on/after 31 July 2019), most classic TP questions -- royalties, management fees, intercompany interest -- are answered **inside** the combined group by **elimination**: the transaction disappears from the group's taxable net income and only the external sales factor matters. What is left for TP planning is (a) group composition (who is in the water's-edge group), (b) the filing-method election, and (c) cross-border payments to entities outside the group. Deep mechanics live in `nj-cbt-and-bait`; this skill is the TP lens.

**Source status:** Division combined-groups revision page (5,451 chars) and CBT reform hub (13,054 chars) verified HTTP 200 and read 2026-10-27; mechanics corroborated by the tier-2 `nj-cbt-and-bait` skill verified against the 2025 CBT-100/CBT-100U instructions and TB series on 2026-10-16. (not yet confirmed)

### 2. Who applies

- **Commonly-owned unitary groups** (more than 50% common ownership, unitary business, at least one CBT filer): mandatory one CBT-100U through the managerial member; intercompany transactions eliminated.
- **Water's-edge default:** entities with significant US business operations; **captive foreign insurers** (more than 50% owned by the group and insuring group risks) and certain treaty-country electors are pulled in.
- **World-wide or affiliated-group elections:** made on a timely original return, bind the election year plus five; revocation only prospectively for reasonable cause by written request to the Director; no election by amended return.
- **Non-unitary or non-group affiliates:** transactions priced at arm's length under federal principles; NJ starts from federal taxable income, so federal §482 adjustments flow through.

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| Rate the TP lands in | 6.5% / 7.5% / 9% graduated on the whole base (see `nj-corporate-income-tax`) | 2025 CBT-100 instructions via `nj-cbt-and-bait` |
| Intercompany transactions | eliminated in the combined group; intercompany dividends also ineligible for the dividend exclusion | CBT-100U instructions via `nj-cbt-and-bait` |
| Allocation | single sales factor; **Finnigan** method for periods ending on/after 31 July 2023 -- all members' NJ receipts in the numerator, group-level rate | CBT-100U instructions via `nj-cbt-and-bait` |
| Dividend exclusion | 100% from qualified subsidiaries (≥80% vote and value); 50% band at ≥50% ownership; **5% clawback** of all dividends/deemed dividends; §250 deductions disallowed; FDDEI gross | TB-110(R) via `nj-cbt-and-bait` |
| NCTI (former GILTI) | treated as a dividend | TB-110(R) / OBBBA renaming notice via `nj-cbt-and-bait` |
| P.L. 86-272 in a group | one member's non-protected activity destroys protection for the whole group (periods ending on/after 31 July 2023) | Division revision page, read 2026-10-27 |

### 4. Deadlines

- No state TP documentation deadline.
- Filing-method election: with the **timely filed original** CBT-100U (extension does not preserve a late election).
- Federal §482 or other federal changes → report to the Division within **90 days**. (`nj-cbt-and-bait`.)
- CBT-100U due 15 May calendar-year; CBT-200-T six-month extension with 90% paid. (`nj-corporate-income-tax`.)

### 5. Penalties and interest

- No TP-specific penalty; adjustments run through the ordinary CBT regime: 5%/month late-filing (cap 25%, plus possible $100/month), 5% late payment, interest at **3% above the average predominant prime rate compounded annually**. (`nj-cbt-and-bait`.)
- Failure to report a federal change within 90 days carries interest from the original due date.

### 6. Cross-border

- **Water's-edge vs world-wide is the biggest NJ "TP" decision:** a world-wide election pulls foreign affiliates' income and factors into the group for six years; the 2023-era Division guidance (TB-109) governs.
- **Captive insurers:** group-owned foreign captives are included in the water's-edge group -- premium stripping into a low-tax captive does not shrink the NJ base.
- **Treaty override:** a treaty-country member's treaty election to be taxed as a US corporation changes its group treatment (TB-88/TB-89 lineage via the reform hub).
- **Dividend repatriation:** the 100%/50% exclusion with the 5% clawback and §250 disallowance makes NJ dividend income materially more expensive than the federal participation deduction -- model before repatriating.
- **Single sales factor + Finnigan:** move sales out of NJ and the group's NJ share falls regardless of where costs sit -- the factor, not the price, is the lever.

### 7. Worked examples

**Example 1 -- intercompany royalty inside vs outside the group.** Group member A (NJ sales factor 0.30) pays a $2,000,000 royalty to group member B (both in the water's-edge combined group). Separately, a non-group licensor receives the same royalty.

```oa-check
name: NJ royalty inside vs outside group
inputs:
  royalty: 2000000
  factor: 0.30
  rate: 0.09
steps:
  - inside_group_effect: 0
  - outside_group_effect: royalty * factor * rate
expected:
  inside_group_effect: 0.00
  outside_group_effect: 54000.00
```

Inside the combined group the royalty nets to zero (eliminated). Paying a non-group affiliate instead moves $54,000 of tax -- the group-structure question, not the price, is the NJ lever.

**Example 2 -- dividend repatriation cost.** Group repatriates $5,000,000 from a 100%-owned foreign qualified subsidiary (water's-edge group; exclusion 100% less 5% clawback).

```oa-check
name: NJ dividend clawback cost
inputs:
  dividend: 5000000
  clawback: 0.05
  rate: 0.09
steps:
  - taxable_slice: dividend * clawback
  - nj_tax: taxable_slice * rate
expected:
  taxable_slice: 250000.00
  nj_tax: 22500.00
```

Even a "100% excluded" dividend carries the 5% clawback -- $22,500 at the 9% rate (plus any §250 federal deduction lost, which NJ disallows anyway).

### 8. Ask the client

1. Is the group unitary and commonly owned -- is a CBT-100U required and filed through a registered managerial member?
2. Which filing method, elected when, bound until when? Is a world-wide election on the table?
3. Any captive insurer or treaty-country member inside the water's-edge perimeter?
4. Repatriation plans -- has the 5% clawback and §250 disallowance been modeled?
5. Any federal §482 audit in progress -- is the 90-day NJ reporting tickler live?

### 9. Sources

1. Existing tier-2 skill `nj-cbt-and-bait` (combined mechanics, elections, Finnigan, dividend exclusion, TB citations): repo `skills/us-states/nj/nj-cbt-and-bait.md` (verified 2026-10-16).
2. NJ Division of Taxation, Revision to Division Policy on Combined Groups and P.L. 86-272: <https://www.nj.gov/treasury/taxation/cbt/combinedgroupsrevision.shtml> -- 200, read 2026-10-27.
3. NJ Division of Taxation, CBT reform hub (TB-86(R), TB-88, TB-89, TB-95(R), TB-102(R), TB-109 links): <https://www.nj.gov/treasury/taxation/cbt/cbtreform.shtml> -- 200, read 2026-10-27.
4. CBT-100U 2025 instructions: <https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf> -- cited via `nj-cbt-and-bait`; not re-fetched this run.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for New Jersey combined-group and cross-border payment questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

## Rates, bands and thresholds

Not yet confirmed against archived sources.

## The taxable base

Not yet confirmed against archived sources.

## Deadlines and filing

Not yet confirmed against archived sources.

## Penalties and interest

Not yet confirmed against archived sources.

## Cross-border points

Not yet confirmed against archived sources.

## Worked examples

Not yet confirmed against archived sources.

## Ask the client first

Not yet confirmed against archived sources.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.


| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | -- | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
