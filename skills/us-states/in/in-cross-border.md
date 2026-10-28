---
name: in-cross-border
description: >
  Use this skill whenever asked about Indiana cross-border personal tax
  situations for tax year 2026 — part-year and nonresident filing on Form
  IT-40PNR, the flat state rate plus the county tax tied to the January 1
  residence rule, reciprocity with OH, KY, MI, PA, and WI, the PTET
  election for out-of-state owners of Indiana pass-throughs, and county
  tax exposure for remote workers. Trigger on "Indiana nonresident",
  "IT-40PNR", "Indiana part-year", "Indiana county tax", "Indiana
  reciprocity", "Indiana commuter", "Indiana remote worker". Source-cited
  draft; DOR pages verified 2026-10-27, statute text needs-sources.
jurisdiction: US-IN
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - in-income-tax
---

# Indiana cross-border v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-27. Indiana taxes residents on worldwide income and nonresidents on Indiana-source income, at a **flat state rate plus a county income tax** (all 92 counties levy one; the county rate is locked to the taxpayer's **January 1 residence** — per `in-payroll`, tier 2, 2026-07-13). **Source status:** DOR form pages verified 2026-10-27 (IT-40 series, IT-40PNR referenced on the DOR "Choosing the Proper Income Tax Form" page); **iga.in.gov SPA — residency definition and IT-40PNR line mechanics are needs-sources**; the current-year flat rate (2.95% for 2025 per `in-income-tax`; statutory phase-down to 2.9% by 2027 per `in-payroll`) must be confirmed for 2026 — **needs-sources**.

## 2. Who applies

- **Indiana residents:** worldwide income, IT-40, county tax at January 1 residence rate.
- **Part-year residents and nonresidents with Indiana income:** **Form IT-40PNR** (DOR page read 2026-10-27: partners report on "IT-40 or IT-40PNR").
- **Commuters from OH, KY, MI, PA, WI:** Indiana has **reciprocal income-tax agreements** with these five states (per `in-payroll`, 2026-07-13) — exempt from Indiana wage withholding on wages; file the applicable exemption form. **needs-sources** for current WH-43-style form IDs.
- **Out-of-state owners of Indiana pass-throughs:** taxed on Indiana-source distributive income unless the entity elects **PTET** (IN-PTET; DOR PTET page read 2026-10-27 — SEA 2, 2023, entity-level tax, refundable owner credit).

## 3. Mechanics

- **County tax follows the person, not the workday:** the January 1 residence rule locks the county rate for the full year (per `in-payroll`) — cross-border movers must know which county (or none, for nonresidents: nonresident county tax applies only to certain Indiana-sourced situations — **needs-sources**).
- **Reciprocity covers wages only** — rental, business, and other Indiana-source income of neighboring-state residents remains taxable in Indiana.
- **PTET route:** electing entities pay at the flat rate; nonresident owners get a refundable credit and avoid individual Indiana filings (DOR PTET page read 2026-10-27).
- **Remote workers:** physical work in Indiana creates Indiana-source wages regardless of employer location (withholding duty per `in-payroll`).

## 4. Deadlines

- IT-40/IT-40PNR: April 15 (calendar year; federal extension generally honored — **needs-sources**).
- Estimated tax: quarterly vouchers (84-ES series) when liability exceeds the threshold — amount **needs-sources**.
- PTET election rides the entity return (DOR PTET page read 2026-10-27).

## 5. Penalties and interest

- IC 6-8.1 penalties/interest — percentages **needs-sources**.
- Reciprocity abuse: unfiled Indiana returns on non-wage Indiana income still draw late-filing penalties — **needs-sources**.

## 6. Cross-border interactions

- Moving to/from Indiana mid-year: part-year IT-40PNR; county rate locked at January 1 residence.
- Kentucky/Ohio border workers: reciprocity exempts wages but Kentucky/Ohio tax the full amount with a credit — check for double-taxation gaps on non-wage income.
- Foreign owners of Indiana flow-throughs: PTET substitutes entity-level tax; otherwise IT-40PNR + withholding.
- Military: Indiana honors resident-state taxation rules for service members stationed elsewhere — **needs-sources**.

## 7. Worked examples

Ohio resident earns $70,000 wages working remotely from Ohio for an Indiana company, plus $12,000 rental income from an Indiana property:

```oa-check
name: IN reciprocity scope
inputs:
  wages: 70000
  rental: 12000
  rate: 0.0295
steps:
  - indiana_taxable: rental
  - tax: indiana_taxable * rate
expected:
  indiana_taxable: 12000.00
  tax: 354.00
```

(Wages exempt under reciprocity; rental stays Indiana-source. Rate illustrative — confirm 2026 rate.)

Illinois resident, part-year Indiana move on July 1, Indiana wages $48,000 earned after the move:

```oa-check
name: IN part-year sourced wages
inputs:
  wages: 48000
  rate: 0.0295
steps:
  - tax: wages * rate
expected:
  tax: 1416.00
```

## 8. Ask the client

- Neighbor-state commuter: reciprocity form on file — and is non-wage Indiana income being missed?
- Mid-year mover: January 1 county lock applied to the county tax?
- Out-of-state partners/shareholders: PTET election modeled against IT-40PNR costs?
- Remote workers physically in Indiana: withholding and county tax set up?

## Sources

1. Indiana DOR choosing the proper income tax form (IT-40/IT-40PNR routing): https://www.in.gov/dor/i-am-a/business-corp/choosing-the-proper-income-tax-form/ (200, read 2026-10-27)
2. Indiana DOR PTET page: https://www.in.gov/dor/tax-forms/other-forms/ptet/ (200, read 2026-10-27)
3. Indiana DOR withholding page (registration triggers incl. nonresident shareholders/partners): https://www.in.gov/dor/i-am-a/business-corp/withholding/ (200, read 2026-10-27)
4. Internal cross-references: `in-income-tax.md`, `in-payroll.md` (tier 2) — rates and reciprocity list originate there.
5. Indiana Code IC 6-3 (residency, source): https://iga.in.gov/laws/2025/ic/titles/6 (SPA — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Indiana cross-border personal questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
