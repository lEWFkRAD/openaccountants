---
name: ct-corporate-income-tax
description: >
  Use this skill whenever asked about Connecticut corporate income tax
  for tax year 2026 -- Form CT-1120 filing, the 7.5% income tax under
  Conn. Gen. Stat. §12-214, the 10% surcharge for 2018-2025 income
  years and its 2026 repeal, the phasing-out capital base tax under
  §12-219 (1.6 mills for 2026), economic nexus under §12-216a,
  estimated installments (30/40/10/20) under §12-242d, and penalties
  under §12-229. Trigger on "Connecticut corporate income tax",
  "CT-1120", "Connecticut 7.5 percent", "Connecticut surcharge",
  "Connecticut capital base tax", "Connecticut corporation business
  tax". Source-cited draft; CGA chapter 208 text read 2026-10-28.
jurisdiction: US-CT
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - ct-income-tax
---

# Connecticut corporate income tax v0.2

Covers the Connecticut corporation business tax (Form CT-1120):
income tax, surcharge, capital base tax, nexus, estimates, penalties.
Primary source: Conn. Gen. Stat. chapter 208 full text (cga.ct.gov
current statutes, archived and read 2026-10-28 -- all quoted rates
below are from that text). DRS form PDFs returned HTML to this agent
in a prior run; form-level details are listed under Not yet confirmed.

## Who this applies to

- Every company carrying on or having the right to carry on business
  in Connecticut, taxed on entire net income (§12-214(a)(1)).
- **Economic nexus:** a company with income from Connecticut sources
  and a "substantial economic presence" -- purposeful direction of
  business toward the state, judged by frequency, quantity and
  systematic nature of economic contacts, without regard to physical
  presence (§12-216a(a)).
- General/limited partners doing business through partnerships are
  "carrying on business" (§12-214(a)(3)).
- Exemptions include S corporations (chapter 228z regime instead) and
  companies subject to gross earnings taxes (§12-214(a)(2)).

## Rates, bands and thresholds

| Item | Amount | Source |
|---|---|---|
| Corporation business tax | 7.5% of entire net income (income years from 1/1/2000) | §12-214(a)(1): "at the rate of seven and one-half per cent" |
| Surcharge | 10% of computed tax for income years 1/1/2018–12/31/2025; **no surcharge provision applies to 2026 income years in the current statute text** | §12-214(b)(4): "an additional tax in an amount equal to ten per cent of the tax calculated under said subsection (a)" |
| Capital base tax | larger-of add-on: two and one-tenth mills per dollar for 2025, **one and six-tenths mills per dollar for 2026**, one and one-tenth mills for 2027, **zero mills from 2028** | §12-219(a)(1)(C)-(F) |
| Surcharge exception | no surcharge where the calculated tax "is equal to two hundred fifty dollars" | §12-214(b) |

**2026 planning point:** the surcharge statute text applies to income
years commencing on or after January 1, 2018 and prior to January 1,
2026 -- confirm no successor surcharge was enacted in the 2026 session
before relying.

## The taxable base

- Entire net income = federal taxable income with CT modifications
  (§12-213/§12-217; itemized modifications not itemized here).
- Combined reporting: combined unitary returns for affiliated groups
  (§12-218c–§12-218h; world-wide, affiliated, or water's-edge bases,
  tax-haven rules).
- Capital base: average value of issued capital stock, surplus,
  undivided profits and reserves, less deficits and holdings of
  private-corporation stock, apportioned under §12-219a.
- Apportionment: property/payroll/receipts factors (§12-218;
  unitary-combination definitions at §12-218a et seq.).

## Deadlines and filing

| Filing | Due date |
|---|---|
| CT-1120 annual return | the fifteenth day of the month next succeeding the due date of the company's corresponding federal income tax return, determined without regard to any extension (§12-222(b)) |
| Estimated installments (§12-242d(a)) | the fifteenth day of the third, sixth, ninth and twelfth months of the income year |
| Installment split (§12-242d(b)) | 30% / 40% / 10% / 20% of the required annual payment |

Required annual payment (§12-242d(e)): lesser of 90% of current-year
tax or 100% of prior-year tax shown (prior year must be twelve months
with a filed return).

## Penalties and interest

- Failure to pay tax shown on return: penalty of ten per cent of the
  unpaid amount or fifty dollars, whichever is greater; interest one
  per cent per month or fraction from the due date (§12-229(a)).
- Commissioner-prepared return after three months late: adds ten per
  cent or fifty dollars minimum; no double penalty with (a)
  (§12-229(b)).
- Deficiency assessments: generally a three-year assessment window from
  return due/receipt date, extended for loss carry-over years
  (§12-233(a)); interest on deficiencies one per cent per month from
  the original due date (§12-235).
- Estimated underpayment: interest at one per cent per month on the
  underpayment (§12-242d(c)).
- Commissioner may waive penalties for reasonable cause (§12-229(c)).

## Cross-border points

- Economic-nexus statute (§12-216a) taxes foreign-state and foreign-country
  companies with substantial economic presence; for foreign
  corporations, only income effectively connected with a U.S. trade
  or business is reached, with ECI-only factor sourcing (§12-216a(b)).
- PL 86-272 (federal) still protects qualifying tangible-goods
  solicitation from net-income tax (see `ct-cross-border`).
- Combined group tax-haven rules (§12-218f) reach low-tax affiliate
  income.
- SALT Parity-style elective entity tax: Connecticut's PTE under
  chapter 228z at 6.99% (see `ct-s-corporation-tax`).

## Worked examples

Hypothetical facts. A calendar-year C corporation (gross income
$40,000,000) has 2026 Connecticut-apportioned entire net income of
$2,000,000 and capital base of $50,000,000 apportioned to Connecticut.
Income tax vs capital base tax (2026: no surcharge, capital base at
one and six-tenths mills per dollar -- both from the confirmed rates
table above):

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

The tax due is the larger of the two computed amounts -- here
$150,000.

The same hypothetical facts for a 2025 income year (10% surcharge,
capital base at two and one-tenth mills per dollar -- from the
confirmed rates table):

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

The larger amount governs -- here $165,000 including the 2025
surcharge.

## Ask the client first

- Is the company in the surcharge's last year (2025) or out of it
  (2026) -- and does any 2026 session legislation revive it?
- Does the company have CT economic presence without physical
  presence (remote workers, marketplace, systematic sales)?
- Is the group unitary → combined return, water's-edge election,
  tax-haven exposure?
- Are estimates tracking the 30/40/10/20 split against the 90%/100%
  safe harbor?
- Does the capital base tax still bind (loss or low-income years with
  big balance sheets)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Conn. Gen. Stat. ch. 208 (Corporation Business Tax) §§12-214, 12-216a, 12-218c–h, 12-219, 12-222, 12-229, 12-233, 12-235, 12-242d | https://www.cga.ct.gov/current/pub/chap_208.htm | 2026-10-28 |
| Conn. Gen. Stat. ch. 228z (Affected Business Entity Tax) §§12-699, 12-699a | https://www.cga.ct.gov/current/pub/chap_228z.htm | 2026-10-28 |

Not yet confirmed: the $250 minimum tax shown on Form CT-1120 (the surcharge exception in §12-214(b) for tax "equal to two hundred fifty dollars" suggests it, but the form itself was not verified -- DRS form PDFs returned HTML to this agent); whether any 2026 session legislation revived or replaced the 10% surcharge for income years commencing on or after January 1, 2026.

## Talk to a verified accountant

**Talk to a verified accountant** -- for Connecticut corporate income-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

This skill is a source-cited draft; no accountant has reviewed it. Verify
figures against the cited primary sources or with a licensed Connecticut
professional before relying on them.
