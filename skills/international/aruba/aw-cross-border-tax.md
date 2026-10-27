---
name: aw-cross-border-tax
description: >-
  Use when a client moves to or from Aruba, works remotely for an Aruba
  payer, or earns Aruba-source income as a non-resident: the
  buitenlandse belastingplichtige (non-resident taxpayer) filing rules,
  part-year treatment with the time-wise pro-rated tax-free amount, the
  2026 income-tax table on table income, the DGA deemed-dividend rule,
  dividend withholding posture, and the Kingdom-treaty territorial
  caveat. Trigger on Aruba non-resident tax, buitenlandse
  belastingplichtige, Aruba expat, Aruba part-year income tax.
  Source-cited draft; DIMP verified 2026-10-27; residency day-counts
  needs-sources.
jurisdiction: AW
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-27
version: 0.1
---

# Aruba cross-border and residency rules

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status (2026-10-27):** DIMP pages verified HTTP 200 with real content: <https://www.impuesto.aw/aangifte-buitenlandse-belastingplichtigen> (non-resident taxpayer definition and filing duty), <https://www.impuesto.aw/belastingplan_2023> (DGA deemed dividend, dividend-rate changes), <https://www.impuesto.aw/dividendbelasting-home> (withholding on Aruba bodies' distributions), <https://www.impuesto.aw/wanneer-moet-u-betalen> (assessment terms). The 2026 table and Afl. 30,000 tax-free amount carry from `aw-individual-income-tax` (DIMP 2026 table, verified 22 Oct 2026). **needs-sources:** the statutory residency test (day-count / domicile criteria in the Landsverordening IB), the current dividendbelasting headline rate, and the treaty territorial position.

## 1. Who this applies to

- **Non-residents with Aruba income sources (buitenlandse belastingplichtigen):** DIMP defines them as persons who **did not live in Aruba during the whole year but had Aruba income sources**, or who **lived in Aruba part of the year and had Aruba income in the non-resident period** (DIMP aangifte-buitenlandse-belastingplichtigen, verified 2026-10-27).
- **Aruba-source income categories named by DIMP:** income from Aruba real estate; income from business/profession carried on in Aruba; pensions and periodic benefits paid by the Land Aruba or APFA.
- **Part-year residents** — full-year rules apply to the resident period; the tax-free amount is pro-rated time-wise (DIMP withholding page, verified 2026-10-27).
- **DGAs of Aruba companies** — deemed-dividend exposure regardless of residence (**needs-sources** for the personal scope).

## 2. Rates and key rules

| Item | Value | Source |
|---|---|---|
| Non-resident income tax | Same 2026 table as residents: 21% (34,930–63,904), 42% (63,904–135,527), 52% (>135,527) on table income | DIMP 2026 table, carried from `aw-individual-income-tax` |
| Tax-free amount | Max Afl. 30,000; **pro-rated for part-year liability** | DIMP 2026 + withholding page, verified 2026-10-27 |
| Filing duty (non-resident) | File when a return is received or when one should reasonably know tax is due | DIMP aangifte-buitenlandse-belastingplichtigen, verified 2026-10-27 |
| Dividend withholding (Aruba bodies) | Rate **needs-sources**; 5% listed-company and 0% IPC rates abolished | DIMP belastingplan_2023, verified 2026-10-27 |
| DGA deemed dividend | Private debt > Afl. 500,000 → fictitious distribution | DIMP belastingplan_2023, verified 2026-10-27 |
| Treaties | Kingdom treaties generally for the European part only — confirm per treaty | **needs-sources** |

## 3. Base and mechanics

- **Table income** = taxable income − available tax-free amount (max Afl. 30,000, pro-rated for part-year); apply the 2026 bands and round down (carried from `aw-individual-income-tax`).
- **Source rules (DIMP list, verified 2026-10-27):** real property follows location; business/professional income follows where carried on; public-pension source follows the payer (Land Aruba/APFA).
- **Employment income** earned while working in Aruba is withheld at source via loonbelasting (see `aw-payroll-withholding`); the non-resident return reconciles the annual position.
- **Residency test:** statutory criteria **needs-sources** — settle residence before computing.

## 4. Deadlines and filings

- Non-resident return: file when DIMP sends a return or when the taxpayer should reasonably know tax is due (DIMP, verified 2026-10-27); the standard annual return calendar is **needs-sources**.
- Assessment payment: usually 2 months (sometimes 1 or more — read the assessment); due dates falling on weekends/holidays shift to the next working day (DIMP wanneer-moet-u-betalen, verified 2026-10-27).
- Emigration: DIMP maintains an "U gaat emigreren" guidance page (linked from the Particulier menu; detail **needs-sources**).

## 5. Penalties and interest

- Late payment: extra costs after the due date (DIMP wanneer-moet-u-betalen, verified 2026-10-27); percentages **needs-sources**.
- Failure to file when one should reasonably know of liability: standard penalty machinery, **needs-sources**.

## 6. Cross-border notes

- **No exit tax** was found in DIMP materials for individuals (**needs-sources** — verify before advising a departure).
- **DGA deemed dividend** (Afl. 500,000 excessive-debt rule) can create Aruba tax on a non-resident DGA — coordinate with the home country to avoid double taxation (**needs-sources** on personal scope).
- **Dividend withholding:** distributions by Aruba-registered bodies carry dividendbelasting withheld by the payer at the moment profits are made available (DIMP dividendbelasting-home, verified 2026-10-27); rate **needs-sources**.
- **CRS:** Aruba exchanges account data — home-country disclosure should assume DIMP data flows (DIMP internationaal, verified 2026-10-27).

## 7. Worked examples

**Example 1 — non-resident with Aruba rental income.** A US-resident owner's Aruba condo nets Afl. 100,000 taxable; no other Aruba income; full Afl. 30,000 tax-free amount applies (full-year source). Table income Afl. 70,000 → band 2 (42% over 63,904 + base 6,084.54).

```oa-check
name: aw xb nonresident rental
inputs:
  taxable: 100000
  vrij: 30000
steps:
  - tabel: taxable - vrij
  - tax: 6084.54 + 0.42 * (tabel - 63904)
  - tax_rounded: floor(tax)
expected:
  tabel: 70000.00
  tax: 8644.86
  tax_rounded: 8644.00
```

**Example 2 — DGA excessive debt.** A DGA owes his Aruba company Afl. 1,800,000 privately; the threshold is Afl. 500,000. The Afl. 1,300,000 excess is a fictitious distribution taxed in the top individual band (52% marginal).

```oa-check
name: aw xb dga deemed dividend
inputs:
  debt: 1800000
  threshold: 500000
  marginal: 0.52
steps:
  - excess: debt - threshold
  - tax: marginal * excess
expected:
  excess: 1300000.00
  tax: 676000.00
```

*(The fictitious-dividend base and its interaction with dividendbelasting and the progressive table are simplified — exact mechanics **needs-sources**.)*

## 8. Ask the client first

1. Resident, part-year, or non-resident for the year — where was the home and how many Aruba days (this decides the whole computation)?
2. Which Aruba income sources exist — property, business carried on in Aruba, Aruba public pension, employment?
3. Is the client a DGA (≥25% with spouse) privately indebted above Afl. 500,000?
4. Does the home country's treaty with the Kingdom extend to Aruba — check the territorial clause before claiming treaty rates?
5. Receiving distributions from Aruba bodies — what withholding was applied, and at what rate?

## 9. Sources

- DIMP — Aangifte buitenlandse belastingplichtigen (non-resident definition, sources list, filing duty): <https://www.impuesto.aw/aangifte-buitenlandse-belastingplichtigen> — verified 200 with text 2026-10-27.
- DIMP — Belastingplan 2023 (DGA debt rule, dividend-rate changes): <https://www.impuesto.aw/belastingplan_2023> — verified 200 with text 2026-10-27.
- DIMP — Dividendbelasting home (withholding trigger, 2-month objection): <https://www.impuesto.aw/dividendbelasting-home> — verified 200 with text 2026-10-27.
- DIMP — Wanneer moet u betalen (assessment terms, holiday shift): <https://www.impuesto.aw/wanneer-moet-u-betalen> — verified 200 with text 2026-10-27.
- DIMP — 2026 income/wage tax table: carried from `aw-individual-income-tax` (verified 22 Oct 2026).
- Landsverordening IB residency articles — **needs-sources** this run.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
