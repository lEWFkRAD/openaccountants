---
name: bb-cross-border
description: >
  Barbados cross-border tax reference for 2026. Covers residence and the
  worldwide-versus-source charging basis, outbound withholding (general 15%
  domestic rate; treaty ranges for dividends, interest, royalties and
  management fees), double taxation relief under the Income Tax Act Cap. 73
  Part IV — Commonwealth relief (s.82), treaties having force of law (s.83)
  and the general unilateral credit (s.83A) — the absence of an exit tax,
  land development duty on disposals, and the Pillar Two layer. Trigger on
  Barbados treaty, non-resident, withholding, double taxation relief.
  Source-cited draft.
jurisdiction: BB
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Barbados cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 22 October 2026: Income Tax Act Cap. 73 full
text (L.R.O. 2007 consolidation PDF from the BRA legislation page — Part IV
sections 82, 83, 83A read in full), the BRA Withholding Tax page, and the BRA
legislation index (Land Development Duty Act Cap. 78). Currency BBD, pegged
BBD 2.00 = USD 1.00.

**Source status caveat:** the individual/company residence tests are not
codified in the LRO 2007 text beyond definitions of "non-resident" (not
resident in Barbados) and a premium-income "resident company" definition; the
practical tests carried from `bb-tax-overview` (PwC-cited) need confirmation
against the current consolidation — **needs-sources**. The treaty network list
is not published on the BRA site at a stable path — **needs-sources** for the
current in-force list.

## 2. Charging scope

- **Resident individuals** — worldwide income; resident but non-domiciled
  individuals are taxed on Barbados-source income and foreign income to the
  extent remitted/benefited in Barbados (carried from `bb-tax-overview`,
  PwC-cited, as_of 2026-07-13 — confirm before relying).
- **Resident companies** — worldwide income; **non-resident companies** —
  Barbados-source income only (Income Tax Act charging division).
- Non-residents are **not entitled to personal allowances** (carried from
  `bb-income-tax`).

## 3. Outbound withholding

BRA Withholding Tax page (read 2026-10-22):

- General withholding on income under the Income Tax Act: **15%**.
- Treaty ranges for payments from Barbados by companies: dividends **0–15%**,
  interest **5–15%**, royalties **5–15%**, management fees **0–15%**.
- Non-treaty countries: **15%**.
- Interest on Government of Barbados bonds/debentures/stock beneficially owned
  by a non-resident: **exempt** from withholding.
- Directors: companies must withhold income tax at source from resident
  directors' fees.

## 4. Double taxation relief (Income Tax Act Part IV)

- **s.82 Commonwealth relief.** Where the same income bears Barbados tax and
  income tax of a Commonwealth country that grants reciprocal relief, credit
  is given at a formula rate: resident taxpayer — the Commonwealth rate if it
  does not exceed half the Barbados rate, otherwise half the Barbados rate;
  non-resident — half the Commonwealth rate, or Barbados rate minus half the
  Commonwealth rate. Dual-residence tie-break in s.82(2)(d): deemed not
  resident in Barbados if more time is spent in the other country.
- **s.83 Treaties.** A double-taxation or prevention-of-fiscal-evasion
  agreement "by whatever name known" **has the force of law in Barbados** and
  prevails over the Act to the extent of inconsistency. Ministerial
  regulations may implement agreements.
- **s.83A General relief (from income year 2005).** Unilateral credit: foreign
  tax payable on profits, income or gains derived from sources in that other
  country is allowed as a **credit against Barbados tax** on the same income.
  Where a resident company holds **≥10%** of the capital of the paying
  non-resident company, the credit extends to the underlying tax.

## 5. Exit / departure

No exit or departure tax on individuals or companies ceasing Barbados
residence (no general capital-gains tax; flag: gains on land can attract the
**Land Development Duty Act, Cap. 78** — a duty on the unearned increment on
land disposals, listed on the BRA legislation page; rate mechanics need
confirmation — needs-sources). Short-term resale and trading gains are taxed
as income under the ordinary charging provisions.

## 6. Pillar Two cross-border layer

Corporation Top-Up Tax Act 2024-16: QDMTT 15% minimum effective rate for
in-scope MNE groups (EUR 750m, two of last four fiscal years), fiscal years
beginning on or after 31 Dec 2023; CbCR under Act 2021-27 (USD 850m). See
`bb-transfer-pricing`.

## 7. Worked examples

**Example 1 — treaty vs domestic withholding on a royalty.** A Barbados
company pays a non-resident licensor BBD 100,000. Domestic rate 15% =
15,000; an in-force treaty capping royalties at 5% = 5,000; withholding saved
= 10,000.00.

```oa-check
name: Royalty BBD 100,000 WHT treaty saving
inputs:
  royalty: 100000
steps:
  - domestic: royalty * 0.15
  - treaty: royalty * 0.05
  - saving: domestic - treaty
expected:
  saving: 10000.00
```

**Example 2 — s.83A unilateral credit.** A Barbados-resident company earns
BBD 200,000 of foreign-source income and has paid BBD 30,000 of foreign tax
on it. Barbados corporation tax on the income at 9% = 18,000; the credit is
limited to the Barbados tax on that income, so 18,000 is credited and net
Barbados tax on the foreign income is 0.00 (the excess 12,000 — confirm
carry-forward treatment; the LRO 2007 text read here does not state one).

```oa-check
name: s.83A credit limit BBD
inputs:
  foreign_income: 200000
  foreign_tax: 30000
steps:
  - bb_tax: foreign_income * 0.09
  - credit: min(foreign_tax, bb_tax)
  - net: bb_tax - credit
expected:
  net: 0.00
```

## 8. Ask the client first

1. Residence facts: days spent in Barbados vs abroad (s.82(2)(d) tie-break
  and the general tests), domicile, remittances.
2. Which treaty (if any) is in force with the counterparty country, and does
  it actually reduce the 15% domestic rate?
3. Is the foreign tax creditable under s.83A (source-based) and is an
  underlying credit available (≥10% holding)?
4. Any Barbados land being disposed of — Land Development Duty exposure?

## 9. Sources

- [Income Tax Act, Cap. 73 (full text PDF, L.R.O. 2007) — Part IV ss.82, 83, 83A](https://bra.gov.bb/attachment?file=Attachments%2fIncome+Tax+Act%2c+Cap.+73.pdf&name=Income+Tax+Act%2c+Cap.+73) — read 2026-10-22.
- [BRA — Withholding Tax](https://bra.gov.bb/Popular-Topics/Companies/Withholding-Tax) — read 2026-10-22.
- [BRA — Legislation & Regulations (Land Development Duty Act Cap. 78; Income Tax amendment Acts to 2025-31)](https://bra.gov.bb/About/Legislation-Regulations) — read 2026-10-22.
- [Corporation Top-Up Tax Act, 2024-16](https://bra.gov.bb/About/Legislation-Regulations/Corporation-Top-up-Tax-Act-2024-16) — read 2026-10-22.

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
