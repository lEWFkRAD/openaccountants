---
name: ky-transfer-pricing
description: >
  Use this skill whenever asked about Kentucky transfer pricing and
  combined filing for tax year 2026 — the mandatory unitary combined
  group filing from tax years beginning 2019, the 48-month
  same-as-federal consolidated group election, the combined-group
  definition (domestic corporations with exceptions), and how
  related-party pricing is policed through the combined computation
  rather than a standalone addback regime. Trigger on "Kentucky
  combined reporting", "Kentucky unitary", "Kentucky consolidated
  election", "Kentucky transfer pricing", "Kentucky 48 month
  election". Source-cited draft; DOR corporate page read 2026-10-27.
jurisdiction: US-KY
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - ky-corporate-income-tax
---

# Kentucky transfer pricing / combined filing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Kentucky polices related-party economics primarily by **forcing the whole unitary group into one combined computation** rather than through an addback statute: for tax years beginning on/after 2019-01-01, unitary combined filing is **required**; a group may instead elect same-as-federal consolidated filing, which binds for **48 months**; separate-entity filing applies only outside a unitary or consolidated group. **Source status:** all three filing-method rules and the combined-group description ("Combined group includes domestic corporations (with some exceptions) involved in unitary business") are read from the DOR Corporation Income & LLET page, fetched 2026-10-27. KRS 141 section pages are JS shells — definitional tests and apportionment specifics **needs-sources**.

## 2. Who applies

- Every member of a **unitary business group** of domestic corporations (with statutory exceptions) — combined filing is mandatory, not elective (DOR page, read 2026-10-27).
- Groups that prefer federal-style consolidation may **elect** it, but the election locks for **48 months** (DOR page, read 2026-10-27).
- Standalone corporations outside any unitary group file separately; intercompany dealings with non-members then sit inside the apportionment analysis (KRS 141.033+ — **needs-sources**).

## 3. Rates and base

| Item | Rule | Source |
|---|---|---|
| Rate | flat **5%** on combined Kentucky taxable income | DOR page, read 2026-10-27 |
| Combined group | domestic corporations in a unitary business, with exceptions (full list: **needs-sources**) | DOR page, read 2026-10-27 |
| Consolidated election | same-as-federal, **48-month** lock-in | DOR page, read 2026-10-27 |
| Intercompany eliminations | combined computation eliminates member transactions (mechanics: **needs-sources**) | KRS 141.031 — JS shell |
| Apportionment | allocation/apportionment of combined income (single sales factor history, water's-edge): **needs-sources** | KRS 141.033–141.043 — JS shells |
| Documentation regime | none standalone | absence noted |

## 4. Deadlines

- Combined return rides the Form 720 calendar (April 15 calendar-year; extension with payment).
- Estimated installments 25%×4 (4/15·6/15·9/15·12/15) computed at the combined level (DOR page, read 2026-10-27).
- The 48-month consolidated election, once made, has no annual deadline — but track the expiry year.
- Federal audit final determinations → amended KY return within **180 days** (DOR page, read 2026-10-27).

## 5. Penalties and interest

"Addition to Tax" penalty regime (KY-TAM-19-02; percentages **needs-sources**); interest on underpayments (**needs-sources**). Common failure modes: (1) filing separate-entity when the group is unitary — combined filing is mandatory; (2) making the consolidated election without modeling the 48-month lock; (3) assuming foreign affiliates are automatically out — the "domestic corporations (with some exceptions)" language needs a member-by-member check; (4) missing the 180-day federal-audit amendment window, which is where most transfer-pricing adjustments surface.

## 6. Cross-border interactions

- **Water's-edge:** the combined group is described as domestic corporations — foreign members' treatment (and the exceptions) must be confirmed against KRS 141.031 text: **needs-sources**.
- Payments to related foreign affiliates are not separately restricted by a Kentucky addback statute found this run (absence noted; confirm against full KRS 141: **needs-sources**).
- LLET paid by LLC members interacts with out-of-state members' credits (see `ky-cross-border`).

## 7. Worked examples

A unitary group with $8,000,000 combined income, 25% apportioned to Kentucky:

```oa-check
name: KY combined tax unitary group
inputs:
  combined: 8000000
  app: 0.25
  rate: 0.05
steps:
  - ky_income: combined * app
  - tax: ky_income * rate
expected:
  ky_income: 2000000.00
  tax: 100000.00
```

The same group shifts $600,000 of intercompany management fees to a non-member affiliate, reducing combined income before apportionment:

```oa-check
name: fee shift effect on combined base
inputs:
  combined: 8000000
  shift: 600000
  app: 0.25
  rate: 0.05
steps:
  - new_combined: combined - shift
  - new_ky: new_combined * app
  - new_tax: new_ky * rate
  - saving: 100000 - new_tax
expected:
  new_combined: 7400000.00
  new_ky: 1850000.00
  new_tax: 92500.00
  saving: 7500.00
```

## 8. Ask the client

- Is the group unitary under Kentucky's definition — has anyone mapped the members against the "domestic corporations with exceptions" rule?
- Has the 48-month consolidated election been made, and when does it expire?
- Are intercompany fees moving income outside the combined base — and are they defensible at the federal level too?
- Any federal audit adjustments — is the 180-day Kentucky amendment clock tracked?

## Sources

1. DOR Corporation Income & LLET page (filing methods, 48-month election, combined group): https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx (200, text read 2026-10-27)
2. KRS 141.031 (combined report): https://apps.legislature.ky.gov/law/krs/141/141.031.asp (JS shell — **needs-sources**)
3. KRS 141.033–141.043 (apportionment): JS shells — **needs-sources**
4. Form 720 PDF: https://revenue.ky.gov/Forms/720.pdf (200 PDF, read 2026-10-27)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kentucky combined-filing questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
