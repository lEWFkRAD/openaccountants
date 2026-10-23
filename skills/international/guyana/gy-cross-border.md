---
name: gy-cross-border
description: >
  Guyana cross-border tax reference for 2026. Covers taxation of
  non-residents under the Income Tax Act (Cap 81:01), the 20% final
  withholding on interest, royalties, management fees and rent, the
  narrow treaty network (CARICOM and bilateral DTCs), the no-exit-tax
  position, and permanent establishment exposure. Trigger on Guyana
  cross-border, non-resident, withholding, treaty, double taxation,
  CARICOM. Source-cited draft.
jurisdiction: GY
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Guyana cross-border

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the Guyana Revenue
Authority portal (home, Income Tax operations, Tax Rates and Thresholds,
Income Tax guides, International Information Exchange / FATCA page), and
the existing Guyana corporate-income skill (withholding figures carried
forward with their citations). Currency is the Guyana dollar (GYD).

**Source status caveat:** GRA publishes no consolidated machine-readable
register of in-force double-taxation conventions on the pages read this
pass, and the consolidated Income Tax Act (Cap 81:01) text did not
resolve. The treaty inventory and article-level withholding rates below
are **needs-sources** — confirm each convention's status with GRA before
relying on treaty relief.

## 2. Who this applies to

- **Non-residents deriving income from Guyana.** Guyana taxes
  non-residents on income arising in or from Guyana, largely through
  final withholding under the Income Tax Act (Cap 81:01).
- **Payers as withholding agents.** Guyana companies and persons paying
  interest, royalties, management/technical fees, rent or contract
  payments to non-residents must withhold and remit by the 14th day of
  the following month (see gy-corporate-income-tax).
- **CARICON/CSME service providers** — intra-CARICOM practice may differ
  under the Revised Treaty of Chaguaramas; **needs-sources**.

## 3. Withholding and outbound payments (rates table)

| Payment to non-residents | Rate | Character | Source |
|---|---|---|---|
| Interest | 20% | final | Income Tax Act (Cap 81:01) — see gy-corporate-income-tax (PwC-cited) |
| Royalties | 20% | final | as above |
| Management / technical service fees | 20% | final | as above |
| Rent / lease payments | 20% | final | as above |
| Dividends | exempt at recipient (no dividend WHT) | — | as above |
| Contract payments to non-resident contractors | 5% (construction) / 10% (other) | final | needs-sources (confirm current GRA schedule) |

## 4. Treaty network

- Guyana's DTC network is narrow. Commonly cited partners include China,
  Portugal, Qatar, UAE, Singapore, South Korea, Italy, Barbados,
  Jamaica and other CARICOM states — status and effective dates vary and
  several were never ratified. **needs-sources** for the consolidated
  in-force list.
- The CARICOM Double Taxation (DTC) regime and the Revised Treaty of
  Chaguaramas bear on intra-CARICOM income; article-level effects:
  **needs-sources**.
- GRA's International Information Exchange page covers FATCA and TIEA/
  CRS exchange, not treaty relief — do not read withholding relief from
  it.

## 5. Exit and departure

- Guyana imposes **no exit tax / departure tax** on individuals or
  companies ceasing residence; gains on Guyanese immovable property
  remain taxable in Guyana after departure (Capital Gains Tax under the
  Income Tax Act — see gy-income-tax).
- Companies winding up face normal Corporation Tax Act assessment on
  chargeable profits up to cessation (see gy-corporate-income-tax).

## 6. Permanent establishment

- A non-resident carrying on business in Guyana through a fixed place
  or dependent agent is assessed as a resident company under the
  Corporation Tax Act (40% commercial / 2% turnover MCT floor — see
  gy-corporate-income-tax).
- Branch remittances are not separately taxed beyond the company charge
  (no branch profits tax confirmed; **needs-sources**).

## 7. Interaction with transfer pricing

Cross-border associate payments carry the 20% final WHT and the
associated-enterprise revaluation rules (see gy-transfer-pricing).
Treaty relief, where a convention is in force, is claimed through GRA;
absent relief the double charge stacks.

## 8. Worked examples

**Example 1 — management fee to a foreign parent.** A Guyana company
pays GYD 250,000 to its non-resident parent for management services.
Final WHT at 20% = GYD 50,000; the parent nets GYD 200,000.

```oa-check
name: management fee WHT GYD 250k
inputs:
  gross: 250000
  rate: 0.20
steps:
  - wht: gross * rate
  - net: gross - wht
expected:
  wht: 50000.00
  net: 200000.00
```

**Example 2 — treaty relief at a reduced rate.** The same fee is paid
to a resident of a state with an in-force Guyana DTC capping the fee
WHT at 10% (illustrative — confirm the convention). WHT falls to GYD
40,000, saving GYD 10,000 against the domestic 20%.

```oa-check
name: treaty-capped fee WHT GYD 400k
inputs:
  gross: 400000
  domestic: 0.20
  treaty: 0.10
steps:
  - wht: gross * treaty
  - saved: gross * domestic - gross * treaty
expected:
  wht: 40000.00
  saved: 40000.00
```

## 9. Ask the client first

1. Where does the income arise — is it Guyanese-source at all?
2. Which WHT rate applies to the payment character, and was it withheld
   and remitted by the 14th of the following month?
3. Is a DTC actually in force with the counterparty's state, and has
   GRA accepted the relief claim?
4. Is the counterparty related — if so, run the associated-enterprise
   check (gy-transfer-pricing) before filing.

## 10. Sources

- [Guyana Revenue Authority — home](https://gra.gov.gy/) — read 2026-10-23.
- [GRA — Income Tax (tax operations)](https://gra.gov.gy/business/tax-operations-and-services/income-tax/) — read 2026-10-23.
- [GRA — Tax Rates and Thresholds](https://gra.gov.gy/tax-services/income-tax/tax-rates-and-thresholds/) — read 2026-10-23.
- [GRA — Tax Guides, Income Tax](https://gra.gov.gy/tax-guides-income-tax/) — read 2026-10-23.
- [GRA — International Information Exchange (FATCA)](https://gra.gov.gy/quick-links-2/fatca-agreement/) — read 2026-10-23.
- [Parliament of Guyana — Acts of Parliament](https://parliament.gov.gy/publications/acts-of-parliament/) — read 2026-10-23.
- Existing pack skill `gy-corporate-income-tax` — withholding figures carried forward with their PwC citations pending statute-level confirmation.

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
