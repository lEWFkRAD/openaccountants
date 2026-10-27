---
name: sx-corporate-income-tax
description: >
  Sint Maarten profit tax (winstbelasting) reference for companies and other
  legal entities. Covers the provisional (31 March) and final (30 June) return
  cycle on official GRC forms, Receivers Office payment, the two-month appeal
  window, and the third-party information declaration. The statutory rate is
  flagged needs-sources: it is not printed on the official return forms and the
  profit-tax ordinance text was not retrievable on 2026-10-27. Worked examples
  use an explicitly assumed rate. Applies to Dutch Sint Maarten.
jurisdiction: SX
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Sint Maarten: profit tax (winstbelasting)

**Source status — rate needs-sources.** The official GRC profit-tax return forms do not print the rate, and the profit-tax ordinance (Landsverordening winstbelasting) text was not retrievable from an official source on 2026-10-27. Do not quote a Sint Maarten corporate rate to a client from this skill; confirm the rate against the ordinance or a written GRC position before computing. Everything else below is source-cited.

## Who applies

Profit tax applies to entities organised under private law — nameless companies (NV, SA), private companies with limited liability, associations, foundations — and other legally acquired entities carrying on a business, per the entity fields of the official return form (deed of incorporation, DBA name, establishment address). Individuals and partnerships earning business income are taxed under the income-tax ordinance, not profit tax. The Tax Administration Sint Maarten (GRC) administers; payment goes to the Receivers Office.

## Rate

- **needs-sources:** statutory percentage not verified from official text on 2026-10-27. The 2025 final return form (GRC document library) lists "Taxable profit according to summary list" and "Profit tax to be paid" with no rate printed.
- No official two-tier or territorial carve-out was found in retrievable sources; do not assume one.

## Base

Taxable profit is declared from a summary list attached to the return (form field 1: "Taxable profit according to summary list"). The official forms distinguish a **Provisional** return (estimate of the year's liability) from the **Final** return (actual, with credit for amounts declared on provisional returns — form line 3 deducts "Profit Tax as declared on Provisional Tax Return"). Payments to third parties must be separately declared on the GRC "opgAAF werkzaamheden derden" (third-party activities) form; the Inspectorate uses these to cross-check deductions.

## Deadlines (calendar-year entities; official GRC guide + 2026 notices)

- **Provisional profit-tax return and payment: 31 March** for the current year (AB guide; GRC notice "Provisional profit tax due by March 31, 2026").
- **Final return and payment: 30 June** following the year end (2025 final form: "Ultimate date for declaration and payment 30 June 2026").
- A request to file a **lower provisional amount than the previous year** must be submitted on or before **1 March**.
- An **extension** request must be submitted on or before **30 June** (the final-return date); extension is not automatic.
- Non-calendar fiscal years: the same 31 March / 30 June pattern runs from the fiscal year end per the guide; confirm the Inspectorate's position for off-cycle years.

## Penalties and interest

Late or incomplete filing, or payment even one day late, triggers an assessment increased with a penalty (official GRC guide: "even if the filing and or payments was or were done a day later… an assessment will be imposed"). Incorrect or incomplete information to the Inspectorate carries a penalty of up to **NAf 1,000**. A taxpayer disputing an assessment has **two months** from the assessment date to file a written, motivated letter of appeal to the Inspector of Taxes; verbal protest at the counter is not accepted and unmotivated appeals are inadmissible.

## Cross-border

Profit tax follows establishment/deed-registered entities in Sint Maarten. Group financing, management fees and royalties paid to related parties abroad hit the third-party declaration and Inspectorate scrutiny; no statutory transfer-pricing documentation regime was found (see sx-transfer-pricing). Dividend/interest withholding to non-residents: not printed on retrievable official forms — treat as needs-sources.

## Worked examples

**Example 1 — final settlement net of provisional credit.** A company's 2025 provisional return declared and paid Cg 40,000. The 2025 final return shows tax due of Cg 65,000.

```oa-check
name: final profit tax due after provisional credit
inputs:
  final_tax: 65000
  provisional_paid: 40000
steps:
  - balance_due: final_tax - provisional_paid
expected:
  balance_due: 25000
```

**Example 2 — assumed-rate computation (rate NOT verified).** Taxable profit Cg 200,000; assume a 30% rate purely to illustrate the arithmetic — replace with the ordinance rate before use.

```oa-check
name: illustrative profit tax at assumed rate
inputs:
  taxable_profit: 200000
  assumed_rate: 0.30
steps:
  - tax: taxable_profit * assumed_rate
expected:
  tax: 60000
```

## Ask the client

- Deed-registered entity or branch? Fiscal year end? (Drives the 31 March / 30 June cycle.)
- Was a lower-than-prior-year provisional requested by 1 March?
- Copies of all third-party payment declarations — the Inspectorate matches deductions against them.
- Any assessment already imposed for late filing — the two-month appeal clock is running.

## Sources

- [2025 Final Profit Tax return form, GRC document library (PDF)](https://www.tax.sx/documents/businesses) — read 2026-10-27 (deadline "30 June 2026", provisional-credit line, entity fields)
- [GRC 2020 tax-filing guide: deadlines, penalties, appeal window, third-party declarations (PDF)](https://www.tax.sx/documents/businesses) — read 2026-10-27
- [GRC notice: provisional profit tax due by March 31, 2026](https://www.tax.sx/blog/provisional-profit-tax-due-by-march-31-2026) — read 2026-10-27
- [GRC notice: 2025 profit tax return deadline June 30](https://www.tax.sx/blog/2025-profit-tax-return-deadline-june-30) — read 2026-10-27
- [General tax-ordinance (formal tax law), lokaleregelgeving CVDR671742](https://lokaleregelgeving.overheid.nl/CVDR671742) — read 2026-10-22
- Profit-tax ordinance text: **needs-sources** (not retrievable 2026-10-27).

<!-- openaccountants-cta-block -->

**Talk to a verified accountant.** This is a source-cited draft, not reviewed advice. [Book time with an OpenAccountants Partner](https://calendly.com/openaccountants/consultation).
