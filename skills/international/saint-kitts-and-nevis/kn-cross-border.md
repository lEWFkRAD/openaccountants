---
name: kn-cross-border
description: >
  Saint Kitts and Nevis cross-border tax reference for 2026. Covers
  residence and the six-month presence rule, the non-domiciliary
  local-source regime (Income Tax Act s.32), source rules for employment
  and trade, the 15% non-resident payment withholding, unilateral
  double-taxation relief via scheduled Orders, permanent-establishment
  articles in those Orders, and the absence of an exit tax. Uses the
  official Law Commission consolidation of the Income Tax Act
  (Cap. 18.22); source-cited draft.
jurisdiction: KN
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Saint Kitts and Nevis cross-border tax

## 1. Scope and sources

Source-cited draft checked 22 October 2026 from the Income Tax Act, Cap. 18.22 (consolidation, revision date 31 December 2017) and the Double Taxation (Relief) Act, Cap. 18.26, both read from the Law Commission site. Amounts are East Caribbean dollars.

## 2. Residence and charging scope

- An individual **resident** in the Federation is chargeable on worldwide income. The Act's residence tests include the physical-presence rule: a person who has resided in the State for periods equal in the whole to **six months in the basic year** is treated as resident for the foreign-income exemption in s.4(1) to fail (a person here for a temporary purpose only, under six months, is not charged on foreign-source income accruing to them).
- A **non-resident** is charged on Federation-source income only: employment exercised here, trades carried on here, rents from local land, and amounts deemed to arise here.
- A trade carried on partly inside and partly outside by a **resident whose home is here** is deemed wholly Federation-source (s.4(1) proviso).

## 3. The non-domiciliary regime (s.32)

A person domiciled outside the Federation who is resident (or otherwise chargeable) may be assessed on the restricted basis: only (a) income arising in the Federation, (b) income **received in or remitted to** the Federation, and (c) income deemed to arise there. Foreign employment income where the employment is exercised wholly outside is excluded. Domicile is determined by the Act's definitions — establish it with evidence before relying on the regime. This is the core planning rule for citizenship-by-investment clients.

## 4. Outbound withholding

Payments to non-residents (rents, interest, service and management fees, recharges, periodic payments — s.40 list) attract **15% withholding** by the payer, quarterly remittance (see `kn-payroll-withholding`).

## 5. Treaties

There is **no comprehensive treaty network**. Relief is unilateral under the Double Taxation (Relief) Act, Cap. 18.26, and by Orders scheduled to the Income Tax Act naming territories (the consolidation schedules Orders for Canada, Denmark, New Zealand, Norway, Sweden, the United Kingdom, Switzerland, the USA, Monaco and San Marino). **Verify which Orders are actually in force and their current text before claiming relief** — several are historic and their operative status needs confirmation (needs-sources). The scheduled texts carry OECD-style PE and associated-enterprise articles where in force.

## 6. Exit / departure

No capital-gains exit charge. The Departure Tax Act (Cap. 8.04) is a per-passenger travel charge collected by carriers; since Act 17 of 1998 it does not apply to the island of Saint Christopher (Nevis only). Short-term resale gains (disposal within one year of acquisition) are taxed at half the applicable rate, capped at 20% (ITA s.4(2)).

## 7. Worked examples

**Example 1 — foreign company with a KN branch.** Branch trading profit EC$250,000 attributable to the permanent establishment: taxed at the company rate, 250,000 × 33% = 82,500.00. No branch-profits tax on repatriation.

```oa-check
name: KN branch profit EC$250,000
inputs:
  profit: 250000
steps:
  - tax: profit * 0.33
expected:
  tax: 82500.00
```

**Example 2 — non-domiciliary resident, EC$40,000 local-source income.**
Allowances: 750 employed-person deduction (assume local employment) + 1,200 personal = 1,950. Chargeable 38,050. Schedule: first 11,000 = 3,062.50; (38,050 − 11,000) × 55% = 14,877.50. Total 17,940.00. Foreign income of 300,000 not remitted: no KN tax.

```oa-check
name: Non-domiciliary, EC$40,000 local income
inputs:
  income: 40000
steps:
  - allowances: min(0.10 * income, 750) + 1200
  - chargeable: income - allowances
  - first_11000: 500*0.05 + 500*0.075 + 500*0.10 + 500*0.125 + 500*0.15 + 1000*0.20 + 1500*0.25 + 1500*0.325 + 2000*0.40 + 2000*0.475
  - top_band: (chargeable - 11000) * 0.55
  - tax: first_11000 + top_band
expected:
  tax: 17940.00
```

## 8. Ask the client first

1. Domicile of origin/choice and evidence — does s.32 apply?
2. Days physically present in the Federation in the basic year (six-month line).
3. What foreign income is received in or remitted to KN (bank transfers count).
4. Whether any scheduled DTA Order is in force for the counterparty territory.

## 9. Sources

- [Income Tax Act, Cap. 18.22 (ss.4, 32, 40; scheduled DTA Orders)](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_22-Income-Tax-Act.pdf) — read 2026-10-22.
- [Departure Tax Act, Cap. 8.04](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-8_04-Departure-Tax-Act.pdf) — read 2026-10-22.
- [Double Taxation (Relief) Act, Cap. 18.26](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_26-Double-Taxation-Relief-Act.pdf) — read 2026-10-22.
