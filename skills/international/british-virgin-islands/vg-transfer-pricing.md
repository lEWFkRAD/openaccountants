---
name: vg-transfer-pricing
description: >
  British Virgin Islands transfer pricing reference for 2026. The
  BVI levies no income tax, so there is no classic arm's-length
  revaluation; the real related-party controls are the Economic
  Substance (Companies and Limited Partnerships) Act 2018, the BVI
  Business Companies Act annual financial return, information
  exchange (CRS/AEOI), and the OECD Pillar Two 15% top-up exposure
  of low-taxed BVI entities inside in-scope groups. Covers payroll
  tax as the only BVI tax on activity. Trigger on BVI transfer
  pricing, economic substance, Pillar Two, related party,
  management company. Source-cited draft.
jurisdiction: VG
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# British Virgin Islands transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the GOV.VG home,
financial-and-tax-information and Inland Revenue Department pages;
Virgin Islands Laws Online (laws.gov.vg) including the BVI Business
Companies Act chain and the Financial Return Order 2023; the Social
Security Board contributions page; the 2026 Budget Address; and the
existing VG pack skills (figures carried forward with their
citations). Currency: US dollar (USD).

**Source status caveat:** the Economic Substance Act 2018, Payroll
Taxes Act 2004 and Income Tax Act consolidated texts were not
locatable on laws.gov.vg this pass, and bvifsc.vg returned 403 to
automated reads — section numbers, ES penalty amounts and the BVI's
Pillar Two implementation status are **needs-sources**. The 2026
Budget Address text read on 2026-10-24 contains no Pillar Two
implementation announcement.

## 2. Who the rules apply to

- **No classic TP regime.** With no corporate or personal income tax
  there is no BVI profit base for the tax authority to revalue; no
  statutory transfer-pricing documentation code (local file / master
  file / CbCR) is confirmed — **needs-sources.**
- **Economic substance users.** Companies and limited partnerships
  carrying on one of the relevant activities (holding, distribution,
  service centre, shipping, fund, financing and leasing, intellectual
  property, headquarters) must direct and manage in the BVI, conduct
  core income-generating activity in the BVI, and have adequate
  staff, expenditure and premises — Economic Substance (Companies and
  Limited Partnerships) Act 2018 (sections needs-sources).
- **Pillar Two exposure.** In-scope multinational groups
  (consolidated revenue ≥ EUR 750m, approx — confirm) face the GloBE
  15% minimum; a low-taxed BVI entity creates top-up liability in
  any jurisdiction that has implemented the QDMTT/UTPR/IBSR — the
  BVI's own implementation status is **needs-sources** (no
  announcement in the 2026 Budget Address read 2026-10-24).
- **Cross-border payments.** BVI companies pay no BVI withholding on
  outbound dividends, interest or royalties (see vg-corporate-income-
  tax); the counterparty's country may impose its own WHT and its own
  arm's-length adjustments on the same flow.

## 3. The rules (control table)

| Rule | Content | Source |
|---|---|---|
| Income tax / TP revaluation | None — no income tax base to adjust | Income Tax Act (rate nil) — vg-corporate-income-tax |
| Economic substance | Relevant-activity entities must prove BVI direction, CIGA, adequate staff/expenditure/premises; reported to the registered agent | Economic Substance Act 2018 (sections needs-sources) |
| Annual financial return | File with the registered agent within 9 months after financial year end | BVI Business Companies (Financial Return) Order, 2023 (laws.gov.vg, read 2026-10-24) |
| Pillar Two 15% | GloBE top-up for in-scope groups; BVI implementation status needs-sources | OECD/G20 GloBE Model Rules — vg-corporate-income-tax |
| Outbound WHT | 0% dividends, interest, royalties | Income Tax Act — vg-corporate-income-tax |
| Payroll Tax (the only activity tax) | 10% Class 1 / 14% Class 2 of remuneration; first US$10,000 per employee exempt | Payroll Taxes Act 2004 — vg-payroll-social |
| Information exchange | CRS/AEOI reporting by in-scope financial institutions | GOV.VG CRS news item (link 404 this pass — needs-sources) |

## 4. Tax base and computation

There is no BVI profit base, so "transfer pricing" in the BVI is a
**substance and counterparty** exercise: (a) test whether the entity
is a relevant-activity entity and whether its intra-group pricing is
consistent with the functions actually performed in the BVI (the ES
test effectively requires group income to match BVI substance);
(b) compute the counterparty country's WHT and any arm's-length
uplift on the same flow; (c) for in-scope groups, compute the GloBE
effective tax rate of the BVI constituent entity (0% plus payroll
tax rarely qualifies as covered taxes) and the resulting top-up in
implementing jurisdictions.

## 5. Deadlines

- **Economic substance report:** to the registered agent within 6
  months after the end of the financial period ((approx — confirm;
  carried from vg-corporate-income-tax)).
- **Annual financial return:** within 9 months after financial year
  end (Financial Return Order 2023).
- **Annual government fee:** incorporation Jan–Jun → by 31 May;
  Jul–Dec → by 30 November ((approx — confirm) — vg-corporate-
  income-tax).
- **Payroll Tax return and payment:** monthly, by the 21st of the
  following month ((approx — confirm) — vg-payroll-social).

## 6. Penalties and interest

ES Act penalties and registered-agent late-return fines are set by
the Acts and are **needs-sources** (amounts not machine-readable this
pass). Non-compliance escalates to striking-off risk for the company
itself.

## 7. Worked examples

**Example 1 — Pillar Two top-up on a low-taxed BVI entity.** An
in-scope group's BVI service entity earns USD 200,000 and pays no
income tax; a member state with a QDMTT/UTPR tops up to the 15%
minimum (illustrative — confirm the group's implementing
jurisdictions).

```oa-check
name: BVI entity 200k low-taxed 15 percent top-up
inputs:
  income: 200000
  min_rate: 15
steps:
  - top_up: income * pct(1, min_rate)
expected:
  top_up: 30000.00
```

**Example 2 — the only BVI tax on the activity: Payroll Tax.** A
Class 2 employer pays USD 250,000 of remuneration to BVI staff; the
first USD 10,000 per employee is exempt, the rest is taxed at 14%.

```oa-check
name: class 2 payroll 250k minus 10k exempt at 14 percent
inputs:
  remuneration: 250000
  exempt: 10000
  rate: 14
steps:
  - base: remuneration - exempt
  - payroll_tax: base * pct(1, rate)
expected:
  base: 240000.00
  payroll_tax: 33600.00
```

## 8. Ask the client first

1. Which of the eight relevant activities does the BVI entity carry
   on, and where are the core income-generating activities actually
   performed?
2. Is the group in Pillar Two scope, and which member states have
   implemented QDMTT/UTPR/IBSR that would catch the BVI entity?
3. Do the intra-group prices match the functions, assets and risks
   the BVI entity actually bears (the ES file will be read against
   them)?
4. Are the annual financial return (9 months) and ES report (6
   months) filed with the registered agent on time?

## 9. Sources

- [Government of the Virgin Islands — home](https://bvi.gov.vg/) — read 2026-10-24.
- [GOV.VG — Financial and Tax Information](https://bvi.gov.vg/topics/financial-and-tax-information) — read 2026-10-24.
- [GOV.VG — Inland Revenue Department](https://bvi.gov.vg/inland-revenue-department) — read 2026-10-24.
- [Virgin Islands Laws Online](https://laws.gov.vg/) — read 2026-10-24.
- [BVI Business Companies (Financial Return) Order, 2023](https://laws.gov.vg/laws/bvi-business-companies-financial-return-order-2023) — read 2026-10-24.
- [GOV.VG — 2026 Budget Address](https://bvi.gov.vg/service-details/2026-budget-address) — read 2026-10-24 (no Pillar Two announcement in the text).
- Existing pack skill `vg-corporate-income-tax` — fees, substance and Pillar Two figures carried forward with their citations.

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
