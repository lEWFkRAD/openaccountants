---
name: wy-sales-tax
description: Use this skill whenever asked about Wyoming sales tax, Wyoming use tax, Wyoming DOR sales tax filing, or Wyoming sales tax compliance. Trigger on phrases like "Wyoming sales tax", "WY sales tax", "W.S. §39-15", "Wyoming DOR", "Wyoming no income tax", "Wyoming SST", or any request involving Wyoming state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
jurisdiction: US-WY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# WY Sales Tax

## Who this applies to

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Wyoming, United States |
| Jurisdiction Code | US-WY |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 4.00% (W.S. 39-15-104) |
| Local Rate | Up to 2.00% county option (W.S. 39-15-204(a)(i), (iii)) |
| Primary Statute | Wyoming Statutes (W.S.) §39-15-101 et seq. |
| Governing Agency | Wyoming Department of Revenue (DOR) |
| Portal | https://revenue.wyo.gov |
| SST Member | Yes -- Full Member |
| No State Income Tax | Yes |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: local rate determination, mineral/energy industry, service taxability. T3: audit defense, complex energy transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

### Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic** -- Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required** -- Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate** -- Do not guess. Escalate to a licensed tax professional.

### Step 0: Client Onboarding Questions

Before proceeding with any Wyoming sales tax analysis, collect the following from the client: [T1]

**Client Onboarding Questions**

| # | Question | Why It Matters |
| --- | --- | --- |
| 1 | Do you have a Wyoming sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Wyoming? | Drives taxability classification under Wyoming law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Wyoming? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Wyoming local jurisdictions? | Local tax rates vary; determines compliance complexity. |

- **Stop condition** -- If the client cannot answer questions 1-4, STOP and gather this information before proceeding. ([T1])

### 1.1 State Sales Tax Rate

- **State Sales Tax Rate** -- 4.00% (T1)  _(W.S. §39-15-104.)_

### 1.2 No State Income Tax [T1]

- **No State Income Tax** -- Wyoming has no state individual or corporate income tax. Sales tax, mineral severance taxes, and property taxes are the primary revenue sources. ([T1])

### 1.3 Local Sales Taxes [T1]

- **County additional sales tax** -- Counties may impose additional sales tax up to 2.00% (general purpose + specific purpose). ([T1])  _(W.S. §39-15-204(a)(i) and (iii).)_
- **Most counties impose local option tax** -- Most counties impose some form of local option tax. ([T1])
- **Combined rate range** -- Combined rates are the 4.00% state rate (W.S. §39-15-104) plus county option taxes (W.S. §39-15-204(a)(i) and (iii)). ([T1])
- **Local tax administration** -- Local taxes are administered by the Wyoming DOR. ([T1])

### 1.4 Sourcing [T1]

- **Sourcing method** -- Wyoming uses destination-based sourcing. ([T1])
- **SST sourcing rules** -- As an SST member, Wyoming follows SSUTA sourcing rules. ([T1])

### 2.1 Grocery Food -- EXEMPT [T1]

- **Unprepared grocery food** -- exempt ([T1])  _(W.S. §39-15-105(a)(viii))_
- **Prepared food** -- taxable at full combined rate ([T1])
- **Candy** -- taxable ([T1])
- **Soft drinks** -- taxable ([T1])
- **SST food definitions** -- Wyoming follows SST food definitions. ([T1])

### 2.2 Clothing [T1]

- **Clothing taxability** -- Clothing is fully taxable. No exemption. ([T1])

### 2.3 Prescription Drugs and Medical [T1]

- **Prescription drugs** -- exempt ([T1])  _(W.S. §39-15-105(a)(iv))_
- **OTC drugs** -- taxable ([T1])
- **DME** -- exempt with prescription ([T1])
- **Prosthetics** -- exempt ([T1])

### 2.4 Services [T2]

Wyoming taxes a limited number of services:

- **Taxable services** -- Intrastate telecommunications, public utilities, lodging, admissions/amusements. ([T2])
- **Exempt services** -- Professional services, personal care, repair labor, cleaning, landscaping, IT services. ([T2])
- **Service tax base** -- Wyoming has a narrow service tax base focused on TPP and a few enumerated services. ([T2])

### 2.5 SaaS and Digital Goods [T2]

- **SaaS** -- Generally not taxable in Wyoming. Not considered TPP or an enumerated service. ([T2])
- **Canned software (physical)** -- Taxable. ([T1])
- **Canned software (electronic delivery)** -- Generally not taxable under current law. ([T2])
- **Digital downloads** -- Generally not taxable. Wyoming has not broadly adopted digital goods taxation. ([T2])
- **Custom software** -- Exempt. ([T2])

### 2.6 Manufacturing [T2]

- **Broad manufacturing equipment exemption** -- Wyoming does NOT have a broad manufacturing equipment exemption. ([T2])
- **Specific incentive programs** -- Some equipment may qualify under specific incentive programs. ([T2])
- **Raw materials for resale** -- exempt under resale exemption ([T1])

### 2.7 Mineral and Energy Industry [T2]

- **Economy reliance** -- Wyoming's economy is heavily reliant on mineral extraction (coal, oil, gas, trona, uranium). ([T1])
- **Mining and drilling equipment** -- generally taxable at the full combined rate ([T2])
- **Mineral severance taxes** -- Mineral severance taxes (coal, oil, gas, trona) are separate from sales tax. ([T1])
- **Wind energy equipment** -- may qualify for specific exemptions under economic development incentives ([T2])
- **Flag for reviewer** -- Mineral/energy tax compliance involves multiple tax types. Escalate complex scenarios. ([T3])

### 2.8 Agricultural [T1]

- **Farm and ranch machinery and equipment** -- exempt ([T1])  _(W.S. §39-15-105(a)(vi))_
- **Feed, seed, fertilizer** -- exempt ([T1])
- **Livestock** -- exempt for breeding/production ([T1])

### 4.1 Filing Details [T1]

**Filing Details**

| Field | Detail |
| --- | --- |
| Return Form | Sales/Use Tax Return (filed via WyoTax) |
| Filing Frequencies | Monthly, quarterly, or annually, as assigned by the Wyoming DOR |
| Due Date | Last day of the month following the reporting period |
| Portal | https://excise.wyo.gov (WyoTax) |
| E-filing | Required for most filers |

- **Due date note** -- Wyoming's due date is the last day of the following month. ([T1])

### 4.2 Vendor Discount [T1]

- **Vendor Discount** -- 1.95% of the tax due, credited for payment by the fifteenth day of the month the tax is due, capped at $500 per month. ([T1])  _(W.S. §39-15-107(b)(xi).)_

### 4.3 Penalties and Interest [T1]

- **Late filing penalty** -- $10 if the vendor files the return within thirty (30) days of receiving the department's delinquency notice, or $25 if the return is filed later. ([T1])  _(W.S. §39-15-108(c)(xiii).)_
- **Interest** -- For sales made on or after July 1, 1994, interest accrues at an annual rate equal to the average prime interest rate as determined by the state treasurer for the preceding fiscal year, plus 4%; the rate is adjusted on January 1 of each year and in no instance exceeds 18%. ([T1])  _(W.S. §39-15-108(b)(i).)_

### Step 4: Deductibility / Exemptions

Exemptions identified in Step 2 above are the primary deductibility rules for Wyoming. Key categories: [T1]

- **Resale exemption** -- Valid resale certificate required. Retain for the statutory period. ([T1])
- **Exempt organizations** -- Government entities and qualifying nonprofits -- require exemption certificate on file. ([T1])
- **Agricultural exemptions** -- Where applicable per Step 2. ([T1])
- **Manufacturing exemptions** -- Where applicable per Step 2. ([T2])
- **Exemption certificate collection** -- All exemption certificates must be collected at or before the time of sale and retained per the state's statute of limitations. ([T1])

### 3.1 Economic Nexus Threshold [T1]

**Economic Nexus Threshold**  _(W.S. §39-15-501(a)(i).)_

| Field | Detail |
| --- | --- |
| Revenue Threshold | $100,000 in gross revenue from sales delivered into Wyoming (W.S. 39-15-501(a)(i)) |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |

### 3.2 Marketplace Facilitator [T1]

- **Marketplace facilitator collection requirement** -- Wyoming requires marketplace facilitators to collect and remit. ([T1])  _(W.S. §39-15-501(a)(ix))_

### 3.3 SST Registration [T1]

- **SST Registration** -- Full SST member. SSTRS and CSPs available. ([T1])

### Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

### PROHIBITIONS

- **Grocery food** -- NEVER tax grocery food in Wyoming. Unprepared food is exempt. ([T1])
- **Uniform rate assumption** -- NEVER assume a uniform 4% rate across Wyoming. County option taxes add up to 2% each (general purpose and specific purpose). ([T1])  _(W.S. §39-15-104; W.S. §39-15-204(a)(i) and (iii).)_
- **SaaS taxability assumption** -- NEVER assume SaaS is taxable in Wyoming. Current law does not tax SaaS. ([T2])
- **Mineral/energy context** -- NEVER ignore the mineral/energy industry context. Wyoming's economy and tax structure revolve around natural resources. ([T2])
- **Filing deadline** -- NEVER file Wyoming returns by the 20th. The due date is the last day of the following month. ([T1])
- **No arithmetic by Claude** -- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. ([T1])

### EC1 -- No Income Tax + Low Sales Tax [T1]

**Situation:** A business considers incorporating or relocating to Wyoming for tax advantages.

**Resolution:**
- Wyoming has no individual or corporate income tax. [T1]
- Sales tax rates are moderate (4% state plus county option taxes of up to 2% each). [T1]  _(W.S. §39-15-104; W.S. §39-15-204(a)(i) and (iii).)_
- However, mineral severance taxes, property taxes, and the Commerce Tax equivalent should be considered. [T2]
- Wyoming is a popular state for LLCs and holding companies due to privacy laws and no income tax. [T1]
- **Flag for reviewer:** Total tax burden analysis requires evaluating all tax types, not just sales tax. [T2]

### EC2 -- Energy Industry Equipment [T2]

**Situation:** An oil company purchases drilling equipment for use in Wyoming.

**Resolution:**
- Drilling equipment is generally subject to sales tax at the full combined rate. [T2]
- No broad manufacturing/mining equipment exemption exists. [T2]
- The oil company also faces mineral severance taxes on production. [T1]
- Specific incentive programs may provide relief for certain types of equipment. [T2]
- **Flag for reviewer:** Verify whether any specific exemptions or incentive programs apply to the equipment type. [T2]

### EC3 -- SaaS Not Taxable [T2]

**Situation:** A technology company asks whether its SaaS product sold to Wyoming customers is taxable.

**Resolution:**
- SaaS is generally NOT taxable in Wyoming under current law. [T2]
- Wyoming's sales tax base focuses on TPP and limited enumerated services. [T2]
- The company should still monitor for legislative changes. [T2]
- **Flag for reviewer:** Wyoming's position on SaaS and digital goods is evolving. Verify current DOR guidance. [T2]

### EC4 -- Agricultural Equipment Exemption [T1]

**Situation:** A rancher purchases a new tractor for use on a cattle ranch.

**Resolution:**
- Farm and ranch machinery is exempt from sales tax. W.S. §39-15-105(a)(vi). [T1]
- The rancher must qualify as a bona fide agricultural producer. [T1]
- The equipment must be used in agricultural production. [T1]
- A mixed-use vehicle used partly for personal purposes may not fully qualify. [T2]
- **Flag for reviewer:** Verify agricultural producer status and primary use of the equipment. [T2]

### EC5 -- Wind Farm Equipment [T2]

**Situation:** A wind energy company purchases wind turbines and related equipment for a Wyoming wind farm.

**Resolution:**
- Wyoming may offer tax incentives for wind energy development. [T2]
- Without a specific exemption, equipment is subject to sales tax at the combined rate. [T2]
- Check current economic development incentive programs for renewable energy. [T2]
- **Flag for reviewer:** Wind energy incentives change with legislative sessions. Verify current programs with Wyoming DOR or WYDEQ. [T2]

### EC6 -- Tourism and Lodging in Jackson Hole [T2]

**Situation:** A hotel in Jackson, WY charges a nightly room rate. What taxes apply?

**Resolution:**
- State sales tax: 4%. [T1]  _(W.S. §39-15-104.)_
- Teton County optional tax: up to 2%. [T1]  _(W.S. §39-15-204(a)(i) and (iii).)_
- Wyoming does not impose a separate state lodging tax. [T1]
- Local lodging taxes may apply (varies by county/city). [T2]
- Combined tax on lodging depends on the specific jurisdiction. [T2]
- **Flag for reviewer:** Jackson/Teton County is a high-tourism area. Verify all applicable local taxes. [T2]

### EC7 -- Use Tax on Cross-Border Personal Purchases [T1]

**Situation:** A Wyoming resident purchases furniture in Montana (no sales tax) and brings it to Wyoming.

**Resolution:**
- Wyoming use tax is due on the purchase at the applicable combined rate. [T1]
- No credit for Montana tax (Montana has no sales tax, so $0 was paid). [T1]
- The resident should report and remit use tax. [T1]
- **Flag for reviewer:** Montana has no sales tax, so no credit applies. Full Wyoming use tax is due. [T1]

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Cheyenne sells equipment at a combined rate of 4% state plus 2% county option.  _(W.S. §39-15-104; W.S. §39-15-204(a)(i).)_
**Expected output:** Tax and total are computed by the deterministic engine at the combined rate.

### Test 2 -- Grocery Food Exempt

**Input:** Customer buys groceries in Casper.
**Expected output:** Groceries are exempt; tax and total are computed by the deterministic engine.

### Test 3 -- Farm Equipment Exempt

**Input:** Rancher buys a tractor for ranch use.
**Expected output:** Farm machinery is exempt; tax and total are computed by the deterministic engine.

### Test 4 -- Economic Nexus

**Input:** Remote seller's gross revenue from sales delivered into Wyoming exceeded $100,000 in the prior calendar year.  _(W.S. §39-15-501(a)(i).)_
**Expected output:** Economic nexus is triggered; the seller must register and collect.

### Test 5 -- Clothing Taxable

**Input:** Customer buys a jacket in Jackson at the applicable combined rate.
**Expected output:** Clothing is taxable; tax and total are computed by the deterministic engine at the combined rate.

### Test 6 -- Lodging in Jackson

**Input:** Guest stays at a Jackson hotel at the applicable combined rate plus any local lodging tax.
**Expected output:** Tax and total are computed by the deterministic engine at the combined rate.

### Test 7 -- Use Tax from Montana Purchase

**Input:** Wyoming resident buys furniture in Montana (no tax paid) for use in Wyoming.
**Expected output:** Use tax is due at the applicable combined rate; no credit applies because Montana has no sales tax.

### Test 8 -- Vendor Discount Calculation

**Input:** Wyoming seller collects tax for the month and files on time.
**Expected output:** The vendor discount is 1.95% of the tax due, capped at $500 per month; the remittance is computed by the deterministic engine.  _(W.S. §39-15-107(b)(xi).)_

### Reviewer Escalation Protocol

**Reviewer Escalation Protocol**

| Trigger | Action |
| --- | --- |
| Any [T3] tagged item encountered | STOP. Do not guess. Escalate to licensed CPA, EA, or tax attorney. |
| Client has audit notice or assessment | Escalate immediately. Do not advise on audit response. |
| Multi-state nexus question involving 3+ states | Flag for senior reviewer with multi-state experience. |
| Penalty abatement or voluntary disclosure | Escalate to licensed professional with state-specific experience. |
| Ambiguous taxability of a product/service | Present both interpretations to reviewer with supporting authority. |

### Contribution Notes

- This skill follows the Q1 execution format (Step 0 through Step 7).
- All rules are tagged [T1], [T2], or [T3] per the Confidence Tier Definitions.
- Rate tables are deterministic lookup tables -- no narrative explanation of rates.
- To update this skill, submit a pull request with the specific section, supporting statutory authority, and effective date of the change.
- All changes require validation by a US CPA or EA before merging.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at the OpenAccountants network. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

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

| Source | URL | Read on |
| --- | --- | --- |
| (state) | https://revenue.wyo.gov | 2026-10-28 |
| Wyoming Statutes Title 39 (sales and use tax article) | https://wyoleg.gov/statutes/compress/title39.pdf | 2026-11-01 |

Not yet confirmed: the 6.00% maximum combined rate and the 4.00% to 6.00% combined-rate range; the filing-frequency dollar thresholds (monthly above $300 average monthly tax, quarterly $100 to $300, annually under $100); the February 1, 2019 economic-nexus effective date; and the worked-example dollar amounts ($2 million drilling equipment, $60,000 tractor, $5 million wind turbines, $400 nightly hotel rate, and the test-suite amounts for the Cheyenne equipment sale, Casper groceries, ranch tractor, remote-seller nexus, Jackson jacket, Jackson lodging, Montana furniture, and vendor-discount examples)

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people.

> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
