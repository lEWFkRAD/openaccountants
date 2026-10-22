---
name: bl-tax-residence-and-property-gains
description: >
  Use this skill when determining Saint-Barthélemy fiscal domicile, reviewing a cross-border property disposal, or estimating territorial immovable-property gains tax for 2026 work. It covers the five-year local-residence gateways, 35% and 20% property-gain rates, the principal-residence condition, the EUR 50,000 property-value exemption, and when an accredited fiscal representative may be required. Trigger on Saint-Barthélemy tax residence, five-year rule, non-resident seller, property gain, real-estate sale, principal residence, accredited representative, departure, treaty, or French-State tax coordination. It does not determine French-State tax without separate analysis.
jurisdiction: BL
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-22
version: 0.1
---

# Saint-Barthélemy Tax Residence and Property Gains v0.1

> **General reference only.** This source-cited draft requires a qualified reviewer to reconcile territorial residence, French-State rules, title history, exemptions, and the current filing procedure before a sale or return.

## 1. Who this applies to

The territorial fiscal-domicile definition applies to individuals testing whether their home, principal professional activity, or centre of economic interests has been in Saint-Barthélemy for at least five years at 1 January. The exact statutory limb and continuity evidence must be checked; a certificate request does not create residence by itself.

The immovable-property gains rules apply to covered transfers of Saint-Barthélemy property or rights. Both individuals and entities can fall within the representative-fiscal rules, particularly where they are outside the territory or France.

## 2. Rates, bands and thresholds

| Item | Amount | Tax year | Official source |
|---|---:|---:|---|
| Property gain where disposal occurs before the eighth year of ownership | 35% | 2026 work | [Code des contributions, art. 101](https://actes.eservices-comstbarth.fr/PJ/Deliberation%20CT/Deliberation%20CT_2024/2024_038_ct_annexe.pdf) |
| Property gain after that point | 20% | 2026 work | Same |
| Qualifying principal-residence property gain | 20% where the property was the seller's uninterrupted principal residence for five years at disposal | 2026 work | Same |
| Property-value exemption | Full-ownership value no more than EUR 50,000, subject to article 105 | 2026 work | [Code des contributions, art. 105](https://actes.eservices-comstbarth.fr/PJ/Deliberation%20CT/Deliberation%20CT_2024/2024_038_ct_annexe.pdf) |
| Local fiscal-domicile gateway | At least five years under a statutory residence limb at 1 January | 2026 work | [Code des contributions, art. 2](https://actes.eservices-comstbarth.fr/PJ/Deliberation%20CT/Deliberation%20CT_2024/2024_038_ct_annexe.pdf) |

## 3. The base

Identify the asset or property right transferred, gross disposal consideration, substantiated acquisition basis, and adjustments permitted by the Code. Do not apply a rate to gross sale proceeds unless the governing provision defines that amount as the taxable gain. Classify the holding period and test exemptions independently.

For rights in an entity whose assets include a principal residence, article 101 limits the 20% benefit to the price fraction represented by that residence relative to total assets. Document the valuation ratio; do not apply 20% to all share-sale gain by default.

## 4. Deadlines and filing

The tax must be dealt with through the conveyance and territorial collection procedure applicable on the sale date. The 2024 annex inspected for this draft establishes the rates and representative framework but did not yield a complete, machine-readable operational deadline or current form. Obtain the notary's calculation, the current Collectivité form, and payment evidence before closing.

### Source status caveat

The official 2024 annex resolved and contains the relevant provisions, but its PDF text layer omits portions of some amended passages. No filing deadline or generic penalty figure is supplied here unless legible in the official source. Visual and professional reconciliation is required for publication beyond draft status.

## 5. Penalties and interest

Do not invent a general penalty or interest rate. Confirm the current recovery article, notice, and filing channel with the Collectivité or acting notary. Article 109 bis makes an accredited fiscal representative jointly responsible with the taxpayer for subsequent control in covered cases, so representative appointment is substantive compliance, not a clerical afterthought.

## 6. Cross-border points

- The five-year territorial domicile test must be coordinated with French-State and any other jurisdiction's residence rules.
- Article 109 bis can require a Collectivité-accredited fiscal representative for covered sellers and describes exceptions based on residence, registered office, ownership duration, and other facts.
- An entity with a French or territorial registered office can still require analysis of its associates' residence.
- Preserve residence certificates, arrival dates, employment and home evidence, entity ownership, title history, and valuations.
- A local exemption does not by itself settle tax in France or another residence jurisdiction.

## 7. Worked examples

### Example 1 — Disposal before the eighth year

A covered property disposal produces a properly computed taxable gain of EUR 200,000 before the eighth year of ownership. At 35%, the territorial tax estimate is EUR 70,000 before any exemption or relief.

```oa-check
name: BL property gain before eighth year
inputs:
  taxable_gain: 200000
steps:
  property_gain_tax: taxable_gain * 0.35
expected:
  property_gain_tax: 70000.00
```

### Example 2 — Later disposal and value-exemption check

A later disposal has EUR 120,000 proceeds, EUR 50,000 supported basis and EUR 10,000 permitted costs, producing EUR 60,000 taxable gain. The property value is EUR 120,000, so the EUR 50,000 article 105 value exemption is not available. At 20%, estimated tax is EUR 12,000.

```oa-check
name: BL later property disposal
inputs:
  proceeds: 120000
  acquisition_basis: 50000
  permitted_costs: 10000
steps:
  taxable_gain: proceeds - acquisition_basis - permitted_costs
  property_gain_tax: taxable_gain * 0.20
  value_over_exemption_limit: proceeds - 50000
expected:
  taxable_gain: 60000.00
  property_gain_tax: 12000.00
  value_over_exemption_limit: 70000.00
```

## 8. Ask the client first

- Which fiscal-domicile limb is claimed, and what continuous five-year evidence exists?
- What property or right was sold, and on what acquisition and disposal dates?
- What basis, costs, and valuations are supported by documents?
- Was the property an uninterrupted principal residence for five years?
- Is the seller an entity, and where are its registered office and associates resident?
- Has a notary or the Collectivité required an accredited fiscal representative?

## 9. Sources

- [Code des contributions, amendment/consolidation annex adopted 26 September 2024](https://actes.eservices-comstbarth.fr/PJ/Deliberation%20CT/Deliberation%20CT_2024/2024_038_ct_annexe.pdf), articles 2, 101, 105, and 109 bis — `as_of: 2026-10-22`.
- [Collectivité de Saint-Barthélemy](https://www.comstbarth.fr/) — `as_of: 2026-10-22`.

<!-- openaccountants-cta-block -->
## Talk to a verified accountant

This guide is a source-cited draft. [Book a review with a verified accountant](https://calendly.com/openaccountants) before filing or paying.
