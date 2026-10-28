---
name: hi-payroll-withholding
description: >
  Use this skill whenever asked about Hawaii income-tax withholding for tax
  year 2026 — HRS §§235-61 to 235-68: employer duty to withhold on wages,
  quarterly returns with semi-weekly (> $40,000/yr) and monthly
  (> $5,000/yr) remittance tiers, and the 7.25% withholding on Hawaii real
  property sold by nonresidents. Trigger on "Hawaii withholding", "Hawaii
  HW-1", "Hawaii W-2", "Hawaii real property withholding", "7.25 FIRPTA
  Hawaii", "HRS 235-61". Source-cited draft; statute text read from
  capitol.hawaii.gov 2026-10-27.
jurisdiction: US-HI
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - hi-income-tax
---

# Hawaii payroll withholding v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Hawaii income-tax withholding runs on HRS §§235-61 to 235-69. Statute text read directly from the HRS mirror at capitol.hawaii.gov 2026-10-27. **Source status:** the withholding duty, deposit tiers, quarterly-return rule, and the 7.25% real-property withholding are verified from statute; current form numbers (HW-1 employee certificate, HW-3 nonresident certificate, HW-4 annual reconciliation) and the e-filing mandate could not be read from tax.hawaii.gov this run (HTTP 429) — **needs-sources** for form identifiers.

## 2. Who applies

- **Every employer** as defined in §235-61(a) (text read 2026-10-27): the person/government for whom services are performed, the person controlling wage payment, and any person under State jurisdiction paying wages for a non-Hawaii employer. "Wages" is all remuneration for services, including non-cash value (§235-61(a), text read 2026-10-27).
- **Transferees buying Hawaii real property from nonresident persons** must withhold under §235-68 (see §6 below).
- Partnerships, estates, and trusts making payments withhold under §235-64.2 (TOC read 2026-10-27).

## 3. Mechanics and rates

| Item | Rule | Source |
|---|---|---|
| Withholding amount | rate that for the taxable year will yield the approximate tax liability, per withholding tables the department prescribes (§235-61(c)) | text read 2026-10-27 (first part); table mechanics **needs-sources** |
| Employee certificate | HW-1 (Hawaii analog of W-4) | **needs-sources** (form page 429) |
| Quarterly return | due **on or before the 15th day of the month after each calendar quarter** (§235-62(a), text read 2026-10-27) | verified |
| Deposit tier — semi-weekly | annual withholding liability **exceeds $40,000** (§235-62(c), text read 2026-10-27) | verified |
| Deposit tier — monthly | annual withholding liability **> $5,000 and ≤ $40,000** (§235-62(c), text read 2026-10-27) | verified |
| Deposit tier — with return | liability ≤ $5,000/yr: remit with the quarterly return | inferred from §235-62(c) tiers; confirm with DORM **needs-sources** |
| Annual reconciliation | W-2 equivalent to department + employees (§235-63 statements to employees, TOC read 2026-10-27); form HW-4 **needs-sources** | partial |
| Nonresident wage withholding | §235-66 further withholdings; HW-3 certificate **needs-sources** | partial |

## 4. Deadlines

- Quarterly withholding returns: **April 15, July 15, October 15, January 15** (15th day of the month following each quarter — §235-62(a), text read 2026-10-27).
- Deposits: semi-weekly or monthly per the §235-62(c) tiers above.
- Jeopardy: the director may demand immediate return/payment if collection is at risk (§235-62(d), text read 2026-10-27).

## 5. Penalties and interest

§235-104 makes the §231-39 penalties apply **to employers as well as taxpayers** (text read 2026-10-27): failure-to-file 5%/month to 25%; negligence up to 25%; fraud up to 50%; late payment after timely filing up to 20%; interest **⅔ of 1% per month** (§231-39, text read 2026-10-27). Withheld wages are held **in trust** for the State — employer is personally liable for amounts not remitted (§235-64, TOC read 2026-10-27; section text not extracted, **needs-sources** for the trust-liability wording).

## 6. Cross-border interactions

- **Nonresident real-property withholding (§235-68, text read 2026-10-27):** every transferee must deduct and withhold **7.25% of the amount realized** on a disposition of Hawaii real property by a "nonresident person"; resident persons are defined to include Hawaii-incorporated corporations, Hawaii-formed LLCs/partnerships, and resident trusts/estates. Exceptions/exemptions exist in later subsections (full text not extracted — **needs-sources** for exemption certificates and the $100,000-ish thresholds commonly used in practice).
- Out-of-State employers with Hawaii-workforce wages: the §235-61(a)(3) rule pulls any person under State jurisdiction paying wages for a non-Hawaii employer into the withholding duty.

## 7. Worked examples

An employer with $52,000 annual Hawaii withholding liability — deposit schedule test:

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

(Both differences positive → liability exceeds both thresholds → **semi-weekly** remitter per §235-62(c).)

A nonresident sells Hawaii real property for $850,000; the transferee withholds at the statutory rate:

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

## 8. Ask the client

- Which deposit tier applies — has annual liability crossed $5,000 or $40,000 mid-year?
- Are quarterly returns filed by the 15th after each quarter even when deposits were made on schedule?
- Any Hawaii real-estate closings involving nonresident sellers — is the 7.25% withholding being collected by the transferee/closing agent?
- Are remote employees working in Hawaii on the Hawaii withholding tables?

## Sources

1. HRS §235-61 (withholding duty, definitions): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0061.htm (200, text read 2026-10-27)
2. HRS §235-62 (quarterly returns; $5,000/$40,000 deposit tiers): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0062.htm (200, text read 2026-10-27)
3. HRS §235-68 (7.25% nonresident real-property withholding): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0068.htm (200, text read 2026-10-27)
4. HRS §235-104 (penalties apply to employers): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0104.htm (200, text read 2026-10-27)
5. HRS §231-39 (penalty/interest amounts): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm (200, text read 2026-10-27)
6. HRS ch. 235 TOC (withholding sections §§235-61–69): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-.htm (200, read 2026-10-27)
7. Hawaii Department of Taxation withholding page: https://tax.hawaii.gov/withholding/ (HTTP 429 all attempts 2026-10-27 — HW-1/HW-3/HW-4 form identifiers **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Hawaii payroll-withholding questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
