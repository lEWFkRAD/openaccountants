---
name: sx-cross-border
description: >
  Sint Maarten cross-border taxation: the official non-resident B-return
  (income tax for taxpayers NOT living on St. Maarten, due within five months,
  no extension), the 65% inclusion rule for rental proceeds of non-resident
  property owners, the special-rate request field, the Kingdom of the
  Netherlands context and absence of a treaty network of Sint Maarten itself,
  and the 1 USD = 1.80 Cg peg for currency math. Applies to Dutch Sint
  Maarten. Treaty applicability to SX must be verified per instrument.
jurisdiction: SX
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Sint Maarten: cross-border and non-residents

## Which return a non-resident files

The GRC issues two individual income-tax returns: the **A-return** "for tax payers living on Sint Maarten" and the **B-return** "for tax payers NOT living on St. Maarten" (official 2025 forms, GRC document library). The B-return for fiscal year 2025 was issued 1 January 2026 and must be returned **within five months** — by **1 June 2026** — and the form states "**No extension will be granted after the return date**." Non-residents must name a person on St. Maarten from whom the Inspectorate can obtain information about the return.

## What the B-return taxes

The B-return's first substantive box is proceeds from immovables not used in a business: **declare 65% of the rental proceeds** (form note), with interest on acquisition debts and compulsory term-life premiums deductible against that box. It also asks whether the taxpayer requests "application of a special rate" for particular income — raise this with the Inspectorate before assuming the progressive schedule applies to a non-resident's Sint Maarten income. Employment income sourced on the island is taxed through wage-tax withholding on the employer's side (see sx-wage-tax-tables); the B-return covers the non-resident's remaining Sint Maarten-sourced income.

## Treaties and the Kingdom context

Sint Maarten is a constituent country of the Kingdom of the Netherlands. Tax treaties are Kingdom instruments and **not all extend to Sint Maarten** — verify each instrument's territorial extension before relying on one (needs-sources: the current extension list was not retrievable from official text on 2026-10-27). There is no separate Sint Maarten treaty network. The France–Sint Maarten relationship (French Saint Martin side) is governed by French domestic and Kingdom rules, not an SX–FR treaty of Sint Maarten's own.

## Currency

The Netherlands Antillean guilder (Cg/NAf) has long been pegged at **1 USD = 1.80 Cg**; the Central Bank of Curaçao and Sint Maarten site (centralbank.org) was unreachable on 2026-10-27, so treat the peg figure as needs-confirmation for filings that depend on it. Official forms and tables are in Cg; convert explicitly and keep the rate used in the file.

## Deadlines

- B-return (non-resident): 1 June for the prior fiscal year; no extension (official form).
- A-return (resident): same 1 June pattern (GRC notice "2025 income tax returns due June 1, 2026").
- Company profit tax: provisional 31 March, final 30 June (see sx-corporate-income-tax).

## Worked examples

**Example 1 — non-resident rental box.** A non-resident lets a Philipsburg condo for Cg 36,000/yr gross; interest on the acquisition mortgage Cg 9,000.

```oa-check
name: B-return immovable proceeds box
inputs:
  rent: 36000
  inclusion: 0.65
  interest: 9000
steps:
  - included: rent * inclusion
  - box_net: included - interest
expected:
  included: 23400
  box_net: 14400
```

**Example 2 — USD income in Cg at the peg.** A US consultant's Sint Maarten fees are USD 50,000.

```oa-check
name: peg conversion USD to Cg
inputs:
  usd: 50000
  peg: 1.80
steps:
  - cg: usd * peg
expected:
  cg: 90000
```

## Ask the client

- Resident or not on 1 January of the tax year? (A-return vs B-return.)
- Where is the property held — personal name, BV, or trust? The B-return box only covers non-business immovable proceeds.
- Which Kingdom treaties extend to Sint Maarten for this client's home country? Verify extension text, not just the treaty title.
- Is the local contact person for the Inspectorate named and reachable?

## Sources

- [2025 Income Tax B-return form, non-residents (PDF, GRC document library)](https://www.tax.sx/documents/individuals) — read 2026-10-27 (five-month/1 June deadline, no-extension note, 65% rental note, special-rate field)
- [GRC notice: 2025 income tax returns due June 1, 2026](https://www.tax.sx/blog/2025-income-tax-returns-due-june-1-2026) — read 2026-10-27
- [GRC notice: income tax return deadline June 1 2026](https://www.tax.sx/blog/income-tax-return-deadline-june-1-2026) — read 2026-10-27
- Treaty extension list for Sint Maarten: **needs-sources** (not retrievable 2026-10-27).

<!-- openaccountants-cta-block -->

**Talk to a verified accountant.** This is a source-cited draft, not reviewed advice. [Book time with an OpenAccountants Partner](https://calendly.com/openaccountants/consultation).
