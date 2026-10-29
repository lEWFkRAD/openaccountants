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

## Scope and sources

Employer social costs for Nebraska employment. **Source status:** the Nebraska state labor portal resolves and NDOL administers UI (verified at portal level 2026-10-28); **NDOL employer rate/wage-base pages returned HTTP 403 to this run's fetcher — all figures needs-sources**.

## Who this applies to

Nebraska employers and out-of-state employers with Nebraska employees. No state disability, family-leave, or state-mandated retirement contribution for private employers beyond federal FICA/FUTA.

## Rates, bands and thresholds

| Item | 2026 figure | Source |
|---|---|---|
| NE UI taxable wage base | see Not yet confirmed (NDOL pages returned 403 to this run's fetcher) | — |
| Experience rates | see Not yet confirmed | — |
| New-employer rate | see Not yet confirmed | — |
| FUTA (context) | 6.0% on first $7,000; credit up to 5.4% | federal standing rule (IRC §3301/§3302) |

## The taxable base

Quarterly wage + contribution reports to NDOL (the NE form ID is listed under Not yet confirmed). Timely SUTA payment preserves the FUTA credit (IRC §3302).

## Deadlines and filing

Quarterly reports due last day of the month following each quarter (convention — **needs-sources** for NE specifics).

## Cross-border points

Multi-state employers localize under the interstate coverage tests (45 CFR Part 6, FUTA conformity); Nebraska income-tax withholding is separate (`ne-payroll.md`).

## Worked examples

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

**Example 2 — hypothetical NE UI (figures hypothetical; NE wage base/rate pending confirmation).** Base $10,800, rate 1.2%:

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

## Ask the client first

- NDOL account current and experience rate reviewed annually?
- Multi-state workforce — localization state confirmed?
- Successor-employer UI liability on acquisitions?

## 9. Sources

## Sources

| Source | URL | Read on |
|---|---|---|
| Nebraska state labor portal (NDOL administers UI; employer sub-pages returned 403 to this run's fetcher) | https://nebraska.gov/labor | 2026-10-28 |

Not yet confirmed: the Nebraska UI taxable wage base, experience-rate schedule, new-employer rate, quarterly report form ID, report due dates, and late-filing/late-payment penalties (NDOL employer pages returned HTTP 403 to this run's fetcher); interstate localization specifics.

<!-- openaccountants-cta-block -->
---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network
