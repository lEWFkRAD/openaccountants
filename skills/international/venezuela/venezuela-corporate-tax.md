---
name: venezuela-corporate-tax
description: >-
  Use when computing or planning Venezuelan corporate income tax (ISLR
  — Impuesto Sobre la Renta) for sociedades anónimas and other legal
  entities: the Tarifa Nº 2 corporate schedule (22% band 2,000–3,000 UT,
  34% over 3,000 UT), special flat rates (40% banks/financial/insurance,
  50% oil exploitation), the 34% withholding on dividends, the Art. 38
  1:1 thin-capitalization limit, 3-year loss carryforward capped at 25%
  of current-year income, and the 31 March filing deadline. Trigger on
  Venezuela corporate tax, ISLR tasa 34%, impuesto sobre la renta
  sociedades, contribuyentes especiales ISLR. Source-cited draft;
  SENIAT site returned 403 this run.
jurisdiction: VE
category: international
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-27
version: 0.1
---

# Venezuela corporate income tax (ISLR)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status (2026-10-27):** figures carry the ISLR Law (Ley de ISLR, G.O. 6.079 E., 22 Dec 2015, as amended) and PwC Worldwide Tax Summaries citations (reviewed Jan 2026) established in the sibling `venezuela-income-tax` / `venezuela-tax-optimization` skills. **seniat.gob.ve returned HTTP 403 to every request 2026-10-26** and taxsummaries.pwc.com rate-limited (429/503) during this run — the corporate-rate and TP article numbers are flagged **needs-sources** below. All amounts are in Tax Units (UT; VES 43.00/UT per Providencia SNAT/2025/0048, G.O. No. 43,140, effective 2 June 2025 — re-confirm the UT in force at filing).

## 1. Who this applies to

- **Sociedades anónimas (C.A.) and other commercial companies** fiscally domiciled in Venezuela (place of effective management in Venezuela — Art. 36 LISLR): taxed on **worldwide** income.
- **Foreign companies with a permanent establishment or fixed base in Venezuela**: Venezuelan-source income attributable to that base.
- **Foreign companies without a PE**: Venezuelan-source income only, typically collected by 34% withholding at source.
- **Contribuyentes especiales** (designated under Providencia SNAT/2025/000091): taxpayer-specific filing calendar; do not compute their deadlines from the general calendar.

## 2. Rates and key rules

| Item | Value | Source |
|---|---|---|
| Corporate rate schedule (Tarifa Nº 2, Art. 50 LISLR) | Band 2,000–3,000 UT: **22%** (fixed deduction 140 UT); over 3,000 UT: **34%** (fixed deduction 500 UT) | Ley del ISLR Art. 50 (carried from `venezuela-tax-optimization`) |
| Special rate — banks, financial institutions, insurance | **40%** | PwC — Venezuela, corporate income (reviewed Jan 2026) |
| Special rate — oil/gas exploitation | **50%** | PwC — Venezuela, corporate income (reviewed Jan 2026) |
| Dividend withholding (domestic) | **34%** flat | Ley del ISLR (carried from `venezuela-tax-optimization`) |
| Non-resident flat rate on VE-source income | **34%** | PwC (reviewed 12 Jan 2026) |
| Thin capitalization (Art. 38 LISLR) | Related-party debt/equity **1:1**; interest on the excess is non-deductible | ISLR Law Art. 38 (carried from `venezuela-tax-optimization`) |
| Loss carryforward | **3 years**, annual offset capped at **25%** of current-year taxable income; foreign losses offset foreign-source income only | PwC (reviewed 12 Jan 2026) |
| Tax year | Calendar year; non-wage businesses may elect an alternative 12-month period | PwC (reviewed 12 Jan 2026) |

**needs-sources:** the exact UT bands of Tarifa Nº 2 for tax year 2026 (bands above are the LISLR Art. 50 schedule carried from the existing skills at the 2025 UT), and the ISLR article number for the arm's-length rule (see `venezuela-transfer-pricing`).

## 3. Base and mechanics

- **Taxable income** = gross income (including inflation adjustments historically applied; hyperinflationary environment — re-confirm current adjustment regime with SENIAT practice) less allowed deductions, less the Tarifa Nº 2 fixed deduction (sustraendo).
- **Deductibility** follows the LISLR Art. 27–38 rules (ordinary, necessary, proportional to income; Art. 38 debt/equity limit) — see `venezuela-income-tax` §deductibility tables for the line-by-line treatment; the same rules apply to corporate taxpayers.
- **Withholding regime:** purchases from and payments to service providers carry ISLR withholding on the payer's return (Forma 33/31); dividends distributed carry 34% withholding credited against the shareholder's own ISLR.
- **Estimated payments** (pagos anticipados) apply to formal businesses; special taxpayers follow their SNAT calendar.

## 4. Deadlines and filings

- **Definitive ISLR return:** **31 March** of the following year — no extension (PwC, reviewed 12 Jan 2026).
- **Contribuyentes especiales:** windows set individually by the SENAT designation resolution (SNAT/2025/000091).
- Monthly withholding (retenciones) filings and the annual information returns follow the SENIAT resolutions of general application.

## 5. Penalties and interest

- Since the 2020 COT reform, pecuniary fines are multiples of the **BCV official rate of the highest-value currency** at payment date (effectively USD) — COT Art. 91; failure-to-file ~150–300× (COT Arts. 103/155; TSJ decisions).
- Late payment interest: market active rate × 1.2 (COT).
- Late payment within one year: 0.28% of the amount owed per day, capped at 100% (Grant Thornton / Galac, carried from `venezuela-payroll`).
- Special taxpayers: formal-duty penalties increased 200% (COT Art. 108).

## 6. Cross-border notes

- Dividends, interest and royalties to non-residents: 34% withholding, reducible only by an applicable treaty (~40 in force, PwC Jan 2026) — see `venezuela-cross-border-tax`.
- Thin-cap Art. 38 bites hardest on foreign-parent debt funding — see `venezuela-transfer-pricing`.
- Venezuela's treaty network includes Spain (0% dividend WHT for qualifying corporate shareholders), US (5%/15%), Mexico (5%), France (0%/15%), Canada (10%/15%), Brazil (10%/15%) — carried from `venezuela-tax-optimization`.

## 7. Worked examples

**Example 1 — industrial C.A., 200,000 UT taxable income.** A Venezuelan C.A. (not a special-rate entity) has taxable income of 200,000 UT (≈ VES 8,600,000 at UT 43).

```oa-check
name: ve corporate 34pct band
inputs:
  ti_ut: 200000
  ut_ves: 43
steps:
  - tax_ut: 0.34 * ti_ut - 500
  - tax_ves: tax_ut * ut_ves
expected:
  tax_ut: 67500.00
  tax_ves: 2902500.00
```

**Example 2 — bank, 50,000 UT taxable income.** A licensed bank earns 50,000 UT. The 40% special flat rate applies (PwC, corporate income, reviewed Jan 2026).

```oa-check
name: ve bank 40pct special rate
inputs:
  ti_ut: 50000
  ut_ves: 43
steps:
  - tax_ut: 0.40 * ti_ut
  - tax_ves: tax_ut * ut_ves
expected:
  tax_ut: 20000.00
  tax_ves: 860000.00
```

## 8. Ask the client first

1. Is the entity a bank/insurer (40%), oil exploitation (50%), or general taxpayer (Tarifa Nº 2)?
2. Is it designated **contribuyente especial**? Its whole calendar and documentation regime differ.
3. Related-party debt from the foreign parent — what is the debt/equity ratio today (Art. 38 1:1)?
4. Any losses from the last 3 years, and how much of the 25% annual offset capacity is unused?
5. Is a dividend distribution planned — has the 34% withholding been priced in, and does a treaty reduce it?

## 9. Sources

- Ley de ISLR, Gaceta Oficial No. 6.079 (Especial), 22 December 2015, as amended — Art. 50 (Tarifas), Art. 38 (thin capitalization).
- Providencia Administrativa SNAT/2025/0048, G.O. No. 43,140 — UT = VES 43.00 from 2 June 2025.
- PwC Worldwide Tax Summaries — Venezuela, corporate income / tax administration: <https://taxsummaries.pwc.com/venezuela/corporate/incomes> — verified 200 with text 2026-10-27 (rate-limited thereafter).
- SENIAT: <https://www.seniat.gob.ve/portal/portal/seniat> — **needs-sources**: HTTP 403 to direct requests 2026-10-26; re-verify the 2026 UT resolution and filing calendar before publication.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
