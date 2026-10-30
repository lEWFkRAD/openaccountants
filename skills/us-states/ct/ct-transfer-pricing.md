---
name: ct-transfer-pricing
description: >
  Use this skill whenever asked about Connecticut transfer pricing and
  related-party adjustments for tax year 2026 -- the intangible-expense
  and interest addback under Conn. Gen. Stat. §12-218c, the
  related-transaction interest restriction under §12-218d, combined
  reporting (world-wide / affiliated / water's-edge) and tax-haven
  rules under §12-218f, combined-group net income under §12-218e, and
  the pass-through entity tax's interaction with unitary groups.
  Trigger on "Connecticut transfer pricing", "Connecticut addback",
  "Connecticut combined reporting", "Connecticut tax haven",
  "water's edge Connecticut", "12-218c", "related member Connecticut".
  Source-cited draft; CGA chapter 208 text read 2026-10-28.
jurisdiction: US-CT
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - ct-corporate-income-tax
---

# Connecticut transfer pricing & combined reporting v0.2

Covers Connecticut's related-party adjustment and unitary-combination
rules. Primary source: Conn. Gen. Stat. chapter 208 full text
(cga.ct.gov, archived and read 2026-10-28). Statute substance below is
quoted or paraphrased from that text; DRS regulations (Conn. Agencies
Regs.) and the current tax-haven list are listed under Not yet
confirmed.

## Who this applies to

- C corporations and combined groups with transactions involving
  "related members" -- §12-218c/§12-218d definitions keyed to
  IRC §§1563(b)/(e) and §318 attribution with fifty-per-cent-value
  ownership thresholds (§12-218c(a)(5)-(6)).
- Affiliated groups and unitary businesses → combined return with a
  designated taxable member (§12-218f, §12-222).

## Rates, bands and thresholds

| Mechanism | Effect | Source |
|---|---|---|
| Intangible/interest addback | Add back otherwise-deductible **intangible expenses/costs and related interest** paid/accrued to related members when computing net income | §12-218c(b) |
| "Intangible expenses and costs" | Includes acquisition/use/maintenance of intangible property, factoring/discounting losses, royalty/patent/technical/copyright fees, licensing fees, similar items | §12-218c(a)(2) |
| Exception 1 | No adjustment if the corporation shows by **clear and convincing evidence** the adjustment is unreasonable, or agrees a §12-221a alternative apportionment method in writing | §12-218c(c)(1) |
| Exception 2 | No adjustment for portions the related member paid on to a **non-related member** AND the transaction's principal purpose was not CT tax avoidance (**preponderance** standard) | §12-218c(c)(2) |
| Interest restriction | Separate restriction on interest expenses/costs related to certain transactions with related members | §12-218d |
| Combined group base | Aggregate net income/loss of taxable + nontaxable members derived from the unitary business; federal-consolidation wrappers stripped | §12-218e(a) |
| Group perimeter | Election: world-wide or affiliated-group basis; tax-haven incorporations included unless a legitimate business purpose is proven | §12-218f(a)-(b) |

## The taxable base

- The addback applies in computing net income under §12-217 for the
  year the expense is paid/accrued/incurred (§12-218c(b)).
- Combined group net income is computed as if members were not
  federally consolidated (§12-218e(a)(1)).
- "Tax haven" determination by the commissioner under §12-218f(b)(4)
  (current list -- see Not yet confirmed).
- Apportionment: property/payroll/receipts factors for the combined
  group (§12-218 et seq.).

## Deadlines and filing

- Combined return filed by the designated taxable member -- same
  fifteenth-day-of-the-month-following-the-federal-due-date rule as
  CT-1120 (§12-222).
- Elections (world-wide/affiliated/water's-edge) made per §12-218f
  procedures with the return (see Not yet confirmed for the current
  DRS election form).

## Penalties and interest

- Addback-driven deficiencies: three-year assessment window (§12-233),
  interest at one per cent per month from the original due date
  (§12-235), ten per cent / fifty-dollar penalty for unpaid amounts
  (§12-229).

## Cross-border points

- **World-wide vs water's-edge:** the default combined perimeter
  reaches foreign affiliates; the water's-edge election is the
  planning lever (§12-218f; election mechanics -- see Not yet
  confirmed).
- **Tax haven inclusions:** a member incorporated in a commissioner-
  determined tax haven joins the affiliated-group base unless a
  legitimate business purpose is proven (§12-218f(a)).
- **Exception 2 is the substance test:** back-to-back payments to
  unrelated parties plus a non-avoidance principal purpose defeat the
  addback -- document contemporaneously (§12-218c(c)(2)).
- Federal §482 documentation is persuasive but Connecticut runs its
  own addback mechanically -- do not assume §482 compliance cures
  §12-218c.

## Worked examples

Hypothetical facts. A CT combined member pays $2,000,000 of royalties
to a Bermuda licensing affiliate (related member). No exception
established; the addback increases CT-apportioned net income by
$2,000,000 at an eighty-per-cent apportionment percentage and the
confirmed 7.5% rate (2026, no surcharge):

```oa-check
name: royalty addback cost
inputs:
  royalties: 2000000
  apportionment: 0.80
  rate: 0.075
steps:
  - apportioned: royalties * apportionment
  - extra_tax: apportioned * rate
expected:
  apportioned: 1600000.00
  extra_tax: 120000.00
```

Same hypothetical facts, but the affiliate pays sixty per cent of the
royalties on to unrelated third parties and the principal purpose is
not CT tax avoidance (Exception 2 applies to that portion):

```oa-check
name: exception 2 partial relief
inputs:
  royalties: 2000000
  passthrough_pct: 0.60
  apportionment: 0.80
  rate: 0.075
steps:
  - added_back: royalties * (1 - passthrough_pct)
  - apportioned: added_back * apportionment
  - extra_tax: apportioned * rate
expected:
  added_back: 800000.00
  apportioned: 640000.00
  extra_tax: 48000.00
```

## Ask the client first

- What intangible (royalty/license/factoring) or intangible-related
  interest flows exist with fifty-per-cent-related members, onshore or
  offshore?
- Can Exception 2 be documented -- back-to-back payments and
  principal-purpose support?
- Is the group on world-wide or water's-edge reporting, and is the
  election current?
- Any affiliate incorporated in a commissioner-listed tax haven --
  legitimate-business-purpose file ready?
- Has a §12-221a alternative-apportionment agreement been considered
  for borderline structures?

## Sources

| Source | URL | Read on |
|---|---|---|
| Conn. Gen. Stat. ch. 208 §§12-218c, 12-218d, 12-218e, 12-218f, 12-222, 12-229, 12-233, 12-235 | https://www.cga.ct.gov/current/pub/chap_208.htm | 2026-10-28 |

Not yet confirmed: the commissioner's current tax-haven list under §12-218f(b)(4) (a determination instrument, not in the chapter text read); DRS regulations (Conn. Agencies Regs.) on combined reporting and the current world-wide/water's-edge election form -- not audited this run.

## Talk to a verified accountant

**Talk to a verified accountant** -- for Connecticut transfer-pricing and combined-reporting questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

This skill is a source-cited draft; no accountant has reviewed it. Verify
figures against the cited primary sources or with a licensed Connecticut
professional before relying on them.
