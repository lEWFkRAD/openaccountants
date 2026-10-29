---
name: ia-payroll-withholding
description: >
  Use this skill whenever asked about Iowa income-tax withholding for tax
  year 2026 — Iowa Code §422.16: the withholding-agent duty on Iowa residents
  and nonresidents working in Iowa, quarterly/monthly/semimonthly remittance
  tiers, the $500 willful-failure civil penalty, and the PTE entity-level
  election under §422.16C. Trigger on "Iowa withholding", "Iowa W-4",
  "Iowa withholding tiers", "422.16", "Iowa PTE election". Corrected
  2026-10-28 against archived Iowa Code 2026 statute text.
jurisdiction: US-IA
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - ia-income-tax
---

# Iowa payroll withholding, tax year 2026

> **Source-cited draft.** Built from Iowa Code §§422.16, 422.16C and 422.19 (Iowa Legislature, Iowa Code 2026), read on 2026-10-28. No accountant has reviewed it. Do not file, pay, amend, or take a tax position from it without review by a qualified Iowa professional.

Tax year: calendar-year withholding. Authority: Iowa Department of Revenue. Currency: US dollars. Covers employer withholding of Iowa individual income tax at source.

See also: `ia-income-tax`, `ia-cross-border`, `ia-social-contributions`.

## Who this applies to

- "Withholding agent" is defined broadly (§422.16(1)) and covers every agent paying wages to an Iowa resident, or to a nonresident working in Iowa (§422.16(2)(a)); the definition includes governments, municipalities, school districts, and entities paying taxable Iowa income to nonresidents.
- Nonresident income not otherwise withheld: "a withholding agent shall withhold from such income at the same rate" unless the department has issued a §422.17 certificate (§422.16(2)(b)).
- Film/TV production: "Nonresidents engaged in any facet of feature film, television, or educational production ... in the state are not subject to Iowa withholding if the employer has applied to the department for exemption ... and the department has determined" the nonresident would be entitled to a credit (§422.16(11)(b)).
- "The claiming of an amount of withholding allowance in excess of entitlement is a serious misdemeanor" (§422.16(2)(a)).

## Rates, bands and thresholds

| Tier | Condition (§422.16(4)) | Deposit due |
|---|---|---|
| Quarterly | withholds less than $6,000 annually and no more than $500 in any one month | with the quarterly return |
| Monthly | more than $500 in any one month and not more than $5,000 in a semimonthly period | on or before the 15th day of the month following withholding; third-month deposit due with the quarterly return |
| Semimonthly | more than $5,000 in a semimonthly period | 1st–15th period due on the 25th of the same month; 16th–end due on the 10th of the following month |

- §422.16(4)(1): remit quarterly if the agent "withholds less than six thousand dollars annually and no more than five hundred dollars in any one month. Payment shall be due on the same day as the quarterly return."
- §422.16(4)(2): monthly remitters "withhold more than five hundred dollars in any one month and not more than five thousand dollars in a semimonthly period", paying "on or before the fifteenth day of the month following the month of withholding, except that a deposit for the third month in a calendar quarter shall be due on the same day as the quarterly return."
- §422.16(4)(3): semimonthly remitters "withhold more than five thousand dollars in a semimonthly period"; "The first semimonthly deposit for the period from the first of the month through the fifteenth of the month is due on the twenty-fifth day of the month in which the withholding occurs."

## The taxable base

- Iowa withholds on wages and other taxable Iowa income at the individual rate (§422.16(2)); the amount withheld "approximates" annual liability using department tables and federal withholding-allowance elections (§422.16(2)(a)).
- **PTE election (§422.16C):** partnerships/S corporations may elect annual entity-level tax "equal to the rate under section 422.5" (3.8%); the election is irrevocable for the year and replaces the §422.16B composite return; partners/shareholders receive a credit (§422.16C(5)).

## Deadlines and filing

- Quarterly return: "A withholding agent required to deduct and withhold tax under subsection 2 shall file a return on or before the last day of the month following the quarterly period" (§422.16(4)) — Jan 31, Apr 30, Jul 31, Oct 31 for calendar quarters.
- Deposits per the tier table above.
- Estimated tax payments on behalf of certain nonresidents: agricultural-commodity election payments are due "on or before the last day of the first month after the end of the tax years of the nonresident" (§422.16(2)).

## Penalties and interest

- **Personal liability:** "Every withholding agent who fails to withhold or pay to the department any sums required by this chapter to be withheld and paid, shall be personally, individually, and corporately liable to the state of Iowa" (§422.16(5)).
- **$500 civil penalty per occurrence:** "a withholding agent required to furnish or file an income statement required by this chapter is subject to a civil penalty of five hundred dollars for each occurrence of" willful failure to furnish an income statement, willfully furnishing a false or fraudulent statement, and related willful failures (§422.16(11)(a)).
- Overwithheld balances: "any balance of one dollar or more shall be refunded to the employee, nonresident, or other person with interest" (§422.16(10)(a)); under $1 only on written application within twelve months (§422.16(10)(b)).
- The current ch. 421 interest rate on unpaid withholding — see Not yet confirmed.

## Cross-border points

- Nonresidents working in Iowa (commuters, seasonal agricultural workers): withholding applies under §422.16(2)(b) unless a §422.17 no-withholding certificate is in force (§422.17).
- Reciprocal states: no archived statute text confirms a neighbour-reciprocity exemption — see Not yet confirmed.
- Foreign owners of Iowa PTEs: the §422.16C election substitutes entity-level tax for composite filings (§422.16C(3)(b)).

## Worked examples

Hypothetical agent withholds $450 in January, $620 in February, $480 in March:

```oa-check
name: IA withholding tier test
inputs:
  jan: 450
  feb: 620
  mar: 480
  monthly_trigger: 500
steps:
  - quarter_total: jan + feb + mar
  - feb_excess: feb - monthly_trigger
expected:
  quarter_total: 1550.00
  feb_excess: 120.00
```

(February exceeds the $500 single-month trigger, so the monthly schedule applies; the quarterly return is still due Apr 30. The $500 and $6,000 thresholds are confirmed §422.16(4) figures.)

Semimonthly test: $5,400 withheld 1–15 March:

```oa-check
name: IA semimonthly deposit test
inputs:
  semimonthly: 5400
  trigger: 5000
steps:
  - excess: semimonthly - trigger
expected:
  excess: 400.00
```

(The excess over the $5,000 semimonthly trigger puts the agent on the semimonthly schedule; the 1–15 March deposit is due March 25 per §422.16(4)(3).)

## Ask the client first

- Which remittance tier applies month-by-month — the tiers flip on single-month spikes (§422.16(4))?
- Are quarterly returns filed even when deposits were current?
- Any nonresident workers (commuters, seasonal, film) — §422.17 certificates or the §422.16C PTE election in place?
- Willful income-statement failures carry a $500 civil penalty each (§422.16(11)(a)) — is W-2/income-statement issuance under control?

## Sources

| Source | URL | Read on |
|---|---|---|
| Iowa Code §422.16 (withholding; remittance tiers; penalties; estimated tax) | https://www.legis.iowa.gov/docs/code/422.16.pdf | 2026-10-28 |
| Iowa Code §422.16C (PTE election — entity-level tax — credit) | https://www.legis.iowa.gov/docs/code/422.16C.pdf | 2026-10-28 |
| Iowa Code §422.17 (certificate authorizing payment without withholding) | https://www.legis.iowa.gov/docs/code/422.17.pdf | 2026-10-28 |
| Iowa Code §422.19 (scope of nonresident tax) | https://www.legis.iowa.gov/docs/code/422.19.pdf | 2026-10-28 |

Not yet confirmed: Iowa withholding form identifiers (the Iowa W-4 variant, the quarterly return form number, e-file thresholds) — the department's withholding pages returned 404/403 when archived and the current forms were not captured; whether the department has adjusted the remittance thresholds by rule; the current ch. 421 interest rate on unpaid withholding; any neighbour-state reciprocity agreements.

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
