---
name: bm-transfer-pricing
description: >
  Bermuda transfer pricing reference for 2026. Covers the arm's-length
  principle and intra-group transaction adjustments in the Corporate Income
  Tax Act 2023 (Part 6, transfer pricing requirements), which apply only to
  Bermuda constituent entities of in-scope MNE groups (EUR 750 million
  threshold), the consolidated-treatment election for transactions between
  Bermuda constituent entities, country-by-country reporting administered by
  the Corporate Income Tax Agency, and the Pillar Two design of the CIT
  itself. Trigger on Bermuda transfer pricing, arm's length, in-scope MNE,
  CbCR, GloBE, CITA. Source-cited draft.
jurisdiction: BM
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: "0.2"
verified_by: pending
---

# Bermuda transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the consolidated full text
of the Corporate Income Tax Act 2023 (PDF published by the Corporate Income
Tax Agency, all amendments consolidated as of 13 September 2026), the CITA
technical-references pages (legislation and guidance lists), and the gov.bm
CIT pages. Currency for CIT computation is the entity's financial-accounting
currency, converted under section 47 where required.

**Source status caveat:** CITA's guidance documents (CIT Guidance Notes,
Group Management Functionality Guidance, Allocation of Taxes Between
Constituent Entities) are posted as items on a JavaScript-rendered page;
their PDF bodies were not read in this pass, and the CbCR page renders no
server-side text. CbCR filing thresholds and deadlines are therefore
**needs-sources** — confirm against the CITA CbCR page and the Corporate
Income Tax (Administrative) Regulations 2025 before tier-1 promotion.

## 2. Who the rules apply to

Bermuda's transfer-pricing rules live inside the Corporate Income Tax Act
2023 and bite only where the CIT itself bites:

- **In-scope MNE groups only.** The CIT (and with it the transfer pricing
  requirements) applies to Bermuda constituent entities of in-scope MNE
  groups — groups with annual consolidated revenue of EUR 750 million or
  more in at least two of the four preceding fiscal years. Entities outside
  the scope have no Bermuda transfer-pricing obligations.
- **Arm's length principle (section 2 definition).** Transactions between
  constituent entities must be recorded by reference to the conditions that
  would have been obtained between independent enterprises in comparable
  transactions and under comparable circumstances.
- **Filing entity.** Compliance runs through the Filing Bermuda Constituent
  Entity for the group; registration, returns and instalments are
  administered by CITA (CITA Online).

## 3. The rules (rates and adjustments table)

| Rule | Content | Source |
|---|---|---|
| Cross-border intra-group transactions | Any transaction between a Bermuda constituent entity and a constituent entity in a different jurisdiction, same in-scope MNE group, that is not consistent with the arm's length principle **must be adjusted** to be consistent with it | Corporate Income Tax Act 2023, Part 6 (transfer pricing requirements) |
| Amount mismatches | Any intra-group transaction not recorded in the same amount in the financial accounts of both constituent entities **must be adjusted** to the same amount | Corporate Income Tax Act 2023, Part 6 |
| Asset transfers between Bermuda constituent entities | A gain or loss on a sale or transfer of an asset between two Bermuda constituent entities that is not at arm's length is **recomputed on arm's-length terms** if the loss is included in taxable income or loss | Corporate Income Tax Act 2023, Part 6 |
| Consolidated-treatment election | At the election of the Filing Bermuda Constituent Entity, income, expenses, gains and losses from transactions between Bermuda constituent entities of the same in-scope group may be eliminated as if consolidated | Corporate Income Tax Act 2023, Part 6 |
| CIT rate | 15% on net taxable income of in-scope Bermuda constituent entities | Corporate Income Tax Act 2023, section 4 |
| CbCR | Country-by-country reporting is administered by CITA (exchangesupport@cita.bm); threshold and deadlines on the CITA CbCR page | CITA — Country-by-Country Reporting |

## 4. Tax base and computation

Transfer-pricing adjustments feed the CIT base: financial accounting net
income or loss (Part 5) plus prescribed taxable adjustments (Part 6, which
includes the transfer pricing requirements). There is no separate
transfer-pricing income charge — mispriced intra-group amounts are restated
inside the 15% CIT computation.

## 5. Deadlines

- **CIT instalments** run on the CITA published calendar; the CITA site
  banner (read 23 October 2026) shows, for example, a 2nd instalment due
  15 October 2026 for fiscal years ending 31 October 2026 and a 1st
  instalment due 31 October 2026 for fiscal years ending 28 February 2027.
- **CIT return** filing dates follow the Corporate Income Tax
  (Administrative) Regulations 2025 and CITA Online guidance.
- **CbCR deadlines:** needs-sources (CITA page not machine-readable in this
  pass).

## 6. Penalties and interest

Part 8A of the Act: interest is chargeable on underpaid amounts, and there
is power to impose civil penalties for failure to register, failure to file
a return, failure to accurately state tax on a return, and failure to pay
tax when due. Part 8B adds criminal offences (deliberate failure to file,
tax evasion). Penalty and interest amounts are set by the regulations —
confirm current rates against the Corporate Income Tax (Administrative)
Regulations 2025.

## 7. Cross-border interaction

Bermuda taxes in-scope groups on a GloBE-aligned net base; foreign taxes
(including foreign withholding taxes on dividends, interest, rents and
royalties) enter the computation through the foreign tax credit division
(Part 4). See bm-cross-border for the treaty and withholding picture.

## 8. Worked examples

**Example 1 — cross-border underpricing corrected.** A Bermuda constituent
entity sells an asset to a group company in a higher-tax jurisdiction for
USD 4,000,000 when the arm's-length price is USD 5,500,000. The Act
requires the transaction to be adjusted to arm's length: uplift USD
1,500,000, additional CIT at 15% = USD 225,000.

```oa-check
name: arm's length uplift BMD/USD 1.5m
inputs:
  arm_length: 5500000
  price: 4000000
steps:
  - uplift: arm_length - price
  - cit: uplift * 0.15
expected:
  cit: 225000.00
```

**Example 2 — mismatched intra-group records.** The Bermuda entity records
a service charge of USD 2,000,000; the foreign affiliate records USD
1,400,000 for the same transaction. The Act requires both to be adjusted to
the same amount; the Bermuda books move by the difference, USD 600,000,
and CIT on the uplift at 15% = USD 90,000.

```oa-check
name: mismatch alignment USD
inputs:
  bermuda_side: 2000000
  affiliate_side: 1400000
steps:
  - difference: bermuda_side - affiliate_side
  - cit: difference * 0.15
expected:
  cit: 90000.00
```

## 9. Ask the client first

1. Is the group in scope (EUR 750m in two of four years)? If not, Bermuda
   has no transfer-pricing regime for it.
2. Which intra-group transactions cross jurisdictions, and are the two
   sides recorded at the same amount?
3. Has the Filing entity made the consolidated-treatment election for
   Bermuda-to-Bermuda transactions?
4. Are CbCR notifications and filings current with CITA?

## 10. Sources

- [Corporate Income Tax Act 2023 — consolidated full text (CITA PDF)](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) — section 2 definitions, Part 4, Part 6 transfer pricing requirements, Part 8A/8B; read 2026-10-23.
- [CITA Technical References — Legislation](https://www.cita.bm/technical-references?sort_id=1) — consolidated acts list; read 2026-10-23.
- [CITA Technical References — Guidance](https://www.cita.bm/technical-references?sort_id=5) — CIT Guidance Notes, Group Management Functionality, Allocation of Taxes Between Constituent Entities; read 2026-10-23.
- [CITA — Country-by-Country Reporting](https://www.cita.bm/country-by-country-reporting-cbcr) — read 2026-10-23 (page renders client-side; details needs-sources).
- [CITA — Filing & Payment Deadlines](https://www.cita.bm/filing-payment-deadlines) — read 2026-10-23 (page renders client-side).
- [gov.bm — Corporate Income Tax information](https://www.gov.bm/roc/corporate-income-tax-information) — read 2026-10-23.


## Recomputing examples

```oa-check
name: CbCR threshold EUR 750M — group at EUR 800M files
inputs:
  revenue_eur: 800000000
  threshold: 750000000
steps:
  - over: revenue_eur - threshold
  - must_file: min(max(over, 0), 1)
expected:
  over: 50000000.00
  must_file: 1.00
```
```oa-check
name: Group at EUR 700M is under the CbCR threshold
inputs:
  revenue_eur: 700000000
  threshold: 750000000
steps:
  - over: max(revenue_eur - threshold, 0)
  - must_file: min(over, 1)
expected:
  over: 0.00
  must_file: 0.00
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Government of Bermuda — Bermuda Corporate Income Tax (CIT effective 1 Jan 2025; CITA administers CbCR) | https://www.gov.bm/CIT | 2026-10-28 |


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