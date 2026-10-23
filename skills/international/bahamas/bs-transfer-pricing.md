---
name: bs-transfer-pricing
description: >
  Bahamas transfer pricing reference for 2026. Covers the Domestic
  Minimum Top-Up Tax Act 2024, which implements the OECD GloBE (Pillar
  Two) Model Rules by incorporation — 15% minimum effective rate, EUR 750
  million in-scope threshold, returns and payment 15 months after fiscal
  year end, DIR notification forms DMTT-24/DMTT-25 — and the absence of a
  general domestic transfer-pricing code for ordinary Bahamian companies
  (no income tax, no withholding). Trigger on Bahamas transfer pricing,
  DMTT, GloBE, Pillar Two, in-scope MNE. Source-cited draft.
jurisdiction: BS
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Bahamas transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the full text of the
Domestic Minimum Top-Up Tax Bill/Act 2024 (PDF from the Office of the
Prime Minister pillar-two portal), the OPM "Introduction of a Domestic
Minimum Top-Up Tax in the Bahamas" explainer (same portal), and the
Department of Inland Revenue (DIR) DMTT pages (notification, forms, FAQs).
Currency is the Bahamian dollar (BSD), pegged 1:1 to USD.

**Source status caveat:** the PDF read is the 2024 Bill as enacted;
consolidated amendments and the DMTT Regulations (if made) were not read.
The GloBE Model Rules are incorporated by reference and amended by order —
the current Inclusive Framework guidance governs substance. There is **no
general transfer-pricing code** for out-of-scope companies because there is
no general income tax; that is a structural fact, not a gap.

## 2. Who the rules apply to

- **In-scope only.** The DMTT applies to Constituent Entities located in
  The Bahamas of MNE Groups within the scope of the GloBE Model Rules —
  groups with consolidated revenue of EUR 750 million or more in at least
  two of the four preceding fiscal years.
- **No general TP regime.** Ordinary Bahamian companies (and IBCs) face no
  arm's-length adjustment rules, no documentation file, and no
  withholding, because The Bahamas imposes no income tax. Related-party
  pricing is commercially, not fiscally, regulated.
- **Notification duty.** Each Bahamian Constituent Entity must notify the
  Financial Secretary (the "Secretary") at the beginning of each fiscal
  year whether the group is likely to be in GloBE scope (Act s.5(2)). DIR
  ran this via Forms DMTT-24 and DMTT-25 (deadlines 31 March 2026 and
  30 April 2026 respectively, per the DIR DMTT page read 2026-10-23).

## 3. Rates and key parameters

| Item | Value | Source |
|---|---|---|
| DMTT rate | 15% minimum effective rate (GloBE top-up design) | DMTT Act 2024, s.3–4 (GloBE Model Rules incorporated) |
| In-scope threshold | EUR 750 million consolidated revenue, two of four fiscal years | DMTT Act 2024 (GloBE scope); OPM explainer |
| Commencement | Deemed in force 1 January 2024; applies to fiscal years of in-scope MNE Groups (first captured FYs beginning on or after 1 January 2025) | DMTT Act 2024, s.1(2) |
| Return deadline | No later than 15 months after the last day of the MNE Group's fiscal year | DMTT Act 2024, s.5(1) |
| Payment deadline | No later than 15 months after the last day of the fiscal year | DMTT Act 2024, s.6(1) |
| Currency | BSD (pegged 1:1 USD); DMTT paid into the Consolidated Fund | DMTT Act 2024, s.6(2) |

## 4. Tax base and computation

The base is GloBE income of Bahamian Constituent Entities less GloBE
losses, with the substance-based income exclusion, per the incorporated
GloBE Model Rules; DMTT equals the top-up amount that brings the Bahamian
ETR to 15%. The arm's-length principle operates through the GloBE Rules'
definitions (related-party transactions valued on arm's-length terms)
rather than a domestic TP section.

## 5. Deadlines

- **Year-start notification** of likely GloBE scope (s.5(2)); DIR forms
  DMTT-24 / DMTT-25 with the 2026 deadlines above.
- **GloBE/DMTT return and payment:** 15 months after fiscal year end
  (s.5(1), s.6(1)).

## 6. Penalties and interest

- The Minister may prescribe penalties for failure to file a return, to
  pay amounts due, or other non-compliance, and may prescribe rates of
  interest on amounts payable (Act s.15).
- Collection may use s.50 of the Business Licence Act 2023 mutatis
  mutandis against third parties holding property for the debtor (s.16).
- Objection and appeal to the Tax Appeal Commission (ss.17–18); record
  keeping under s.19. Assessment windows: five years after the relevant
  taxation year, extended where an audit is opened within that period
  (Act, assessment division).

## 7. Cross-border interaction

Bahamas imposes no withholding tax on dividends, interest or royalties, so
inbound payments carry no Bahamian WHT credit for foreign parents; the
DMTT itself is the mechanism that can raise the Bahamian ETR to 15% for
in-scope groups. See bs-cross-border.

## 8. Worked examples

**Example 1 — DMTT top-up.** An in-scope group's Bahamian Constituent
Entities have GloBE income BSD 10,000,000 and covered taxes (including
credited business licence tax) of BSD 900,000 — an ETR of 9%. Top-up =
10,000,000 × 15% − 900,000 = BSD 600,000, due 15 months after fiscal year
end.

```oa-check
name: DMTT top-up BSD
inputs:
  income: 10000000
  covered_tax: 900000
steps:
  - etr: covered_tax / income
  - topup: income * 0.15 - covered_tax
expected:
  topup: 600000.00
```

**Example 2 — no top-up at or above 15%.** Same income; covered taxes BSD
1,600,000 (ETR 16%). Top-up = max(1,500,000 − 1,600,000, 0) = nil.

```oa-check
name: DMTT nil when ETR above 15%
inputs:
  income: 10000000
  covered_tax: 1600000
steps:
  - topup: max(income * 0.15 - covered_tax, 0)
expected:
  topup: 0.00
```

## 9. Ask the client first

1. Is the group in GloBE scope (EUR 750m, two of four years)? Did the
   entity file the DMTT-24/DMTT-25 notifications?
2. What covered taxes exist — business licence tax credits included?
3. What is the fiscal year end? (Return and payment fall 15 months later.)
4. Are elections under the GloBE Rules made in the prescribed form?

## 10. Sources

- [Domestic Minimum Top-Up Tax Bill/Act 2024 — full text (OPM PDF)](https://opm.gov.bs/wp-content/uploads/2024/08/Domestic-Minimum-Top-Up-Tax-Bill-2024.pdf) — ss.1–6, 15–19; read 2026-10-23.
- [Introduction of a Domestic Minimum Top-Up Tax in the Bahamas (OPM explainer PDF)](https://opm.gov.bs/wp-content/uploads/2024/08/Introduction-of-a-Domestic-Minimum-Top-Up-Tax-in-the-Bahamas.pdf) — read 2026-10-23.
- [OPM — Bahamas CIT / Pillar Two portal](https://opm.gov.bs/bahamascitpillar2/) — read 2026-10-23.
- [DIR — D.M.T.T. page (notification, forms DMTT-24/25, deadlines)](https://inlandrevenue.finance.gov.bs/dmtt/) — read 2026-10-23.
- [DIR — DMTT FAQs](https://inlandrevenue.finance.gov.bs/faqs-dmtt/) — read 2026-10-23.

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
