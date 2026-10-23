---
name: gy-transfer-pricing
description: >
  Guyana transfer pricing reference for 2026. Covers the associated-
  enterprise arm's-length rules inside the Income Tax Act (Cap 81:01),
  GRA revaluation powers on non-arm's-length transactions between
  associates, the interaction with the 40% commercial company rate and
  2% minimum corporation tax under the Corporation Tax Act (Cap 81:03),
  the 20% non-resident withholding overlay, and the absence of a
  published standalone transfer-pricing documentation code. Trigger on
  Guyana transfer pricing, associated enterprises, arm's length, GRA
  revaluation, associates. Source-cited draft.
jurisdiction: GY
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Guyana transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the Guyana Revenue
Authority portal (home, Income Tax operations page, Tax Rates and
Thresholds page, Income Tax guides page), and the existing Guyana
corporate-income skill (Corporation Tax Act figures carried forward with
their citations). Currency is the Guyana dollar (GYD).

**Source status caveat:** the consolidated Income Tax Act (Cap 81:01)
text did not resolve from a machine-readable official page this pass —
parliament.gov.gy's Acts pages index recent Acts only, and the GRA site
publishes guides, not the Act. The section numbers of the associated-
enterprise / revaluation provisions, any statutory documentation
deadline, and the country-by-country reporting position are therefore
**needs-sources** — confirm against the consolidated Cap 81:01 (GRA or
the Attorney Chambers' revised edition) before tier-1 promotion.

## 2. Who the rules apply to

- **Transactions between associates.** The Income Tax Act (Cap 81:01)
  contains associated-enterprise / associate-person provisions allowing
  GRA to recompute income where a transaction between associates is not
  at arm's length and has the effect of reducing a Guyana tax base.
  Article-level section numbers: needs-sources.
- **Cross-border payments to non-resident associates** additionally run
  through the 20% final withholding regime (see gy-cross-border) — the
  two charges stack.
- **No published standalone TP documentation code** (no local-file /
  master-file / CbCR triplet confirmed) — GRA requests records through
  its audit powers. **needs-sources.**

## 3. The rules (revaluation table)

| Rule | Content | Source |
|---|---|---|
| Arm's-length revaluation | GRA may recompute the profits of a person carrying on business in Guyana where an associate transaction departs from arm's length and understates the Guyana base | Income Tax Act (Cap 81:01), associated-enterprise provisions (sections needs-sources) |
| Company rate the adjustment feeds | 40% of chargeable profits (commercial company), or 2% of turnover minimum corporation tax, whichever is higher | Corporation Tax Act (Cap 81:03) — see gy-corporate-income-tax |
| Non-commercial company rate | 25% of chargeable profits | Corporation Tax Act (Cap 81:03) — see gy-corporate-income-tax |
| Withholding overlay | 20% final WHT on interest, royalties, management fees, rent to non-residents | Income Tax Act (Cap 81:01) withholding provisions — see gy-corporate-income-tax |
| Documentation | No standalone statutory TP-file regime confirmed; records on request under GRA assessment powers | needs-sources |

## 4. Tax base and computation

A revaluation feeds chargeable profits for the Corporation Tax Act
computation. Because the 2% minimum corporation tax on turnover also
applies, an arm's-length uplift that raises turnover (for a distributor)
can raise the MCT floor as well as the 40% charge — compute both and pay
the higher.

## 5. Deadlines

- **Corporation tax return:** within four months of the financial
  year-end (see gy-corporate-income-tax; confirm current GRA calendar).
- **WHT returns:** by the 14th day of the month following payment (see
  gy-corporate-income-tax).
- **TP documentation:** no statutory preparation deadline confirmed —
  **needs-sources**.

## 6. Penalties and interest

Assessment and collection run through the Income Tax Act: GRA may assess
under-declared amounts, with penalties and interest on late/incorrect
returns (amounts set by the Act — section-level figures
**needs-sources**). Objections follow the GRA guides page route.

## 7. Cross-border interaction

Guyana's treaty network is narrow (see gy-cross-border), so a
revaluation of a cross-border associate payment rarely gets treaty
relief on the withholding side. CARICOM members' double-tax conventions
and the CARICOM Agreement may bear on intra-CARICOM services —
**needs-sources**.

## 8. Worked examples

**Example 1 — service fee undercharge by a Guyana associate.** A Guyana
company provides back-office services to its foreign parent for GYD
620,000 when the arm's-length fee is GYD 900,000. GRA recomputes the
Guyana profits up by GYD 280,000; additional corporation tax at the 40%
commercial rate = GYD 112,000.

```oa-check
name: service fee uplift GYD 280k
inputs:
  arm_length: 900000
  price: 620000
steps:
  - uplift: arm_length - price
  - cta: uplift * 0.40
expected:
  cta: 112000.00
```

**Example 2 — royalty overcharge.** A Guyana licensee pays its foreign
associate GYD 1,500,000 in royalties; GRA accepts GYD 1,200,000 as arm's
length. The GYD 300,000 excess is disallowed; additional corporation tax
at 40% = GYD 120,000 (the 20% WHT already borne on the gross royalty is
separate and final).

```oa-check
name: royalty disallowance GYD 300k
inputs:
  royalty_paid: 1500000
  arm_length: 1200000
steps:
  - disallowed: royalty_paid - arm_length
  - cta: disallowed * 0.40
expected:
  cta: 120000.00
```

## 9. Ask the client first

1. Which transactions crossed borders with associates in the year —
   goods, services, royalties, management fees, loans?
2. Are the two sides recorded at the same price in both countries?
3. Was 20% WHT withheld and remitted by the 14th of the following month
   on every cross-border associate payment?
4. Does the uplift push the 2% minimum corporation tax above the 40%
   charge — has the MCT floor been checked?

## 10. Sources

- [Guyana Revenue Authority — home](https://gra.gov.gy/) — read 2026-10-23.
- [GRA — Income Tax (tax operations)](https://gra.gov.gy/business/tax-operations-and-services/income-tax/) — read 2026-10-23.
- [GRA — Tax Rates and Thresholds](https://gra.gov.gy/tax-services/income-tax/tax-rates-and-thresholds/) — read 2026-10-23.
- [GRA — Tax Guides, Income Tax](https://gra.gov.gy/tax-guides-income-tax/) — read 2026-10-23.
- [Parliament of Guyana — Acts of Parliament](https://parliament.gov.gy/publications/acts-of-parliament/) — read 2026-10-23.
- Existing pack skill `gy-corporate-income-tax` — Corporation Tax Act and withholding figures carried forward with their PwC citations pending statute-level confirmation.

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
