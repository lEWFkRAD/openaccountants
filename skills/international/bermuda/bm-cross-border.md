---
name: bm-cross-border
description: >
  Bermuda cross-border tax reference for 2026. Covers Bermuda's limited
  double-taxation treaty network (including the 1987 US-Bermuda tax
  information-gathering agreement and the Bahrain DTA amendment aligned to
  BEPS), the absence of dividend, interest, royalty and capital-gains
  withholding, foreign tax credits under Part 4 of the Corporate Income Tax
  Act 2023 for in-scope MNE groups, permanent establishment definitions,
  and economic substance / exchange-of-information obligations (FATCA,
  CRS, CARF, CbCR). Trigger on Bermuda cross-border, treaty, withholding,
  permanent establishment, EOI, economic substance. Source-cited draft.
jurisdiction: BM
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Bermuda cross-border

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the consolidated Corporate
Income Tax Act 2023 (CITA PDF), the gov.bm news item on the Bahrain DTA
amendment, the gov.bm international-conventions article, and the CITA
exchange-of-information pages. Bermuda's treaty network is narrow; the
authoritative consolidated list is **needs-sources** (see caveat).

**Source status caveat:** gov.bm publishes no consolidated, machine-readable
DTA register. The gov.bm "International Conventions or Treaties" article
lists human-rights and maritime conventions, not tax treaties. Treat the
treaty inventory below as partial: confirm each treaty's status and text
with CITA or the Bermuda Attorney General's Chambers before relying on it.

## 2. Who this applies to

- In-scope MNE groups (EUR 750m+) with Bermuda constituent entities — the
  foreign tax credit, permanent establishment and CbCR rules below apply to
  them via the Corporate Income Tax Act 2023.
- All Bermuda entities remain subject to economic substance (ES Act) and
  exchange-of-information obligations (FATCA, CRS, CARF) regardless of CIT
  scope — administered by CITA.

## 3. Withholding and outbound payments (rates table)

| Item | Position | Source |
|---|---|---|
| Dividends to non-residents | No withholding tax | Corporate Income Tax Act 2023 imposes no WHT division; long-standing position |
| Interest, royalties, service fees to non-residents | No withholding tax | as above |
| Capital gains of non-residents | No Bermuda tax (outside CIT scope; in-scope groups taxed on net income per the Act) | as above |
| CIT (in-scope only) | 15% on net taxable income of Bermuda constituent entities | Corporate Income Tax Act 2023, section 4 |

## 4. Treaty network

- Bermuda's tax-treaty network is limited. A US-Bermuda agreement dating
  from 1988 (tax information-gathering; the historic instrument was
  transferred to the Bermuda Archives in 2025 per gov.bm) underpins the
  FATCA relationship.
- A double-taxation agreement with the Kingdom of Bahrain was amended with
  an amendment signed per the gov.bm news item (read 2026-10-23), aligned
  to the OECD/G20 Inclusive Framework BEPS minimum standards, including
  treaty-abuse prevention and strengthened dispute resolution.
- The Act defines "tax treaty" as an agreement for the avoidance of double
  taxation on income and capital, and states nothing in the Act affects
  the meaning of terms in any tax treaty.
- Full consolidated DTA list: **needs-sources**.

## 5. Permanent establishment and source rules in the Act

The CIT Act's "permanent establishment" definition keys to treaty practice:
a place of business treated as a PE under an applicable tax treaty where
the jurisdiction taxes the income per an Article 7-type provision; failing
a treaty, a place of business whose income the jurisdiction taxes on a net
basis like its own residents; and for non-corporate-tax jurisdictions, a
place of business that would be a PE under the OECD Model. Fiscal
transparency and PE attribution rules (Part 5) determine which cross-border
income lands in the Bermuda base.

## 6. Foreign tax credits (in-scope groups)

Part 4 of the Act gives a foreign tax credit division: creditable foreign
taxes (including foreign withholding taxes on dividends, interest, rents
and royalties, and taxes imposed in lieu of income tax) are computed,
adjusted and allocated to Bermuda constituent entities, and credited
against Bermuda CIT. QDMTT amounts accrued under qualified domestic
minimum top-up taxes count as covered foreign taxes for GloBE purposes.

## 7. Deadlines

- CIT instalments and returns: CITA calendar (see bm-transfer-pricing).
- EOI filings (FATCA/CRS/CARF/CbCR): CITA publishes separate EOI filing &
  payment deadlines; page renders client-side — **needs-sources** for exact
  dates.

## 8. Worked examples

**Example 1 — foreign tax credit against Bermuda CIT.** An in-scope Bermuda
constuent entity has net taxable income USD 10,000,000 and paid USD 400,000
of creditable foreign withholding tax. Bermuda CIT at 15% = USD 1,500,000;
credit reduces it to USD 1,100,000.

```oa-check
name: FTC against 15% CIT USD
inputs:
  income: 10000000
  foreign_tax: 400000
steps:
  - cit_before: income * 0.15
  - cit_after: cit_before - foreign_tax
expected:
  cit_after: 1100000.00
```

**Example 2 — low-foreign-tax case, credit fully absorbed.** Same income;
creditable foreign tax USD 2,000,000 exceeds the Bermuda CIT of USD
1,500,000, so Bermuda CIT payable is nil (excess credit treatment follows
Part 4 allocation rules — confirm carry-forward mechanics).

```oa-check
name: FTC capped at Bermuda CIT USD
inputs:
  income: 10000000
  foreign_tax: 2000000
steps:
  - cit_before: income * 0.15
  - cit_payable: max(cit_before - foreign_tax, 0)
expected:
  cit_payable: 0.00
```

## 9. Ask the client first

1. Which jurisdictions receive payments from the Bermuda entity — and does
   the counterparty jurisdiction impose its own withholding (Bermuda
   imposes none)?
2. Is the group in CIT scope, and where are creditable foreign taxes
   arising?
3. Is there a treaty between Bermuda and the counterparty jurisdiction at
   all? (Network is narrow — verify before claiming treaty benefits.)
4. Are FATCA/CRS/CARF/CbCR registrations and filings current with CITA?

## 10. Sources

- [Corporate Income Tax Act 2023 — consolidated full text (CITA PDF)](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) — section 2 (permanent establishment, tax treaty), Part 4 foreign tax credits; read 2026-10-23.
- [gov.bm — Bermuda signs amendment to the Double Taxation Agreement with the Kingdom of Bahrain](https://www.gov.bm/news/bermuda-signs-amendment-double-taxation-agreement-kingdom-bahrain) — read 2026-10-23.
- [gov.bm — Attorney General transfers historic 1988 US-Bermuda tax treaty to Bermuda Archives](https://www.gov.bm/news/attorney-general-transfers-historic-1988-us-bermuda-tax-treaty-bermuda-archives) — read 2026-10-23.
- [CITA — Exchange of Information / Tax Transparency (FATCA, CRS, CbCR, CARF)](https://www.cita.bm/exchange-of-information-eoi1) — read 2026-10-23.
- [CITA — EOI Filing & Payment Deadlines](https://www.cita.bm/exchange-of-information-filing-payment-deadlines) — read 2026-10-23 (client-side render; needs-sources).
- [gov.bm — International Conventions or Treaties](https://www.gov.bm/articles/international-conventions-or-treaties) — read 2026-10-23 (non-tax list; confirms no consolidated DTA register).

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
