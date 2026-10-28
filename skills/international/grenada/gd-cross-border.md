---
name: gd-cross-border
description: >
  Grenada cross-border tax reference for 2026. Covers source-based
  chargeability, final 15% withholding on payments to non-residents under
  Income Tax Act Cap. 149 section 50 and the Third Schedule, 15% withholding on
  non-resident employment income (s.51), the 30% charge on 2% of gross
  carriage for non-resident shipping and airlines (s.46), the foreign-address
  presumption, treaty rate directions under s.43/s.50(5), and the absence of a
  statutory exit tax. Use for Grenada inbound/outbound engagements and
  non-resident payment working papers. Independent accountant review pending.
jurisdiction: GD
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
---

# Grenada cross-border v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows; not reviewed for any specific person's facts. Do not file, pay, or take a position on it without review by a qualified Grenadian professional.

## 1. Scope and sources

Grenada charges non-residents on income accruing in or derived from Grenada (Income Tax Act Cap. 149, consolidated PDF read 2026-10-27, [Grenada Parliament](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf); chapter page [laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act)). Passive and services payments to non-residents are almost always captured by **final withholding** rather than a Grenada return. This skill covers the non-resident charge and outbound payments; the resident worldwide charge is `gd-income-tax`; PAYE is `gd-payroll-withholding`; related-party pricing is `gd-transfer-pricing`.

**Source status caveat:** consolidated text to Act No. 2 of 2010; 2011–2026 amendments not retrievable in consolidated form on 2026-10-27 (gazettes.gov.gd reachable; www.ird.gd tax pages HTTP 500). The IRD G-TAX FAQ (read 2026-10-27) independently describes withholding at 15% on payments by a resident to a non-resident, corroborating the Third Schedule rate. **needs-sources:** in-force DTR orders under s.43.

## 2. Who applies

- **Non-resident carrying on business in Grenada:** assessed on Grenada-source business profits like a resident (with s.93 instalments); the Third Schedule does **not** apply to "other payments" to a non-resident trading in Grenada (Third Schedule para 1(1)(g) carve-out).
- **Non-resident receiving passive/services payments** (interest, discounts, commissions, fees, management charges, rent, lease premiums, licence charges, royalties, annuities, other periodic payments): the payment **does not form part of the payee's chargeable income** — 15% withholding is the **final liability** (s.50 + Third Schedule paras 2–3).
- **Non-resident performing independent personal services in Grenada:** same Third Schedule withholding (para 1(2)).
- **Non-resident employee paid by a Grenada business that deducts the salary:** 15% withholding under s.51 within 7 days (distinct from Fourth Schedule PAYE — see `gd-payroll-withholding`).
- **Non-resident partner in a Grenada partnership:** s.51A — the Comptroller may charge the partnership on the non-resident partner's share and the partnership recovers on payment.
- **Payer side:** every person making a covered payment (whether or not in business) must withhold (s.50(1)); a payee at an **address outside Grenada is presumed non-resident** unless the contrary is proved (s.50(4)).
- **Accruals discipline:** where a covered expense is accrued but unpaid at the accounting date, the payer must pay the withholding **when the business return is filed** and may recover it when the payment is later made (s.50(2)).

## 3. Rates and base

Withholding on payments to non-residents (base = gross payment; [Cap. 149 Third Schedule para 3](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf) read 2026-10-27; corroborated by [IRD G-TAX FAQ](https://www.ird.gd/gtax/index.html) read 2026-10-27):

| Payment category | WHT rate | Character |
|---|---|---|
| Interest, rent/lease/licence, royalty, management charge, commission/fee, annuities, other deductible payments | **15%** | final |
| Independent personal services performed in Grenada | **15%** | final |
| Non-resident employment income (s.51) | **15%** | on account |
| Non-resident shipping/airline: 2% of gross carriage from Grenada deemed assessable, charged at 30% (s.46) — effective **0.6% of gross fare** | 30% of deemed base | final; collected by local agents within 7 days of month end |
| Deposit interest (s.53/54 area) | special deposit-interest regime — **needs-sources:** current percentage (consolidated text shows 0% deposit banking tax as amended to 2010) | — |

The Comptroller may **direct a lower rate** where the payee is resident in a country with a s.43 agreement providing a lower WHT rate (s.50(5)) — never self-apply a treaty rate.

**Exit tax:** no statutory departure charge appears in the consolidated Cap. 149 (read 2026-10-27). **needs-sources:** absence confirmed only against the consolidated text.

## 4. Deadlines

- **WHT remittance:** pay the Comptroller **within 7 days** after the date of payment or credit to the payee (s.50(1)); PAYE-linked amounts are due within 7 days after month end (s.96).
- **Annual reconciliation:** return of total WHT deducted and remitted **within 2 months after the calendar year end** (Third Schedule para 5(2)); deficiencies must be accounted for (para 5(3)).
- **Certificates** to payee for every deduction (para 4(1)); records per payee kept for inspection (para 4(2)).
- Non-resident **business** filers: return within 90 days of basis period end (s.65(1)); 2025-year deadline extended to 30 April 2026 ([press release PDF](https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf), read 2026-10-27).

## 5. Penalties and interest

- **Failure to deduct:** payer is **personally liable** for the tax plus any penalty (Third Schedule para 6(1)); may recover from the payee (para 6(3)).
- **Disallowance:** unpaid WHT makes the expense non-deductible (s.50(3)) — the dominant economic penalty.
- **Interest on unpaid deducted/deductible amounts:** 2% per month (s.97), unrecoverable from the payee (s.97(2)).
- Late returns/assessments: ss.111–112 penalties, 1.5%/month interest (s.95).

## 6. Cross-border (treaties and residence)

s.43 empowers the Minister to conclude DTR agreements covering non-arm's-length attribution (s.43(1)(c)), PE attribution (s.43(1)(b)), source location (s.43(1)(d)) and reciprocal assistance/exchange of information (s.43(1)(e)). **needs-sources:** the consolidated PDF lists no subsidiary legislation under Cap. 149 — pull the in-force orders (Grenada's known treaty network includes the UK, Canada and CARICOM double-tax arrangements) from gazettes.gov.gd before crediting relief or applying reduced rates. Residence ties break on the s.2 definitions (read 2026-10-27); the foreign-address presumption (s.50(4)) governs withholding decisions. No exit tax; departure triggers only the ordinary return for the year of departure.

## 7. Worked examples

**Example 1 — royalty to a non-resident licensor.** Annual royalty EC$20,000 paid to a non-resident company.

```oa-check
name: final 15 percent WHT on royalty
inputs:
  royalty: 20000
  wht: 0.15
steps:
  - wht_amount: royalty * wht
  - net_paid: royalty - wht_amount
expected:
  wht_amount: 3000
  net_paid: 17000
```

Remit 3,000 within 7 days of payment; the licensor files nothing further in Grenada (final liability).

**Example 2 — non-resident airline carrying passengers from Grenada.** Gross ticket revenue from Grenada-origin carriage EC$500,000 for the month.

```oa-check
name: s.46 shipping and airline charge
inputs:
  gross_carriage: 500000
  deemed_pct: 0.02
  wht: 0.30
steps:
  - deemed_income: gross_carriage * deemed_pct
  - wht_amount: deemed_income * wht
expected:
  deemed_income: 10000
  wht_amount: 3000
```

The local agent/branch withholds and pays 3,000 within 7 days after month end (s.46(2)); Third Schedule paras 4–6 record-keeping applies (s.46(3)).

## 8. Ask the client

- Payee addresses and residence evidence — the foreign-address presumption decides withholding.
- Whether accrued-but-unpaid related-party fees were caught by the s.50(2) advance-payment rule at return time.
- Any Comptroller **direction** for a treaty-reduced rate — a direction must exist before applying less than 15%.
- Airline/shipping/local-agent arrangements for s.46 carriage collections.
- For inbound assignments: whether the salary runs through Fourth Schedule PAYE or s.51 non-resident withholding — the two routes differ.

## 9. Sources

- [Income Tax Act Cap. 149 consolidated PDF — ss. 2, 43, 46, 50, 51, 51A, 53, 65, 95–97, Third Schedule paras 1–6](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf) — read 2026-10-27
- [Cap. 149 chapter page, laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act) — read 2026-10-27
- [IRD G-TAX FAQ (15% WHT description, G-TAX scope)](https://www.ird.gd/gtax/index.html) — read 2026-10-27
- [IRD filing-deadline extension press release, 31 March 2026 (PDF)](https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf) — read 2026-10-27
- [Grenada Gazette portal](https://www.gazettes.gov.gd/index.php/publications/2025?layout=default) — read 2026-10-27 (DTR order search pending)

<!-- openaccountants-cta-block -->

**Talk to a verified accountant** — this skill is a source-cited draft (tier 2). For Grenada cross-border work under professional review, book time with an OpenAccountants verified accountant: [Calendly](https://www.openaccountants.com).
