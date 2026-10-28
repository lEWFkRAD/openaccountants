---
name: aw-corporate-tax
description: >-
  Use for Aruba corporate income tax (winstbelasting) questions: the 22%
  flat rate (reduced from 25% on 1 January 2023, AB 2022 no. 161),
  pro-rata rate blending for financial years straddling the change,
  deduction limits (investment deduction 10% local assets, real-estate
  depreciation floor at 50% bodemwaarde, 15% nominal-tax recipient rule
  on intra-group interest), the DGA excessive-debt deemed dividend, and
  the 22%-rate worked examples. Trigger on Aruba winstbelasting, Aruba
  corporate tax rate, Aruba company. Source-cited draft; DIMP verified
  2026-10-27; dividend rate needs-sources.
jurisdiction: AW
category: international
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-28
version: 0.2
---

# Aruba corporate income tax (winstbelasting)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status (2026-10-27):** DIMP (Departamento di Impuesto) pages verified HTTP 200 with real content: <https://www.impuesto.aw/winstbelasting> and <https://www.impuesto.aw/belastingplan_2023> (22% rate text, investment deduction, depreciation floor, DGA debt rule, dividend-rate changes). **needs-sources:** the Landsverordening winstbelasting article numbers (statute PDF not parsed this run), the 2026 corporate return filing deadline, and the current dividendbelasting headline rate (the /dividendbelasting page 404s; only /dividendbelasting-home resolves).

## 1. Who this applies to

- **Aruba-registered companies (winstbelasting subject):** nv, avw and other bodies established in Aruba — taxed on their whole profits.
- **Permanent establishments of foreign companies** — taxed on profits attributable to the Aruba PE.
- **Sole proprietors and partnerships** fall in the inkomstenbelasting (individual) sphere, not winstbelasting — see `aw-individual-income-tax`.
- **DGA (director-major shareholder):** a DGA holding ≥25% (with spouse) is subject to the excessive-private-debt deemed-dividend rule (see §6).

## 2. Rates and key rules

| Item | Value | Source |
|---|---|---|
| Corporate income tax (winstbelasting) | **22%** flat from 1 Jan 2023 (was 25%) | DIMP belastingplan_2023, verified 2026-10-27 |
| Straddling financial year | Pro-rata by days in each rate period | DIMP belastingplan_2023, verified 2026-10-27 |
| Investment deduction | 10% (local investments only from 1 Jan 2023) | DIMP belastingplan_2023 |
| Real-estate depreciation | Capped at bodemwaarde = 50% of the property's value | DIMP belastingplan_2023 |
| Interest deduction anti-abuse | Recipient must be subject to nominal tax ≥15% | DIMP belastingplan_2023 |
| DGA excessive private debt | Debt > Afl. 500,000 → fictitious dividend; threshold uprated by prior deemed amounts; pre-2023 loans grandfathered to 31 Dec 2024 | DIMP belastingplan_2023 |
| Dividend withholding on distributions | Rate **needs-sources** (5% listed-company and 0% IPC rates abolished) | DIMP dividendbelasting-home + belastingplan_2023 |

## 3. Base and mechanics

- **Taxable profit** follows the commercial accounts with statutory adjustments: the 10% investment deduction (local assets only), the 50% bodemwaarde depreciation floor on real estate, and the 15%-nominal-tax recipient condition on related-party interest (all DIMP belastingplan_2023, verified 2026-10-27).
- **Pro-rata rate blending:** for a financial year that straddles 1 January 2023, DIMP states the rate is computed pro rata on the days falling in 2022 (25%) and 2023 (22%) — the same mechanism applies to any future rate change.
- **Losses:** carry-forward mechanics **needs-sources** (statute PDF not parsed this run).
- **Dividend withholding:** the paying Aruba body withholds dividend tax when profits are made available to shareholders (DIMP dividendbelasting-home, verified 2026-10-27); objections to the return within 2 months of payment.

## 4. Deadlines and filings

- Corporate return deadline for 2026: **needs-sources** (DIMP winstbelasting page links the forms; the statutory term not parsed this run).
- **Assessment payment term:** usually 2 months from the assessment (sometimes 1 or more months — read the assessment); due date is the last day payment must be received; a due date on a Saturday, Sunday or recognized holiday shifts to the next working day (DIMP wanneer-moet-u-betalen, verified 2026-10-27).

## 5. Penalties and interest

- Late payment: extra costs after the due date (DIMP wanneer-moet-u-betalen, verified 2026-10-27); the surcharge/interest percentages are **needs-sources**.
- Failure to file / insufficient profit: standard Landsverordening penalties — article numbers **needs-sources**.

## 6. Cross-border notes

- **PE exposure:** foreign companies carrying on business in Aruba through a fixed establishment are winstbelasting-subject on attributable profits.
- **Group financing:** interest to a related party is deductible only if the recipient is subject to at least a 15% nominal rate (DIMP belastingplan_2023) — classic low-tax holding structures fail this test.
- **DGA deemed dividend:** private DGA debt above Afl. 500,000 is treated as a fictitious distribution (see §2) — a cross-border DGA must watch both the Aruba deemed dividend and home-country treatment.
- **Treaties:** Aruba is not automatically covered by Kingdom of the Netherlands treaties — confirm each treaty's territorial application (**needs-sources**).

## 7. Worked examples

**Example 1 — standard year.** An Aruba nv has taxable profit Afl. 500,000 for FY 2026 (all days at 22%).

```oa-check
name: aw corp standard 22
inputs:
  profit: 500000
steps:
  - tax: 0.22 * profit
  - after_tax: profit - tax
expected:
  tax: 110000.00
  after_tax: 390000.00
```

**Example 2 — straddling year (rate change).** A company with FY 1 April 2022 – 31 March 2023 (275 days at 25%, 90 days at 22%) has profit Afl. 1,000,000. DIMP: pro-rata by days.

```oa-check
name: aw corp prorata 25 to 22
inputs:
  profit: 1000000
  days25: 275
  days22: 90
steps:
  - rate: (0.25 * days25 + 0.22 * days22) / (days25 + days22)
  - tax: profit * rate
expected:
  rate: 0.242603
  tax: 242602.74
```

## 8. Ask the client first

1. Is the entity Aruba-registered or a foreign PE — and what is its financial-year end (rate blending and deadlines key off it)?
2. Any related-party loans or financing — does the recipient meet the 15% nominal-tax condition?
3. Real-estate holdings — is depreciation above the 50% bodemwaarde floor?
4. Investments — local (10% deduction eligible) or foreign assets?
5. Is a DGA privately indebted to the company above Afl. 500,000?

## 9. Sources

- Departamento di Impuesto (DIMP) — Winstbelasting: <https://www.impuesto.aw/winstbelasting> — verified 200 with text 2026-10-27.
- DIMP — Belastingplan 2023 (22% rate, investment deduction, bodemwaarde floor, 15% recipient rule, DGA debt rule, dividend-rate changes): <https://www.impuesto.aw/belastingplan_2023> — verified 200 with text 2026-10-27.
- DIMP — Dividendbelasting (withholding on making profits available; 2-month objection term): <https://www.impuesto.aw/dividendbelasting-home> — verified 200 with text 2026-10-27.
- DIMP — Wanneer moet u betalen (assessment terms, holiday shift): <https://www.impuesto.aw/wanneer-moet-u-betalen> — verified 200 with text 2026-10-27.
- Landsverordening winstbelasting (article text **needs-sources** this run).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
