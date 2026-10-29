---
name: al-transfer-pricing
description: >
  Use this skill whenever asked about Alabama transfer pricing and
  combined reporting for tax year 2026 — how related-party economics
  are policed through mandatory combined reporting for unitary
  business groups and single-sales-factor apportionment rather than a
  standalone addback statute, the Alabama unitary-group definition,
  and the elimination of intercompany transactions in the combined
  computation. Trigger on "Alabama combined reporting", "Alabama
  unitary group", "Alabama transfer pricing", "Alabama intercompany
  elimination", "Alabama addback". Source-cited draft; ALDOR
  corporate page read 2026-10-27; unitary-definition text
  needs-sources.
jurisdiction: US-AL
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - al-corporate-income-tax
---

# Alabama transfer pricing / combined reporting v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Alabama has **no standalone transfer-pricing documentation statute and no royalty/interest addback regime** the way some states do. Related-party economics are policed structurally: unitary affiliated groups file a **combined return** (Ala. Code §40-18-50 — text **needs-sources**) in which intercompany transactions are eliminated, and the apportionment fraction is a **single sales factor** (ALDOR corporate page, read 2026-10-27, confirming single sales factor for tax years beginning on or after 2021-01-01). **Source status:** the single-sales-factor rule is read from the ALDOR page; the combined-reporting mandate, the unitary-group definition, the water's-edge rule, and the common-reporting-company mechanics sit in §40-18-50 and §40-18-160+ whose text was not retrievable from this host this run — all flagged **needs-sources**.

## 2. Who applies

- Corporations that are part of a **unitary business group** must combine (Alabama moved combined reporting from elective to mandatory in the 2021 income-tax reform — effective-date detail **needs-sources**).
- A unitary group generally requires a **common ownership** test (typically >50% shared ownership, with 80% for the classic unitary definition) plus **functional/geographic integration** — Alabama's precise thresholds: **needs-sources**.
- Standalone corporations outside a unitary group file separately; intercompany dealings with non-members then surface through the single-sales-factor numerator and the §40-18-50 anti-distortion authority.

## 3. Mechanics

| Item | Rule | Source |
|---|---|---|
| Combined return | required for unitary groups | Ala. Code §40-18-50 — text **needs-sources** |
| Intercompany eliminations | eliminate intercompany transactions and unrealized profits in the combined computation | §40-18-50 — **needs-sources** |
| Apportionment | single sales factor (TYB ≥ 2021) | ALDOR page, read 2026-10-27 |
| Addback statutes | none found for royalties/interest — **needs-sources** confirmation | — |
| Water's-edge | foreign affiliates excluded (confirm) — **needs-sources** | — |

## 4. Deadlines

The combined return follows the corporate return calendar (see `al-corporate-income-tax`); one member typically files as the common reporting entity for the group (**needs-sources**). Federal audit changes must be reported to Alabama within the statutory window (days: **needs-sources**).

## 5. Penalties and interest

No TP-specific documentation penalty exists; exposure runs through the ordinary underpayment penalty and interest (percentages **needs-sources**). Common failure modes: (1) filing separate returns when the group is unitary post-2021; (2) leaving intercompany management fees or royalties in the combined computation; (3) pricing intangibles on a "cost-plus" default that the single sales factor then amplifies into the Alabama fraction.

## 6. Cross-border interactions

- Interstate only: Alabama's TP surface is the unitary-combined computation plus market-based sales sourcing (see `al-cross-border`).
- No Alabama analog to §267A or EU arm's-length documentation; federal intercompany rules carry over through federal taxable income as the starting point.

## 7. Worked examples

Unitary group, two members: OpCo (Alabama sales $900,000, other sales $1,100,000) pays MgmtCo (no sales) a $200,000 management fee. Combined computation eliminates the fee:

```oa-check
name: AL combined elimination effect on group income
inputs:
  opco_income: 700000
  mgmtco_income: 180000
  fee: 200000
steps:
  - separate_total: opco_income + mgmtco_income
  - combined_total: separate_total
  - drift: separate_total - combined_total
expected:
  separate_total: 880000.00
  combined_total: 880000.00
  drift: 0.00
```

(The elimination is income-neutral inside the group but moves each member's separate fraction — the combined single factor uses group sales.)

Group apportionment with the fee eliminated:

```oa-check
name: AL combined single sales factor
inputs:
  group_al_sales: 900000
  group_total_sales: 2000000
  combined_income: 880000
  rate: 0.065
steps:
  - factor: group_al_sales / group_total_sales
  - apportioned: combined_income * factor
  - tax: apportioned * rate
expected:
  factor: 0.45
  apportioned: 396000.00
  tax: 25740.00
```

## 8. Ask the client

- Is the group unitary under Alabama's post-2021 mandatory combining rule — has anyone run the ownership + integration test?
- Are intercompany fees, royalties, and interest fully eliminated in the combined workpapers?
- Does the sales-factor numerator use the same market rules for every member?
- Any foreign affiliates — is water's-edge being applied correctly?

## Sources

1. ALDOR Corporate Income Tax page: https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ (200, text read 2026-10-27 — single sales factor from TYB 2021, authority citations)
2. Ala. Code §40-18-50 (combined reporting): https://law.justia.com/codes/alabama/title-40/ (not fetched this run — **needs-sources**)
3. Alabama Form 20CR (combined return): https://revenue.alabama.gov/forms/ (not located this run — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Alabama combined-reporting questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
