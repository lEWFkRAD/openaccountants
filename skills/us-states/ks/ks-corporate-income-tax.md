---
name: ks-corporate-income-tax
description: >
  Use this skill whenever asked about Kansas corporate income tax for tax
  year 2026 — the Form K-120 filing duty for corporations doing business in
  or deriving income from Kansas sources, automatic Subchapter S status for
  Kansas (banks excluded, they file the privilege tax), the repealed
  franchise tax, and federal-extension mechanics. Trigger on "Kansas
  corporate income tax", "K-120", "K-120S", "Kansas privilege tax banks",
  "KDOR corporate". Source-cited draft; KDOR pages read 2026-10-28,
  K.S.A. statute text not machine-readable this run (rates needs-sources).
jurisdiction: US-KS
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ks-income-tax
---

# Kansas corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-28. Covers Kansas corporate income tax (Form K-120), S-corporation treatment, and the bank privilege-tax carve-out. **Source status:** the KDOR Corporate Income page (https://www.ksrevenue.gov/bustaxtypescorp.html, read 2026-10-28) and Franchise page (https://www.ksrevenue.gov/bustaxtypesfranchise.html, read 2026-10-28) were fetched and their text verified. **kslegislature.org statute pages return a JavaScript shell with no server-side text to plain HTTP** — so the **rate brackets (K.S.A. 79-32-110) and the combined-report mechanics are carried as needs-sources**. Never rely on a bracket figure without confirming it against the current statute.

## 2. Who applies

- **All corporations** doing business within or deriving income from sources within Kansas who are required to file a federal income tax return must file a Kansas return, **whether or not tax is due** (KDOR Corporate Income page, read 2026-10-28).
- **Subchapter S corporations** for federal purposes are **automatically** S for Kansas and must file as such — **except banks, savings and loan associations, and trust companies**, which are barred from S status for Kansas and file the **privilege tax return** instead (KDOR FAQ on the same page, read 2026-10-28).
- **Short-period returns:** required for Kansas whenever required federally (same page).
- **501(c)(3) nonprofits:** no Kansas copy of federal Form 990 is required; most still file the Secretary of State annual report (same page).
- **Franchise tax: repealed.** No Kansas franchise tax for tax year 2011 and after; the old KDOR tax (max $20,000, 0.03125% of net worth in its final year, Form K-150) is historical only. A separate **$55 Secretary of State filing fee** with the annual report still applies (KDOR Franchise page, read 2026-10-28).

## 3. Rates and base

| Item | Rule | Source status |
|---|---|---|
| Rate | graduated brackets on Kansas net income — K.S.A. 79-32-110; commonly cited as 4% on the first $50,000 and 12% above | **needs-sources** — statute page is JS-only this run; verify current brackets before use |
| Base | federal taxable income with Kansas modifications; Kansas-source income only for multistate filers | duty verified (KDOR); modification detail needs-sources |
| Apportionment | multistate allocation via Form K-40 Schedule S logic for individuals; corporate apportionment under K.S.A. 79-32.140 series | **needs-sources** (formula factors not machine-readable) |
| Combined report | affiliated-group combined reporting exists post-SB 2017 debate era; form ID (K-120M) unverified | **needs-sources** |
| Banks | privilege tax return, not K-120 (S-corp banks included) | verified (KDOR FAQ) |

## 4. Deadlines

- K-120: due the **15th day of the 4th month** after year end (April 15 calendar-year filers) — consistent with the KDOR franchise-page due-date language; corporate-specific citation **needs-sources**.
- **Federal extension honored:** "Kansas accepts the federal extension of time and will follow accordingly. The extension of time is to file the return not pay the tax. **Ninety percent of the tax must be paid by the due date to avoid late payment penalty**" (KDOR Corporate Income page, read 2026-10-28 — verified quote).
- Estimated tax: corporate ES mechanics **needs-sources**.

## 5. Penalties and interest

- Late-payment penalty avoided only if **90%** of tax is paid by the due date (verified quote above).
- Interest and late-filing percentages under K.S.A. 79-32-173 et seq. — **needs-sources**.

## 6. Cross-border interactions

- Non-Kansas corporations with Kansas-source income file K-120 and apportion (see `ks-cross-border`).
- S-corp shareholders: Kansas taxes the distributive share; nonresident shareholders file K-40PN/Schedule S Part B (needs-sources for form IDs).
- No Kansas franchise or gross-receipts tax to stack on top (franchise repealed, KDOR page verified).

## 7. Worked examples

**Example 1 — C corporation with 80% Kansas apportionment (bracket rates illustrative, needs-sources):** $120,000 federal-basis Kansas-unitary income, apportionment factor 0.80.

```oa-check
name: KS corporate graduated tax (illustrative brackets)
inputs:
  income: 120000
  factor: 0.80
  bracket1_top: 50000
  rate1: 0.04
  rate2: 0.12
steps:
  - ks_income: income * factor
  - band1: min(ks_income, bracket1_top) * rate1
  - band2: max(ks_income - bracket1_top, 0) * rate2
  - tax: band1 + band2
expected:
  ks_income: 96000
  band1: 2000
  band2: 5520
  tax: 7520
```

**Example 2 — extension safe harbor on the same facts:** the corporation extends via federal Form 7006; how much must be paid by April 15 to avoid the late-payment penalty?

```oa-check
name: KS 90% extension payment
inputs:
  tax: 7520
  safe: 0.90
steps:
  - must_pay: tax * safe
  - balance_due: tax - must_pay
expected:
  must_pay: 6768
  balance_due: 752
```

## 8. Ask the client

- Federal filing status (C, S, bank/thrift/trust company) — drives K-120 vs K-120S vs privilege return.
- Kansas nexus footprint: property, payroll, sales by state — drives the apportionment factor.
- Affiliated group members in other states — combined-report exposure.
- Whether 90% of estimated tax was paid by the unextended due date before relying on the federal extension.

## 9. Sources

- KDOR Corporate Income (filing duty, S auto-status, bank privilege carve-out, 90% extension rule): https://www.ksrevenue.gov/bustaxtypescorp.html — read 2026-10-28, text verified.
- KDOR Franchise (repealed 2011+; SOS $55 fee): https://www.ksrevenue.gov/bustaxtypesfranchise.html — read 2026-10-28, text verified.
- K.S.A. 79-32-110 (corporate rates): https://www.kslegislature.org/li/b2025_26/statutes/2025_79-32-110/ — page resolves HTTP 200 but serves a JS shell; **rates needs-sources**.
- KDOR forms index: https://www.ksrevenue.gov/forms.html — read 2026-10-28.

**Needs-sources:** current bracket rates (K.S.A. 79-32-110), apportionment factor detail (79-32.140 series), combined-report form/threshold, corporate ES mechanics, penalty/interest percentages.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kansas corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
