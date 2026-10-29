---
name: la-cross-border
description: >
  Use this skill whenever asked about Louisiana cross-border taxation for
  tax year 2026 — nonresident and part-year filing (Form IT-540B), the
  resident-worldwide-plus-credit structure, no reciprocity with
  neighboring states, no exit tax, and the verified LDR rule that
  Louisiana residents working in another state are LA-withheld when that
  state does not withhold. Trigger on "Louisiana nonresident", "IT-540B",
  "Louisiana part-year", "moving to Louisiana", "Louisiana reciprocity",
  "Louisiana credit for taxes paid". Source-cited draft; LDR withholding
  residence rule verified 2026-10-28; credit statute and IT-540B detail
  not confirmed.
jurisdiction: US-LA
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - la-income-tax
---

# Louisiana cross-border taxation v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 2026-10-28. Covers Louisiana exposure for nonresidents, part-year residents, and Louisianans working out of state. **Source status:** the LDR Withholding page (residence-based withholding rule) and the LDR Individual Income Tax page (nonresident sourcing, gambling-winnings rule, Schedule C credit, military part-year rule for taxable years beginning before January 1, 2023) verified 2026-10-28; **the credit statute (R.S. 47:287.182 expected) and IT-540B mechanics sit behind the session-state legislature site**, so citations and credit ordering are **not confirmed**.

## Rates, bands and thresholds

- **Louisiana residents**: taxed on worldwide income at the flat 3% (per `la-income-tax.md`, effective 2025); the LDR Withholding page confirms LA residents working in another state may be LA-withheld when the other state doesn't withhold (verified).
- **Nonresidents**: taxed on Louisiana-source income only — the LDR Individual Income Tax page (verified 2026-10-28) states that nonresidents add to federal AGI only LA-sourced income, and that gambling winnings earned in Louisiana are LA-sourced income; file **IT-540B** (per pre-existing skill's scope note; form ID not confirmed for 2026).
- **Part-year residents**: split-year treatment; allocation detail **not confirmed**.
- **Entities**: foreign corporations doing business in Louisiana file CIFT-620 (verified category — see `la-corporate-income-tax`).

## The taxable base

| Item | Rule | Source status |
|---|---|---|
| Resident base | worldwide income at flat 3% (2025+ reform) | structure verified via withholding rule; rate per pre-existing skill + RIB 25-012 PDF (verified PDF) |
| Nonresident base | Louisiana-source income, IT-540B | **not confirmed** |
| Credit for taxes paid to other states | Residents are "allowed a credit on Schedule C for the net tax liability paid to another state if that income is included on the Louisiana return" (LDR page, verified 2026-10-28) | rule verified; **statute citation/ordering not confirmed** |
| Reciprocity | **none** — no agreements with TX, MS, AR, OK, or any neighbor | structural; not confirmed for citation |
| Exit tax | **none** — no departure/exit tax | structural, low risk |
| Remote work sourcing | services sourced where performed; LA residents still LA-taxed (verified withholding rule) | verified |

## Deadlines and filing

- IT-540/IT-540B: **May 15** for calendar-year filers (Louisiana's individual deadline — verified against the LDR Individual Income Tax page 2026-10-28); R.S. 47:103 gives an automatic six-month extension to file, never to pay.
- Withholding remittances follow the payroll calendar (see `la-payroll`).

## 5. Penalties and interest

- Standard R.S. 47 late-filing/late-payment regime — tiers **not confirmed**.
- Dual-residency disputes (e.g. LA vs TX domicile fights) are litigation-prone; no special penalty for the dispute itself.

## Cross-border points

- **LA resident working in Texas** (classic pattern): Texas has no income tax and doesn't withhold → the LDR rule (verified) means the Texas employer may need to withhold Louisiana tax; Louisiana taxes worldwide with credit for tax paid elsewhere — here zero credit, full LA tax.
- **Nonresident working in Louisiana**: LA withholds and taxes; home state generally credits LA tax.
- **Military**: for taxable years beginning before January 1, 2023, LA-domiciled (home-of-record) military personnel filed as part-year residents (LDR page, verified 2026-10-28); MMRA resident-retention adoption detail **not confirmed**.
- Louisiana's **May 15** individual deadline is later than most states' April 15 — coordinate multi-state extensions.

## 7. Worked examples

**Example 1 — Louisiana resident working in Texas (no TX tax):** hypothetical client facts: Louisiana tax on worldwide income $5,100; Texas tax $0; no credit available (Texas levies no income tax).

```oa-check
name: LA resident TX commuter (no credit)
inputs:
  la_tax: 5100
  tx_tax: 0
steps:
  - credit: min(tx_tax, la_tax)
  - la_net: la_tax - credit
  - combined: tx_tax + la_net
expected:
  credit: 0
  la_net: 5100
  combined: 5100
```

The household pays full Louisiana tax — the no-reciprocity/no-TX-tax pattern is why the verified LA-withholding rule for out-of-state work exists.

**Example 2 — nonresident working in Louisiana:** hypothetical client facts: Mississippi resident earns in Louisiana; LA tax $1,800; Mississippi tax on the same income $2,600 with credit for LA tax.

```oa-check
name: Nonresident LA work home-state credit
inputs:
  la_tax: 1800
  home_tax: 2600
steps:
  - credit: min(la_tax, home_tax)
  - home_net: home_tax - credit
  - combined: la_tax + home_net
expected:
  credit: 1800
  home_net: 800
  combined: 2600
```

## Ask the client first

- Domicile and statutory-day counts in Louisiana vs other states (LA vs TX domicile disputes are common).
- Where services were physically performed each day.
- Employer withholding posture for LA residents working in no-income-tax states (verified duty).
- Home/work state credit rules — credits, not exemptions, do the double-tax relief.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| LDR Withholding (resident-out-of-state withholding rule, nonresident duty) | https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/ | 2026-10-28 |
| LDR Revenue Information Bulletin 25-012 (flat 3% reform; archived PDF) | https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf | 2026-10-28 |
| LDR Individual Income Tax (nonresident sourcing, gambling winnings, Schedule C credit, military part-year rule, extension) | https://revenue.louisiana.gov/individuals/general-resources/individual-income-tax/ | 2026-10-28 |

Not yet confirmed: IT-540B 2026 form ID and mechanics; the resident-credit statute citation and ordering (R.S. 47:287.182 numbering not verified — legis.la.gov serves only a JS shell to plain fetchers); part-year allocation detail; current-year military provisions; the citation for the absence of reciprocity.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Louisiana cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
