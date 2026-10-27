---
name: ct-corporate-income-tax
description: >
  Use this skill whenever asked about Connecticut corporate income tax
  for tax year 2026 — Form CT-1120 filing, the 7.5% income tax under
  Conn. Gen. Stat. §12-214, the 10% surcharge for 2018-2025 income
  years and its 2026 repeal, the phasing-out capital base tax under
  §12-219 (1.6 mills for 2026), economic nexus under §12-216a,
  estimated installments (30/40/10/20) under §12-242d, and penalties
  under §12-229. Trigger on "Connecticut corporate income tax",
  "CT-1120", "Connecticut 7.5 percent", "Connecticut surcharge",
  "Connecticut capital base tax", "Connecticut corporation business
  tax". Source-cited draft; CGA chapter 208 text read 2026-10-27.
jurisdiction: US-CT
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ct-income-tax
---

# Connecticut corporate income tax v0.1

## 1. Scope and sources

Covers the Connecticut corporation business tax (Form CT-1120):
income tax, surcharge, capital base tax, nexus, estimates, penalties.
Primary verified source: Conn. Gen. Stat. chapter 208 full text
(cga.ct.gov current statutes, downloaded and read 2026-10-27 — all
quoted rates below are from that text). DRS form PDFs returned HTML
to this agent this run; form-level details flagged where unverified.

## 2. Who applies

- Every company carrying on or having the right to carry on business
  in Connecticut, taxed on entire net income (§12-214(a)(1) —
  verified).
- **Economic nexus:** a company with income from Connecticut sources
  and a "substantial economic presence" — purposeful direction of
  business toward the state, judged by frequency, quantity and
  systematic nature of economic contacts, without regard to physical
  presence (§12-216a(a) — verified).
- General/limited partners doing business through partnerships are
  "carrying on business" (§12-214(a)(3) — verified).
- Exemptions include S corporations (chapter 228z regime instead) and
  companies subject to gross earnings taxes (§12-214(a)(2) —
  verified).

## 3. Rates

| Item | Amount | Source |
|---|---|---|
| Corporation business tax | 7.5% of entire net income (income years from 1/1/2000) | §12-214(a)(1) (verified) |
| Surcharge | 10% of computed tax for income years 1/1/2018–12/31/2025; **no surcharge provision applies to 2026 income years in the current statute text** | §12-214(b)(4) (verified) |
| Capital base tax | larger-of add-on: 2.1 mills/$ for 2025, **1.6 mills/$ for 2026**, 1.1 mills for 2027, **0 mills from 2028** | §12-219(a)(1) (verified) |
| Minimum tax | $250 (statute excepts companies whose tax "is equal to two hundred fifty dollars" from surcharge — implies the $250 minimum; confirm on CT-1120) | §12-214(b) (verified text; form-level needs-sources) |

**2026 planning point:** the surcharge lapses for income years
commencing on or after January 1, 2026 per the current statute text —
verify no successor surcharge was enacted in 2026 session before
relying.

## 4. Base and timing

- Entire net income = federal taxable income with CT modifications
  (§12-213/§12-217 — verified chapter; itemized modifications not
  re-audited this run).
- Combined reporting: combined unitary returns for affiliated groups
  (§12-218c–§12-218h — verified section headings; world-wide,
  affiliated, or water's-edge bases, tax-haven rules).
- Capital base: average value of issued capital stock, surplus,
  undivided profits and reserves, less deficits and holdings of
  private-corporation stock, apportioned under §12-219a (verified).
- Apportionment: property/payroll/receipts factors (§12-218 —
  verified chapter; unitary-combination definitions at §12-218a et
  seq.).

## 5. Deadlines

| Filing | Calendar-year due date |
|---|---|
| CT-1120 annual return | 15th day of the month **after** the federal return due date (no federal-extension consideration) — April 15 for calendar-year C corps (§12-222(b) — verified) |
| Estimated installments (§12-242d(a)) | 15th day of months 3, 6, 9, 12 of the income year — April 15 / June 15 / Sept 15 / Dec 15 (verified) |
| Installment split (§12-242d(b)) | 30% / 40% / 10% / 20% of the required annual payment (verified) |

Required annual payment (§12-242d(e) — verified): lesser of 90% of
current-year tax or 100% of prior-year tax shown (prior year must be
12 months with a filed return).

## 6. Penalties and interest

- Failure to pay tax shown on return: penalty of 10% of the unpaid
  amount or $50, whichever is greater; interest 1% per month or
  fraction from the due date (§12-229(a) — verified).
- Commissioner-prepared return after 3 months late: adds 10% or $50
  minimum; no double penalty with (a) (§12-229(b) — verified).
- Deficiency assessments: generally 3-year assessment window from
  return due/receipt date, extended for loss carry-over years
  (§12-233(a) — verified); interest on deficiencies 1%/month from
  original due date (§12-235 — verified).
- Estimated underpayment: 1%/month interest on the underpayment
  (§12-242d(c) — verified).
- Commissioner may waive penalties for reasonable cause (§12-229(c) —
  verified).

## 7. Cross-border interactions

- Economic-nexus statute (§12-216a) taxes foreign-state and foreign-country
  companies with substantial economic presence; for foreign
  corporations, only income effectively connected with a U.S. trade
  or business is reached, with ECI-only factor sourcing (§12-216a(b) —
  verified).
- PL 86-272 (federal) still protects qualifying tangible-goods
  solicitation from net-income tax (see `ct-cross-border`).
- Combined group tax-haven rules (§12-218f — verified heading) reach
  low-tax affiliate income.
- SALT Parity-style elective entity tax: Connecticut's PTE under
  chapter 228z at 6.99% (see `ct-s-corporation-tax`).

## 8. Worked examples

A calendar-year C corporation (gross income $40,000,000) has 2026
Connecticut-apportioned entire net income of $2,000,000 and capital
base of $50,000,000 apportioned to Connecticut. Income tax vs capital
base tax (2026: no surcharge, 1.6 mills capital base):

```oa-check
name: 2026 larger-of computation
inputs:
  net_income: 2000000
  income_rate: 0.075
  capital_base: 50000000
  mills: 0.0016
steps:
  - income_tax: net_income * income_rate
  - capital_tax: capital_base * mills
expected:
  income_tax: 150000.00
  capital_tax: 80000.00
```

The tax due is the larger of the two computed amounts — here
$150,000.

The same facts for a 2025 income year (10% surcharge, 2.1 mills):

```oa-check
name: 2025 surcharge computation
inputs:
  net_income: 2000000
  income_rate: 0.075
  surcharge: 0.10
  capital_base: 50000000
  mills: 0.0021
steps:
  - income_tax: net_income * income_rate
  - sur: income_tax * surcharge
  - total_income_tax: income_tax + sur
  - capital_tax: capital_base * mills
expected:
  income_tax: 150000.00
  sur: 15000.00
  total_income_tax: 165000.00
  capital_tax: 105000.00
```

The larger amount governs — here $165,000 including the 2025
surcharge.

## 9. Ask the client

- Is the company in the surcharge's last year (2025) or out of it
  (2026) — and does any 2026 session legislation revive it?
- Does the company have CT economic presence without physical
  presence (remote workers, marketplace, systematic sales)?
- Is the group unitary → combined return, water's-edge election,
  tax-haven exposure?
- Are estimates tracking the 30/40/10/20 split against the 90%/100%
  safe harbor?
- Does the capital base tax still bind (loss or low-income years with
  big balance sheets)?

## Sources

1. Conn. Gen. Stat. ch. 208 (Corporation Business Tax) §§12-214, 12-216a, 12-218c–h, 12-219, 12-222, 12-229, 12-233, 12-235, 12-242d: https://www.cga.ct.gov/current/pub/chap_208.htm (200 HTML, read 2026-10-27)
2. Conn. Gen. Stat. ch. 228z (Affected Business Entity Tax) §§12-699, 12-699a: https://www.cga.ct.gov/current/pub/chap_228z.htm (200 HTML, read 2026-10-27)
3. Connecticut DRS Form CT-1120: https://portal.ct.gov/forms (form PDF returned HTML to this agent 2026-10-27 — form-level cites needs-sources)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Connecticut corporate income-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
