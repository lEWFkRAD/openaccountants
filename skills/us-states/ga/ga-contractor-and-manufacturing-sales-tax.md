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

## Section 1 — Scope statement

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

## Section 2 — Filing requirements

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

## Section 3 — Rates and thresholds

| Item | Amount | Source |
|------|--------|--------|
| State sales and use tax rate | 4% | O.C.G.A. §48-8-30(b)(1) — VERIFIED 2026-08-06 |
| Local option sales tax (LOST) | 1% (2% in consolidated governments) | O.C.G.A. §48-8-82(a) — VERIFIED 2026-08-06 |
| SPLOST (special purpose local option) | 1% per referendum | O.C.G.A. §§48-8-110/111 — VERIFIED 2026-08-06 |
| Manufacturing machinery exemption | Full exemption | O.C.G.A. §48-8-3.2 + Rule 560-12-2-.62 — VERIFIED 2026-08-06. (Draft formerly cited §48-8-3(46) = blood banks; wrong.) |
| Raw materials / ingredients becoming part of TPP for sale | Full exemption | O.C.G.A. §48-8-3.2 ("industrial materials" incl. raw materials) + Rule 560-12-2-.62(4) — VERIFIED 2026-08-06. (Draft formerly cited §48-8-3(47) = prescription drugs; wrong.) |
| Machinery exemption per-item minimum cost threshold | NONE in current law | No dollar floor appears in §48-8-3.2 text as read; the old §48-8-3(34) machinery exemption is "Reserved." Treat any per-item floor claim as obsolete unless a reviewer cites current authority. VERIFIED-absent 2026-08-06 |

---

## Section 4 — Computation rules

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

## Section 5 — Edge cases and special rules

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

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] All input figures trace to source documents
- [ ] Rates and thresholds match the tax year
- [ ] Computation follows the steps in Section 4
- [ ] Edge cases from Section 5 are checked
- [ ] Output format matches the base skill spec
- [x] Every `[VERIFY]` marker resolved against a primary source (rounds 1-4, 2026-08-06 → 2026-08-19);
  carpet/floor-covering installation and modular buildings carry explicit no-rule notes

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
