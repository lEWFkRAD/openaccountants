---
name: mo-transfer-pricing
description: >
  Use this skill whenever asked about Missouri transfer pricing and
  related-party rules for tax year 2026 — Missouri has no standalone TP
  documentation regime; related-party economics enter the MO-1120 base via
  the consolidated-federal/separate-Missouri pro forma rule, the optional
  Missouri consolidated return (Form MO-22, §143.431), Form MO-MS
  apportionment elections, the §163(j) interest addback, the dividends
  deduction on Form MO-C, and the related-party expense/intangible addback
  regime (§143.471, Form MO-470 — source pending). Trigger on "Missouri
  transfer pricing", "Missouri related party addback", "MO-470", "143.471",
  "Missouri consolidated return", "MO-MS apportionment election".
  Source-cited draft; 2025 MO-1120 instructions read 2026-10-27; MO-470
  fetch blocked (403) — addback specifics flagged not yet confirmed.
jurisdiction: US-MO
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - mo-corporate-income-tax
---

# Missouri transfer pricing / related-party overlay v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Missouri has **no standalone transfer-pricing documentation statute** — no state §482 analogue with its own penalty. Related-party pricing shapes Missouri outcomes through five verified levers in the 2025 MO-1120 instructions plus one addback regime whose source page was blocked this run:

1. **Consolidated federal / separate Missouri:** members of a federally consolidated group compute federal taxable income **as if separately filed**, attaching a **pro forma Federal Form 1120** — intercompany prices survive into each member's Missouri base. (Instructions, read 2026-10-27.)
2. **Optional Missouri consolidated return** (§143.431 RSMo; 12 CSR 10-2.045), only for federally consolidated groups, with **Form MO-22** per member. (Instructions, read 2026-10-27.)
3. **Form MO-MS apportionment elections** (2a, 3, 4, 5, 6, 7) — the election choice, not an arm's-length standard, drives the Missouri share. (Instructions, read 2026-10-27.)
4. **§163(j) disallowed business interest addback** (§143.121.3(11) RSMo) — intercompany interest that fails the federal cap is added back at Missouri. (Instructions, read 2026-10-27.)
5. **Dividends deduction mechanics on Form MO-C** keyed to the apportionment factor. (Instructions, read 2026-10-27.)
6. **Related-party expense / intangible addback (§143.471 RSMo, Form MO-470):** Missouri operates this regime, but the MO-470 instructions PDF returned **403** and the DOR addback page **404** from the drafting environment on 2026-10-27 — the addback's current scope, thresholds and exceptions are **not yet confirmed**; do not compute an MO-470 position from this skill alone.


### Who this applies to


- Corporations filing MO-1120 with intercompany royalties, management fees, rent, interest, or service charges crossing state lines.
- Federally consolidated groups: each member's separate-Missouri posture makes every intercompany price a Missouri-base question.
- Groups electing Missouri consolidation: MO-22 membership schedules expose the intercompany eliminations the Department will review.
- Lenders in the group: §163(j)-limited interest is added back at Missouri regardless of arm's-length status.

## Rates, bands and thresholds

| Item | Amount / rule | Source |
|---|---|---|
| Rate the adjustments land in | 4% flat (MO-1120 line 14) | Instructions, read 2026-10-27 |
| §163(j) addback | interest not deductible federally under §163(j) is added to Missouri income (§143.121.3(11)) | Instructions, read 2026-10-27 |
| MO-470 related-party addback | regime exists (§143.471); current scope/thresholds **not yet confirmed** | fetch log 2026-10-27 (403/404) |
| Combined reporting | none — Missouri uses separate returns or full consolidation, no unitary combined return | Instructions, read 2026-10-27 |
| TP documentation requirement | none at state level | absence verified in instructions read |

## The taxable base
Base levers (pro forma rule, MO-22 consolidation, MO-MS elections, §163(j) addback, MO-C, MO-470) are listed under "Who this applies to" above; no separate base section.
## Deadlines and filing

- No state TP documentation deadline.
- MO-470 (if required) is filed with MO-1120 — due the 15th day of the 4th month; automatic extension with federal Form 7004 (check the box). (Instructions, read 2026-10-27.)
- Missouri consolidated election: initial MO-22 with the first consolidated MO-1120; new members add MO-22 as added. (Instructions, read 2026-10-27.)

## Penalties and interest

- No TP-specific penalty. Adjustments land in the ordinary regime: 5%/month late-filing (cap 25%), 5% late-payment, **7% simple interest from 1 January 2026** (§32.065). (Instructions, read 2026-10-27.)
- MO-470-specific penalties: **not yet confirmed** (form instructions blocked).

## Cross-border points

- Apportionable income includes income from **tangible and intangible property** where the property's acquisition, management, employment, development or disposition relates to the trade or business — intercompany IP and financing sit inside the factor math. (Instructions, read 2026-10-27.)
- P.L. 86-272 protects goods-order solicitation only; intercompany services/royalties create nexus exposure — Form 4458 documents the boundary.
- No water's-edge election exists (no combined return at all).
- Another state's minimum tax does not by itself make the taxpayer "taxable" there — matters for MO-CR credit-for-taxes-paid claims. (Instructions, read 2026-10-27.)

## Worked examples

**Example 1 — intercompany royalty, separate-Missouri posture.** Member A (Missouri apportionment 40%) pays a $500,000 royalty to related Member B (no Missouri nexus). Royalty deducted pre-apportionment on A's separate-Missouri pro forma.

```oa-check
name: MO royalty strip effect
inputs:
  royalty: 500000
  factor: 0.40
  rate: 0.04
steps:
  - mo_deduction: royalty * factor
  - tax_saved: mo_deduction * rate
expected:
  mo_deduction: 200000.00
  tax_saved: 8000.00
```

If the Department re-prices or the MO-470 addback applies (scope **not yet confirmed**), the clawback is $8,000 plus 7% interest.

**Example 2 — §163(j) interest addback.** The group pays $300,000 intercompany interest; $120,000 is disallowed federally under §163(j); Missouri apportionment 25%.

```oa-check
name: MO 163j addback
inputs:
  disallowed: 120000
  factor: 0.25
  rate: 0.04
steps:
  - mo_addback: disallowed * factor
  - extra_tax: mo_addback * rate
expected:
  mo_addback: 30000.00
  extra_tax: 1200.00
```

## Ask the client first

1. Federally consolidated? Separate-Missouri pro forma or Missouri consolidated (MO-22) — which, and why?
2. Which MO-MS apportionment election is in use, and would another election reduce Missouri exposure?
3. Any MO-470 filing history — and has anyone read the current instructions (fetch was blocked this run)?
4. Intercompany interest: does §163(j) disallowance flow to the Missouri addback?
5. Do intercompany services/royalties exceed P.L. 86-272 — is Form 4458 on file?

## Sources

| # | Source | URL | Read on |
| --- | --- | --- | --- |
| 1 | Missouri DOR, Form MO-1120 General Instructions (2025) (pro forma rule, MO-22 consolidation, MO-MS elections, §163(j) addback, MO-C, P.L. 86-272/Form 4458) | https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf | 2026-10-28 |
| 2 | Form MO-470 instructions | https://dor.mo.gov/forms/MO-470%20Instructions_2025.pdf | 2026-10-29 |
Not yet confirmed: the items above flagged as not sourced, and the RSMo cites (§143.431, §143.471, §143.121.3(11), §32.065) — no archived copy of those sections exists yet; figures tied to them stay unconfirmed until the source is archived with readable text..

## Talk to a verified accountant

**Talk to a verified accountant** — for Missouri related-party and consolidation questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

<!-- openaccountants-cta-block -->
