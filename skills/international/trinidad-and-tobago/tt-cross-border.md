---
name: tt-cross-border
description: >
  Trinidad and Tobago cross-border tax reference for 2026. Covers the
  183-day residence test, non-resident taxation of TT-source income,
  withholding rates on dividends, interest and royalties to
  non-residents, the fifteen-treaty network listed by the IRD (USA, UK,
  CARICOM, China and others with years), CARICOM 0% intra-group
  dividends, and the IRD Mutual Agreement Procedure guidelines.
  Trigger on Trinidad and Tobago cross-border, non-resident, treaty,
  double taxation, expat, withholding. Source-cited draft.
jurisdiction: TT
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Trinidad and Tobago cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the IRD home,
double-taxation-treaties, legislation, withholding-tax and MAP-
guidelines pages; the Ministry of Finance income-tax services page; and
the existing TT pack skills (figures carried forward with their
citations). Currency: Trinidad and Tobago dollar (TTD).

**Source status caveat:** consolidated Act texts (laws.gov.tt Digital
Legislative Library) were not machine-readable this pass — residence-
test wording, treaty article numbers and exit positions are
**needs-sources**. The treaty list below is copied from the IRD's own
treaties page (read 2026-10-24).

## 2. Who the rules apply to

- **Individuals.** Resident if present in TT for at least 183 days in
  the year of income, or otherwise ordinarily resident (approx —
  confirm). Residents are taxed on the worldwide basis; non-residents
  on TT-source income only, through the same 25%/30% two-tier schedule
  (30% above TTD 1,000,000), with the personal allowance (TTD 90,000)
  generally unavailable to non-residents except on TT-source pension
  income. Passive income may instead suffer final withholding. See
  tt-income-tax.
- **Companies.** Resident companies are assessed on chargeable profits
  wherever arising; non-resident companies on TT-source profits
  (including through a branch/PE). See tt-corporate-income-tax.
- **Departure.** No confirmed exit-charge regime for individuals or
  companies — **needs-sources**.

## 3. Rates and reliefs table

| Item | Content | Source |
|---|---|---|
| Individual rates | 25% to TTD 1,000,000; 30% above | Income Tax Act (Chap. 75:01) — tt-income-tax |
| Personal allowance | TTD 90,000; generally not for non-residents (pension exception) | Income Tax Act — tt-income-tax |
| Dividend WHT to non-residents | 10% non-treaty; 0% within CARICOM; reduced/0% under other treaties | Income Tax Act — tt-corporate-income-tax |
| Interest WHT to non-residents | 10% individuals / 8% companies non-treaty (approx — confirm) | Income Tax Act — tt-corporate-income-tax |
| Royalty WHT to non-residents | 15% non-treaty; reduced under treaties | Income Tax Act — tt-corporate-income-tax |
| Payments to residents | 0% WHT on dividends, interest, royalties between residents | Income Tax Act — tt-corporate-income-tax |
| Corporation tax | 30% standard; 35% banks/petrochemicals; 50%/30% petroleum | Corporation Tax Act / Petroleum Taxes Act — tt-corporate-income-tax |
| Exit tax | No confirmed departure charge | needs-sources |

## 4. Treaty network (IRD list, read 2026-10-24)

The IRD's Double Taxation Treaties page lists fifteen instruments with
effective years: Brazil 2008, Canada 1996, CARICOM 1994, China 2004,
France 1987, Germany 1976, India 1999, Italy 1971, Luxembourg 2001,
Spain 2009, Sweden 1984, Switzerland 1973, United Kingdom 1983, United
States 1971, Venezuela 1997. Treaty relief requires beneficial-owner
residence in the treaty state; article-level rates are **needs-
sources** (confirm each instrument). The IRD publishes MAP guidelines
for treaty disputes.

## 5. Tax base and computation

Source rules drive the non-resident charge: TT employment exercised
here, TT immovable property, TT business activity (branch/PE), and TT-
source passive income. Withholding on passive income is often final for
non-residents; employment and business income are assessed on the same
schedule as residents.

## 6. Deadlines

- **Individual return:** 30 April following the year of income;
  self-employed quarterly instalments 31 March / 30 June / 30
  September / 31 December (see tt-income-tax).
- **PAYE, WHT and Health Surcharge remittance:** by the 15th of the
  following month (see tt-payroll-social).
- **Corporation tax return:** 30 April (see tt-corporate-income-tax).

## 7. Penalties and interest

Late or incorrect returns attract the Income Tax Act penalty-and-
interest regime (section-level amounts **needs-sources**); objections
follow the IRD's published objection route, treaty disputes the MAP
guidelines.

## 8. Worked examples

**Example 1 — US parent receives a dividend.** A TT company
distributes TTD 3,000,000 to its US parent. Non-treaty dividend WHT is
10% = TTD 300,000; if the treaty rate applies at 5% (confirm article —
needs-sources), WHT is TTD 150,000, a TTD 150,000 saving.

```oa-check
name: dividend TTD 3m non-treaty vs 5 percent
inputs:
  dividend: 3000000
  non_treaty: 10
  treaty: 5
steps:
  - non_treaty_wht: dividend * pct(1, non_treaty)
  - treaty_wht: dividend * pct(1, treaty)
  - saving: non_treaty_wht - treaty_wht
expected:
  non_treaty_wht: 300000.00
  treaty_wht: 150000.00
  saving: 150000.00
```

**Example 2 — non-resident employee, 200 days in TT.** A UK consultant
spends 200 days in TT on a single project (resident by the 183-day
test), earning TTD 480,000 TT-source. Chargeable income after the
TTD 90,000 personal allowance (residents get it) is TTD 390,000; at the
25% first-tier rate the illustrative tax is TTD 97,500 (no higher-tier
30% applies below TTD 1,000,000).

```oa-check
name: 200-day consultant TTD 480k
inputs:
  income: 480000
  allowance: 90000
  tier1: 25
steps:
  - chargeable: income - allowance
  - tax: chargeable * pct(1, tier1)
expected:
  chargeable: 390000.00
  tax: 97500.00
```

## 9. Ask the client first

1. How many days in TT in the year of income — 183 or more triggers
   residence (approx — confirm the test's wording)?
2. Is the payee the beneficial owner in a treaty state on the IRD
   list, and can it produce residence documentation?
3. Is the counterparty CARICOM-resident (0% dividend WHT route)?
4. Does a foreign company's TT activity create a branch/PE exposure —
   staff, site, agency, or dependent contractor?

## 10. Sources

- [IRD — Double Taxation Treaties](https://www.ird.gov.tt/law-policy/double-taxation-treaties) — read 2026-10-24 (fifteen treaties listed with years).
- [IRD — Guidelines for Mutual Agreement Procedure](https://www.ird.gov.tt/law-policy/map-guidelines) — read 2026-10-24.
- [IRD — Withholding Tax](https://www.ird.gov.tt/withholding-tax) — read 2026-10-24.
- [IRD — Legislation and Tax Laws](https://www.ird.gov.tt/law-policy/legislation) — read 2026-10-24.
- [Ministry of Finance — Income Tax services](https://www.finance.gov.tt/services/income-tax/) — read 2026-10-24.
- [Digital Legislative Library](https://laws.gov.tt/) — read 2026-10-24 (Acts not machine-readable this pass; section citations needs-sources).
- Existing pack skills `tt-income-tax`, `tt-corporate-income-tax`, `tt-payroll-social` — figures carried forward with their PwC citations pending statute-level confirmation.

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
