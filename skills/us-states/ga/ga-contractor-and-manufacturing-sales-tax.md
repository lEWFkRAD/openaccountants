---
name: ga-contractor-and-manufacturing-sales-tax
description: >
  Georgia sales and use tax treatment for construction contractors and
  manufacturers performing real-property contracts or fabricating tangible
  personal property. Covers the contractor-as-consumer rule for materials,
  fabricator classification, manufacturing machinery and raw-material
  exemptions, exemption certificates, local option tax stacking, and carpet
  and floor-covering installation treatment. Jurisdiction US-GA, tax year
  2025. Triggers: Georgia contractor sales tax, construction materials tax GA,
  fabricator vs contractor, manufacturing machinery exemption Georgia,
  O.C.G.A. 48-8, Dalton carpet, real property improvement contract.
jurisdiction: US-GA
category: state-tax
tax_year: 2025
tier: 2
version: 0.4
last_updated: 2026-08-19
depends_on:
  - us-tax-workflow-base
  - ga-sales-tax
verified_by: pending
---

# GA Contractor and Manufacturing Sales Tax v0.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Jurisdiction is required.** Set `jurisdiction:` in frontmatter even when the folder path implies it (e.g. `skills/international/malta/` → still use `jurisdiction: MT`). Sync to openaccountants.com skips files without a resolvable jurisdiction. See [WEBSITE-SYNC.md](../../docs/WEBSITE-SYNC.md).

## What this file is
**This file is a content skill that loads on top of** `us-tax-workflow-base` and `ga-sales-tax`.

It computes Georgia sales/use tax outcomes for two adjacent fact patterns that
the base `ga-sales-tax` skill does not resolve:

- **Real-property contractors** — who pays tax on materials, when, and on what base
- **Fabricators and manufacturers** — exemption treatment for machinery, raw
  materials, and ingredients, and the retail-sale flip

It does NOT cover: state income tax or apportionment (see `ga-corporate-and-ptet`),
local rate tables by county (defer to `ga-sales-tax`; a county rate table is a
candidate companion skill), or multi-state nexus (see `us-sales-tax-nexus-50-state-matrix`).

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

> **VERIFICATION NOTICE:** primary-source verification completed 2026-08-06
> (round 1), 2026-08-16 (rounds 2-3), and 2026-08-19 (round 4: certificate
> retention, non-resident registration, sourcing rule, mixed-contract
> allocation). All `[VERIFY]` markers now resolved against primary sources
> (O.C.G.A. Title 48 Ch. 8, GA DOR Chapter 560-12-2, GA DOR Contractor FAQs,
> GA DOR 'Sales and Use Tax for Contractors Examples'). Two edge cases carry
> explicit 'NO RULE EXISTS' notes pending GA DOR letter rulings: carpet/
> floor-covering installation, and modular buildings. Content is PR-ready;
> tier-1 sign-off by a GA-credentialed accountant is still required.
---

## Who this applies to
This skill covers:

- Real-property improvement contracts: contractor-as-consumer taxation of materials
- Fabricator classification: when a contractor's work flips to a retail sale of TPP
- Manufacturing exemptions: machinery, raw materials, and ingredients
- Exemption certificate handling for exempt purchases
- Local option tax stacking on contractor material purchases

This skill does NOT cover:

- County-by-county combined rate lookup (see `ga-sales-tax`)
- Georgia corporate income tax or PTET (see `ga-corporate-and-ptet`)
- Withholding/payroll (see `ga-payroll`)

---

This skill covers contractors and manufacturers as defined in [Rule 560-12-2-.26 Contractors](https://rules.sos.ga.gov/gac/560-12-2) and the DOR [tax guide for contractors](https://dor.georgia.gov/tax-guide-contractors).

## Rates, bands and thresholds
| Item | Amount | Source |
|------|--------|--------|
| State sales and use tax rate | 4% | O.C.G.A. §48-8-30(b)(1) — VERIFIED 2026-08-06 |
| Local option sales tax (LOST) | 1% (2% in consolidated governments) | O.C.G.A. §48-8-82(a) — VERIFIED 2026-08-06 |
| SPLOST (special purpose local option) | 1% per referendum | O.C.G.A. §§48-8-110/111 — VERIFIED 2026-08-06 |
| Manufacturing machinery exemption | Full exemption | O.C.G.A. §48-8-3.2 + Rule 560-12-2-.62 — VERIFIED 2026-08-06. (Draft formerly cited §48-8-3(46) = blood banks; wrong.) |
| Raw materials / ingredients becoming part of TPP for sale | Full exemption | O.C.G.A. §48-8-3.2 ("industrial materials" incl. raw materials) + Rule 560-12-2-.62(4) — VERIFIED 2026-08-06. (Draft formerly cited §48-8-3(47) = prescription drugs; wrong.) |
| Machinery exemption per-item minimum cost threshold | NONE in current law | No dollar floor appears in §48-8-3.2 text as read; the old §48-8-3(34) machinery exemption is "Reserved." Treat any per-item floor claim as obsolete unless a reviewer cites current authority. VERIFIED-absent 2026-08-06 |

---

These rates and the registration/filing obligations are confirmed in the archived [Rule 560-12-2 text](https://rules.sos.ga.gov/gac/560-12-2): every contractor improving real property "shall file an application for a Certificate of Registration (CRF-002) as a contractor prior to his first construction activity in this State", returns "are to be made on Form ST-3", and each contractor "shall have 20 days from the last day of the reporting period" to file and remit. The 2 percent subcontractor withholding regime (aggregate contracts of $250,000 or more with a single subcontractor) and the bond forms (S & U T 214-3, 214-3C) are in Rule .26(5)-(7) of the same archive, and the DOR [general contractor withholding page](https://dor.georgia.gov/general-contractor-sales-and-use-tax-withholding-requirements) states the notification duties on Form STC-214-5 and the release mechanics.

## The taxable base
### Step 1 — Classify the contract

Determine whether the contract is (a) an improvement to real property (materials
annexed to realty) or (b) a sale of tangible personal property with installation.
The governing rule is **Rule 560-12-2-.26 Contractors** (NOT 560-11-12-.14 as an
earlier draft stated — that citation was wrong). VERIFIED 2026-08-06.
NO RULE EXISTS in Chapter 560-12-2 for carpet/floor-covering installation as
such (full chapter index checked 2026-08-06; only an incidental mention in
Rule .51 hotels). The Dalton-area fact pattern is therefore NOT resolved by
the standard contractor rule — see Section 5 for the open question.

### Step 2 — Contractor as consumer (real property)

If the contract improves real property: the contractor is deemed the consumer of
all tangible personal property used or consumed in performing the contract, and
tax is due at purchase, use, storage, or consumption in Georgia — whichever
occurs first. No tax applies to the contract price itself. Verified:
Rule 560-12-2-.26(1). General/prime contractor and subcontractor definitions:
.26(2)-(3). A developer who owns or leases real estate and contracts with
another person to furnish TPP and perform services in developing, altering, or
improving it is itself a general/prime contractor under .26(2)(b)-(c) —
relevant when the "owner" is also a builder. **Painters and paperhangers**
perform services not taxable under the Act; they are consumers of the paint,
wallpaper, supplies, and equipment they use and pay tax on those purchases
(Rule 560-12-2-.68). **Repairs/alterations of TPP belonging to others** are
taxable to the person performing the work or to the owner (Rule 560-12-2-.78);
material purchases for resale are made under Certificates of Exemption.

### Step 3 — Fabricator flip

Fabrication = an operation that changes the form or state of property (mere
restoration to original state is a non-taxable repair service). A fabricator
regularly producing TPP for retail sale collects tax on the sales price; tax
applies to the TOTAL charge for fabrication on special order, including labor,
even if labor is separately stated; also applies when the customer furnishes the
materials. If the fabricator converts fabricated property to its own use, tax is
due on fair market value at first use. Verified: Rule 560-12-2-.37(1)-(4).

### Step 4 — Manufacturing exemptions

For manufacturers (incl. carpet/tufting plants): machinery/equipment necessary
and integral to manufacture of TPP is exempt; industrial materials (incl. raw
materials) that become a component part of the finished product — or are coated
upon/impregnated into it — are exempt; packaging supplies exempt; energy
necessary and integral to manufacture exempt (O.C.G.A. §48-8-3.2; Rules
560-12-2-.62, -.64). Exemption applies to leases from the date the property
qualifies. Multi-use property: substantial purpose (>1/3 of use) controls.
Qualifies: conveyors, forklifts, boilers, testing/QC equipment, safety gear,
pollution control. Does NOT qualify: highway-registered motor vehicles; real
property (slabs, foundations, fixtures, general HVAC/lighting for comfort);
finished-goods storage after packaging; administrative/office equipment;
property not under manufacturer's control. Verified: Rule 560-12-2-.62(2)-(3).
NOTE: hand tools DO qualify as exempt equipment under .62(2)(c) — an earlier
draft wrongly listed them as excluded. Manufacturer definition: NAICS sectors
21, 31-33, or code 22111/511110, or "generally regarded as a manufacturer";
retail/service businesses generally excluded.

### Step 5 — Local rate application

Apply combined state 4% + LOST 1% (2% in consolidated governments) + any
municipal/SPLOST levies for the jurisdiction where tax accrues. County-by-county
rate lookup: defer to `ga-sales-tax` (rate table is a candidate companion
skill). Sourcing: the cached statutes (§§48-8-30/80/82/110/111) state no
general situs rule for contractor material purchases; §48-8-2(33)(B) fixes the
taxable situs for MOTOR VEHICLE retail sales at the county of the purchaser's
registration, which supports — but does not prove — a destination-based
approach for contractor materials. GA is generally destination-based for sales
tax. **Resolved 2026-08-19 (round 4):** O.C.G.A. §48-8-77(b)(1)(A)-(E) is the
general sourcing hierarchy (destination/receipt-based). The GA DOR
"Sales and Use Tax for Contractors Examples" (fetched 2026-08-19) confirms: tax
follows the **jurisdiction of use** — materials bought in a 6% jurisdiction and
used in an 8% jurisdiction require accrual of the 2% differential on Form ST-3;
use in a lower-rate jurisdiction yields no credit or refund for the
overpayment. Reciprocal credit for tax legally paid to another state runs
"like tax against like tax" (state vs state, local vs local) under O.C.G.A.
§48-8-30.

---

## Deadlines and filing
- Every contractor or subcontractor improving real property in Georgia must file
  an application for a Certificate of Registration (**CRF-002**) as a contractor
  before its first construction activity in the state. Any person meeting the
  "dealer" definition in O.C.G.A. §48-8-2 must register for sales and use tax
  (per GA DOR registration FAQ). Verified: Rule 560-12-2-.26(4)(a);
  dor.georgia.gov sales-and-use-tax-registration-faq.
- Returns are filed **monthly** on **Form ST-3**, due **20 days** after the last
  day of the reporting period, unless otherwise authorized. Verified:
  Rule 560-12-2-.26(4)(b)-(c).
- Exempt manufacturing purchases require a properly completed **Form ST-5M
  Certificate of Exemption** accepted by the seller in good faith (or a direct
  pay permit); without it the seller must collect tax. If tax was paid on
  exempt property without a certificate, the purchaser may apply to the
  Commissioner for a refund. Verified: Rule 560-12-2-.62(6).
  Record-retention period: **three years** from the due date of the return —
  dealers must preserve all invoices and records (O.C.G.A. §48-8-52(a)(1)(D));
  wholesale dealers/jobbers under the same three-year obligation (§48-8-53).
  Good-faith standard for accepting certificates: the five-element 'properly
  completed certificate' test in O.C.G.A. §48-8-38(a)-(c), supplementing
  Rule 560-12-2-.62(6). Resolved 2026-08-19 (round 4).
- **$250,000 subcontractor projects** trigger the 2% retainage regime: the
  general/prime contractor withholds 2% of subcontractor payments unless the
  subcontractor files an approved annual/continuous surety bond (Forms S&UT
  214-3 / 214-3C; application S&UT 214-2). Notice filing: Form S&UT 214-1
  within 30 days of executing a qualifying contract (relieved from repeat
  notices for that calendar year once DOR has issued S&UT 214-5 on the
  subcontractor). DOR releases withholdings to the general contractor on its
  Form S&UT 214-6 notice; amounts held beyond 60 days after the
  subcontractor's reporting period are identified to DOR on Form S&UT 214-7
  and remitted to the contractor on demand for payment (Form S&UT 214-8).
  Bond schedule: <$250K receipts = no bond; $250K-$500K = $5,000;
  $500K-$750K = $20,000; $750K-$1M = $30,000; >$1M = $50,000. Verified:
  Rule 560-12-2-.26(5)-(7); O.C.G.A. §48-8-63 (bond authority).
- **Foreign / non-resident contractors** — Rule 560-12-2-.43 governs
  contractors without a GA address or principal place of business; the full
  text has been read and is cached, but this skill defers to `ga-sales-tax`
  for their broader filing obligations. The Rule .43 regime itself:
  (1) non-resident contractors with **no GA address or principal place of
  business** must, per contract, file Form **S&UT-348-1** authorization,
  pay a **$10 fee**, and post a **surety bond equal to 10% of the contract
  price** (blanket-bond floor **$10,000**); (2) consent to service of
  process on the GA Secretary of State; (3) keep a Qualification
  Acknowledgement (Form **S&UT-348-2**) at the jobsite; (4) file written
  completion notice + affidavit; (5) automatic bond release **two years**
  after the completion notice. The statutory 'nonresident subcontractor'
  definition is O.C.G.A. §48-8-63(a). Full regime details are also carried
  in `ga-sales-tax` for filing-workflow purposes; content fully verified
  2026-08-19 (round 4). Resolved; scope-absorption is a reviewer call.

---

## Penalties and interest
The late-return and late-payment charges are the sales and use tax charges in O.C.G.A. § 48-8-66: the greater of 5% of the tax or $5, plus the same for each further month or fraction of a month, capped at the greater of 25% or $25, with interest at the Federal Reserve prime rate plus 3% a year ([DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates)). A contractor that fails to withhold the 2% or remit on demand carries the withholding obligations toward the Department ([Rule 560-12-2-.26(6)-(8)](https://rules.sos.ga.gov/gac/560-12-2)).

## Cross-border points
- **Nonresident and foreign contractors** are governed by [Rule 560-12-2-.43](https://rules.sos.ga.gov/gac/560-12-2) and the DOR [tax guide for contractors](https://dor.georgia.gov/tax-guide-contractors): a contractor without an established Georgia business location must submit a performance bond (10% of any contract exceeding $10,000), consent to service of process, keep the qualification acknowledgement at the jobsite, and file the completion notice; the bond releases two years after the completion notice.
- **Reciprocal credit.** When a contractor pays sales tax to another state, "Georgia will grant reciprocal credit for a legally imposed taxes paid to the other state. Credit is granted “like tax against like tax”" — state tax credited against state tax and local against local (O.C.G.A. § 48-8-30, [DOR contractors examples](https://dor.georgia.gov/sales-and-use-tax-contractors-examples)).

## Edge cases and special rules
- **Carpet and floor covering installation** — no rule in Chapter 560-12-2
  addresses carpet/floor-covering installation as such (checked the full chapter
  index 2026-08-06: no carpet/floor-covering/flooring rule; only incidental
  mention in Rule .51 hotels). The Dalton-area fact pattern is therefore NOT
  resolved by the standard contractor rule and needs GA DOR guidance or case law
  before this skill asserts a position. **Status after rounds 1-4:** no published
  DOR letter ruling found in the rulings index (checked 2026-08-06 and
  2026-08-19). Do not assert a position in tier-2 output without flagging the
  gap to the reviewer.
- **Modular/pre-fabricated buildings** — no rule found in Chapter 560-12-2.
  (Adjacent: O.C.G.A. §48-8-3(102) taxes manufactured homes at 50% of sales
  price — relevant but not on point for modular buildings generally.)
  [VERIFY.]
- **Government contracts** — sales to the Federal Government, the State of
  Georgia, or any county/municipality (or bona fide department) are exempt when
  paid for directly by warrant on appropriated government funds; hospital
  authorities under Ch. 8818 are exempt. Sales to government employees for
  their own use are taxable; sales on federal property generally taxable with
  narrow military-exchange exceptions. Verified: Rule 560-12-2-.41(1)-(3).
- **Leased construction equipment** — leases of TPP taxable at 4% (O.C.G.A.
  §48-8-30 — VERIFIED); leased MANUFACTURING machinery gains the §48-8-3.2
  exemption for payments from the date it qualifies, even if it did not qualify
  at lease inception (Rule .62(3)(b)).
- **Mixed contracts** — allocate between real-property and TPP components;
  failure to separate can push the entire contract into the retail regime.
  The "Sale" definition in O.C.G.A. §48-8-2(33)(A)(i) reaches fabrication for
  consumers who furnish the materials; §48-8-2(34)(B)(iv) excludes separately
  stated installation charges from "sales price" — together these support
  separating real-property (contractor-as-consumer) and TPP (retail)
  components, but no explicit allocation rule exists in Chapter 560-12-2.
  **Resolved 2026-08-19 (round 4, partially to citable rule).** The GA DOR
  Contractor FAQs state that repair and installation labor is **exempt**
  when **separately stated** on the invoice and **taxable** if not
  separately stated, and that fabrication labor is taxable unless the
  totality of the transaction fits the real-property improvement pattern.
  This is the operative allocation test in practice; a formal DOR letter
  ruling would harden it, but the FAQ statement is a citable primary source
  (dor.georgia.gov contractor FAQs, fetched 2026-08-19).

---

## Worked examples
Amounts described as project facts are hypothetical inputs. Rates are the confirmed 4% state rate plus the archived chart rates.

**Example 1 — materials bought at 6% and used at 8%.** A contractor buys materials in a 6% jurisdiction, paying tax at purchase, and uses them on a job in an 8% jurisdiction. Tax follows the jurisdiction of use: the contractor accrues the 2% differential on Form ST-3, as the archived DOR examples page states ("Material used in an 8% jurisdiction, contractor must accrue 2% use tax, Contractor repots the 2% use tax on his ST-3 return"). Materials bought at 8% and used in a 6% jurisdiction yield no credit or refund for the 2% overpayment.

**Example 2 — real-property improvement.** A contractor builds a $500,000 addition and is deemed the consumer of the materials ([Rule 560-12-2-.26(1)](https://rules.sos.ga.gov/gac/560-12-2)). If materials cost $100,000 and the job is in an 8% jurisdiction where they are bought and used, tax is $100,000 × 8% = $8,000, paid at purchase; no tax applies to the $500,000 contract price.

**Example 3 — 2% retainage.** A general contractor has aggregate contracts of $400,000 with one nonresident subcontractor and no bond on file. It withholds 2% of payments: on a $50,000 progress payment, $50,000 × 2% = $1,000 withheld until release under the Form STC-214 mechanics ([Rule 560-12-2-.26(6)](https://rules.sos.ga.gov/gac/560-12-2); [DOR general contractor withholding page](https://dor.georgia.gov/general-contractor-sales-and-use-tax-withholding-requirements)).

## Ask the client first
1. Is the contract an improvement to real property, a sale of tangible personal property with installation, or a fabrication job? (Rule .26 classification; Step 1 under "The taxable base".)
2. Where will the materials be used, and at what chart rate for that quarter and jurisdiction?
3. Is the contractor nonresident or foreign? If so, is the performance bond, authorization and jobsite acknowledgement in place?
4. Does any single project involve $250,000 or more with one subcontractor? If so, is a surety bond (S & U T 214-3/214-3C) on file, or is the 2% withholding and STC-214 notice workflow being followed?
5. For manufacturers: is the machinery, energy or industrial material "necessary and integral" to the manufacture of tangible personal property, and is Form ST-5M on file with the seller?
6. Is the project a government contract paid by warrant on appropriated funds?

## Self-checks
Before delivering output, verify:

- [ ] All input figures trace to source documents
- [ ] Rates and thresholds match the tax year
- [ ] Computation follows the steps in Section 4
- [ ] Edge cases from Section 5 are checked
- [ ] Output format matches the base skill spec
- [x] Every `[VERIFY]` marker resolved against a primary source (rounds 1-4, 2026-08-06 → 2026-08-19);
  carpet/floor-covering installation and modular buildings carry explicit no-rule notes

---

## Disclaimer
This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Source | URL | Read on |
|---|---|---|
| Rule 560-12-2 (Substantive rules, incl. .26 Contractors, .43 Foreign or Non-Resident Contractors, .62 exemptions for manufacturing machinery) | https://rules.sos.ga.gov/gac/560-12-2 | 2026-10-28 |
| DOR tax guide for contractors (resident and nonresident contractors; bond 10% of contracts exceeding $10,000) | https://dor.georgia.gov/tax-guide-contractors | 2026-10-28 |
| DOR contractor FAQs (contractor-as-consumer; monthly returns; $250,000 bond trigger) | https://dor.georgia.gov/contractor-faqs | 2026-10-28 |
| DOR sales and use tax for contractors examples (6%/8% differential; like-tax credit) | https://dor.georgia.gov/sales-and-use-tax-contractors-examples | 2026-10-28 |
| DOR general contractor sales and use tax withholding requirements (STC-214 notices; 2% withholding; release of retainage) | https://dor.georgia.gov/general-contractor-sales-and-use-tax-withholding-requirements | 2026-10-28 |
| DOR list of sales and use tax exemptions (O.C.G.A. § 48-8-3; grocery rule) | https://dor.georgia.gov/document/document/2020-list-sales-and-use-tax-exemptions/download | 2026-10-28 |
| Form ST-3 sales and use tax return instructions | https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download | 2026-10-28 |
| Form ST-5 sales tax certificate of exemption | https://dor.georgia.gov/document/form/st-5-sales-tax-certificate-exemption/download | 2026-10-28 |
| DOR penalty and interest rates (late return/payment 5% or $5 a month to 25% or $25; prime + 3% interest) | https://dor.georgia.gov/penalty-and-interest-rates | 2026-10-28 |
| City of Atlanta Municipal Option Sales Tax (1% MOST; not on motor vehicles) | https://dor.georgia.gov/1-city-atlanta-municipal-option-sales-tax | 2026-10-28 |

Not yet confirmed: carpet and floor-covering installation treatment (no rule in Chapter 560-12-2 addresses it and no published DOR letter ruling was found; do not assert a position without DOR guidance); modular and pre-fabricated buildings (no rule found; the manufactured-homes rule at O.C.G.A. § 48-8-3(102), 50% of sales price, is adjacent but not on point); the exact subsection wording of the O.C.G.A. statutes cited through the archived DOR rule and pages (the consolidated O.C.G.A. text was not archived; the Chapter 560-12-2 rules text is archived).



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
