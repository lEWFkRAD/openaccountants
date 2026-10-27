---
name: ky-corporate-income-tax
description: >
  Use this skill whenever asked about Kentucky corporate income tax
  for tax year 2026 — the flat 5% corporation income tax, the Limited
  Liability Entity Tax (LLET) with its $175 minimum, mandatory unitary
  combined filing (or 48-month same-as-federal consolidated election),
  Form 720 mechanics, and the 25%×4 estimated installments due
  4/15-6/15-9/15-12/15. Trigger on "Kentucky corporate tax", "Kentucky
  720", "LLET", "Kentucky combined filing", "Kentucky consolidated
  election", "Kentucky estimated tax corporation". Source-cited draft;
  DOR corporate page + Form 720 PDF read 2026-10-27.
jurisdiction: US-KY
category: corporate
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ky-income-tax
---

# Kentucky corporate income tax + LLET v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Kentucky taxes corporations at a **flat 5%** (rate brackets replaced for tax years beginning on/after 2018-01-01) and layers the **Limited Liability Entity Tax (LLET)** on top for LLCs and corporations electing LLET treatment, credited against the income tax. **Source status:** the DOR Corporation Income & LLET page was fetched and text-read 2026-10-27 (revenue.ky.gov, 200) — the flat 5%, the filing-method rules (unitary combined required from TYB 2019-01-01; 48-month same-as-federal consolidated election; separate-entity otherwise), the estimated-tax installment pattern (25% each, 4/15·6/15·9/15·12/15, annualization + adjusted seasonal methods allowed), the "Addition to Tax" penalty replacing the old declaration penalty, and the 180-day federal-audit amendment window are all read from that page. Form 720 (10-19 revision) PDF text-read 2026-10-27 (LLET credit interplay, $175 minimum visible). KRS 141 section pages are JS shells — statutory cites **needs-sources**; the current 2026 form revision was not located — **needs-sources**.

## 2. Who applies

- Corporations doing business in Kentucky, deriving income from Kentucky, or registered to do business there (KRS 141 — section text **needs-sources**).
- **Filing method (from the DOR page, read 2026-10-27):** for tax years beginning on/after 2019-01-01, a **unitary combined group filing is required**; alternatively a group may elect same-as-federal consolidated filing (binding for **48 months**); otherwise separate-entity filing.
- LLCs taxed as partnerships pay **LLET** (gross-receipts based, credited against members' income tax — mechanics per KRS 141.035: **needs-sources**); corporations may elect LLET treatment with the income-tax credit shown on Form 720 Part II Lines 5–6.

## 3. Rates and base

| Item | Rate / base | Source |
|---|---|---|
| Corporation income tax | **flat 5%** (TYB ≥ 2018-01-01) | DOR corporate page, read 2026-10-27 |
| LLET minimum | **$175** (visible on Form 720 credit line) | Form 720 PDF, read 2026-10-27 |
| LLET gross-receipts tiers | tiered on gross receipts (current schedule: **needs-sources**) | KRS 141.035 — JS shell |
| Combined report | unitary combined required (TYB ≥ 2019) | DOR page, read 2026-10-27 |
| Base | federal taxable income with Kentucky modifications (KRS 141.010–141.030 — text **needs-sources**) | DOR page describes 3-step calc |

Kentucky's own page describes the computation in three steps: Kentucky adjustments to federal taxable income → apportion/allocate → apply the 5% rate.

## 4. Deadlines

- **Return:** Form 720 follows the federal due date (April 15 calendar-year; extension available — extension payment required, per DOR page).
- **Estimated tax:** four installments of **25%** of the estimated tax due **April 15, June 15, September 15, December 15**; annualization and adjusted seasonal installment methods allowed (DOR page, read 2026-10-27).
- **Federal audit changes:** amended Kentucky return due within **180 days** of the federal final determination (increased from 30 days; DOR page, read 2026-10-27).

## 5. Penalties and interest

The old declaration penalty was replaced by an **"Addition to Tax" penalty** (KY-TAM-19-02 referenced on the DOR page, read 2026-10-27; current percentages: **needs-sources**). Interest accrues on unpaid amounts (rate: **needs-sources**). Common failure modes: (1) filing separate-entity when unitary combined is mandatory; (2) treating the 48-month consolidated election casually — it binds for four years; (3) missing the 180-day federal-audit reporting window; (4) forgetting LLET still applies at the $175 minimum even with zero income tax.

## 6. Cross-border interactions

- Unitary combined filing means out-of-state affiliates inside the unitary group pull into the Kentucky combined computation (group definition per DOR page: domestic corporations with exceptions — full text **needs-sources**).
- Apportionment/allocation rules (single sales factor history, water's-edge): KRS 141.033–141.043 — JS shells, **needs-sources**.
- LLET paid by an LLC credits against members' Kentucky income tax — relevant for out-of-state members (see `ky-cross-border`).

## 7. Worked examples

A Kentucky-apportioned combined group with $2,000,000 Kentucky taxable income for 2026:

```oa-check
name: KY corporate tax flat 5 percent
inputs:
  ky_income: 2000000
  rate: 0.05
steps:
  - tax: ky_income * rate
expected:
  tax: 100000.00
```

Same group's estimated installments (25% each):

```oa-check
name: KY estimated installments
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

## 8. Ask the client

- Is the group unitary under Kentucky's combined-filing mandate, or has the 48-month consolidated election been made (and when does it expire)?
- Are LLC members tracking the LLET credit against their Kentucky income tax?
- Are estimated payments on the 25%×4 calendar, and is annualization being used where income is seasonal?
- Any open federal audits — is the 180-day Kentucky amendment calendar tracked?

## Sources

1. DOR Corporation Income & LLET page: https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx (200, text read 2026-10-27)
2. Form 720 (10-19) PDF: https://revenue.ky.gov/Forms/720.pdf (200 PDF, text read 2026-10-27; 2026 revision **needs-sources**)
3. Estimated Tax Payments TAM-19-02 PDF: https://revenue.ky.gov/TaxProfessionals/PublishingImages/Pages/Guidance/Estimated%20Tax%20Payments%20TAM-19-02%20FINAL%204.3.19.pdf (linked from DOR page 2026-10-27)
4. KRS ch. 141: https://apps.legislature.ky.gov/law/krs/141/141.010.asp (JS shell — statute text **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kentucky corporate and LLET questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
