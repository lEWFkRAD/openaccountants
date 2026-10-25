---
name: py-transfer-pricing
description: >-
  Use when a Paraguay taxpayer has related-party or cross-border connected
  transactions and needs the 2026 arm's-length, documentation, adjustment, and
  penalty position. Trigger on Paraguay transfer pricing, precios de
  transferencia, related-party pricing Paraguay, DNIT connected-party audit.
  Paraguay's statutory transfer-pricing regime is thin — the arm's-length
  principle is enforced through the IRE necessity-of-expense rules and DNIT
  audit practice, not a dedicated documentation code. Source-cited draft with
  needs-sources caveat.
jurisdiction: PY
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Paraguay transfer pricing

## 1. Who this applies to

- Paraguayan IRE taxpayers (general regime; IRE SIMPLE taxpayers on the real-income basis) that transact with related parties — affiliates, parent companies, directors-related entities — especially cross-border.
- Paraguayan payers making payments to foreign suppliers for services deemed Paraguay-source: those payments are caught by the **non-resident tax** withholding rules (see `py-cross-border-tax`), which function as the primary connected-party control.
- Out of scope: purely domestic unrelated-party pricing; IVA treatment (`paraguay-iva`).

## 2. Core rules and threshold

- Paraguay has **no dedicated transfer-pricing statute with fixed documentation tiers** comparable to OECD-country local-file/master-file regimes. The operative rules are: (a) IRE deductions require costs and expenses "necessary to produce and maintain the source of income" (PwC Paraguay, corporate CIT, read 2026-10-24), and (b) DNIT's audit practice tests whether connected-party prices shift Paraguay-source profit out of the 10% base.
- **AUDIT FLASH POINT** — related-party management fees, royalties, and intercompany interest charged by foreign affiliates are the classic recharacterisation targets: DNIT can disallow the expense entirely (not merely reprice it) when necessity or arm's-length support is missing.
- Statutory arm's-length methodology and any documentation threshold under Ley 72/2023: **needs-sources** (gazette text not reachable from the drafting environment 2026-10-24). Do not assert a documentation deadline without the statute.

## 3. Practical standard

- Price connected-party goods, services, intangibles and financing as if the parties were unrelated; keep contemporaneous support (contracts, invoices meeting DNIT formal requirements, benchmarking or cost build-ups).
- The conclusive-presumption tax bases in the non-resident tax (fixed deemed-source portions, 15% rate — PwC Paraguay withholding taxes, read 2026-10-24) mean the withholding lane does **not** accept transfer-pricing arguments to shrink the base; recharacterisation happens on the IRE side instead.

## 4. Adjustments and double tax

- A DNIT upward adjustment increases the Paraguayan IRE base by the disallowed/difference amount at 10%.
- No treaty relief mechanism is confirmed for corresponding adjustments (treaty network limited — needs-sources).

## 5. Penalties and interest

- Underpayment from a recharacterisation carries the general regime: late-payment fine 4%–14% plus 0.116% per day interest; omission of payment fine 50%; tax fraud one to three times the tax (PwC Paraguay tax administration, read 2026-10-24).
- Audit window: last five fiscal years.

## 6. Cross-border points

- Payments to foreign affiliates for services used in Paraguay are Paraguay-source for non-resident tax purposes regardless of where performed; withholding attaches when funds become available, are remitted, or are paid, whichever first (PwC Paraguay withholding taxes, read 2026-10-24).
- Payments to entities in low/no-tax jurisdictions draw additional scrutiny (see `py-cross-border-tax`).

## 7. Worked examples

**Example 1 — management-fee disallowance.** A Paraguayan distributor pays its foreign parent a management fee of PYG 150,000,000. DNIT finds no necessity or benefit evidence and disallows the expense. IRE effect: 150,000,000 × 10% = PYG 15,000,000 additional tax, before fines and interest.

```oa-check
name: py related-party fee disallowance
inputs:
  fee_disallowed: 150000000
steps:
  - extra_tax: fee_disallowed * 0.10
expected:
  extra_tax: 15000000.00
```

**Example 2 — understated transfer price on goods.** A Paraguayan manufacturer sells export goods to its foreign affiliate at PYG 1,200,000,000 when the supported arm's-length price is PYG 1,500,000,000. The PYG 300,000,000 profit shift back into the Paraguay base costs 300,000,000 × 10% = PYG 30,000,000.

```oa-check
name: py understated export price uplift
inputs:
  arm_length_price: 1500000000
  recorded_price: 1200000000
steps:
  - uplift: arm_length_price - recorded_price
  - extra_tax: uplift * 0.10
expected:
  extra_tax: 30000000.00
```

## 8. Ask the client first

1. Which connected-party flows exist (goods, services, royalties, interest, management fees) and at what prices?
2. Is there contemporaneous support that each expense was necessary and at arm's length?
3. Were non-resident tax withholdings applied on the payment leg?
4. Is the counterparty in a low/no-tax jurisdiction?
5. Any DNIT requerimiento (audit notice) already received — which years?

## 9. Sources

- [PwC Worldwide Tax Summaries — Paraguay Corporate: Taxes on corporate income](https://taxsummaries.pwc.com/paraguay/corporate/taxes-on-corporate-income) — read 2026-10-24 (PwC last reviewed 19 Oct 2026).
- [PwC Worldwide Tax Summaries — Paraguay Corporate: Withholding taxes](https://taxsummaries.pwc.com/paraguay/corporate/withholding-taxes) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — Paraguay Corporate: Tax administration](https://taxsummaries.pwc.com/paraguay/corporate/tax-administration) — read 2026-10-24.
- [DNIT portal](https://www.set.gov.py/) — read 2026-10-24 (HTTP 200).
- Ley 72/2023 statutory transfer-pricing text — **needs-sources** (unreachable 2026-10-24).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
