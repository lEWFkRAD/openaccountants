---
name: vc-transfer-pricing
description: >
  Saint Vincent and the Grenadines transfer pricing and related-party rules for
  2026. Covers Income Tax Act Cap. 435 section 23: the Comptroller's power to
  counteract non-arm's-length transactions, profit adjustment for resident–
  non-resident business arrangements, deemed interest on below-market and
  constructive loans, the deduction block where non-resident withholding is
  unpaid, and treaty-based attribution under section 60. No statutory TP
  documentation regime exists. Use for SVG related-party pricing working papers.
  Does not cover OECD guidelines as law or Economic Substance requirements.
  Independent accountant review pending.
jurisdiction: VC
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Saint Vincent and the Grenadines transfer pricing v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows; not reviewed for any specific person's facts. Do not file, pay, or take a position on it without review by a qualified SVG professional.

## 1. Scope and sources

SVG has **no standalone transfer-pricing statute and no statutory TP documentation regime**. Related-party pricing is policed through the Income Tax Act Cap. 435 arm's-length provisions and treaty attribution rules. Sources: [Income Tax Act Cap. 435 consolidated PDF](https://ird.gov.vc/images/pdf/Cap435.pdf), read 2026-10-27 (ss. 13, 23, 60, 66; DTR orders list); [IRD legislation page](https://ird.gov.vc/index.php/legislation) read 2026-10-27. This skill covers when the Comptroller can reprice a related-party deal and the loan rules. It does not cover Economic Substance Act obligations (separate IRD guidance) or OECD guidelines, which are persuasive only.

## 2. Who applies

- Any **resident person** transacting with a **non-resident** where the relationship affects pricing (s.23(2)).
- Any person using a **transaction, operation or scheme** — including property alienation — that avoids, reduces or postpones tax, where the manner or the rights created are not what independent persons dealing at arm's length would normally create (s.23(1)).
- Any **resident lender** making an interest-free or low-interest loan (including a constructive loan: unpaid business indebtedness that would not persist between independents) to a non-resident (s.23(3)).
- Permanent establishments in SVG of non-residents, and SVG residents with PE abroad, via s.60 treaty orders.

## 3. Rates and base

There is no TP "rate". The base adjustments are:

| Provision | Adjustment mechanism |
|---|---|
| s.23(1) scheme rule | Comptroller determines liability as if the transaction had not occurred, or otherwise counteracts the avoidance |
| s.23(2) related trade | Comptroller deems additional gains assessable to the resident, and/or deems part of the non-resident's profits to have a SVG source |
| s.23(3) cheap/constructive loans | Deemed interest accrues to the resident lender each year at a commercial rate the Comptroller deems reasonable |
| s.13(2) deduction block | No deduction for payments to non-residents under s.66 unless the withholding tax has actually been paid |
| s.66(3) treaty override | Comptroller may direct a lower WHT rate where a DTA provides one |

Companies face the 28% corporate rate (`vc-corporate-income-tax`); the repriced amount follows the taxpayer's own rate schedule.

## 4. Deadlines

No separate TP return or filing calendar. Adjustments surface through assessment: CIT returns are due 3 months after financial year end ([IRD taxes page](https://ird.gov.vc/index.php/taxes), read 2026-10-27), and the Comptroller may raise assessments with the Tax Administration Act late-filing/late-payment consequences (see `vc-paye-withholding` §5 for the TAA penalty table). Deemed interest under s.23(3) accrues **for each year of assessment after the loan is made** — exposure compounds annually.

## 5. Penalties and interest

- Underpayment found through a s.23 adjustment can attract the TAA s.77 negligent/fraudulent underpayment penalty: 75% of the underpayment where it exceeds $150,000 or 25% of liability, otherwise 25% ([IRD non-compliance page](https://ird.gov.vc/index.php/non-compliance), read 2026-10-27).
- Interest 1.5% monthly on unpaid assessed amounts (IRD taxes page).
- Unpaid non-resident WHT both blocks the deduction (s.13) and carries its own late-payment penalty.

## 6. Cross-border

The DTR orders listed under Cap. 435 include the United Kingdom, Canada, Sweden, Norway, Denmark, the USA, New Zealand and Switzerland (consolidated PDF list, read 2026-10-27; **needs-sources:** current in-force status of each order not verified — some are old and may be superseded). Treaty associated-enterprise articles attribute to a PE the profits an independent enterprise would have derived dealing at arm's length (e.g. the UK order's business-profits article in the Cap. 435 PDF). See `vc-cross-border` for non-resident taxation and WHT.

## 7. Worked examples

**Example 1 — below-market intercompany loan.** SVG resident lends a non-resident affiliate EC$200,000 interest-free; the Comptroller deems a commercial rate of 8%.

```oa-check
name: s.23(3) deemed interest, one year
inputs:
  principal: 200000
  rate: 0.08
  cit: 0.28
steps:
  - deemed_interest: principal * rate
  - cit_on_adjustment: deemed_interest * cit
expected:
  deemed_interest: 16000
  cit_on_adjustment: 4480
```

**Example 2 — underpriced management fee gross-up.** A resident pays a non-resident affiliate a fee the Comptroller reprices upward by EC$50,000; the fee was already subject to 20% services WHT that was not remitted.

```oa-check
name: repriced fee plus unpaid WHT consequence
inputs:
  uplift: 50000
  wht: 0.20
  cit: 0.28
steps:
  - wht_due: uplift * wht
  - extra_deduction: uplift
  - cit_effect: extra_deduction * cit
  - net_cost_shift: wht_due - cit_effect
expected:
  wht_due: 10000
  cit_effect: 14000
  net_cost_shift: -4000
```

The deduction for the uplifted fee is only available once the WHT is paid (s.13) — the CIT effect above is conditional on remittance.

## 8. Ask the client

- Full list of transactions with non-resident affiliates: goods, services, fees, rent, interest, IP, guarantees.
- Loan ledger: interest-free or low-interest balances to non-residents and aged unpaid trade credit (constructive loans).
- Whether WHT on every non-resident payment was actually remitted — unpaid WHT kills the deduction.
- Which treaty (if any) the counterparty relies on, and whether the Comptroller has directed a reduced rate.
- Whether the entity has Economic Substance Act obligations that interact with the pricing story.

## 9. Sources

- [Income Tax Act Cap. 435 (consolidated PDF) — ss. 13, 23, 60, 66, DTR orders](https://ird.gov.vc/images/pdf/Cap435.pdf) — read 2026-10-27
- [IRD — Taxes (rates, deadlines, interest)](https://ird.gov.vc/index.php/taxes) — read 2026-10-27
- [IRD — Non-Compliance (TAA 2019 penalties)](https://ird.gov.vc/index.php/non-compliance) — read 2026-10-27
- [IRD — Legislation](https://ird.gov.vc/index.php/legislation) — read 2026-10-27

<!-- openaccountants-cta-block -->

**Talk to a verified accountant** — this skill is a source-cited draft (tier 2). For SVG related-party work under professional review, book time with an OpenAccountants verified accountant: [Calendly](https://www.openaccountants.com).
