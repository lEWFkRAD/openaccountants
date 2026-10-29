---
name: dc-payroll-withholding
description: >
  Use this skill whenever asked about District of Columbia payroll
  withholding for tax year 2026 — the OTR withholding regime: FR-900Q
  quarterly withholding return (mandatory e-file since tax year
  2023), FR-900A annual reconciliation, FR-900NP for 1099/W-2G,
  FR-900P, WT-1/WT-2 wage-and-tax transmittals, the D-4 employee
  withholding certificate, deposit due dates, and household-employer
  rules. Trigger on "DC withholding", "DC FR-900Q", "DC FR-900A",
  "DC D-4", "District of Columbia withholding deposit", "DC W-2
  filing DC", "DC household employer withholding".
jurisdiction: US-DC
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - dc-income-tax
---

# District of Columbia payroll withholding, tax year 2026

> **Source-cited draft.** Built from the OTR Withholding Tax Forms page and D.C. Code §§ 47-4201 and 47-4213, read on 2026-10-28. No accountant has reviewed it. Do not run a payroll from it without review by a qualified professional.

DC withholding is administered by the **Office of Tax and Revenue (OTR)**. The OTR Withholding Tax Forms page (archived 2026-10-28 as `US-DC-otr-withholding-forms.html`) defines the form family: **FR-900Q** (quarterly withholding return — e-filing mandatory for tax year 2023 and later), **FR-900A** (annual return, due January 31), **FR-900NP** (non-payroll withholding: 1099s and W-2G), **FR-900P** (payment voucher), **WT-1/WT-2** (wage and tax statement transmittal), and the **D-4** employee withholding certificate (the page notes the D-4 is currently under review).

## Who this applies to

- Any employer paying DC-source wages — including **household employers**: "Beginning January 1, 2019, if you have a household employee, you must obtain an FEIN and report such withholding using the FR-900Q" (OTR Withholding Tax Forms page, read 2026-10-28).
- Payers of DC-source 1099 income and gambling winnings file **FR-900NP** (same page).
- Employees claim withholding allowances on the **D-4**, filed with the employer "when starting new employment or when claimed allowances change" (same page). The **D-4A** is the certificate of non-residence.
- Non-resident employees working in DC: DC-withheld wages are recovered on Form D-40B (see `dc-income-tax`); the Home Rule Act bars DC from taxing a nonresident's income ([D.C. Code § 1-206.02](https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02)).

## Rates, bands and thresholds

| Item | Value | Source |
|---|---|---|
| FR-900Q filing | Quarterly; **e-file mandatory beginning TY2023** on MyTax.DC.gov | OTR Withholding Tax Forms page: "Beginning TY2023, FR-900Q must be filed electronically on MyTax.DC.gov" |
| FR-900A | Annual return for employers "whose threshold is less than $200 per year"; the 2026 FR-900A is due January 31, 2027; deposits for the calendar year are due by January 20, 2027 | OTR Withholding Tax Forms page |
| FR-900Q deposit/filing timing | "Filing: On or before the last day of the month following the quarter being reported"; deposits per the FR-900Q instructions | OTR Withholding Tax Forms page |
| FR-900P | Payment voucher for payments "other than electronically and less than $5,000" | OTR Withholding Tax Forms page |
| FR-900A deposits | "On or before January 20th of the year following the year being reported" | OTR Withholding Tax Forms page |
| Weekend/holiday rule | If a due date falls on a Saturday, Sunday or legal holiday, statements must be filed by the next business day | OTR Withholding Tax Forms page |

The withholding rate tables and the deposit-frequency tiering sit in the OTR withholding instructions ("deposit due dates" pages linked from the forms page); they were not extracted from an archived source this run — see the Not yet confirmed line.

## The taxable base

DC withholding applies to **DC-source wages** paid by an employer. The D-4 drives the allowance computation; the D-4A certifies non-residence so no DC tax is withheld from a commuter's wages. Withholding reconciles annually on the FR-900A against the WT-1/WT-2 transmittals (W-2 DC wage data, box 16).

## Deadlines and filing

- **FR-900Q:** filed and deposited quarterly — filing "on or before the last day of the month following the quarter being reported" (OTR Withholding Tax Forms page, read 2026-10-28).
- **FR-900A:** due **January 31** (the 2026 FR-900A is due January 31, 2027); year deposits due by **January 20, 2027** (same page).
- **WT-1/WT-2:** transmitted to OTR with the annual reconciliation, not just e-filed with the SSA.
- **D-4 refresh:** upon hire and when allowances change (OTR page).
- **Electronic filing** of FR-900Q through MyTax.DC.gov is mandatory beginning tax year 2023.

## Penalties and interest

- **Failure-to-file / failure-to-pay additions:** 5% a month up to 25% each, with the failure-to-file addition reduced by the failure-to-pay addition for the same months; neither applies with reasonable cause and no willful neglect ([D.C. Code § 47-4213](https://code.dccouncil.gov/us/dc/council/code/sections/47-4213), archived 2026-10-28 as `US-DC-47-4213.html`).
- **Interest** on unpaid tax runs at **10% a year, compounded daily** ([D.C. Code § 47-4201](https://code.dccouncil.gov/us/dc/council/code/sections/47-4201), archived 2026-10-28 as `US-DC-47-4201.html`).
- Common failure modes: (1) paper-filing FR-900Q after the 2023 e-file mandate; (2) household employers unaware of the post-2019 FR-900Q duty; (3) W-2s e-filed with SSA but FR-900A/WT-1 never sent to OTR; (4) 1099 gambling winnings withheld federally but FR-900NP missed.

## Cross-border points

- Remote workers performing services in DC create DC withholding duties for out-of-state employers (see `dc-cross-border`).
- DC has no income-tax reciprocity agreements with Maryland or Virginia in the archived sources; a nonresident's DC-withheld wages are recovered on **Form D-40B**, not a nonresident return — the Home Rule Act bars DC from taxing nonresident income ([D.C. Code § 1-206.02](https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02), archived 2026-10-28 as `US-DC-1-206.02.html`).

## Worked examples

Client facts below are hypothetical; the filing counts come from the confirmed quarterly/annual regime above.

**Quarterly FR-900Q filings plus one annual FR-900A per year:**

```oa-check
name: DC withholding filing volume
inputs:
  quarters: 4
  annual: 1
steps:
  - filings: quarters + annual
expected:
  filings: 5.00
```

**An annual filer's deposit timing:** an employer whose annual DC withholding is expected to stay under the $200 FR-900A threshold files the FR-900A by January 31 and deposits by January 20 of the following year (OTR Withholding Tax Forms page, read 2026-10-28).

## Ask the client first

- Is FR-900Q e-filed (mandatory since TY2023) and reconciled to W-2 DC wages box 16?
- Household employees: is the employer registered with an FEIN and filing FR-900Q?
- Are FR-900A + WT-1 transmitted to OTR, not just SSA e-file?
- Remote DC workers on out-of-state payrolls: withholding set up?
- Commuter employees: is the D-4A (non-residence certificate) on file so DC tax is not withheld in error?

## Sources

| Source | URL | Read on |
|---|---|---|
| OTR: Withholding Tax Forms (FR-900Q/A/NP/P, WT-1/WT-2, D-4/D-4A) | https://otr.cfo.dc.gov/page/withholding-tax-forms | 2026-10-28 |
| D.C. Code § 1-206.02 (Home Rule bar on taxing nonresident income) | https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02 | 2026-10-28 |
| D.C. Code § 47-4201 (interest, 10% compounded daily) | https://code.dccouncil.gov/us/dc/council/code/sections/47-4201 | 2026-10-28 |
| D.C. Code § 47-4213 (failure-to-file/pay additions) | https://code.dccouncil.gov/us/dc/council/code/sections/47-4213 | 2026-10-28 |
| OTR: DC Individual and Fiduciary Income Tax Rates (rate schedule mirrored by withholding tables) | https://otr.cfo.dc.gov/page/dc-individual-and-fiduciary-income-tax-rates | 2026-10-28 |

Not yet confirmed: the DC withholding rate tables and employer withholding-method formulas (the OTR withholding guide pages were not archived this run); the deposit-frequency tiering (lookback thresholds for monthly vs quarterly depositors); and the existence (or absence) of withholding reciprocity agreements with Maryland or Virginia — no reciprocity was found in the archived sources, but confirm against OTR guidance before advising.

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
