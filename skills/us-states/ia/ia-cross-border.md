---
name: ia-cross-border
description: >
  Use this skill whenever asked about Iowa cross-border personal tax
  situations for tax year 2026 — nonresident taxation of Iowa-source income
  (§422.19 receipt-basis rule), the flat 3.8% rate for residents and
  nonresidents alike, the §422.17 no-withholding certificate, and the PTE
  election vs. composite returns for out-of-state owners. Trigger on
  "Iowa nonresident", "Iowa part-year", "Iowa commuter", "Iowa-source
  income", "422.19", "Iowa composite return", "Iowa PTE". Corrected
  2026-10-28 against archived Iowa Code 2026 statute text.
jurisdiction: US-IA
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - ia-income-tax
---

# Iowa cross-border, tax year 2026

> **Source-cited draft.** Built from Iowa Code §§422.5, 422.16, 422.16C, 422.17 and 422.19 (Iowa Legislature, Iowa Code 2026), read on 2026-10-28. No accountant has reviewed it. Do not file, pay, amend, or take a tax position from it without review by a qualified Iowa professional.

Tax year: the individual's tax year. Authority: Iowa Department of Revenue. Currency: US dollars. Covers residents, nonresidents, part-year residents, and out-of-state owners of Iowa flow-throughs.

See also: `ia-income-tax`, `ia-payroll-withholding`.

## Who this applies to

- **Iowa residents:** the tax is imposed "upon every resident and nonresident of the state ... upon and with respect to the entire taxable income" at a flat 3.8% (§422.5(1)(a)).
- **Nonresidents:** Iowa-source income only. §422.5(1)(b)(1) computes nonresident tax by "multiplying this resulting amount by a fraction of which the nonresident's net income allocated to Iowa ... is the numerator and the nonresident's total net income computed under section 422.7 is the denominator" — this proration formula "also applies to individuals who are residents of Iowa for less than the entire tax year".
- Part-year residents: same allocated-fraction mechanics (§422.5(1)(b)(1)); the §422.8 allocation detail is listed under Not yet confirmed.
- Withholding agents paying Iowa-source income to nonresidents: withhold under §422.16(2)(b) "at the same rate" unless the department has issued a §422.17 certificate.

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Individual rate | flat 3.8% on taxable income, residents and nonresidents | §422.5(1)(a) |
| Nonresident computation | tax × (Iowa-allocated net income ÷ total net income) | §422.5(1)(b)(1) |
| Estimated tax | required when Iowa income tax liability "can reasonably be expected to amount to one thousand dollars or more for the year" | §422.16(12)(a)(1) |

- §422.5(1)(a): "A tax is imposed upon every resident and nonresident of the state which tax shall be levied, collected, and paid annually upon and with respect to the entire taxable income ... at a rate of three and eight-tenths percent."

## The taxable base

- Residents: entire (worldwide) taxable income as defined in ch. 422 subchapter II.
- Nonresidents: the nonresident's "net income allocated to Iowa" drives the proration fraction; income counts when "actually received by such nonresident regardless of when such income was earned" (§422.19), subject to the when-demandable rule for accrual-basis nonresidents in §422.19. (not yet confirmed)

## Deadlines and filing

- Estimated tax installments: "on or before the last day of the fourth month of the taxpayer's tax year", the last day of the sixth month, the last day of the ninth month, and the last day of the first month of the following tax year (§422.16(12)(b)(1)).
- Final tax: due "on or before the end of the fourth month following the close of the tax year" (§422.16(12)(b)(3)).
- §422.17 certificate: a nonresident who "pays the entire amount of tax properly estimated on or before the last day of the fourth month of the nonresident's tax year" may be granted a certificate authorizing payment without withholding (§422.17).
- The IA 1040/IA 1040NR return due date and extension mechanics — see Not yet confirmed.

## Penalties and interest

- A withholding agent who fails to withhold or pay "shall be personally, individually, and corporately liable to the state of Iowa" (§422.16(5)).
- Overwithheld amounts: "any balance of one dollar or more shall be refunded to the employee, nonresident, or other person with interest" (§422.16(10)(a)); amounts under $1 only on written application within twelve months (§422.16(10)(b)).
- Nonresident underpayment penalties and the current ch. 421 interest rate — see Not yet confirmed.

## Cross-border points

- **Receipt rule:** §422.19 taxes Iowa-source income "actually received by such nonresident regardless of when such income was earned" — income earned in earlier years can land in the nonresident year it is received. (not yet confirmed)
- **PTE election (§422.16C):** a partnership or S corporation "may elect to be subject to" entity-level tax "in an amount equal to the rate under section 422.5" (3.8%); the election "shall be irrevocable once made"; the electing entity "shall not be required to file a composite return for the same tax year pursuant to section 422.16B"; partners/shareholders get a credit (§422.16C(5)); a nonresident individual whose only Iowa income is from the electing entity "shall not be required to file an individual income tax return under section 422.13" (§422.16C(6)).
- Reciprocity with neighbouring states: no archived statute text confirms any — see Not yet confirmed.
- Remote workers: physical presence working in Iowa creates Iowa-source wages (see `ia-social-contributions` for the UI mirror).

## Worked examples

Hypothetical Wisconsin resident works 120 of 250 job-site days in Iowa, wages $90,000, no withholding by the agent:

```oa-check
name: IA nonresident sourced wages
inputs:
  wages: 90000
  iowa_days: 120
  work_days: 250
  rate: 0.038
steps:
  - sourced: wages * (iowa_days / work_days)
  - tax: sourced * rate
expected:
  sourced: 43200.00
  tax: 1641.60
```

(Day-count sourcing is a hypothetical allocation method; the confirmed mechanics are the §422.5(1)(b)(1) allocated-income fraction at the confirmed 3.8% rate. IA 1040NR allocation schedules are listed under Not yet confirmed.)

Same hypothetical taxpayer obtains a §422.17 certificate by paying the full $1,641.60 estimated tax by the last day of the fourth month of the tax year:

```oa-check
name: IA 422.17 certificate funding check
inputs:
  estimated_tax: 1641.60
  threshold: 1000
steps:
  - above_estimated_threshold: estimated_tax - threshold
expected:
  above_estimated_threshold: 641.60
```

(The $1,000 threshold is the confirmed §422.16(12)(a)(1) estimated-tax trigger; the certificate itself requires paying the entire estimated tax, §422.17.)

## Ask the client first

- Commuter or remote worker: is Iowa withholding happening, or is a §422.17 certificate in place?
- Mid-year move: has the §422.5(1)(b)(1) allocated-income fraction been applied for the part-year period?
- Out-of-state owners of Iowa partnerships: PTE election vs. composite vs. individual filings — which is cheaper at the 3.8% flat rate (§422.16C)?
- Overwithheld commuters: refund claim with interest available for balances of $1 or more (§422.16(10)).

## Sources

| Source | URL | Read on |
|---|---|---|
| Iowa Code §422.5 (flat 3.8% rate; nonresident proration) | https://www.legis.iowa.gov/docs/code/422.5.pdf | 2026-10-28 |
| Iowa Code §422.19 (scope of nonresident tax; receipt rule) | https://www.legis.iowa.gov/docs/code/422.19.pdf | 2026-10-28 |
| Iowa Code §422.17 (no-withholding certificate) | https://www.legis.iowa.gov/docs/code/422.17.pdf | 2026-10-28 |
| Iowa Code §422.16 (withholding; estimated tax; refunds) | https://www.legis.iowa.gov/docs/code/422.16.pdf | 2026-10-28 |
| Iowa Code §422.16C (PTE election — entity-level tax — credit) | https://www.legis.iowa.gov/docs/code/422.16C.pdf | 2026-10-28 |
| Iowa Code §422.7 (total net income of nonresident) | https://www.legis.iowa.gov/docs/code/422.7.pdf | 2026-10-28 |

Not yet confirmed: the residency/domicile definition and part-year allocation detail under §422.8; IA 1040 / IA 1040NR form mechanics and the individual return due date and extension; whether Iowa has income-tax reciprocity agreements with Illinois, Minnesota, Nebraska, Wisconsin or any other state; composite-return mechanics under §422.16B; the current ch. 421 interest rate and nonresident underpayment penalty percentages.

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
