---
name: bolivia-transfer-pricing
description: >
  Bolivia transfer pricing reference for 2026. Bolivia has no
  standalone transfer-pricing statute: related-party pricing is
  policed through the IUE (Ley 843) deductibility and source rules
  and the general anti-avoidance rule of the Codigo Tributario
  (Ley 2492). Covers the audit exposure on affiliate purchases,
  management fees and financing, the 12.5% non-resident withholding
  overlay, treaty relief for the Andean Community and treaty
  partners, and documentation practice. Trigger on Bolivia transfer
  pricing, partes vinculadas, precio de transferencia, SIN
  revaluation. Source-cited draft.
jurisdiction: BO
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Bolivia transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the SIN portal
(impuestos.gob.bo, SIAT) and the PwC Worldwide Tax Summaries Bolivia
corporate chapter (reviewed 21 July 2026). Currency: boliviano (BOB).

**Source status caveat:** Bolivia has **no dedicated transfer-pricing
law** confirmed in force for 2026 — the control levers are the IUE
deductibility/necessity rules (Ley 843) and the Codigo Tributario
general anti-avoidance rule (Ley 2492). Article numbers for both, and
any SIN normative resolution on related-party evidence, are
**needs-sources** (the official gazette did not resolve this pass).
Do not cite a Bolivian "arm's-length article" — there is none by that
name.

## 2. Who the rules apply to

- **Any Bolivian taxpayer (company or PE) transacting with a
  non-resident related party**: goods purchases/sales, services,
  financing, intangibles. SIN attacks the **deduction** (or the
  declared price) rather than running a formal arm's-length adjustment
  under a TP statute.
- **Exporters to affiliates**: underpricing Bolivian-source exports
  shifts source profit out of Bolivia; SIN can recompute the
  Bolivian-source base.
- **Groups paying management fees, royalties or interest abroad**:
  the 12.5% non-resident withholding applies on the gross payment
  regardless of deductibility, so an expense can be denied for IUE
  **and** still have suffered WHT.

## 3. The rules (control table)

| Lever | Content | Source |
|---|---|---|
| IUE necessity/deductibility | Deductions must be necessary for Bolivian-source income and evidenced by fiscal documentation; unsupported affiliate charges are disallowed | Ley 843 — article needs-sources; PwC Bolivia, read 2026-10-24 |
| Source principle | Bolivian-source income cannot be shifted abroad by transfer prices; SIN recomputes the Bolivian base | Ley 843 — PwC Bolivia, read 2026-10-24 |
| General anti-avoidance | Codigo Tributario GAAR allows SIN to disregard acts/forms whose sole purpose is tax avoidance | Ley 2492 — article needs-sources |
| WHT overlay | 12.5% on dividends, interest, royalties, services to non-residents (2.5% partially-performed activities) | PwC Bolivia withholding, read 2026-10-24 |
| Documentation | No statutory TP file/CbCR confirmed; fiscal documentation (factura, contracts) and on-audit evidence are the practical standard | needs-sources |

## 4. Tax base and computation

Two separate exposures on any adjustment:

1. **IUE side (25%)**: disallowed affiliate expense or underpriced
   export increases the IUE base by the adjustment amount.
2. **WHT side (12.5% gross)**: the payment itself may already have
   suffered (or should have suffered) 12.5% withholding on the gross
   amount — a disallowed expense does not refund the WHT.

Compute both. Treaty relief on the WHT layer exists only for Bolivia's
treaty network (Andean Community decisions with Colombia, Ecuador,
Peru; DTTs with Argentina, France, Germany, Spain, Sweden, UK — PwC
Bolivia, read 2026-10-24).

## 5. Deadlines

- No statutory TP-documentation deadline (none confirmed) — evidence
  must survive the audit window.
- IUE return: 120 days after fiscal year-end (see
  bolivia-corporate-income-tax).
- WHT on associate payments: monthly per the SIN vencimientos calendar
  (exact day: confirm in SIAT).
- Audit window: 4 years from 1 January after the payment due date
  (+2 years if improperly registered) — Ley 1733 amending art. 59
  Codigo Tributario, per PwC Bolivia, read 2026-10-24.

## 6. Penalties and interest

Recomputed IUE/IT runs through the Codigo Tributario regime: indexed
updatings, interest, and proportional penalties (article-level amounts
**needs-sources**). Taxpayers get 30 days to answer the preliminary
audit report; taxes must be paid to litigate in court (PwC Bolivia,
read 2026-10-24).

## 7. Worked examples

**Example 1 — underpriced export to the parent.** A Bolivian miner
exports ore to its parent for BOB 800,000 where the arm's-length price
is BOB 1,000,000. SIN recomputes the Bolivian-source base up by the
difference; IUE at 25% follows, and the IT layer keys on the higher
gross.

```oa-check
name: export underpricing uplift
inputs:
  arm_length: 1000000
  declared: 800000
  iue_rate: 25
  it_rate: 3
steps:
  - uplift: arm_length - declared
  - extra_iue: uplift * pct(1, iue_rate)
  - it_on_arm: arm_length * pct(1, it_rate)
expected:
  uplift: 200000.00
  extra_iue: 50000.00
  it_on_arm: 30000.00
```

**Example 2 — management fee disallowed but WHT already paid.** A
Bolivian company pays a BOB 300,000 management fee to a foreign
affiliate with no evidence of service. SIN disallows the deduction
(+25% IUE on the fee); the 12.5% WHT on the gross was owed regardless.

```oa-check
name: mgmt fee disallowed plus WHT
inputs:
  fee: 300000
  iue_rate: 25
  wht: 12.5
steps:
  - extra_iue: fee * pct(1, iue_rate)
  - wht_due: fee * pct(1, wht)
expected:
  extra_iue: 75000.00
  wht_due: 37500.00
```

## 8. Ask the client first

1. Which cross-border related-party flows ran in the year, at what
   prices, and is each supported by contract + fiscal documentation?
2. Were exports to affiliates priced at commodity/market benchmarks?
3. Was 12.5% WHT actually withheld on every affiliate service,
   interest and royalty payment?
4. Is the counterparty in a treaty state (Andean Community, Spain,
   Sweden, UK, etc.) and was treaty relief documented at source?

## 9. Sources

- [SIN — Servicio de Impuestos Nacionales](https://www.impuestos.gob.bo/) — read 2026-10-24.
- [SIN — SIAT](https://siat.impuestos.gob.bo/) — read 2026-10-24.
- [PwC — Bolivia withholding taxes](https://taxsummaries.pwc.com/bolivia/corporate/withholding-taxes) — read 2026-10-24 (WHT rates, treaty network).
- [PwC — Bolivia tax administration](https://taxsummaries.pwc.com/bolivia/corporate/tax-administration) — read 2026-10-24 (audit, limitation period).
- Ley 843 / Ley 2492 article texts — **needs-sources** (gazette unreachable 2026-10-24).

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
