---
name: ks-transfer-pricing
description: >
  Use this skill whenever asked about Kansas transfer pricing and
  related-party adjustments for tax year 2026 — Kansas has no standalone
  TP documentation regime; related-party exposure runs through combined
  reporting, intangible/management-fee addbacks, and the apportionment
  base. Trigger on "Kansas transfer pricing", "Kansas combined report",
  "Kansas related party", "Kansas addback", "Kansas unitary".
  Source-cited draft; statutory basis needs-sources (kslegislature.org
  JS-only this run); KDOR corporate duty verified 2026-10-28.
jurisdiction: US-KS
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ks-corporate-income-tax
---

# Kansas transfer pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-28. **Kansas has no standalone transfer-pricing documentation statute** (no state version of IRC §482 documentation requirements, no state CbCR). Related-party pricing risk in Kansas arises from three mechanisms: (1) **combined reporting** for affiliated/unitary groups, (2) **addback adjustments** for intangible and management-fee payments to related low-tax affiliates, and (3) the **apportionment base** itself (intercompany sales shift the sales factor). **Source status:** the KDOR Corporate Income page (filing duty, entity scope) was verified 2026-10-28; **kslegislature.org returns a JS shell with no statute text to plain HTTP**, so every statutory citation, threshold, and form ID below is **needs-sources** — treat this skill as a map of where the exposure lives, not as authority.

## 2. Who applies

- Members of an **affiliated/unitary group** doing business in Kansas — combined-report exposure (form ID, e.g. K-120M, unverified).
- Any K-120 filer making **intercompany payments** (royalties, interest, management fees) to out-of-state affiliates — addback exposure.
- Multistate filers whose **intercompany sales** move the Kansas apportionment factor.
- S corporations: distributive-share pricing issues flow to shareholders; combined reporting applicability to S corps **needs-sources**.

## 3. Rules and adjustments

| Mechanism | Rule sketch | Source status |
|---|---|---|
| Combined report | unitary/affiliated group files on combined basis; ownership test (80%-type expected) | **needs-sources** |
| Intangible addback | royalties/license fees paid to related affiliates in low/no-tax states added back | **needs-sources** (statute numbering 79-32.140 series unverified) |
| Management-fee / service-fee addback | similar addback for management, shared-services fees | **needs-sources** |
| Interest addback | thin-cap-style or related-party interest limits at state level | **needs-sources** (likely none beyond federal 163(j)) |
| CbCR | no Kansas-specific CbCR | structural, low risk |
| Arm's-length standard | federal §482 principles carry into the Kansas base via federal taxable income starting point | **needs-sources** |

## 4. Deadlines

- No separate Kansas TP filing calendar; adjustments ride the K-120 return and any combined-report attachment (due with the return — 15th day of 4th month).
- Transfer-pricing documentation for audit defense: keep contemporaneous federal §6662(e) principal-file work — Kansas examiners use it. **needs-sources** for Kansas-specific penalty linkage.

## 5. Penalties and interest

- Understatement adjustments carry interest; accuracy penalties under K.S.A. 79-32 — tiers **needs-sources**.
- No Kansas-specific TP documentation penalty identified — **needs-sources** (absence unverified).

## 6. Cross-border interactions

- Foreign-parent groups: Kansas follows the federal §482 starting point; state adjustments layer on top — **needs-sources**.
- intangible holding companies in zero-tax states (DE/NV/WY patterns) are the classic Kansas addback target.
- Combined reporting pulls out-of-state affiliates' Kansas-sourced results into one factor set.

## 7. Worked examples

**Example 1 — royalty addback exposure (illustrative):** Kansas operating company pays $400,000 royalties to a related affiliate in a no-income-tax state; illustrative 25% of the deduction added back.

```oa-check
name: KS royalty addback (illustrative)
inputs:
  royalty: 400000
  addback_pct: 25
  corp_rate: 0.12
steps:
  - addback: royalty * addback_pct / 100
  - tax_effect: addback * corp_rate
expected:
  addback: 100000
  tax_effect: 12000
```

**Example 2 — arm's-length range defense:** royalty reduced to $250,000 after benchmarking; addback and tax effect at the same illustrative parameters.

```oa-check
name: KS royalty after benchmarking
inputs:
  royalty: 250000
  addback_pct: 25
  corp_rate: 0.12
steps:
  - addback: royalty * addback_pct / 100
  - tax_effect: addback * corp_rate
expected:
  addback: 62500
  tax_effect: 7500
```

## 8. Ask the client

- Entity map: which affiliates receive intercompany payments, and where are they taxed?
- Is the group unitary (common control, integrated operations) — combined-report trigger?
- Federal §6662(e) documentation on file? Kansas examiners will ask for it.
- Intercompany sales volumes that could swing the Kansas sales factor.

## 9. Sources

- KDOR Corporate Income (entity scope, filing duty): https://www.ksrevenue.gov/bustaxtypescorp.html — read 2026-10-28, verified.
- K.S.A. 79-32-110 (corporate rates, starting point): https://www.kslegislature.org/li/b2025_26/statutes/2025_79-32-110/ — HTTP 200, JS shell; **needs-sources**.
- Kansas apportionment/combined statutes (79-32.140 series — numbering unverified): https://www.kslegislature.org/li/ — search UI is JS-only; **needs-sources**.

**Needs-sources:** combined-report ownership test and form ID, addback statute numbering and scope, interest addback existence, penalty tiers, S-corp combined applicability.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kansas related-party questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
