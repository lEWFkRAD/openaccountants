---
name: ne-payroll
description: >
  Use this skill whenever asked about Nebraska payroll withholding for
  2026 — employer income-tax withholding under Revenue Act § 77-3513, the
  Department of Revenue withholding rails, the annual Income Tax
  Withholding Circular (Circular EN, 2026 and 2027 editions verified),
  and pass-through entity withholding rails. Trigger on "Nebraska
  withholding", "941-N", "Circular EN", "Nebraska W-2", "Nebraska
  employer withholding". Source-cited draft; withholding page, § 77-3513
  and the Circular EN 2026/2027 PDFs verified 2026-10-28; form IDs and
  deposit frequencies needs-sources (circular text not parsed).
jurisdiction: US-NE
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ne-income-tax
---

# Nebraska payroll withholding v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## 1. Scope and sources

Employer income-tax withholding for Nebraska wages. **Source status:** verified 2026-10-28 — the DOR withholding page (https://revenue.nebraska.gov/businesses/income-tax-withholding, fetched, 200), the withholding forms index (https://revenue.nebraska.gov/about/forms/income-tax-withholding-forms, fetched, 200), statute **§ 77-3513** (fetched), and the official **Circular EN PDFs for 2026 and 2027** (https://revenue.nebraska.gov/sites/default/files/doc/forms/2026cir_en_whole.pdf, .../2027cir_en_whole.pdf — existence verified). The **withholding return form ID (941-N is the conventional number — confirm) and deposit-frequency thresholds live inside Circular EN, not parsed this run — needs-sources**.

## 2. Who applies

Every employer paying Nebraska wages (residents and nonresidents working in Nebraska), per § 77-3513 (statute verified reachable). PTE-level rails where the entity elects the PTE tax (see `ne-corporate-income-tax.md`).

## 3. Rates / tables

Withholding follows the individual graduated schedule (2026 top rate 5.5% expected — see `ne-income-tax.md`; confirm against Circular EN — **needs-sources**).

## 4. Base

Wages, pensions, and statutory categories per Circular EN (not parsed — **needs-sources**).

## 5. Deadlines, penalties, interest

- Withholding return cadence and W-2 annual filing: per Circular EN — **needs-sources**.
- Penalty/interest percentages: **needs-sources**.

## 6. Cross-border notes

Nonresident workers: Nebraska taxes workday-sourced wages; withholding applies regardless of residence (verify sourcing rule detail — **needs-sources**). Reciprocity: none located — **needs-sources**.

## 7. Worked examples

**Example 1 — quarterly remittance.** Q1 Nebraska wages $100,000, effective withheld rate 5%:

```oa-check
name: NE quarterly withholding
inputs:
  wages: 100000
  eff_rate: 0.05
steps:
  - withheld: wages * eff_rate
expected:
  withheld: 5000.00
```

**Example 2 — annual true-up sketch.** Employer remitted $18,400 across four quarters; annual W-2-based liability $19,150:

```oa-check
name: NE annual true-up
inputs:
  remitted: 18400
  liability: 19150
steps:
  - balance_due: liability - remitted
expected:
  balance_due: 750.00
```

## 8. Ask the client

- Is the payroll system loaded with the current-year Circular EN tables?
- Remote workers performing days in Nebraska?
- PTE tax election — does withholding posture change at the entity level?

## 9. Sources

1. DOR Income Tax Withholding: https://revenue.nebraska.gov/businesses/income-tax-withholding — fetched and verified 2026-10-28.
2. Circular EN 2026: https://revenue.nebraska.gov/sites/default/files/doc/forms/2026cir_en_whole.pdf — existence verified 2026-10-28.
3. Circular EN 2027: https://revenue.nebraska.gov/sites/default/files/doc/forms/2027cir_en_whole.pdf — existence verified 2026-10-28.
4. § 77-3513: https://nebraskalegislature.gov/laws/statutes.php?statute=77-3513 — fetched 2026-10-28.

**Needs-sources:** form IDs (941-N, W-2 NE box), deposit frequency, penalty/interest, Circular EN table figures, sourcing/reciprocity detail.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Nebraska payroll questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
