---
name: venezuela-cross-border-tax
description: >-
  Use when a client moves to or from Venezuela, works remotely for a
  Venezuelan payer, or repatriates Venezuelan-source income: ISLR
  residency (worldwide vs Venezuelan-source taxation), the 34% flat
  non-resident regime with 90%-of-gross base for professional services,
  treaty-reduced dividend/interest/royalty withholding (~40 treaties),
  and the 31 March non-resident filing posture. Trigger on Venezuela
  tax residency, no residente ISLR 34%, retencion dividendos convenio,
  expatriate Venezuela. Source-cited draft; SENIAT 403 this run.
jurisdiction: VE
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-27
version: 0.1
---

# Venezuela cross-border and residency rules

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status (2026-10-27):** residency/source rules and non-resident rates carry the PwC Worldwide Tax Summaries citations (reviewed 12 Jan 2026) established in `venezuela-income-tax`; treaty dividend rates carry `venezuela-tax-optimization` (PwC withholding page, Jan 2026). **seniat.gob.ve returned HTTP 403 to every request 2026-10-26.** **needs-sources:** the statutory day-count / centre-of-vital-interest test details in the LISLR articles (PwC summary verified; article text not retrieved this run) and the current treaty list in force at 2026.

## 1. Who this applies to

- **Individuals becoming Venezuelan residents** — taxed on **worldwide** income under Tarifa Nº 1.
- **Individuals leaving Venezuela** — Venezuelan-source income remains taxable after departure.
- **Non-residents earning Venezuelan-source income** — salary/services performed in Venezuela, rent from Venezuelan property, dividends/interest/royalties from Venezuelan payers.
- **Foreign resident with a fixed base in Venezuela** — national- and foreign-source income attributable to that base (PwC, reviewed 12 Jan 2026).

## 2. Rates and key rules

| Item | Value | Source |
|---|---|---|
| Resident | Worldwide income, Tarifa Nº 1 (6%–34% in UT) | LISLR; PwC reviewed 12 Jan 2026 |
| Non-resident | Venezuelan-source income only, **34% flat**, withheld at source | PwC reviewed 12 Jan 2026 |
| Non-resident professional (non-business) services | **34% on 90% of gross** (effective ~30.6%) | PwC reviewed 12 Jan 2026 |
| Dividend WHT (domestic rate) | **34%** | Ley del ISLR |
| Treaty dividend WHT examples | Spain 0% qualifying corporates / 10% other; US 5% (≥10% holding) / 15%; Mexico 5%; France 0%/15%; Canada 10% (≥25%) / 15%; Brazil 10%/15% | PwC withholding page (Jan 2026), carried from `venezuela-tax-optimization` |
| Treaties in force | ~40 | PwC (Jan 2026) |
| Filing | Residents: definitive return 31 March, no extension | PwC reviewed 12 Jan 2026 |

## 3. Base and mechanics

- **Residency triggers** (LISLR, as summarized by PwC — verified 2026-10-27; article text needs-sources): presence in Venezuela, habitual residence, centre of vital/economic interests. Residency status must be settled before any computation (rule R-VE-1 in `venezuela-income-tax`).
- **Source rules:** services are Venezuelan-source where performed; directors' fees, rents from Venezuelan real property, and returns from Venezuelan securities follow the payer/asset location.
- **Withholding is usually the final tax** for non-residents — no annual return when the payer withheld correctly; a return/credit path exists for over-withheld amounts and treaty refunds.
- **Foreign tax credit:** residents crediting foreign tax follow the LISLR limitation rules (carried from `venezuela-income-tax`); confirm per-country posture with SENIAT practice.

## 4. Deadlines and filings

- Resident definitive ISLR return: **31 March**, no extension (PwC, reviewed 12 Jan 2026).
- Part-year: a resident for any part of the year files the definitive return for that year; non-residents rely on the payer's withholding.
- Treaty relief at source requires documentation of the beneficial owner (residence certificate of the other state) — SENIAT form requirements **needs-sources**.

## 5. Penalties and interest

- Payer failed to withhold: the payer owes the tax plus COT interest and fines (BCV-currency multiples, COT Art. 91 mechanism) — the cross-border failure mode is almost always on the payer side.
- Non-resident underpayment discovered later: same COT regime; collection runs against Venezuelan assets/payers.

## 6. Cross-border notes

- **Hyperinflation/USD:** USD-denominated compensation must be converted at the applicable BCV rate; the rate and date drive the ISLR figure (flag in `venezuela-income-tax`).
- **No exit tax** was confirmed for individuals (**needs-sources** — verify before advising a departure).
- **Remittance posture:** residents are taxed on accrual worldwide, not on remittance — moving cash out does not defer ISLR.
- Treaty shopping through a ~40-treaty network is SENIAT-reviewed; beneficial-ownership substance matters (carried from `venezuela-tax-optimization`).

## 7. Worked examples

**Example 1 — non-resident consultant invoice.** A US consultant (no PE) invoices a Caracas client VES 1,000,000 for services performed in Venezuela. Base = 90% of gross; WHT = 34%.

```oa-check
name: ve xb nonresident services
inputs:
  gross: 1000000
steps:
  - base: 0.90 * gross
  - wht: 0.34 * base
  - net: gross - wht
expected:
  base: 900000.00
  wht: 306000.00
  net: 694000.00
```

**Example 2 — treaty dividend rate.** A US corporate shareholder holding ≥10% of a Venezuelan C.A. receives a VES 500,000 dividend. Treaty rate 5% vs domestic 34%.

```oa-check
name: ve xb treaty dividend us
inputs:
  div: 500000
steps:
  - domestic: 0.34 * div
  - treaty: 0.05 * div
  - saving: domestic - treaty
expected:
  domestic: 170000.00
  treaty: 25000.00
  saving: 145000.00
```

## 8. Ask the client first

1. Resident or non-resident for the year — days present, family/economic centre (this decides the whole computation).
2. Where were services physically performed, and who is the Venezuelan payer (withholding agent)?
3. Holding percentage and chain above a Venezuelan company — does a treaty rate apply, and is beneficial-ownership documentation available?
4. Any foreign taxes paid on the same income — credit posture for residents.
5. Planned departure/arrival date — part-year filing and post-departure Venezuelan-source exposure.

## 9. Sources

- Ley de ISLR, G.O. 6.079 (Especial), 22 Dec 2015, as amended — residency, source, non-resident rates (article text **needs-sources** this run).
- PwC Worldwide Tax Summaries — Venezuela, individual residence and source: <https://taxsummaries.pwc.com/venezuela/individual/residence-and-domicile> — verified 200 with text 2026-10-27; withholding page (Jan 2026 review) carried from `venezuela-tax-optimization`.
- Venezuela treaty network (~40; Spain/US/Mexico/France/Canada/Brazil dividend rates as listed) — PwC withholding page, Jan 2026.
- SENIAT: <https://www.seniat.gob.ve/portal/portal/seniat> — HTTP 403 2026-10-26.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
