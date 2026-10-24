---
name: dm-cross-border
description: >
  Use this skill whenever asked about Dominica cross-border taxation — tax residence (183-day rule), source rules, withholding on payments to non-residents (dividends, interest, rent, royalties, management charges), the CARICOM Double Taxation Agreement, and non-resident filing duties. Trigger on phrases like "Dominica non-resident tax", "withholding Dominica remittance", "CARICOM double taxation Dominica", "183 days Dominica", "Dominica source income", "repatriate profits Dominica". Tax year 2026 draft; withholding figures verified from the IRD page 2026-10-24.
jurisdiction: DM
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Dominica cross-border taxation

## 1. Who applies

- **Resident individuals** — worldwide-style return duty: residents (including anyone physically present in Dominica more than 183 days continuously) must file by 31 March each calendar year (IRD personal-income page, read 2026-10-24).
- **Non-residents** — taxed on Dominica-source income, collected mainly through 15% withholding by the payer (ITA ss. 53, 55(13), 56(1)(b), 57 and Third Schedule — section numbers verified from the IRD withholding page, read 2026-10-24).
- **Companies** — 25% on net profit; non-resident companies taxed on Dominica-source gains/profits through the same assessable-income base.

## 2. Rates and thresholds

Withholding on payments to non-residents — **15%** on (IRD withholding page, verified 2026-10-24):

- dividends;
- interest or discounts;
- rent, lease premium or licence for immovable property;
- rent for plant, machinery, equipment or other movable property;
- royalties;
- management charges;
- commissions or fees (not employment payments under s. 57);
- annuities and other periodic payments (incl. alimony/maintenance);
- trust income distributions of the specified kinds;
- any other payment of an income nature.

Treaty overlay: the CARICOM Double Taxation Agreement Order 2008 is the instrument the IRD points companies to (corporate page, read 2026-10-24). Dominica's wider treaty network is minimal — **verify per instrument** before quoting relief.

## 3. Base

- Source concept follows the Act's assessable-income categories (gains/profits arising in or transmitted from Dominica); article-level text **needs-sources** (scanned PDF).
- Withholding base is the actual amount paid, at 15%, subject to s. 50 (IRD page wording verified 2026-10-24).

## 4. Deadlines

- Withholding remittance: due within **15 days after the end of the month** in which it was deducted; the payer files a return in the Comptroller-approved form with certificates (verified 2026-10-24).
- Non-resident company with a Dominica year: return within 3 months after financial year-end; quarterly instalments 25%/35%/40% (IRD corporate page, verified 2026-10-24).

## 5. Penalties and interest

- Unpaid withheld tax: interest at **1% per month** until paid (s. 98), on top of penalties; failure to deduct or remit is an offence (s. 121) — fine $1,000 and/or 1 year imprisonment, continuing offences add $50/month (IRD page, verified 2026-10-24).
- Incorrect/missing returns: penalty up to 10% of tax chargeable (ss. 117–126 per IRD page).

## 6. Cross-border

- No US/Colombia/China treaty — statutory 15% governs those flows.
- MAP: IRD maintains a MAP page under international tax (existence verified 2026-10-24; content **needs-sources**).
- CRS/AEOI reporting runs through the Financial Intelligence Unit regime — separate from the ITA; verify current orders.

## 7. Worked examples

**Example 1 — interest to a non-resident lender.**

```oa-check
name: Interest EC$60,000 to non-resident, 15% WHT
inputs:
  interest: 60000
steps:
  - wht: interest * 0.15
expected:
  wht: 9000
```

**Example 2 — annual management charge to an offshore parent.**

```oa-check
name: Management charge EC$36,000/yr, 15% WHT
inputs:
  charge: 36000
steps:
  - wht: charge * 0.15
expected:
  wht: 5400
```

## 8. Ask the client

1. Is the recipient a Dominica resident (183-day test) or a CARICOM national under the DTA?
2. What is the payment category under the Third Schedule list?
3. Is the payer registered/deducting and remitting within 15 days of month-end?
4. Does the non-resident have a Dominica presence creating a source/taxable-nexus question?
5. Any exchange-of-information or CbCR exposure for the group?

## 9. Sources

- [IRD — Withholding Tax](https://ird.gov.dm/tax-laws/withholding-tax) — read 2026-10-24 (categories, 15%, 15-day remittance, s. 98/121/117–126 verified).
- [IRD — Personal Income Tax](https://ird.gov.dm/tax-laws/personal-income-tax) — read 2026-10-24 (183-day rule, 31 March filing).
- [IRD — Corporate Income Tax](https://ird.gov.dm/tax-laws/corporate-income-tax) — read 2026-10-24 (25%, instalments, CARICOM DTA Order 2008).
- [IRD — International Tax](https://ird.gov.dm/international-tax) — read 2026-10-24 (CbCR/MAP pages; text not rendered — **needs-sources**).
- [Income Tax Act Ch. 67:01 (PDF)](http://www.dominica.gov.dm/laws/chapters/chap67-01.pdf) — scanned, no text layer 2026-10-24; **needs-sources** for article quotes.

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
