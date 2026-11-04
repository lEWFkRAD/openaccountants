---
name: tn-sales-tax
description: "Use this skill whenever asked about Tennessee sales tax, Tennessee use tax, Tennessee sales tax nexus, Tennessee sales tax returns, Tennessee exemption certificates, taxability of goods or services in Tennessee, or any request involving Tennessee state-level consumption taxes. Trigger on phrases like \"Tennessee sales tax\", \"TN sales tax\", \"Tennessee use tax\", \"Tennessee nexus\", \"T.C.A. 67-6\", \"Tennessee DOR sales tax\", or any request involving Tennessee sales and use tax filing, classification, or compliance. NOTE: Tennessee has NO state income tax, making sales tax revenue critical. Tennessee has among the HIGHEST combined sales tax rates in the US (7% state + up to 2.75% local). ALWAYS read the parent us-sales-tax skill first for federal context."
jurisdiction: US-TN
version: "1.2"
tax_year: 2026
last_updated: 2026-11-03
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# TN Sales Tax

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Tennessee, United States |
| Jurisdiction Code | US-TN |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 7% (standard); 4% on grocery food |
| Maximum Combined Rate | 9.75% (7% state + 2.75% max local; the August 2026 manual works a 9.75% example) |
| Primary Legal Framework | Tennessee Code Annotated (T.C.A.) Title 67, Chapter 6 |
| Governing Body | Tennessee Department of Revenue (TNDOR) |
| Filing Portal | TNTAP (Tennessee Taxpayer Access Point) -- https://tntap.tn.gov |
| Economic Nexus ($100,000) Effective Date | October 1, 2020 (interim $500,000 threshold applied October 1, 2019 - September 30, 2020) |
| No State Income Tax | Yes -- Tennessee has NO state income tax (Hall income tax repealed for tax periods beginning on or after January 1, 2021) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability. Tier 2: single article cap, SaaS taxability, food rate distinctions. Tier 3: audit defense, penalty abatement, complex bundled transactions. |
| Format | Restructured to Q1 execution format, April 2026 |

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

## Step 0: Client Onboarding Questions

Before proceeding with any Tennessee sales tax analysis, collect the following from the client: [T1]

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

**Client Onboarding Questions**

| # | Question | Why It Matters |
| --- | --- | --- |
| 1 | Do you have a Tennessee sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Tennessee? | Drives taxability classification under Tennessee law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Tennessee? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Tennessee local jurisdictions? | Local tax rates vary; determines compliance complexity. |

## Step 1: Tax Rate Structure

### 1.1 State Rate

- **State sales tax rate** -- 7% (general state sales tax rate for most tangible personal property, taxable services, and other taxable products; one of the highest state-level sales tax rates in the US)  _(TN Sales & Use Tax Manual, Aug 2026; T.C.A. Section 67-6-202)_

### 1.2 Reduced Rate on Grocery Food

- **Reduced rate on grocery food effective July 1, 2017** -- State rate on food and food ingredients reduced from 5% to 4% effective July 1, 2017 under Public Chapter 181, Section 30 of the IMPROVE Act (TNDOR Notice #17-07); the applicable local rate (up to 2.75%) still applies to food  _(T.C.A. Section 67-6-228)_
- **Food and food ingredients definition** -- substances sold for ingestion or chewing by humans and consumed for their taste or nutritional value; excludes alcoholic beverages, tobacco, candy, dietary supplements, and prepared food, all of which stay at the general 7% state rate plus local  _(TNDOR Notice #17-07; T.C.A. Section 67-6-102)_
- **Local food-rate option (metro counties)** -- for tax periods beginning on or after October 1, 2026, a county with a metropolitan form of government may tax food and food ingredients at a lower local rate or exempt food from the local rate; the county rate still applies  _(TN Sales & Use Tax Manual, Aug 2026, Chapter 18)_

### 1.3 Local Rates

**Local Rates**

| Tax Component | Rate Range | Authority |
| --- | --- | --- |
| State tax (general) | 7.0% | T.C.A. Section 67-6-202 |
| State tax (grocery food) | 4.0% | T.C.A. Section 67-6-228 |
| Local option tax (county/city) | 1.50% -- 2.75%, must be a multiple of 0.25 | T.C.A. Section 67-6-702 |
| **Maximum combined (general)** | **9.75%** (7% state + 2.75% local; worked in the Aug 2026 manual) |  |
| **Maximum combined (grocery)** | state 4% + local up to 2.75% |  |

**Tennessee has among the highest combined sales tax rates in the United States.** The Aug 2026 manual works a Rocky Top transaction at 9.75% (7% state, 2.75% local). [T1]

- **City tax rate** -- where a county rate is below 2.75%, a city may adopt a "city tax rate" equal to the difference; e.g., Stewart County is 2.25% and the City of Dover is 2.75%, so Dover's city rate is 0.50%, and Dover may lower or zero its city rate on food while the 2.25% county rate still applies to food  _(TN Sales & Use Tax Manual, Aug 2026, Chapter 18)_

### 1.4 Single Article Cap on Local Tax [T1]

- **Single article cap on local tax** -- in most local jurisdictions the local tax applies only to the first $1,600 of the sales price of any single article of tangible personal property. A single article is one item, exclusive of accessories, capable of being sold as an independent unit; the cap applies per item, not per invoice. The state 7% tax applies to the full price (no cap). The cap does NOT apply to custom (non-prewritten) software, software maintenance contracts, services, amusements, specified digital products, or warranty/service contracts covering TPP -- the entire price of those is subject to local tax.  _(T.C.A. Section 67-6-702(a); TN DOR "Single Article and Special Tax Rates")_
- **State single article tax** -- in addition to the general 7%, a state single article tax of 2.75% applies to the portion of a single article's sales price above $1,600 but not more than $3,200 (caps out at $44 per item); amounts over $3,200 are not subject to it. Unlike local rates, the state single article rate is a standard 2.75%.  _(Tenn. Code Ann. § 67-6-202; TN DOR "Single Article and Special Tax Rates"; TN DOR Single Article Sales Tax webinar)_

**Example:** A $50,000 boat -- state tax: $50,000 x 7% = $3,500 (no cap). Local tax: $1,600 x 2.75% (max) = $44 (local base capped at $1,600). State single article tax: $1,600 x 2.75% = $44. Total: $3,588.

### 1.5 Sourcing Rules [T1]

- **Marketplace facilitator sourcing** -- a marketplace facilitator with no physical location in Tennessee must collect tax based on the shipping address (destination sourcing). A facilitator with a physical location in Tennessee that facilitates sales from that location uses origin sourcing.  _(TN Sales & Use Tax Manual, Aug 2026, Chapter 11)_

## Step 2: Transaction Classification Rules

### 2.1 General Rule

- **General taxability rule** -- Tennessee sales tax applies to the retail sale of tangible personal property and certain enumerated services.  _(T.C.A. Section 67-6-201)_

### 2.2 Taxability Matrix

**Taxability Matrix**

| Item Category | Taxable? | Rate | Authority | Tier |
| --- | --- | --- | --- | --- |
| General tangible personal property and taxable services | Yes | 7% state + local | T.C.A. Section 67-6-202; Manual Ch. 1 | [T1] |
| Food and food ingredients (groceries) | Yes (reduced rate) | **4% state + local** | T.C.A. Section 67-6-228; Manual Ch. 18 | [T1] |
| Prepared food (restaurant meals) | Yes | 7% state + local | Manual Ch. 18 | [T1] |
| Candy, dietary supplements | Yes | 7% state + local | Manual Ch. 18; Notice #17-07 | [T1] |
| Alcoholic beverages, tobacco | Yes | 7% state + local (not "food") | Notice #17-07 | [T1] |
| Motor fuel taxed by the gallon | Exempt from sales tax (excise tax) | N/A | T.C.A. Section 67-6-329; Title 67, Ch. 3, Part 2 | [T1] |
| Gas, electricity, fuel, oil, coal, other energy fuels sold to consumers for residential use | Exempt | 0% | T.C.A. Section 67-6-329 (Manual exemption list) | [T1] |
| Software access services (SaaS) | **Taxable** | 7% state + local | Manual Ch. 13-14 | [T2] |
| Specified digital products (digital audio-visual works, digital audio works, digital books) | Yes | 7% state + local | Manual Ch. 1, 14 | [T1] |
| Cable TV (monthly charge $15.01-$27.50) | Yes | 8.25% state | T.C.A. Section 67-6-226 | [T1] |
| Direct-to-home satellite TV | Yes | 8.25% state | T.C.A. Section 67-6-227 | [T1] |
| Interstate/international telecom sold to business | Yes | 7.5% state | T.C.A. Section 67-6-221 | [T1] |
| Manufactured homes | Yes | 3.5% state (half the general rate) | T.C.A. Section 67-6-216 | [T1] |
| Aviation fuel | Yes | 4.25% state | T.C.A. Section 67-6-217 | [T1] |
| Industrial water / industrial energy fuel for manufacturers | Yes (reduced) | 1.0% / 1.5% state | T.C.A. Section 67-6-206 | [T2] |
| Electricity for a qualified data center | Yes (reduced) | 1.5% state | T.C.A. Section 67-6-206 | [T2] |
| Products containing a hemp-derived cannabinoid | Yes | additional 6% on top of 7% + local (effective July 1, 2023) | Manual Ch. 6 | [T1] |
| Amusement, sports, entertainment admissions | Yes | 7% state + local (sourced to venue) | Manual Ch. 12 | [T1] |

### 2.3 SaaS Taxability -- Tennessee Position [T2]

- **SaaS taxability position** -- Tennessee taxes software access services: the tax applies to any access and use of the software from a location in Tennessee, whether charged per use, per user, per license, subscription, or any other basis. Software is accessed from a location in Tennessee if the customer's residential or primary business address is in the state. If the seller does not collect, Tennessee purchasers who remotely access and use the software must report and pay use tax directly on the purchase price.  _(TN Sales & Use Tax Manual, Aug 2026, Chapters 13-14)_

### 2.4 Services Taxability [T2]

**Services Taxability**

| Service | Taxable? | Authority |
| --- | --- | --- |
| Repair and installation of TPP (labor + parts) | Yes | Manual Ch. 5 |
| Telecommunications (intrastate) | Yes -- 7% state + local | Manual Ch. 15 |
| Interstate/international telecom sold to business | Yes -- 7.5% state | T.C.A. Section 67-6-221 |
| Cable/satellite TV | Yes -- 8.25% state on monthly charges $15.01-$27.50 | T.C.A. Section 67-6-226 |
| Amusement and recreation admissions | Yes -- 7% state + local, sourced to venue | Manual Ch. 12 |
| Waste collection and disposal (commercial) | Yes | Manual Ch. 5 |

## Step 3: Return Form Structure

### 3.1 Registration

- **Registration requirement** -- all sales and use tax returns and associated payments must be submitted electronically through TNTAP. A person engaged in business as a dealer in Tennessee without a registration certificate from the Department is guilty of a Class C misdemeanor. Remote sellers with no business location in Tennessee that register through the Streamlined Central Registration System may file using the Streamlined Simplified Electronic Return (SER).  _(TN DOR "Registration"; TN Sales & Use Tax Manual, Aug 2026)_

### 3.2 Filing Frequency

**Filing Frequency**  _(TN Sales & Use Tax Manual, Aug 2026, "Filing Periods and Due Dates")_

| Situation | Filing Frequency | Due Date |
| --- | --- | --- |
| Meets the filing threshold of $400 gross sales per month or $4,800 gross sales per year | Monthly (law requires monthly filing; this applies to most taxpayers) | 20th of the month following the reporting period |
| Sales and use tax liability averaged $1,000 or less per month for 12 consecutive months | Monthly OR quarterly | Quarterly: 20th of month following quarter-end (January 20, April 20, July 20, October 20) |
| Manufacturers, wholesalers, and marketplace sellers selling only through a collecting marketplace facilitator | Annual (generally) | January 20 |
| Below the $400/month filing threshold | Should pay sales tax to their suppliers in lieu of registering to collect and remit | N/A |

**Note:** TNDOR assigns frequency. Tennessee sales and use tax applies on an accrual basis, not a cash basis. [T1]

### 3.3 Returns and Payment

- **Returns and payment requirements** -- returns are filed through TNTAP (electronic filing required; a penalty not to exceed $500 per instance may be assessed for filing by any other means). Payment is due on the same date as the return. Both state and local taxes are reported on the same return. Taxpayers are not required to create a TNTAP account to file consumer use tax.  _(TN Sales & Use Tax Manual, Aug 2026)_

### 3.4 Vendor Discount (Vendor Compensation)

- **No general vendor discount** -- Tennessee, with very limited exceptions, no longer offers vendor compensation for sales tax collection; the Aug 2026 Sales & Use Tax Manual contains no vendor discount for in-state filers. The historical 2% allowance from 1947 was eliminated.  _(TACIR, "Equitable Vendor Compensation," January 2025)_
- **Limited exception -- out-of-state "volunteer sellers"** -- vendor compensation remains only as an option for out-of-state businesses that are "volunteer sellers": 2% of the first $2,500 of tax, 1.15% above that, capped at $25. After Wayfair, few if any out-of-state businesses qualify.  _(T.C.A. Section 67-6-509; TACIR January 2025)_
- **T.C.A. Section 67-6-508 is "Credits to purchaser," not vendor compensation.** [T1]

### 3.5 Penalties and Interest

**Penalties and Interest**  _(TN Sales & Use Tax Manual, Aug 2026)_

| Violation | Penalty | Authority |
| --- | --- | --- |
| Late filing or late payment (delinquency) | 5% per month (or portion), max 25%, minimum $15 | T.C.A. Section 67-1-804 |
| Negligence | 10% of the underpayment | T.C.A. Section 67-1-804 |
| Fraud | 100% of the underpayment (in lieu of all other DOR penalties except dishonored-check and Tax Enforcement Procedures Act penalties) | T.C.A. Section 67-1-804(c)(2) |
| Failure to file electronically | Up to $500 per instance | T.C.A. Section 67-1-804 |
| Interest | Rate recalculated each July 1 by statutory formula; see table; interest may NOT be waived under any circumstances | T.C.A. Sections 67-1-801(a), 67-1-803(a)(2)(B) |

**Statutory interest rates (TNDOR published table; T.C.A. 67-1-801(a))**

| Fiscal Year | Interest Rate | Installment Payment Agreements |
| --- | --- | --- |
| July 1, 2026 - June 30, 2027 | 10.75% | 13% |
| July 1, 2025 - June 30, 2026 | 11.50% | 13.25% |
| July 1, 2024 - June 30, 2025 | 12.50% | 13.25% |
| July 1, 2023 - June 30, 2024 | 12.25% | 13.25% |
| July 1, 2022 - June 30, 2023 | 8% | 11% |
| July 1, 2021 - June 30, 2022 | 7.25% | 9.25% |

The Commissioner may waive penalties (not fraud penalties) for good and reasonable cause; interest may never be waived.

## Step 4: Deductibility / Exemptions

### 5.1 Exemption and Resale Certificates

- **Resale exemption** -- property purchased for resale may be purchased exempt upon presentation of a resale certificate; a purchaser who uses a resale certificate for property it keeps for use owes the tax and is guilty of a misdemeanor for fraudulent use.  _(TN Sales & Use Tax Manual, Aug 2026)_
- **Use-based exemptions** -- most use-based exemptions require a special exemption certificate (e.g., pollution control, industrial machinery).  _(TN Sales & Use Tax Manual, Aug 2026)_

### 5.2 Requirements [T1]

- **Good-faith acceptance** -- absent fraud or illegal solicitation, a seller who obtains a fully completed exemption certificate is protected.  _(TN Sales & Use Tax Manual, Aug 2026)_

### 6.1 When Use Tax Applies

- **When use tax applies** -- Tennessee use tax applies when sales tax was not collected on items used, stored, or consumed in Tennessee.  _(TN Sales & Use Tax Manual, Aug 2026)_

### 6.2 Use Tax Rate

- **Use tax rate** -- the use tax rate equals the sales tax rate: 7% state + applicable local (4% state on food). The single article local cap and state single article tax apply to use as well.  _(TN Sales & Use Tax Manual, Aug 2026)_
- **Out-of-state credit** -- Tennessee taxpayers get a use tax credit for sales/use tax legally paid to another state, limited to the Tennessee use tax due.  _(TN Sales & Use Tax Manual, Aug 2026)_

### 6.3 Use Tax Reporting

- **Use tax reporting** -- businesses report use tax on the sales and use tax return through TNTAP. Consumers may file the consumer use tax without a TNTAP logon. Remote purchasers of software access services pay use tax directly if the seller did not collect.  _(TN DOR "Registration"; TN Sales & Use Tax Manual, Aug 2026)_

## Step 5: Key Thresholds

### 4.1 Physical Nexus

- **Physical nexus** -- marketplace sellers with a physical presence (storefront, employees, or operations in Tennessee) are required to register.  _(TN Sales & Use Tax Manual, Aug 2026)_

### 4.2 Economic Nexus [T1]

Tennessee's economic nexus sales threshold history  _(T.C.A. Section 67-6-524; TNDOR RS-1)_

| Period | Threshold for Out-of-State Dealers |
| --- | --- |
| October 1, 2019 - September 30, 2020 | $500,000 in sales to Tennessee customers |
| October 1, 2020 and later | $100,000 in sales to Tennessee customers (previous 12 months) |

- The $100,000 threshold includes all retail sales, including exempt sales, but excludes sales for resale.

### 4.3 Marketplace Facilitator Rules [T1]

- **Marketplace facilitator rules effective October 1, 2020** -- facilitators that make or facilitate more than $100,000 in sales to Tennessee customers in the previous 12-month period must collect and remit. Marketplace sellers whose only sales are facilitated by a collecting facilitator are not required to register; facilitated sales do not count toward the seller's own $100,000 threshold.  _(TNDOR "Marketplace Sellers, Marketplace Facilitators & Out-of-State Dealers"; TN Sales & Use Tax Manual, Aug 2026)_

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies, due dates, penalties, and interest. [T1]

## PROHIBITIONS

1. **NEVER** advise that grocery food is exempt in Tennessee (it is taxable at a reduced 4% state rate + local). [T1]
2. **NEVER** advise that SaaS or specified digital products are not taxable in Tennessee (both are taxable). [T1]
3. **NEVER** ignore the single article cap on local tax when calculating tax on items over $1,600. [T1]
4. **NEVER** use a transaction-count threshold for Tennessee economic nexus (revenue only, $100K). [T1]
5. **NEVER** state that Tennessee has a state income tax (Hall income tax repealed for tax periods beginning on or after January 1, 2021). [T1]
6. **NEVER** apply the reduced food rate to prepared food, candy, dietary supplements, alcoholic beverages, or tobacco (those are taxed at the full 7% state rate + local). [T1]
7. **NEVER** forget to apply local taxes in Tennessee -- local rates can add up to 2.75% to the state rate. [T1]
8. **NEVER** cap the state tax at $1,600 -- only the LOCAL tax has the single article base limitation, and the separate 2.75% state single article tax applies to the $1,600-$3,200 band. [T1]
9. **NEVER** advise that Tennessee offers a general vendor discount -- vendor compensation exists only for out-of-state "volunteer sellers" and is capped at $25. [T1]
10. **NEVER** quote a single "current" interest rate without checking the fiscal year -- the rate is recalculated each July 1. [T1]

## Edge Case Registry

### 7.1 Single Article Cap Application [T1]

- **Single article cap application scenarios** -- High-value items: a $100,000 piece of equipment pays 7% state tax ($7,000) on the full price, local tax only on $1,600 (at 2.75% = $44), plus the 2.75% state single article tax on the $1,600-$3,200 band ($44). Total: $7,088. Multiple items: each item is evaluated separately -- 10 items at $500 each take local tax on the full $500 per item. The cap does not apply to services, custom software, amusements, specified digital products, or warranty/service contracts. [T2]

### 7.2 No State Income Tax Impact [T1]

- **No state income tax impact** -- the Hall income tax (interest and dividends) was repealed for tax periods beginning on or after January 1, 2021; do not file a Hall return for any tax year beginning on or after that date. Sales tax is a critical revenue source; businesses relocating to Tennessee for income tax savings must budget for higher sales tax costs. [T2]

### 7.3 Manufacturing Exemptions and Reduced Rates [T2]

- **Manufacturing treatment** -- industrial water is taxed at 1.0% and industrial energy fuel at 1.5% for manufacturers (T.C.A. Section 67-6-206); machinery used directly and primarily in manufacturing is handled through the industrial machinery exemption certificate regime. Escalate the "directly and primarily" judgement. [T2]

### 7.4 Sales Tax Holiday [T1]

- **Sales tax holiday** -- Tennessee holds annual sales tax holidays; school instructional materials (textbooks, workbooks, reference books/maps/globes) are excluded from holiday-qualifying products. Specific holiday items and dollar caps change annually -- verify with TNDOR each year.  _(TN Sales & Use Tax Manual, Aug 2026, Chapter 21)_

### 7.5 Amusement / Admissions Sourcing [T1]

- **Amusement sourcing** -- sales tax on amusement, sports, and entertainment admissions is sourced to the venue location address (e.g., 7% state + 2.25% Nashville or 7% + 2.75% Franklin depending on venue).  _(TN Sales & Use Tax Manual, Aug 2026, Chapter 12)_

### 7.6 CBID Fee [T1]

- **Central Business Improvement District fee** -- effective January 1, 2026 the CBID fee is 0.50% of the sales price of certain taxable TPP and services sold by retailers inside CBID boundaries (0.25% before January 1, 2026).  _(TN Sales & Use Tax Manual, Aug 2026)_

### Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Nashville (2.25% local) sells a $200 pair of shoes. What is the total sales tax?

**Expected Answer:** State: $200 x 7% = $14.00. Local: $200 x 2.25% = $4.50. Total: $18.50.

### Test 2: Grocery Food Rate [T1]

**Question:** A consumer buys $300 in groceries in a jurisdiction with 2.25% local tax. What tax is due?

**Expected Answer:** State: $300 x 4% = $12.00. Local: $300 x 2.25% = $6.75. Total: $18.75.

### Test 3: Single Article Cap [T1]

**Question:** A customer buys a $50,000 boat in a county with 2.75% local tax. What is the total sales tax?

**Expected Answer:** State: $50,000 x 7% = $3,500 (no cap). Local: $1,600 x 2.75% = $44 (capped). State single article: $1,600 x 2.75% = $44. Total: $3,588.

### Test 4: SaaS Taxability [T2]

**Question:** A Tennessee business subscribes to a $500/month SaaS CRM tool. Is Tennessee sales tax due?

**Expected Answer:** Yes. Tennessee taxes access and use of software from a location in Tennessee. At Nashville's rate: $500 x 9.25% = $46.25/month. If the seller did not collect, the purchaser owes use tax.

### Test 5: Economic Nexus [T1]

**Question:** An out-of-state seller made $90,000 in sales and 400 transactions in Tennessee in the previous 12 months. Does the seller have nexus?

**Expected Answer:** No. Tennessee's economic nexus is revenue-only at $100,000. The seller is below the threshold. Transaction count is not relevant.

### Test 6: No Income Tax Context [T1]

**Question:** A company considering relocating from New York to Tennessee asks about the overall tax burden. What should be highlighted about sales tax?

**Expected Answer:** Tennessee has no state income tax, but the 7% state sales tax rate is among the highest in the US, and combined rates reach 9.75%. Businesses must factor in higher sales tax costs on purchases to offset income tax savings.

### Test 7: Vendor Compensation [T1]

**Question:** An out-of-state volunteer seller remits $10,000 of Tennessee sales tax. What vendor compensation may it keep?

**Expected Answer:** 2% of the first $2,500 = $50.00 plus 1.15% of the $7,500 above = $86.25, total $136.25, but compensation is capped at $25. In-state filers get no vendor compensation at all.

## Recomputing examples

```oa-check
name: TN single-article boat 50,000 at max local 2.75
inputs:
  price: 50000
  local: 0.0275
steps:
  - state_tax: price * 0.07
  - local_tax: min(price, 1600) * local
  - state_single_article: min(max(price - 1600, 0), 1600) * 0.0275
  - total: state_tax + local_tax + state_single_article
expected:
  state_tax: 3500.00
  local_tax: 44.00
  state_single_article: 44.00
  total: 3588.00
```

```oa-check
name: TN single article 1,500 (under both caps)
inputs:
  price: 1500
  local: 0.0275
steps:
  - state_tax: price * 0.07
  - local_tax: min(price, 1600) * local
  - state_single_article: min(max(price - 1600, 0), 1600) * 0.0275
  - total: state_tax + local_tax + state_single_article
expected:
  total: 146.25
```

## Reviewer Escalation Protocol

**Reviewer Escalation Protocol**

| Trigger | Action |
| --- | --- |
| Any [T3] tagged item encountered | STOP. Do not guess. Escalate to licensed CPA, EA, or tax attorney. |
| Client has audit notice or assessment | Escalate immediately. Do not advise on audit response. |
| Multi-state nexus question involving 3+ states | Flag for senior reviewer with multi-state experience. |
| Penalty abatement or voluntary disclosure | Escalate to licensed professional with state-specific experience. |
| Ambiguous taxability of a product/service | Present both interpretations to reviewer with supporting authority. |

## Contribution Notes

- This skill follows the Q1 execution format (Step 0 through Step 7).
- All rules are tagged [T1], [T2], or [T3] per the Confidence Tier Definitions.
- Rate tables are deterministic lookup tables -- no narrative explanation of rates.
- To update this skill, submit a pull request with the specific section, supporting statutory authority, and effective date of the change.
- All changes require validation by a US CPA or EA before merging.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at the OpenAccountants network. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

### Sources

Figures in this skill are cited to the archived sources listed in the Sources table below.

- https://www.tn.gov/revenue/taxes/sales---use-tax.html (as_of: 2026-10-28)
- https://www.tn.gov/revenue/taxes/sales---use-tax/rates--thresholds--and-other-information.html (as_of: 2026-10-28)
- https://www.tn.gov/revenue/taxes/sales-and-use-tax/due-dates-and-tax-rates.html (as_of: 2026-10-28)

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
the OpenAccountants network.

- Use it in your AI: 
- Meet the accountants: 

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Who this applies to

Any business with a physical presence in Tennessee, and any out-of-state or
marketplace seller exceeding $100,000 in sales to Tennessee customers in the
previous 12 months (T.C.A. 67-6-524; TNDOR RS-1). Consumers owe use tax when
Tennessee sales tax was not collected, including on remotely accessed software.
Tennessee has no individual income tax: the Hall income tax was repealed for
tax periods beginning on or after January 1, 2021.

## Rates, bands and thresholds

- General state rate: 7% on most tangible personal property and taxable
  services.
- Food and food ingredients: 4% state (reduced from 5% effective July 1, 2017
  by the IMPROVE Act, TNDOR Notice #17-07) plus local.
- Local option: 1.50% to 2.75%, multiples of 0.25; every jurisdiction has one.
- Highest worked combined rate in the Aug 2026 manual: 9.75% (7% + 2.75%).
- Single article: local tax base limited to the first $1,600 in most
  jurisdictions; state single article tax 2.75% on the $1,600-$3,200 band
  (max $44); nothing above $3,200 is subject to it.
- Special state rates: cable TV 8.25% (monthly charge $15.01-$27.50), DTH
  satellite 8.25%, interstate/international telecom to business 7.5%,
  manufactured homes 3.5%, aviation fuel 4.25%, industrial water 1.0%,
  industrial energy fuel 1.5%, qualified data center electricity 1.5%,
  hemp-derived cannabinoid products +6% additional (from July 1, 2023),
  CBID fee 0.50% (from January 1, 2026; 0.25% before).
- Economic nexus: $100,000 (from October 1, 2020; $500,000 for
  October 1, 2019 - September 30, 2020). Marketplace facilitators: more than
  $100,000 facilitated from October 1, 2020.
- Filing threshold: $400 gross sales per month or $4,800 per year.

## The taxable base

Tax is computed on the sales price (use tax on the purchase price); sales and
use share the same rate and basis. For a single article, the local base is
capped at $1,600 in most jurisdictions while the 7% state tax runs on the full
price, and the 2.75% state single article tax covers the $1,600-$3,200 band.
Services, custom software, amusements, specified digital products, and
warranty/service contracts have no local single-article cap. Sales tax applies
on an accrual basis. Facilitated marketplace sales are reported separately by
the facilitator.

## Deadlines and filing

- Monthly returns: due the 20th of the month following the reporting period;
  monthly filing is the statutory default and required at $400 gross sales per
  month / $4,800 per year.
- Taxpayers whose liability averaged $1,000 or less per month for 12
  consecutive months may file monthly or quarterly; quarterly returns are due
  January 20, April 20, July 20, October 20.
- Annual returns: due January 20; generally manufacturers, wholesalers, and
  marketplace sellers selling only through a collecting facilitator.
- Below the filing threshold: pay sales tax to suppliers in lieu of
  registering.
- All returns and payments are electronic through TNTAP; consumer use tax does
  not require a TNTAP logon.

## Penalties and interest

- Delinquency: 5% per month or portion, capped at 25%, minimum $15.
- Negligence: 10% of the underpayment.
- Fraud: 100% of the underpayment (T.C.A. 67-1-804(c)(2)), in lieu of other
  DOR penalties except dishonored-check and Tax Enforcement Procedures Act
  penalties.
- Failure to file electronically: up to $500 per instance.
- Interest: recalculated each July 1 under the T.C.A. 67-1-801(a) formula --
  10.75% for FY July 1, 2026 - June 30, 2027; 11.50% for FY 2025-26; 12.50%
  for FY 2024-25; 12.25% for FY 2023-24; 8% for FY 2022-23; 7.25% for FY
  2021-22. Installment-agreement rates run 13% to 9.25% over the same years.
  Interest may never be waived.
- Vendor compensation: none for in-state filers; out-of-state volunteer
  sellers only, 2% up to $2,500 plus 1.15% above, capped at $25
  (T.C.A. 67-6-509).

## Cross-border points

- Out-of-state dealers: register and collect at $100,000 in Tennessee sales
  (previous 12 months; includes exempt retail sales, excludes resale).
- Marketplace facilitators over $100,000 facilitated (from October 1, 2020)
  collect; sellers selling only through collecting facilitators need not
  register, and facilitated sales do not count toward the seller's threshold.
- Remote sellers may register through the Streamlined Central Registration
  System and file the Streamlined SER (not available to taxpayers with a
  business location in Tennessee).
- Credit: Tennessee use tax is reduced by sales/use tax legally paid to
  another state, up to the Tennessee use tax due.
- Sourcing: facilitators without a Tennessee location use destination
  sourcing (shipping address); facilitators with a Tennessee location use
  origin sourcing.

## Worked examples

### Worked example 1: $50,000 boat at max local rate

State 7% on the full price, local tax capped at a $1,600 base, plus the 2.75%
state single article tax on the $1,600-$3,200 band.

```oa-check
name: boat 50000 max local 2.75
inputs:
  price: 50000
  local: 0.0275
steps:
  - state_tax: price * 0.07
  - local_tax: min(price, 1600) * local
  - state_single_article: min(max(price - 1600, 0), 1600) * 0.0275
  - total: state_tax + local_tax + state_single_article
expected:
  state_tax: 3500.00
  local_tax: 44.00
  state_single_article: 44.00
  total: 3588.00
```

### Worked example 2: $300 of groceries at 2.25% local

```oa-check
name: groceries 300 local 2.25
inputs:
  price: 300
  local: 0.0225
steps:
  - state_tax: price * 0.04
  - local_tax: price * local
  - total: state_tax + local_tax
expected:
  state_tax: 12.00
  local_tax: 6.75
  total: 18.75
```

### Worked example 3: maximum combined grocery rate

State 4% plus the 2.75% local maximum on $300 of food -- the combined rate
works out to 6.75%.

```oa-check
name: groceries 300 max local 2.75
inputs:
  price: 300
  local: 0.0275
steps:
  - state_tax: price * 0.04
  - local_tax: price * local
  - total: state_tax + local_tax
  - combined_rate: total / price
expected:
  state_tax: 12.00
  local_tax: 8.25
  total: 20.25
  combined_rate: 0.0675
```

### Worked example 4: volunteer-seller vendor compensation, capped

An out-of-state volunteer seller remits $10,000 of tax: 2% of the first
$2,500 plus 1.15% of the excess, capped at $25.

```oa-check
name: volunteer seller comp 10000
inputs:
  tax_due: 10000
steps:
  - uncapped: 2500 * 0.02 + (tax_due - 2500) * 0.0115
  - compensation: min(uncapped, 25)
expected:
  uncapped: 136.25
  compensation: 25.00
```

### Worked example 5: delinquency penalty, 3 months late

$2,000 of tax filed and paid 3 months late: 5% per month, capped at 25%,
minimum $15.

```oa-check
name: delinquency 2000 three months
inputs:
  tax_due: 2000
  months: 3
steps:
  - raw_penalty: tax_due * 0.05 * months
  - penalty: min(raw_penalty, tax_due * 0.25)
  - penalty_final: max(penalty, 15)
expected:
  raw_penalty: 300.00
  penalty: 300.00
  penalty_final: 300.00
```

## Ask the client first

- Registration status, assigned filing frequency, and nexus type (physical,
  economic, marketplace).
- Whether all Tennessee sales flow through collecting marketplace
  facilitators (may allow annual filing and no registration).
- Product mix (food vs prepared food vs candy/supplements; software and
  digital products; items over $1,600).
- Whether the client is an out-of-state dealer near $100,000 of Tennessee
  sales in the previous 12 months.
- Whether any sales occur inside a Central Business Improvement District
  (CBID fee 0.50% from January 1, 2026).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| TN Sales & Use Tax Manual (Aug 2026) | https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/august-2026/sales-use-tax-manual.pdf | 2026-11-01 |
| TN DOR sales & use tax main page | https://www.tn.gov/revenue/taxes/sales---use-tax.html | 2026-10-28 |
| TN DOR sales due dates & tax rates | https://www.tn.gov/revenue/taxes/sales-and-use-tax/due-dates-and-tax-rates.html | 2026-10-28 |
| TN DOR local sales tax | https://www.tn.gov/revenue/taxes/sales-and-use-tax/local-sales-tax.html | 2026-11-01 |
| TN DOR single article & special tax rates | https://www.tn.gov/revenue/taxes/sales-and-use-tax/single-article-special-tax-rates.html | 2026-11-01 |
| TN DOR single article sales tax webinar | https://www.tn.gov/content/dam/tn/revenue/documents/taxpayer_education/sales/Tennessee%20Single%20Article%20Sales%20Tax.pdf | 2026-11-01 |
| TN DOR registration | https://www.tn.gov/revenue/taxes/sales-and-use-tax/registration.html | 2026-11-01 |
| TN DOR marketplace & out-of-state dealers | https://www.tn.gov/revenue/taxes/sales-and-use-tax/out-of-state-dealers-marketplace-facilitators.html | 2026-11-01 |
| TNDOR RS-1 sales threshold for out-of-state dealers | https://revenue.support.tn.gov/hc/en-us/articles/360057677332-RS-1-Sales-Threshold-for-Out-of-State-Dealers | 2026-11-01 |
| TNDOR Notice #17-07 (food rate change) | https://www.tn.gov/content/dam/tn/revenue/documents/notices/sales/sales17-07.pdf | 2026-11-01 |
| TN tax rates & interest rate page | https://www.tn.gov/revenue/tax-resources/legal-resources/tax-rates-and-interest-rate.html | 2026-11-01 |
| TN Hall income tax page | https://www.tn.gov/revenue/taxes/hall-income-tax.html | 2026-11-01 |
| TACIR vendor compensation report (Jan 2025) | https://www.tn.gov/content/dam/tn/tacir/commission-meetings/2025january/2025Jan_Tab5VendorComp_Report.pdf | 2026-11-01 |

Not yet confirmed: Streamlined Sales Tax membership status; general origin-
based sourcing for intrastate sales; exemption certificate form numbers
(ST-14, ST-18, F-13) and the 3-year certificate retention rule; prescription
drug and durable medical equipment exemptions; sales tax holiday item dollar
caps ($100 clothing, $100 supplies, $1,500 computers); the July 1, 2015
effective date of the digital products/SaaS legislation; hotel/motel and
parking taxes; clothing and professional-services taxability; registration
statute cite T.C.A. 67-6-601; marketplace facilitator definition cite
T.C.A. 67-6-102(24)(C).

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at the OpenAccountants network.
