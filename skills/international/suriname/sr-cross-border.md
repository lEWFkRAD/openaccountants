---
name: sr-cross-border
description: >
  Suriname cross-border tax reference for 2026. Covers residence and
  source rules for individuals and companies, the 25% dividend
  withholding tax under the Dividendbelasting with the intercompany
  exemption, the narrow treaty network (Netherlands 7.5% dividend rate,
  Curaçao 5%/10%), non-resident taxation of Suriname-source profit, and
  the absence of a confirmed exit-tax regime. Trigger on Suriname
  cross-border, non-resident, treaty, dividend withholding, expat,
  moving to Suriname. Source-cited draft.
jurisdiction: SR
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Suriname cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026. **Source status
caveat:** only gov.sr and the Ministry of Finance and Planning pages
resolved this pass; the tax administration and statute portals
(belastingkantoor.sr, surinamewetten.sr) did not resolve, so treaty
article numbers, the residence-test wording, and any exit-tax position
are **needs-sources**. Figures are carried from the existing
source-cited drafts (sr-income-tax, sr-corporate-income-tax) with their
citations; nothing is invented. Currency: Surinamese dollar (SRD).

## 2. Who the rules apply to

- **Individuals.** A person domiciled in Suriname is resident and
  taxed on worldwide income; otherwise only Suriname-source income is
  taxed, through the same progressive schedule (8%–38% bands over the
  SRD 108,000 tax-free amount — approx — confirm non-resident threshold
  treatment). See sr-income-tax.
- **Companies.** Resident NV/BV companies are taxed at 36% on
  worldwide profit; non-resident companies only on Suriname-source
  profit (including through a permanent establishment). See
  sr-corporate-income-tax.
- **Outbound.** Suriname individuals working abroad remain taxable on
  worldwide income while domiciled; there is no confirmed expatriate
  suspension or exit-charge regime — **needs-sources.**

## 3. Rates and reliefs table

| Item | Content | Source |
|---|---|---|
| Corporate rate, residents | 36% on worldwide net profit | Income Tax Act 1922 — sr-corporate-income-tax |
| Non-resident companies | Suriname-source profit only | Income Tax Act 1922 — sr-corporate-income-tax |
| Dividend WHT, domestic | 25% on distributions by resident companies | Dividendbelasting — sr-corporate-income-tax |
| Intercompany dividend exemption | Resident-to-qualifying-resident dividends exempt from dividend WHT | Dividendbelasting — sr-corporate-income-tax |
| Dividend WHT — Netherlands treaty | 7.5% reduced rate | Suriname–Netherlands DTT |
| Dividend WHT — Curaçao treaty | 5% (≥10% holding); 10% otherwise | Suriname–Curaçao DTT |
| Interest / royalty WHT | No general domestic withholding confirmed (approx — confirm) | Income Tax Act 1922 — sr-corporate-income-tax |
| Personal bands | 8/18/28/38% over SRD 42,000/84,000/126,000 steps above SRD 108,000 tax-free | Income Tax Act 1922 / Loonbelasting — sr-income-tax |
| Exit tax | No confirmed departure charge | needs-sources |

## 4. Tax base and computation

Source is the operative concept for non-residents: services performed
in Suriname, Suriname immovable property, and Suriname business
activity (including a PE) create a Suriname base. Dividends from a
resident company carry the separate 25% Dividendbelasting charge on the
gross distribution, before any income-tax computation on the recipient
side.

## 5. Deadlines

- **Individual return:** 30 June following the tax year (approx —
  confirm) — sr-income-tax.
- **Wage tax remittance:** by the seventh working day of the following
  month — sr-payroll-social.
- **Corporate return:** on the administration's post-year-end schedule
  (approx — confirm) — sr-corporate-income-tax.

## 6. Penalties and interest

Ordinary income-tax / Dividendbelasting penalty-and-interest regime on
late or understated filings; statute-level amounts **needs-sources**
(portals unresolved this pass).

## 7. Treaty network

Confirmed instruments in the existing drafts: the Suriname–Netherlands
double-taxation treaty and the Suriname–Curaçao arrangement (dividend
rates above). No wider network confirmed — **needs-sources** for a full
list, MAP articles, and saving-clause wording. Withholding relief
requires the recipient to be the beneficial owner resident in the
treaty state; documentation practice is set by the tax administration
(**needs-sources**).

## 8. Worked examples

**Example 1 — Dutch parent receives a dividend.** A Suriname NV
distributes SRD 2,000,000 to its 40%-holding Dutch parent. Treaty rate
7.5% instead of the domestic 25%: Suriname dividend WHT = SRD 150,000
(a SRD 350,000 saving versus the domestic rate).

```oa-check
name: NL treaty dividend SRD 2m
inputs:
  dividend: 2000000
  domestic: 25
  treaty: 7.5
steps:
  - domestic_wht: dividend * pct(1, domestic)
  - treaty_wht: dividend * pct(1, treaty)
  - saving: domestic_wht - treaty_wht
expected:
  treaty_wht: 150000.00
  saving: 350000.00
```

**Example 2 — non-resident sells Suriname property.** A non-resident
individual sells Suriname immovable property for SRD 900,000 with an
adjusted basis of SRD 400,000. The SRD 500,000 gain is Suriname-source
and enters the progressive schedule; at the 38% top band the tax is
SRD 190,000 (band-by-band computation per sr-income-tax; top-band
illustration — confirm source treatment of gains, needs-sources).

```oa-check
name: non-resident property gain
inputs:
  proceeds: 900000
  basis: 400000
  top_rate: 38
steps:
  - gain: proceeds - basis
  - tax_illustrative: gain * pct(1, top_rate)
expected:
  gain: 500000.00
  tax_illustrative: 190000.00
```

## 9. Ask the client first

1. Where is the person actually domiciled — the Suriname residence
   test keys on domicile, not days (approx — confirm)?
2. Is the dividend recipient in the Netherlands or Curaçao (the only
   confirmed treaty routes), or elsewhere at 25%?
3. Does the foreign company have a Suriname PE through staff, site, or
   agency?
4. Are inbound interest/royalty payments really WHT-free under current
   practice — has the administration confirmed the no-general-WHT
   position?

## 10. Sources

- [Republiek van Suriname — portaal](https://gov.sr/) — read 2026-10-24.
- [Ministerie van Financiën en Planning](https://gov.sr/ministeries/ministerie-van-financien-en-planning/) — read 2026-10-24.
- Existing pack skills `sr-income-tax`, `sr-corporate-income-tax`, `sr-payroll-social` — figures carried forward with their citations (Income Tax Act 1922, Loonbelasting, Dividendbelasting, Suriname–Netherlands and Suriname–Curaçao treaties).
- Tax administration / statute portals (belastingkantoor.sr, surinamewetten.sr) — DNS unresolved 2026-10-24; **needs-sources**.

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
