---
name: mo-cross-border
description: >
  Use this skill whenever asked about Missouri cross-border personal tax for
  tax year 2026 — part-year Form MO-1040P and nonresident Form MO-NRI, the
  Form MO-CR credit for taxes paid to other states, nonresident withholding
  via the MO W-4 allocation section, Military Spouses Residency Relief Act
  handling, and the Kansas City / St. Louis 1% city earnings taxes that hit
  residents wherever earned and nonresidents who work inside the city limits
  (KC reauthorization vote April 2026). Trigger on "Missouri nonresident",
  "MO-NRI", "MO-1040P", "Missouri part-year", "MO-CR credit", "Kansas City
  earnings tax", "St. Louis earnings tax", "Missouri commuter".
  Source-cited draft; corroborated by the existing tier-2 mo-income-tax and
  mo-payroll skills (MO-1040PNR instructions PDF 403 on 2026-10-27).
jurisdiction: US-MO
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - mo-income-tax
  - mo-payroll
---

# Missouri cross-border (nonresidents, part-year, city earnings taxes) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

How Missouri taxes people who cross its borders: individual part-year (Form **MO-1040P**) and nonresident (Form **MO-NRI**) filing, the **MO-CR** credit for taxes paid to other states, nonresident withholding, military-spouse relief, and the two **city earnings taxes** (Kansas City, St. Louis) that are Missouri's most common cross-border trap. Corporate cross-border sits in `mo-corporate-income-tax` / `mo-transfer-pricing`.

**Source status:** figures corroborated by the existing tier-2 `mo-income-tax` and `mo-payroll` skills (verified against DOR Form 4282, KC Revenue Division and St. Louis Collector guidance in 2025). The **MO-1040PNR instructions PDF returned 403** from the drafting environment on 2026-10-27 — procedural specifics (thresholds, allocation worksheets) are flagged **not yet confirmed**. Missouri has **no reciprocal agreements** with any state (per `mo-payroll` scope analysis) — unlike Maryland, commuters pay Missouri tax on Missouri-worked wages.


### Who this applies to


- **Nonresidents working in Missouri:** MO-NRI on Missouri-source income; withholding on the Missouri-work share via the MO W-4 nonresident allocation section (employee estimates the Missouri %; employer keeps timekeeping/project support). (per `mo-payroll` §5.4.)
- **Part-year residents (moved in/out):** MO-1040P. (per `mo-income-tax` form table.)
- **Missouri residents working in another state:** full MO resident return + **MO-CR** credit for taxes paid to the other state (non-refundable; requires the other state's return). (per `mo-income-tax` MO-T2-04.)
- **Military spouses:** MSRRA reduced-withholding claim on the MO W-4 when the spouse's domicile is elsewhere. (per `mo-payroll`.)
- **Kansas City:** 1% earnings tax on **KC residents wherever earned** and on **nonresidents for work inside KC corporate limits** (KC Code ch. 68; §92.110 RSMo). Employers with anyone working inside KC limits must withhold 1% and remit to the city, regardless of where the employer sits. (per `mo-payroll` §7.)
- **St. Louis City:** same 1% structure on city residents and work inside **city** limits — St. Louis **County** has no earnings tax. (per `mo-payroll`.)

## Rates, bands and thresholds

| Item | Amount / rule | Source |
|---|---|---|
| State PIT top rate | 4.95% (2025; phasing down via revenue triggers) | `mo-income-tax` skill |
| Nonresident base | Missouri-source income allocated via MO-NRI worksheets (allocation mechanics **not yet confirmed** — PNR instructions 403) | `mo-income-tax` form table |
| MO-CR credit | Non-refundable credit for taxes paid to other states; needs the other state's return | `mo-income-tax` MO-T2-04 |
| KC earnings tax | **1.0%** — residents on all earnings, nonresidents on KC-worked earnings; separate city return | KC ch. 68; §92.110 RSMo via `mo-payroll` |
| KC reauthorization | voter vote **April 2026** (reauthorized 2021; five-year cycle) | §92.115 RSMo via `mo-payroll` |
| STL City earnings tax | **1.0%** — city residents and city-limits work; STL County none | STL ch. 5.22 via `mo-payroll` |
| Reciprocity | **none** — Missouri has no reciprocal agreements | `mo-payroll` scope analysis |

## The taxable base
Sourcing and base rules (workday sourcing, city-limit situs) are covered under "Cross-border points" below; no separate base section.
## Deadlines and filing

- MO-1040P / MO-NRI follow the individual calendar: **15 April** for calendar-year filers.
- KC earnings tax: quarterly estimated payments for self-employed; employer withholding per KC Revenue Division schedule; annual return 15 April (KC schedules **not yet confirmed** re-verification).
- STL City: annual return 15 April; nonfilers who owe are the classic audit population.
- MO-CR: claim on the resident return; amended within the ordinary assessment window.

## Penalties and interest

- State regime: 5%/month late-filing (cap 25%), 5% late-payment, 7% simple interest from 1 January 2026 (§32.065 RSMo, per `mo-corporate-income-tax` fetch — same statute across DOR taxes).
- KC/STL: city-level penalties and interest on unpaid earnings tax; percentages **not yet confirmed** (city collector pages not fetched this run).
- Employers failing to withhold KC 1% for city-worked employees carry the unwithheld tax plus city penalties.

## Cross-border points

- **IL/MO commuter (no reciprocity):** the Illinois worker who performs services in Missouri owes Missouri on the Missouri-work share (MO-NRI) and Illinois credits it (IL nonresident + credit); the reverse Missouri-resident-in-IL pattern uses MO-CR.
- **Remote work:** wages are sourced to where services are performed — a Kansas City employer letting staff work from home outside KC limits moves those wages out of the KC 1% base (document locations).
- **KC vs STL distinction matters:** STL County is not STL City; the 2025 state preemption of local sick-leave laws did not repeal the earnings taxes (per `mo-payroll`).
- **Self-employed in KC/STL:** 1% on net self-employment earnings tied to the city; separate filing required (per `mo-income-tax` MO-T2-05).

## Worked examples

**Example 1 — Illinois resident working 3 of 5 days in St. Louis County (not city).** Wages $150,000; Missouri-source share by workdays; no KC/STL city work.

```oa-check
name: MO-NRI rough exposure
inputs:
  wages: 150000
  mo_days: 3
  total_days: 5
  top: 0.0495
steps:
  - mo_source: wages * mo_days / total_days
  - rough_tax: mo_source * top
expected:
  mo_source: 90000.00
  rough_tax: 4455.00
```

Upper bound at the 4.95% top rate (graduated brackets compute lower); **no city earnings tax** because the work is in the county. Illinois taxes the full $150,000 and credits the Missouri tax within IL's limits.

**Example 2 — KC-resident commuter to STL City.** KC resident earns $100,000 working inside St. Louis City limits.

```oa-check
name: KC and STL double city tax
inputs:
  wages: 100000
  kc: 0.01
  stl: 0.01
steps:
  - kc_tax: wages * kc
  - stl_tax: wages * stl
  - total_city: kc_tax + stl_tax
expected:
  kc_tax: 1000.00
  stl_tax: 1000.00
  total_city: 2000.00
```

Both cities assert a claim — KC on residency, STL on situs of work. Whether one city grants a credit for the other is a city-ordinance question: **not yet confirmed**; model the gross $2,000 until the collectors' guidance is read.

## Ask the client first

1. Which days are physically worked where — is there a workday log for the commuter?
2. KC resident, STL City work (or reverse) — is the double city-tax exposure modeled, and has anyone checked city credits?
3. Is the employer withholding the KC 1% for anyone working inside KC limits, even remotely?
4. Missouri resident working in IL/IA/KS/AR — is MO-CR being claimed with the other state's return attached?
5. Military family — is an MSRRA claim appropriate on the MO W-4?

## Sources

1. Existing tier-2 skills: `mo-income-tax` (MO-1040P/MO-NRI/MO-CR table, city earnings tax table) and `mo-payroll` (KC ch. 68 / §92.110, STL ch. 5.22, §92.115 reauthorization, nonresident withholding, MSRRA) — repo `skills/us-states/mo/`.
2. Missouri DOR, MO-1040PNR instructions (2025): <https://dor.mo.gov/forms/MO-1040PNR%20Instructions_2025.pdf> — **403 on 2026-10-27, not yet confirmed** for allocation worksheets and thresholds.
3. §32.065 RSMo interest (7% from 1 Jan 2026) via the MO-1120 2025 instructions fetch, 200, read 2026-10-27.

Not yet confirmed: the items above flagged as not sourced — figures tied to them stay unconfirmed until the source is archived.

## Talk to a verified accountant

**Talk to a verified accountant** — for Missouri commuter and city earnings-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

<!-- openaccountants-cta-block -->
