---
name: hi-corporate-income-tax
description: >
  Use this skill whenever asked about Hawaii corporate income tax for tax
  year 2026 -- HRS ch. 235 subch. IV rates (4.4%/5.4%/6.4% graduated), Form
  N-30, estimated tax under HRS §235-97, the §235-4.2 economic-nexus
  presumption, and three-factor apportionment under §235-29. Trigger on
  "Hawaii corporate income tax", "Hawaii N-30", "HRS 235-71", "Hawaii
  corporation tax rates", "Hawaii franchise tax". Source-cited draft;
  statute text read from capitol.hawaii.gov 2026-10-27 and 2026-10-28.
jurisdiction: US-HI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - hi-income-tax
---

# Hawaii corporate income tax v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from HRS §§235-4, 235-4.2, 235-29, 235-71, 235-71.5, 235-72, 235-97, 235-98, 235-104 and §231-39, read on capitol.hawaii.gov (runs of 2026-10-27 and 2026-10-28). No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

Hawaii taxes corporations with a **graduated net-income tax under HRS chapter 235 part IV** -- not a franchise or gross-receipts tax (the General Excise Tax is a separate seller-side excise; see `hi-sales-tax`). Rates, the apportionment formula, the nexus presumption, estimated-tax mechanics, and the penalty/interest provisions below are verified from the statute text archived in the Sources table.

## Who this applies to

- Every "corporation" for HRS ch. 235 purposes, including professional corporations under HRS ch. 415A, and **corporations carrying on business in partnership** (HRS §235-72 -- treated as the IRC treats them; text read 2026-10-27).
- Resident corporations: entire income. Nonresident (foreign) corporations: Hawaii-source income only (HRS §235-4(b); text read 2026-10-27).
- **Economic nexus presumption** (HRS §235-4.2): a person that lacks physical presence in the State is presumed to be systematically and regularly engaging in business -- and therefore taxable -- if during the current or preceding calendar year it (1) "engages in two hundred or more business transactions with persons within the State", or (2) its Hawaii-attributable gross income (or sales-factor numerator for a business within and without the State) "equals or exceeds $100,000".
- Real estate investment companies (RICs) and REITs are taxed under special subsections of §235-71 (text read 2026-10-27).

## Rates, bands and thresholds

**Base:** taxable income computed under HRS ch. 235, which conforms to the Internal Revenue Code subject to the modifications in §§235-2.3 to 235-2.45 (conformity architecture read from the ch. 235 table of contents, 2026-10-27).

**Rates (HRS §235-71(a), text read 2026-10-27):** "The tax on all taxable income shall be at the rate of 4.4 per cent if the taxable income is not over $25,000, 5.4 per cent if over $25,000 but not over $100,000, and on all over $100,000, 6.4 per cent."

| Taxable income | Rate |
|---|---|
| Not over $25,000 | 4.4% |
| Over $25,000 but not over $100,000 | 5.4% |
| Over $100,000 | 6.4% |

The rates apply on a graduated (bracket) basis as written in the statute.

**Alternative tax for corporations** (HRS §235-71.5): the archived statute text reads: "§235-71.5  Alternative tax for corporations.  Section 1201 (with respect to alternative tax for corporations) of the Internal Revenue Code of 1986, as amended as of December 31, 1996, shall be operative for the purposes of this chapter." Hawaii does not state alternative-tax percentages in this section; it incorporates IRC §1201 as amended as of December 31, 1996 (text read 2026-10-28).

**Apportionment** (HRS §235-29): "All business income shall be apportioned to this State by multiplying the income by a fraction, the numerator of which is the property factor plus the payroll factor plus the sales factor, and the denominator of which is three." Hawaii has not adopted single-sales-factor apportionment in the statute text read.

## The taxable base

- Resident corporations: entire income regardless of source (§235-4(a)); nonresident (foreign) corporations: Hawaii-source income only (§235-4(b)).
- Business income is apportioned with the §235-29 three-factor formula; nonbusiness income is allocated under §§235-24 to 235-27 (see `hi-transfer-pricing`).
- §235-7.3 can exclude patent/copyright/trade-secret royalties from gross income entirely when owned by, and arising out of, a "qualified high technology business" (see `hi-transfer-pricing`).

## Deadlines and filing

- **Estimated tax** (HRS §235-97): corporations (including S corporations), estates, trusts, and individuals file estimated declarations and pay in **four installments** -- for calendar-year taxpayers the first voucher is filed "on or before April 20", with payments due the twentieth day of June and September and the fourth-quarter payment "by January 20 of the year following the taxable year" (text read 2026-10-27). Fiscal-year taxpayers follow the equivalent pattern per §235-97. Estimated tax is not required "in the case of a taxpayer whose tax liability is less than $500" (§235-97(a)(6)).
- **Returns** (§235-98): corporate returns are in the form the department prescribes and are authenticated by an authorized officer; the statute authorizes the department to grant extensions. The customary N-30 due date for calendar-year filers follows the ch. 235 estimated-tax calendar (April 20); see Not yet confirmed below on the current form-instruction due date.
- The federal-conformity date and current administrative-rule citations: see Not yet confirmed below.

## Penalties and interest

HRS §231-39, applied to income tax through §235-104 ("The penalties and interest provided by section 231-39 shall apply to employers as well as taxpayers."):

| Item | Amount (HRS §231-39, text read 2026-10-27) |
|---|---|
| Failure to file | "five per cent of the amount of the tax if the failure is for not more than one month, with an additional five per cent for each additional month or fraction", "not exceeding twenty-five per cent in the aggregate" (reasonable-cause exception) |
| Failure to pay due to negligence or intentional disregard | "there shall be added to the tax an amount up to twenty-five per cent of the underpayment" |
| Fraud | "an amount up to fifty per cent of the underpayment" (replaces the failure-to-file penalty) |
| Timely-filed return, tax not completely paid within 60 days | "there shall be added to the unpaid tax an amount up to twenty per cent" |
| Interest on underpayment | "interest on such amount at the rate of two-thirds of one per cent a month or fraction of a month" from the date prescribed for payment |

Common failure modes: (1) treating the GET as the only Hawaii business tax and never filing N-30; (2) ignoring the §235-4.2 transaction-count nexus presumption for e-commerce/remote sellers; (3) applying single-sales-factor apportionment out of habit -- Hawaii's statute is three-factor.

## Cross-border points

- Foreign corporations: Hawaii-source income only, apportioned under §235-29; the §235-4.2 presumption can create filing obligations with **no physical presence**.
- Combined/group reporting: the statute text read does not impose mandatory combined reporting; unitary-group and related-party intangible planning detail -- see Not yet confirmed below.
- Federal conformity: ch. 235 adopts IRC provisions subject to listed non-operative sections (§§235-2.3, 235-2.35); the current conformity date -- see Not yet confirmed below.

## Worked examples

### Example 1: calendar-year C corporation, Hawaii-apportioned taxable income $200,000 (hypothetical client facts)

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

(Rates are the confirmed §235-71 brackets above.)

### Example 2: nonresident corporation, $1,000,000 unitary business income, hypothetical three-factor apportionment factors 0.30 / 0.25 / 0.50

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

(The ÷3 formula is the confirmed §235-29 rule; the factor values are hypothetical client facts.)

## Ask the client first

1. Is the entity's Hawaii transaction count or Hawaii sales-factor numerator near the §235-4.2 thresholds (200 transactions / $100,000) even without a physical office?
2. Are estimated payments being made on the 4/20, 6/20, 9/20, 1/20 calendar?
3. Is the group modeling Hawaii on a three-factor formula, not single-sales-factor?
4. Any capital-gain year where the §235-71.5 alternative tax could be lower?
5. Is the entity relying on a federal-conformity date that has not been confirmed for the current tax year?

## Sources

| Source | URL | Read on |
|---|---|---|
| HRS §235-71 (corporation tax rates 4.4/5.4/6.4%) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0071.htm | 2026-10-28 |
| HRS §235-71.5 (alternative tax for corporations; incorporates IRC §1201 as of 12/31/1996) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0071_0005.htm | 2026-10-28 |
| HRS §235-72 (corporations in partnership) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0072.htm | 2026-10-28 |
| HRS §235-4 (residents/nonresidents) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004.htm | 2026-10-28 |
| HRS §235-4.2 (nexus presumption: 200+ transactions / $100,000) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004_0002.htm | 2026-10-28 |
| HRS §235-29 (three-factor apportionment) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0029.htm | 2026-10-28 |
| HRS §235-97 (estimated tax; $500 de minimis; installment dates) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0097.htm | 2026-10-28 |
| HRS §235-98 (returns; form; extensions) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0098.htm | 2026-10-28 |
| HRS §231-39 (penalties; ⅔%/month interest) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm | 2026-10-28 |
| HRS §235-104 (penalties apply to income tax) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0104.htm | 2026-10-28 |
| HRS ch. 235 table of contents (subch. IV; §§235-2.3–2.45 conformity architecture) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-.htm | 2026-10-28 |

Not yet confirmed: the current-year federal IRC conformity date adopted by HRS §235-2.3 (the archived department tax-law page could not be parsed for a specific date this run); the exact current N-30 due-date wording in the form instructions (the statutory calendar implies April 20 for calendar-year filers); mandatory combined reporting / unitary-group filing requirements; addback rules for related-party intangibles; and current administrative-rule (HAR ch. 18-235) citations. Each of these was flagged in v0.2 and has not been tied to an archived primary source, so no figure for them is asserted here.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
