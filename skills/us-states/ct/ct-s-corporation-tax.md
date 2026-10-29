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
  chapter 228z text read 2026-10-28.
jurisdiction: US-CT
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - ct-corporate-income-tax
---

# Connecticut pass-through entities: PTE tax v0.2

Covers Connecticut's entity-level regime for partnerships, LLCs and
S corporations. Primary sources: Conn. Gen. Stat. chapter 228z full
text (cga.ct.gov, archived and read 2026-10-28) plus §12-284b (chapter
213a, archived same date) and the 2025 Form CT-PET instructions
(DRS, archived same date). All mechanics below are quoted or
paraphrased from those texts. DRS form numbers not verified are
listed under Not yet confirmed.

## Who this applies to

- "Affected business entity" = partnership (incl. LLC taxed as
  partnership) or S corporation (incl. LLC taxed as S corp);
  publicly-traded partnerships that agreed to file under §12-726
  reporting each unitholder are excluded (§12-699(a)(3)).
- The PTE tax is **elective**: "For taxable years commencing on or
  after January 1, 2024, an affected business entity that is required
  to file a return under the provisions of section 12-726 may elect
  to pay to the commissioner a tax as determined under this section"
  — written notice of election due not later than the due date (or
  extended due date) of the return, for each taxable year elected
  (§12-699(b)).
- S corporations are exempt from the corporation business tax chapter
  (§12-214(a)(2)(J)); the PTE tax is the entity-level alternative.

## Rates, bands and thresholds

| Item | Amount | Source |
|---|---|---|
| PTE tax | 6.99% of the tax base ("six and ninety-nine-hundredths per cent multiplied by the tax base") | §12-699(c); 2025 Form CT-PET instructions |
| Member credit against CT income tax | direct + indirect share of PTE tax "multiplied by eighty-seven and one-half per cent" — 87.5% | §12-699(f)(1); 2025 Form CT-PET instructions ("87.5% (.875)") |
| Old business entity tax | $250 every other year — §12-284b text covers taxable years before 1/1/2020 | §12-284b (see Not yet confirmed for current practice) |

## The taxable base

- **Tax base = resident portion of unsourced income + modified
  Connecticut source income** (§12-699(c)):
  - *Resident portion of unsourced income*: unsourced income
    multiplied by the combined ownership interests of members who are
    Connecticut residents (§12-699(a)(7)-(8)).
  - *Modified CT source income*: CT source income multiplied by the
    combined ownership of members subject to CT income tax (chapter
    229), with a rebuttable presumption (clear and convincing
    evidence) for lower-tier entity members (§12-699(a)(9)).
- Lower-tier entity members: subtract the distributive share of
  upper-tier CT-source income to avoid double counting (§12-699(d)).
- The entity must report each member's direct and indirect share of
  the PTE tax (§12-699(e)).
- Credit excess over member liability is refunded without interest
  (§12-699(f)(1)).
- Members also get a credit for their share of substantially similar
  taxes paid to another state or DC, "calculated in a manner
  consistent with the provisions of section 12-704" (§12-699(f)(2)).

## Deadlines and filing

| Filing | Due date |
|---|---|
| PTE tax payment | "on or before the fifteenth day of the third month following the close of each taxable year" — mid-March for calendar-year entities (§12-699(b)) |
| PTE estimated installments (§12-699a(b)) | required when the required annual payment is $1,000 or more: the fifteenth day of the fourth, sixth and ninth months of the taxable year and the first month of the next succeeding taxable year; each installment is twenty-five per cent of the required annual payment (annualized-income alternative available) (§12-699a(b)) |
| PTE required annual payment (§12-699a(a)) | lesser of ninety per cent of the current-year PTE tax or one hundred per cent of the prior-year PTE tax (prior year twelve months, return filed) (§12-699a(a)) |
| Election notice | not later than the return due date / extended due date, annually (§12-699(b)) |

Note the mid-March payment date differs from the April income-tax
return date — calendar the gap.

## Penalties and interest

- Failure to pay PTE tax within thirty days of the due date: §12-35
  collection warrant and lien provisions apply (§12-699(g)).
- "If any tax is not paid when due as provided in this section, there
  shall be added to the amount of the tax interest at the rate of one
  per cent per month or fraction thereof from the date the tax became
  due until it is paid" (§12-699(h)); the same one per cent per month
  applies to underpaid PTE estimates (§12-699a(c)).
- Historical fifty-dollar BET penalty under §12-284b (pre-2020
  regime).

## Cross-border points

- The PTE base deliberately reaches **unsourced income of CT
  residents** — multistate groups cannot park income in no-tax states
  to escape CT (§12-699(a)(7)-(8)).
- Other states' PTE/composite taxes: members get a §12-699(f)(2)
  credit for substantially similar taxes paid to another state or DC.
- Nonresident members: Connecticut's old composite election (§12-699b)
  "is repealed, effective January 1, 2024" — nonresident members file
  CT-1040NR/PY directly unless the entity elects PTE.
- Federal SALT-cap planning: the entity-level tax is the common
  workaround — coordinate with the federal advisor.

## Worked examples

Hypothetical facts. A calendar-year partnership (all members CT
residents) with $1,000,000 of CT-source income elects the PTE tax for
2026:

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

## Ask the client first

- Has the entity elected PTE for 2026 — and will it re-elect (the
  election is year-by-year)?
- Are the PTE payment date and the four estimated installment dates
  calendared separately from the return due date?
- What share of members are CT residents vs nonresidents — how much
  unsourced income falls into the base?
- Do members track the 87.5% credit (not 100%) on their CT-1040/1040NR?
- Any lower-tier entity structures needing the §12-699(d)
  subtraction?

## Sources

| Source | URL | Read on |
|---|---|---|
| Conn. Gen. Stat. ch. 228z §§12-699, 12-699a, 12-699b (repealed 1/1/2024) | https://www.cga.ct.gov/current/pub/chap_228z.htm | 2026-10-28 |
| Conn. Gen. Stat. §12-284b (affected business entity tax, ch. 213a) | https://www.cga.ct.gov/current/pub/chap_213a.htm | 2026-10-28 |
| 2025 Form CT-PET instructions (DRS) | https://portal.ct.gov/-/media/drs/forms/2025/pass-through/ct-pet-instructions_1225.pdf | 2026-10-28 |

Not yet confirmed: whether any current annual business entity tax applies after 1/1/2020 (the §12-284b text read covers earlier taxable years; current DRS practice was not confirmed); DRS form numbers and form-level line references for CT-106 / CT-1120S / CT-PTE (DRS form PDFs returned HTML to this agent in a prior run).

## Talk to a verified accountant

**Talk to a verified accountant** — for Connecticut PTE and pass-through questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

This skill is a source-cited draft; no accountant has reviewed it. Verify
figures against the cited primary sources or with a licensed Connecticut
professional before relying on them.
