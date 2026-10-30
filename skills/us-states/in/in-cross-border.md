---
name: in-cross-border
description: >
  Use this skill whenever asked about Indiana cross-border personal tax
  situations for tax year 2026 -- part-year and nonresident filing on Form
  IT-40PNR, the flat state rate plus the county tax tied to the January 1
  residence rule, reciprocity with OH, KY, MI, PA, and WI, the PTET
  election for out-of-state owners of Indiana pass-throughs, and county
  tax exposure for remote workers. Trigger on "Indiana nonresident",
  "IT-40PNR", "Indiana part-year", "Indiana county tax", "Indiana
  reciprocity", "Indiana commuter", "Indiana remote worker". Source-cited
  draft; DOR pages verified 2026-10-27, statute text pending confirmation.
jurisdiction: US-IN
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - in-income-tax
---

# Indiana cross-border v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 2026-10-27. Indiana taxes residents on worldwide income and nonresidents on Indiana-source income, at a **flat state rate plus a county income tax** (all 92 counties levy one; the county rate is locked to the taxpayer's **January 1 residence** -- per `in-payroll`, tier 2, 2026-07-13). **Source status:** DOR form pages verified 2026-10-27 (IT-40 series, IT-40PNR referenced on the DOR "Choosing the Proper Income Tax Form" page); iga.in.gov is a SPA, so the residency definition, IT-40PNR line mechanics, and the 2026 flat rate are listed under Not yet confirmed below.

### Who applies

- **Indiana residents:** worldwide income, IT-40, county tax at January 1 residence rate.
- **Part-year residents and nonresidents with Indiana income:** **Form IT-40PNR** (DOR page read 2026-10-27: partners report on "IT-40 or IT-40PNR").
- **Commuters from OH, KY, MI, PA, WI:** Indiana has **reciprocal income-tax agreements** with these five states (per `in-payroll`, 2026-07-13) -- exempt from Indiana wage withholding on wages; file the applicable exemption form -- current WH-43-style form IDs are not yet confirmed.
- **Out-of-state owners of Indiana pass-throughs:** taxed on Indiana-source distributive income unless the entity elects **PTET** (IN-PTET; DOR PTET page read 2026-10-27 -- SEA 2, 2023, entity-level tax, refundable owner credit).

## Rates, bands and thresholds

- **County tax follows the person, not the workday:** the January 1 residence rule locks the county rate for the full year (per `in-payroll`) -- cross-border movers must know which county (or none, for nonresidents: nonresident county tax applies only to certain Indiana-sourced situations -- not yet confirmed).
- **Reciprocity covers wages only** -- rental, business, and other Indiana-source income of neighboring-state residents remains taxable in Indiana.
- **PTET route:** electing entities pay at the flat rate; nonresident owners get a refundable credit and avoid individual Indiana filings (DOR PTET page read 2026-10-27).
- **Remote workers:** physical work in Indiana creates Indiana-source wages regardless of employer location (withholding duty per `in-payroll`).

## The taxable base

The taxable base follows the mechanics described under Rates, bands and thresholds above.

## Deadlines and filing

- IT-40/IT-40PNR: April 15 (calendar year; federal extension generally honored -- not yet confirmed).
- Estimated tax: quarterly vouchers (84-ES series) when liability exceeds the threshold -- the threshold amount is not yet confirmed.
- PTET election rides the entity return (DOR PTET page read 2026-10-27).

## Penalties and interest

- IC 6-8.1 penalties/interest -- percentages not yet confirmed.
- Reciprocity abuse: unfiled Indiana returns on non-wage Indiana income still draw late-filing penalties -- amounts not yet confirmed.

## Cross-border points

- Moving to/from Indiana mid-year: part-year IT-40PNR; county rate locked at January 1 residence.
- Kentucky/Ohio border workers: reciprocity exempts wages but Kentucky/Ohio tax the full amount with a credit -- check for double-taxation gaps on non-wage income.
- Foreign owners of Indiana flow-throughs: PTET substitutes entity-level tax; otherwise IT-40PNR + withholding.
- Military: Indiana honors resident-state taxation rules for service members stationed elsewhere -- not yet confirmed.

## Worked examples

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

(Wages exempt under reciprocity; rental stays Indiana-source. Rate hypothetical -- confirm 2026 rate.)

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

## Ask the client first

- Neighbor-state commuter: reciprocity form on file -- and is non-wage Indiana income being missed?
- Mid-year mover: January 1 county lock applied to the county tax?
- Out-of-state partners/shareholders: PTET election modeled against IT-40PNR costs?
- Remote workers physically in Indiana: withholding and county tax set up?

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

## Sources

| Source | URL | Read on |
|---|---|---|
| Indiana DOR choosing the proper income tax form (IT-40/IT-40PNR routing) | https://www.in.gov/dor/i-am-a/business-corp/choosing-the-proper-income-tax-form/ | 2026-10-29 |
| Indiana DOR PTET page | https://www.in.gov/dor/tax-forms/other-forms/ptet/ | 2026-10-29 |
| Indiana DOR withholding page (registration triggers incl. nonresident shareholders/partners) | https://www.in.gov/dor/i-am-a/business-corp/withholding/ | 2026-10-28 |
| Indiana Code IC 6-3 (residency, source; iga.in.gov SPA -- no server-side text captured) | https://iga.in.gov/laws/2025/ic/titles/6 | 2026-10-28 |

Internal cross-references: `in-income-tax.md`, `in-payroll.md` (tier 2) -- rates and reciprocity list originate there.

Not yet confirmed: the 2026 flat individual rate (2.95% for 2025 per `in-income-tax`, 3.15% per `in-payroll` -- reconcile); the statutory residency definition and IT-40PNR line mechanics; current reciprocity exemption form IDs (WH-43-style); nonresident county-tax situations; the estimated-tax threshold; IC 6-8.1 penalty and interest percentages; federal-extension honoring; military stationed-elsewhere rules.

<!-- openaccountants-cta-block -->

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