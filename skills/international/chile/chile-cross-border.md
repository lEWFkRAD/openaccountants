---
name: chile-cross-border
description: >
  Chile cross-border tax reference for 2026. Covers the 35%
  additional withholding on dividends/remittances to non-residents
  with the 65% partial FCT credit under the partially integrated
  system (44.45% combined non-treaty ceiling), the treaty network
  including the Chile-US DTT in force since December 2023 (interest
  4/10, royalties 2/10), the Chilean Clause on dividend credits,
  branch remittance taxation, the 3-year source-only rule for new
  residents, the 15% flat on qualifying technical services from
  abroad, and the no-confirmed-exit-tax position. Trigger on Chile
  cross-border, non-resident, treaty, dividend chain, expat Chile.
  Source-cited draft.
jurisdiction: CL
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Chile cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the PwC Chile
corporate withholding chapter (last reviewed 19 December 2025 —
treaty table and the 44.45% formula), the PwC Chile personal-income
chapter (residence rules), and the PwC Chile corporate income chapter
(PIS mechanics). Treaty article details are **needs-sources** —
confirm each DTT text before applying a reduced rate.

## 2. Who the rules apply to

- **Non-resident shareholders** of Chilean companies: distributions
  bear the 35% 'additional' tax withheld at source, with the FCT paid
  by the company creditable against it — fully under the pro-Pyme
  (fully integrated) regime, **65% under the partially integrated
  system (PIS)** (PwC Chile corporate income, read 2026-10-24).
- **Non-resident recipients of Chilean-source interest, royalties and
  services**: WHT at 35% interest (4% for foreign-bank/financial-
  institution loans), 30% royalties (+15% additional on customised
  software), 35% services; treaty rates below.
- **Branches of foreign companies**: 35% WHT on amounts remitted or
  withdrawn, less the FCT credit (PwC Chile withholding, read
  2026-10-24).
- **New residents**: foreigners are taxed only on Chilean-source
  income for their first three years in Chile, then worldwide
  (PwC Chile personal income, read 2026-10-24). No confirmed exit tax
  on departure (**needs-sources**).

## 3. Withholding and treaty table

| Payment to non-resident | Rate | Source |
|---|---|---|
| Dividends / branch remittance | 35% additional, FCT creditable (65% under PIS) | PwC Chile withholding, read 2026-10-24 |
| Interest (general) | 35% | PwC Chile withholding, read 2026-10-24 |
| Interest — foreign bank/financial institution loans | 4% | PwC Chile withholding, read 2026-10-24 |
| Royalties | 30% (+15% additional on customised software) | PwC Chile withholding, read 2026-10-24 |
| Services performed in Chile | 35% | PwC Chile withholding, read 2026-10-24 |
| Technical/engineering services from abroad (report/advice/plan) | 15% flat | PwC Chile personal income, read 2026-10-24 |
| Treaty interest/royalties (examples) | US 4/10 interest, 2/10 royalties (in force 19 Dec 2023, WHT from 1 Feb 2024); Spain 5/15, 5/10; UK 4/10, 2/10; Brazil 15, 15 | PwC Chile treaty table, read 2026-10-24 — DTT texts **needs-sources** |

**Chilean Clause:** in all Chilean DTTs, Chile grants no reduction on
dividend WHT while the corporate tax remains fully creditable against
it — dividend chains are governed by domestic integration rules even
under treaties (PwC Chile withholding, read 2026-10-24).

## 4. Tax base and computation

The dividend chain for a PIS company: FCT 27% on the company's income,
then 35% additional on the distributed amount **grossed up by the FCT
paid**, with a credit of 65% of the FCT. Non-treaty combined burden =
27% + (35% − 65% × 27%) = **44.45%** (PwC Chile corporate income, read
2026-10-24). Treaty residents face the same additional-tax mechanics
(Chilean Clause) but the 65% vs 100% credit and reduced rates on
interest/royalties turn on the regime and treaty.

## 5. Deadlines

- Additional-tax WHT: monthly with the payer's Form 29/retention
  declaration (SII calendar — exact day **needs-sources**).
- Annual FCT/IGC returns: before 30 April (PwC Chile tax
  administration, read 2026-10-24).
- Treaty relief: certificate of residence filed with the SII before
  applying the reduced rate (procedure **needs-sources**).

## 6. Penalties and interest

Under-withheld additional tax: payer jointly liable, Art. 97 CT
penalties + promedio interest (percentages **needs-sources**).
Limitation: 3 years, 6 if no return/maliciously false (PwC Chile,
read 2026-10-24).

## 7. Worked examples

**Example 1 — PIS dividend chain to a non-treaty holder.** A PIS
company earns CLP 1,000,000 and distributes the after-FCT profit:
FCT 27%, then 35% additional on the gross-up with a 65% FCT credit —
combined 44.45%.

```oa-check
name: PIS dividend chain 44.45
inputs:
  profit: 1000000
  fct: 27
  additional: 35
  credit_pct: 65
steps:
  - fct_paid: profit * pct(1, fct)
  - distributed: profit - fct_paid
  - additional_gross: distributed + fct_paid
  - additional_tax: additional_gross * pct(1, additional)
  - credit: fct_paid * pct(1, credit_pct)
  - wht_net: additional_tax - credit
  - total: fct_paid + wht_net
expected:
  fct_paid: 270000.00
  distributed: 730000.00
  additional_gross: 1000000.00
  additional_tax: 350000.00
  credit: 175500.00
  wht_net: 174500.00
  total: 444500.00
```

**Example 2 — loan interest: foreign bank 4% vs general 35%.** CLP
500,000 of interest: a qualifying foreign-bank loan bears 4%; the
general rate is 35%.

```oa-check
name: interest bank 4 vs general 35
inputs:
  interest: 500000
  general: 35
  bank: 4
steps:
  - general_wht: interest * pct(1, general)
  - bank_wht: interest * pct(1, bank)
  - delta: general_wht - bank_wht
expected:
  general_wht: 175000.00
  bank_wht: 20000.00
  delta: 155000.00
```

## 8. Ask the client first

1. Is the paying Chilean company in the PIS (27%, 65% credit) or the
   pro-Pyme regime (25%, full credit) — the dividend chain changes?
2. Is the counterparty in a DTT state, and is the Chilean Clause
   understood (no dividend relief, but interest/royalty caps apply)?
3. Does foreign debt qualify for the 4% bank-loan rate, or is it
   related-party debt caught by thin capitalisation?
4. For incoming executives/engineers: are the first three years'
   source-only rules and the 15% technical-services flat being used
   correctly?

## 9. Sources

- [PwC — Chile withholding taxes](https://taxsummaries.pwc.com/chile/corporate/withholding-taxes) — read 2026-10-24 (last reviewed 2025-12-19; treaty table, Chilean Clause, branch WHT).
- [PwC — Chile taxes on corporate income](https://taxsummaries.pwc.com/chile/corporate/taxes-on-corporate-income) — read 2026-10-24 (PIS 44.45% formula).
- [PwC — Chile taxes on personal income](https://taxsummaries.pwc.com/chile/individual/taxes-on-personal-income) — read 2026-10-24 (3-year source rule, 15% flat).
- [PwC — Chile tax administration](https://taxsummaries.pwc.com/chile/corporate/tax-administration) — read 2026-10-24 (deadlines, limitation).
- DTT texts (US, Spain, UK, Brazil et al.), SII treaty procedure, Art. 97 CT percentages — **needs-sources**.

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
