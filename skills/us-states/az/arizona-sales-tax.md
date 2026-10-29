---
name: arizona-sales-tax
description: Use this skill whenever asked about Arizona sales tax, Arizona Transaction Privilege Tax (TPT), Arizona use tax, Arizona tax nexus, or any request involving Arizona state-level consumption taxes. Trigger on phrases like "Arizona sales tax", "AZ sales tax", "TPT", "Transaction Privilege Tax", "Arizona DOR", or any request involving Arizona TPT compliance. CRITICAL -- Arizona has a Transaction Privilege Tax on the SELLER, not a traditional sales tax. ALWAYS load us-sales-tax first.
jurisdiction: US-AZ
tax_year: 2026
last_updated: 2026-10-28
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Arizona Sales Tax (Transaction Privilege Tax)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Any business selling tangible personal property or performing a taxable business activity in Arizona, including out-of-state remote sellers and marketplace facilitators that meet Arizona's economic-nexus threshold. Arizona's consumption tax is the **Transaction Privilege Tax (TPT)** — "Although commonly referred to as a sales tax, the Arizona transaction privilege tax (TPT) is actually a tax on a vendor for the privilege of doing business in the state" (AZDOR Transaction Privilege Tax page, read 2026-10-28). Various business activities are subject to TPT and must be licensed; a city privilege-tax or use-tax license may also be required (AZDOR TPT page, read 2026-10-28).

**CRITICAL: Arizona TPT is a tax on the privilege of doing business in Arizona, imposed on the SELLER. It is NOT a sales tax on the buyer, though sellers typically pass it through.**

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Arizona, United States |
| Jurisdiction code | US-AZ |
| Tax type | Transaction Privilege Tax (TPT) -- NOT a traditional sales tax; tax is on the SELLER |
| State TPT rate (retail classification) | 5.6% (AZDOR rate tables, read 2026-10-28: "the state's transaction privilege tax rate of 5.6%") |
| Economic nexus | $100,000 in gross proceeds of sales or gross income from direct retail sales into Arizona (2021 and each year thereafter) |
| Primary legislation | A.R.S. Title 42, Chapter 5 |
| Tax authority | Arizona Department of Revenue (ADOR) |
| Filing portal | https://www.aztaxes.gov |
| SST member | No -- Arizona is not a Streamlined Member State (SST Governing Board state detail, read 2026-10-28) |
| Federal framework skill | us-sales-tax |
| Skill version | 2.1 |

### Required inputs

| # | Question | Why it matters |
| --- | --- | --- |
| 1 | Arizona TPT license number? | Required for filing |
| 2 | Filing frequency? | Monthly, quarterly, annual |
| 3 | Nexus type? | $100,000 economic threshold for remote sellers |
| 4 | Business classification? | Different TPT rates by classification |
| 5 | Contractor? | Prime contracting applies a reduced tax base (see The taxable base) |
| 6 | Sell into multiple cities? | City TPT rates vary; confirm the local rate for each jurisdiction |

### Refusal catalogue

- **R-AZ-1** — Prime contracting classification. The reduced prime-contracting tax base and the deduction mechanics are complex; escalate to a verified accountant.  _(R-AZ-1 -- Prime contracting classification)_

## Rates, bands and thresholds

**TPT classifications and state rates**

| Classification | State rate | Source |
| --- | --- | --- |
| Retail | 5.6% | AZDOR Transaction Privilege and Other Tax Rate Tables, effective October 1, 2026 (read 2026-10-28): "the state's transaction privilege tax rate of 5.6%"; imposed by A.R.S. §42-5010 (five per cent) together with the education rate under §42-5010.01 |
| Mining | 3.125% | A.R.S. §42-5010(A)(3) (three and one-eighth per cent of the tax base for the mining classification, read 2026-10-28); AZDOR rate tables |
| Utilities | 5.6% | A.R.S. §42-5010(A)(1)(b) (five per cent, read 2026-10-28) together with the education rate under §42-5010.01; AZDOR rate tables |
| Telecommunications | 5.6% | A.R.S. §42-5010(A)(1)(c) (five per cent, read 2026-10-28) together with the education rate under §42-5010.01; AZDOR rate tables |
| Transient lodging | five and one-half per cent | A.R.S. §42-5010(A)(2) (five and one-half per cent of the tax base for the transient lodging classification, read 2026-10-28) |
| Restaurants/bars | 5.6% | A.R.S. §42-5010(A)(1)(j) (five per cent for the restaurant classification, read 2026-10-28) together with the education rate under §42-5010.01; AZDOR rate tables |
| Contracting (prime) | 5.6% | A.R.S. §42-5010(A)(1)(h) (five per cent for the prime contracting classification, read 2026-10-28) together with the education rate under §42-5010.01; AZDOR rate tables |
| Rental of tangible personal property | 5.6% | A.R.S. §42-5010(A)(1)(k) (five per cent for the personal property rental classification, read 2026-10-28) together with the education rate under §42-5010.01; AZDOR rate tables |
| Commercial lease | zero per cent at the state level | A.R.S. §42-5010(A)(4) (zero per cent of the tax base for the commercial lease classification, read 2026-10-28) |

**Economic nexus (remote sellers and marketplace facilitators)**

| Parameter | Value | Source |
| --- | --- | --- |
| Remote-seller threshold (2021 and each year thereafter) | gross proceeds of sales or gross income from direct (non-marketplace) retail sales into Arizona of more than $100,000 | A.R.S. §42-5044(A)(1)(c) (read 2026-10-28): "For calendar year 2021 and for each calendar year thereafter, $100,000" |
| Marketplace-facilitator threshold | more than $100,000 in gross proceeds of sales or gross income | A.R.S. §42-5044(A)(2) (read 2026-10-28); AZDOR Economic Threshold page (read 2026-10-28): "more than $100,000 in sales" |
| Transaction count | none -- dollar threshold only | AZDOR Out-of-State Sellers page (read 2026-10-28): "Economic nexus means a business' gross proceeds of sales or income derived from sales into Arizona exceeds the required economic thresholds" |
| Effective date | October 1, 2019 | AZDOR Out-of-State Sellers / Economic Threshold pages (read 2026-10-28): "begin filing and paying transaction privilege tax (TPT) in Arizona starting October 1, 2019" |
| Historical remote-seller thresholds | $200,000 (2019); $150,000 (2020) | AZDOR Economic Threshold page (read 2026-10-28) |

**Model City Tax Code**

Arizona cities adopt the Model City Tax Code with local modifications; city rates and exemptions can vary significantly from the state. City and county add-on rates are not on this skill's confirmed table -- pull the current combined rate from the AZDOR Tax Rate Look-Up before relying on any local figure.

## The taxable base

### TPT is on the seller

TPT liability is a privilege tax on the seller for conducting business in Arizona; the buyer is not legally liable for TPT, though most sellers pass the amount through (AZDOR TPT page, read 2026-10-28). The taxable base is generally gross proceeds of sales or gross income from the business, before the deductions and exemptions in the classification statutes.

### Retail classification patterns (A.R.S. §42-5061, read 2026-10-28)

| Pattern | Status | Notes |
| --- | --- | --- |
| General tangible personal property | TAXABLE | retail classification (§42-5061) |
| Grocery food | EXEMPT | §42-5061 exempts "Food, as provided in and subject to the conditions of …" — the food article of this chapter, together with §§42-5074 and 42-6017 (read 2026-10-28) |
| Prescription drugs and medical oxygen | EXEMPT | §42-5061(8): "Drugs and medical oxygen, including delivery hose, mask or tent, regulator and tank, if prescribed by a member of the medical, dental or veterinarian profession who is licensed by law to administer such substances" |
| Insulin, insulin syringes and glucose test strips | EXEMPT | §42-5061 exemption list, read 2026-10-28 |
| Prescription eyeglasses or contact lenses | EXEMPT | §42-5061 exemption list, read 2026-10-28 |
| Hearing aids | EXEMPT | §42-5061 exemption list, read 2026-10-28 |
| Other retail exemptions | read §42-5061 | the statute lists many further exemptions (e.g. items purchased with SNAP benefits); confirm each item against the statutory text before relying on it |

Clothing, prepared food, SaaS/cloud software, digital goods, and the general services patterns (professional services vs job printing) are not on this skill's confirmed table -- see the Not yet confirmed line and read §42-5061 and the AZDOR TPT guidance before advising.

### Prime contracting base

For prime contracting, the taxable base is reduced by statute: "The tax base for the prime contracting classification is sixty-five per cent of the gross proceeds of sales or gross income derived from the business" (A.R.S. §42-5075(B), read 2026-10-28), with the listed items (e.g. the sales price of land) deducted from gross proceeds before computing the base. Do not compute prime-contracting tax without reading §42-5075 in full.

## Deadlines and filing

TPT is filed and paid via AZTaxes.gov. ADOR collects state TPT, county excise taxes and (for most cities) city privilege tax; a separate city license may still be required (AZDOR TPT page, read 2026-10-28). Filing frequencies and specific return due dates are not on this skill's confirmed table -- see the Not yet confirmed line.

## Penalties and interest

Late-filed and late-paid TPT draws ADOR penalties and interest. Specific penalty percentages for TPT are not tied out this run -- see the Not yet confirmed line. Common failure mode: assuming no TPT duty for a single out-of-state marketplace sale when the economic threshold is already met; the threshold tests the current or previous calendar year (A.R.S. §42-5044, read 2026-10-28).

## Cross-border points

- **Out-of-state sellers:** a remote seller or marketplace facilitator with no physical presence must register and pay TPT once its Arizona direct retail sales exceed the dollar threshold in A.R.S. §42-5044 (read 2026-10-28). The AZDOR economic-threshold page (read 2026-10-28) states the remote-seller threshold as "$100,000 (2021 and beyond)" and the marketplace-facilitator threshold as more than $100,000.
- **Marketplace sales:** sales made through a marketplace facilitator are reported and remitted by the facilitator, and are not counted toward the remote seller's own threshold (AZDOR Economic Threshold page, read 2026-10-28).
- **Sourcing:** whether a transaction is sourced origin- or destination-based is not tied out this run -- see the Not yet confirmed line and read the classification statute before advising.

## Worked examples

### Example 1: retail sale, state TPT only (client facts hypothetical)

A business sells a $500 item delivered in Arizona. State retail TPT at 5.6% (city and county add-ons excluded -- the actual combined rate depends on the jurisdiction):

```oa-check
name: retail sale 500 at 5.6 percent state TPT
inputs:
  price: 500
  rate: 0.056
steps:
  - tax: price * rate
expected:
  tax: 28.00
```

### Example 2: grocery food exempt (client facts hypothetical)

$200 of grocery food sold at retail: state TPT is $0 -- food is exempt under A.R.S. §42-5061 (read 2026-10-28). City privilege tax on food may still apply under the Model City Tax Code; confirm the city code before advising.

```oa-check
name: grocery food exempt
inputs:
  price: 200
  rate: 0
steps:
  - tax: price * rate
expected:
  tax: 0.00
```

### R-AZ-1 refusal: prime contracting

A contractor builds a house. The prime-contracting classification applies, and the tax base is reduced by statute ("The tax base for the prime contracting classification is sixty-five per cent of the gross proceeds of sales or gross income derived from the business", A.R.S. §42-5075(B), read 2026-10-28). The base and deduction mechanics are complex -- escalate to a verified accountant; do not compute without reading §42-5075 in full.

## Ask the client first

- Does the client sell tangible personal property or perform a classified business activity in Arizona (including through a marketplace)?
- What are its Arizona direct retail sales for the current and previous calendar year (economic threshold under A.R.S. §42-5044)?
- Which business classification(s) apply? (Rate differs by classification.)
- Which cities does it deliver into? Pull each jurisdiction's combined rate from the AZDOR Tax Rate Look-Up before quoting a price-inclusive rate.
- Is it a contractor? Prime contracting has a reduced statutory base -- escalate (R-AZ-1).

### Prohibitions

- NEVER call Arizona's tax a "sales tax" without noting it is a Transaction Privilege Tax on the SELLER.
- NEVER forget that city TPT rates and exemptions can differ from the state.
- NEVER quote a combined state+local rate without confirming it against the AZDOR rate tables for that jurisdiction and period.
- NEVER treat grocery food as taxable at the state level -- it is exempt under A.R.S. §42-5061 (city treatment may differ).
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the model.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| AZDOR — Transaction Privilege Tax (overview) | https://azdor.gov/business/transaction-privilege-tax | 2026-10-28 |
| AZDOR — Transaction Privilege and Other Tax Rate Tables (effective October 1, 2026) | https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf | 2026-10-28 |
| AZDOR — Out-of-State Sellers | https://azdor.gov/business/transaction-privilege-tax/retail-sales-subject-tpt/out-of-state-sellers | 2026-10-28 |
| AZDOR — Economic Threshold | https://azdor.gov/business/transaction-privilege-tax/retail-sales-subject-tpt/out-state-sellers/economic-threshold | 2026-10-28 |
| A.R.S. §42-5010 — Rates; distribution base | https://www.azleg.gov/ars/42/05010.htm | 2026-10-28 |
| A.R.S. §42-5044 — Nexus; out-of-state businesses; threshold | https://www.azleg.gov/ars/42/05044.htm | 2026-10-28 |
| A.R.S. §42-5061 — Retail classification; exemptions | https://www.azleg.gov/ars/42/05061.htm | 2026-10-28 |
| A.R.S. §42-5075 — Prime contracting classification | https://www.azleg.gov/ars/42/05075.htm | 2026-10-28 |
| Streamlined Sales Tax Governing Board — Arizona state detail | https://www.streamlinedsalestax.org/state-details/arizona | 2026-10-28 |

Not yet confirmed: local city/county TPT add-on rates and the maximum combined rate (the earlier draft's local range and combined-rate ceiling were not tied to a primary source); the combined state+city rate for Phoenix; taxability of clothing, prepared food, canned software, SaaS/cloud software, digital goods, and the general services patterns (professional services, job printing); the manufacturing-machinery exemption scope; resale and interstate-commerce exemption wording (read §42-5061 before relying on it); TPT filing frequencies and return due dates; specific TPT late-filing/late-payment penalty and interest percentages; origin- vs destination-based sourcing per classification.

## Talk to a verified accountant

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
