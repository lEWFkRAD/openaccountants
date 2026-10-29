---
name: ia-transfer-pricing
description: >
  Use this skill whenever asked about Iowa related-party pricing,
  consolidated returns, and income allocation for tax year 2026 — Iowa
  Code §422.36 fair-price and income-shifting adjustments, §422.37
  consolidated returns for IRC §1504(a) affiliated groups, §422.32
  business-income and commercial-domicile definitions, and the §422.17
  no-withholding certificate for nonresidents. Trigger on "Iowa transfer
  pricing", "Iowa consolidated return", "Iowa affiliated group", "422.36",
  "422.37", "Iowa fair price", "Iowa income shifting". Source-cited draft;
  Iowa Code 2026 text read from legis.iowa.gov 2026-10-27.
jurisdiction: US-IA
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - ia-corporate-income-tax
---

# Iowa transfer pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-27. Iowa has **no separate transfer-pricing statute**; the related-party toolkit is §422.36(2)-(3) (fair-price restatement and income-shifting), §422.37 (consolidated returns), and the §422.32 allocation definitions. Statute text read directly from Iowa Code 2026 PDFs at legis.iowa.gov 2026-10-27. **Source status:** §§422.36, 422.37, 422.32, 422.17 verified from statute text; Iowa's **apportionment formula** (property/payroll/sales factors, single-sales-factor status) is set in rules/department guidance not located this run — **needs-sources**.

## 2. Who applies

- Any corporation taxable under §422.33 that transacts with a **substantially-owned related party** or is part of a **commonly-controlled group** (§422.36(2)-(3), text read 2026-10-27).
- **Affiliated group** = group of corporations as defined in **IRC §1504(a)** (§422.32(1)(a), text read 2026-10-27). Any such group **may elect** — and **on the director's demand shall be required** — to file an Iowa consolidated return (§422.37, text read 2026-10-27).
- Consolidated-return conditions (§422.37, text read 2026-10-27): federal consolidated return for the same year; all members subject to §422.33 join (except as §29C.24 provides); §422.34-exempt members excluded; **statutory allocation/apportionment method mandatory for all members** unless the director grants an alternative; filing = consent to the director's rules.

## 3. Mechanics

- **Fair-price adjustment (§422.36(2), text read 2026-10-27):** where a corporation sells to, or buys from, a substantially-owned corporation **at less than the fair price**, the department may restate the seller's Iowa income to the fair price.
- **Income-shifting adjustment (§422.36(3), text read 2026-10-27):** where income of a commonly-controlled group is **"arbitrarily shifted... through price fixing, charges for services, or otherwise"**, the department may reallocate it to the earning member.
- **Business income (§422.32(1)(b), text read 2026-10-27):** unitary-flavored definition — income from transactions in the regular course of business, and property gains **operationally related** to Iowa business; the legislature intends **all constitutionally apportionable income** to be apportionable. Note the statute's carve-out: filing on a **combined-report basis is neither allowed nor required by that paragraph** — Iowa's group tool is the §422.37 consolidated return, not water's-edge combined reporting.
- **Commercial domicile (§422.32(1)(c), text read 2026-10-27):** principal place of direction/management — the non-business-income anchor.
- Apportionment factors/formula: **needs-sources** (see §1).

## 4. Deadlines

- Consolidated-return election: **no later than the due date for the return, including extensions** (§422.37 preamble, text read 2026-10-27).
- Corporate return due end of the fourth month after year-end; estimates per §422.16(12) (see ia-corporate-income-tax skill).

## 5. Penalties and interest

- Restated income carries the graduated rates (5.5%→9.8%) plus interest under ch. 421 — rate **needs-sources**.
- **90-day non-filing/non-payment** lets the director certify to the secretary of state, **canceling** a domestic corporation's articles or a foreign corporation's authority to do business (§422.40(1), text read 2026-10-27); exercising privileges after cancellation is an offense (§422.40(2)).
- §422.39 imports §§422.24–422.27 collection/assessment machinery, including pass-through-entity assessment under §422.25A (text read 2026-10-27).

## 6. Cross-border interactions

- Foreign (out-of-state) corporations: Iowa taxes income from Iowa-located property/sources (§422.32(1)(g), text read 2026-10-27) and business income under the operational-relationship test.
- Nonresident individuals/entities receiving Iowa income: withholding under §422.16(2)(b) unless the department issues a **no-withholding certificate** after the nonresident pays estimated tax by the last day of the fourth month of their tax year (§422.17, text read 2026-10-27).
- No Iowa addback statute specific to royalties paid to related parties in zero-tax jurisdictions was located in ch. 422 subchapter III — flag as **needs-sources** rather than assert absence.

## 7. Worked examples

Domestic parent sells goods to a wholly-owned out-of-state subsidiary at $60/unit where fair price is $85/unit; 40,000 units:

```oa-check
name: IA 422.36(2) fair-price restatement
inputs:
  units: 40000
  charged: 60
  fair: 85
  top_rate: 0.098
steps:
  - understatement: (fair - charged) * units
  - extra_tax: understatement * top_rate
expected:
  understatement: 1000000.00
  extra_tax: 98000.00
```

Service-fee shifting: commonly-controlled group shifts $350,000 of Iowa-earning income to an affiliate via management charges; department reallocates under §422.36(3):

```oa-check
name: IA 422.36(3) reallocation
inputs:
  shifted: 350000
  top_rate: 0.098
  saved_rate: 0.055
steps:
  - extra_tax: shifted * top_rate
  - affiliate_relief: shifted * saved_rate
  - net_effect: extra_tax - affiliate_relief
expected:
  extra_tax: 34300.00
  affiliate_relief: 19250.00
  net_effect: 15050.00
```

## 8. Ask the client

- Is the group an IRC §1504(a) affiliated group — and has the director ever demanded a consolidated Iowa return?
- Intercompany goods/services/intangibles: is transfer documentation defensible against §422.36(2)-(3)?
- Are all group members using the same (statutory) allocation method — alternatives need the director's permission for every member?
- 90 days late on any corporate filing risks charter/authority cancellation under §422.40.

## Sources

1. Iowa Code §422.36 (returns; fair-price and income-shifting adjustments): https://www.legis.iowa.gov/docs/code/422.36.pdf (200, text read 2026-10-27)
2. Iowa Code §422.37 (consolidated returns): https://www.legis.iowa.gov/docs/code/422.37.pdf (200, text read 2026-10-27)
3. Iowa Code §422.32 (definitions: affiliated group, business income, commercial domicile): https://www.legis.iowa.gov/docs/code/422.32.pdf (200, text read 2026-10-27)
4. Iowa Code §422.40 (cancellation of authority for non-filing): https://www.legis.iowa.gov/docs/code/422.40.pdf (200, text read 2026-10-27)
5. Iowa Code §422.17 (no-withholding certificate): https://www.legis.iowa.gov/docs/code/422.17.pdf (200, text read 2026-10-27)
6. Iowa Code §422.39 (imported assessment/collection provisions): https://www.legis.iowa.gov/docs/code/422.39.pdf (200, text read 2026-10-27)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Iowa related-party and consolidated-return questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
