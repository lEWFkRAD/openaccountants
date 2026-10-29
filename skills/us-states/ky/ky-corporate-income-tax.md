---
name: ky-corporate-income-tax
description: >
  Use this skill whenever asked about Kentucky corporate income tax for tax year 2026 — the flat 5% corporation income tax, the Limited Liability Entity Tax (LLET) with its $175 minimum, mandatory unitary combined filing (or 48-month same-as-federal consolidated election), Form 720 mechanics, and the 25%x4 estimated installments due 4/15-6/15-9/15-12/15. Trigger on "Kentucky corporate tax", "Kentucky 720", "LLET", "Kentucky combined filing", "Kentucky consolidated election", "Kentucky estimated tax corporation". ALWAYS load us-tax-workflow-base first.
version: 0.3
jurisdiction: US-KY
category: corporate
tax_year: 2026
last_updated: 2026-10-28
tier: 2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - ky-income-tax
---

# Kentucky corporate income tax + LLET, tax year 2026

> **Source-cited draft.** Built from KRS 141.040, 141.0401, 141.120, 141.202, the DOR Corporation Income & LLET page, Form 720 and TAM-19-02, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

Corporations doing business in Kentucky, deriving income from Kentucky, or registered to do business there (KRS 141.040). Limited liability pass-through entities (LLCs taxed as partnerships) pay the LLET under KRS 141.0401; corporations may elect LLET treatment, with the LLET credited against the income tax on Form 720 Part II.

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Corporation income tax | Flat 5% of taxable net income for tax years beginning on or after 1 January 2018 | KRS 141.040(2): "For taxable years beginning on or after January 1, 2018, the rate of five percent (5%) of taxable net income shall apply"; DOR page: "the previous rate brackets have been replaced with a flat 5% tax rate" |
| Apportionment | Receipts-only fraction: income multiplied by a fraction whose "numerator ... is the total receipts of the taxpayer in this state" and "denominator ... is the total receipts of the taxpayer everywhere" | KRS 141.120(9) |
| LLET minimum | $175 regardless of credits: "The tax shall be the greater of the amount computed under paragraph (b) of this subsection or one hundred seventy-five dollars ($175)" | KRS 141.0401 |
| LLET gross-receipts brackets | Gross receipts ≤ $3,000,000: $175; > $3M but < $6M: $0.095 per $100 of Kentucky gross receipts reduced by the ratio with a $3M denominator (floor $175); ≥ $6M: $0.095 per $100 of Kentucky gross receipts; a parallel gross-profits computation exists and the greater applies | KRS 141.0401 |
| Filing method (TYB on/after 1 Jan 2019) | "Unitary Combined Group filing required; or Group election for a 48 month same-as-federal consolidated group filing; otherwise Separate entity filing if not part of a unitary or consolidated group" | DOR page; KRS 141.202 |

## The taxable base

Kentucky starts from federal taxable income, makes Kentucky adjustments (including the IRC date conformity under KRS 141.010), apportions by the receipts fraction (KRS 141.120), and applies the 5% rate. The DOR page describes "three steps": "1) Make Kentucky adjustments to Federal taxable income ... Kentucky's corporate income tax calculation starts with federal taxable income"; apportion/allocate; then compute tax by "multiplying taxable net income by the Kentucky tax rate." The LLET is computed on Kentucky gross receipts and Kentucky gross profits (whichever method yields more, subject to the $175 minimum) under KRS 141.0401.

Section 179: per the DOR page, the "IRC §179 expense deduction increased to $100,000 for Kentucky for property placed in service on or after January 1, 2020."

## Deadlines and filing

- **Return:** Form 720 follows the federal due date for the taxable year (April 15 for calendar-year filers).
- **Estimated tax (TYB on/after 1 January 2019):** the DOR page states "Four installments at 25% of the estimated tax due on April 15, June 15, September 15, and December 15," with annualization and adjusted seasonal installment methods allowed; the declaration penalty was replaced with an "Addition to Tax" penalty (see TAM-19-02).
- **Federal audit final determinations:** "Taxpayers now have 180 days to submit an amended income tax return to Kentucky from the date the federal audit final determination is issued by the IRS" (DOR page; also reflected in the 740 instructions for individuals).

## Penalties and interest

- Underpayment of estimated tax or LLET is "multiplied by the tax due interest rate" (DOR Penalties, Interest and Fees page), computed per installment under the federal [26 U.S.C. §6654(a)] pattern.
- Late payment and failure to collect/withhold: 2% per 30 days or fraction, capped at 20%, minimum $10 (DOR Penalties, Interest and Fees page).
- Interest on unpaid tax: 9% for calendar year 2026, 10% for 2025, under KRS 131.183(2)(a)2 (DOR interest notices). KRS 141.985 provides that tax not paid by the date due accrues interest "at the tax interest rate as defined in KRS 131.010(6)."

Common failure modes: (1) filing separate-entity when unitary combined is mandatory; (2) treating the 48-month consolidated election casually — it binds for four years; (3) missing the 180-day federal-audit reporting window; (4) forgetting the LLET applies at the $175 minimum even with zero income tax.

## Cross-border points

- Out-of-state affiliates inside a unitary group are pulled into the Kentucky combined computation: KRS 141.202 requires "the group of all corporations whose income and apportionment factors are required to be taken into account," with the combined report filed "on a waters-edge basis" and a 50%+ common-ownership test.
- Apportionment is receipts-only (KRS 141.120(9)), so market-based sales into Kentucky create apportioned income for combined-group members.
- LLET paid by a limited liability pass-through entity credits against members' Kentucky income tax (KRS 141.0401; see `ky-cross-border`).
- Nexus protection: 15 U.S.C. §381 (P.L. 86-272) still shields pure solicitation of tangible-goods orders (see `ky-cross-border`).

## Worked examples

### Example 1: flat 5% on apportioned income (hypothetical facts)

A combined group with $8,000,000 of combined apportionable income and 25% Kentucky receipts factor: Kentucky income $2,000,000; tax $2,000,000 × 5% = $100,000.

```oa-check
name: KY corporate tax flat 5 percent
inputs:
  combined_income: 8000000
  app: 0.25
  rate: 0.05
steps:
  - ky_income: combined_income * app
  - tax: ky_income * rate
expected:
  ky_income: 2000000.00
  tax: 100000.00
```

### Example 2: estimated installments (hypothetical facts)

The same group's estimated tax of $100,000 is paid in four installments of 25%: $25,000 each on April 15, June 15, September 15 and December 15.

```oa-check
name: KY estimated installments 25 percent
inputs:
  tax: 100000
  pct: 0.25
steps:
  - installment: tax * pct
  - four: installment * 4
expected:
  installment: 25000.00
  four: 100000.00
```

### Example 3: LLET brackets (hypothetical facts)

An LLC with Kentucky gross receipts of $8,000,000 (and lower gross-profits computation) is in the ≥ $6,000,000 bracket: LLET $8,000,000 / 100 × $0.095 = $7,600. An LLC with Kentucky gross receipts of $2,000,000 falls in the ≤ $3,000,000 bracket: LLET is the $175 minimum.

```oa-check
name: KY LLET brackets
inputs:
  receipts_small: 2000000
  receipts_large: 8000000
  per_hundred: 0.095
  minimum: 175
steps:
  - llet_small: max(receipts_small / 100 * per_hundred * 0, minimum)
  - llet_large: receipts_large / 100 * per_hundred
expected:
  llet_small: 175.00
  llet_large: 7600.00
```

## Ask the client first

- Is the group unitary under Kentucky's combined-filing mandate, or has the 48-month consolidated election been made (and when does it expire)?
- Are LLC members tracking the LLET credit against their Kentucky income tax?
- Are estimated payments on the 25%x4 calendar, and is annualization used where income is seasonal?
- Any open federal audits — is the 180-day Kentucky amendment calendar tracked?

## Sources

| Source | URL | Read on |
|---|---|---|
| KRS 141.040 (corporation income tax; flat 5% from TYB 2018) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.040 | 2026-10-28 |
| KRS 141.0401 (LLET; $175 minimum; $0.095 per $100 brackets at $3M/$6M) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.0401 | 2026-10-28 |
| KRS 141.120 (apportionment; receipts-only fraction) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.120 | 2026-10-28 |
| KRS 141.202 (unitary combined report; waters-edge; TYB 2019+) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.202 | 2026-10-28 |
| KRS 141.985 (interest on tax not paid by date due) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.985 | 2026-10-28 |
| DOR Corporation Income & LLET page (flat 5%; three-step computation; 48-month election; 25% installments; Addition to Tax; 180 days; Section 179 $100,000) | https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx | 2026-10-28 |
| Form 720 (Corporation Income Tax and LLET return, PDF) | https://revenue.ky.gov/Forms/720.pdf | 2026-10-28 |
| TAM-19-02 Estimated Tax Payments (PDF) | https://revenue.ky.gov/TaxProfessionals/PublishingImages/Pages/Guidance/Estimated%20Tax%20Payments%20TAM-19-02%20FINAL%204.3.19.pdf | 2026-10-28 |
| DOR Penalties, Interest and Fees page (estimated tax penalty; 2%/20%/$10; interest rates) | https://revenue.ky.gov/Collections/Pages/Penalties-Interest-and-Fees.aspx | 2026-10-28 |
| DOR news release: interest rate update for 01-01-26 (9% on unpaid tax) | https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-26.aspx | 2026-10-28 |

Not yet confirmed: the current (2026) Form 720 revision date (the archived Form 720 is the 2019 revision; LLET credit mechanics read from that form); the full list of statutory exceptions to combined-group membership in KRS 141.202(3) (the archived text is the statute itself, but the DOR page's "with some exceptions" shorthand was only cross-checked against the 50% voting-stock rule); the corporate net operating loss provisions in detail (DOR page references NOL provisions; KRS 141.011 not archived this run).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
