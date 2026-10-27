---
name: pr-vat-ivu
description: >
  Puerto Rico sales and use tax (IVU) reference for 2026. Covers the 6% state IVU on taxable retail sales plus the 0.5% municipal IVU (Code 1-2011 sections 4020.01, 4020.02, 4020.10, read from the OGP May 2026 revision), use tax on imports, remittance timing under section 4042.03, and the special-rate schedule flagged needs-sources. Trigger on Puerto Rico IVU, sales tax PR, use tax, impuesto sobre ventas, municipal sales tax. Source-cited draft.
jurisdiction: PR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Puerto Rico IVU (sales and use tax)

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: the OGP official
consolidated PDF of the Código de Rentas Internas de Puerto Rico de 2011
(Ley 1-2011, revision stamp 28 May 2026) was read directly; §§4020.01,
4020.02, 4020.10, 4042.01-4042.03 are quoted from that text. The special
IVU rates introduced by Ley 110-2020 and later amendments are not in the
sections read and are needs-sources.

## 2. Who applies

Every "comerciante" (merchant) making retail sales of tangible personal
property (and enumerated services) in Puerto Rico collects IVU; importers
and users owe the complementary use tax (§4020.02, read). Non-resident
and remote sellers register with Hacienda; the municipal 0.5% is
collected by the Secretary as agent for municipalities (§4020.10, read).

## 3. Rates

| Item | Rate | Source |
|---|---|---|
| State IVU on taxable sales | 6% | Code §4020.01(b) (read 2026-10-27) |
| Municipal IVU | 0.5% | Code §4020.10 (read 2026-10-27) |
| Use tax on imports | same rates, due before taking possession (general rule) | Code §4042.03(a)(1) (read) |
| Special rates (hotels, motor vehicles, professional services, etc.) | varies | Ley 110-2020 / later — needs-sources |

The Code text read carries the 6% state rate effective 1 February 2014
plus the 0.5% municipal rate; the post-2020 special-rate schedule must be
confirmed against Hacienda's current IVU page before quoting anything
other than 6% + 0.5%.

## 4. Base and timing

Taxable base is the retail sales price of "partida tributable" (tangible
personal property and enumerated services) in Puerto Rico, subject to the
Chapter 3 exemptions (§4020.01(a), read). Combined transactions (property
plus service) are taxed on the combined price. Use tax applies to
property brought into PR, generally paid before the importer takes
possession, with a 10th-of-following-month route for bonded/bonded-class
merchants (§4042.03(a)(1), read).

## 5. Deadlines and filings

| Obligation | Deadline | Source |
|---|---|---|
| IVU return and remittance to the Secretary | per §4042.03 schedule (monthly for most merchants; current administrative calendar needs-sources) | Code §§4042.01-4042.03 (read) |
| Use tax on imports | before possession (general rule); otherwise by the 10th of the following month | §4042.03(a)(1) (read) |

## 6. Penalties and interest

The IVU subtitle carries its own penalty provisions; the general
interest rule is 10% annually on deficiencies and unpaid amounts
(§6030.01, §6030.02, read) and failure-to-file adds 5% within 30 days
plus 10% per additional 30-day period (§6030.11, read). IVU-specific
penalty amounts: needs-sources.

## 7. Cross-border interactions

PR sits outside the US federal sales-tax world (the US has none) but
inside the US customs regime for most purposes; imported goods pay the
use tax at IVU rates at entry (§4042.03, read). Services exported from
PR and goods shipped to the US mainland are not PR retail sales; goods
shipped from the mainland by non-registered sellers trigger the
registration/use-tax net.

## 8. Worked examples

A San Juan retailer sells USD 2,000 of taxable goods, including the
municipal component:

```oa-check
name: IVU on a 2000 dollar sale including municipal tax
inputs:
  precio: 2000
  estatal: 0.06
  municipal: 0.005
steps:
  - impuesto_estatal: precio * estatal
  - impuesto_municipal: precio * municipal
  - total: precio * (estatal + municipal)
expected:
  impuesto_estatal: 120.00
  impuesto_municipal: 10.00
  total: 130.00
```

A merchant imports taxable property and is a bonded merchant ("comerciante
afianzado"): use tax is payable by the 10th of the month following
introduction rather than before possession (§4042.03(a)(1)(B), read) —
same rate base as the example above.

## 9. Ask the client / sources

Ask: Is the client registered for IVU and municipal IVU with Hacienda?
Are exempt items (unprepared food, prescription drugs, professional
services under current law) coded correctly? Are imports self-assessing
use tax at entry? Which special-rate category applies to the client's
line items (needs-sources schedule)?

Sources: OGP consolidated Code PDF (read 2026-10-27); Hacienda IVU page
(read 2026-10-27). Needs-sources: current special-rate schedule (Ley
110-2020 and later), administrative filing calendar and form numbers,
IVU-specific penalty amounts.

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
