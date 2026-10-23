---
name: ky-cross-border
description: >
  Cayman Islands cross-border tax reference for 2026. Covers the
  zero-withholding position on dividends, interest and royalties, the
  absence of a Cayman treaty network, exchange-of-information
  obligations (CRS, FATCA, EoI) as the real cross-border compliance
  layer, economic substance for relevant activities, and the Pillar Two
  Income Tax Act 2025 context. Trigger on Cayman Islands cross-border,
  withholding, treaty, CRS, FATCA, substance, exempted company.
  Source-cited draft.
jurisdiction: KY
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Cayman Islands cross-border

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the DITC site (home,
frameworks pages, CbCR hub), the CIREgistry fees page, and the existing
Cayman corporate-income skill (zero-withholding figures carried forward
with their citations). Currency is the Cayman Islands dollar (CI$).

**Source status caveat:** legislation.gov.ky did not resolve from this
network this pass, so statute-level citations (Companies Act 2025
Revision, Income Tax Act 2025, TIA Act instruments) rest on the DITC
and CIREgistry administering pages. Treat the Pillar Two paragraphs as
**needs-sources**.

## 2. Who this applies to

- **Exempted and local companies paying abroad.** Cayman companies pay
  dividends, interest and royalties to non-residents with **no Cayman
  withholding** — the cross-border burden is informational, not a tax
  charge.
- **Institutions and in-scope entities** carrying out CRS/FATCA
  reporting and economic-substance obligations administered by the DITC
  as the competent authority under the Tax Information Authority Act
  (2021 Revision).
- **MNE groups** with Cayman constituent entities facing partner-
  jurisdiction CFC/substance rules and Pillar Two GloBE.

## 3. Outbound payments (rates table)

| Payment to non-residents | Cayman WHT | Character | Source |
|---|---|---|---|
| Dividends | 0% | none | existing ky-corporate-income-tax (PwC-cited) |
| Interest | 0% | none | as above |
| Royalties / fees | 0% | none | as above |
| Branch / repatriation charge | 0% (no branch profits tax) | none | as above |
| Import duty on goods brought in | 27% schedule (not a tax on payments) | — | see ky-vat-gst |

## 4. Treaty network

- The Cayman Islands has **no income-tax treaty network of its own**;
  relief questions are resolved in the counterparty's jurisdiction.
- The cross-border layer that does bite is exchange of information:
  **CRS** (Common Reporting Standard), **FATCA** (US IGA regime), and
  **exchange of information on request**, all administered by the DITC
  under the TIA Act framework — see the DITC frameworks pages.
- UK territories' treaty exposure: UK-signed conventions generally do
  not extend to the Cayman Islands unless expressly applied —
  **needs-sources** per convention.

## 5. Exit and departure

- No exit tax, no capital-gains charge on departure — the zero-tax
  regime simply ends with the entity's striking-off or continuation
  elsewhere (Companies Act continuation provisions; **needs-sources**
  at statute level).
- Exempted-company tax-undertaking certificates (up to 20 years,
  extendable) predate the 2025 Income Tax Act; their interaction with
  Pillar Two is **needs-sources**.

## 6. Substance and residence

- **Economic Substance Act (2026 Revision):** in-scope entities carrying
  on a "relevant activity" (fund management, financing, headquarter,
  holding, shipping, distribution, service centre, IP, banking,
  insurance, trust) must satisfy the substance test and file the annual
  ES notification and return with the DITC.
- Cayman "residence" rarely matters for Cayman tax (there is none) but
  drives partner-jurisdiction CFC and treaty-benefit analysis — the
  substance test is the factual record that answers those questions.

## 7. Pillar Two context

The Cayman Income Tax Act 2025 was enacted to implement the Pillar Two
global minimum tax for MNE groups (EUR 750m+): a domestic minimum
top-up tax / QDMTT-style charge for in-scope groups, otherwise the
zero-rate baseline stands for everyone else. Consolidated text and
effective-date mechanics: **needs-sources** (statute portal unreachable
this pass). See ky-transfer-pricing for the CbCR data plumbing.

## 8. Worked examples

**Example 1 — dividend repatriation.** A Cayman exempted company pays a
US$1,000,000 dividend to its non-resident shareholder. Cayman WHT is
nil; the shareholder nets the full US$1,000,000 (home-country tax is
the shareholder's problem).

```oa-check
name: dividend repatriation US$1m
inputs:
  gross: 1000000
  rate: 0.0
steps:
  - wht: gross * rate
  - net: gross - wht
expected:
  wht: 0.00
  net: 1000000.00
```

**Example 2 — three outbound payments.** The same company pays US$300k
interest, US$450k royalties and US$250k service fees abroad: total
US$1,000,000, total Cayman WHT nil.

```oa-check
name: outbound payments stack US$1m
inputs:
  interest: 300000
  royalties: 450000
  fees: 250000
steps:
  - total: interest + royalties + fees
  - wht: total * 0.0
expected:
  total: 1000000
  wht: 0.00
```

## 9. Ask the client first

1. Is the Cayman entity in scope for economic substance — which
   relevant activity, and was the ES notification/return filed?
2. Is the group CRS/FATCA-reporting through this entity, and are
   account classifications current?
3. Does the group cross the Pillar Two EUR 750m threshold — has the
   2025 Act's top-up charge been assessed for the structure?
4. What will partner jurisdictions say about the profit sitting in the
   Cayman entity — is the substance file ready for their auditors?

## 10. Sources

- [DITC — home](https://www.ditc.ky/) — read 2026-10-23.
- [DITC — CbCR hub](https://www.ditc.ky/cbcr/) — read 2026-10-23.
- [DITC — International Tax Co-operation (Economic Substance) Act 2026 Revision](https://www.ditc.ky/legislation-resources/international-tax-co-operation-economic-substance-act-2026-revision/) — read 2026-10-23.
- [DITC — Tax Information Authority Act 2021 Revision](https://www.ditc.ky/legislation-resources/tax-information-authority-act-2021-revision/) — read 2026-10-23.
- [CIREgistry — fees](https://www.ciregistry.ky/fees/) — read 2026-10-23.
- Existing pack skill `ky-corporate-income-tax` — zero-withholding baseline carried forward with its PwC citations.

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
