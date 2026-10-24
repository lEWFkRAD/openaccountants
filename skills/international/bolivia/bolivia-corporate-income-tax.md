---
name: bolivia-corporate-income-tax
description: >
  Bolivia corporate income tax (IUE) reference for 2026. Covers the
  25% IUE on Bolivian-source income under the territorial source
  principle, the 3% monthly transaction tax (IT) collected as an
  advance against IUE, the 25% additional tax on financial and
  insurance companies with return on equity above 6%, the 25%
  extractives surtax and 12.5%/7.5% mining taxes, fiscal-year
  calendars by sector, the 120-day return deadline, SIN audit
  procedure and the four-year statute of limitations. Trigger on
  Bolivia corporate tax, IUE, impuesto sobre las utilidades,
  transaction tax, IT 3%. Source-cited draft.
jurisdiction: BO
category: corporate
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Bolivia corporate income tax (IUE)

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the SIN portal
(impuestos.gob.bo, SIAT) and the PwC Worldwide Tax Summaries Bolivia
corporate chapter (last reviewed 21 July 2026). Currency: boliviano
(BOB). The governing statute is the Ley 843 Codigo Tributario (IUE)
with the Ley 2492 Codigo Tributario (procedure); article-level
citations are **needs-sources** this pass (the official gazette did not
resolve).

## 2. Who the rules apply to

- **All companies (resident or foreign)** earning Bolivian-source
  income: Bolivia taxes by **source**, not residence — income from
  goods/assets located or economically used in Bolivia and from
  activities carried out in Bolivia is taxable regardless of the
  parties' nationality or where contracts were signed.
- **Financial institutions** (except development banks) and
  **insurance/reinsurance companies** additionally face the DIT
  (additional income tax) when return on equity exceeds 6%.
- **Extractive companies** (mining, oil and gas) face the extractives
  surtax and, for mining, the PAT and royalties.
- Branches of foreign companies are taxed like residents on
  Bolivian-source income; profit remittances to the head office suffer
  the 12.5% dividend-equivalent withholding (see
  bolivia-cross-border).

## 3. Rates table

| Tax | Rate | Base | Source |
|---|---|---|---|
| IUE (corporate income tax) | 25% | Bolivian-source net income per Bolivian GAAP adjusted for tax | Ley 843 via PwC Bolivia, read 2026-10-24 |
| IT (transaction tax) | 3% | Monthly gross revenue from economic/commercial activity | PwC Bolivia, read 2026-10-24 |
| DIT (financial institutions/insurers) | 25% additional | Net profit when ROE > 6% | PwC Bolivia, read 2026-10-24 |
| Extractives surtax | 25% additional | Same base as IUE with extra deductions (33% accumulated investment cap, 45% gross-revenue deduction, BOB 250m threshold per operation) | PwC Bolivia, read 2026-10-24 |
| PAT mining — exploitation | 12.5% | Taxable net profits | PwC Bolivia, read 2026-10-24 |
| PAT mining — manufacturing with raw minerals | 7.5% | Taxable net profits | PwC Bolivia, read 2026-10-24 |
| Mining royalty | 1%–7% | Total sales price (60% discount on domestic sales) | PwC Bolivia, read 2026-10-24 |

The IT is an **advance** against IUE: the annual IUE paid is credited
against the monthly IT for the following 12 months, and the taxpayer
effectively pays whichever is higher. There are no departmental or
local income taxes.

## 4. Tax base and computation

IUE base = accounting profit per Bolivian GAAP, adjusted for
non-deductible and non-taxable items. Key mechanics:

- Deductions must be necessary to generate/maintain Bolivian-source
  income and be evidenced by fiscal documentation (factura).
- Payments to related parties without substance/evidence are the main
  audit exposure (see bolivia-transfer-pricing).
- Losses: carry-forward of Bolivian-source losses is allowed (limit
  and period: **needs-sources** — confirm against Ley 843 and SIN
  normative resolutions before relying).
- The DIT is not deductible for IUE and cannot be offset against IT.

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| Fiscal year-end | 31 Dec banks/services; 31 Mar industrial/oil/gas; 30 Jun agro/forestry; 30 Sep mining | PwC Bolivia, read 2026-10-24 |
| IUE return + balance payment | 120 days after fiscal year-end | PwC Bolivia, read 2026-10-24 |
| IT (transaction tax) | Monthly (SIN vencimientos calendar) | PwC Bolivia, read 2026-10-24 |
| Mining additional-tax advances | Monthly | PwC Bolivia, read 2026-10-24 |

Exact day-of-month calendars are published by SIN each year (SIAT
portal) — confirm the current vencimiento calendar before filing.

## 6. Penalties and interest

Under the Ley 2492 Codigo Tributario: unpaid tax accrues indexed
updatings plus interest (rates set by SIN resolutions — exact current
rates **needs-sources**), and infractions draw proportional penalties
(percentage of the tax owed; article numbers **needs-sources**). Audit
process: formal notification, inspection up to ~12 months, preliminary
report, 30 days for the taxpayer's defence, 60 days for the final
report; taxes must be paid to litigate in court (PwC Bolivia, read
2026-10-24). Statute of limitations: 4 years from 1 January after the
payment due date, extendable by 2 years for improper registration
(Ley 1733 amending art. 59 Codigo Tributario, per PwC Bolivia).

## 7. Worked examples

**Example 1 — CIT vs transaction tax.** A Bolivian trading company has
BOB 1,000,000 net profit on BOB 10,000,000 gross revenue. IUE is 25% of
profit; IT is 3% of gross; the annual burden is the higher of the two.

```oa-check
name: IUE vs IT higher-of
inputs:
  profit: 1000000
  revenue: 10000000
  iue_rate: 25
  it_rate: 3
steps:
  - iue: profit * pct(1, iue_rate)
  - it: revenue * pct(1, it_rate)
  - due: max(iue, it)
expected:
  iue: 250000.00
  it: 300000.00
  due: 300000.00
```

**Example 2 — financial institution DIT.** A bank with BOB 2,000,000
net profit and return on equity above 6% pays the 25% IUE plus the 25%
additional DIT on the same base.

```oa-check
name: bank IUE plus DIT
inputs:
  net_profit: 2000000
  rate: 25
steps:
  - iue: net_profit * pct(1, rate)
  - dit: net_profit * pct(1, rate)
  - total: iue + dit
expected:
  iue: 500000.00
  dit: 500000.00
  total: 1000000.00
```

## 8. Ask the client first

1. What is the fiscal year-end for the activity, and is the 120-day
   IUE filing calendar being tracked in SIAT?
2. Is cumulative monthly IT exceeding the IUE advance — i.e. is the
   company actually paying IT month by month?
3. Is the entity a financial institution/insurer (ROE test for DIT) or
   extractive (surtax, PAT, royalty registration)?
4. Are related-party charges (management fees, interest, purchases
   from affiliates) evidenced and priced defensibly?

## 9. Sources

- [SIN — Servicio de Impuestos Nacionales](https://www.impuestos.gob.bo/) — read 2026-10-24.
- [SIN — SIAT](https://siat.impuestos.gob.bo/) — read 2026-10-24.
- [PwC — Bolivia taxes on corporate income](https://taxsummaries.pwc.com/bolivia/corporate/taxes-on-corporate-income) — read 2026-10-24 (last reviewed 2026-07-21).
- [PwC — Bolivia tax administration](https://taxsummaries.pwc.com/bolivia/corporate/tax-administration) — read 2026-10-24 (deadlines, audit, limitation period).
- Ley 843 and Ley 2492 article texts — **needs-sources** (gazette unreachable 2026-10-24).

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
