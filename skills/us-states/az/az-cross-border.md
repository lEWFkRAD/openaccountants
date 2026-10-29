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
  trust residency". Source-cited draft; statute texts read 2026-10-27.
jurisdiction: US-AZ
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - az-income-tax
---

# Arizona cross-border (nonresidents, residency change, clearance) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: azleg.gov texts of A.R.S. §§43-1131, 43-1133, 43-1134, 43-1144, 43-1146, 43-1151, 43-1301, 43-1361, 43-1362 fetched HTTP 200 with real content, plus the AZDOR Corporate Income Tax page. **needs-sources:** the Form 140NR instructions PDF and the ADOR part-year/nonresident guidance page (azdor.gov paths 404'd or timed out this run), the statutory residency day-count definition for individuals, and the current PTE election mechanics (the PTE-E FAQs PDF is linked from the ADOR corporate page but was not fetched).

## 2. Who applies

- **Individuals:** part-year residents and nonresidents with Arizona-source income file Form 140NR (form name carried from ADOR practice; instructions: needs-sources). Residents file Form 140 (see `az-income-tax`). Arizona taxes a nonresident's Arizona-source income at the same flat 2.5% rate.
- **Estates and trusts:** a **resident estate** is the estate of a decedent who was an Arizona resident at death; a **resident trust** has at least one individual fiduciary resident in Arizona, and an interstate corporate fiduciary alone (or with nonresidents) makes the trust resident **only if it conducts the administration of the trust in Arizona** (§43-1301(5), text read 2026-10-27). A nonresident estate/trust's Arizona gross income is its **Arizona-source taxable income computed per the IRC** (§43-1301(1)(a), read).
- **Corporations:** a foreign corporation not itself subject to Arizona tax keeps its income and expenses out of Arizona apportionment (§43-1132(A)-(B), read); "taxable in another state" is defined by actual or potential net-income/franchise taxation (§43-1133, read).
- **Fiduciaries of estates over $20,000 with a nonresident beneficiary:** probate final account requires an ADOR tax-clearance certificate (§43-1361), issued or contested within 30 days of request (§43-1362) (both read 2026-10-27).
- **Corporations ceasing activity:** dissolution, surrender, or term reduction requires an ADOR clearance certificate before the court/corporation commission acts (§43-1151, read).

## 3. Rates and sourcing rules

| Item | Rule | Source |
|---|---|---|
| Individual rate (resident and nonresident alike) | flat 2.5% | carried from `az-income-tax` (2025 flat rate; 2026 confirmation: needs-sources) |
| Nonbusiness income sourcing | rents/royalties from real/tangible property, capital gains, interest, dividends allocated under §§43-1135–43-1138 (property situs / commercial domicile) | §43-1134 (read 2026-10-27); sub-sections needs-sources |
| Employment income situs | compensation is Arizona-paid if service is entirely in AZ, out-of-state service is incidental, or the base of operations / direction-and-control / residence tie-breaker lands in AZ | §43-1144 (read 2026-10-27) |
| Tangible-goods sales situs | delivered/shipped to purchaser in Arizona regardless of F.O.B. | §43-1146 (read 2026-10-27) |
| Trust residency | administration-in-Arizona test for interstate corporate fiduciaries | §43-1301(5) (read 2026-10-27) |

Arizona has no "convenience of the employer" rule on the statute pages read this run — remote work by a nonresident is taxed only where §43-1144's service/base-of-operations tests land it (**confirm against Form 140NR instructions: needs-sources**).

## 4. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| Form 140NR (part-year/nonresident) | follows the individual filing deadline (April 15) | carried from `az-income-tax`; instructions needs-sources |
| Estate clearance certificate request | before the probate final account is allowed | §43-1361 (read 2026-10-27) |
| ADOR response on clearance requests | within 30 days | §43-1362/§43-1151(B) (read 2026-10-27) |
| Corporate clearance | before dissolution/surrender decree is filed | §43-1151(A) (read 2026-10-27) |

## 5. Penalties and interest

Clearance certificates do not discharge later-found liabilities — issuance "shall not relieve the corporation or any individual from liability" (§43-1151(C), read); the estate-certificate rule works the same way in substance. Interest runs at the §6621-tracked rate, compounded annually (AZDOR interest page, read 2026-10-27). Common failure modes: (1) a nonresident owner of an Arizona LLC assuming K-1 income is not Arizona-source — business income apportioned to Arizona is; (2) moving mid-year and filing only one full-year return — part-year status needs Form 140NR in both states per each state's rules; (3) a trust with an Arizona-resident co-fiduciary silently becoming an Arizona resident trust (§43-1301(5)).

## 6. Worked examples

A nonresident works 40% of the year from an Arizona home office (service performed in Arizona under §43-1144); wages $150,000, Arizona-source share 40%, flat 2.5%:

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

An Arizona-taxable C corporation dissolves with $12,000 of unpaid tax; clearance requires payment or bond before the decree (§43-1151):

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

## 7. Ask the client

- Where is the client domiciled, and did they move during the tax year? Count Arizona days and locate the base of operations (§43-1144).
- Is there Arizona-source business income (sales delivered into Arizona, employees working from Arizona, Arizona real property rents)?
- For trusts: who are the fiduciaries, and where is trust administration actually conducted (§43-1301(5))?
- Closing an Arizona corporation? Order the §43-1151 clearance certificate early — the 30-day ADOR clock blocks the decree.

## Sources

1. A.R.S. §43-1301 Estates/trusts definitions, residency tests: https://www.azleg.gov/ars/43/01301.htm (200, 2026-10-27)
2. A.R.S. §43-1361/§43-1362 Estate clearance certificate: https://www.azleg.gov/ars/43/01361.htm, /01362.htm (200, 2026-10-27)
3. A.R.S. §43-1151 Corporate tax clearance: https://www.azleg.gov/ars/43/01151.htm (200, 2026-10-27)
4. A.R.S. §43-1132 Foreign-corporation bar; §43-1133 taxability in another state: https://www.azleg.gov/ars/43/01132.htm, /01133.htm (200, 2026-10-27)
5. A.R.S. §43-1134 allocation of nonbusiness income; §43-1144 compensation situs; §43-1146 sales situs: https://www.azleg.gov/ars/43/01134.htm etc. (200, 2026-10-27)
6. AZDOR — Corporate Income Tax (PTE-E FAQs link): https://azdor.gov/business/corporate-income-tax (200 with text, 2026-10-27)
7. AZDOR — Interest Rates: https://azdor.gov/business/interest-rates (200 with text, 2026-10-27)
