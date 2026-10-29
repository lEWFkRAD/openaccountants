---
name: mi-cross-border-tax
description: >-
  Use when a nonresident works or invests in Michigan, a Michigan
  pass-through has nonresident members, or an out-of-state company has
  Michigan activity, and the 2026 Schedule NR, reciprocity, composite-return
  and P.L. 86-272 position is needed. Trigger on Michigan Schedule NR,
  MI-1040 nonresident, reciprocal state Michigan, composite return Michigan,
  P.L. 86-272 Michigan. Source-cited draft; statute section pages are
  JS-rendered and carry unverified caveats.
jurisdiction: US-MI
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---
## Who this applies to


- Nonresident and statutory/part-year individuals with Michigan-source income: MI-1040 with **Schedule NR** (Treasury resident/non-resident FAQ hub — <https://www.michigan.gov/taxes/iit/file-your-income-taxes/resident-and-non-resident-income-faqs>, 200 with content on 2026-10-25).
- Residents of **reciprocal states** (Indiana, Kentucky, Ohio, Wisconsin, plus Minnesota under the reciprocity agreement) working in Michigan: exempt from Michigan tax on wages with a reciprocity certificate (Treasury FAQ hub, read 2026-10-25).
- Michigan pass-throughs with nonresident members (composite-return route) and out-of-state corporations with Michigan activity (CIT nexus / P.L. 86-272).
- Out of scope: Detroit city income tax for nonresidents working in Detroit (`mi-detroit-individual-return`).

## Rates, bands and thresholds


- **IIT rate:** flat 4.25% (mi-income-tax, read 2026-10-25).
- **Reciprocity:** wages of residents of the reciprocal states are taxable only in the state of residence when the employee files Form 4880 (MI) / the home-state equivalent; without the certificate, Michigan withholds and the worker claims a refund (Treasury FAQ hub, read 2026-10-25).
- **Nonresidents** file MI-1040 + Schedule NR: Michigan-source income (wages for work performed in Michigan, Michigan rents, Michigan business income) is grossed up against total income to derive the Michigan tax ratio (Schedule NR instructions — **unverified**: the Treasury form page did not machine-verify on 2026-10-25; mechanics corroborated by the FAQ hub and `mi-income-tax`).
- **Composite returns:** Michigan permits composite filings for nonresident partners/members in defined cases (MCL 206.131 — <https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-131>, 200 on 2026-10-25 but the section text renders via JavaScript and was **not machine-verified** — unverified; confirm the current composite mechanics with Treasury before use).
- **P.L. 86-272:** solicitation-only activity for tangible personal property is exempt from the Michigan CIT (net-income tax); the analysis sits in the CIT lane (mi-corporate-income-tax, read 2026-10-25).

## The taxable base


- Wages: sourced to where work is physically performed; remote Michigan workdays create Michigan-source wages (FAQ hub, read 2026-10-25).
- Schedule NR ratio: Michigan-source income over total net income, applied to the full-state tax (unverified for the exact line mechanics).
- Hybrid work: no special 60-day-style sourcing rule of the Northeast type; day-by-day performance sourcing applies (unverified).

## Deadlines and filing


- MI-1040 + Schedule NR: 15 April for calendar-year individuals; 6-month extension with payment by 15 April (mi-income-tax / mi-estimated-tax, read 2026-10-25).
- Reciprocity certificates (Form 4880) are filed with the employer and renewed annually (Treasury FAQ hub, read 2026-10-25).

## Penalties and interest


- Late filing/payment penalties and interest under the IIT act (MCL 206.95 et seq. — **unverified**, JS-rendered; `mi-income-tax` corroborates the general framework).

## Cross-border points


- No state treaty power; US treaties can limit federal tax on some nonresident income but not Michigan wage sourcing.
- Military: servicemembers stationed in Michigan keep domicile elsewhere; Michigan taxes only Michigan-source non-stationed income (Servicemembers Civil Relief Act overlay — unverified).
- Michigan residents taxed by another state claim the Michigan credit for taxes paid to other jurisdictions (mi-income-tax, read 2026-10-25).

## Worked examples


**Example 1 — Ohio resident working in Michigan.** An Ohio resident earns USD 90,000 working in Michigan with no Form 4880 on file: Michigan withholds at 4.25%: 90,000 × 0.0425 = 3,825. With a valid reciprocity certificate: Michigan tax 0; Ohio taxes the wages. Refund claim recovers the 3,825.

```oa-check
name: mi reciprocity withholding refund
inputs:
  wages: 90000
  rate: 0.0425
steps:
  - withheld: wages * rate
  - mi_tax_with_cert: 0
  - refund: withheld - mi_tax_with_cert
expected:
  withheld: 3825.00
  refund: 3825.00
```

**Example 2 — nonresident Schedule NR ratio.** A nonresident's only income is a 30% share of a Michigan LLC's USD 200,000 profit: Michigan-source 200,000 × 0.30 = 60,000; total income 60,000 → ratio 1.00. Michigan tax: 60,000 × 0.0425 = 2,550 (unverified caveat on the exact Schedule NR line mechanics).

```oa-check
name: mi nonresident schedule nr ratio
inputs:
  profit: 200000
  share: 0.30
  rate: 0.0425
steps:
  - mi_income: profit * share
  - ratio: mi_income / mi_income
  - mi_tax: mi_income * rate * ratio
expected:
  mi_income: 60000.00
  ratio: 1.00
  mi_tax: 2550.00
```

## Ask the client first


- Home state (is it a reciprocity state?) and whether Form 4880 is on file with the employer.
- Workday log for hybrid work near the state line.
- Whether the pass-through has nonresident members and whether a composite filing was considered (mechanics unverified).

## Sources


| Source | URL | Read on |
| --- | --- | --- |
| Treasury resident/non-resident FAQ hub — 200 with content | https://www.michigan.gov/taxes/iit/file-your-income-taxes/resident-and-non-resident-income-faqs | 2026-10-25 |
| MCL 206.131 (composite) — 200; section text JS-rendered, **unverified** | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-131 | 2026-10-25 |
| `mi-income-tax`, `mi-estimated-tax`, `mi-detroit-individual-return` skills — internal corroboration | (internal skills) | 2026-10-25 |

Not yet confirmed: exact Schedule NR line mechanics; MCL 206.131 composite mechanics; MCL 206.95 et seq. penalty/interest text; SCRA overlay specifics; day-by-day sourcing rule details.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant


This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
