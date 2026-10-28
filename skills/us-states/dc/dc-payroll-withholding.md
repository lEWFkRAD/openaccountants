---
name: dc-payroll-withholding
description: >
  Use this skill whenever asked about District of Columbia payroll
  withholding for tax year 2026 — the OTR withholding regime: FR-900Q
  quarterly withholding return (mandatory e-file since tax year 2023),
  FR-900A annual reconciliation, FR-900NP for 1099/W-2G, FR-900P,
  WT-1/WT-2 wage-and-tax transmittals, the D-4 employee withholding
  certificate, deposit due dates, and household-employer rules.
  Trigger on "DC withholding", "DC FR-900Q", "DC FR-900A", "DC D-4",
  "District of Columbia withholding deposit", "DC W-2 filing DC",
  "DC household employer withholding". Source-cited draft; OTR
  Withholding Tax Forms page read 2026-10-27.
jurisdiction: US-DC
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - dc-income-tax
---

# District of Columbia payroll withholding v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. DC withholding is administered by the **Office of Tax and Revenue (OTR)**. The OTR Withholding Tax Forms page (fetched 2026-10-27, 200, text read) defines the form family: **FR-900Q** (quarterly withholding return — e-filing mandatory for tax year 2023 and later), **FR-900A** (annual reconciliation, due January 31), **FR-900NP** (non-payroll withholding: 1099s and W-2G), **FR-900P**, **WT-1/WT-2** (wage and tax statement transmittal), and the **D-4** employee withholding certificate (page notes D-4 content under review). Household employers have been required to file FR-900Q since 2019 (page note, read 2026-10-27). **Source status:** form names, e-file mandate, and household-employer rule are read from the OTR page; the withholding rate tables, deposit-frequency thresholds, and penalty percentages are **needs-sources** (the page links a separate "deposit due dates" page not extracted this run).

## 2. Who applies

- Any employer paying DC-source wages — including **household employers** (FR-900Q obligation since 2019, OTR page note, read 2026-10-27).
- Payers of DC-source 1099 income and gambling winnings file **FR-900NP** (OTR page, read 2026-10-27).
- Employees claim withholding adjustments on the **D-4** (OTR page, read 2026-10-27).
- Non-resident employees working in DC are withheld on DC-source wages (reciprocity: DC has none with neighboring states — confirm, **needs-sources**).

## 3. Mechanics and rates

| Item | Value | Source |
|---|---|---|
| Withholding tables | graduated, mirrors DC income-tax brackets — **needs-sources** | OTR withholding page |
| Deposit frequency | by liability tier — see OTR deposit-due-dates page (**needs-sources**) | OTR page link, read 2026-10-27 |
| FR-900Q filing | quarterly; **e-file mandatory since TY2023** | OTR page, read 2026-10-27 |
| FR-900A + WT-1/WT-2 | annual, due **January 31** | OTR page, read 2026-10-27 |
| FR-900NP | 1099/W-2G withholding, annual | OTR page, read 2026-10-27 |

## 4. Deadlines

- **FR-900Q:** quarterly (last day of the month after each quarter — confirm on deposit page, **needs-sources**).
- **FR-900A / WT-1:** January 31 (OTR page, read 2026-10-27).
- **D-4 refresh:** upon hire and on life changes (practice point).

## 5. Penalties and interest

Failure-to-file/pay penalties under DC Code §47-1801.11 et seq. — percentages **needs-sources**. Common failure modes: (1) paper-filing FR-900Q after the 2023 e-file mandate; (2) household employers unaware of the post-2019 FR-900Q duty; (3) W-2s e-filed with SSA but FR-900A/WT-1 never sent to OTR; (4) 1099 gambling winnings withheld federally but FR-900NP missed.

## 6. Cross-border interactions

- Remote workers performing services in DC create DC withholding duties for out-of-state employers (see `dc-cross-border`).
- No withholding reciprocity with MD/VA (confirm — **needs-sources**); non-resident employees file DC D-40NR or rely on composite relief where available.

## 7. Worked examples

An employer with DC-source wages of $50,000/month withheld at an illustrative 5.1% effective rate (rate **needs-sources**):

```oa-check
name: DC monthly withholding illustrative
inputs:
  wages: 50000
  rate: 0.051
steps:
  - withheld: wages * rate
  - annual: withheld * 12
expected:
  withheld: 2550.00
  annual: 30600.00
```

Quarterly FR-900Q filings plus one annual FR-900A per year:

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

## 8. Ask the client

- Is FR-900Q e-filed (mandatory since TY2023) and reconciled to W-2 DC wages box 16?
- Household employees: is the employer registered and filing FR-900Q?
- Are FR-900A + WT-1 transmitted to OTR, not just SSA e-file?
- Remote DC workers on out-of-state payrolls: withholding set up?

## Sources

1. OTR Withholding Tax Forms: https://otr.cfo.dc.gov/page/withholding-tax-forms (200, text read 2026-10-27 — FR-900Q e-file mandate, FR-900A Jan 31, FR-900NP, FR-900P, WT-1/WT-2, D-4, household-employer rule)
2. OTR deposit due dates page: linked from the withholding page (not extracted — **needs-sources**)
3. DC Code §47-1801.11: https://code.dccouncil.gov/us/dc/council/code/titles/47/chapters/18/ (200; section text not extracted — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for DC withholding questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
