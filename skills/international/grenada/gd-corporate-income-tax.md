---
name: gd-corporate-income-tax
description: >
  Grenada corporate income tax reference for 2026. Covers the flat 30% company
  rate under Income Tax Act Cap. 149 Fifth Schedule, basis periods, monthly
  one-twelfth instalment payments under section 93, the 90-day return deadline,
  deposit-taking 25% special charge, withholding credits against the assessment,
  and interest on unpaid instalments. Use for Grenada company tax computations
  and instalment planning. Independent accountant review pending.
jurisdiction: GD
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
---

# Grenada corporate income tax v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows; not reviewed for any specific person's facts. Do not file, pay, or take a position on it without review by a qualified Grenadian professional.

## 1. Scope and sources

Company income tax is imposed by the Income Tax Act Cap. 149; the consolidated PDF (to Act No. 2 of 2010) was read 2026-10-27 at [Grenada Parliament](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf) (chapter page: [laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act)). A company resident in Grenada is taxable on worldwide income; a non-resident company on Grenada-source income including through a branch or agent. This skill covers the company charge and instalments; withholding on outbound payments is `gd-cross-border`; management-charge limits are `gd-transfer-pricing`.

**Source status caveat:** consolidated text runs to Act No. 2 of 2010; 2011–2026 amendments not retrievable in consolidated form on 2026-10-27. **needs-sources:** confirm the 30% Fifth Schedule company rate and the deposit-taking special charge against current amendments (the IRD G-TAX FAQ, read 2026-10-27, lists CIT among the three G-TAX monthly taxes but does not restate the rate).

## 2. Who applies

- **Resident companies** (incorporated or managed/controlled in Grenada per s.2 definitions, consolidated PDF read 2026-10-27): worldwide income.
- **Non-resident companies** carrying on business in Grenada (including branches): Grenada-source income; s.93 instalments apply to them too (s.93(1)(c)).
- **Deposit-taking banking companies:** a separate deposit-interest charge regime (s.53 area, consolidated PDF: deposit banking tax at 0% of interest as amended in the consolidated text — **needs-sources:** current percentage and interaction with the 30% company rate).
- **Approved enterprises** may hold fiscal-incentive exemptions under s.27 — check the incentive schedule before computing.

## 3. Rates and base

| Item | Amount | Source |
|---|---|---|
| Company chargeable income | **30%** flat | Cap. 149 Fifth Schedule [s.56], consolidated PDF read 2026-10-27 |
| Monthly instalment | 1/12 of estimated annual tax | s.93(3) |
| Return deadline | 90 days after basis period end | s.65(1) |

**Base:** profits and gains computed under the Act — trading income on the basis period (s.11), capital allowances per the Third Schedule, trading stock valued per the Second Schedule, general deductions s.36 with specific restrictions (management charges capped at 1% of allowable deductions other than cost of sales — s.38(1)(ii); see `gd-transfer-pricing`), loss relief s.39.

## 4. Deadlines

- **Instalments:** every resident company and every non-resident company trading in Grenada pays **one-twelfth of estimated tax at the end of each calendar month** (s.93(3)); a business with a non-December basis period pays at the end of each month of the basis period from commencement (s.93(4)(a)).
- **Final instalment:** the balance is due **on filing the annual return, within 90 days after the basis period ends** (s.93(3) final clause).
- **2025 year of assessment:** filing/payment deadline extended to **30 April 2026** ([press release PDF](https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf), read 2026-10-27).
- A missed instalment makes **the whole outstanding balance immediately due** (s.93(3)).

## 5. Penalties and interest

- **Unpaid instalments/assessments:** 1.5% interest per month or part-month (s.95).
- **Unpaid withheld amounts** (s.50/52 credits etc.): 2% per month (s.97).
- **Late/incorrect returns:** ss.111–112 penalties with s.114 prior notice; mitigation s.123.
- **Disallowance lever:** the Comptroller disallows expenses (including fees, royalties, discounts, management charges) where the s.52 15% withholding was not deducted and paid — a cash-tax cost larger than the rate itself.

## 6. Cross-border

Branches of non-resident companies are assessed like residents on Grenada-source profits; head-office management charges face the s.38(1) 1% cap (CARICOM-sourced services exception where the Comptroller is satisfied — s.38(1) proviso). Outbound payments to non-residents carry final 15% withholding (s.50 + Third Schedule) and non-resident shipping/airline gross-carriage charges (s.46) — see `gd-cross-border`. Group relief and consolidation do not appear in the consolidated text; treat each entity standalone. **needs-sources:** DTR orders under s.43 must be pulled from the gazette.

## 7. Worked examples

**Example 1 — monthly instalments.** A company estimates its year's tax at EC$120,000.

```oa-check
name: monthly one-twelfth instalment
inputs:
  est_tax: 120000
  months: 12
steps:
  - instalment: est_tax / months
expected:
  instalment: 10000
```

Pay 10,000 at each month-end; reconcile the balance with the return filed within 90 days of the basis period end.

**Example 2 — assessment net of s.52 withholding credits.** Company profits EC$250,000; during the year it paid EC$40,000 in fees/royalties to residents from which 15% tax was deducted and credited (s.52(2)).

```oa-check
name: company assessment less withholding credits
inputs:
  profits: 250000
  rate: 0.30
  fees_paid: 40000
  wht: 0.15
steps:
  - gross_tax: profits * rate
  - credit: fees_paid * wht
  - net_due: gross_tax - credit
expected:
  gross_tax: 75000
  credit: 6000
  net_due: 69000
```

## 8. Ask the client

- Basis period end date and whether instalments tracked the current-year estimate (a low estimate creates a large final instalment; a missed month accelerates the whole balance).
- Whether any incentive exemption (s.27) or concession order (s.55A Minister/Cabinet exemption power) applies.
- All payments to non-residents and to resident fee/royalty recipients — confirm 15% WHT was deducted and remitted within 7 days, and that credit certificates exist.
- Management charges to non-residents or head offices: quantify the s.38(1) 1% cap exposure.
- Deposit-taking status and which banking-specific charge regime applies.

## 9. Sources

- [Income Tax Act Cap. 149 consolidated PDF — ss. 11, 27, 36–39, 52, 53, 55A, 56, 65, 93, 95, 97, 111–114, 123, Second/Third/Fifth Schedules](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf) — read 2026-10-27
- [Cap. 149 chapter page, laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act) — read 2026-10-27
- [IRD G-TAX FAQ (CIT on G-TAX, compliance duties)](https://www.ird.gd/gtax/index.html) — read 2026-10-27
- [IRD filing-deadline extension press release, 31 March 2026 (PDF)](https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf) — read 2026-10-27
- [Grenada Gazette portal](https://www.gazettes.gov.gd/index.php/publications/2025?layout=default) — read 2026-10-27

<!-- openaccountants-cta-block -->

**Talk to a verified accountant** — this skill is a source-cited draft (tier 2). For Grenada company filings under professional review, book time with an OpenAccountants verified accountant: [Calendly](https://www.openaccountants.com).
