---
name: ct-s-corporation-tax
description: >
  Use this skill whenever asked about Connecticut taxation of
  partnerships, LLCs and S corporations for tax year 2026 — the
  Pass-Through Entity (PTE) elective tax under Conn. Gen. Stat.
  chapter 228z (§12-699, 6.99%), the resident-portion/modified-source
  tax base, the 87.5% member credit, PTE estimated installments
  (§12-699a), the repealed $250 business entity tax (§12-284b), and
  composite-return history. Trigger on "Connecticut PTE tax",
  "Connecticut pass-through entity tax", "Connecticut S corporation
  tax", "CT-106", "CT-1120S", "Connecticut composite return",
  "Connecticut entity-level tax", "12-699". Source-cited draft; CGA
  chapter 228z text read 2026-10-27.
jurisdiction: US-CT
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ct-corporate-income-tax
---

# Connecticut pass-through entities: PTE tax v0.1

## 1. Scope and sources

Covers Connecticut's entity-level regime for partnerships, LLCs and
S corporations. Primary verified source: Conn. Gen. Stat. chapter
228z full text (cga.ct.gov, read 2026-10-27) plus §12-284b (chapter
213a, same date). All mechanics below are quoted or paraphrased from
those texts. DRS form numbers (CT-106/CT-1120S/CT-PTE) flagged
needs-sources — form PDFs returned HTML to this agent.

## 2. Who applies

- "Affected business entity" = partnership (incl. LLC taxed as
  partnership) or S corporation (incl. LLC taxed as S corp);
  publicly-traded partnerships filing under §12-726 excluded
  (§12-699(a)(3) — verified).
- The PTE tax is **elective**: an affected business entity required
  to file under §12-726 may elect for each taxable year commencing
  on or after January 1, 2024; written notice of election due by the
  return due date (or extended due date), year by year (§12-699(b) —
  verified).
- S corporations are exempt from the corporation business tax
  chapter (§12-214(a)(2)(J) — verified); the PTE tax is the
  entity-level alternative.

## 3. Rates

| Item | Amount | Source |
|---|---|---|
| PTE tax | 6.99% of the tax base | §12-699(c) (verified) |
| Member credit against CT income tax | direct + indirect share of PTE tax × **87.5%** | §12-699(f)(1) (verified) |
| Old business entity tax | $250 every other year — statute text covers taxable years before 1/1/2020; current CT practice: no annual BET | §12-284b (verified text; current practice needs-sources) |

## 4. Base and timing

- **Tax base = resident portion of unsourced income + modified
  Connecticut source income** (§12-699(c) — verified):
  - *Resident portion of unsourced income*: entity income not
    sourced to CT or another taxing state × combined ownership of CT
    resident members (§12-699(a)(7)-(8) — verified).
  - *Modified CT source income*: CT source income × combined
    ownership of members subject to CT income tax (chapter 229),
    with a rebuttable presumption for lower-tier entity members
    (§12-699(a)(9) — verified).
- Lower-tier entity members: subtract distributive share of
  upper-tier CT-source income to avoid double counting (§12-699(d) —
  verified).
- The entity must report each member's direct and indirect share of
  PTE tax (§12-699(e) — verified).
- Credit excess over member liability is refundable without interest
  (§12-699(f)(1) — verified).
- Members also get a credit for their share of similar taxes paid to
  other states, computed consistently with §12-704 (§12-699(f)(2) —
  verified).

## 5. Deadlines

| Filing | Calendar-year due date |
|---|---|
| PTE tax payment | 15th day of the **3rd** month after year close — March 15 for calendar-year entities (§12-699(b) — verified) |
| PTE estimated installments (§12-699a(b)) | Required when the required annual payment ≥ $1,000: 15th day of months 4, 6, 9, and 1 (of the next year); each installment 25% of the required annual payment (annualized-income alternative available) (§12-699a — verified) |
| PTE required annual payment (§12-699a(a)) | Lesser of 90% of current-year PTE tax or 100% of prior-year PTE tax (prior year 12 months, return filed) (§12-699a — verified) |
| Election notice | By the return due date / extended due date, annually (§12-699(b) — verified) |

Note the March 15 payment date differs from the April 15 income-tax
return date — calendar the gap.

## 6. Penalties and interest

- Failure to pay PTE tax within 30 days: §12-35 collection warrant
  and lien provisions apply (§12-699(g) — verified).
- Underpaid PTE estimates: interest on underpayments per §12-699a
  heading; rate in current text not re-audited this run —
  needs-sources.
- Historical $50 BET penalty and 1%/month interest under §12-284b
  (verified text, pre-2020 regime).

## 7. Cross-border interactions

- The PTE base deliberately reaches **unsourced income of CT
  residents** — multistate groups cannot park income in no-tax
  states to escape CT (verified §12-699(a)(7)-(8)).
- Other states' PTE/composite taxes: members get a §12-699(f)(2)
  credit for substantially similar taxes paid to other states
  (verified).
- Nonresident members: Connecticut's old composite election
  (§12-699b) was **repealed effective January 1, 2024** (verified) —
  nonresident members file CT-104PNR directly unless the entity
  elects PTE.
- Federal SALT-cap planning: the entity-level tax is the common
  workaround — coordinate with the federal advisor.

## 8. Worked examples

A calendar-year partnership (all members CT residents) with $1,000,000
of CT-source income elects the PTE tax for 2026:

```oa-check
name: PTE tax on CT-source income
inputs:
  ct_source: 1000000
  ownership_residents: 1.0
  rate: 0.0699
steps:
  - modified_source: ct_source * ownership_residents
  - tax: modified_source * rate
expected:
  modified_source: 1000000.00
  tax: 69900.00
```

The member's credit against CT income tax on that same income:

```oa-check
name: member credit at 87.5 percent
inputs:
  entity_tax: 69900
  credit_pct: 0.875
steps:
  - credit: entity_tax * credit_pct
expected:
  credit: 61162.50
```

## 9. Ask the client

- Has the entity elected PTE for 2026 — and will it re-elect (the
  election is year-by-year)?
- Are March 15 payment and the 4/6/9/1 estimated installments
  calendared separately from the April 15 return?
- What share of members are CT residents vs nonresidents — how much
  unsourced income falls into the base?
- Do members track the 87.5% credit (not 100%) on CT-104/104NR?
- Any lower-tier entity structures needing the §12-699(d)
  subtraction?

## Sources

1. Conn. Gen. Stat. ch. 228z §§12-699, 12-699a, 12-699b (repealed 1/1/2024): https://www.cga.ct.gov/current/pub/chap_228z.htm (200 HTML, read 2026-10-27)
2. Conn. Gen. Stat. §12-284b (affected business entity tax, ch. 213a): https://www.cga.ct.gov/current/pub/chap_213a.htm (200 HTML, read 2026-10-27)
3. Connecticut DRS forms CT-106 / CT-1120S / CT-PTE: https://portal.ct.gov/forms (PDFs returned HTML to this agent 2026-10-27 — form-level cites needs-sources)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Connecticut PTE and pass-through questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
