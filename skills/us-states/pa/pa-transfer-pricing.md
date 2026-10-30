---
name: pa-transfer-pricing
description: >
  Use this skill whenever asked about Pennsylvania transfer pricing and
  combined reporting for tax year 2026 -- the choice between NON-COMBINED
  (entity-by-entity) and COMBINED (unitary group) RCT-1 filing, the
  intercompany-transaction addback rule of 72 P.S. § 7337 (dividends,
  royalties, rents, interest and similar payments to related members added
  back unless the taxpayer proves a business purpose and arm's-length
  pricing), the unitary-combination test (unity of ownership, operation and
  an integrated enterprise), and apportionment consequences of combining.
  Trigger on "Pennsylvania combined return", "PA unitary", "RCT-1 combined",
  "7337 addback", "Pennsylvania addback", "PA intercompany royalties",
  "Pennsylvania combined reporting election".
  Source-cited draft; 72 P.S. § 7337 and the combined-reporting provisions
  could NOT be retrieved from legis.state.pa.us on 2026-10-27 (all probed
  USC paths 404 -- the CNIT article is an uncodified session law) -- statute
  text is not yet confirmed and mechanics are flagged as unverified.
jurisdiction: US-PA
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - pa-corporate-income-tax
---

# Pennsylvania transfer pricing / combined reporting v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Pennsylvania professional.

## Who this applies to

How related-party pricing and group structure interact with the Corporate Net Income Tax: the **combined vs non-combined RCT-1 choice**, the **unitary group** test, and the **§ 7337 intercompany addback** that makes transfer-pricing documentation the central PA corporate compliance issue.

**Source status (as_of 2026-10-27):** 72 P.S. § 7337 and the CNIT combined-reporting provisions **could not be retrieved** -- every probed legis.state.pa.us USC path returned 404 on 2026-10-27 (the CNIT is the uncodified Act of Mar. 4, 1971). The mechanics below are the standard, widely-described PA framework and are flagged **not yet confirmed**; do not compute a filing position from them without pulling the current statute/RCT-1 instructions.

### 2. Who applies

- Every CNIT filer chooses a filing posture: **non-combined** (each entity files its own RCT-1) or **combined** (the unitary group files one combined RCT-1). Certain affiliated groups meeting the ownership thresholds file combined returns; others may elect.
- The **§ 7337 addback** applies to non-combined filers with intercompany dividends, royalties, rents, interest, management/service fees and similar payments to related members -- the classic PA trap.
- Combined filers eliminate intercompany transactions inside the group, which is why groups with heavy intercompany payments usually prefer combining.

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| CNIT rate | See `pa-corporate-income-tax` -- 2026 rate not yet confirmed | not yet confirmed |
| § 7337 addback | Intercompany dividends/royalties/rents/interest/similar payments added to income **unless** the taxpayer proves a business purpose AND arm's-length pricing (the "double burden") | 72 P.S. § 7337 -- **not yet confirmed** (not retrievable 2026-10-27) |
| Unitary test | Unity of ownership + unity of operation + an integrated enterprise (functionally related/contributory) | not yet confirmed |
| Combined election | Made on the combined RCT-1; consistency rules apply across years | not yet confirmed |
| Apportionment | Single sales factor (post-2014 -- not yet confirmed); combined group apportions as one | not yet confirmed |

### 4. Deadlines

| Filing | Due |
|---|---|
| Combined RCT-1 | Same April 15 as the RCT-1 (not yet confirmed re-verify) |
| Election / revocation | With the return for the year of change -- not yet confirmed |
| Documentation for the 7337 burden | Contemporaneous; produce on audit |

### 5. Penalties and interest

- Failed 7337 burden → the full intercompany payment is added back; interest runs on the deficiency (rate not yet confirmed).
- PA audits of royalty/management-fee structures are a known enforcement area -- **AUDIT FLASH POINT**: intangible-royalty and shared-services charges from related parties are the highest-risk PA corporate positions.

### 6. Cross-border

- Combined groups can sweep **foreign affiliates** into the PA base when unitary -- the main PA cross-border exposure.
- Non-combined foreign-parent structures face the 7337 addback on cross-border royalties/management fees.
- Compare Ohio: no unitary concept for CAT combined reporting (`oh-transfer-pricing`) and no gross-receipts addback analogue.

### 7. Worked examples

**Example A -- § 7337 addback exposure, non-combined filer.**

```oa-check
name: Addback of royalty to related affiliate without meeting the burden
inputs:
  pa_apportioned_income_before: 1500000
  royalty_to_affiliate: 400000
  rate: 0.0649
steps:
  - income_after_addback: pa_apportioned_income_before + royalty_to_affiliate
  - cnit: income_after_addback * rate
expected:
  income_after_addback: 1900000
  cnit: 123310.00
```

The royalty was deducted in computing the 1,500,000; failing the business-purpose + arm's-length burden adds it back. Rate is the hypothetical 6.49% step -- **not yet confirmed for 2026**.

**Example B -- combined group nets the same payment away.**

```oa-check
name: Combined group eliminates the intercompany royalty
inputs:
  entity_a_income: 1900000
  entity_b_loss: -300000
  royalty: 400000
  rate: 0.0649
steps:
  - combined_income: entity_a_income + entity_b_loss
  - cnit: combined_income * rate
expected:
  combined_income: 1600000
  cnit: 103840.00
```

Inside a combined return the royalty disappears (elimination) and the affiliate's loss joins the group -- the structural reason PA groups elect combining.

### 8. Ask the client

- Combined or non-combined posture -- and is it consistent across years and states?
- Every intercompany royalty, rent, management fee, interest note: is there contemporaneous transfer-pricing documentation meeting the 7337 double burden?
- Is the group unitary (ownership + operation + integration)?
- Foreign affiliates: in or out of the combined group?
- Ohio/other-state posture for the same entities -- inconsistent group definitions across states invite audits.

### 9. Sources

- 72 P.S. § 7337 (intercompany addback) -- **not yet confirmed**: probed legis.state.pa.us USC paths 404 on 2026-10-27
- CNIT combined-reporting provisions (Act of Mar. 4, 1971) -- **not yet confirmed**: same 404 pattern
- [PA Revenue CNIT page](https://www.revenue.pa.gov/Businesses/Taxes/CorporateNetIncomeTax.aspx) -- HTTP 200 2026-10-27, JS shell
- `pa-corporate-income-tax` (this pack) -- rate status; `oh-transfer-pricing` -- Ohio contrast
- **not yet confirmed:** statute text, election mechanics, 2026 apportionment factor rules, interest rate.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Pennsylvania combined-return and intercompany-pricing questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

## Rates, bands and thresholds

Not yet confirmed against archived sources.

## The taxable base

Not yet confirmed against archived sources.

## Deadlines and filing

Not yet confirmed against archived sources.

## Penalties and interest

Not yet confirmed against archived sources.

## Cross-border points

Not yet confirmed against archived sources.

## Worked examples

Not yet confirmed against archived sources.

## Ask the client first

Not yet confirmed against archived sources.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.


| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | -- | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
