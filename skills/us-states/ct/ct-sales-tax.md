---
name: ct-sales-tax
description: Use this skill whenever asked about Connecticut sales and use tax, luxury tax, DRS filings. Trigger on phrases like "Connecticut sales tax", "CT sales tax", "DRS", "luxury tax Connecticut". ALWAYS load us-sales-tax first.
version: 2.2
jurisdiction: US-CT
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CT Sales Tax

## Who this applies to

Retailers making retail sales of tangible personal property or taxable
services in Connecticut, and remote sellers shipping into the state
(see nexus below). Load `us-sales-tax` first for the general
multistate framework. The rates below are confirmed from Conn. Gen.
Stat. chapter 219 (read 2026-10-28) and the archived 2025 Form
CT-1040 instructions use-tax section.

## Rates, bands and thresholds

| Item | Rate or threshold | Source |
| --- | --- | --- |
| General rate | 6.35% of gross receipts ("six and thirty-five-hundredths per cent") | §12-408(1)(A) |
| Luxury rate | 7.75% on the entire sales price of (i) a motor vehicle exceeding $50,000, (ii) jewelry exceeding $5,000, and (iii) clothing or footwear, a handbag, luggage, umbrella, wallet or watch exceeding $1,000 | §12-408(1)(H); 2025 Form CT-1040 instructions |
| Computer and data processing services | one per cent (statute wording; §12-408(1)(D)(i)) | §12-408(1)(D)(i); 2025 Form CT-1040 instructions ("1% Tax Rate: Computer and Data Processing Services") |
| Remote-seller economic nexus | gross receipts of at least one hundred thousand dollars AND two hundred or more retail sales into Connecticut in the preceding twelve months (AND test) | §12-407(19) |
| Local add-on sales taxes | none -- no local sales taxes in Connecticut | §12-408 (statewide rates only) |
| Sourcing | destination-based | §12-407/§12-411 (use-tax destination rules) |

## The taxable base

**Transaction pattern library** (statutory bases; rates from the
confirmed table above):

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE at the general rate | §12-408(1)(A) |
| Luxury items (see thresholds above) | TAXABLE at 7.75% | §12-408(1)(H) |
| Grocery food | EXEMPT | §12-412 exemptions |
| Meals sold by an eating establishment, caterer or grocery store | TAXABLE -- an additional one per cent on top of the general rate (§12-408(1)(I)) | §12-408(1)(I) |
| Computer/data processing services | TAXABLE at one per cent | §12-408(1)(D)(i) |
| Digital goods / SaaS | TAXABLE when they constitute a taxable sale of a service under §12-407 | §12-407 |
| Professional services | NOT TAXABLE unless the service is a sale under §12-407 | §12-407 |
| Manufacturing equipment | EXEMPT | §12-412 exemptions |
| Prescription drugs | EXEMPT | §12-412 exemptions |
| Resale | EXEMPT | §12-410 resale exemption |
| Clothing | TAXABLE -- the general rate applies year-round; only the one-week August suspension for items under one hundred dollars breaks it (§12-407e) | §12-407e |

## Deadlines and filing

Returns and payment are made to DRS (myconneCT). Filing frequencies
and due dates for a given taxpayer are set by DRS -- see Not yet
confirmed.

## Penalties and interest

Failure to report and remit use tax subjects the taxpayer to a ten per
cent penalty of the total tax due plus interest at one per cent per
month (2025 Form CT-1040 instructions, use-tax section). Additional
statutory penalties apply under chapter 219.

## Cross-border points

- Remote sellers and referrers: nexus requires gross receipts of at
  least one hundred thousand dollars AND two hundred or more retail
  sales into Connecticut -- the AND test, not either/or (§12-407(19)).
- Use tax is the flip side: purchases from out-of-state retailers
  where no CT sales tax was paid must be reported (Form CT-1040
  Schedule 4 for individuals).

## Worked examples

**UNIQUE: luxury rate 7.75% on the specific categories above (vehicles, jewelry, clothing/footwear, handbags, luggage, umbrellas, wallets, watches at their thresholds). AND test for nexus like NY.**

## Prohibitions

- **Prohibition: luxury rate** -- NEVER forget the 7.75% luxury rate on the threshold categories in §12-408(1)(H).
- **Prohibition: nexus threshold** -- NEVER assume nexus with only one threshold -- Connecticut requires BOTH the gross-receipts amount AND the transaction count (§12-407(19)).
- **Prohibition: computer/data processing rate** -- NEVER ignore the one per cent rate on computer and data processing services (§12-408(1)(D)(i)).
- **Prohibition: clothing** -- NEVER assume clothing is exempt outside the one-week August suspension (§12-407e).
- **Prohibition: computation** -- NEVER compute any number.

## Ask the client first

- What is being sold -- general TPP, a luxury category item, meals, or
  computer/data processing services?
- Does the seller cross the nexus thresholds (gross receipts AND
  transaction count)?
- Any purchases from out-of-state retailers without CT tax paid (use
  tax exposure)?
- Is the client's DRS filing frequency and due-date schedule current?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Conn. Gen. Stat. ch. 219 (Sales and Use Taxes) §§12-407, 12-407e, 12-408, 12-410, 12-412 | https://www.cga.ct.gov/current/pub/chap_219.htm | 2026-10-28 |
| 2025 Form CT-1040 instructions, use-tax section (DRS) | https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf | 2026-10-28 |

Not yet confirmed: DRS filing frequencies and return due dates for sales taxpayers; SST membership status (not confirmed from the statute text); the earlier draft's claim that prepared food is taxed at a combined 7.35% figure -- the statute instead imposes the general rate plus an additional one per cent on meals (§12-408(1)(I)), so per-item computation should follow the statutory components; the earlier draft's claim that clothing under $50 is exempt -- the current chapter 219 text taxes clothing year-round except the one-week August suspension for items under one hundred dollars (§12-407e), and the old §12-412b clothing exemption is repealed.

## Talk to a verified accountant

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

Informational only. Review by a qualified Connecticut professional is
required before filing. Verify figures against the cited primary
sources or with a licensed professional before relying on them.
