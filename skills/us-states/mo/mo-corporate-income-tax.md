---
name: mo-corporate-income-tax
description: >
  Use this skill whenever asked about Missouri corporate income tax for tax
  year 2026 — the flat 4% rate on Missouri taxable income (Form MO-1120
  line 14), consolidated-federal/separate-Missouri pro forma rule, optional
  Missouri consolidated return (Form MO-22), Form MO-MS apportionment
  elections, Form MO-1120ES estimated tax ($250 threshold, four quarterly
  dates, 90%/100% safe harbors), automatic federal extension, the 5%/month
  late-filing and 5% late-payment additions, 7% simple interest from
  1 January 2026, and charter forfeiture after 90 days of nonfiling.
  Trigger on "Missouri corporate income tax", "MO-1120", "Missouri CBT",
  "Missouri corporation apportionment", "MO-1120ES", "Missouri consolidated
  return", "Form 4458 Missouri".
  Source-cited draft; 2025 MO-1120 instructions and 2026 MO-1120ES read
  2026-10-27.
jurisdiction: US-MO
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - mo-income-tax
---

# Missouri corporate income tax (Form MO-1120) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Covers Missouri corporation income tax (Form MO-1120): who files, the 4% rate, base modifications, apportionment via Form MO-MS, consolidated-return options, estimated tax (MO-1120ES), extensions, penalties, interest, and the dissolution trap. Out of scope: personal income tax (`mo-income-tax`), payroll/withholding and UI (`mo-payroll`), sales/use (`mo-sales-tax`), S corporations (Form 1120-S pass-through level), local earnings taxes (see `mo-cross-border`).

**Source status:** the Department of Revenue **2025 Form MO-1120 instructions** (76,812 chars) and **2026 Form MO-1120ES** (10,406 chars) were fetched as PDFs and read in full on 2026-10-27 — every figure below is quoted from them. The MO-470 instructions PDF and the related-party addback page returned 403/404 from the drafting environment; anything tied to those is flagged **needs-sources**.

## 2. Who applies

- Every corporation required to file a federal Form 1120 with Missouri-source/apportionable Missouri income, unless protected by **P.L. 86-272** (solicitation of orders for tangible personal property). The return has a P.L. 86-272 checkbox; **Form 4458** (Business Activity Questionnaire) documents the claim. (MO-1120 instructions, read 2026-10-27.)
- **Consolidated federal group, separate Missouri return:** a member of an affiliated group filing a consolidated federal return must determine federal taxable income **as if it had filed a separate federal return**, enclosing a **pro forma Federal Form 1120** — unless the group files a Missouri consolidated return. (MO-1120 instructions, "Consolidated Federal Return and Separate Missouri Return", read 2026-10-27.)
- **Missouri consolidated return is optional** and requires the group to be consolidated federally (12 CSR 10-2.045; §143.431 RSMo); attach **Form MO-22** for each member at initiation and for each new member. (Instructions, read 2026-10-27.)
- Federal tax-exempt corporations (Form 990 filers) do not file MO-1120 for exempt income but are taxable on UBTI. (Instructions, read 2026-10-27.)

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| Corporate income tax rate | **4%** flat — MO-1120 line 14: "Enter the amount of Line 13 multiplied by 4 percent. Income tax cannot be prorated or annualized." | MO-1120 2025 instructions, read 2026-10-27; re-verified 2026-10-28 against archived PDF, verbatim match |
| Base | Federal taxable income (separate-company pro forma if federally consolidated) + additions (incl. §163(j) disallowed interest addback, §143.121.3(11)) − Missouri subtraction modifications, × MO apportionment percentage | Instructions, read 2026-10-27 |
| Apportionment | Form MO-MS with apportionment election (2a, 3, 4, 5, 6, or 7); percentage to three decimals (e.g. 12.345%); partnership factors multiplied by ownership % and folded into MO-MS | Instructions, read 2026-10-27 |
| Dividends deduction | Form MO-C: eligible dividends × apportionment percentage factor (from MO-MS Part 1 line 3), plus Missouri-allocated nonapportionable dividends; FDII portion of the federal §250 deduction handled on MO-C line 27 | Instructions, read 2026-10-27 |
| Related-party/intangible addback (§143.471, Form MO-470) | **needs-sources** — MO-470 instructions 403'd on 2026-10-27 and the addback page 404'd; not referenced in the 2025 MO-1120 instructions text read | fetch log 2026-10-27 |
| Minimum tax | none found in the instructions read | booklet read 2026-10-27; absence noted |

## 4. Deadlines

- **Return:** due the **15th day of the 4th month** after year-end (calendar-year 2025 → **15 April 2026**). Weekend/holiday rolls to next business day. (Instructions, read 2026-10-27.)
- **Extension:** automatic with the federal extension — check the box and attach a copy of **Form 7004**; failure to check the box may disallow the extension. (Instructions, read 2026-10-27.)
- **Estimated tax (MO-1120ES):** required if Missouri estimated tax "could reasonably be expected to be at least **$250**" (§143.521 RSMo). Calendar-year installments **15 April / 15 June / 15 September / 15 December**; mid-year income changes trigger catch-up filings at the next date. (2026 MO-1120ES, read 2026-10-27.)
- **Safe harbor:** no underpayment addition if each installment is timely and total estimated payments by the last installment date equal or exceed **90% of the current-year tax** or **the tax shown on the preceding year's return** (12-month year with liability). (2026 MO-1120ES, read 2026-10-27.)
- **Dissolution trap:** a corporation that fails to file **and** pay within **90 days** of the original (or extended) due date **forfeits its Missouri charter** (§351.486). (Instructions, read 2026-10-27.)

## 5. Penalties and interest

- **Late filing:** **5% of unpaid tax per month, capped at 25%** aggregate. (Instructions, "Addition to Tax – Failure to File", read 2026-10-27.)
- **Late payment:** flat **5% of unpaid tax** if not paid by the original due date, even with an extension. (Instructions, read 2026-10-27.)
- **Interest:** **7% simple per annum effective 1 January 2026** (§32.065 RSMo), from the return due date until paid. (Instructions, read 2026-10-27; archived PDF confirms verbatim: "The simple interest rate, effective January 1, 2026, is 7 percent per annum (Section 32.065, RSMo)".)
- **Estimated underpayment:** addition to tax via **Form MO-2220** line 26, with statutory exceptions (§143.761); overpayments are netted against additions (12 CSR 10-2.067). (Instructions, read 2026-10-27.)

## 6. Cross-border / multistate

- Apportionable income includes income from tangible **and intangible** property where acquisition/management/development/disposition relates to the trade or business; nonapportionable income is allocated separately. (Instructions, read 2026-10-27.)
- Another state's minimum tax does not create "taxability" there unless nexus-level activities exist — relevant to credit-for-taxes-paid claims. (Instructions, read 2026-10-27.)
- P.L. 86-272 claim: check the box and attach Form 4458.
- Nonresident individuals: MO-1040P / part-year and nonresident returns plus MO-CR credit — see `mo-cross-border`.

## 7. Worked examples

**Example 1 — Missouri-only C corporation.** Federal taxable income $1,000,000, no modifications, 100% Missouri sources.

```oa-check
name: MO unistate corp tax
inputs:
  income: 1000000
  rate: 0.04
steps:
  - tax: income * rate
expected:
  tax: 40000.00
```

**Example 2 — multistate manufacturer, MO apportionment 12.345%.** Modified income $3,000,000.

```oa-check
name: MO apportioned tax
inputs:
  income: 3000000
  factor: 0.12345
  rate: 0.04
steps:
  - mo_income: income * factor
  - tax: mo_income * rate
expected:
  mo_income: 370350.00
  tax: 14814.00
```

**Example 3 — late filing, 3 months.** $40,000 tax, filed 3 months late, paid at filing.

```oa-check
name: MO late filing penalty
inputs:
  tax: 40000
  monthly: 0.05
  months: 3
  rate_int: 0.07
steps:
  - ftf: min(tax * monthly * months, tax * 0.25)
  - ftp: tax * 0.05
  - interest: tax * rate_int * months / 12
  - total: tax + ftf + ftp + interest
expected:
  ftf: 6000.00
  ftp: 2000.00
  interest: 700.00
  total: 48700.00
```

## 8. Ask the client

1. Federally consolidated? Then which members file separate Missouri returns with pro forma 1120s — or is a Missouri consolidated return (MO-22) in place or worth electing?
2. Which MO-MS apportionment election is in use, and do partnership factors flow through?
3. Are MO-1120ES installments tracking the 90%/100% safe harbor — and is the $250 threshold even met?
4. Any P.L. 86-272 position — is a Form 4458 on file?
5. Any §163(j) disallowed-interest addback or FDII §250 nuance on MO-C?

## 9. Sources

1. Missouri DOR, Form MO-1120 General Instructions (2025): <https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf> — 200 with full text, read 2026-10-27.
2. Missouri DOR, Form MO-1120ES (2026): <https://dor.mo.gov/forms/MO-1120ES_2026.pdf> — 200 with full text, read 2026-10-27.
3. Missouri DOR tax types index: <https://dor.mo.gov/taxation/> — 200, read 2026-10-27.
4. Form MO-470 instructions (related-party addback): <https://dor.mo.gov/forms/MO-470%20Instructions_2025.pdf> — **403 on 2026-10-27, needs-sources**.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Missouri corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
