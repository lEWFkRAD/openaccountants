---
name: ct-transfer-pricing
description: >
  Use this skill whenever asked about Connecticut transfer pricing and
  related-party adjustments for tax year 2026 — the intangible-expense
  and interest addback under Conn. Gen. Stat. §12-218c, the
  related-transaction interest restriction under §12-218d, combined
  reporting (world-wide / affiliated / water's-edge) and tax-haven
  rules under §12-218f, combined-group net income under §12-218e, and
  the pass-through entity tax's interaction with unitary groups.
  Trigger on "Connecticut transfer pricing", "Connecticut addback",
  "Connecticut combined reporting", "Connecticut tax haven",
  "water's edge Connecticut", "12-218c", "related member Connecticut".
  Source-cited draft; CGA chapter 208 text read 2026-10-27.
jurisdiction: US-CT
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - ct-corporate-income-tax
---

# Connecticut transfer pricing & combined reporting v0.1

## 1. Scope and sources

Covers Connecticut's related-party adjustment and unitary-combination
rules. Primary verified source: Conn. Gen. Stat. chapter 208 full
text (cga.ct.gov, read 2026-10-27). Statute substance below is quoted
or paraphrased from that text; DRS regulations (Conn. Agencies Regs.)
not re-audited this run.

## 2. Who applies

- C corporations and combined groups with transactions involving
  "related members" — §12-218c/§12-218d definitions keyed to
  IRC §§1563(b)/(e) and §318 attribution with 50%-value ownership
  thresholds (§12-218c(a)(5)-(6) — verified).
- Affiliated groups and unitary businesses → combined return with a
  designated taxable member (§12-218f, §12-222 — verified).

## 3. Core mechanics

| Mechanism | Effect | Source |
|---|---|---|
| Intangible/interest addback | Add back otherwise-deductible **intangible expenses/costs and related interest** paid/accrued to related members when computing net income | §12-218c(b) (verified) |
| "Intangible expenses and costs" | Includes acquisition/use/maintenance of intangible property, factoring/discounting losses, royalty/patent/technical/copyright fees, licensing fees, similar items | §12-218c(a)(2) (verified) |
| Exception 1 | No adjustment if corporation shows by **clear and convincing evidence** the adjustment is unreasonable, or agrees a §12-221a alternative apportionment method in writing | §12-218c(c)(1) (verified) |
| Exception 2 | No adjustment for portions the related member paid on to a **non-related member** AND the transaction's principal purpose was not CT tax avoidance (**preponderance** standard) | §12-218c(c)(2) (verified) |
| Interest restriction | Separate restriction on interest expenses/costs related to certain transactions with related members | §12-218d (verified heading/definitions) |
| Combined group base | Aggregate net income/loss of taxable + nontaxable members derived from the unitary business; federal-consolidation wrappers stripped | §12-218e(a) (verified) |
| Group perimeter | Election: world-wide or affiliated-group basis; default per statute; tax-haven incorporations included unless legitimate business purpose proven | §12-218f(a)-(b) (verified) |

## 4. Base and timing

- Addback applies in computing net income under §12-217 for the year
  the expense is paid/accrued/incurred (verified §12-218c(b)).
- Combined group net income computed as if members were not federally
  consolidated (§12-218e(a)(1) — verified).
- "Tax haven" determination by the commissioner under §12-218f(b)(4)
  (verified reference; current list — needs-sources).
- Apportionment: property/payroll/receipts factors for the combined
  group (§12-218 et seq. — verified chapter).

## 5. Deadlines

- Combined return filed by the designated taxable member — same
  15th-day-after-federal-due-date rule as CT-1120 (§12-222 —
  verified).
- Elections (world-wide/affiliated/water's-edge) made per §12-218f
  procedures with the return — confirm current DRS election form
  (needs-sources).

## 6. Penalties and interest

- Addback-driven deficiencies: 3-year assessment window (§12-233 —
  verified), interest 1%/month from original due date (§12-235 —
  verified), 10%/$50 penalty for unpaid amounts (§12-229 — verified).

## 7. Cross-border interactions

- **World-wide vs water's-edge:** the default combined perimeter
  reaches foreign affiliates; the water's-edge election is the
  planning lever (§12-218f — verified headings; election mechanics
  needs-sources).
- **Tax haven inclusions:** a member incorporated in a commissioner-
  determined tax haven joins the affiliated-group base unless a
  legitimate business purpose is proven (§12-218f(a) — verified).
- **Exception 2 is the substance test:** back-to-back payments to
  unrelated parties plus a non-avoidance principal purpose defeat the
  addback — document contemporaneously (verified §12-218c(c)(2)).
- Federal §482 documentation is persuasive but Connecticut runs its
  own addback mechanically — do not assume §482 compliance cures
  §12-218c.

## 8. Worked examples

A CT combined member pays $2,000,000 of royalties to a Bermuda
licensing affiliate (related member). No exception established; the
addback increases CT-apportioned net income by $2,000,000 at an 80%
apportionment percentage and 7.5% rate (2026, no surcharge):

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

Same facts, but the affiliate pays 60% of the royalties on to
unrelated third parties and principal purpose is not CT tax
avoidance (Exception 2 applies to that portion):

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

## 9. Ask the client

- What intangible (royalty/license/factoring) or intangible-related
  interest flows exist with 50%-related members, onshore or offshore?
- Can Exception 2 be documented — back-to-back payments and
  principal-purpose support?
- Is the group on world-wide or water's-edge reporting, and is the
  election current?
- Any affiliate incorporated in a commissioner-listed tax haven —
  legitimate-business-purpose file ready?
- Has a §12-221a alternative-apportionment agreement been considered
  for borderline structures?

## Sources

1. Conn. Gen. Stat. ch. 208 §§12-218c, 12-218d, 12-218e, 12-218f, 12-222, 12-229, 12-233, 12-235: https://www.cga.ct.gov/current/pub/chap_208.htm (200 HTML, read 2026-10-27)
2. Conn. Agencies Regs. on combined reporting: not audited this run — needs-sources

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Connecticut transfer-pricing and combined-reporting questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
