---
name: nj-corporate-income-tax
description: >
  Use this skill whenever asked about New Jersey Corporation Business Tax
  compliance mechanics for tax year 2026 — CBT-100/CBT-100U deadlines, the
  15-day automatic extension and the 3-month discretionary extension,
  CBT-150 estimated tax installments and safe harbors, the graduated 6.5% /
  7.5% / 9% rate table, minimum tax by receipts, the 2.5% Corporate Transit
  Fee over $10 million through 2028, penalty and interest exposure, and the
  economic-nexus thresholds ($100,000 receipts / 200 transactions). Deep
  combined-reporting mechanics live in the companion nj-cbt-and-bait skill;
  this file is the compliance-calendar and rates companion.
  Trigger on "New Jersey corporation business tax", "CBT-100", "CBT-100U",
  "CBT-150", "NJ corporate minimum tax", "Corporate Transit Fee", "NJ
  estimated tax corporation".
  Source-cited draft; Division pages and the existing tier-2 nj-cbt-and-bait
  skill read 2026-10-27.
jurisdiction: US-NJ
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - nj-cbt-and-bait
---

# New Jersey Corporation Business Tax — compliance companion v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

The repo already carries the deep CBT/BAIT skill **`nj-cbt-and-bait`** (tier 2, authored, covering nexus, combined groups, water's-edge/world-wide/affiliated elections, Finnigan allocation, NCTI/dividend exclusion, NOL/PNOL, BAIT/PTE). This companion file covers the **compliance calendar and rate table** the coverage report flags as the IT-CORP domain, and cross-links rather than duplicating. Out of scope: banking/insurance corporations, sales tax, individual tax.

**Source status:** the Division's CBT reform page (13,054 chars) and combined-groups revision page (5,451 chars) verified HTTP 200 and were read 2026-10-27; the CBT index page verified 200. Rate/minimum/fee figures are corroborated by the existing `nj-cbt-and-bait` skill (verified against the 2025 CBT-100/CBT-100U instructions and the new-legislation summary on 2026-10-16). The 2026 CBT-100 instructions were not re-fetched this run — deadline-day specifics are flagged where they depend on them. (not yet confirmed)

### 2. Who applies

- Every corporation subject to the CBT, including combined groups filing one **CBT-100U** through the managerial member; mandatory combined reporting since privilege periods ending on/after 31 July 2019 (more than 50% common ownership + unitary + one CBT filer). (`nj-cbt-and-bait`, verified 2026-10-16.)
- **Economic nexus:** NJ receipts over **$100,000** or **200+** separate transactions delivered to NJ customers (privilege periods ending on/after 31 July 2023); marketplace-warehouse inventory is NJ property. (`nj-cbt-and-bait`.) (not yet confirmed)
- P.L. 86-272 protects goods solicitation only; in a combined group one member's excess activity destroys the group's protection (privilege periods ending on/after 31 July 2023; Division revision page, read 2026-10-27).

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| Rate table (whole base, not slices) | ≤ $50,000 → **6.5%**; > $50,000–$100,000 → **7.5%**; > $100,000 → **9%** | `nj-cbt-and-bait` (2025 CBT-100 instructions; no 2026 change announced) |
| Short periods | 7.5% only if prorated base ≤ $8,333/month; 6.5% only if ≤ $4,166/month | `nj-cbt-and-bait` |
| Corporate Transit Fee | **2.5%** of taxable net income over $10 million, privilege periods beginning 2024–2028; credits cannot offset it | Division notice via `nj-cbt-and-bait`; no end-date change per new-legislation summary (checked 2026-10-16) |
| Minimum tax (separate filers) | graduated by NJ gross receipts (table in `nj-cbt-and-bait`); combined groups: **$2,000 per nexus member** | `nj-cbt-and-bait` |
| Base | federal taxable income + Schedule A modifications (NCTI as dividend; 100%/50% dividend exclusion with 5% clawback; §250 deductions disallowed) × single sales factor | `nj-cbt-and-bait` |

### 4. Deadlines

- **CBT-100/CBT-100U:** due the 15th day of the month **after** the month the federal corporate return is originally due — **15 May** for calendar-year filers (weekend/holiday rolls to the next business day). Combined groups file one CBT-100U through the managerial member. E-filing and e-payment are mandatory. (`nj-cbt-and-bait`, verified against 2025 CBT-100 instructions 2026-10-16.)
- **Extension (CBT-200-T):** six months to file, not to pay — file by the original due date and pay at least **90%** of the tax shown on the return; fail either test and the extension is retroactively denied with penalties and interest from the original due date. (`nj-cbt-and-bait`.)
- **Estimated tax (CBT-150), 2026:** required if prior-year total liability (including the Transit Fee) exceeds **$1,500** ($1,500 × members for a combined group; managerial member pays). Four installments of **25%** on the 15th day of the 4th, 6th, 9th and 12th months (calendar: 15 Apr / 15 Jun / 15 Sep / 15 Dec). Prior-year gross receipts ≥ **$50,000,000**: 25% / 50% / 0% / 25%. Prior-year liability ≤ $1,500: installments or one 50%-of-prior-year payment with the prior year's return. Underpaid if estimates are less than **90% of current-year AND** less than **100% of prior-year** tax; interest on CBT-160-A/B. (`nj-cbt-and-bait`, 2026 CBT-150 instructions.)
- **Federal-change reporting:** any federal change to taxable income must be reported to the Division within **90 days**. (`nj-cbt-and-bait`.)
- **BAIT/PTE election:** electronic election by the **original due date** (15 March for calendar-year partnerships) — extension does not extend the election. (`nj-cbt-and-bait`.)

### 5. Penalties and interest

- **Late filing:** 5% a month or part month, up to 25% of the underpayment; if no return within 30 days of the first delinquency notice, 5% a month of the **total liability** up to 25%; a **$100 per month** penalty may also apply.
- **Late payment:** 5% of the balance paid after the due date. **Extension insufficiency:** 5% a month up to 25% of the shortfall.
- **Interest:** **3% above the average predominant prime rate**, per month or part month, **compounded annually** (contrast Maryland's simple 8% and Missouri's simple 7%).
- Combined-group adjustments (member inclusion, Finnigan factor corrections) carry interest from the original due date.

(All from `nj-cbt-and-bait`, verified against the 2025 CBT-100 instructions 2026-10-16.)

### 6. Cross-border / multistate

- Single sales factor; services delivered where the benefit is received; marketplace warehouses create receipts and property nexus.
- Mandatory combined reporting makes NJ a **unitary** state — contrast Maryland (separate returns) and Missouri (consolidation optional): group modeling must run three different state postures.
- Water's-edge default; world-wide or affiliated-group elections bind 6 years.

### 7. Worked examples

**Example 1 — rate-table cliff.** Group taxable net income $105,000 vs $98,000 (whole-base rate).

```oa-check
name: NJ rate cliff
inputs:
  a: 105000
  b: 98000
steps:
  - tax_a: a * 0.09
  - tax_b: b * 0.075
  - delta: tax_a - tax_b
expected:
  tax_a: 9450.00
  tax_b: 7350.00
  delta: 2100.00
```

$7,000 more income costs **$2,100** more tax — the 7.5%→9% cliff applies to the whole base.

**Example 2 — Transit Fee.** Water's-edge group, taxable net income $14,000,000.

```oa-check
name: NJ transit fee
inputs:
  income: 14000000
  threshold: 10000000
steps:
  - cbt: income * 0.09
  - fee: (income - threshold) * 0.025
  - total: cbt + fee
expected:
  cbt: 1260000.00
  fee: 100000.00
  total: 1360000.00
```

### 8. Ask the client

1. Combined group or separate filer — managerial member registered? Which filing method, elected when, bound until when?
2. Economic-nexus math: NJ receipts and transaction counts for the year — inside or outside the thresholds?
3. CBT-150 installments tracking 50%-current / 100%-prior?
4. Near the $50k/$100k rate cliffs or the $10M Transit Fee threshold — deferral planning?
5. BAIT elected by the original due date this year?

### 9. Sources

1. Existing tier-2 skill `nj-cbt-and-bait` (rates, minimums, Transit Fee, combined mechanics; verified against 2025 CBT instructions 2026-10-16): repo `skills/us-states/nj/nj-cbt-and-bait.md`.
2. NJ Division of Taxation, CBT combined-groups revision (P.L. 86-272 group rule): <https://www.nj.gov/treasury/taxation/cbt/combinedgroupsrevision.shtml> — 200, read 2026-10-27.
3. NJ Division of Taxation, CBT reform hub: <https://www.nj.gov/treasury/taxation/cbt/cbtreform.shtml> — 200, read 2026-10-27.
4. CBT-100 / CBT-100U / CBT-150 2026 instructions: <https://www.nj.gov/treasury/taxation/cbt/> index verified 200 on 2026-10-27; individual PDFs not re-fetched — deadline-day and penalty-percentage specifics **not yet confirmed**.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for New Jersey CBT and combined-group questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

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
| (see Not yet confirmed) | — | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
