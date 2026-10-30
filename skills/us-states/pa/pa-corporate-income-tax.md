---
name: pa-corporate-income-tax
description: >
  Use this skill whenever asked about Pennsylvania corporate income tax for
  tax year 2026 -- the Corporate Net Income Tax (CNIT), Act of March 4, 1971
  (an uncodified session law: 72 P.S. §§ 7401–7518), a flat income tax on C
  corporations on a phase-down from 9.99% under Act 53 of 2022; the capital
  stock/franchise tax repealed effective 2017 and the margins tax expired
  2016; combined (unitary) vs non-combined RCT-1 filing; 8.99%/7.49%/6.49%
  historic steps with the 2026 rate flagged not yet confirmed; P.L. 86-272
  applies to the CNIT; S corporations and most pass-throughs pay nothing at
  entity level (owners taxed at 3.07%). Trigger on "Pennsylvania corporate
  income tax", "PA CNIT", "corporate net income tax", "RCT-1", "PA combined
  return", "Pennsylvania corporate tax rate", "PA margins tax", "PA capital
  stock tax", "unitary combined Pennsylvania".
  Source-cited draft; CNIT statute is uncodified and the RCT-1 instructions
  PDF 404s on every probed path as of 2026-10-27 -- the rate schedule is
  not yet confirmed, corroborated only by the tier-2 mn-corporate-and-pte skill.
jurisdiction: US-PA
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - pa-income-tax
  - pa-transfer-pricing
---

# Pennsylvania corporate income tax (CNIT) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Pennsylvania professional.

## Who this applies to

Pennsylvania taxes C corporations with the **Corporate Net Income Tax (CNIT)** -- the Act of March 4, 1971, P.L. 67, as amended (72 P.S. §§ 7401–7518). It is a **flat rate on apportioned taxable income**, on a statutory **phase-down from 9.99%** enacted by Act 53 of 2022. The **capital stock/franchise tax was repealed** effective January 1, 2017, and the temporary **margins tax expired** after 2016. Pass-through entities (S corps, partnerships, LLCs, sole proprietors) pay **no entity-level CNIT** -- owners pay the 3.07% PIT (`pa-income-tax`).

**Source status (as_of 2026-10-27):** the CNIT is an **uncodified session law**, so legis.state.pa.us USC section pages 404 (probed 2026-10-27); the Department CNIT pages (revenue.pa.gov and pa.gov variants) return HTTP 200 but are JavaScript-rendered shells with no extractable figures; the **RCT-1 instructions PDF 404s on every probed path**. The 9.99% historic rate and the phase-down-to-4.99% schedule are corroborated **only** by the tier-2 `mn-corporate-and-pte` skill (read 2026-07-13: "Pennsylvania historically at 9.99% … on a phase-down schedule to 4.99%"). **The exact 2026 rate is not yet confirmed -- do not file on the figure below without checking the current RCT-1.**

### 2. Who applies

- **C corporations** (including banks and insurance companies under separate articles) with nexus to Pennsylvania.
- **Nexus:** the CNIT is an income tax, so **P.L. 86-272 protects** purely solicitation-of-sales activities in PA (unlike Ohio's CAT). Physical presence, property, payroll or sales beyond solicitation creates nexus.
- **S corporations:** no CNIT on ordinary income (PA recognizes the federal S election); note the PA addback history and the Ohio-shareholder wage rule in `pa-cross-border`.
- **Combined filers:** a **unitary group** that elects (or is required, for certain affiliated groups) to file a **combined** RCT-1 -- see `pa-transfer-pricing`.
- Exempt organizations under the CNIT article must still file informational returns in some cases -- not yet confirmed.

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| CNIT rate (historic) | **9.99%** flat | `mn-corporate-and-pte` (tier 2, 2026-07-13) | (not yet confirmed)
| CNIT phase-down | Act 53 of 2022 steps the rate down toward **4.99%**; commonly cited steps 8.99% (2023), 7.49% (2024), 6.49% (2025) -- **2026 rate not yet confirmed** | Act 53 text not retrievable 2026-10-27 (all probed paths 404) -- **not yet confirmed** |
| Base | Federal taxable income with PA modifications, **apportioned** (single sales factor since 2014 -- not yet confirmed re-verify) | not yet confirmed (RCT-1 not read) |
| Capital stock / franchise tax | **Repealed** effective 2017 | `pa-income-tax` README note; not yet confirmed for the repealer cite |
| Margins tax | 0.99% of PA gross receipts -- **expired** after 2016 | not yet confirmed |
| Pass-throughs | No entity-level CNIT; owners at 3.07% PIT | `pa-income-tax` (2026 REV-413 read 2026-09-25) | (not yet confirmed)
| P.L. 86-272 | Applies (income tax) | federal statute; PA administrative practice not yet confirmed |

### 4. Deadlines

| Filing | Due |
|---|---|
| RCT-1 (calendar-year C corp) | **April 15**; extension to October 15 on request (RCT-1071) -- not yet confirmed re-verify |
| RCT-1 quarterly estimates | Four installments: June 15, September 15, December 15, following March 15 -- not yet confirmed |
| Combined election | With the combined return for the year -- see `pa-transfer-pricing` |
| RCT-99 net loss carryforward schedule | With the RCT-1 |

Quarter dates follow the standard PA corporate pattern but the RCT-1 instructions were not retrievable this run -- **not yet confirmed**.

### 5. Penalties and interest

- Late filing/payment: PA charges a **5% non-filing penalty** plus **0.5% per month** (max 25%) and monthly underpayment interest -- exact 2026 interest rate **not yet confirmed** (72 P.S. § 7205 not read this run).
- Underpayment of estimated tax: interest on the shortfall per quarter.
- PA has a voluntary disclosure program (VDPA) for unregistered CNIT filers -- not yet confirmed.

### 6. Cross-border

- **P.L. 86-272 shelter** for solicitation-only out-of-state and foreign corporations -- the key difference from Ohio's CAT (`oh-corporate-income-tax`).
- **Apportionment:** sales are the single factor (post-2014 uniformity act -- not yet confirmed); market-based sourcing for services -- not yet confirmed.
- **Unitary combined reporting** can pull foreign affiliates into the group -- see `pa-transfer-pricing`.
- Foreign-filed states' taxes on PA-source income interact with the corporate credit -- not yet confirmed.

### 7. Worked examples

**Example A -- hypothetical CNIT at a cited step rate (verify the 2026 rate first).**

```oa-check
name: CNIT on 2,000,000 PA-apportioned income at 6.49%
inputs:
  pa_income: 2000000
  rate: 0.0649
steps:
  - cnit: pa_income * rate
expected:
  cnit: 129800.00
```

The 6.49% is the commonly cited 2025 step -- **not yet confirmed for 2026**; substitute the current RCT-1 rate before relying on the total.

**Example B -- estimate installment split.**

```oa-check
name: Quarterly estimate installments on 129,800 CNIT
inputs:
  annual_tax: 129800
  installments: 4
steps:
  - each: annual_tax / installments
expected:
  each: 32450.00
```

### 8. Ask the client

- Entity type: C corp, S corp, or disregarded -- the CNIT reaches only C corps (and insurers/banks separately).
- PA-apportioned sales and whether activities are pure solicitation (P.L. 86-272).
- Is the group **unitary**? Has a combined RCT-1 election been made? (`pa-transfer-pricing`)
- NOLs and RCT-99 carryforwards -- PA NOL rules diverge from federal.
- Which rate step applies to the tax year -- **confirm against the current RCT-1 before computing**.
- Any prior PA exposure: consider the VDPA before registering.

### 9. Sources

- [PA Department of Revenue CNIT page](https://www.revenue.pa.gov/Businesses/Taxes/CorporateNetIncomeTax.aspx) -- HTTP 200 2026-10-27, JS-rendered shell (no figures extractable)
- [DLI UC yearly tax highlights](https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/yearly-tax-highlights) -- HTTP 200 2026-10-27 (read for SC, not CNIT)
- `mn-corporate-and-pte` (tier 2, read 2026-07-13) -- corroborates 9.99% historic and phase-down to 4.99% (not yet confirmed)
- `pa-income-tax` (tier 2) -- 3.07% PIT for pass-through owners (not yet confirmed)
- **not yet confirmed:** 2026 CNIT rate (Act 53 schedule -- RCT-1 instructions PDF 404 on all probed paths 2026-10-27); apportionment factor rules; RCT-1 deadline/estimate calendar; 72 P.S. § 7205 penalty and interest rates; VDPA.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Pennsylvania CNIT questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

## Rates, bands and thresholds

Not yet confirmed against archived sources.

## The taxable base

Not yet confirmed against archived sources.

## Deadlines and filing

Not yet confirmed against archived sources.

## Penalties and interest

Not yet confirmed against archived sources.

## Cross-border points

Not yet confirmed against archived sources.

## Worked examples

Not yet confirmed against archived sources.

## Ask the client first

Not yet confirmed against archived sources.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.


| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | -- | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
