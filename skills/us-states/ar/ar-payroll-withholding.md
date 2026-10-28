---
name: ar-payroll-withholding
description: >
  Use this skill whenever asked about Arkansas payroll withholding
  for tax year 2026 — the DFA Withholding Tax Branch, Form AR 1000-WE
  (withholding tax return), corporate (Sub-S) withholding, the
  pass-through entity (PET) withholding regime, composite filing for
  non-resident members, and ATAP e-filing. Trigger on "Arkansas
  withholding", "Arkansas AR 1000-WE", "Arkansas Sub-S withholding",
  "Arkansas pass-through entity tax withholding", "Arkansas composite
  filing", "Arkansas ATAP". Source-cited draft; DFA withholding page
  read 2026-10-27; rate tables needs-sources.
jurisdiction: US-AR
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ar-income-tax
---

# Arkansas payroll withholding v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Arkansas withholding is run by the DFA **Withholding Tax Branch**. The branch's own page (fetched 2026-10-27, 200, text read) organizes the regime into: individual withholding (AR 1000-WE family), **Corporate (Sub-S) Withholding**, **Pass-Through Tax Withholding** and **Pass-Through Entity Tax** programs, **Composite Filing** for non-resident members, and e-filing through **ATAP** (Arkansas Taxpayer Access Point). Deposit due dates are published on the branch's "Due Dates" page (linked; content not extracted this run). **Source status:** program names and structure are read from the DFA page; withholding rate tables, deposit thresholds, and penalty percentages are **needs-sources**.

## 2. Who applies

- Employers paying Arkansas-source wages withhold individual income tax (Form AR 1000-WE; employee certificate AR W4EC) — table mechanics **needs-sources**.
- **S corporations** withhold on distributions to members (Corporate (Sub-S) Withholding program — DFA page, read 2026-10-27; rate **needs-sources**).
- Partnerships/LLCs participate in the **Pass-Through Entity Tax (PET)** or withhold on non-electing/non-resident members' distributions (Pass-Through Tax Withholding — DFA page, read 2026-10-27; mechanics **needs-sources**).
- Entities can file a **composite return** covering non-resident members instead of individual returns (Composite Filing — DFA page, read 2026-10-27; eligibility **needs-sources**).

## 3. Mechanics and rates

| Item | Value | Source |
|---|---|---|
| Individual withholding tables | graduated — **needs-sources** | DFA withholding branch |
| Deposit frequency | by liability tier — see branch Due Dates page (**needs-sources**) | DFA page, read 2026-10-27 |
| Sub-S withholding rate | **needs-sources** | DFA page (program listed) |
| PET rate | **needs-sources** | DFA page (program listed) |
| EFT mandate | large filers must pay by EFT ("Who must pay by EFT?" — DFA page, read 2026-10-27; threshold **needs-sources**) | DFA page |

## 4. Deadlines

- **AR 1000-WE returns/deposits:** monthly/semi-weekly by tier (branch Due Dates page — **needs-sources**).
- **Annual reconciliation + W-2/1099:** January 31 (pattern — **needs-sources**).
- **Composite/PET returns:** entity-level deadlines differ from member deadlines — **needs-sources**.

## 5. Penalties and interest

Withholding failures trigger Ark. Code Ann. §26-18-403 penalties (percentages **needs-sources**). Common failure modes: (1) S-corp distributions paid without Sub-S withholding; (2) non-resident members filing nothing because the entity never withheld or filed composite; (3) EFT-mandated payers remitting by check.

## 6. Cross-border interactions

- Non-resident members: choose PET, withholding, or composite filing — see `ar-cross-border`.
- No withholding reciprocity with neighboring states (verify — **needs-sources**).

## 7. Worked examples

An S corporation distributes $200,000 to a non-resident member; at an illustrative 2% Sub-S withholding rate (rate **needs-sources**):

```oa-check
name: AR Sub-S withholding illustrative
inputs:
  distribution: 200000
  rate: 0.02
steps:
  - withheld: distribution * rate
expected:
  withheld: 4000.00
```

Employer deposits 12 monthly AR 1000-WE payments plus one annual reconciliation:

```oa-check
name: AR withholding filing volume
inputs:
  months: 12
  annual: 1
steps:
  - filings: months + annual
expected:
  filings: 13.00
```

## 8. Ask the client

- Are S-corp distributions running through Sub-S withholding (or PET) correctly?
- Non-resident members: which of PET / withholding / composite is being used, consistently?
- Is the employer above the EFT threshold and paying electronically?
- Deposit frequency tier re-checked after headcount growth?

## Sources

1. DFA Withholding Tax Branch: https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/withholding-tax-branch/ (200, text read 2026-10-27 — program structure: Corporate (Sub-S) Withholding, Pass-Through Tax Withholding, PET, Composite Filing, ATAP, EFT question)
2. DFA Corporation Income Tax page (PET links): https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/ (read 2026-10-27)
3. Ark. Code Ann. §26-18-403 et seq.: not retrievable this host — **needs-sources**

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Arkansas withholding and PET questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
