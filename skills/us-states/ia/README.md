---
pack: US-IA
jurisdiction: US-IA
applicable:
  - IT-IND
  - IT-CORP
  - VAT
  - SC
  - PR
  - TP
  - XB
not_applicable: {}
as_of: 2026-10-28
---

# Iowa (US-IA) -- pack map

Iowa taxes individuals at a **flat 3.8%** (§422.5 as amended: "at a rate of three and eight-tenths percent", text read 2026-10-28), corporations at graduated **5.5%/5.5%/9%/9.8%** for tax years beginning on or after January 1, 2021, with a statutory receipts-trigger rate adjustment (§422.33, text read 2026-10-28), and sales at a 6% state rate (§423.2) plus a local option sales and service tax of not more than 1% where adopted. Employer social contributions are UI-only under ch. 96, employer-paid (wage deductions void under §96.15). State disability insurance and health-coverage mandates are not confirmed from archived statute text.

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | corrected 2026-10-28 | `ia-income-tax.md` | flat 3.8%, IA 1040, self-employed focus |
| IT-CORP corporate income | corrected 2026-10-28 | `ia-corporate-income-tax.md` | rates + receipts trigger verified against §422.33; consolidated-return detail verified against §422.37 |
| VAT sales/use | corrected 2026-10-28 | `ia-sales-tax.md` | 6% state rate (§423.2); LOST ≤1% (IAC 701-107.2); $100,000 nexus (§423.14A) |
| SC social contributions | corrected 2026-10-28 | `ia-social-contributions.md` | UI coverage tests, 1%/month interest, penalty ladder verified against ch. 96; 2026 wage base/rates listed under Not yet confirmed |
| PR payroll withholding | corrected 2026-10-28 | `ia-payroll-withholding.md` | §422.16 tiers verified; form IDs listed under Not yet confirmed |
| TP transfer pricing | corrected 2026-10-28 | `ia-transfer-pricing.md` | §422.36 fair-price/income-shifting + §422.37 consolidated verified; apportionment formula listed under Not yet confirmed |
| XB cross-border | corrected 2026-10-28 | `ia-cross-border.md` | §422.19 receipt rule, §422.17 certificate, PTE verified; 1040NR mechanics listed under Not yet confirmed |

All seven domains apply to Iowa -- no not_applicable entries.

## Key statutes (Iowa Code 2026, all text read from legis.iowa.gov 2026-10-28)

- §422.5 individual flat 3.8% · §422.33 corporate rates · §422.34 exempt corps · §422.35 net income adjustments · §422.36 returns + fair-price/income-shifting · §422.37 consolidated returns (IRC §1504(a) affiliated group) · §422.32 allocation definitions · §422.16 withholding/estimated tax · §422.16C PTE election · §422.17 no-withholding certificate · §422.19 nonresident scope · §422.40 charter cancellation · §422.63 franchise tax (financial institutions, 3.8% for tax years beginning in 2026) · ch. 96 UI (§96.1A coverage, §96.14 penalties, §96.15 employer-only) · §423.2/§423.14A sales tax and remote-seller nexus.

## Open items for reviewer

- 2026 UI taxable wage base and contribution-rate ranges (workforce.iowa.gov 403 this run).
- Iowa apportionment formula / single-sales-factor status.
- Form IDs: 4562C, 4407, IA 1040NR, W-4 Iowa.
- Whether the receipts trigger (§422.33(1)(b), $700M threshold) has fired for 2026 rates.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
