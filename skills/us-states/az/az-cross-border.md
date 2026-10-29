---
name: az-cross-border
description: >
  Use this skill whenever asked about Arizona cross-border tax for tax
  year 2026 — part-year and nonresident filing (Form 140NR), Arizona
  source income for nonresidents, nonresident estate and trust
  residency under §43-1301, the estate tax-clearance certificate
  (§§43-1361/43-1362), corporate tax clearance on dissolution
  (§43-1151), moving into or out of Arizona, and the pass-through
  entity (PTE) elective withholding context. Trigger on "Arizona
  nonresident", "Form 140NR", "Arizona part-year", "moving to Arizona
  taxes", "Arizona source income", "Arizona tax clearance", "Arizona
  trust residency". Source-cited draft; statute texts read 2026-10-28.
jurisdiction: US-AZ
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - az-income-tax
---

# Arizona cross-border (nonresidents, residency change, clearance) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft; statute texts read 28 October 2026 (azleg.gov texts of A.R.S. §§43-1131, 43-1133, 43-1134, 43-1144, 43-1146, 43-1151, 43-1301, 43-1361, 43-1362, plus AZDOR pages). Items not tied to a primary source this run are on the Not yet confirmed line in Sources.

- **Individuals:** part-year residents and nonresidents with Arizona-source income file Form 140NR (form name carried from ADOR practice; see the Not yet confirmed line for the instructions). Residents file Form 140 (see `az-income-tax`). Arizona taxes a nonresident's Arizona-source income at the same flat 2.5% rate (AZDOR Individual Income Tax Highlights, read 2026-10-28: "2025 New Tax Rate of 2.5% for All Income Levels and Filing Status").
- **Estates and trusts:** a **resident estate** is the estate of a decedent who was an Arizona resident at death; a **resident trust** has at least one individual fiduciary resident in Arizona, and an interstate corporate fiduciary alone (or with nonresidents) makes the trust resident **only if it conducts the administration of the trust in Arizona** (§43-1301(5), read 2026-10-28). A nonresident estate/trust's Arizona gross income is its **Arizona-source taxable income computed per the IRC** (§43-1301(1)(a), read).
- **Corporations:** a foreign corporation not itself subject to Arizona tax keeps its income and expenses out of Arizona apportionment (§43-1132(A)-(B), read); "taxable in another state" is defined by actual or potential net-income/franchise taxation (§43-1133, read).
- **Fiduciaries of estates over twenty thousand dollars with a nonresident beneficiary:** the probate final account is not allowed unless the fiduciary obtains an ADOR tax-clearance certificate — §43-1361 (read 2026-10-28): "If the value of the assets of an estate at the death of the decedent exceeds twenty thousand dollars and if any beneficiary is a nonresident, the final account of the fiduciary shall not be allowed by the probate court unless the fiduciary obtains from the department" the certificate. ADOR responds within thirty days of a request (§43-1362, read: "Within thirty days after receiving a request for a certificate, the department shall either issue the certificate or notify the person requesting the certificate of the amount of tax that shall" be paid).
- **Corporations ceasing activity:** dissolution, surrender, or term reduction requires an ADOR clearance certificate before the court/corporation commission acts (§43-1151, read).

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Individual rate (resident and nonresident alike) | flat 2.5% | AZDOR Individual Income Tax Highlights (read 2026-10-28): "2025 New Tax Rate of 2.5% for All Income Levels and Filing Status" |
| Nonbusiness income sourcing | rents/royalties from real/tangible property, capital gains, interest, dividends allocated under §§43-1135–43-1138 (property situs / commercial domicile) | §43-1134 (read 2026-10-28); sub-sections on the Not yet confirmed line |
| Employment income situs | compensation is Arizona-paid if service is entirely in AZ, out-of-state service is incidental, or the base of operations / direction-and-control / residence tie-breaker lands in AZ | §43-1144 (read 2026-10-28) |
| Tangible-goods sales situs | delivered/shipped to purchaser in Arizona regardless of F.O.B. | §43-1146 (read 2026-10-28) |
| Trust residency | administration-in-Arizona test for interstate corporate fiduciaries | §43-1301(5) (read 2026-10-28) |
| Estate clearance threshold | estates whose assets exceed twenty thousand dollars at death, with a nonresident beneficiary | §43-1361 (read 2026-10-28) |
| Clearance response time | within thirty days of a request | §43-1362 (read 2026-10-28) |

Arizona has no "convenience of the employer" rule on the statute pages read this run — remote work by a nonresident is taxed only where §43-1144's service/base-of-operations tests land it (see the Not yet confirmed line for the Form 140NR instructions check).

## The taxable base

For nonresidents and part-year residents, the base is Arizona-source income: compensation under §43-1144's situs tests, business income apportioned to Arizona, and nonbusiness income allocated under §§43-1134–43-1138. For trusts and estates, residency (and therefore the base) turns on the §43-1301 definitions. Foreign corporations keep non-Arizona income and related expenses out of the apportionment base (§43-1132(A)-(B), read).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Form 140NR (part-year/nonresident) | follows the individual filing deadline (April 15) | carried from `az-income-tax`; instructions on the Not yet confirmed line |
| Estate clearance certificate request | before the probate final account is allowed | §43-1361 (read 2026-10-28) |
| ADOR response on clearance requests | within thirty days | §43-1362 / §43-1151(B) (read 2026-10-28) |
| Corporate clearance | before dissolution/surrender decree is filed | §43-1151(A) (read 2026-10-28) |

## Penalties and interest

Clearance certificates do not discharge later-found liabilities — issuance "shall not relieve the corporation or any individual from liability" (§43-1151(C), read); the estate-certificate rule works the same way in substance. Interest runs at the §6621-tracked rate, compounded annually (AZDOR interest page, read 2026-10-28). Common failure modes: (1) a nonresident owner of an Arizona LLC assuming K-1 income is not Arizona-source — business income apportioned to Arizona is; (2) moving mid-year and filing only one full-year return — part-year status needs Form 140NR in both states per each state's rules; (3) a trust with an Arizona-resident co-fiduciary silently becoming an Arizona resident trust (§43-1301(5)).

## Cross-border points

- Compensation situs: service performed entirely in Arizona, incidental out-of-state service, or the base-of-operations / direction-and-control / residence tie-breakers make compensation Arizona-source (§43-1144, read).
- Tangible-goods sales are sited at delivery/shipment to the Arizona purchaser regardless of F.O.B. terms (§43-1146, read).
- A foreign corporation not itself Arizona-taxable cannot contribute losses or expenses to the Arizona base (§43-1132(A)-(B), read), unless it joins an Arizona affiliated group (§43-1132(D), read, with §43-947).
- Pass-through-entity elective tax and withholding mechanics: see the AZDOR Corporate Income Tax page; the PTE election details are on the Not yet confirmed line.

## Worked examples

A nonresident works 40% of the year from an Arizona home office (hypothetical facts; service performed in Arizona under §43-1144); wages $150,000 (hypothetical), Arizona-source share 40%, flat 2.5%:

```oa-check
name: nonresident wages 40 percent of 150000 at 2.5 percent
inputs:
  wages: 150000
  share: 0.4
  rate: 0.025
steps:
  - az_income: wages * share
  - tax: az_income * rate
expected:
  az_income: 60000.00
  tax: 1500.00
```

An Arizona-taxable C corporation dissolves with $12,000 of unpaid tax (hypothetical); clearance requires payment or bond before the decree (§43-1151):

```oa-check
name: clearance bond equals unpaid tax
inputs:
  tax_due: 12000
  bond: 1.0
steps:
  - secure: tax_due * bond
expected:
  secure: 12000.00
```

## Ask the client first

- Where is the client domiciled, and did they move during the tax year? Count Arizona days and locate the base of operations (§43-1144).
- Is there Arizona-source business income (sales delivered into Arizona, employees working from Arizona, Arizona real property rents)?
- For trusts: who are the fiduciaries, and where is trust administration actually conducted (§43-1301(5))?
- Closing an Arizona corporation? Order the §43-1151 clearance certificate early — the thirty-day ADOR clock blocks the decree.
- Settling an estate with a nonresident beneficiary? Check the §43-1361 certificate before the probate final account is allowed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| A.R.S. §43-1301 — Estates/trusts definitions, residency tests | https://www.azleg.gov/ars/43/01301.htm | 2026-10-28 |
| A.R.S. §43-1361 — Certificate of payment of taxes (estate) | https://www.azleg.gov/ars/43/01361.htm | 2026-10-28 |
| A.R.S. §43-1362 — Request for certificate | https://www.azleg.gov/ars/43/01362.htm | 2026-10-28 |
| A.R.S. §43-1151 — Corporate tax clearance | https://www.azleg.gov/ars/43/01151.htm | 2026-10-28 |
| A.R.S. §43-1132 — Foreign-corporation bar | https://www.azleg.gov/ars/43/01132.htm | 2026-10-28 |
| A.R.S. §43-1133 — Taxability in another state | https://www.azleg.gov/ars/43/01133.htm | 2026-10-28 |
| A.R.S. §43-1134 — Allocation of nonbusiness income | https://www.azleg.gov/ars/43/01134.htm | 2026-10-28 |
| A.R.S. §43-1144 — Compensation situs | https://www.azleg.gov/ars/43/01144.htm | 2026-10-28 |
| A.R.S. §43-1146 — Sales situs | https://www.azleg.gov/ars/43/01146.htm | 2026-10-28 |
| AZDOR — Individual Income Tax Highlights | https://azdor.gov/forms/individual-income-tax-highlights | 2026-10-28 |
| AZDOR — Corporate Income Tax (PTE-E FAQs link) | https://azdor.gov/business/corporate-income-tax | 2026-10-28 |
| AZDOR — Interest Rates | https://azdor.gov/business/interest-rates | 2026-10-28 |

Not yet confirmed: the Form 140NR instructions PDF and the ADOR part-year/nonresident guidance page (form number carried from ADOR practice); the statutory residency day-count definition for individuals; the current PTE election mechanics (PTE-E FAQs); the sub-sections of §§43-1135–43-1138; the 2026 confirmation of the 2.5% rate for nonresidents beyond the 2025 highlights page.

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
