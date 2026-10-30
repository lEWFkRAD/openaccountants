---
name: va-cross-border-tax
description: >-
  Use when a taxpayer's situation crosses Virginia's borders: part-year
  residents filing Form 760PY, nonresidents filing Form 763 with the
  § 58.1-332 credit for tax paid to another state (Schedule OSC), the
  two residency tests of § 58.1-302 (domicile, or a Virginia abode for
  more than 183 days), the DC/KY/MD/PA/WV wage-reciprocity exemptions,
  and the Arizona/California/Oregon rule where the credit is claimed on
  the other state's nonresident return instead. Trigger on Virginia
  part-year, Form 760PY, Form 763, Schedule OSC, credit for tax paid to
  another state, Virginia 183-day rule, Virginia reciprocity.
  Source-cited draft; return-form section numbers need-sources.
jurisdiction: US-VA
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-27
version: 0.1
---

# Virginia cross-border: residency, part-year and nonresident filing

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

- Individuals domiciled in Virginia who move in or out during the year (part-year, Form 760PY).
- Nonresidents with Virginia-source income — wages, in-state business income, Virginia rentals (Form 763).
- Dual-residency cases: a Virginia domiciliary working in another state, or a non-domiciliary who keeps a Virginia home more than 183 days.
- Employers with cross-border staff: the DC/KY/MD/PA/WV reciprocity exemptions change the withholding answer.

**Residency rule (verified):** a resident is "every person domiciled in Virginia at any time during the taxable year and every other person who, for an aggregate of more than 183 days of the taxable year, maintained his place of abode within Virginia" — Va. Code § 58.1-302, carried from `va-income-tax` (which cites the law.lis page). Both tests are independent: the 183-day abode test can make a non-domiciliary a full Virginia resident.

## 2. Rates and key figures

| Item | Figure / rule | Source / status |
|---|---|---|
| Rate schedule (Virginia taxable income) | 2% to $3,000; $60 + 3% to $5,000; $120 + 5% to $17,000; $720 + **5.75%** above $17,000 | § 58.1-320 via `va-income-tax` (law.lis cited there) |
| Exemptions 2026 | $930 personal/dependent; +$800 age 65+/blind | § 58.1-322.03 via `va-income-tax` |
| Part-year mechanics | Form 760PY: compute tax as a resident on federal AGI, then prorate by the Virginia-source ratio | Form 760PY instructions — **not yet confirmed** (form PDF not fetched this run) |
| Nonresident mechanics | Form 763: tax on Virginia-source income; allocation rules in § 58.1-338.02 | §§ 58.1-338.01/-338.02 — **not yet confirmed** (section body not retrieved 2026-10-27) |
| Credit for tax paid to another state | Credit = lesser of (a) the other state's net tax on income also taxed by Virginia and (b) Virginia tax × (income taxed by other state ÷ Virginia taxable income); nonrefundable | § 58.1-332 — verified 2026-10-27 (law.lis text); Schedule OSC mechanics carried from `va-income-tax` |
| Reciprocity | Wages of DC/KY/MD/PA/WV residents exempt from VA withholding and tax if VA-4 exemption claimed; reciprocity covers wages only | `va-payroll` skill; withholding portal tax.virginia.gov/withholding-tax verified 200 2026-10-27 |
| AZ/CA/OR rule | Do not claim the Virginia credit for income taxed by AZ/CA/OR — claim it on that state's nonresident return | `va-income-tax` (Department instructions) |
| DC quirk | No Virginia credit for DC income tax; DC-taxed income is refunded through DC's process | `va-income-tax` |

## 3. Base and mechanics

- **Part-year (760PY):** start from the full resident computation, then the tax is prorated by the ratio of Virginia-source income (income received while a Virginia resident plus Virginia-source income while a nonresident) to total income.
- **Nonresident (763):** only Virginia-source income is in the base; the other state's tax on the same income is credited under § 58.1-332 with the ratio cap above.
- **The ratio cap is the whole game in dual-residency cases:** the credit can never exceed Virginia tax × (other-state-taxed income ÷ Virginia taxable income). Double-taxed income is common; double *tax* is capped away only by the credit.
- **Reciprocity is withholding relief for wages only** — self-employment, rental, partnership and S-corp income of a reciprocal-state resident still gets Virginia withholding/filing treatment (Form 763).

### 4. Deadlines and filings

- Individual returns follow the federal date (May 1 for calendar-year 2025 filings per Virginia's conforming extension practice — [VERIFY current-year date on tax.virginia.gov]).
- Part-year and nonresident returns use the same due dates; extension via Form 550L/VAT-101 (payment required to avoid the § 58.1-455 penalty stack).
- Employers: VA-4 reciprocity exemption certificates must be on file for the withholding exemption to apply — missing certificate means Virginia withholding was due (va-payroll audit flash point).

### 5. Penalties and interest

- Late payment: **6% per month capped at 30%**, plus interest at the IRC § 6621 underpayment rate **+ 2%** — § 58.1-455 and § 58.1-15, verified 2026-10-27.
- Wrong-residency filings are the classic trigger: a 760 filed by a part-year resident overpays (no penalty) but a 760PY filed by a statutory resident underpays and accrues the full stack from the original due date.
- Employer failure to withhold/pay over: § 58.1-468 liability — verified 2026-10-27.

### 6. Cross-border notes

- **Moving states mid-year:** Virginia taxes a domiciliary for the entire year unless the domicile actually changes; the 183-day abode test independently captures the move-in side. Keep day counts and lease/abode evidence.
- **Remote workers:** a W-2 employee living in MD/DC/PA/WV/KY working remotely for a Virginia employer is wage-exempt under reciprocity (with VA-4); a 1099 contractor is not.
- **Multi-state credits:** where more than one other state taxes the same income, Schedule OSC runs per state and the nonrefundable-credit total is capped at the Form 760 Line 18 tax.
- **No Virginia exit tax and no estate tax** — the cross-border exposure is purely income-tax residency mechanics.

### 7. Worked examples

**Example 1 — part-year mover with the § 58.1-332 ratio cap.** Taxpayer moves from Maryland to Virginia on 18 March 2026 (day 77). Total wages $100,000: $20,000 Maryland-source (pre-move), $80,000 Virginia-source. Virginia resident-schedule tax on $100,000 Virginia taxable income:

```oa-check
name: va resident schedule tax on 100000
inputs:
  ti: 100000
steps:
  - t1: 0.02 * 3000
  - t2: 0.03 * (5000 - 3000)
  - t3: 0.05 * (17000 - 5000)
  - t4: 0.0575 * (ti - 17000)
  - va_tax: t1 + t2 + t3 + t4
expected:
  t1: 60.00
  t2: 60.00
  t3: 600.00
  t4: 4772.50
  va_tax: 5492.50
```

Credit cap under § 58.1-332 (Virginia tax × other-state-taxed share) vs Maryland tax at 4.75% on the $20,000:

```oa-check
name: va osc credit cap vs maryland tax
inputs:
  va_tax: 5492.50
  other_income: 20000
  ti: 100000
  md_rate: 0.0475
steps:
  - cap: va_tax * other_income / ti
  - md_tax: other_income * md_rate
  - credit: min(cap, md_tax)
expected:
  cap: 1098.50
  md_tax: 950.00
  credit: 950.00
```

The credit is the lesser figure ($950), not the cap — the remaining $148.50 of cap headroom is unused.

**Example 2 — PA resident, temporary Virginia work, reciprocity.** A Pennsylvania resident works 60 days at a Virginia client site, earning $30,000 of Virginia wages, with a VA-4 exemption on file. Virginia tax on the wages: $0 (reciprocity). Pennsylvania tax at the flat 3.07%:

```oa-check
name: pa resident va wages reciprocity
inputs:
  wages: 30000
  pa_rate: 0.0307
steps:
  - va_tax: 0
  - pa_tax: wages * pa_rate
expected:
  va_tax: 0.00
  pa_tax: 921.00
```

Without the VA-4 on file, Virginia withheld and the taxpayer files 763 to get it back — and the employer sits in the § 58.1-468 exposure zone for the period.

### 8. Ask the client first

1. Where was domicile on 31 December, and is there evidence of the change (voter registration, driver's licence, homestead)?
2. How many days was a Virginia abode maintained — did the 183-day test trip even without domicile?
3. Which states taxed the same income — is any of them AZ, CA or OR (credit goes on their return, not Schedule OSC)?
4. Are VA-4 reciprocity certificates on file for MD/DC/PA/WV/KY staff — wages only, not 1099 income?
5. Part-year or full-year: what is the Virginia-source income ratio for the 760PY proration?

### 9. Sources

- Code of Virginia § 58.1-302 (resident definition — domicile + 183-day abode): carried from `va-income-tax` (law.lis § 58.1-302 cited there); § 58.1-303 (part-year residents) verified 200 with text 2026-10-27: <https://law.lis.virginia.gov/vacode/title58.1/chapter13/section58.1-303/>
- Code of Virginia § 58.1-332 (credit for tax paid to another state): <https://law.lis.virginia.gov/vacode/title58.1/chapter13/section58.1-332/> — 200 with text, 2026-10-27.
- Code of Virginia § 58.1-455 (6%/month penalty to 30%) and § 58.1-15 (interest = IRC § 6621 + 2%): 200 with text, 2026-10-27.
- Code of Virginia § 58.1-468 (employer failure to pay over withheld tax): 200, 2026-10-27.
- Virginia Tax withholding portal: <https://www.tax.virginia.gov/withholding-tax> — 200 with text, 2026-10-27.
- Existing `va-income-tax` and `va-payroll` skills (rate schedule, Schedule OSC mechanics, reciprocity detail, AZ/CA/OR and DC quirks — carried with their citations): read 2026-10-27.
- §§ 58.1-338.01 / 58.1-338.02 (763/760PY statutory basis) and Form 760PY/763 instruction PDFs: **not yet confirmed** — section bodies not retrieved 2026-10-27; verify before publication.

<!-- openaccountants-cta-block -->

---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at the OpenAccountants network.

- Use it in your AI: 
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min

## Who this applies to

Not yet confirmed against archived sources.

## Rates, bands and thresholds

Not yet confirmed against archived sources.

## The taxable base

Not yet confirmed against archived sources.

## Deadlines and filing

Not yet confirmed against archived sources.

## Penalties and interest

Not yet confirmed against archived sources.

## Cross-border points

Not yet confirmed against archived sources.

## Worked examples

Not yet confirmed against archived sources.

## Ask the client first

Not yet confirmed against archived sources.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.


| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | — | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
