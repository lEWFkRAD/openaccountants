---
name: ms-payroll
description: >
  Use this skill whenever asked about Mississippi payroll withholding for
  2026 — mandatory electronic filing through the Taxpayer Access Point
  (TAP), the MCA § 27-3-83(4) penalty of $25 per return capped at $500
  for paper filing, the 10-or-more electronic mandate for W-2/1099
  filings, and withholding mechanics against the 2026 4% rate. Trigger on
  "Mississippi withholding", "TAP", "Mississippi W-2", "82-111",
  "Mississippi employer withholding". Source-cited draft; TAP mandate,
  § 27-3-83(4) penalty and the 10-return electronic threshold verified on
  DOR pages 2026-10-28; withholding form ID and deposit-frequency
  thresholds needs-sources.
jurisdiction: US-MS
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ms-income-tax
---

# Mississippi payroll withholding v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## 1. Scope and sources

Employer income-tax withholding for Mississippi wages. **Source status:** DOR withholding/TAP pages (fetched and verified 2026-10-28) confirm **electronic filing through the Taxpayer Access Point (TAP) is required; Miss. Code Ann. § 27-3-83(4) imposes a $25-per-return penalty capped at $500 when paper is filed despite the electronic mandate; W-2/1099 information returns must be filed electronically when the filer files 10 or more such returns in a year**. The **withholding return form ID (82-111 is the conventional number — confirm) and deposit-frequency thresholds — needs-sources**.

## 2. Who applies

Every employer paying Mississippi wages (residents and nonresidents working in Mississippi), plus withholding on certain nonresident gambling winnings and other statutory categories (**needs-sources**).

## 3. Rates / tables

Withholding tracks the individual schedule — **2026: 4%** on taxable income above the $10,000 zero-rate band (verified — see `ms-income-tax.md`). Percentage-method tables: **needs-sources**.

## 4. Base

Wages, pensions, and statutory extras (gambling winnings detail **needs-sources**).

## 5. Deadlines, penalties, interest

- Withholding return cadence: monthly/quarterly per deposit rules — **needs-sources**.
- **Electronic filing via TAP mandatory; paper penalty $25/return up to $500 (§ 27-3-83(4))** (verified).
- **10+ W-2/1099s → electronic mandate** (verified).
- Late-payment penalty/interest percentages: **needs-sources**.

## 6. Cross-border notes

Nonresident workers: Mississippi taxes wages for work performed in-state; no reciprocity agreements located (**needs-sources**). Withholding applies regardless of employee residence.

## 7. Worked examples

**Example 1 — paper-filing penalty cap.** Employer files 30 W-2s on paper despite the mandate:

```oa-check
name: MS 27-3-83 penalty cap
inputs:
  returns: 30
  per_return: 25
  cap: 500
steps:
  - raw: returns * per_return
  - penalty: min(raw, cap)
expected:
  penalty: 500.00
```

**Example 2 — quarterly withholding at the 2026 rate.** Mississippi wages $200,000 in a quarter, flat 4% approximation (ignoring the zero-rate band):

```oa-check
name: MS quarterly withholding 4 percent
inputs:
  wages: 200000
  rate: 0.04
steps:
  - withheld: wages * rate
expected:
  withheld: 8000.00
```

## 8. Ask the client

- Is the payroll provider wired to TAP for withholding returns and W-2s?
- Count of information returns — over 10? electronic mandate applies (verified).
- Nonresident remote workers performing days in Mississippi?

## 9. Sources

1. DOR withholding: https://www.dor.ms.gov/taxes/withholding — fetched and verified 2026-10-28 (TAP, § 27-3-83(4), 10-return threshold).
2. DOR individual rates: https://www.dor.ms.gov/taxes/individual-income-tax — fetched 2026-10-28 (2026: 4%).

**Needs-sources:** withholding form ID, deposit frequency, penalty/interest for late deposits, gambling-winnings withholding detail, reciprocity confirmation.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Mississippi payroll questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
