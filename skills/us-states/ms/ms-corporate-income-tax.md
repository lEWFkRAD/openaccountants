---
name: ms-corporate-income-tax
description: >
  Use this skill whenever asked about Mississippi corporate income tax for
  tax year 2026 — the Title 27 Chapter 7 Article 1 income tax, the
  combined-report regime (Form 83-310) with the 90%-of-current-year
  estimated-payment rule (Form 83-105), and the separate franchise tax
  (Title 27 Chapter 13). Trigger on "Mississippi corporate income tax",
  "83-100", "83-310", "Mississippi combined report", "Mississippi
  franchise tax". Source-cited draft; combined-report rails, form IDs
  83-310/83-105 and the 90% estimate rule verified on the DOR combined
  filing page 2026-10-28; the 3%/4%/5% rate table and Form 83-100
  identity needs-sources.
jurisdiction: US-MS
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ms-income-tax
---

# Mississippi corporate income tax v0.1

> **General reference only.** General tax reference for AI-assisted workflows; not reviewed for any specific client's facts. Do not file, pay, or take a position on this alone — use a qualified Mississippi practitioner.

## 1. Scope and sources

Covers Mississippi corporation income tax and the combined-report overlay. **Source status:** the DOR combined-filing page (https://www.dor.ms.gov/taxes/combined-filing, fetched and verified 2026-10-28) confirms **combined reporting via Form 83-310, combined-group membership, and the requirement that combined groups pay estimates at 90% of the current-year liability (Form 83-105)**. The **rate table (commonly cited as 3%/4%/5% bands) and the standalone return form number (83-100) were not on a fetched official page — needs-sources**. Statute: Miss. Code Ann. Title 27 Ch. 7 Art. 1 (structure verified); section cites **needs-sources**.

## 2. Who applies

- C corporations and other entities taxable as corporations with Mississippi income.
- **Combined groups:** commonly-owned unitary groups file a combined report (83-310) in addition to / instead of separate-company returns per the DOR page (verified framing; membership tests **needs-sources**).
- Financial institutions and certain entities also face the **franchise tax** (Title 27 Ch. 13 — existence verified; rates **needs-sources**).

## 3. Rates (tax year 2026)

| Mississippi taxable income | Rate | Source status |
|---|---|---|
| First $25,000 (approx.) | 3% | **needs-sources** |
| Next $25,000 (approx.) | 4% | **needs-sources** |
| Over $50,000 (approx.) | 5% | **needs-sources** |

Treat 5% as the planning default for income above $50,000 pending source confirmation.

## 4. Base and apportionment

Federal taxable income with Mississippi modifications (chapters verified; modification detail **needs-sources**). Apportionment factor mix **needs-sources**; combined-report income is apportioned to Mississippi per the combined-filing page (verified framing).

## 5. Deadlines, estimates, penalties

- Standalone corporate return due date: expected 15th day of 4th month (federal conformity) — **needs-sources**.
- **Estimates: 90% of current-year liability for combined groups** (verified); separate-company estimate rules **needs-sources**; Form 83-105 is the estimate voucher (verified).
- Underpayment/late penalties: **needs-sources**.

## 6. Cross-border notes

Nexus thresholds (P.L. 86-272 protection scope) **needs-sources**. Mississippi taxes the Mississippi-apportioned share of a nonunitary or combined group's income (verified framing).

## 7. Worked examples

**Example 1 — $500,000 Mississippi taxable income at the 5% top band (rate needs-sources):**

```oa-check
name: MS corporate 5 percent
inputs:
  income: 500000
  rate: 0.05
steps:
  - tax: income * rate
expected:
  tax: 25000.00
```

**Example 2 — combined-group estimate floor.** Prior-year combined liability $100,000; the verified 90%-of-current-year rule makes safe-harbor planning anchor on current year, not prior year — illustrate the 90% figure on a projected $120,000 current-year liability:

```oa-check
name: MS combined 90 percent estimates
inputs:
  projected: 120000
  pct: 0.90
steps:
  - required_estimates: projected * pct
expected:
  required_estimates: 108000.00
```

## 8. Ask the client

- Is the group commonly owned above the combined-report threshold? → 83-310 exposure and the 90% estimate rule.
- Are intercompany fees shifting income out of Mississippi inside a combined group?
- Any franchise-tax-applicable entity (banks, certain LLCs)?

## 9. Sources

1. DOR Combined Filing: https://www.dor.ms.gov/taxes/combined-filing — fetched and verified 2026-10-28 (83-310, 83-105, 90% rule).
2. DOR corporate tax landing: https://www.dor.ms.gov/taxes/corporate-income-tax — resolves; rate table not extracted this run.
3. Miss. Code Ann. Title 27 Ch. 7 Art. 1 and Ch. 13 — structure verified via DOR pages.

**Needs-sources:** rate bands, Form 83-100 identity, due dates, separate-company estimate rules, penalties/interest, nexus thresholds, franchise rates, modification detail.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Mississippi corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
