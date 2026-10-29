---
name: nc-cross-border-tax
description: >-
  Use when a nonresident works or invests in North Carolina, an NC resident
  works in another state, or an out-of-state business has NC activity, and
  the 2026 answer is needed: D-400/D-400NR filing tests under N.C.G.S.
  § 105-153.8, NC sourcing of income under § 105-153.2, the standard
  deduction threshold (§ 105-153.5, $12,750 single 2025), the flat 3.99%
  rate for post-2025 years (§ 105-153.7), nonresident withholding, and
  P.L. 86-272 limits. Trigger on North Carolina nonresident return, D-400NR,
  105-153.2, 105-153.8, NC source income, part-year NC. Source-cited draft;
  statute text verified 2026-10-25.
jurisdiction: US-NC
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---

# North Carolina cross-border tax (nonresidents, sourcing, filing tests)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

- Nonresidents and part-year residents with NC-source income (Form D-400NR).
- NC residents working in reciprocity or non-reciprocity neighboring states (SC, TN, VA, GA — none have income-tax reciprocity with NC; see § 6).
- Out-of-state businesses with NC nexus (corporate side: `nc-corporate-tax`, `nc-transfer-pricing`).
- Nonresident owners of NC real estate and nonresident partners/members of NC pass-throughs.

## Rates, bands and thresholds

## Core rules and rates

- **Filing test (§ 105-153.8, text verified 2026-10-25).** A nonresident must file if NC-source gross income, **combined with total worldwide gross income**, exceeds the standard deduction. The test uses total gross income, not just NC income — a trap that catches low-NC-income filers.
- **Standard deduction (§ 105-153.5, text verified 2026-10-25):** $12,750 single / $25,500 joint for 2025; NC indexes annually — **2026 figures not yet confirmed** (NCDOR publishes in the D-400 instructions).
- **Rate (§ 105-153.7, text verified 2026-10-25):** flat 3.99% for taxable years beginning after 2025, with a statutory trigger that can reduce it to as low as 2.49% when revenue targets and rate-cuts in other states align — check the current-year NCDOR rate before quoting anything else.
- **Sourcing (§ 105-153.2, text verified 2026-10-25):** compensation is sourced to where services are performed; business income follows the apportionment concepts; NC real-estate gains are NC-source; NC-sourced dividends/interest follow the payer/residence conventions in the section.
- **Withholding:** NC employers withhold on all wages including nonresidents (§ 105-163.1, text verified 2026-10-25). Nonresident withholding on NC real-estate dispositions: the commonly cited 2% rule (G.S. 105-163.14) **returned 404 on ncleg.gov 2026-10-25 — not yet confirmed** for the current successor provision; verify against the current D-400NR/real-estate forms before advising.
- **No reciprocity.** NC has no income-tax reciprocity agreement with any state — unlike the ND/MN/MI/MT cluster. A nonresident commuter pays the other state's tax AND files NC on NC-source work.

## The taxable base

## Base

D-400NR computes NC taxable income by starting with federal AGI, then removing non-NC income and applying the NC standard or itemized deduction. The flat rate applies to that NC taxable income. Credits for taxes paid to other states exist for NC residents working elsewhere (§ 105-153.6(c) mechanics — verify current form before use).

## Deadlines and filing

## Deadlines

- D-400/D-400NR: Apr 15 (automatic 6-month extension to Oct 15 by timely application — NCDOR individual hub, 200, 2026-10-25).
- Estimated payments (D-400ES, § 105-163.15 text verified 2026-10-25): Apr 15, Jun 15, Sep 15, Jan 15.
- Safe harbor: 90% of current-year NC tax or 100% of prior-year (110% for high-income) — installment mechanics per § 105-163.15.

## Penalties and interest

- Late filing/failure to pay: Chapter 105 penalties (5% per month up to 5%) plus interest; the 2026 published underpayment rate is on the NCDOR rate page — **not yet confirmed** for the current percentage.
- Underpaid installments: interest from each installment due date (§ 105-163.15(c)).
- Nonresident real-estate withholding errors: agent/broker liability under the current successor to 105-163.14 — **not yet confirmed** (see § 2).

## Cross-border points

## Cross-border patterns

- **Commuters:** VA/SC/TN/GA workers who perform services in NC owe NC on those wages; the home state generally credits the NC tax (most home states grant a credit for tax paid to NC on work performed there).
- **Remote workers:** an employee working from NC for an out-of-state employer creates NC-source wages and NC withholding; the employer's nexus analysis follows P.L. 86-272 only for protected solicitation — services are never protected.
- **Pass-throughs:** NC-source income allocated to nonresident partners; NC requires the entity to report and, in some structures, withhold/issue K-1s with NC allocations — composite-return availability: **not yet confirmed** (not located on ncleg.gov 2026-10-25).
- **P.L. 86-272:** protects solicitation of orders for tangible personal property only; NC taxes net income of nonresident corporations beyond that protection via the single sales factor.

## Worked examples

**Example 1 — does the nonresident have to file?** Nonresident, single. NC-source wages $30,000 (worked 60 days in NC); total worldwide gross income $120,000. 2025 standard deduction $12,750.

```oa-check
name: nc nonresident filing test
inputs:
  nc_gross: 30000
  total_gross: 120000
  std: 12750
steps:
  - exceeds_std: total_gross - std
  - must_file: min(exceeds_std, 1)
expected:
  exceeds_std: 107250
  must_file: 1
```

The worldwide-income test is met, so a D-400NR is required even though only $30,000 is NC-source.

**Example 2 — NC tax on NC taxable income.** Same filer; after removing non-NC income and applying the NC standard deduction, NC taxable income is $80,000 (hypothetical client facts). Rate 3.99%.

```oa-check
name: nc nonresident tax
inputs:
  nc_taxable: 80000
  rate: 0.0399
steps:
  - tax: nc_taxable * rate
expected:
  tax: 3192.00
```

## Ask the client first

1. Where were services physically performed, day by day (work-from-home days count as NC)?
2. Total worldwide gross income — not just NC income — for the filing test.
3. Any NC real-estate sale (withholding successor rule) or NC K-1 income?
4. Does the home state grant a credit for NC tax, and at what rate?
5. Part-year movers: NC residency rules (183-day/domicile concepts) — confirm the residency split before sourcing.

## Sources

| Source | URL | Read on |
|---|---|---|
| N.C.G.S. § 105-153.2 (purpose/sourcing of individual tax): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.2.html | 2026-10-25 |
| N.C.G.S. § 105-153.5 (standard deduction): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html | 2026-10-25 |
| N.C.G.S. § 105-153.7 (rate; 3.99% post-2025 with trigger to 2.49%): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html | 2026-10-25 |
| N.C.G.S. § 105-153.8 (who must file): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.8.html | 2026-10-25 |
| N.C.G.S. § 105-163.1 (withholding agent): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.1.html | 2026-10-25 |
| N.C.G.S. § 105-163.15 (estimated installments): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html | 2026-10-25 |
| NCDOR individual hub: | https://www.ncdor.gov | 2026-10-25 |

Not yet confirmed: 2026 indexed standard deduction; nonresident real-estate withholding successor (105-163.14 repealed 1985 per chapter index, successor not located 2026-10-25); composite-return availability; 2026 published underpayment interest rate

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
