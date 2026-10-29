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
as_of: 2026-10-27
---

# Iowa (US-IA) — pack map

Iowa taxes individuals at a **flat 3.8%** (SF 2442 (2024) completed the flat-tax reform; §422.5 as amended, text read 2026-10-27), corporations at graduated **5.5%/5.5%/9%/9.8%** with a statutory receipts-trigger rate adjustment (§422.33, text read 2026-10-27), and sales at 6% state rate. Employer social contributions are UI-only (ch. 96, employer-paid; wage deductions void under §96.15). No state disability insurance, no state health-coverage mandate. Inheritance tax repealed effective 2025.

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | drafted (pre-existing) | `ia-income-tax.md` | flat 3.8%, IA 1040, self-employed focus |
| IT-CORP corporate income | drafted 2026-10-27 | `ia-corporate-income-tax.md` | rates + receipts trigger verified; combined-reporting detail needs-sources |
| VAT sales/use | drafted (pre-existing) | `ia-sales-tax.md` | 6% state rate |
| SC social contributions | drafted 2026-10-27 | `ia-social-contributions.md` | UI coverage tests, 1%/mo interest, penalty ladder verified; 2026 wage base/rates needs-sources |
| PR payroll withholding | drafted 2026-10-27 | `ia-payroll-withholding.md` | §422.16 tiers verified; form IDs needs-sources |
| TP transfer pricing | drafted 2026-10-27 | `ia-transfer-pricing.md` | §422.36 fair-price/income-shifting + §422.37 consolidated verified; apportionment formula needs-sources |
| XB cross-border | drafted 2026-10-27 | `ia-cross-border.md` | §422.19 receipt rule, §422.17 certificate, PTE verified; 1040NR mechanics needs-sources |

All seven domains apply to Iowa — no not_applicable entries.

## Key statutes (Iowa Code 2026, all text read from legis.iowa.gov 2026-10-27)

- §422.5 individual flat 3.8% · §422.33 corporate rates · §422.34 exempt corps · §422.35 net income adjustments · §422.36 returns + fair-price/income-shifting · §422.37 consolidated returns (IRC §1504(a) affiliated group) · §422.32 allocation definitions · §422.16 withholding/estimated tax · §422.16C PTE election · §422.17 no-withholding certificate · §422.19 nonresident scope · §422.40 charter cancellation · §422.63 franchise tax (financial institutions, 3.8% for 2026) · ch. 96 UI (§96.1A coverage, §96.14 penalties, §96.15 employer-only).

## Open items for reviewer

- 2026 UI taxable wage base and contribution-rate ranges (workforce.iowa.gov 403 this run).
- Iowa apportionment formula / single-sales-factor status.
- Form IDs: 4562C, 4407, IA 1040NR, W-4 Iowa.
- Whether the receipts trigger (§422.33(1)(b), $700M threshold) has fired for 2026 rates.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Iowa questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
