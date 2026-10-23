---
name: ky-transfer-pricing
description: >
  Cayman Islands transfer pricing reference for 2026. Covers the
  country-by-country reporting (CbCR) regime administered by the DITC
  under BEPS Action 13 — notification, US$850 million threshold,
  12-month reporting deadline, DITC Portal filing — the absence of a
  domestic arm's-length adjustment code for the zero-tax regime, and the
  Pillar Two GloBE context created by the Income Tax Act 2025. Trigger
  on Cayman Islands transfer pricing, CbCR, country-by-country report,
  DITC portal, UPE, SPE, Pillar Two, GloBE. Source-cited draft.
jurisdiction: KY
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Cayman Islands transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the DITC site (home,
CbCR hub, CbCR FAQs, CbCR Legislation & Resources page) and the existing
Cayman corporate-income skill. Currency is the Cayman Islands dollar
(CI$); the CbCR threshold is expressed in US dollars.

**Source status caveat:** legislation.gov.ky (the statute portal) did not
resolve from the network this pass, so the CbCR Regulations text and the
Income Tax Act 2025 (Pillar Two) provisions are cited from the DITC's
administering pages, not the statute. Section-level citations and the
GloBE/QDMTT mechanics are **needs-sources** — confirm against the
gazetted regulations and the 2025 Act before tier-1 promotion.

## 2. Who the rules apply to

- **Multinational enterprise (MNE) groups with a Cayman constituent
  entity.** The Cayman Islands has implemented BEPS Action 13 CbCR: an
  MNE group is in scope where consolidated group revenue is not less
  than the specified threshold — the Cayman Islands has specified
  **US$850 million** in the preceding fiscal year (other jurisdictions
  may use €750 million).
- **Reporting Entities.** A Reporting Entity (Ultimate Parent Entity
  UPE, or a Surrogate/Specified Reporting Entity SPE) **resident in the
  Cayman Islands** files the CbC Report through the DITC Portal.
- **No domestic arm's-length adjustment code.** With no ordinary income
  tax base, there is no classic transfer-pricing revaluation regime for
  Cayman entities; pricing matters flow through to partner/member
  jurisdictions and, for in-scope MNEs, through Pillar Two GloBE
  computations under the Income Tax Act 2025 (**needs-sources**).

## 3. The rules (CbCR table)

| Rule | Content | Source |
|---|---|---|
| Legal basis | CbCR under BEPS Action 13, implemented in Cayman law (CbCR regulations under the Tax Information Authority Act framework) | DITC — CbCR page (states BEPS Action 13 basis); TIA Act 2021 Revision |
| Threshold | Consolidated group revenue not less than US$850 million in the preceding fiscal year | DITC — CbCR FAQs (read 2026-10-23) |
| Notification | One-off notification via the DITC Portal; deadline before the end of the relevant fiscal year; updates by email/portal for UPE/SPE changes | DITC — CbCR FAQs |
| Reporting | CbC Report filed via the DITC Portal within 12 months of the end of the reporting fiscal year | DITC — CbCR FAQs |
| 2024-year extension | Industry Advisory of 3 December 2025 extended 2024 fiscal-year filings with deadlines between 31 July and 31 December 2025 to **27 February 2026** | DITC — CbCR FAQs |
| Content | Revenue, profit, taxes paid/accrued and activity indicators per jurisdiction, per OECD CbCR XML Schema User Guide v2.0 (June 2019) and the Cayman CbC XML Schema User Guide | DITC — CbCR FAQs |
| Prior legislation versions | Official Gazette | DITC — CbCR Legislation & Resources page |

## 4. Tax base and computation

There is no Cayman taxable base to adjust. The CbC Report is an
information return; its numbers feed partner jurisdictions' risk
assessments. For Pillar Two in-scope MNEs (group revenue EUR 750m+),
GloBE effective-tax-rate computations use the group's jurisdictional
data — the Cayman domestic minimum top-up tax position under the Income
Tax Act 2025 is **needs-sources**.

## 5. Deadlines

- **Notification:** before the end of the relevant fiscal year (one-off;
  amend on UPE/SPE changes).
- **CbC Report:** within 12 months of the fiscal year-end (standard
  filing deadline).
- **2024 fiscal-year filings:** extended to 27 February 2026 for groups
  whose deadline fell between 31 July and 31 December 2025 (DITC
  Industry Advisory, 3 December 2025).
- **ES notification/return (separate regime):** DITC prescribed dates
  under the Economic Substance Act 2026 Revision — see ky-tax-overview
  and the DITC ES pages.

## 6. Penalties and interest

Failure to notify or file CbCR attracts penalties under the CbCR
regulations (fixed and continuing daily penalties; exact amounts in the
regulations — **needs-sources**, legislation.gov.ky unreachable this
pass). No interest applies because no Cayman tax is due.

## 7. Cross-border interaction

Cayman entities sit in the middle of related-party structures far more
often than they earn Cayman income. Expect the CbC Report to be the
document partner-jurisdiction auditors use to challenge where profit
sits; substance (ES Act) and the actual functions performed by the
Cayman entity are the defence. See ky-cross-border.

## 8. Worked examples

**Example 1 — in-scope group.** An MNE group with a Cayman SPE has
consolidated revenue of US$920 million in the preceding fiscal year.
US$920m ≥ US$850m, so the group is in scope; the margin above the
threshold is US$70 million.

```oa-check
name: CbCR threshold test US$920m
inputs:
  revenue: 920000000
  threshold: 850000000
steps:
  - margin: revenue - threshold
expected:
  margin: 70000000
```

**Example 2 — below threshold.** A group with US$840 million consolidated
revenue is US$10 million below the US$850 million Cayman threshold and
out of CbCR scope (watch the following year).

```oa-check
name: CbCR threshold test US$840m
inputs:
  revenue: 840000000
  threshold: 850000000
steps:
  - gap: threshold - revenue
expected:
  gap: 10000000
```

## 9. Ask the client first

1. Is the group's consolidated revenue at or above US$850 million — and
   was the one-off DITC Portal notification filed?
2. Is the Cayman entity the UPE, an SPE, or a non-reporting constituent
   entity — who files, and where?
3. Was the 2024 CbC Report filed by 27 February 2026 if the deadline
   fell in the extension window?
4. Do the Cayman entity's functions and substance support the profit
   split that partner jurisdictions will see in the CbC Report?

## 10. Sources

- [DITC — CbCR hub](https://www.ditc.ky/cbcr/) — read 2026-10-23.
- [DITC — CbCR FAQs](https://www.ditc.ky/cbcr/cbcr-faqs/) — threshold, deadlines, extension; read 2026-10-23.
- [DITC — CbCR Legislation & Resources](https://www.ditc.ky/cbcr/cbcr-legislation-resources/) — read 2026-10-23.
- [DITC — Tax Information Authority Act 2021 Revision](https://www.ditc.ky/legislation-resources/tax-information-authority-act-2021-revision/) — read 2026-10-23.
- [DITC — home](https://www.ditc.ky/) — read 2026-10-23.
- Existing pack skill `ky-corporate-income-tax` — zero-tax baseline carried forward with its citations.

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
