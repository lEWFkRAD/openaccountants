---
name: nd-transfer-pricing
description: >-
  Use when a corporate group with North Dakota nexus needs the 2026 answer
  on ND connected-party and unitary rules: combined reporting for unitary
  businesses under N.D.C.C. § 57-38.1-19 (Joyce/Finnigan allocation
  questions), the water's-edge election with its 3.5% surtax under
  § 57-38.1-15, the double-weighted-sales three-factor formula with
  single-sales-factor election, and alternative apportionment under
  § 57-38.1-18 — against the graduated 1.41%/3.55%/4.31% corporate
  brackets. Trigger on North Dakota combined return, ND unitary, water's
  edge surtax, 57-38.1-19, 57-38.1-15, Schedule SA, ND addback.
  Source-cited draft; ndlegis.nd.gov unreachable 2026-10-25, statute text
  carried from the existing nd-corporate-tax skill with VERIFY flags.
jurisdiction: US-ND
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.2
---

# North Dakota transfer pricing (combined reporting, water's edge, apportionment)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

C corporations filing North Dakota Form 40 that are members of a controlled or unitary group with intercompany debt, intangibles, management fees, or factoring flows — and any multinational choosing between worldwide and water's-edge unitary reporting. North Dakota is a **combined-reporting state**: a corporation that is part of a unitary business must file a combined Form 40 reflecting the group's combined income with ND apportionment on the combined basis. _(N.D.C.C. § 57-38.1-19 per the existing `nd-corporate-tax` skill §10.6, carried with [VERIFY]; ndlegis.nd.gov DNS failure 2026-10-25 — statute text unverified this run.)_

## 2. Core rules and rates

- **Corporate brackets (graduated):** 1.41% on the first $25,000 of ND taxable income; 3.55% on the next $25,000 (to $50,000); 4.31% above $50,000 — i.e. $352.50 at $25,000, $1,240 at $50,000, then $1,240 + 4.31% × (income − $50,000). _(N.D.C.C. § 57-38-30 per the existing `nd-corporate-tax` skill rate table, carried with [VERIFY]; stable since 2015 per that skill.)_
- **Combined reporting.** Unitary groups file combined Form 40; Joyce/Finnigan allocation questions apply and current ND rule needs confirmation. _(§ 57-38.1-19 [VERIFY])_
- **Water's-edge election + 3.5% surtax.** A corporation electing water's-edge apportionment (excluding certain foreign affiliates from the unitary group) pays an **additional 3.5% of ND taxable income** as a surtax. The election trades worldwide inclusion for a flat surcharge. _(N.D.C.C. § 57-38.1-15 per the existing `nd-corporate-tax` skill §5.2, carried with [VERIFY].)_
- **Apportionment formula.** Three factors (property, payroll, sales) with the **sales factor double-weighted** by default; a **single-sales-factor election** is available to qualifying taxpayers. _(N.D.C.C. § 57-38.1-09 / Schedule SA instructions per the existing `nd-corporate-tax` skill, carried with [VERIFY].)_
- **Alternative apportionment.** A taxpayer (or the Commissioner) may seek an alternative method under § 57-38.1-18 where the statutory formula does not "fairly represent" ND activity — the Commissioner's tool against engineered IP/financing footprints. _(existing `nd-corporate-tax` skill §, carried with [VERIFY].)_
- **No PTET.** ND offers no pass-through entity tax election, so S-corp/partnership owners have no entity-level SALT workaround (existing `nd-corporate-tax` skill).

## 3. Base and adjustments

1. Start from federal taxable income (ND starts from FTI per the existing skill).
2. On a combined basis: eliminate/adjust intercompany transactions per the unitary-combination rules (eliminations mechanics: **needs-sources** — Form 40 booklet not fetched 2026-10-25).
3. Apply the water's-edge election if made; if made, add the 3.5% surtax on top of the normal bracket tax.
4. Apportion on the combined basis: double-weighted sales default, single-sales-factor election if qualified, subject to § 57-38.1-18 modification.
5. ND has no separate corporate franchise tax — the bracket tax is the only entity-level income charge.

## 4. Deadlines

- Form 40 (combined where required): 15th day of the 4th month after year end (Apr 15 calendar filers).
- Estimated payments: quarterly installments per the existing `nd-estimated-tax` skill (corporate estimates on Form 40 ES; confirm current schedule).
- Water's-edge election timing and duration (election window, renewal period): **needs-sources** — § 57-38.1-15 election mechanics not fetched 2026-10-25.

## 5. Penalties and interest

- Underpayment of estimates: interest on the shortfall (ND charges interest on underpaid estimates — tax.nd.gov estimated-tax page verified 2026-10-25; the exact 2026 rate: **needs-sources**).
- Late filing/failure to file: Chapter 57-38 penalties; exact 2026 percentages **needs-sources** (ndlegis DNS failure).
- Intercompany intangible/management-fee stripping is a named multistate audit theme; the Commissioner more often imposes unitary computation against aggressive separate-entity filers (existing skill § on alternative apportionment).

## 6. Cross-border and federal overlay

- Foreign affiliates: the water's-edge election is the principal gate between worldwide and US-only unitary reporting; the 3.5% surtax is its price.
- Federal §267 related-party deferrals and §163(j) interest limits change the federal deduction and therefore the ND starting point.
- Treaty analysis is federal (see federal skills); ND conforms to federal taxable income as its starting line.
- Joyce/Finnigan: whether a non-unitary-but-affiliated member's factors enter the ND fraction is a live ND question — flag for a multistate specialist (existing skill refusal catalogue).

## 7. Worked examples

**Example 1 — standalone bracket tax, $100,000 ND taxable income.** No water's-edge election, fully ND-apportioned.

```oa-check
name: nd corp bracket tax 100k
inputs:
  ti: 100000
steps:
  - b1: 352.50
  - b2: (min(ti, 50000) - 25000) * 0.0355
  - b3: (ti - 50000) * 0.0431
  - tax: b1 + b2 + b3
expected:
  tax: 3395.00
```

**Example 2 — water's-edge elector, $200,000 ND taxable income.** Bracket tax plus the 3.5% water's-edge surtax under § 57-38.1-15.

```oa-check
name: nd waters edge surtax 200k
inputs:
  ti: 200000
steps:
  - base: (ti - 50000) * 0.0431 + 1240
  - sur: ti * 0.035
  - total: base + sur
expected:
  base: 7705.00
  sur: 7000.00
  total: 14705.00
```

(The surtax nearly doubles the bill at this income level — the election's price must be modeled, not assumed.)

## 8. Ask the client first

1. Is the group unitary under ND's definition — common control plus functional/economic integration?
2. Worldwide or water's-edge? Has the election been made, and when does it expire/renew?
3. Are intercompany interest, royalties, and management fees arm's-length and documented?
4. Does the group qualify for the single-sales-factor election, and is double-weighted sales currently being used?
5. Any non-ND states with conflicting combined-reporting regimes that create double inclusion (keep both returns in the file)?

## 9. Sources

- Existing `nd-corporate-tax` skill — bracket table, § 57-38.1-15 water's-edge surtax, § 57-38.1-18 alternative apportionment, § 57-38.1-19 combined reporting (all carried with the skill's own [VERIFY] flags): read 2026-10-25.
- ND Office of State Tax Commissioner — individual/estimated pages (interest on underpaid estimates): <https://www.tax.nd.gov/individual-income-tax> — 200 with text, 2026-10-25.
- N.D.C.C. §§ 57-38-30, 57-38.1-09, 57-38.1-15, 57-38.1-18, 57-38.1-19 statute text: **needs-sources** — ndlegis.nd.gov DNS failure on 2026-10-25 (getaddrinfo); Justia mirror returned 403. Re-verify before publication.
- Form 40 booklet combined-computation mechanics: **needs-sources**.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
