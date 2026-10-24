---
name: vg-cross-border
description: >
  British Virgin Islands cross-border tax reference for 2026. The
  BVI imposes no income tax, no withholding tax and no exit tax, so
  the cross-border picture is about other countries' charges on BVI
  positions: outbound withholding in the counterparty state, the
  Economic Substance Act, CRS/FATCA information exchange, UK/US
  anti-avoidance look-through, and Pillar Two top-up exposure.
  Covers payroll tax and social charges for staff seconded to the
  BVI. Trigger on BVI cross-border, non-resident, offshore holding,
  withholding, economic substance, CRS, expatriate. Source-cited
  draft.
jurisdiction: VG
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# British Virgin Islands cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the GOV.VG home,
financial-and-tax-information and Inland Revenue Department pages;
Virgin Islands Laws Online (laws.gov.vg); the Social Security Board
contributions page (vissb.vg); the 2026 Budget Address; and the
existing VG pack skills (figures carried forward with their
citations). Currency: US dollar (USD).

**Source status caveat:** the Income Tax Act, Payroll Taxes Act and
Economic Substance Act consolidated texts were not locatable on
laws.gov.vg this pass; vinhi.vg returned 403 to automated reads; the
CRS news link on GOV.VG 404'd. Statute-level citations and the BVI
treaty/CDI position are **needs-sources**. The BVI is a British
Overseas Territory; double-tax treaties generally do not extend to
it unless expressly listed — confirm per instrument.

## 2. Who the rules apply to

- **Non-resident shareholders, lenders and licensors.** No BVI
  withholding on dividends, interest, royalties or service fees paid
  abroad (rate nil — Income Tax Act, sections needs-sources). The
  counterparty's country may impose its own WHT on the same flow.
- **BVI companies with foreign activity.** No CFC, no exit tax, no
  repatriation rule in the BVI itself; the foreign country's CFC /
  substance rules decide whether the BVI entity shelters anything.
- **Individuals.** No BVI personal income tax for residents or
  non-residents; home-country residence rules do all the taxing.
  Anyone employed in and physically present in the BVI pays Payroll
  Tax (employer side) plus Social Security and NHI (both sides).
- **Departure.** No BVI exit charge — **needs-sources** for any
  successor regime.

## 3. Rates and reliefs table

| Item | Content | Source |
|---|---|---|
| WHT — dividends / interest / royalties out of the BVI | 0% | Income Tax Act (rate nil) — vg-corporate-income-tax |
| Personal income tax | None | vg-tax-overview |
| Corporate income tax | None (fixed annual fees instead) | BVI Business Companies Act — vg-corporate-income-tax |
| Exit tax | None confirmed | needs-sources |
| Payroll Tax | 10% Class 1 / 14% Class 2 of remuneration; first US$10,000 per employee exempt | Payroll Taxes Act 2004 — vg-payroll-social |
| Social Security | 8.5% total (employee 4% / employer 4.5% private sector); maximum insurable earnings US$53,400, rising to US$55,536 from 1 Jan 2027 | Social Security Board (vissb.vg, read 2026-10-24) |
| National Health Insurance | 7.5% total (employee 3.75% / employer 3.75%) — carried from vg-payroll-social; vinhi.vg 403 this pass | needs-sources |
| Pillar Two 15% | GloBE top-up risk for in-scope groups; BVI implementation not announced in the 2026 Budget Address | needs-sources |
| Information exchange | CRS and FATCA reporting by in-scope financial institutions; AEOI | GOV.VG (CRS link 404 this pass — needs-sources) |

## 4. Tax base and computation

The BVI taxes **activity inside the territory**, not income: payroll
tax on remuneration of employees who work wholly or partly in the
BVI (Class 1 where the employee's main place of work is outside the
BVI — 10%; Class 2 where it is in the BVI — 14%), social insurance on
insurable earnings up to the statutory maximum, and NHI on the
statutory band. Everything else cross-border is computed in the
counterparty's law: its WHT on payments to the BVI entity, its
substance/CFC tests on the BVI entity's profits, and (for in-scope
groups) the GloBE top-up on the BVI entity's low-taxed income.

## 5. Deadlines

- **Payroll Tax return and payment:** monthly, by the 21st of the
  following month ((approx — confirm) — vg-payroll-social).
- **Social Security contributions:** monthly remittance to the SSB
  (exact day: needs-sources).
- **Annual financial return:** within 9 months after financial year
  end (BVI Business Companies (Financial Return) Order, 2023 —
  laws.gov.vg read 2026-10-24).
- **Economic substance report:** to the registered agent within 6
  months after period end ((approx — confirm) — vg-corporate-
  income-tax).

## 6. Penalties and interest

Payroll Tax and SSB late-payment penalties and interest are set by
the Acts and are **needs-sources**; registered-agent late returns
carry escalating fines and striking-off risk (vg-corporate-income-
tax).

## 7. Worked examples

**Example 1 — payroll tax on a cross-border worker.** A Class 1
employer (employee's main place of work outside the BVI) pays USD
120,000 of remuneration for BVI work days; the first USD 10,000 per
employee is exempt, the balance is taxed at 10%.

```oa-check
name: class 1 payroll 120k minus 10k exempt at 10 percent
inputs:
  remuneration: 120000
  exempt: 10000
  rate: 10
steps:
  - base: remuneration - exempt
  - tax: base * pct(1, rate)
expected:
  base: 110000.00
  tax: 11000.00
```

**Example 2 — social charges capped at the insurable maximum.** An
employee earns USD 60,000; Social Security is 8.5% of insurable
earnings capped at US$53,400 (2026 maximum, read from vissb.vg), and
NHI is 7.5% capped at US$106,800 (carried from vg-payroll-social —
needs-sources).

```oa-check
name: ss 8.5 percent capped 53400 and nhi 7.5 percent capped 106800
inputs:
  earnings: 60000
  ss_cap: 53400
  nhi_cap: 106800
  ss_rate: 8.5
  nhi_rate: 7.5
steps:
  - ss: min(earnings, ss_cap) * pct(1, ss_rate)
  - nhi: min(earnings, nhi_cap) * pct(1, nhi_rate)
expected:
  ss: 4539.00
  nhi: 4500.00
```

## 8. Ask the client first

1. Where do the owners, lenders and the company itself actually
   reside and manage — which country's CFC/substance rules will read
   the BVI entity?
2. Does the counterparty country's domestic WHT apply to payments
   into the BVI (no treaty relief is usually available)?
3. Is the group in Pillar Two scope, and will implementing member
   states top up the BVI entity's 0% rate?
4. Are staff physically working in the BVI (payroll tax, SS, NHI) or
   purely outside it, and are the monthly filings current?

## 9. Sources

- [Government of the Virgin Islands — home](https://bvi.gov.vg/) — read 2026-10-24.
- [GOV.VG — Financial and Tax Information](https://bvi.gov.vg/topics/financial-and-tax-information) — read 2026-10-24.
- [GOV.VG — Inland Revenue Department](https://bvi.gov.vg/inland-revenue-department) — read 2026-10-24.
- [Virgin Islands Laws Online](https://laws.gov.vg/) — read 2026-10-24.
- [BVI Business Companies (Financial Return) Order, 2023](https://laws.gov.vg/laws/bvi-business-companies-financial-return-order-2023) — read 2026-10-24.
- [Social Security Board — Contributions](https://www.vissb.vg/contributions/) — read 2026-10-24 (rates and 2027 insurable-earnings increase).
- Existing pack skills `vg-corporate-income-tax`, `vg-payroll-social`, `vg-tax-overview` — figures carried forward with their citations.

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
