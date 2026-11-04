---
name: fl-annual-report
description: "Florida Annual Report filing for LLCs and corporations registered with the Division of Corporations (Sunbiz). Covers the annual report requirement, $138.75 fee for LLCs, filing deadline, late filing penalties, and administrative dissolution risk. Primary source: Florida Statutes Chapter 605 (LLCs) and Chapter 607 (corporations)."
version: 1.1
jurisdiction: US-FL
tax_year: 2025
last_updated: 2026-11-04
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - us-tax-workflow-base
category: state
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FL Annual Report

## Florida Annual Report (Sunbiz) v1.0

## Who this applies to

**Obligation category:** EF (Entity Fees)
**Functional role:** Entity filing
**Status:** Complete

This is a Tier 2 content skill that loads on top of `us-tax-workflow-base`. It covers the Florida Division of Corporations annual report filing requirement for LLCs and corporations registered to do business in Florida. The annual report is NOT a tax return; it is an informational filing that keeps entity status active with the state.

**Tax year coverage.** This skill targets **reporting year 2025** (report due by May 1, 2025, for entities formed or qualified before January 1, 2025).

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs off on the filing. The skill produces working papers and a brief, not the filed report itself.

### Scope statement

**In scope:**

- Florida domestic LLCs (Chapter 605, F.S.)
- Florida domestic corporations (for-profit, Chapter 607, F.S.)
- Florida domestic not-for-profit corporations (Chapter 617, F.S.)
- Foreign LLCs and corporations registered to transact business in Florida
- The Sunbiz annual report form (filed online at sunbiz.org)
- Supplemental report for changes made between annual reports

**Out of scope (refused):**

- Limited partnerships (Chapter 620, F.S.) -- separate filing regime
- Sole proprietors with no LLC -- no annual report requirement
- Fictitious name (DBA) renewals -- separate process under §865.09, F.S.
- Federal tax return preparation
- Florida corporate income tax (Form F-1120) -- separate skill
- Reinstatement of administratively dissolved entities

## Rates, bands and thresholds

**Fees**  _(See table)_

| Entity type | Annual report fee | Source |
| --- | --- | --- |
| LLC (domestic or foreign) | $138.75 | §605.0212(5)(a), F.S. |
| For-profit corporation (domestic or foreign) | $150.00 | §607.0122(1), F.S. |
| Not-for-profit corporation | $61.25 | §617.0122, F.S. |
| Late fee (profit corporations, LLCs, LPs, LLLPs; not-for-profits exempt) | $400.00 | §607.193(2)(b), F.S.; Sunbiz filing instructions |
| Registered agent change fee (if changing) | $25.00 | §605.0213(7), F.S.; Sunbiz LLC fee schedule |

### Fees note

- **Note on the $138.75 LLC fee** - This is Sunbiz's "Annual Report (& Supplemental Fee)" line: the $50 annual report fee under §605.0213(5), F.S. plus the $88.75 supplemental corporate fee under §607.193(1), F.S.  _(§605.0213(5), F.S.; §607.193(1), F.S.; Sunbiz LLC fee schedule)_

### Computation rules (Step format)

#### Step 1: Determine filing obligation

- **Determine filing obligation** -- - Confirm the entity is registered with the Florida Division of Corporations (search sunbiz.org by entity name or document number). - Confirm the entity's status is Active or Inactive (if inactive, this skill does not cover reinstatement). - If the entity was formed or qualified after January 1 of the current year, no annual report is due until the following year.  _(unsure)_

#### Step 2: Gather required information

- **Gather required information** -- The annual report requires the following data points: 1. Entity name (as registered) 2. Federal Employer Identification Number (FEIN) 3. Principal office address (street address required; P.O. Box alone is insufficient) 4. Mailing address 5. Registered agent name and address (must be a Florida street address) 6. Name and address of each manager/managing member (LLCs) or officer/director (corporations) 7. For LLCs: name and address of each authorized person (if different from manager)  _(unsure)_

#### Step 3: Verify registered agent

- **Verify registered agent** -- - The registered agent must be a Florida resident or a business entity authorized to transact business in Florida. - The registered agent's address must be a Florida street address (not a P.O. Box). - If changing the registered agent, the new agent must sign an acceptance.  _(unsure)_

#### Step 4: Complete the filing

- **Complete the filing** -- - Log in to sunbiz.org annual report filing system. - Enter the entity's document number. - Review pre-populated information and update any changes. - Confirm all manager/member or officer/director information is current. - Pay the filing fee electronically.  _(unsure)_

#### Step 5: Document the filing

- **Document the filing** -- - Record the confirmation number provided by Sunbiz. - Save/print the filing confirmation for the entity's records. - Note the filing date for the reviewer brief.  _(unsure)_

## The taxable base

The annual report is not a tax; there is no taxable base. The filing keeps entity status active and updates the registered record: entity name, FEIN, principal office and mailing addresses, registered agent (Florida street address required), and current managers/members or officers/directors.

## Deadlines and filing

### Who must file

- **Who must file** -- Every LLC, corporation, and not-for-profit corporation registered with the Florida Division of Corporations must file an annual report each year to maintain active status.  _(§605.0212, F.S. (LLCs); §607.1622, F.S. (corporations).)_

### When to file

**When to file**  _(See table)_

| Item | Detail | Source |
| --- | --- | --- |
| Filing window opens | January 1 of each year | Sunbiz filing instructions |
| Filing deadline | May 1 of each year | §605.0212(5), F.S.; §607.1622, F.S. |
| Late filing (supplemental fee) | After May 1, $400 late fee applies to profit corporations, LLCs, LPs and LLLPs; not-for-profit corporations are not subject to it | §607.193(2)(b), F.S.; Sunbiz filing instructions |
| Administrative dissolution | If no annual report filed by the 3rd Friday in September | §605.0714, F.S. |

### How to file

- **How to file** -- The annual report must be filed electronically through the Division of Corporations website (sunbiz.org). Paper filings are not accepted for annual reports.  _(sunbiz.org)_

## Penalties and interest

- A $400 late fee applies to annual reports filed after May 1 for profit corporations, limited liability companies, limited partnerships, and limited liability limited partnerships. Not-for-profit corporations are not subject to the $400 late fee.  _(Sunbiz filing instructions; §607.193(2)(b), F.S.)_
- There is no provision to abate or waive the $400 late fee; it applies even if the entity did not receive annual report filing notices.  _(Sunbiz filing instructions)_
- An LLC that fails to file may not maintain or defend an action in a Florida court until the report is filed and fees and penalties are paid, and is subject to dissolution.  _(§605.0212(6), F.S.)_

## Cross-border points

#### E-1: Entity formed mid-year

- **Entity formed mid-year** -- An LLC formed on July 15, 2024, must file its first annual report by May 1, 2025. The report covers the entity's current information as of the filing date, not a specific fiscal period.  _(§605.0212, F.S.)_

#### E-2: Multiple LLCs under same ownership

- **Multiple LLCs under same ownership** -- Each LLC is a separate filing. There is no consolidated annual report. Each pays its own $138.75 fee. Flag for reviewer if client has many LLCs -- the aggregate cost may be significant.  _(unsure)_

#### E-3: Address changes during the year

- **Address changes during the year** -- Address changes can be made on the annual report. If an address changes after the annual report is filed, a supplemental filing ($50 fee) can update the records before the next annual report cycle.  _(unsure)_

#### E-4: Foreign LLC withdrawing from Florida

- **Foreign LLC withdrawing from Florida** -- A foreign LLC that has filed a certificate of withdrawal is not required to file an annual report for the year following the effective date of withdrawal. However, the annual report for the year of withdrawal is still due.  _(§605.0906, F.S.)_

#### E-5: Administrative dissolution risk

- **Administrative dissolution risk** -- If the annual report is not filed by the third Friday in September, the entity will be administratively dissolved (LLCs) or revoked (corporations). This means the entity loses its legal authority to transact business in Florida. Reinstatement requires additional fees and filings.  _(§605.0714, F.S.)_

#### E-6: Disregarded entity status

- **Disregarded entity status** -- A single-member LLC that is disregarded for federal tax purposes is still treated as a separate legal entity under Florida law and must file the annual report. The federal tax classification does not affect the Sunbiz filing obligation.  _(unsure)_

## Worked examples

### Worked example 1: Standard LLC annual report

- **Input:** Active Florida domestic LLC, formed 2020, no changes to officers or address.
- **Expected output:** File annual report by May 1, 2025. Fee: $138.75. No late fee.
- **Verify:** Confirmation number documented.

### Worked example 2: Late filing

- **Input:** Active Florida domestic LLC, annual report not yet filed as of May 15, 2025.
- **Expected output:** File immediately. Fee: $138.75 + $400.00 late fee = $538.75.
- **Verify:** Flag for reviewer that late fee applies.

### Worked example 3: Corporation annual report

- **Input:** Active Florida for-profit corporation, standard filing.
- **Expected output:** Fee: $150.00 by May 1, 2025.
- **Verify:** Officer/director information current.

### Worked example 4: New LLC formed in current year

- **Input:** LLC formed March 15, 2025.
- **Expected output:** No annual report due until May 1, 2026. Flag for reviewer.

### Worked example 5: Multiple LLCs

- **Input:** Same owner operates 3 Florida LLCs.
- **Expected output:** 3 separate filings. Total fees: 3 x $138.75 = $416.25.

### Prohibitions

- **P-1:** Do NOT file the annual report without confirming current manager/member or officer/director information with the client. Stale data creates legal liability.
- **P-2:** Do NOT use a P.O. Box as the registered agent address. Florida requires a street address.
- **P-3:** Do NOT assume a disregarded LLC is exempt from annual report filing.
- **P-4:** Do NOT advise on whether to let an entity dissolve for tax planning purposes. That is legal advice outside this skill's scope.
- **P-5:** Do NOT attempt to file a paper annual report. Sunbiz requires electronic filing.

## Ask the client first

Before delivering output, verify:

- [ ] Entity is confirmed as registered on sunbiz.org
- [ ] Entity type (LLC, corporation, not-for-profit) correctly identified
- [ ] Correct fee amount used for entity type
- [ ] Filing deadline (May 1) has not passed; if passed, late fee included
- [ ] Registered agent address is a Florida street address
- [ ] All manager/member or officer/director names and addresses are current
- [ ] FEIN is provided and matches IRS records
- [ ] Confirmation number documented after filing
- [ ] Reviewer brief includes any flags (late filing, address changes, dissolution risk)

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| §605.0212 Fla. Stat. -- LLC annual report; first report due Jan 1-May 1 of following year | https://www.flsenate.gov/Laws/Statutes/2025/605.0212 | 2026-11-01 |
| §605.0213 Fla. Stat. -- LLC fees; $50 annual report filing fee | https://www.flsenate.gov/Laws/Statutes/2025/605.0213 | 2026-11-01 |
| §607.1622 Fla. Stat. -- corporation annual report; first report due Jan 1-May 1 of following year | https://www.flsenate.gov/Laws/Statutes/2025/607.1622 | 2026-11-01 |
| §607.193 Fla. Stat. -- $88.75 supplemental corporate fee; $400 late charge after May 1 | https://www.flsenate.gov/Laws/Statutes/2025/607.193 | 2026-11-01 |
| §607.0122 Fla. Stat. -- corporation filing fees | https://www.flsenate.gov/Laws/Statutes/2025/607.0122 | 2026-11-01 |
| §617.0122 Fla. Stat. -- not-for-profit filing fees; annual report $61.25 | https://www.flsenate.gov/Laws/Statutes/2025/617.0122 | 2026-11-01 |
| Sunbiz -- Annual Report filing instructions ($400 late fee scope; fee schedule) | https://efile.sunbiz.org/sbs_ar_instr.html | 2026-11-01 |
| Sunbiz -- LLC annual report help ($138.75 fee; $400 late fee) | https://efile.sunbiz.org/llc_ar_help.html | 2026-11-01 |
| Sunbiz -- LLC Fees schedule (Annual Report & Supplemental Fee $138.75; after May 1 $538.75) | https://dos.fl.gov/sunbiz/forms/fees/llc-fees/ | 2026-11-01 |
| Sunbiz -- Annual Report landing (third Friday in September dissolution date) | https://dos.fl.gov/sunbiz/manage-business/efile/annual-report/ | 2026-11-01 |

Not yet confirmed: the $25 registered-agent change fee as a line in §605.0212 (the $25 fee is in §605.0213(7) and the Sunbiz LLC fee schedule, not §605.0212); the $50 supplemental/amended annual report fee (Sunbiz LLC fee schedule only); the $150 for-profit corporation annual report fee (Sunbiz filing instructions state it; the archived §607.0122 fee list does not show a $150 annual report line); the §605.0714 dissolution statute text (the Sunbiz page confirms the third-Friday-in-September date).

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
