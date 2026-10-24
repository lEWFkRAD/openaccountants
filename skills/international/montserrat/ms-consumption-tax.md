---
name: ms-consumption-tax
description: >
  Montserrat consumption tax reference for 2026. Montserrat has no VAT:
  the consumption domain is served by the single-stage Consumption Tax
  (ICT) under the Customs Duties and Consumption Tax Act (Cap. 17.05,
  1 January 2025 revision), collected at import alongside CARICOM Common
  External Tariff customs duties and at production for local
  manufacturers. Covers the rate structure (Schedule 1 ICD/ICT columns,
  CET bands 0–65%), the import valuation base (customs value plus duty),
  production-stage liability, export relief, and the Tax
  Administration Act interest and penalty regime. Trigger on Montserrat
  consumption tax, ICT, import duty Montserrat, CARICOM CET, octroi.
  Source-cited draft.
jurisdiction: MS
category: international
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-23
version: 0.1
---

# Montserrat consumption tax (no VAT)

## 1. Who this applies to

- Importers of goods into Montserrat for consumption in Montserrat — Consumption Tax is levied on all imported goods plus all goods manufactured or produced in Montserrat (Cap. 17.05 s.5(1)).
- Producers and manufacturers in Montserrat — liable at the time of production or manufacture (s.5(4)).
- There is no value-added tax, GST or sales tax in Montserrat. Anyone asking for a "Montserrat VAT return" is asking about the wrong regime: the consumption domain is a border/production excision-style tax administered by the Minister of Customs and Excise within the Montserrat Customs and Revenue Services (MCRS), not a periodic credit-and-declare VAT.

## 2. Rates (with sources)

Rates are item-specific and sit in the Montserrat Customs and Excise Tariff (Schedule 1 to Cap. 17.05): Column 3 carries the Import Customs Duty (ICD) and Column 5 the Consumption Tax (ICT). The published tariff is the CARICOM Common External Tariff schedule as applied by S.R.O. 27 of 2021; the extracted schedule shows the standard CET rate bands.

| Rate band (applies per HS item, ICD and ICT columns separately) | Typical use |
|---|---|
| 0% | Essentials, raw inputs |
| 5%, 10%, 15%, 20%, 25%, 30%, 35%, 40%, 50%, 60%, 65% | Graduated CET protection bands; e.g. beer ICT 15%, spirits ICT 30%, live animals ICD 0/40% |

- Rate authority: Cap. 17.05 s.3(2) (ICD = Schedule 1 Column 3) and s.5(2) (ICT = Schedule 1 Column 5). [Customs Duties and Consumption Tax Act, revision date 1 Jan 2025](https://legislation.gov.ms/wp-content/uploads/2026-02-17.05-Customs-Duties-and-Consumption-Tax-Act.pdf)
- Item-level rates: [Montserrat Customs Tariff (S.R.O. 27/2021, using 2017 HS codes)](https://mcrs.ms/wp-content/uploads/2022/08/Customs-2021-Tariff-Using-2017-HS-Code-SRO-27-of-2021.pdf) — the ICD/ICT two-column rate table was read from this PDF on 2026-10-23.

**Source status:** the Act and the tariff PDF resolve and were read 2026-10-23. The MCRS site publishes no separate "consumption tax rate" page; the MCRS 2024 Tax Tables cover PAYE withholding only. Item-by-item ICT rates must be read from the tariff PDF per HS code — do not quote a headline rate.

## 3. Tax base

- Imported goods: the value for Consumption Tax is the customs value assessed under Schedule 2 to the Customs (Control and Management) Act **plus the Customs Duty payable** (Cap. 17.05 s.6). ICT is therefore charged on a duty-inclusive base.
- Locally produced goods: payable by the producer or manufacturer at the time of production or manufacture, or as prescribed by the Governor in Council (s.5(4)).
- Exports relief: no Consumption Tax on goods manufactured or produced in Montserrat and exported (s.5(5)).
- Conditional duty and consumption tax exemptions exist under Schedule 2 (list of conditional exemptions reproduced in the tariff PDF).

## 4. Deadlines and mechanics

- Imported goods: ICT is payable by the importer at the time prescribed for payment of Customs Duties under the Customs (Control and Management) Act (s.5(3)) — i.e. at entry/clearance, not on a periodic return.
- Local production: at the time of production or manufacture (s.5(4)).
- There is no periodic consumption-tax return; obligations attach to customs entries and production events.

## 5. Penalties and interest

The Tax Administration Act (Cap. 17.26, 1 Jan 2025 revision) applies to "tax" broadly, including duties:

- Interest on underpayment: 6% simple per annum from the due date to payment (s.56–57); the Governor may vary the rate by Gazette Order.
- Late filing: greater of 5% of tax owing + 1%/month, or $500 + $100/month, capped at $100 (within 1 month), $1,000 (within 6 months) or $10,000 otherwise (s.58); reasonable-cause relief available.
- Late payment: 5% late-payment fee on the unpaid amount (s.59).
- A tax lien arises at midnight after the due date over all property of the taxpayer (s.64).

[Tax Administration Act (Cap. 17.26)](https://legislation.gov.ms/wp-content/uploads/2026-02-17.26-Tax-Administration-Act.pdf)

## 6. Cross-border notes

- Goods from CARICOM Member States (Schedule 3 list) may qualify for Common Market duty rates; origin rules are in Cap. 17.05 ss.11–14.
- No VAT registration, reverse charge or import-VAT mechanism exists; cross-border services are outside this tax entirely (it is a goods tax).
- Duty-free licensing exists (s.22) for approved outlets.

## 7. Worked examples

**Example 1 — imported goods, ICT on a duty-inclusive base.** An importer brings in goods with a customs value of XCD 100,000. The item carries ICD 5% and ICT 15%.

```oa-check
name: ICT on duty-inclusive customs value
inputs:
  customs_value: 100000
  icd_rate: 0.05
  ict_rate: 0.15
steps:
  - icd: customs_value * icd_rate
  - ict_base: customs_value + icd
  - ict: ict_base * ict_rate
expected:
  icd: 5000
  ict_base: 105000
  ict: 15750
```

Total border tax XCD 20,750; landed cost before margin XCD 120,750.

**Example 2 — spirits import.** CIF XCD 20,000, ICD 10%, ICT 20%:

```oa-check
name: spirits import ICT
inputs:
  cif: 20000
  icd_rate: 0.10
  ict_rate: 0.20
steps:
  - icd: cif * icd_rate
  - ict_base: cif + icd
  - ict: ict_base * ict_rate
expected:
  icd: 2000
  ict_base: 22000
  ict: 4400
```

## 8. Ask the client

- Exact HS classification of each good — the ICT rate is item-specific and misclassification changes both ICD and ICT.
- Whether goods are for re-export (s.5(5) relief) or enter a duty-free/conditional-exemption scheme (Schedule 2).
- CARICOM origin documentation if claiming Community rates.
- Whether the goods are petroleum products (adjustment levy, s.10).

## 9. Sources

- [Customs Duties and Consumption Tax Act, Cap. 17.05 (1 Jan 2025 revision)](https://legislation.gov.ms/wp-content/uploads/2026-02-17.05-Customs-Duties-and-Consumption-Tax-Act.pdf) — read 2026-10-23.
- [Montserrat Customs Tariff, S.R.O. 27 of 2021 (2017 HS)](https://mcrs.ms/wp-content/uploads/2022/08/Customs-2021-Tariff-Using-2017-HS-Code-SRO-27-of-2021.pdf) — read 2026-10-23 (ICD/ICT columns, conditional exemption list).
- [Tax Administration Act, Cap. 17.26 (1 Jan 2025 revision)](https://legislation.gov.ms/wp-content/uploads/2026-02-17.26-Tax-Administration-Act.pdf) — read 2026-10-23 (interest, penalties).
- [MCRS customs legislation page](https://mcrs.ms/customs-legislation/) — read 2026-10-23.
- [MCRS 2024 Tax Tables](https://mcrs.ms/2024-tax-tables/) — read 2026-10-23 (PAYE only; confirms no consumption-tax rate page).

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
