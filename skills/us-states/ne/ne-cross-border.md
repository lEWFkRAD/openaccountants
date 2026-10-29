---
name: ne-cross-border
description: >
  Use this skill whenever asked about Nebraska cross-border individual
  taxation for 2026 — nonresident and part-year taxation of
  Nebraska-source income, the pass-through entity (PTE) tax election as a
  collection and SALT-posture rail for nonresident members, credit for
  taxes paid to other states, and inheritance tax administration.
  Trigger on "Nebraska nonresident", "Nebraska part-year", "Nebraska PTE
  election", "Nebraska credit for taxes paid", "Nebraska inheritance
  tax". Source-cited draft; PTE-tax page and withholding rails verified
  2026-10-28; nonresident schedule mechanics, credit statute and
  inheritance-tax figures needs-sources.
jurisdiction: US-NE
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ne-income-tax
  - ne-payroll
---

# Nebraska cross-border taxation v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## 1. Scope and sources

How Nebraska reaches nonresidents and how residents recover other-state tax. **Source status:** verified 2026-10-28 — the DOR individual income-tax page resolves, the **PTE tax page** is official, and withholding rails (§ 77-3513, Circular EN) are verified. **Nonresident return/schedule mechanics, the credit-for-taxes-paid statute, reciprocity, and inheritance-tax rates/thresholds — needs-sources** (inheritance tax is county-administered per pre-existing `ne-income-tax.md` notes; not re-verified this run).

## 2. Who applies

- **Nonresidents with Nebraska-source income** — wages for Nebraska workdays, Nebraska business income, rents/gains; filing mechanics **needs-sources**.
- **Part-year residents** — split-period filing, mechanics **needs-sources**.
- **Nebraska residents paying other-state tax** — credit expected under conformity — **needs-sources**.
- **Nonresident members of NE pass-throughs** — PTE tax election moves the liability to entity level (page verified).

## 3. Rates

Graduated individual schedule (2026 top 5.5% expected — see `ne-income-tax.md`, confirm). PTE tax rate (commonly cited 5.5%) — **needs-sources**.

## 4. Base and mechanics

- Workday sourcing for wages (verify convenience rules — **needs-sources**).
- PTE election: entity-level tax, member credit (mechanics **needs-sources**).
- **No Nebraska exit tax** — assertion, **needs-sources**.

## 5. Deadlines, penalties, interest

Individual due April 15 expected; PTE election deadlines are annual and election-window-bound (**needs-sources** — commonly January 31 for the following year, confirm).

## 6. Cross-border notes

- Colorado/Nebraska and Iowa/Nebraska border workers: check the other state's nonresident filing and credits (see those packs) — **needs-sources**.
- Inheritance tax (county-administered, close relative exemption) affects nonresident decedents with Nebraska property — figures **needs-sources**.

## 7. Worked examples

**Example 1 — nonresident ratio (illustrative).** Nonresident, total income $220,000, Nebraska-source $55,000; hypothetical full-return tax $11,000:

```oa-check
name: NE nonresident ratio
inputs:
  total_income: 220000
  ne_source: 55000
  tax_on_total: 11000
steps:
  - ratio: ne_source / total_income
  - ne_tax: tax_on_total * ratio
expected:
  ne_tax: 2750.00
```

**Example 2 — PTE election at entity level.** Nebraska pass-through income $300,000, PTE rate 5.5% (needs-sources):

```oa-check
name: NE PTE election tax
inputs:
  income: 300000
  pte_rate: 0.055
steps:
  - pte_tax: income * pte_rate
expected:
  pte_tax: 16500.00
```

## 8. Ask the client

- Workdays physically in Nebraska vs home state — and does the home state credit Nebraska tax?
- Is the pass-through considering the PTE election for SALT-cap posture? Election deadline missed?
- Out-of-state decedent owning Nebraska real property — inheritance tax exposure?

## 9. Sources

1. DOR PTE tax: https://revenue.nebraska.gov/tax-credits/nebraska-pass-through-entity-tax-ptet — verified 2026-10-28.
2. DOR individual income tax: https://revenue.nebraska.gov/individuals/individual-income-tax — fetched 2026-10-28 (200).
3. § 77-3513: https://nebraskalegislature.gov/laws/statutes.php?statute=77-3513 — fetched 2026-10-28.

**Needs-sources:** nonresident schedule, credit statute, reciprocity, PTE rate/deadline/credit mechanics, inheritance-tax figures, exit-tax confirmation.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Nebraska nonresident/cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
