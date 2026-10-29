---
name: ne-social-contributions
description: >
  Use this skill whenever asked about Nebraska employer social
  contributions for 2026 — unemployment insurance administered by the
  Nebraska Department of Labor (NDOL), quarterly wage and contribution
  reporting, and the FUTA/SUTA credit interaction. Trigger on "Nebraska
  unemployment", "NDOL", "Nebraska SUTA", "Nebraska employer
  contributions". Source-cited draft; NDOL administration verified via
  state portal 2026-10-28 (employer pages returned 403 to this run);
  wage base and rate tables needs-sources.
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

# Nebraska social contributions (employer side) v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## 1. Scope and sources

Employer social costs for Nebraska employment. **Source status:** the Nebraska state labor portal resolves and NDOL administers UI (verified at portal level 2026-10-28); **NDOL employer rate/wage-base pages returned HTTP 403 to this run's fetcher — all figures needs-sources**.

## 2. Who applies

Nebraska employers and out-of-state employers with Nebraska employees. No state disability, family-leave, or state-mandated retirement contribution for private employers beyond federal FICA/FUTA.

## 3. Rates and wage base

| Item | 2026 figure | Source status |
|---|---|---|
| NE UI taxable wage base | not fetched (403) | **needs-sources** |
| Experience rates | not fetched | **needs-sources** |
| New-employer rate | not fetched | **needs-sources** |
| FUTA (context) | 6.0% on first $7,000; credit up to 5.4% | federal standing rule |

## 4. Base and mechanics

Quarterly wage + contribution reports to NDOL (conventional form: "Report of Contributions and Wages" — confirm, **needs-sources**). Timely SUTA preserves the FUTA credit.

## 5. Deadlines, penalties, interest

Quarterly reports due last day of the month following each quarter (convention — **needs-sources** for NE specifics).

## 6. Cross-border notes

Multi-state: localize under the interstate coverage tests (**needs-sources**); Nebraska income-tax withholding is separate (`ne-payroll.md`).

## 7. Worked examples

**Example 1 — FUTA net per employee (federal context):**

```oa-check
name: FUTA net 0.6 percent
inputs:
  wage_base: 7000
  net_rate: 0.006
steps:
  - futa: wage_base * net_rate
expected:
  futa: 42.00
```

**Example 2 — illustrative NE UI (figures assumed, needs-sources).** Base $10,800, rate 1.2%:

```oa-check
name: NE UI illustrative
inputs:
  wage_base: 10800
  rate: 0.012
steps:
  - ui: wage_base * rate
expected:
  ui: 129.60
```

## 8. Ask the client

- NDOL account current and experience rate reviewed annually?
- Multi-state workforce — localization state confirmed?
- Successor-employer UI liability on acquisitions?

## 9. Sources

1. Nebraska labor portal: https://nebraska.gov/labor — resolves 2026-10-28; employer sub-pages 403 to fetcher.
2. Pre-existing `ne-income-tax.md` for the income-tax side.

**Needs-sources:** wage base, rate schedule, new-employer rate, form ID, due dates, penalties.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Nebraska payroll/social-cost questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
