---
name: ar-corporate-income-tax
description: >
  Use this skill whenever asked about Arkansas corporate income tax
  for tax year 2026 — the SB 567 / Act 719 of 2025 corporate-tax
  modernization (market-based sourcing for services and intangibles,
  economic nexus for non-resident entities), Form AR-1100 /
  AR-1100ADJ / AR-1100S mechanics, the pass-through entity tax, and
  estimated tax. Trigger on "Arkansas corporate tax", "Arkansas
  AR-1100", "Arkansas SB 567", "Arkansas Act 719", "Arkansas market
  based sourcing", "Arkansas pass-through entity tax". Source-cited
  draft; DFA corporate page read 2026-10-27 and archived 2026-10-28 (page confirms: "On April 16, 2025, Arkansas Gov. Sarah Huckabee Sanders signed Senate Bill 567 into law as Act 719 of 2025, modernizing the state's corporate income tax… adopting Market-Based Sourcing for Sales of Services and Intangibles… establishes an economic nexus filing threshold for non-resident corporations or partnerships"); the current rate
  percentage is flagged needs-sources.
jurisdiction: US-AR
category: corporate
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: "0.2"
verified_by: pending
depends_on:
  - ar-income-tax
---

# Arkansas corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Arkansas taxes C corporations on Arkansas-apportioned income and layered a major reform in 2025: **SB 567, signed as Act 719 of 2025 on 2025-04-16**, "modernizing the state's corporate income tax" — it amends Arkansas' adoption of the Multistate Tax Compact/UDITPA, adopts **market-based sourcing for sales of services and intangibles** (location where delivered to the customer), establishes an **economic nexus filing threshold for non-resident corporations or partnerships**, and amends business-income provisions (all quoted/paraphrased from the DFA Corporation Income Tax page, fetched 2026-10-27). **Source status:** the reform narrative is read from the DFA page; the **current corporate rate percentage is needs-sources** — arkleg.state.ar.us served empty/500 responses from this host and the Act 719 PDF downloaded 0 bytes, so the rate must be confirmed against the AR-1100 instructions (2026-01-08 revision exists per DFA search) before publishing figures.

## 2. Who applies

- C corporations doing business in Arkansas, and **non-resident corporations over the SB 567 economic-nexus threshold** (threshold amount: **needs-sources**).
- S corporations file AR-1100S; partnerships/LLCs file the partnership return and members pay individually, unless the entity elects the **pass-through entity tax (PET)** (election mechanics on ATAP; rate **needs-sources**).
- The AR-1100ADJ adjustment schedule carries the state modifications to federal taxable income (2026-01-08 revision located via DFA search 2026-10-27; line detail **needs-sources**).

## 3. Rates and base

| Item | Rate / base | Source |
|---|---|---|
| Corporate income tax | **needs-sources** (post-Act 719 rate; confirm on AR-1100 instructions) | arkleg unreachable this run |
| Base | federal taxable income with AR modifications (AR-1100ADJ) | DFA page / form list, read 2026-10-27 |
| Apportionment | UDITPA as amended; market-based sourcing for services/intangibles (Act 719) | DFA page, read 2026-10-27 |
| Pass-through entity tax | elective; rate **needs-sources** | DFA page (PET links), read 2026-10-27 |
| Minimum tax | **needs-sources** | — |

## 4. Deadlines

- **AR-1100:** follows the federal corporate due date (April 15 calendar-year) — confirm on instructions (**needs-sources**).
- **Estimated tax:** quarterly corporate estimates; percentage/safe-harbor **needs-sources**.
- **AR-1100S:** S-corp return follows the individual calendar (March 16 for 2026 calendar-year — confirm, **needs-sources**).

## 5. Penalties and interest

Arkansas penalty/interest under Ark. Code Ann. §26-18-403 et seq. — percentages **needs-sources**. Common failure modes: (1) ignoring the new **economic nexus threshold** for non-resident corporations/partnerships post-Act 719; (2) sourcing services/inintangibles by place-of-performance after 2025 instead of market (customer delivery) rules; (3) forgetting corporate (Sub-S) withholding obligations (see `ar-payroll-withholding`).

## 6. Cross-border interactions

- Market-based sourcing moves the numerator to the customer's location — see `ar-transfer-pricing` and `ar-cross-border`.
- Non-resident entity filing threshold created by Act 719 (amount **needs-sources**).
- Arkansas uses a **throwback** rule history for sales where the customer market is untaxed — confirm current status post-Act 719 (**needs-sources**).

## 7. Worked examples

A corporation with $1,500,000 Arkansas-apportionable income at an illustrative 1% post-reform rate (rate **needs-sources** — replace when confirmed):

```oa-check
name: AR corporate tax illustrative
inputs:
  apportioned: 1500000
  rate: 0.01
steps:
  - tax: apportioned * rate
expected:
  tax: 15000.00
```

Market-based sourcing of a services contract: $2,000,000 total service revenue, $800,000 delivered to Arkansas customers:

```oa-check
name: AR market sourcing services fraction
inputs:
  ar_market: 800000
  total: 2000000
  income: 1500000
steps:
  - factor: ar_market / total
  - apportioned: income * factor
expected:
  factor: 0.40
  apportioned: 600000.00
```

## 8. Ask the client

- Has the nexus model been re-run against the Act 719 economic-nexus threshold for non-resident entities?
- Are services/intangible revenues sourced to the customer-delivery location for post-2025 years?
- Is the entity considering the pass-through entity tax election — and what is the member-savings math?
- Confirm the current rate from the AR-1100 instructions before quoting figures to clients (this draft's rate is needs-sources).

## Sources

1. DFA Corporation Income Tax page: https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/ (200, text read 2026-10-27 — Act 719/SB 567 narrative, market-based sourcing, economic nexus, ATAP links)
2. DFA forms index (AR-1100, AR-1100ADJ, AR-1100S dated 2026-01-08): https://www.dfa.arkansas.gov/?s=corporate+income+tax+rate (search page read 2026-10-27)
3. Act 719 of 2025 PDF: https://www.arkleg.state.ar.us/Acts/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf (200 but 0 bytes from this host — rate text **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Arkansas corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
