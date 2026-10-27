---
name: sx-transfer-pricing
description: >
  Sint Maarten related-party pricing: no statutory transfer-pricing
  documentation regime was found in retrievable official sources, so
  adjustments run through the Inspector's assessment powers under the general
  tax ordinance and the third-party payment declarations the GRC matches
  against deductions. Covers practical evidence standards, the appeal route,
  and what to tell cross-border groups. Applies to Dutch Sint Maarten.
jurisdiction: SX
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Sint Maarten: transfer pricing

## Regime status

No dedicated transfer-pricing ordinance, arm's-length standard, or documentation requirement was found in the retrievable official sources (general tax ordinance CVDR671742; GRC guides and forms) as of 2026-10-27. Treat Sint Maarten as a **Comptroller/Inspector-assessment jurisdiction**: related-party pricing is policed indirectly, through the Inspectorate's assessment and information powers and the third-party payment declarations, not through a filing form.

**needs-sources:** the profit-tax and income-tax ordinances themselves (not retrievable 2026-10-27) may contain general anti-arbitrariness or arm's-length language; confirm before advising a group that nothing exists.

## How the Inspectorate actually reaches related parties

- **Third-party activity declarations ("opgAAF werkzaamheden derden")**: businesses must declare payments to third parties on the official GRC form (2021–2025 editions in the document library). Management fees, royalties, interest and service charges to foreign affiliates surface here and are matched against deductions taken on profit-tax and income-tax returns.
- **Assessment + penalty machinery**: under the general tax ordinance (CVDR671742) the Inspector issues assessments; late/incorrect information carries penalties up to NAf 1,000; the taxpayer's route is the two-month motivated written appeal.
- **Bookkeeping and information duties**: the employer/business is "obliged by law to provide correct and complete information to the Inspectorate of Taxes" (GRC guide).

## Practical evidence standard

Absent a statutory method, build the file a Dutch-Caribbean inspector will accept: intercompany agreements, benchmarking from a recognised method (CUP/TNMM) for material flows, invoices matching services actually rendered, and proof of benefit for management fees. The France–Saint Martin and Netherlands–Sint Maarten constitutional link means Dutch-tax-literature arm's-length concepts are commonly understood by the Inspectorate, but they are not Sint Maarten law — cite them as practice, not authority.

## Worked examples

**Example 1 — exposure sizing on an unbenchmarked royalty.** A Sint Maarten operator pays a foreign affiliate Cg 180,000/yr royalty with no benchmarking. Assume the Inspectorate re-allowances only 60% of it.

```oa-check
name: royalty disallowance exposure at assumed 30% rate
inputs:
  royalty: 180000
  allowed_fraction: 0.60
  assumed_rate: 0.30
steps:
  - disallowed: royalty * (1 - allowed_fraction)
  - extra_tax: disallowed * assumed_rate
expected:
  disallowed: 72000
  extra_tax: 21600
```

(Rate is the same needs-sources assumption as sx-corporate-income-tax.)

**Example 2 — appeal clock.** Assessment dated 15 July 2026; written motivated appeal must reach the Inspector within two months.

```oa-check
name: appeal deadline month arithmetic
inputs:
  assessment_month: 7
  appeal_window_months: 2
steps:
  - appeal_deadline_month: assessment_month + appeal_window_months
expected:
  appeal_deadline_month: 9
```

Deadline: 15 September 2026 (same day-of-month two months on).

## Ask the client

- Full intercompany inventory: who receives what from the Sint Maarten entity, and where are the counterparties tax-resident?
- Copies of every third-party declaration filed — do they match the deduction schedules on the returns?
- Any transfer-pricing file prepared for the group's home jurisdiction (NL/France/US) — reuse it as evidence even though it is not locally mandated.
- Has any assessment or information request arrived? The two-month appeal clock governs.

## Sources

- [General tax-ordinance (formal tax law), lokaleregelgeving CVDR671742](https://lokaleregelgeving.overheid.nl/CVDR671742) — read 2026-10-22
- [GRC document library: third-party activity declaration forms 2021–2025; guide text on information duties and penalties (PDFs)](https://www.tax.sx/documents/businesses) — read 2026-10-27
- Statutory arm's-length standard: **needs-sources** (profit-tax/income-tax ordinances not retrievable 2026-10-27).

<!-- openaccountants-cta-block -->

**Talk to a verified accountant.** This is a source-cited draft, not reviewed advice. [Book time with an OpenAccountants Partner](https://calendly.com/openaccountants/consultation).
