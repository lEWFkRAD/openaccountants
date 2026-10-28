---
name: hi-corporate-income-tax
description: >
  Use this skill whenever asked about Hawaii corporate income tax for tax
  year 2026 — HRS ch. 235 subch. IV rates (4.4%/5.4%/6.4% graduated), Form
  N-30, estimated tax under HRS §235-97, the §235-4.2 economic-nexus
  presumption, and three-factor apportionment under §235-29. Trigger on
  "Hawaii corporate income tax", "Hawaii N-30", "HRS 235-71", "Hawaii
  corporation tax rates", "Hawaii franchise tax". Source-cited draft;
  statute text read from capitol.hawaii.gov 2026-10-27.
jurisdiction: US-HI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - hi-income-tax
---

# Hawaii corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Hawaii taxes corporations with a **graduated net-income tax under HRS chapter 235 part IV** — not a franchise or gross-receipts tax (the General Excise Tax is a separate seller-side excise; see `hi-sales-tax`). Statute text below was read directly from the Hawaii Revised Statutes mirror at capitol.hawaii.gov on 2026-10-27. **Source status:** rates, apportionment formula, nexus presumption, estimated-tax mechanics, and penalty/interest provisions are verified from statute; the 2026 federal-conformity date and current administrative-rule citations could not be extracted from tax.hawaii.gov this run (HTTP 429 rate-limiting) — flagged **needs-sources** where relied on.

## 2. Who applies

- Every "corporation" for HRS ch. 235 purposes, including professional corporations under HRS ch. 415A, and **corporations carrying on business in partnership** (HRS §235-72 — treated as the IRC treats them; text read 2026-10-27).
- Resident corporations: entire income. Nonresident (foreign) corporations: Hawaii-source income only (HRS §235-4(b); text read 2026-10-27).
- **Economic nexus presumption** (HRS §235-4.2, text read 2026-10-27): a person lacking physical presence in Hawaii is presumed to be systematically and regularly engaging in business — and therefore taxable — if in the current or preceding calendar year it (1) engages in **200 or more business transactions** with persons in the State, or (2) its Hawaii-attributable gross income (or sales-factor numerator for out-of-State business) is **$100,000 or more**.
- Real estate investment companies (RICs) and REITs are taxed under special subsections of §235-71 (text read 2026-10-27).

## 3. Rates and base

**Base:** taxable income computed under HRS ch. 235, which conforms to the Internal Revenue Code subject to the modifications in §§235-2.3 to 235-2.45 (conformity architecture read from the ch. 235 table of contents, 2026-10-27; the current-year federal conformity date — **needs-sources**, tax.hawaii.gov unreachable this run).

**Rates (HRS §235-71(a), text read 2026-10-27):**

| Taxable income | Rate |
|---|---|
| ≤ $25,000 | 4.4% |
| > $25,000 but ≤ $100,000 | 5.4% |
| > $100,000 | 6.4% |

The rates apply on a graduated (bracket) basis as written in the statute.

**Alternative tax on net capital gain** (HRS §235-71.5, text read 2026-10-27): if less than the regular tax, a corporation with net capital gain may be taxed at 3.08% on pre-1987-treatment gain amounts plus 4% on the excess capital gain, with the remaining income taxed at the regular graduated rates.

**Apportionment** (HRS §235-29, text read 2026-10-27): all business income is apportioned by the classic **three-factor formula** — (property factor + payroll factor + sales factor) ÷ 3. Hawaii has not adopted single-sales-factor apportionment in the statute text read.

## 4. Returns and deadlines

- **Form N-30** annual return; the statutory filing-time rule (§235-98, text read 2026-10-27) allows the department to grant extensions, capped at **six months**. The customary N-30 due date is the 20th day of the fourth month after year-end (calendar-year filers: April 20) — consistent with the §235-97 estimated-tax calendar; confirm the current form instruction (**needs-sources**).
- **Estimated tax** (HRS §235-97, text read 2026-10-27): corporations (including S corporations), estates, trusts, and individuals file estimated declarations and pay in **four installments — April 20, June 20, September 20, and January 20** of the following year (calendar-year taxpayers). Fiscal-year taxpayers follow the equivalent 4th/6th/9th-month and 1st-month-of-following-year pattern per §235-97(3).

## 5. Penalties and interest

HRS §231-39 (text read 2026-10-27), applied to income tax via §235-104:

| Item | Amount |
|---|---|
| Failure to file | 5% of tax per month, capped at 25% (reasonable-cause exception) |
| Failure to pay due to negligence/intentional disregard | up to 25% of underpayment |
| Fraud | up to 50% of underpayment (replaces the failure-to-file penalty) |
| Timely-filed return, tax unpaid after 60 days | up to 20% of unpaid tax |
| Interest on underpayment | **⅔ of 1% per month** (≈8%/yr) from the due date |

Common failure modes: (1) treating the GET as the only Hawaii business tax and never filing N-30; (2) ignoring the §235-4.2 transaction-count nexus presumption for e-commerce/remote sellers; (3) applying single-sales-factor apportionment out of habit — Hawaii's statute is three-factor.

## 6. Cross-border interactions

- Foreign corporations: Hawaii-source income only, apportioned under §235-29; the §235-4.2 presumption can create filing obligations with **no physical presence**.
- Combined/group reporting: Hawaii's statute text read this run does not impose mandatory combined reporting; unitary-group and related-party intangible planning detail — **needs-sources**.
- Federal conformity: ch. 235 adopts IRC provisions subject to listed non-operative sections (§§235-2.3, 235-2.35); the current conformity date — **needs-sources**.

## 7. Worked examples

A calendar-year C corporation with $200,000 Hawaii-apportioned taxable income:

```oa-check
name: HI corporate graduated tax 200k
inputs:
  income: 200000
steps:
  - bracket1: min(income, 25000) * 0.044
  - bracket2: (min(income, 100000) - 25000) * 0.054
  - bracket3: max(income - 100000, 0) * 0.064
  - tax: bracket1 + bracket2 + bracket3
expected:
  bracket1: 1100.00
  bracket2: 4050.00
  bracket3: 6400.00
  tax: 11550.00
```

A nonresident corporation with $1,000,000 unitary business income and a three-factor apportionment factor of 0.35 (illustrative factors):

```oa-check
name: HI apportioned foreign corp base
inputs:
  income: 1000000
  property_factor: 0.30
  payroll_factor: 0.25
  sales_factor: 0.50
steps:
  - factor: (property_factor + payroll_factor + sales_factor) / 3
  - hi_base: income * factor
expected:
  factor: 0.35
  hi_base: 350000.00
```

## 8. Ask the client

- Is the entity's Hawaii transaction count or Hawaii sales-factor numerator near the §235-4.2 thresholds (200 transactions / $100,000) even without a physical office?
- Are estimated payments being made on the 4/20, 6/20, 9/20, 1/20 calendar?
- Is the group modeling Hawaii on a three-factor formula, not single-sales-factor?
- Any capital-gain year where the §235-71.5 alternative tax could be lower?

## Sources

1. HRS §235-71 (rates): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0071.htm (200, text read 2026-10-27 — 4.4/5.4/6.4%)
2. HRS §235-71.5 (alternative capital-gain tax): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0071_0005.htm (200, text read 2026-10-27)
3. HRS §235-72 (corporations in partnership): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0072.htm (200, text read 2026-10-27)
4. HRS §235-4 (residents/nonresidents): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004.htm (200, text read 2026-10-27)
5. HRS §235-4.2 (nexus presumption): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004_0002.htm (200, text read 2026-10-27)
6. HRS §235-29 (three-factor apportionment): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0029.htm (200, text read 2026-10-27)
7. HRS §235-97 (estimated tax dates): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0097.htm (200, text read 2026-10-27)
8. HRS §235-98 (returns, 6-month extension cap): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0098.htm (200, text read 2026-10-27)
9. HRS §231-39 (penalties, ⅔% monthly interest): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm (200, text read 2026-10-27)
10. HRS §235-104 (penalties apply to income tax): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0104.htm (200, text read 2026-10-27)
11. Hawaii Department of Taxation tax-law page (conformity date, forms): https://tax.hawaii.gov/legal/taxlawandrules/ (search-result reference; direct fetch rate-limited 429 this run — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Hawaii corporate-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
