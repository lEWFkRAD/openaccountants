---
name: ia-payroll-withholding
description: >
  Use this skill whenever asked about Iowa income-tax withholding for tax
  year 2026 — Iowa Code §422.16: withholding-agent duty on Iowa residents
  and nonresidents working in Iowa, quarterly/monthly/semimonthly remittance
  tiers ($6,000 annual / $500 monthly / $5,000 semimonthly), the $500
  willful-failure civil penalty, and the PTE entity-level election under
  §422.16C. Trigger on "Iowa withholding", "Iowa W-4", "Iowa Form 4407",
  "Iowa withholding tiers", "422.16", "Iowa PTE election". Source-cited
  draft; Iowa Code 2026 text read from legis.iowa.gov 2026-10-27.
jurisdiction: US-IA
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ia-income-tax
---

# Iowa payroll withholding v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-27. Iowa withholding runs on Iowa Code §422.16 (withholding at source — penalties — interest — estimated tax). Statute text read directly from the Iowa Code 2026 PDF at legis.iowa.gov 2026-10-27. **Source status:** the withholding-agent definition, remittance tiers, deposit dates, personal liability, and $500 civil penalties are verified from statute text; form identifiers (W-4 Iowa version, Form 4407 quarterly return) and e-filing thresholds for withholding agents — **needs-sources** (tax.iowa.gov paths 404 this run).

## 2. Who applies

- **Every withholding agent** paying wages to an Iowa resident, or to a nonresident working in Iowa (§422.16(1)-(2)(a)(1), text read 2026-10-27). The definition sweeps in governments, municipalities, school districts, and any entity paying taxable Iowa income to a nonresident.
- Officers/employees with responsibility under the section who **knowingly violate** it are personally within the definition (§422.16(1), text read 2026-10-27).
- Nonresident income not otherwise withheld: agent withholds at the same rate unless the department issues a no-withholding certificate under §422.17 (§422.16(2)(b), text read 2026-10-27).
- Film/TV production nonresidents: exempt from Iowa withholding where the employer holds a department exemption (§422.16(11)(b), text read 2026-10-27).

## 3. Mechanics and remittance tiers

| Tier | Condition (text read 2026-10-27, §422.16(4)) | Deposit due |
|---|---|---|
| Quarterly | withholds **< $6,000 annually** and ≤ $500 in any one month | with the quarterly return, last day of month after quarter |
| Monthly | > $500 in any one month and ≤ $5,000 in a semimonthly period | 15th of month following withholding; third-month deposit due with the quarterly return |
| Semimonthly | > $5,000 in a semimonthly period | 1st–15th period → 25th of same month; 16th–end → 10th of following month |

- Quarterly withholding return due **on or before the last day of the month following the quarter** (§422.16(4), text read 2026-10-27).
- Amount withheld approximates annual liability using department tables/schedules; over-claiming withholding allowance is a serious misdemeanor (§422.16(2)(a), text read 2026-10-27).
- Department may adjust the remittance thresholds by rule (§422.16(4), text read 2026-10-27) — confirm current thresholds **needs-sources**.
- **PTE election (§422.16C, text read 2026-10-27):** partnerships/S corps may elect annual, irrevocable entity-level tax at the individual rate (3.8% for 2026), replacing composite returns under §422.16B; partners get a credit.

## 4. Deadlines

- Quarterly returns: Jan 31, Apr 30, Jul 31, Oct 31 (last day of month after each quarter — §422.16(4), text read 2026-10-27).
- Deposits per the tier table above.
- Estimated tax (agents pay on behalf of certain nonresidents; individuals/corps self-estimate): installments due last day of the 4th, 6th, 9th, and 1st months of the tax year when liability ≥ $1,000 (§422.16(12), text read 2026-10-27).

## 5. Penalties and interest

- **Personal liability:** a withholding agent who fails to withhold or pay is "personally, individually, and corporately liable" (§422.16(5), text read 2026-10-27).
- **$500 civil penalty per occurrence** for willful failure to furnish/file income statements, or furnishing false/fraudulent statements (§422.16(11)(a), text read 2026-10-27).
- Interest on unpaid amounts runs under §421.60(2)(e) mechanics — current rate **needs-sources**.
- Overwithheld balances ≥ $1 refunded to the employee with interest; < $1 only on written application within 12 months (§422.16(10), text read 2026-10-27).

## 6. Cross-border interactions

- Nonresidents working in Iowa (including commuters and seasonal ag workers): withholding applies; agricultural-commodity estimated-payment election exists for agents (§422.16(11)(a) area, text read 2026-10-27).
- Reciprocal states: Iowa has **no** general neighbor reciprocity exemption in the text read — confirm treatment of IL/WI/MN/NE commuters **needs-sources**.
- Foreign owners of Iowa PTEs: the §422.16C election substitutes entity-level tax for composite filings.

## 7. Worked examples

Agent withholds $450 in January, $620 in February, $480 in March:

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

(February exceeds $500 → monthly remitter for the period; quarterly return still due Apr 30.)

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

(Excess positive → semimonthly schedule; the 1–15 March deposit is due March 25.)

## 8. Ask the client

- Which remittance tier applies month-by-month — the tiers flip on single-month spikes?
- Are quarterly returns filed even when deposits were current?
- Any nonresident workers (commuters, seasonal, film) — certificates or PTE election in place?
- Willful statement failures carry $500 each — is W-2/income-statement issuance under control?

## Sources

1. Iowa Code §422.16 (withholding; tiers; penalties; estimated tax): https://www.legis.iowa.gov/docs/code/422.16.pdf (200, text read 2026-10-27)
2. Iowa Code §422.16C (PTE entity-level election): https://www.legis.iowa.gov/docs/code/422.16C.pdf (200, text read 2026-10-27)
3. Iowa Code §422.19 (scope of nonresident tax): https://www.legis.iowa.gov/docs/code/422.19.pdf (200, text read 2026-10-27)
4. Iowa Department of Revenue withholding page: https://tax.iowa.gov/withholding (404 this run — form IDs **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Iowa payroll-withholding questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
