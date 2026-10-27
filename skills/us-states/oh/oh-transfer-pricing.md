---
name: oh-transfer-pricing
description: >
  Use this skill whenever asked about Ohio transfer pricing and related-party
  rules for tax year 2026 — Ohio has no standalone TP documentation statute
  and no income-tax addback (there is no corporate income tax); related-party
  economics live inside the Commercial Activity Tax group rules: >50% common
  ownership forces a COMBINED group (intermember receipts NOT excluded, one
  $6,000,000 exclusion), while an optional CONSOLIDATED election (50% or 80%
  test, forms CAT ES/AR, binding eight calendar quarters) excludes intermember
  receipts and can pull in no-nexus and foreign entities. Covers situsing of
  intercompany receipts, the election trade-off, and the 2024 cancellation
  relief for groups under the exclusion.
  Trigger on "Ohio transfer pricing", "Ohio CAT group", "CAT consolidated",
  "CAT combined group", "Ohio related party", "Ohio common owner", "CAT ES",
  "CAT AR", "Ohio intercompany receipts", "Ohio 80% election".
  Source-cited draft; ORC 5751.01 statute text read 2026-10-27; group
  mechanics carried from the tier-2 oh-cat skill (Department CAT groups page,
  CAT 2023-01, CAT 2005-03, CAT 2005-12, read 2026-10-16).
jurisdiction: US-OH
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - oh-cat
  - oh-corporate-income-tax
---

# Ohio transfer pricing / CAT group overlay v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Ohio professional.

## 1. Scope and sources

Ohio has **no corporate income tax, therefore no income-tax transfer-pricing addback, no state §482 analogue, and no TP documentation requirement**. Because the entity-level tax is the gross-receipts CAT, the Ohio "transfer pricing" question is entirely about **group membership and intermember receipts**:

- **Combined group (default):** entities under **more than 50%** common ownership with Ohio nexus file as one taxpayer with **one $6,000,000 exclusion** — and **intermember receipts are NOT excluded**, so intra-group fees and sales increase the group's CAT base.
- **Consolidated elected group (optional):** entities at **at least 50%** common ownership may elect (choosing the 50% or 80% test) on forms **CAT ES / CAT AR**; the election binds **eight calendar quarters**; **intermember receipts are excluded** and ignored when testing the exclusion; all entities meeting the chosen test must join, even with no Ohio nexus or excluded-person status; the group chooses whether to include non-U.S. corporations (that choice also binds eight quarters).

**Source status (as_of 2026-10-27):** [ORC 5751.01](https://codes.ohio.gov/ohio-revised-code/section-5751.01) fetched HTTP 200 and read (definitions, excluded persons, nexus). Group mechanics are carried from the tier-2 `oh-cat` skill, verified against the Department CAT groups page, CAT 2023-01, CAT 2005-03 and CAT 2005-12 on 2026-10-16. The Department groups page returned a JS-rendered shell on 2026-10-27 — mechanics **not re-read this run**.

## 2. Who applies

- **Common owner:** owns more than half of another entity, or holds majority control directly or through related interests, and can direct the entities below it through voting power. Individuals, trusts and estates can be common owners; a common owner **without Ohio nexus still counts**.
- **Combined default:** >50% common ownership, no consolidation election; only members with Ohio nexus are included.
- **Consolidated election:** ≥50% common ownership; group picks the 50% or 80% test; every entity meeting the chosen test must be included (no-nexus entities, excluded persons, and — if the group so chooses — non-U.S. corporations).
- An entity cannot be in both a consolidated and a combined group; entities owned >50% but <80% under an 80% election must still register as a combined group.
- Federal §482 adjustments flow into gross receipts only as a practical matter (gross receipts are measured without expense deduction, so most income-based TP adjustments do not change the CAT base).

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| CAT rate the TP lands in | 0.26% above the exclusion (see `oh-corporate-income-tax`) | `oh-cat` (Department page, 2026-10-16) |
| Combined group | One taxpayer, one $6,000,000 exclusion; **intermember receipts included** in TGR | `oh-cat` (groups page + CAT 2023-01, 2026-10-16) |
| Consolidated election | ≥50% ownership; 50% or 80% test; **intermember receipts excluded** and ignored for the exclusion test; binds 8 quarters | `oh-cat` (CAT 2005-03/2005-12, 2026-10-16) |
| Election forms | CAT ES (election statement), CAT AR (annual registration) | `oh-cat` |
| Non-U.S. corporations | Inclusion is the group's choice; choice binds 8 quarters | `oh-cat` |
| Situsing of intercompany receipts | Goods by ship-to; services by where the purchaser receives the benefit (ORC 5751.033) | [ORC 5751.01(G)](https://codes.ohio.gov/ohio-revised-code/section-5751.01), read 2026-10-27 |
| Under-exclusion relief (2024+) | A registered consolidated group whose TGR will not exceed the exclusion may cancel its account notwithstanding the 8-quarter binding; a would-be combined group need not register if TGR would fall under the exclusion **after** a valid consolidated election | Rule 5703-29-04 / CAT 2005-03 via `oh-cat` |

## 4. Deadlines

| Action | Due |
|---|---|
| Consolidated election (CAT ES) | With the CAT AR for the first quarter the election covers |
| Election term | Eight calendar quarters from the first elected quarter |
| Non-U.S. inclusion choice | Same election window; binds eight quarters |
| Group quarterly returns | Same CAT calendar: last day of the month after each quarter |
| Separate-filing permission (CAT 2005-12) | Request to the Tax Commissioner; no fixed statutory date |

## 5. Penalties and interest

- Filing separately when the group rules required combined filing: the Department can re-assess the group as one taxpayer with one exclusion — usually a **reduction**, but the reverse error (assuming consolidation without a valid election) leaves intermember receipts taxed, and refund claims run on the four-year ORC 5751.08(A) window.
- Interest on CAT underpayments and ORC 5751.09 penalty percentages: **needs-sources** (not read this run).

## 6. Cross-border

- The consolidated election's **non-U.S. corporation choice** is Ohio's only affirmative cross-border group rule: including foreign affiliates pulls their receipts into the group's exclusion test (their own Ohio-sitused receipts are taxed regardless).
- Management fees, royalties and intercompany interest paid to foreign affiliates are **gross receipts of the recipient only if sitused to Ohio** — a foreign licensor receiving royalties for Ohio-benefiting use can have Ohio TGR from the royalty alone.
- No Ohio addback means outbound fees are not penalized on the payer side; the exposure sits entirely on the recipient's sitused receipts.

## 7. Worked examples

**Example A — two Ohio siblings, combined default vs consolidated election.**

```oa-check
name: Combined vs consolidated, sibling group
inputs:
  external_a: 4000000
  external_b: 3500000
  intermember: 1500000
  exclusion: 6000000
  rate: 0.0026
steps:
  - combined_base: external_a + external_b + intermember - exclusion
  - combined_tax: combined_base * rate
  - consol_base: max(external_a + external_b - exclusion, 0)
  - consol_tax: consol_base * rate
  - saving: combined_tax - consol_tax
expected:
  combined_base: 3000000
  combined_tax: 7800.00
  consol_base: 1500000
  consol_tax: 3900.00
  saving: 3900.00
```

The consolidated election halves the group's CAT here because the $1.5M of intermember receipts leaves the base.

**Example B — group under the exclusion after consolidation.**

```oa-check
name: Consolidated election drops group under exclusion
inputs:
  external: 5200000
  intermember: 1200000
  exclusion: 6000000
steps:
  - combined_tgr: external + intermember
  - consol_tgr: external
  - combined_over: combined_tgr - exclusion
  - consol_over: consol_tgr - exclusion
expected:
  combined_tgr: 6400000
  consol_tgr: 5200000
  combined_over: 400000
  consol_over: -800000
```

Combined filing would put the group $400,000 over the exclusion; after a valid consolidated election the group is under it and — from 2024 — need not register (Rule 5703-29-04 via `oh-cat`).

## 8. Ask the client

- Full ownership map: who owns >50% of each entity, and what else that owner controls (including individuals and trusts).
- Is a consolidated election already in place, when did its eight-quarter term start, and does it use the 50% or 80% test?
- Volume of intermember receipts by quarter — the election's value is proportional to it.
- Any foreign affiliates: does the group want them inside or outside the election, understanding the eight-quarter lock?
- Where do intercompany services actually benefit the purchaser (situsing of service receipts)?
- Would the group fall under the $6,000,000 exclusion after consolidation (registration/cancellation relief)?

## 9. Sources

- [ORC 5751.01 — CAT definitions, related concepts, nexus](https://codes.ohio.gov/ohio-revised-code/section-5751.01) — read 2026-10-27
- [ORC 5751.08 — four-year refund window](https://codes.ohio.gov/ohio-revised-code/section-5751.08) — read 2026-10-27
- `oh-cat` (tier 2, read 2026-10-16) — combined/consolidated mechanics, CAT ES/AR, eight-quarter binding, Rule 5703-29-04 cancellation relief, citing the Department CAT groups page, CAT 2023-01, CAT 2005-03, CAT 2005-12
- [Department CAT groups page](https://tax.ohio.gov/business/commercial-activity-tax/commercial-activity-tax-groups) — cited via `oh-cat`; JS-rendered shell 2026-10-27
- **needs-sources:** ORC 5751.09 penalty / 5703.06 interest percentages; CAT ES/AR form PDFs not re-fetched this run

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Ohio CAT group and related-party questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
