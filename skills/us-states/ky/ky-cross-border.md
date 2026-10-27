---
name: ky-cross-border
description: >
  Use this skill whenever asked about Kentucky cross-border taxation
  for tax year 2026 — corporate nexus and the unitary combined
  mandate's reach over out-of-state affiliates, nonresident
  individual taxation of Kentucky-source income, the LLET credit for
  out-of-state LLC members, nonresident withholding, PL 86-272
  protection, and credits for taxes paid to other states. Trigger on
  "Kentucky nexus", "Kentucky nonresident", "Kentucky LLET credit
  out of state", "nonresident withholding Kentucky", "moving to
  Kentucky taxes", "Kentucky credit for taxes paid". Source-cited
  draft; DOR pages read 2026-10-27.
jurisdiction: US-KY
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ky-income-tax
---

# Kentucky cross-border (nexus, non-residents, other-state taxes) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Kentucky's cross-border profile: corporations are reached through the unitary combined mandate (out-of-state unitary members pull into the Kentucky combined computation), individuals pay the flat income tax on Kentucky-source income when nonresident, and the LLET creates a Kentucky tax even for LLCs whose members live elsewhere — with a credit mechanism back to the entity level. **Source status:** the DOR Corporation Income & LLET page and the DOR Nonresident Withholding Tax page were identified/fetched 2026-10-27 (combined-filing rules read from the corporate page; the nonresident-withholding page was located in site navigation but its body text was not extracted this run — flagged **needs-sources**). KRS ch. 140/141 section pages are JS shells — individual-side specifics **needs-sources**.

## 2. Who applies

- **Out-of-state corporations** inside a Kentucky unitary group: combined filing is mandatory from TYB 2019 (DOR page, read 2026-10-27) — membership, not physical presence alone, drives the exposure.
- **Corporations with Kentucky activity** outside a unitary group: separate-entity filing with Kentucky-source apportionment (nexus standard: KRS 141 — **needs-sources**).
- **Nonresident individuals**: taxed on Kentucky-source income (work performed in Kentucky, Kentucky business/rental income) — IL-740 equivalent is the KY 740-NP; mechanics **needs-sources**.
- **Out-of-state LLC members**: the entity pays LLET; members take the entity-level credit on their Kentucky returns (credit lines visible on Form 720 Part II, read 2026-10-27).

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| Corporate rate | flat 5% on combined/apportioned Kentucky income | DOR page, read 2026-10-27 |
| Individual rate | flat income tax (current rate + brackets: **needs-sources**; see `ky-income-tax`) | KRS ch. 140 — JS shell |
| Nonresident base | Kentucky-source income only (KY 740-NP) | mechanics **needs-sources** |
| LLET | gross-receipts tiers, $175 minimum, credited at entity level | Form 720 PDF, read 2026-10-27 |
| Nonresident withholding | employer obligation for nonresident employees (rate/mechanics: **needs-sources**) | DOR Nonresident Withholding page (located 2026-10-27, text not extracted) |
| Credit for taxes paid to other states | available per statute (mechanics **needs-sources**) | KRS 140/141 — JS shells |

## 4. Deadlines

- Form 720 (combined or separate): April 15 calendar-year; estimated 25%×4 (DOR page, read 2026-10-27).
- Federal audit final determination → Kentucky amended return within **180 days** (DOR page, read 2026-10-27).
- Individual KY 740 / 740-NP follow the federal due date (confirm: **needs-sources**).

## 5. Penalties and interest

"Addition to Tax" penalty regime for corporates (KY-TAM-19-02; percentages **needs-sources**); individual penalties under KRS ch. 141 — **needs-sources**. Common failure modes: (1) out-of-state parent assuming no Kentucky exposure while a unitary member operates there — combined filing is mandatory; (2) remote employees working in Kentucky without nonresident withholding; (3) LLC members missing the LLET credit on their own returns; (4) double taxation where the work state and residence state both tax — run the credit analysis both directions.

## 6. Cross-border interactions

- **PL 86-272** (15 U.S.C. §381) protects pure solicitation of tangible-goods orders shipped from outside Kentucky; services, digital, and in-state fulfillment are unprotected.
- **Unitary reach**: the combined group includes domestic corporations "with some exceptions" (DOR page, read 2026-10-27) — map every affiliate before assuming a water's-edge position.
- **Reciprocity**: Kentucky has **no** income-tax reciprocity with neighboring states (Indiana/Illinois/Missouri/Virginia/West Virginia each tax Kentucky work income; confirm current list: **needs-sources**).
- **Foreign parents**: no Kentucky-specific treaty provisions; federal ECI/treaty analysis governs.

## 7. Worked examples

An Indiana resident works 40 of 240 workdays at a Louisville client site, $120,000 wages (illustrative source fraction):

```oa-check
name: IN resident 40 KY workdays
inputs:
  wages: 120000
  ky_days: 40
  total_days: 240
  rate: 0.045
steps:
  - src_frac: ky_days / total_days
  - ky_tax: wages * src_frac * rate
expected:
  src_frac: 0.17
  ky_tax: 900.00
```

A Texas-owned LLC with $900,000 Kentucky gross receipts pays LLET (assumed $2,500 tier — confirm schedule) and members claim the credit:

```oa-check
name: LLET credit at member level
inputs:
  llet: 2500
  members: 2
steps:
  - per_member: llet / members
  - credit_total: per_member * members
expected:
  per_member: 1250.00
  credit_total: 2500.00
```

## 8. Ask the client

- Which affiliates sit inside the Kentucky unitary group — and has anyone checked the statutory exceptions?
- How many workdays do remote/cross-border employees actually spend in Kentucky?
- For LLC members: is the LLET credit being claimed on personal returns?
- Does the residence state credit Kentucky tax, and at what rate?

## Sources

1. DOR Corporation Income & LLET page: https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx (200, text read 2026-10-27)
2. DOR Nonresident Withholding Tax page: https://revenue.ky.gov/Business/Nonresident-Withholding-Tax/Pages/default.aspx (located in site nav 2026-10-27 — body text **needs-sources**)
3. Form 720 PDF (LLET credit lines): https://revenue.ky.gov/Forms/720.pdf (200 PDF, read 2026-10-27)
4. 15 U.S.C. §381 (PL 86-272): https://www.law.cornell.edu/uscode/text/15/381 (200 with text, 2026-10-27)
5. KRS ch. 140/141 (individual tax, credits, nexus): https://apps.legislature.ky.gov/law/krs/141/141.010.asp (JS shells — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kentucky nexus and nonresident questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
