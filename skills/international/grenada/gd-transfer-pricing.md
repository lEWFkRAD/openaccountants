---
name: gd-transfer-pricing
description: >
  Grenada transfer pricing and related-party reference for 2026. Covers the
  Comptroller's associated-enterprise adjustment power under Income Tax Act
  Cap. 149 section 23(2), arm's-length deemed interest on resident-to-non-
  resident loans and constructive loans (s.23(3)-(4)), the general anti-
  avoidance rule (s.23(1)), the 1% management-charge deduction cap (s.38(1)),
  shareholder-advance income (s.29(1)(h)), and the absence of a statutory TP
  documentation regime. Use for Grenada related-party pricing reviews and
  Comptroller adjustment exposure. Independent accountant review pending.
jurisdiction: GD
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Grenada transfer pricing v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows; not reviewed for any specific person's facts. Do not file, pay, or take a position on it without review by a qualified Grenadian professional.

## 1. Scope and sources

Grenada has **no statutory transfer-pricing documentation regime** (no local/master file, no TP form) in the consolidated Income Tax Act Cap. 149 (PDF read 2026-10-27, [Grenada Parliament](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf); chapter page [laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act)). Adjustments are **Comptroller-driven** under three levers: the general anti-avoidance rule and associated-enterprise provisions in s.23, the management-charge cap in s.38(1), and the treaty-power attribution rules in s.43. This skill maps those levers; the payment-withholding consequences sit in `gd-cross-border`.

**Source status caveat:** consolidated text to Act No. 2 of 2010; 2011–2026 amendments not retrievable in consolidated form on 2026-10-27. **needs-sources:** confirm no post-2010 act introduced a documentation or penalty regime (OECS neighbours have moved on AEOI-driven compliance; the IRD G-TAX FAQ, read 2026-10-27, does not mention TP).

## 2. Who applies

- **A resident carrying on business with a non-resident** where the relationship between them has arranged the course of business so the resident's profits are more or less than they would be absent the relationship — s.23(2) lets the Comptroller deem additional gains assessable and deem part of the non-resident's profits Grenada-source.
- **A resident making an interest-free or cheap loan (including a constructive loan) to a non-resident** not at arm's length — deemed interest accrues to the resident at a Comptroller-set commercial rate each year (s.23(3)); "constructive loan" covers unpaid business indebtedness that would not stand between independent persons (s.23(4)).
- **Any person in a tax-avoiding transaction** — s.23(1) GAAR: Comptroller may recharacterise transactions whose manner or created rights/obligations deviate from arm's-length norms.
- **Companies paying management charges to non-residents or to non-Grenada head offices/branches** — s.38(1) deduction cap.
- **Controlled companies advancing funds to shareholders/associates** — the advance becomes shareholder income (s.29(1)(h) with s.38(3) "associate" definition, consolidated PDF read 2026-10-27).

## 3. Rates and base

| Lever | Effect | Source |
|---|---|---|
| Associated-enterprise profits | Comptroller-determined reasonable attribution | Cap. 149 s.23(2) |
| Cheap/constructive loans | deemed interest at Comptroller-set commercial rate | s.23(3)–(4) |
| Management charges to non-residents | deduction capped at the **lesser** of the charge or **1% of allowable s.36 deductions (excluding cost of sales)** | s.38(1)(ii) |
| CARICOM-sourced management services | cap may be relaxed where the Comptroller is satisfied (s.38(1) proviso) | s.38(1) |
| Treaty attribution | s.43(1)(c) non-arm's-length trading arrangements; s.43(1)(b) PE attribution | s.43 |

**Base:** the adjustments operate on the assessable/chargeable income computed under `gd-corporate-income-tax` or `gd-income-tax`. There is no separate TP return; exposure surfaces on audit under s.68 information powers and s.78/79 assessments.

## 4. Deadlines

- No TP filing deadline exists. Records supporting related-party pricing should be ready for a s.68 notice; failure to comply with a notice carries a penalty up to $1,000 (s.113) and assessments then bear 1.5%/month interest (s.95).
- The s.38(1) cap and s.52 withholding bite **at deduction time** — model them in the same computation as the return, not after.

## 5. Penalties and interest

- Reconstructed assessments (ss.78–79) attract 1.5%/month interest (s.95(2)).
- GAAR/associated-enterprise adjustments carry the tax plus interest; criminal offences for false statements under the Act's Division II provisions (sanction-controlled, s.115).
- The heaviest practical penalty is **expense disallowance**: unpaid s.50/s.52 withholding makes the underlying expense non-deductible (s.50(3), s.52(3)) — a 30% × expense hit on top of the withheld tax.

## 6. Cross-border

All three levers are cross-border by design (resident ↔ non-resident). s.43 empowers DTR agreements with non-arm's-length attribution and PE-attribution articles; **needs-sources:** pull the in-force orders from the gazette (the consolidated PDF lists no subsidiary legislation under Cap. 149). Asset transfers between related persons are valued at arm's length (consolidated PDF's deemed-disposal provisions, read 2026-10-27). Export-side: a Grenada parent trading with a foreign subsidiary should price services and funding to survive s.23(2)/23(3) review.

## 7. Worked examples

**Example 1 — management-charge cap.** A Grenada distributor deducts EC$80,000 of management charges to a non-resident affiliate; its other allowable s.36 deductions (excluding cost of sales) are EC$6,000,000.

```oa-check
name: s.38(1) one percent management charge cap
inputs:
  mgmt_charge: 80000
  other_deductions: 6000000
  cap_pct: 0.01
steps:
  - cap: other_deductions * cap_pct
  - allowed: min(mgmt_charge, cap)
  - disallowed: mgmt_charge - allowed
expected:
  cap: 60000
  allowed: 60000
  disallowed: 20000
```

The disallowed 20,000 also needs the s.50 15% withholding lens — see Example 2.

**Example 2 — withholding on the allowed management charge.** The allowed EC$60,000 is paid to the non-resident; s.50 + Third Schedule require 15% final withholding.

```oa-check
name: WHT on allowed management charge
inputs:
  charge: 60000
  wht: 0.15
steps:
  - wht_amount: charge * wht
  - net_paid: charge - wht_amount
expected:
  wht_amount: 9000
  net_paid: 51000
```

Remit 9,000 within 7 days of payment; if not, the whole 60,000 becomes non-deductible (s.50(3)).

## 8. Ask the client

- Full related-party transaction inventory: goods, services, management charges, loans, royalties, asset transfers — with counterparties' residence.
- Loan books: any interest-free or below-market advances to non-residents, and aged unpaid trade balances (constructive loans).
- Management-charge computation against the s.38(1) 1% base, and whether services come from CARICOM (proviso).
- Shareholder/associate advances outstanding at year-end (s.29(1)(h) income trigger).
- Evidence file quality: pricing comparables a Comptroller audit could test — there is no safe harbour and no penalty for lacking documents, but the burden effectively falls on the taxpayer.

## 9. Sources

- [Income Tax Act Cap. 149 consolidated PDF — ss. 23, 29(1)(h), 38, 43, 50, 52, 68, 78–79, 95, 113](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf) — read 2026-10-27
- [Cap. 149 chapter page, laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act) — read 2026-10-27
- [IRD G-TAX FAQ](https://www.ird.gd/gtax/index.html) — read 2026-10-27
- [Grenada Gazette portal](https://www.gazettes.gov.gd/index.php/publications/2025?layout=default) — read 2026-10-27 (DTR orders search pending)

<!-- openaccountants-cta-block -->

**Talk to a verified accountant** — this skill is a source-cited draft (tier 2). For Grenada related-party work under professional review, book time with an OpenAccountants verified accountant: [Calendly](https://www.openaccountants.com).
