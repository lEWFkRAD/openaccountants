---
name: oh-corporate-income-tax
description: >
  Use this skill whenever asked about Ohio corporate income tax for tax year
  2026 — Ohio has NO corporate income tax: the 2013 reform replaced the
  corporate franchise and income taxes with the Commercial Activity Tax
  (CAT, ORC Ch. 5751), a gross-receipts tax, plus the financial institutions
  tax (Ch. 4591) for banks and insurers. Covers the CAT as the entity-level
  substitute (0.26% on taxable gross receipts above the $6,000,000 exclusion,
  no annual surcharge since 2024, quarterly 10-Q/annual 10-C filings), the
  pass-through consequence (business income taxed only at owner level,
  optional PTE election), and P.L. 86-272 being unavailable against the CAT.
  Trigger on "Ohio corporate income tax", "Ohio CIT", "Ohio CAT",
  "Commercial Activity Tax", "Ohio franchise tax", "Ohio corporate tax rate",
  "Ohio PTE election", "financial institutions tax Ohio".
  Source-cited draft; ORC 5751.01/5751.02 statute text read 2026-10-27;
  rate and exclusion figures corroborated by the tier-2 oh-cat / oh-cat-tax
  skills verified against the Department CAT page 2026-10-16.
jurisdiction: US-OH
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - oh-cat
  - oh-income-tax
---

# Ohio corporate income tax (there is none — the CAT stands in) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Ohio professional.

## Who this applies to

Ohio repealed its corporate income tax and corporate franchise tax effective for tax years beginning in 2014. There is **no Ohio corporate income tax return and no Ohio corporate income tax rate**. The entity-level tax on business activity is the **commercial activity tax (CAT)**, ORC Chapter 5751 — a gross-receipts tax, not an income tax. Financial institutions pay the **financial institutions tax** (ORC Ch. 4591) instead of the CAT; insurers pay premiums taxes.

**Source status (as_of 2026-10-28):** [ORC 5751.02](https://codes.ohio.gov/ohio-revised-code/section-5751.02) (text effective 2026-06-15, SB 450) and [ORC 5751.01](https://codes.ohio.gov/ohio-revised-code/section-5751.01) fetched HTTP 200 and read (archived). The **$6,000,000 exclusion is now verified from the statute itself** (ORC 5751.01(R)) and the archived CAT 1 registration instructions (Rev. 11/23) confirm the threshold ladder ($150,000 pre-2024; $3M 2024; $6M 2025+; quarterly filing required above $1,000,000 annual TGR). The **0.26% rate and surcharge tiers** remain carried from the tier-2 `oh-cat` skill (Department CAT page read 2026-10-16) — the rate number does not appear in the archived PDFs, so it still needs a 2026 primary-source re-verification.

## 2. Who applies

- **Every "person" doing business in Ohio** with substantial nexus and Ohio taxable gross receipts (TGR) above the exclusion: corporations (C and S), LLCs, partnerships, sole proprietors, trusts, disregarded entities. The CAT reaches the same population a corporate income tax would, plus pass-throughs.
- **Excluded persons** (ORC 5751.01(E)): persons with not more than **$150,000** TGR (unless in a consolidated elected group), public utilities paying the excise tax, nonprofits, government bodies, financial institutions paying the financial institutions tax, insurers paying premiums taxes, dealers in intangibles.
- **Substantial nexus** (ORC 5751.01(H)) — bright-line: Ohio property, Ohio payroll, **$500,000** Ohio TGR, 25% of total property/payroll/receipts in Ohio, or Ohio domicile.
- **P.L. 86-272 does not apply**: ORC 5751.02(A) says the CAT "is not a transactional tax and is not subject to Public Law No. 86-272". A company shielded from Ohio income tax by 86-272 is **not** shielded from the CAT.

## Rates, bands and thresholds

| Item | Amount / rule | Source |
|---|---|---|
| Ohio corporate income tax | **None** — repealed for tax years beginning 2014 | ORC Ch. 5751 replacing Ch. 4503/5745; `oh-cat` |
| CAT rate | **0.26%** of Ohio taxable gross receipts above the exclusion | `oh-cat` (Department CAT page, read 2026-10-16); archived CAT 1 registration instructions (Rev. 11/23) confirm the 2024/2025 threshold ladder and quarterly filing above $1,000,000 — rate itself still needs a 2026 primary-source re-verify |
| CAT exclusion | **$6,000,000** Ohio TGR (2025 and forward; $3,000,000 for 2024) — VERIFIED: archived [ORC 5751.01(R)](https://codes.ohio.gov/ohio-revised-code/section-5751.01): "'Exclusion amount' means three million dollars beginning in 2024 and six million dollars beginning in 2025."; archived CAT 1 instructions: "$3,000,000 for 2024; $6,000,000 for 2025 and thereafter" |
| CAT annual surcharge | **None for 2025 and 2026** — eliminated by HB 33 (2024 onward). Historic 2014–2023 tiers ran $150–$2,600 | `oh-cat` figures table (Department CAT page, read 2026-10-16 / 2026-09-25) |
| Exclusion carry-forward | The full $6,000,000 exclusion applies to the first quarterly return of the year; unused parts carry to later quarters of the **same** calendar year only | CAT 2023-01 via `oh-cat` |
| Base | Gross receipts **sitused to Ohio** under ORC 5751.033 — no cost-of-goods or expense deduction | [ORC 5751.01(G)](https://codes.ohio.gov/ohio-revised-code/section-5751.01), read 2026-10-27 |
| Filing threshold | Open CAT account must keep filing quarterly even at zero tax | `oh-cat` |
| Financial institutions tax | ORC Ch. 4591 — separate tax on covered financial institutions | not yet confirmed (Ch. 4591 not read this run) |
| Pass-through owners | Business income taxed only at owner level under ORC 5747; Ohio offers an elective **pass-through entity (PTE) tax** | not yet confirmed (PTE cite not read this run) |

## The taxable base

Not yet confirmed against archived sources.
## Deadlines and filing

| Filing | Due |
|---|---| (not yet confirmed)
| CAT annual registration / estimate (form 10-CW) | By the last day of the calendar year for the following year | (not yet confirmed)
| CAT quarterly returns (form 10-Q) | Last day of the month after each calendar quarter end (Apr 30, Jul 31, Oct 31, Jan 31) |
| CAT annual return (form 10-C) | April 15 (calendar-year taxpayers) | (not yet confirmed)
| CAT surcharge installments | Historic (2014–2023 years): 15th day of the 4th and 10th months; **no surcharge for 2025–2026** | (not yet confirmed)
| Refund claim | Within **four years** after the date of the erroneous payment | [ORC 5751.08(A)](https://codes.ohio.gov/ohio-revised-code/section-5751.08), read 2026-10-27 |

Quarter dates and installment split are from `oh-cat` (Department page, 2026-10-16) — **not yet confirmed for 2026**.

## Penalties and interest

- Underpayment of estimated CAT: interest accrues on the shortfall; the Department assesses by notice.
- Failure to file / failure to pay: statutory penalties plus interest; the CAT has no P.L. 86-272 shelter, so a non-filer that met bright-line nexus is exposed for up to four open years.
- Refund window is four years (ORC 5751.08(A)) — longer than most state income-tax refund windows.
- Exact 2026 penalty percentages and interest rate: **not yet confirmed** (ORC 5751.09/5703.06 not read this run).

## Cross-border points

- The CAT is imposed on receipts **sitused to Ohio** (ORC 5751.033), not on the taxpayer's worldwide income: goods are sitused by ship-to, services by where the purchaser receives the benefit.
- A foreign or out-of-state corporation with no Ohio office can still owe CAT on Ohio-sitused receipts once a bright-line nexus test is met.
- Once nexus is met at any point in a year, the person remains a CAT taxpayer for the rest of that year **and the whole following calendar year** (`oh-cat`).
- Consolidated / affiliated-group treatment for related members: see `oh-transfer-pricing`.

## Worked examples

**Example A — Ohio operating company, $9.4M Ohio receipts.**

```oa-check
name: CAT on 9,400,000 Ohio TGR (2026)
inputs:
  tgr: 9400000
  exclusion: 6000000
  rate: 0.0026
steps:
  - excess: tgr - exclusion
  - cat: excess * rate
expected:
  excess: 3400000
  cat: 8840.00
```

No annual surcharge applies for 2026 (eliminated from 2024). The exclusion is applied against the first quarterly return of the year and any unused part carries forward within the same calendar year.

**Example B — out-of-state seller, no Ohio office, $4.2M Ohio receipts.**

```oa-check
name: Below exclusion, no CAT
inputs:
  tgr: 4200000
  exclusion: 6000000
steps:
  - excess: max(tgr - exclusion, 0)
  - cat: excess * 0.0026
expected:
  excess: 0
  cat: 0.00
```

Nexus exists ($500,000 Ohio receipts bright-line) but the exclusion applies, so no CAT is due — an open account must still file.

## Ask the client first

- Entity type and whether it is an **excluded person** (bank, insurer, nonprofit, public utility).
- Ohio taxable gross receipts by quarter, and whether the $6,000,000 exclusion is crossed — crossing it late in a year still creates a full-year liability.
- Is a CAT account already open? (Open accounts must file even at zero.)
- Does the client rely on P.L. 86-272? That protection does **not** reach the CAT.
- Related entities and common ownership above 50% — drives consolidated/affiliated-group treatment (`oh-transfer-pricing`).
- Has the client considered the Ohio PTE election for its owners?

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.

| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | — | 2026-10-28 |

- [ORC 5751.02 — commercial activity tax levied](https://codes.ohio.gov/ohio-revised-code/section-5751.02) — read 2026-10-27, text effective 2026-06-15 (SB 450, 136th GA)
- [ORC 5751.01 — CAT definitions, excluded persons, substantial nexus](https://codes.ohio.gov/ohio-revised-code/section-5751.01) — read 2026-10-27
- [ORC 5751.08 — CAT refund application, four-year window](https://codes.ohio.gov/ohio-revised-code/section-5751.08) — read 2026-10-27
- [Ohio Department of Taxation — Commercial Activity Tax](https://tax.ohio.gov/portal/divisions/enterprise_services/commercial_activity_tax_cat) — HTTP 200 2026-10-27, JS-rendered (figures not re-read)
- `oh-cat`, `oh-cat-tax` (tier 2, Department CAT page read 2026-10-16) — rate, exclusion, surcharge tiers, filing calendar
- **not yet confirmed:** 2026 CAT rate/surcharge re-verification (exclusion now verified via ORC 5751.01(R)); ORC 4591 financial institutions tax; Ohio PTE election cite; ORC 5751.09 penalty and 5703.06 interest rates. Note: archived ORC 5751.08(A) gives the CAT refund claim window — **within four years** after the erroneous payment.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Ohio CAT and entity-level questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
## Talk to a verified accountant

Not yet confirmed against archived sources.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | — | 2026-10-28 |


- [ORC 5751.02 — commercial activity tax levied](https://codes.ohio.gov/ohio-revised-code/section-5751.02) — read 2026-10-27, text effective 2026-06-15 (SB 450, 136th GA)
- [ORC 5751.01 — CAT definitions, excluded persons, substantial nexus](https://codes.ohio.gov/ohio-revised-code/section-5751.01) — read 2026-10-27
- [ORC 5751.08 — CAT refund application, four-year window](https://codes.ohio.gov/ohio-revised-code/section-5751.08) — read 2026-10-27
- [Ohio Department of Taxation — Commercial Activity Tax](https://tax.ohio.gov/portal/divisions/enterprise_services/commercial_activity_tax_cat) — HTTP 200 2026-10-27, JS-rendered (figures not re-read)
- `oh-cat`, `oh-cat-tax` (tier 2, Department CAT page read 2026-10-16) — rate, exclusion, surcharge tiers, filing calendar
- **not yet confirmed:** 2026 CAT rate/surcharge re-verification (exclusion now verified via ORC 5751.01(R)); ORC 4591 financial institutions tax; Ohio PTE election cite; ORC 5751.09 penalty and 5703.06 interest rates. Note: archived ORC 5751.08(A) gives the CAT refund claim window — **within four years** after the erroneous payment.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Ohio CAT and entity-level questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

## Talk to a verified accountant


Not yet confirmed against archived sources.
