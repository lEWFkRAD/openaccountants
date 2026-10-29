---
name: la-transfer-pricing
description: >
  Use this skill whenever asked about Louisiana transfer pricing and
  related-party adjustments for tax year 2026 — Louisiana has no
  standalone TP documentation regime; related-party exposure runs through
  unitary combined reporting, the water's-edge and addback toolkit, and
  the apportionment base. Trigger on "Louisiana transfer pricing",
  "Louisiana combined report", "Louisiana unitary", "Louisiana related
  party addback", "R.S. 47:287.83". Source-cited draft; corporate duty
  and 5.5% rate verified from LDR 2026-10-28; statutory combination and
  addback detail needs-sources (legis.la.gov session-state).
jurisdiction: US-LA
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - la-corporate-income-tax
---

# Louisiana transfer pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-28. **Louisiana has no standalone transfer-pricing documentation statute** (no state documentation mandate, no state CbCR). Related-party risk arises from: (1) **unitary combined reporting** (R.S. 47:287.83 series — combination required for affiliated groups above an ownership threshold; exact test **needs-sources**), (2) **addback adjustments** for intangible/management payments to related low-tax affiliates, and (3) the **apportionment base**. **Source status:** the LDR Corporation Income Tax page (filing duty, 5.5% flat rate) verified 2026-10-28; **legis.la.gov requires session state for article text**, so statutory citations, thresholds, and forms are **needs-sources** — treat this as a map of exposure, not authority.

## 2. Who applies

- **Affiliated/unitary groups** with Louisiana filing members — combined-report exposure (ownership test expected 80%-type; **needs-sources**).
- Any CIFT-620 filer making **intercompany royalty, interest, management, or service payments** to out-of-state affiliates — addback exposure.
- Multistate filers whose **intercompany sales** move the Louisiana apportionment factor.
- **S corporations taxed as corporations for Louisiana** (verified category on LDR page) — intra-group pricing matters at the entity level.

## 3. Rules and adjustments

| Mechanism | Rule sketch | Source status |
|---|---|---|
| Combined report | unitary combination for affiliated groups; R.S. 47:287.83 expected | **needs-sources** |
| Intangible addback | royalties/license fees to related low-tax affiliates added back | **needs-sources** |
| Management/service fee addback | similar for shared-services fees | **needs-sources** |
| Interest | federal §163(j) carries into the state base; no separate state thin-cap identified | **needs-sources** |
| CbCR | no Louisiana-specific CbCR | structural, low risk |
| Arm's-length standard | federal §482 flows through the federal-taxable-income starting point | **needs-sources** |

## 4. Deadlines

- No separate TP filing calendar; adjustments ride CIFT-620 (due 15th day of 5th month — verified) and any combined-report attachment.
- Keep contemporaneous federal §6662(e) documentation — Louisiana examiners use the federal file. Linkage **needs-sources**.

## 5. Penalties and interest

- Understatements carry interest and accuracy penalties under R.S. 47 — tiers **needs-sources**.
- No Louisiana-specific TP documentation penalty identified — absence **needs-sources**.

## 6. Cross-border interactions

- Foreign-parent groups: federal §482 starting point; state combination layers on top — **needs-sources**.
- Intangible holding companies in zero-tax states (TX/NV/WY) are the classic Louisiana addback target given the 5.5% flat rate makes adjustments material.
- Combined reporting pulls out-of-state affiliates into one Louisiana factor set.

## 7. Worked examples

**Example 1 — royalty addback exposure (illustrative):** Louisiana operating company pays $500,000 royalties to a related Texas affiliate (no TX income tax); illustrative 30% addback at the verified 5.5% rate.

```oa-check
name: LA royalty addback (illustrative addback, verified rate)
inputs:
  royalty: 500000
  addback_pct: 30
  corp_rate: 0.055
steps:
  - addback: royalty * addback_pct / 100
  - tax_effect: addback * corp_rate
expected:
  addback: 150000
  tax_effect: 8250
```

**Example 2 — arm's-length defense:** benchmarking supports $300,000 royalties instead of $500,000; same illustrative parameters.

```oa-check
name: LA royalty after benchmarking
inputs:
  royalty: 300000
  addback_pct: 30
  corp_rate: 0.055
steps:
  - addback: royalty * addback_pct / 100
  - tax_effect: addback * corp_rate
expected:
  addback: 90000
  tax_effect: 4950
```

## 8. Ask the client

- Entity map: which affiliates receive intercompany payments and where are they taxed?
- Is the group unitary/common-controlled — combined-report trigger?
- Federal §6662(e) documentation on file?
- Intercompany sales volumes that could swing the Louisiana sales factor.

## 9. Sources

- LDR Corporation Income Tax (duty, 5.5% flat rate, S-corp-as-corporation category): https://revenue.louisiana.gov/businesses/widely-used-tax-types/corporate-income-franchise-tax/ — read 2026-10-28, verified.
- La. R.S. 47:287.83 (combination — numbering expected, unverified): https://legis.la.gov/legis/Laws_Toc.aspx?folder=90&title=47 — resolves; article text session-state; **needs-sources**.

**Needs-sources:** combination ownership test and form, addback statute numbering/scope, interest treatment beyond federal 163(j), penalty tiers, S-corp combined applicability.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Louisiana related-party questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
