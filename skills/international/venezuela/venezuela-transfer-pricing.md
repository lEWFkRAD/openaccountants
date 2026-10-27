---
name: venezuela-transfer-pricing
description: >-
  Use when a Venezuelan taxpayer transacts with related parties abroad or
  domestically: the ISLR arm's-length requirement, the Art. 38 1:1
  debt-to-equity thin-capitalization limit (interest on related-party debt
  above equity is non-deductible), SENIAT reassessment powers, and
  documentation posture for contribuyentes especiales. Trigger on Venezuela
  transfer pricing, precios de transferencia, subcapitalizacion Art 38,
  related-party interest Venezuela, SENIAT arm's length. Source-cited
  draft; the arm's-length article number is needs-sources.
jurisdiction: VE
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-27
version: 0.1
---

# Venezuela transfer pricing and thin capitalization

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status (2026-10-27):** the thin-capitalization rule (1:1, interest on the excess non-deductible) is cited to **ISLR Law Art. 38** as carried from the existing `venezuela-tax-optimization` skill. **seniat.gob.ve returned HTTP 403 to every request 2026-10-26** and the PwC transfer-pricing page verified earlier this run could not be re-fetched (rate-limited). **needs-sources:** the ISLR article number establishing the general arm's-length rule and the statutory list of accepted methods, and whether a formal TP documentation filing currently exists (no dedicated annual TP return was confirmed this run).

## 1. Who this applies to

- Venezuelan tax residents (companies and individuals) transacting with **related parties abroad** — imports, exports, services, royalties, financing.
- Venezuelan companies financed by a **foreign parent or affiliate** (Art. 38 debt/equity test).
- **Contribuyentes especiales** — SENIAT scrutiny and the special-taxpayer penalty uplift (COT Art. 108, +200%) make documentation posture decisive.

## 2. Rates and key rules

| Item | Value | Source |
|---|---|---|
| Arm's-length requirement | Related-party income/expense adjusted to market conditions | ISLR Law (arm's-length article **needs-sources**); PwC — Venezuela transfer pricing (verified 200 with text 2026-10-27) |
| Thin capitalization limit | Related-party debt / equity **1:1** | ISLR Law Art. 38 |
| Consequence of exceeding 1:1 | Interest on the excess related-party debt is **non-deductible** | ISLR Law Art. 38 |
| Reassessment exposure | SENIAT may recompute related-party results; underpayment attracts interest (COT) and fines in BCV-currency multiples | COT Arts. 91/103/155 |
| Treaty overlay | ~40 treaties in force; associated-enterprise articles follow the OECD Model | PwC (Jan 2026) |

## 3. Base and mechanics

- **Scope of adjustment:** prices, margins, interest rates, royalties and service fees between related parties are tested against what independent parties would agree (condiciones de mercado).
- **Methods:** PwC's Venezuela transfer-pricing page (verified this run) describes alignment with the OECD methods (CUP, resale price, cost-plus, transactional profit methods); the statutory article list is **needs-sources** — do not cite a method article number until verified.
- **Financial transactions:** shareholder/affiliate loans face the Art. 38 1:1 cap **in addition to** the arm's-length interest test — model both limits.
- **Currency:** hyperinflation and multiple exchange-rate history mean the BCV rate used for each related-party cash flow drives both the VES amount and the adjustment — document the rate and date per flow.

## 4. Deadlines and filings

- No standalone annual TP return was confirmed this run (**needs-sources**); TP exposure travels inside the definitive ISLR return due **31 March**.
- Special taxpayers: documentation can be demanded at any time under the SNAT/2025/000091 designation powers.

## 5. Penalties and interest

- Understatement via non-arm's-length pricing: material infraction — tax plus COT interest (market active rate × 1.2) plus fines computed as multiples of the BCV highest-value currency rate at payment (COT Art. 91, 2020 reform).
- Formal-duty failures: 150–300× band (COT Arts. 103/155); special taxpayers +200% (COT Art. 108).

## 6. Cross-border notes

- Outbound royalties/services to affiliates in low-tax jurisdictions draw the most SENIAT attention; treaty relief does not cure a pricing adjustment, only the withholding rate.
- Non-deductible excess interest (Art. 38) is a permanent difference — re-plan the debt/equity mix before year-end, not after filing.
- Double taxation from a mirrored adjustment abroad: MAP available under treaties with an associated-enterprise article.

## 7. Worked examples

**Example 1 — understated export price.** A Venezuelan C.A. sells to its US parent at VES 1,000,000; the arm's-length price for the same goods to unrelated buyers is VES 1,600,000. SENIAT adjusts income upward by the difference; tax effect at the 34% band rate.

```oa-check
name: ve tp export price adjustment
inputs:
  actual: 1000000
  arm: 1600000
steps:
  - delta: arm - actual
  - tax: 0.34 * delta
expected:
  delta: 600000.00
  tax: 204000.00
```

**Example 2 — thin-cap interest disallowance.** Equity VES 1,000,000; related-party debt VES 3,000,000 (1:1 limit = VES 1,000,000; excess VES 2,000,000). Total related-party interest paid VES 500,000; the portion attributable to the excess debt (2/3 of the loan balance) is non-deductible: VES 333,333.33. Tax effect at 34%.

```oa-check
name: ve art38 thin cap interest
inputs:
  equity: 1000000
  debt: 3000000
  interest: 500000
steps:
  - excess: debt - equity
  - nd_interest: interest * excess / debt
  - tax: 0.34 * nd_interest
expected:
  excess: 2000000.00
  nd_interest: 333333.33
  tax: 113333.33
```

## 8. Ask the client first

1. Full list of related-party flows (goods, services, royalties, loans) with amounts and BCV rates used.
2. Current debt/equity ratio against the foreign parent — above 1:1 today?
3. Any contemporaneous comparability documentation, even informal — SENIAT requests it without warning for special taxpayers.
4. Has any related-party price ever been adjusted by SENIAT or a foreign authority (mirror-adjustment / MAP posture)?
5. Are dividends being used to fix an over-leveraged balance sheet — 34% dividend withholding cost modelled?

## 9. Sources

- Ley de ISLR, G.O. 6.079 (Especial), 22 Dec 2015, as amended — Art. 38 (debt/equity); arm's-length article **needs-sources**.
- PwC Worldwide Tax Summaries — Venezuela, transfer pricing: <https://taxsummaries.pwc.com/venezuela/corporate/transfer-pricing> — verified 200 with text 2026-10-27 (rate-limited on re-fetch).
- Código Orgánico Tributario Arts. 91, 103, 108, 155 (penalty mechanism; carried from `venezuela-income-tax` / `venezuela-payroll`).
- SENIAT: <https://www.seniat.gob.ve/portal/portal/seniat> — HTTP 403 2026-10-26; **needs-sources** for the current TP documentation resolution.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
