---
name: py-cross-border-tax
description: Use when a non-resident receives Paraguay-source income or a Paraguay-connected taxpayer needs the 2026 non-resident tax withholding rates, deemed-source rules, tax-haven treatment, or treaty position. Trigger on Paraguay non-resident tax, Impuesto a la Renta de No Residentes, IRNR withholding Paraguay, payments to foreign suppliers Paraguay, Paraguay tax haven list. Covers the 15% non-resident tax on conclusive-presumption bases, 10% dividend withholding, branch treatment, and the limited treaty network. Source-cited draft with needs-sources caveats.
jurisdiction: PY
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Paraguay cross-border tax

## 1. Who this applies to

- Individuals, legal entities, and other entities **not residing in Paraguay** that obtain income, profits, or benefits of Paraguay source — taxpayers of the **non-resident tax** (PwC Paraguay withholding taxes, read 2026-10-24).
- Paraguayan payers (banks, companies, individuals with taxed independent services) acting as **withholding agents** on outbound payments.
- Out of scope: resident taxpayers' own IRE/IRP (`py-corporate-income-tax`, `paraguay-income-tax`); connected-party pricing (`py-transfer-pricing`).

## 2. Rates and deemed-source bases

| Payment / income | Rate | Base | Source (as_of 2026-10-24) |
|---|---|---|---|
| Non-resident tax on Paraguay-source services and similar | 15% | **conclusive-presumption** deemed bases per service type (a fixed portion is deemed Paraguay-source; proof to the contrary not accepted) | PwC Paraguay withholding taxes |
| Dividends from Paraguayan entities to any shareholder | 10% withholding | gross dividend | PwC Paraguay corporate income determination (read 2026-10-24) |
| Non-resident capital gains (Paraguay-source assets, incl. shares of Paraguayan companies) | 10% | gain; issuing Paraguayan company answers for the seller's tax on private share transfers | PwC Paraguay withholding taxes |
| International freight | non-resident tax | paid before withdrawal of goods from customs; one-time definitive payment | PwC Paraguay withholding taxes |

- **Deemed source**: income from activities carried out with assets or rights used financially in Paraguay is Paraguay-source, even if the counterparty is abroad (PwC Paraguay withholding taxes, read 2026-10-24).
- **Withholding trigger**: the obligation attaches when funds become available, when they are remitted abroad, or whenever a payment is made — whichever comes first; compensation/novation counts as availability (PwC, read 2026-10-24).

## 3. Base and computation

- Apply the statutory deemed-source percentage for the service type to the gross payment, then 15% to that base. The percentages are set by the law/regulations per service category — **needs-sources** for the current table (statute text unreachable 2026-10-24); do not invent a percentage.
- Dividends: 10% of the gross distribution, withheld by the paying Paraguayan entity (PwC Paraguay income determination, read 2026-10-24).

## 4. Deadlines and filing

- Withheld non-resident tax is settled through the payer's DNIT filings; the attachment moment is availability/remittance/payment (above). Payment deadlines follow the DNIT calendar keyed to taxpayer-ID digits (PwC Paraguay tax administration, read 2026-10-24).
- Share transfers: the Paraguayan issuer company must pay the seller's tax by the transaction/contract date (PwC Paraguay withholding taxes, read 2026-10-24).

## 5. Penalties and interest

- Failure to withhold exposes the payer: late-payment fine 4%–14% plus 0.116% per day; omission of payment 50% fine; fraud one to three times (PwC Paraguay tax administration, read 2026-10-24).
- Five-year audit window.

## 6. Treaties and tax havens

- Paraguay's double-tax-treaty network is **limited**; treaty entitlement for a specific counterparty is **needs-sources** — verify before reducing any withholding.
- No statutory domestic "tax haven blacklist" is confirmed in the sources read; low/no-tax counterparties attract audit scrutiny rather than a distinct statutory rate — **needs-sources**.

## 7. Worked examples

**Example 1 — dividend withholding.** A Paraguayan S.A. distributes PYG 500,000,000 of 2026 profits to a foreign parent. Dividend withholding: 500,000,000 × 10% = PYG 50,000,000, withheld and paid to DNIT by the company.

```oa-check
name: py dividend withholding 10%
inputs:
  dividend: 500000000
steps:
  - wht: dividend * 0.10
expected:
  wht: 50000000.00
```

**Example 2 — service fee on a deemed base.** A Paraguayan company pays a foreign consultant PYG 1,000,000,000. The regulations deem 50% of that service income Paraguay-source (illustrative base — confirm the statutory percentage). Non-resident tax: 1,000,000,000 × 50% × 15% = PYG 75,000,000, withheld when funds become available.

```oa-check
name: py non-resident tax deemed base
inputs:
  gross_fee: 1000000000
  deemed_portion: 0.50
steps:
  - base: gross_fee * deemed_portion
  - tax: base * 0.15
expected:
  tax: 75000000.00
```

## 8. Ask the client first

1. What is the counterparty's residence, and is there any applicable treaty?
2. What service type is the payment — which deemed-source percentage applies?
3. When do funds become available / when is remittance planned (withholding trigger)?
4. For share sales of Paraguayan companies: has the issuer company collected/paid the seller's tax?
5. Are there repeated small remittances that each trigger withholding?

## 9. Sources

- [PwC Worldwide Tax Summaries — Paraguay Corporate: Withholding taxes](https://taxsummaries.pwc.com/paraguay/corporate/withholding-taxes) — read 2026-10-24 (PwC last reviewed 19 Oct 2026).
- [PwC Worldwide Tax Summaries — Paraguay Corporate: Income determination](https://taxsummaries.pwc.com/paraguay/corporate/income-determination) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — Paraguay Corporate: Tax administration](https://taxsummaries.pwc.com/paraguay/corporate/tax-administration) — read 2026-10-24.
- [DNIT portal](https://www.set.gov.py/) — read 2026-10-24 (HTTP 200).
- Ley 72/2023 non-resident tax deemed-base table — **needs-sources** (unreachable 2026-10-24).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
