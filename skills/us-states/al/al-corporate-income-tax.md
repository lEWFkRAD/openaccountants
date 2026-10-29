---
name: al-corporate-income-tax
description: >
  Use this skill whenever asked about Alabama corporate income tax
  for tax year 2026 — the flat 6.5% rate with the deduction for
  federal income tax paid, single sales factor apportionment for tax
  years beginning on or after 2021, Form 20C mechanics, Alabama
  combined reporting for unitary groups, estimated tax, and the
  franchise-tax authority. Trigger on "Alabama corporate tax",
  "Alabama 6.5 percent", "Alabama Form 20C", "Alabama combined
  reporting", "Alabama single sales factor", "Ala Code 40-18".
  Source-cited draft; ALDOR corporate page read 2026-10-27.
jurisdiction: US-AL
category: corporate
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - al-income-tax
---

# Alabama corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Alabama taxes corporations at a **flat 6.5%** of annual net income **with a deduction allowed for federal income tax paid or accrued** — a genuine rate-plus-base quirk that makes the Alabama effective rate sensitive to the federal bill. **Source status:** the rate, the federal-tax deduction, the single-sales-factor rule (tax years beginning on or after 2021-01-01), the statutory authority (Ala. Code §§40-18-1 through 40-18-59 and 40-18-160 through 40-18-176), the franchise-tax authority (§§40-27-1 through 40-27-6), and the constitutional rate history (Amendment 212 → 5%, Amendment 662 → 6.5% from calendar 2001) are all read from the ALDOR Corporate Income Tax page, fetched 2026-10-27. Form 20C/20S PDF paths 404'd this run — form-level figures (deadlines, minimum tax, estimated percentages) carry **needs-sources**; the Code of Alabama mirror did not resolve, so section text is **needs-sources**.

## 2. Who applies

- Corporations with net taxable income from business within Alabama, and foreign corporations on Alabama-source income (per the ALDOR page's Application section and Amendment 211/212 language, read 2026-10-27).
- Alabama is a **single sales factor** apportionment state for tax years beginning on or after 2021-01-01 (ALDOR page, read 2026-10-27) — property and payroll factors no longer enter the fraction.
- Unitary groups file on a **combined** basis (Ala. Code §40-18-50 — text **needs-sources**; see `al-transfer-pricing`).
- S corporations and pass-throughs pay the composite/pass-through tax on members' Alabama income rather than entity-level income tax (mechanics **needs-sources**).

## 3. Rates and base

| Item | Rate / base | Source |
|---|---|---|
| Corporate income tax | **flat 6.5%** of annual net income | ALDOR corporate page, read 2026-10-27; re-verified 2026-10-28 verbatim: "Rate 6.5 percent of annual net income with a deduction allowed for federal income tax paid or accrued" (Amendment 662, ratified 2000-06-19, effective calendar 2001) |
| Base modification | **deduction for federal income tax paid or accrued** | ALDOR page (Amendment 212/662 text), read 2026-10-27 |
| Apportionment | single sales factor (TYB ≥ 2021-01-01) | ALDOR page, read 2026-10-27 |
| Minimum tax | **needs-sources** (Form 20C not retrievable this run) | — |
| Franchise tax | separate tax, authority §§40-27-1 to 40-27-6; rate table **needs-sources** | ALDOR page, read 2026-10-27 |

Alabama net income starts from federal taxable income with the federal-income-tax deduction and state modifications (§§40-18-7 et seq. — text **needs-sources**).

## 4. Deadlines

- **Return:** Form 20C follows the federal due date (April 15 for calendar-year filers) — **needs-sources** (form instructions not retrievable this run; confirm on ALDOR forms page).
- **Estimated tax:** corporations pay quarterly estimated tax; the installment percentage and safe-harbor rules are **needs-sources** (Form 20ES not retrievable).
- **Extension:** federal extension generally extends the Alabama return, with payment due at the original date — **needs-sources**.

## 5. Penalties and interest

Late-filing/late-payment penalties and interest under Ala. Code §40-2A-1 et seq. — percentages **needs-sources** (statute mirror unreachable this run). Common failure modes: (1) forgetting the **federal-tax deduction** when projecting Alabama cost on a restructuring that changes the federal bill; (2) apportioning with an old three-factor spreadsheet after 2021; (3) missing the franchise tax while focused on the income tax.

## 6. Cross-border interactions

- Foreign (out-of-state) corporations are taxed on Alabama-source income only (Amendment 212 language, read from the ALDOR page 2026-10-27).
- Single sales factor means market-state sourcing of sales drives the fraction — see `al-cross-border` and `al-transfer-pricing`.
- Alabama has no income tax treaty; interstate allocation runs under §40-18-160+ (Uniform Division of Income for Tax Purposes Act as adopted — text **needs-sources**).

## 7. Worked examples

A domestic corporation with $500,000 federal taxable income, $105,000 federal income tax paid, 100% Alabama sales:

```oa-check
name: AL corporate tax with federal tax deduction
inputs:
  fti: 500000
  fed_tax: 60000
  rate: 0.065
steps:
  - al_base: fti - fed_tax
  - tax: al_base * rate
expected:
  al_base: 440000.00
  tax: 28600.00
```

Same corporation, multistate: total sales $5,000,000, Alabama sales $1,200,000:

```oa-check
name: AL single sales factor apportionment
inputs:
  al_sales: 1200000
  total_sales: 5000000
  al_base: 440000
  rate: 0.065
steps:
  - factor: al_sales / total_sales
  - apportioned: al_base * factor
  - tax: apportioned * rate
expected:
  factor: 0.24
  apportioned: 105600.00
  tax: 6864.00
```

## 8. Ask the client

- Is the federal-income-tax deduction modeled in state projections (it moves with federal credits, NOLs, R&D capitalization)?
- Post-2021 apportionment: is the sales factor numerator market-based and complete (delivery state for tangible goods)?
- Is the franchise tax being filed alongside the income tax?
- Any unitary affiliates that trigger combined reporting?

## Sources

1. ALDOR Corporate Income Tax page: https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ (200, text read 2026-10-27 — rate, federal-tax deduction, single sales factor, authority citations)
2. Code of Alabama 1975 Title 40: https://law.justia.com/codes/alabama/title-40/ (not fetched this run — section text **needs-sources**)
3. Form 20C instructions: https://revenue.alabama.gov/forms/ (form PDF path not located this run — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Alabama corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
