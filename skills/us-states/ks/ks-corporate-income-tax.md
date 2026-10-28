---
name: ks-corporate-income-tax
description: >
  Use this skill whenever asked about Kansas corporate income tax for tax
  year 2026 — the Form K-120 filing duty for corporations doing business in
  or deriving income from Kansas sources, automatic Subchapter S status for
  Kansas (banks excluded, they file the privilege tax), the repealed
  franchise tax, and federal-extension mechanics. Trigger on "Kansas
  corporate income tax", "K-120", "K-120S", "Kansas privilege tax banks",
  "KDOR corporate". Corrected 2026-10-28 against archived statute text:
  K.S.A. 79-32,110(c) normal tax 4% + surtax 3% over $50,000 (NOT a 12%
  bracket), no rate reduction for TY2026 per KDOR Notice 25-06.
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

# Kansas corporate income tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Covers Kansas corporate income tax (Form K-120), S-corporation treatment, and the bank privilege-tax carve-out. **Source status:** corrected 2026-10-28 against archived statute text from ksrevisor.gov (the kslegislature.org JS shell was bypassed via the Revisor's static chapter pages): **K.S.A. 79-32,110** (`SRC-US-KS-79-32110.html`), **79-32,110c** rate-reduction mechanism (`SRC-US-KS-79-32110c.html`), **79-32,101/103** estimated tax, **79-32,107** penalties, **79-32,141/142** allocation/consolidation, plus **KDOR Notice 25-06** (`SRC-US-KS-DORE-notice-25-06.pdf`) and the KDOR 2025 Corporate Tax Booklet.

## 2. Who applies

- **All corporations** doing business within or deriving income from sources within Kansas who are required to file a federal income tax return must file a Kansas return, **whether or not tax is due** (KDOR Corporate Income page + Corporate Tax Booklet, archived).
- **Subchapter S corporations** for federal purposes are **automatically** S for Kansas and must file as such (Form K-120S) — **except banks, savings and loan associations, and trust companies**, which are barred from S status for Kansas and file the **privilege tax return** instead (KDOR FAQ, archived).
- **Short-period returns:** required for Kansas whenever required federally (same page).
- **501(c)(3) nonprofits:** no Kansas copy of federal Form 990 is required; most still file the Secretary of State annual report (same page).
- **Franchise tax: repealed.** No Kansas franchise tax for tax year 2011 and after; the old KDOR tax (max $20,000, 0.03125% of net worth in its final year, Form K-150) is historical only. A separate **$55 Secretary of State filing fee** with the annual report still applies (KDOR Franchise page, read 2026-10-28).

## 3. Rates and base

| Item | Rule | Source |
|---|---|---|
| Normal tax | **4%** of Kansas taxable income | K.S.A. 79-32,110(c)(1), archived `SRC-US-KS-79-32110.html` |
| Surtax | **3%** of Kansas taxable income **in excess of $50,000** (one surtax exemption per corporate taxpayer) | K.S.A. 79-32,110(c)(2) + Corporate Tax Booklet line 30 instructions |
| TY2026 rate reduction | **None** — FY2025 adjusted collections did not exceed inflation-adjusted base-year revenues, so the Secretary published no reduction | KDOR **Notice 25-06** (archived PDF, text verified) |
| Future reductions | 79-32,110c (SB 291 mechanism, L. 2025 ch. 116): surtax decreases only until **combined normal+surtax = 4%**; 79-32,110d adds a corporate-receipts trigger from FY2028 | archived `SRC-US-KS-79-32110c.html` |
| Base | federal taxable income with Kansas modifications (K.S.A. 79-32,138); Kansas-source income for multistate filers | statute index + Booklet |
| Apportionment | UDITPA three-factor formula (property/payroll/sales, equal-weighted) per KDOR Booklet; § 79-32,141 gives the director allocation authority for affiliated/controlled groups | `SRC-US-KS-79-32141.html` + Booklet |
| Combined/consolidated | **79-32,142**: federal-consolidated groups with all-Kansas income **must** file consolidated; director may permit/require for affiliated groups (Schedule K-121 mechanics per Booklet) | `SRC-US-KS-79-32142.html` + Booklet |
| Banks | privilege tax return (79-1107/1108), not K-120 | verified (KDOR FAQ) |

**Correction:** the v0.1 draft carried "commonly cited as 4% first $50,000 and 12% above" — the 12% figure is obsolete (pre-2022 law). Current law is 4% + 3% surtax over $50,000 = **7% marginal** on income above $50,000.

## 4. Deadlines

- K-120: **April 15, 2026** for calendar-year filers; fiscal-year returns due the 15th day of the 4th month after year end; Kansas conforms to federal due dates (Corporate Tax Booklet, archived: "Payment of any liability shall be due April 15, 2026").
- **Federal extension honored:** "Kansas accepts the federal extension of time and will follow accordingly. The extension of time is to file the return not pay the tax. **Ninety percent of the tax must be paid by the due date to avoid late payment penalty**" (KDOR Corporate Income page — verified quote).
- Estimated tax: required if Kansas liability **reasonably expected to exceed $500** (K.S.A. 79-32,101(a)(2), archived). Installments **April 15, June 15, September 15, and December 15** for corporations (79-32,103(a)(1) — note the corporate 4th installment is Dec 15, not Jan 15). First-year Kansas filers exempt from estimates and the underpayment penalty (Booklet). Form K-120ES.

## 5. Penalties and interest

- Late-payment penalty avoided only if **90%** of tax is paid by the due date (verified quote above).
- Estimated-tax underpayment: interest at the delinquent-tax rate (K.S.A. 79-2968(b)) on the shortfall, measured against **90% of the tax shown on the return**; not added if under $1 (79-32,107(a), archived).
- Late-filing addition and interest rates: K.S.A. 79-3228 series — **needs-sources** (percentages not yet archived).

## 6. Cross-border interactions

- Non-Kansas corporations with Kansas-source income file K-120 and apportion (see `ks-cross-border`).
- S-corp shareholders: Kansas taxes the distributive share (79-32,139); nonresident shareholders file K-40 (needs-sources for exact nonresident form ID).
- No Kansas franchise or gross-receipts tax to stack on top (franchise repealed, KDOR page verified).

## 7. Worked examples

**Example 1 — C corporation with 80% Kansas apportionment (statutory 4% + 3% surtax):** $120,000 federal-basis Kansas-unitary income, apportionment factor 0.80.

```oa-check
name: KS corporate tax statutory rates
inputs:
  income: 120000
  factor: 0.80
  normal: 0.04
  surtax: 0.03
  exemption: 50000
steps:
  - ks_income: income * factor
  - band1: ks_income * normal
  - band2: max(ks_income - exemption, 0) * surtax
  - tax: band1 + band2
expected:
  ks_income: 96000
  band1: 3840
  band2: 1380
  tax: 5220
```

**Example 2 — extension safe harbor on the same facts:** the corporation extends via federal Form 7006; how much must be paid by April 15 to avoid the late-payment penalty?

```oa-check
name: KS 90% extension payment
inputs:
  tax: 5220
  safe: 0.90
steps:
  - must_pay: tax * safe
  - balance_due: tax - must_pay
expected:
  must_pay: 4698
  balance_due: 522
```

## 8. Ask the client

- Federal filing status (C, S, bank/thrift/trust company) — drives K-120 vs K-120S vs privilege return.
- Kansas nexus footprint: property, payroll, sales by state — drives the apportionment factor.
- Affiliated group members in other states — consolidated-return exposure under 79-32,142.
- Whether 90% of estimated tax was paid by the unextended due date before relying on the federal extension.

## 9. Sources

1. **K.S.A. 79-32,110** (rates: 4% normal + 3% surtax over $50,000): https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html — archived `SRC-US-KS-79-32110.html`, fetched 2026-10-28.
2. **K.S.A. 79-32,110c** (rate-reduction mechanism; surtax floor at combined 4%): archived `SRC-US-KS-79-32110c.html`.
3. **KDOR Notice 25-06** ("there will be no rate reduction for tax year 2026"): https://www.ksrevenue.gov/taxnotices/notice25-06.pdf — archived `SRC-US-KS-DORE-notice-25-06.pdf`, pdftotext verified.
4. **KDOR 2025 Corporate Tax Booklet** (April 15, 2026 due date, K-121 combined mechanics, $500 estimate threshold, 3-factor formula): https://www.ksrevenue.gov/corpbook25.html — archived `SRC-US-KS-DORE-corp-booklet-2025.html`.
5. **K.S.A. 79-32,101 / 79-32,103** (estimated tax $500 threshold; corporate installments Apr 15/Jun 15/Sep 15/Dec 15): archived sidecars.
6. **K.S.A. 79-32,107** (underpayment interest at 79-2968(b) rate, 90% measure): archived.
7. **K.S.A. 79-32,141 / 79-32,142** (allocation; consolidated returns): archived.
8. KDOR Corporate Income (filing duty, S auto-status, bank privilege carve-out, 90% extension rule): https://www.ksrevenue.gov/bustaxtypescorp.html — archived `SRC-US-KS-DORE-corp-tax-page.html`.
9. KDOR Franchise (repealed 2011+; SOS $55 fee): https://www.ksrevenue.gov/bustaxtypesfranchise.html — read 2026-10-28, text verified.

**Needs-sources:** late-filing addition percentage (79-3228 series), current interest rate under 79-2968(b), nonresident S-shareholder form ID, KW-110 deposit thresholds (scanned PDF — OCR pending).

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kansas corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
