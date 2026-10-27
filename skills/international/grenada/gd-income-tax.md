---
name: gd-income-tax
description: >
  Grenada individual income tax reference for 2026. Covers the flat 30% rate on
  chargeable income under Income Tax Act Cap. 149 Fifth Schedule, residence and
  source basis, employment income and PAYE interaction (Fourth Schedule, 30%
  deduction with the EC$60,000 accumulation trigger), net-of-tax gross-up,
  annual return within 90 days, and interest on unpaid tax. Use for Grenada
  personal income tax working papers and individual filings. Independent
  accountant review pending.
jurisdiction: GD
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Grenada individual income tax v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows; not reviewed for any specific person's facts. Do not file, pay, or take a position on it without review by a qualified Grenadian professional.

## 1. Scope and sources

Grenada's individual income tax is imposed by the Income Tax Act Cap. 149 (consolidated PDF to Act No. 2 of 2010: [Grenada Parliament](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf), read 2026-10-27; chapter page [laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act), read 2026-10-27). Residents are taxable on worldwide income; non-residents on income accruing in or derived from Grenada (s.2 residence definitions, read 2026-10-27). The year of assessment follows the calendar year for individuals. This skill covers the individual charge; employment withholding mechanics sit in `gd-payroll-withholding`, non-resident payment withholding in `gd-cross-border`, NIS in `gd-social-contributions`.

**Source status caveat:** the consolidated PDF consolidates amendments only to Act No. 2 of 2010. Amendment acts 2011–2026 were not retrievable in consolidated form on 2026-10-27 (gazettes.gov.gd reachable but no consolidated reprint found; www.ird.gd tax pages returned HTTP 500). The 30% flat rate is as per the Fifth Schedule in the consolidated text; the IRD G-TAX FAQ (read 2026-10-27) describes PAYE registration for individuals earning over EC$3,000 monthly / EC$36,000 annually, consistent with a taxable-but-not-withheld boundary rather than a rate change. **needs-sources:** confirm no post-2010 amendment altered Fifth Schedule rates.

## 2. Who applies

- **Resident individuals** (including "ordinarily resident" per s.2 definitions in the consolidated PDF): taxable on income from all sources, in and outside Grenada.
- **Non-resident individuals:** taxable on Grenada-source income; employment income of non-residents is subject to Comptroller-directed withholding (Fourth Schedule para 2(5)).
- **Minors/wards and incapacitated persons:** chargeable via representative taxpayers (Cap. 149 representative-taxpayer provisions).
- The G-TAX FAQ (read 2026-10-27) flags the individual registration benchmark as remuneration above EC$3,000 monthly or EC$36,000 annually — treat below-threshold earners as still within the charge but commonly outside PAYE registration practice.

## 3. Rates and base

| Item | Amount | Source |
|---|---|---|
| Rate on individual chargeable income | **30%** flat | Cap. 149 Fifth Schedule [Rates of Tax, s.56], consolidated PDF read 2026-10-27 |
| PAYE deduction rate | 30% of chargeable remuneration | Fourth Schedule para 2(1), same PDF |
| Accumulation trigger | at EC$60,000 accumulated remuneration in a basis period, excess taxed at 30% for the remainder of the period | Fourth Schedule para 2(2) |

**Base:** assessable income (employment, business, rent, investment, pensions) less allowable deductions (ss.36–38 restrictions, capital allowances Third Schedule, loss relief s.39) = chargeable income. No personal reliefs appear in the consolidated text's computation provisions — **needs-sources:** verify against post-2010 amendments before assuming none exist.

## 4. Deadlines

- **Annual return:** furnish the return of income within **90 days after the end of the basis period** (s.65(1), consolidated PDF read 2026-10-27); for calendar-year individuals that is 31 March.
- **2025 year of assessment:** the IRD extended the PIT/CIT/Annual Stamp Tax filing-and-payment deadline to **30 April 2026** ([Finance Ministry press release PDF](https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf), read 2026-10-27) — extensions are gazetted/announced per year; check current-year announcements.
- **Individuals with business income:** monthly one-twelfth instalments under s.93 (see `gd-corporate-income-tax` for the instalment mechanics that also apply to non-employment resident persons).
- Employees whose only income is PAYE-remunerated are outside s.93 instalments (s.93(1)(b) exception).

## 5. Penalties and interest

- **Interest on unpaid assessed tax:** 1.5% per month or part-month (s.95, consolidated PDF read 2026-10-27).
- **Interest on unpaid withheld/deducted tax:** 2% per month (s.97) — see `gd-payroll-withholding`.
- **Failure to furnish a return / incorrect return:** penalties under ss.111–112; notice before imposition required (s.114); mitigation/compounding under s.123.
- **Failure to comply with a s.68 information notice:** penalty up to $1,000 (s.113).

## 6. Cross-border

Residence definitions in s.2 govern; a non-resident's Grenada-source employment income is charged through Comptroller-directed PAYE (Fourth Schedule para 2(5)); passive payments to non-residents are final 15% withholding (s.50 — see `gd-cross-border`). Double-taxation relief orders exist under s.43; **needs-sources:** the consolidated PDF lists no subsidiary legislation under Cap. 149, so the in-force DTR orders must be pulled from the gazette before crediting foreign tax.

## 7. Worked examples

**Example 1 — salaried employee, annual chargeable income.** Chargeable income EC$48,000 for the year.

```oa-check
name: flat 30% individual charge
inputs:
  chargeable: 48000
  rate: 0.30
steps:
  - tax: chargeable * rate
  - monthly_equiv: tax / 12
expected:
  tax: 14400
  monthly_equiv: 1200
```

PAYE of 30% through the year (Fourth Schedule) should settle this; the 90-day return reconciles any Comptroller-directed variation.

**Example 2 — net-of-tax (tax-free) monthly salary.** Employer agrees to pay EC$3,500 per month free of tax.

```oa-check
name: net-of-tax gross-up at 30 percent
inputs:
  net_month: 3500
  rate: 0.30
steps:
  - deemed_gross: net_month / (1 - rate)
  - tax: deemed_gross * rate
expected:
  deemed_gross: 5000
  tax: 1500
```

Fourth Schedule para 4 deems the grossed-up amount paid and the difference payable by the employer to the Comptroller.

## 8. Ask the client

- Residence status and days present in Grenada for the year (s.2 definitions decide worldwide vs source-only charging).
- All employment income sources — multiple concurrent employments require a Comptroller-directed deduction rate (Fourth Schedule para 2(4)).
- Whether any income is exempt (NIS benefits are exempt per Amendment Act 12 of 2015 — [PDF](https://grenadaparliament.gd/wp-content/uploads/2021/08/Act-No.-12-of-2015-Income-Tax-Amendment.pdf), read 2026-10-27).
- PAYE certificates received (Fourth Schedule para 5) and whether the employer actually remitted.
- For business income: whether monthly instalments were paid — unpaid instalments accelerate the whole balance (s.93(3)).

## 9. Sources

- [Income Tax Act Cap. 149 consolidated PDF — ss. 2, 36–42, 56, 65, 93–97, 111–114, 123, Fourth & Fifth Schedules](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf) — read 2026-10-27
- [Cap. 149 chapter page, laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act) — read 2026-10-27
- [IRD G-TAX FAQ (registration thresholds, G-TAX scope)](https://www.ird.gd/gtax/index.html) — read 2026-10-27
- [IRD filing-deadline extension press release, 31 March 2026 (PDF)](https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf) — read 2026-10-27
- [Income Tax (Amendment) Act No. 12 of 2015 (NIS benefits exemption) (PDF)](https://grenadaparliament.gd/wp-content/uploads/2021/08/Act-No.-12-of-2015-Income-Tax-Amendment.pdf) — read 2026-10-27
- [Grenada Gazette portal (2025 publications index)](https://www.gazettes.gov.gd/index.php/publications/2025?layout=default) — read 2026-10-27

<!-- openaccountants-cta-block -->

**Talk to a verified accountant** — this skill is a source-cited draft (tier 2). For Grenada individual filings under professional review, book time with an OpenAccountants verified accountant: [Calendly](https://www.openaccountants.com).
