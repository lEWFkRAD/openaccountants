---
name: hi-payroll-withholding
description: >
  Use this skill whenever asked about Hawaii income-tax withholding for tax
  year 2026 — HRS §§235-61 to 235-68: employer duty to withhold on wages,
  quarterly returns with semi-weekly (over $40,000/yr) and monthly
  (over $5,000/yr) remittance tiers, and the 7.25% withholding on Hawaii real
  property sold by nonresidents. Trigger on "Hawaii withholding", "Hawaii
  HW-1", "Hawaii W-2", "Hawaii real property withholding", "7.25 FIRPTA
  Hawaii", "HRS 235-61". Source-cited draft; statute text read from
  capitol.hawaii.gov 2026-10-27 and 2026-10-28.
jurisdiction: US-HI
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - hi-income-tax
---

# Hawaii payroll withholding v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from HRS §§235-61, 235-62, 235-68, 235-104 and §231-39, read on capitol.hawaii.gov (runs of 2026-10-27 and 2026-10-28). No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

Hawaii income-tax withholding runs on HRS §§235-61 to 235-69. The withholding duty, the deposit tiers, the quarterly-return rule, and the 7.25% real-property withholding below are verified from the archived statute text.

## Who this applies to

- **Every employer** as defined in §235-61(a): the person/government for whom services are performed, the person controlling wage payment, and any person under State jurisdiction paying wages for a non-Hawaii employer. "Wages" is all remuneration for services, including non-cash value (§235-61(a)).
- **Transferees buying Hawaii real property from nonresident persons** must withhold under §235-68.
- Partnerships, estates, and trusts making payments withhold under §235-64.2 (ch. 235 withholding subchapter; section list from the archived ch. 235 TOC).

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Withholding amount | rate that for the taxable year will yield the approximate tax liability, per withholding tables the department prescribes (§235-61) — "The certificate shall be in such form and contain such information as may be prescribed by the department." | §235-61, archived text |
| Quarterly return | "make a return of such wages to the department of taxation on or before the fifteenth day of the calendar month following the close of each such quarter for which the taxes have been withheld" (§235-62) | §235-62, archived text |
| Deposit tier — semi-weekly | "each employer whose liability for taxes withheld exceeds $40,000 annually shall remit the complete amount of tax withheld on a semi-weekly schedule" (§235-62) | §235-62, archived text |
| Deposit tier — monthly | "each employer whose liability for taxes withheld exceeds $5,000 but does not exceed $40,000 annually shall remit the complete amount of tax withheld on a monthly schedule" (§235-62) | §235-62, archived text |
| Deposit tier — with return | liability not over $5,000/yr follows the default quarterly-return remittance (the statute sets semi-weekly over $40,000 and monthly over $5,000; the base rule is remittance with the quarterly return) | §235-62, archived text (tiers) |
| Nonresident wage withholding | §235-66 further withholdings by nonresident individuals and withholding on nonresident partners/beneficiaries (ch. 235 TOC) | TOC |
| Annual reconciliation | §235-63 statements to employees (ch. 235 TOC) | TOC |

## The taxable base

- Wages: "all remuneration for services" including non-cash value (§235-61 definitions).
- Withheld wages are held in trust for the State; the employer is liable for amounts not remitted (§235-64 area of the ch. 235 withholding subchapter — see Not yet confirmed below for the trust-liability wording).

## Deadlines and filing

- Quarterly withholding returns: due "on or before the fifteenth day of the calendar month following the close of each such quarter" (§235-62, archived text).
- Deposits: semi-weekly (over $40,000 annual liability) or monthly (over $5,000 but not over $40,000) per the §235-62 tiers.
- Jeopardy: the director may require immediate return and payment if collection is at risk (§235-62, archived text).

## Penalties and interest

§235-104 (archived text): "The penalties and interest provided by section 231-39 shall apply to employers as well as taxpayers." The §231-39 amounts: failure-to-file 5%/month capped at 25%; negligence up to 25%; fraud up to 50%; late payment after timely filing up to 20%; interest at two-thirds of one per cent a month (see `hi-corporate-income-tax` for the exact confirmed quotes).

## Cross-border points

- **Nonresident real-property withholding (§235-68, archived text):** "every transferee shall deduct and withhold a tax equal to 7.25 per cent of the amount realized on the disposition of Hawaii real property." "Nonresident person" means every person other than a resident person (resident persons per §235-68(a) include Hawaii-incorporated corporations, Hawaii-formed LLCs/partnerships, and resident trusts/estates).
- Out-of-State employers with Hawaii-workforce wages: the §235-61(a) rule pulls any person under State jurisdiction paying wages for a non-Hawaii employer into the withholding duty.
- Exemption certificates and lower-withholding mechanics in later §235-68 subsections: see Not yet confirmed below.

## Worked examples

### Example 1: employer with $52,000 annual Hawaii withholding liability — deposit-schedule test (hypothetical client facts)

```oa-check
name: HI withholding deposit tier test
inputs:
  annual_liability: 52000
  monthly_threshold: 5000
  semiweekly_threshold: 40000
steps:
  - over_monthly: annual_liability - monthly_threshold
  - over_semiweekly: annual_liability - semiweekly_threshold
expected:
  over_monthly: 47000.00
  over_semiweekly: 12000.00
```

(Both differences positive → liability exceeds $40,000 → semi-weekly remitter per the confirmed §235-62 tiers.)

### Example 2: nonresident sells Hawaii real property for $850,000 (hypothetical client facts); transferee withholds at the statutory rate

```oa-check
name: HI nonresident realty withholding
inputs:
  amount_realized: 850000
  rate: 0.0725
steps:
  - withheld: amount_realized * rate
expected:
  withheld: 61625.00
```

(The 7.25% rate is the confirmed §235-68(b) sentence.)

## Ask the client first

1. Which deposit tier applies — has annual liability crossed $5,000 or $40,000 mid-year?
2. Are quarterly returns filed by the 15th after each quarter even when deposits were made on schedule?
3. Any Hawaii real-estate closings involving nonresident sellers — is the 7.25% withholding being collected by the transferee/closing agent?
4. Are remote employees working in Hawaii on the Hawaii withholding tables?

## Sources

| Source | URL | Read on |
|---|---|---|
| HRS §235-61 (withholding duty, definitions) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0061.htm | 2026-10-28 |
| HRS §235-62 (quarterly returns; $5,000/$40,000 deposit tiers) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0062.htm | 2026-10-28 |
| HRS §235-68 (7.25% nonresident real-property withholding) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0068.htm | 2026-10-28 |
| HRS §235-104 (penalties apply to employers) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0104.htm | 2026-10-28 |
| HRS §231-39 (penalty/interest amounts) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm | 2026-10-28 |
| HRS ch. 235 table of contents (withholding sections §§235-61–69; §235-63 statements; §235-64.2) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-.htm | 2026-10-28 |

Not yet confirmed: current form identifiers (HW-1 employee certificate, HW-3 nonresident certificate, HW-4 annual reconciliation — tax.hawaii.gov was unreachable for the forms pages this run); the withholding-table mechanics prescribed by the department; the §235-64 trust-liability wording; §235-68 exemption certificates and any dollar thresholds in later subsections; the current e-filing mandate; and the current N-15 instruction details for nonresident withholding. Each was flagged in v0.2 and has not been tied to an archived primary source, so no figure for them is asserted here.

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
