---
name: dc-franchise-tax
description: >
  Use this skill whenever asked about District of Columbia franchise
  tax for tax year 2026 — the 8.25% corporate and unincorporated
  business franchise tax, mandatory combined reporting for unitary
  groups, the $250/$1,000 minimum taxes, the 30% owner salary
  allowance and $5,000 exemption for unincorporated businesses, the
  personal-services exemption, estimated tax (D-20ES/D-30ES, 110%
  safe harbor), and D-22/D-30 return mechanics. Trigger on "DC
  franchise tax", "District of Columbia corporate tax", "DC 8.25
  percent", "DC combined reporting", "DC D-20", "DC D-30", "DC
  minimum franchise tax". Source-cited draft; OTR rates, combined
  reporting, and estimated-tax pages read 2026-10-27.
jurisdiction: US-DC
category: corporate
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - dc-income-tax
---

# District of Columbia franchise tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. The District's business income tax is the **franchise tax**: **8.25%** of DC-computed net income for corporations and for unincorporated businesses, computed on a **combined-reporting basis** for unitary groups (rate table 2018–2025 and the combined-reporting mandate read from the OTR Business Franchise Tax Rates page and the Combined Reporting page, fetched 2026-10-27). **Source status:** the 8.25% rate (2018–2025 table), the $250/$1,000 minimum taxes, the unincorporated-business rules (gross receipts > $12,000 filing trigger, 30% owner salary allowance, $5,000 exemption, personal-services exemption), the combined-reporting rule (TYB ≥ 2011-01-01), and the estimated-tax regime (>$1,000 trigger; 4/15·6/15·9/15·12/15; 110%-prior-year safe harbor; D-20ES/D-30ES/D-2210/D-2220) are all read from OTR pages. The 2026 rate is not yet printed in OTR's table — **needs-sources** (8.25% assumed from the 2018–2025 run). Return-form line detail (D-20/D-30) not extracted — **needs-sources**.

## 2. Who applies

- **Corporations** (including financial institutions) with DC-source income, filing on a combined basis for unitary groups (OTR pages, read 2026-10-27). Corporations/financial institutions cannot escape the minimum tax even with exempt business income (note read from the OTR rates page).
- **Unincorporated businesses** (partnerships, LLCs, sole proprietorships) with DC gross receipts over **$12,000** (OTR rates page, read 2026-10-27).
- **Exemption:** an unincorporated business is exempt where more than 80% of gross income is personal services rendered by members and capital is not a material income-producing factor; also entities that by law/customs/ethics cannot incorporate (OTR rates page, read 2026-10-27) — a critical rule for professional practices.

## 3. Rates and base

| Item | Rate / base | Source |
|---|---|---|
| Corporate franchise tax | **8.25%** (table shows 2018–2025; 2026 needs-sources) | OTR rates page, read 2026-10-27 |
| Unincorporated franchise tax | **8.25%** (same table) | OTR rates page, read 2026-10-27 |
| Minimum tax | **$250** (DC gross receipts ≤ $1M) / **$1,000** (> $1M) | OTR rates page, read 2026-10-27 |
| Unincorporated deductions | 30% owner salary allowance + $5,000 exemption | OTR rates page, read 2026-10-27 |
| Filing trigger (unincorporated) | DC gross receipts > $12,000 | OTR rates page, read 2026-10-27 |
| Base | DC-computed net income on combined-reporting basis | OTR combined reporting page, read 2026-10-27 |

## 4. Deadlines

- **Returns:** D-20 (corporate) / D-30 (unincorporated) follow the federal calendar (April 15 individual-based, corporate per federal date) — form-level confirmation **needs-sources**.
- **Estimated tax:** required when liability > **$1,000**; calendar-year filers pay **April 15, June 15, September 15, December 15**; fiscal filers on months 4/6/9/12 (OTR Estimated Tax page, read 2026-10-27).
- **Safe harbor:** no underpayment interest when current-year liability < $1,000, prior-year liability was zero, payments ≥ **110% of prior year**, or remaining due < 10% of liability (OTR page, read 2026-10-27). Annualization via D-2220 (OTR page, read 2026-10-27).

## 5. Penalties and interest

Underpayment-of-estimated interest computed on D-2210 (individuals) / D-2220 (business annualization) — OTR page, read 2026-10-27; statutory penalty percentages under DC Code §47-1801.02 et seq. — **needs-sources**. Common failure modes: (1) professional LLCs assuming the individual return covers everything — the unincorporated franchise tax applies unless the 80% personal-services exemption is documented; (2) forgetting the owner-salary allowance when computing the base; (3) 100%-of-prior-year accruals when DC's safe harbor is **110%**; (4) minimum tax missed by exempt-income corporations.

## 6. Cross-border interactions

- Combined reporting pulls out-of-District unitary affiliates into the DC computation (see `dc-transfer-pricing`).
- DC sources income under DC Code Title 47 ch. 18 subch. II (apportionment — single-sales-factor history: confirm, **needs-sources**).
- No DC exit tax regime for entities; non-resident entity taxation runs through DC-source combined income (see `dc-cross-border`).

## 7. Worked examples

An unincorporated business with $200,000 DC net income (gross receipts well over $12,000, no personal-services exemption):

```oa-check
name: DC unincorporated franchise tax with salary allowance
inputs:
  net_income: 200000
  salary_pct: 0.30
  exemption: 5000
  rate: 0.0825
steps:
  - salary_allowance: net_income * salary_pct
  - base: net_income - salary_allowance - exemption
  - tax: base * rate
expected:
  salary_allowance: 60000.00
  base: 135000.00
  tax: 11137.50
```

A corporation with $1,000,000 DC-apportioned combined net income:

```oa-check
name: DC corporate franchise tax
inputs:
  base: 1000000
  rate: 0.0825
steps:
  - tax: base * rate
  - min_check: max(tax, 1000)
expected:
  tax: 82500.00
  min_check: 82500.00
```

## 8. Ask the client

- Does the entity qualify for the 80% personal-services exemption — is the capital-not-material test documented?
- Are estimated payments tracking the 110% safe harbor (not 100%)?
- Is the owner-salary allowance being claimed correctly on the D-30?
- Part of a unitary group? The combined report is mandatory — see `dc-transfer-pricing`.

## Sources

1. OTR Business Franchise Tax Rates: https://otr.cfo.dc.gov/page/dc-business-franchise-tax-rates (200, text read 2026-10-27 — 8.25% table, minimums, unincorporated rules, exemptions)
2. OTR Combined Reporting: https://otr.cfo.dc.gov/page/combined-reporting-business-entities (200, text read 2026-10-27 — mandatory combination TYB ≥ 2011)
3. OTR Estimated Tax Requirement: https://otr.cfo.dc.gov/page/underpayment-estimated-tax-interest (200, text read 2026-10-27 — thresholds, dates, safe harbor, forms)
4. DC Code Title 47 ch. 18: https://code.dccouncil.gov/us/dc/council/code/titles/47/chapters/18/ (200; section text not extracted — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for DC franchise tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
