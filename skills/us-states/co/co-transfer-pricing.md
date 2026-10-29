---
name: co-transfer-pricing
description: >
  Use this skill whenever asked about Colorado transfer pricing and
  related-party adjustments for tax year 2026 — the related-party
  transaction adjustment rule at C.R.S. §39-22-503, combined reporting
  for tax-haven countries under §39-22-5303, receipts-factor
  apportionment under §39-22-303.6, and sourcing rules under Rule
  39-22-109. Trigger on "Colorado transfer pricing", "Colorado
  related party", "Colorado addback", "Colorado tax haven combined
  reporting", "Colorado receipts factor", "39-22-503", "39-22-5303".
  Source-cited draft; DR 0106 instructions read 2026-10-27, statute
  text pending verification.
jurisdiction: US-CO
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - co-corporate-income-tax
---

# Colorado transfer pricing & related-party rules v0.1

## 1. Scope and sources

Covers how Colorado adjusts intercompany and cross-border related-party
income. **Source status:** the C.R.S. text for §§39-22-503, 39-22-5303,
39-22-303.6 was unreachable from this workstation this run
(leg.colorado.gov PDFs 404; Justia/casetext/findlaw 403/410/404 on
2026-10-27). The apportionment and sourcing references below are
verified from the DR 0106 instructions (2025 PDF, read 2026-10-27);
statute-level substance is flagged **pending verification** and must
be re-read before any filing position.

## 2. Who applies

- Corporations and pass-through entities with transactions involving
  related parties (common ownership/control) — the §39-22-503
  adjustments-for-related-party-transactions rule (pending
  verification).
- Taxpayers with affiliates in low- or no-tax ("tax haven") countries
  — combined reporting under §39-22-5303 (pending verification).
- Entities apportioning income across states — receipts-factor
  apportionment under §39-22-303.6 (verified reference on DR 0106
  instructions).

## 3. Rates and mechanics

| Mechanism | Effect | Source |
|---|---|---|
| Corporate rate | 4.4% flat | Verified DR 0106 line 20 (0.044) |
| Related-party adjustments | DOR may adjust interest/rent/royalty and other related-party transactions to clearly reflect income | C.R.S. §39-22-503 (pending) |
| Tax-haven combined reporting | Combined return with tax-haven affiliates in specified circumstances | C.R.S. §39-22-5303 (pending) |
| Apportionment | Receipts-factor apportionment; direct sourcing election for some items | C.R.S. §39-22-303.6 (verified reference) |
| Sourcing | Colorado-source items: property in CO, business carried on in CO, intangibles employed in CO business | Rule 39-22-109(3) (verified reference on DR 0106) |

## 4. Base and timing

- Ordinary income of a partnership is generally sourced using
  receipts-factor apportionment even without a full §39-22-303.6
  election (verified DR 0106 text).
- No activity outside Colorado → 100% sourced to Colorado (verified
  DR 0106 text).
- Related-party adjustments apply to the taxable year of the affected
  transaction; DOR has authority to reallocate and recharacterize
  (pending verification of §39-22-503 text).

## 5. Deadlines

- Adjustments follow the return and assessment cycle: DR 0107/DR 0106
  due 15th day of the 4th month (April 15 calendar year); DOR
  assessment statute of limitations — verify current rules.

## 6. Penalties and interest

- Underpaid tax from adjustments accrues interest under C.R.S.
  §39-21-118 (pending verification).
- Delinquent payment penalty: greater of $5 or 5% first month + 0.5%
  per additional month; 90%-by-due-date shield (verified DR 0106
  text).

## 7. Cross-border interactions

- Tax-haven combined reporting (§39-22-5303) is Colorado's principal
  cross-border anti-avoidance rule — confirm the current definition of
  "tax haven country" and the ownership thresholds before advising
  (pending verification).
- Federal international provisions (GILTI/FDII) conformity: verify
  current-year Colorado conformity before using federal starting
  points (pending).
- PL 86-272 applies to net-income tax on protected solicitation
  (federal — see `co-cross-border`).

## 8. Worked examples

A Colorado corporation pays $1,000,000 in royalties to a wholly owned
affiliate in a low-tax country. DOR adjusts the royalty to an
arm's-length $600,000; the $400,000 disallowed amount is added back
and taxed at 4.4%:

```oa-check
name: royalty addback tax effect
inputs:
  paid: 1000000
  arm_length: 600000
  rate: 0.044
steps:
  - disallowed: paid - arm_length
  - tax: disallowed * rate
expected:
  disallowed: 400000.00
  tax: 17600.00
```

A multistate licensor earns $8,000,000 of royalty income; receipts
sourced to Colorado are $2,000,000:

```oa-check
name: receipts-factor royalty apportionment
inputs:
  co_receipts: 2000000
  total_receipts: 8000000
  rate: 0.044
steps:
  - factor: co_receipts / total_receipts
  - apportioned: total_receipts * factor
  - tax: apportioned * rate
expected:
  factor: 0.25
  apportioned: 2000000.00
  tax: 88000.00
```

## 9. Ask the client

- What intercompany interest, rent, royalty, or service fees exist
  with related parties (domestic or foreign)?
- Are there affiliates in low- or no-tax jurisdictions → §39-22-5303
  combined-reporting exposure?
- Is transfer-pricing documentation contemporaneous and defensible
  under §482 (federal) and Colorado's adjustment authority?
- Which receipts are Colorado-sourced under Rule 39-22-109?

## Sources

1. Colorado DOR — Form DR 0106 instructions (2025): https://tax.colorado.gov/sites/tax/files/documents/DR0106_2025.pdf (200 PDF, 2026-10-27)
2. Colorado DOR — Form DR 0107 (2025): https://tax.colorado.gov/sites/tax/files/documents/DR0107_2025.pdf (200 PDF, 2026-10-27)
3. C.R.S. §39-22-503 Adjustments for related-party transactions: https://leg.colorado.gov (403/404 this run — **needs-sources**, re-read before relying)
4. C.R.S. §39-22-5303 Combined reporting for tax-haven countries: https://leg.colorado.gov (403/404 this run — **needs-sources**)
5. C.R.S. §39-22-303.6 Receipts-factor apportionment: verified as cited on DR 0106 instructions; full text **needs-sources**

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Colorado transfer-pricing questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
