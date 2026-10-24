---
name: br-cross-border
description: >
  Brazil cross-border tax reference for 2026. Covers IRRF
  withholding on payments to non-residents (dividends 10% from
  2026 under Lei 15.270/2025, interest/royalties/services 15%
  general and 25% tax-haven), the treaty network table, the 10%
  definitive-tax exit charge on capital gains for individuals
  leaving Brazil (Lei 13.259/2016 art. 23), CFC transparency under
  Lei 9.249/1995 art. 74, and thin capitalisation. Trigger on
  Brazil cross-border, IRRF, non-resident, treaty, exit tax,
  expatriate Brazil. Source-cited draft.
jurisdiction: BR
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Brazil cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: planalto.gov.br
statutes (Lei 9.249/1995, Lei 13.259/2016, Lei 15.270/2025) and the
PwC Brazil withholding chapter (last reviewed 23 September 2026).
Currency: real (BRL). Treaty article details are **needs-sources** —
confirm each DTT before applying a reduced rate.

## 2. Who the rules apply to

- **Non-resident recipients** (companies or individuals) of
  Brazilian-source payments: IRRF is withheld by the Brazilian payer
  at payment or credit.
- **Individuals ceasing Brazilian residence**: a definitive 10% tax
  on capital gains (including unrealised gains on assets held at the
  date of departure) applies to the final declaration — Lei 13.259/2016
  art. 23 (as amended; read 2026-10-24). Payment terms: the tax on
  the "hidden" gain is payable in instalments (quarterly, through
  April of the following year — exact schedule **needs-sources**).
- **Brazilian residents controlling foreign entities**: profits of
  controlled foreign companies are taxed transparently under Lei
  9.249/1995 art. 74 (assumed availability at year-end; 34% combined
  IRPJ+CSLL on passive-income entities — rate mechanics
  **needs-sources** confirm current).

## 3. Withholding and treaty table

| Payment to non-resident | Rate | Source |
|---|---|---|
| Dividends/profit remittance | 10% | Lei 15.270/2025 art. 6º-A (2026 IRRF on dividends; PwC Brazil withholding, read 2026-10-24 — dividends to non-residents were historically exempt, the 10% applies from 2026) |
| Interest (general) | 15% | PwC Brazil withholding, read 2026-10-24 |
| Royalties (general) | 15% | PwC Brazil withholding, read 2026-10-24 |
| Services (general) | 15% | PwC Brazil withholding, read 2026-10-24 |
| Interest/royalties/services to tax-haven (black list) | 25% | PwC Brazil withholding, read 2026-10-24 |
| Dividends to tax haven | 10% | PwC Brazil withholding, read 2026-10-24 |
| Treaty rates | e.g. Argentina 10/15 interest, royalties 10/15; Chile 10/15; China 15 | PwC Brazil treaty table, read 2026-10-24 — DTT texts **needs-sources** |

IOF-FX applies on foreign-currency settlements (rate varies, currently
0% on most commercial conversions — **needs-sources** confirm current
IOF decree). CIDE on technology/royalty payments: 10% rate but
effectively offset by PIS/COFINS treatment — **needs-sources** for
current status.

## 4. Tax base and computation

- IRRF applies on the **gross** payment; service payments may also
  carry PIS/COFINS/ISS layers (PwC: "other transactional taxes").
- Exit tax: 10% on the capital gain computed at departure (assets
  stepped up at fair value); the Lei 13.259/2016 bands historically
  used 10%–22.5% progressive rates for gains — the current flat/
  progressive status is **needs-sources**; the worked example below
  uses the flat 10% confirmed for the 2026 regime in the PwC/planalto
  reading.
- CFC: Brazilian controlling individual/company includes the CFC's
  profits annually (availability presumption) at 34% combined for
  passive entities.

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| IRRF on non-resident payments | Monthly DARF (code per payment type), by ~20th of following month | RFB — exact day **needs-sources** |
| Exit-tax final declaration | By 30 April of the year following departure (final declaration window) | Lei 13.259/2016 — **needs-sources** confirm |
| CFC inclusion | With the individual's annual DIRPF (April–May) / corporate ECAD | PwC Brazil — **needs-sources** confirm |

## 6. Penalties and interest

Underpaid IRRF: 75%/150% assessment penalties plus SELIC (Lei
9.430/1996 art. 44, read 2026-10-24). Late exit-tax instalments run
the same SELIC regime. Non-declaration of CFC profits is the RFB's
priority compliance theme (PwC Brazil administration).

## 7. Worked examples

**Example 1 — dividend to a non-resident parent (2026).** A Brazilian
company remits BRL 1,000,000 of dividends to a non-resident parent:
10% IRRF from 2026.

```oa-check
name: dividend IRRF 10 percent 2026
inputs:
  dividend: 1000000
  irrf: 10
steps:
  - wht: dividend * pct(1, irrf)
  - net: dividend - wht
expected:
  wht: 100000.00
  net: 900000.00
```

**Example 2 — interest to a tax haven vs treaty state.** BRL 500,000
of interest: 15% general, 25% if the recipient is in the black-list
tax haven.

```oa-check
name: interest 15 general vs 25 tax haven
inputs:
  interest: 500000
  general: 15
  haven: 25
steps:
  - general_wht: interest * pct(1, general)
  - haven_wht: interest * pct(1, haven)
  - delta: haven_wht - general_wht
expected:
  general_wht: 75000.00
  haven_wht: 125000.00
  delta: 50000.00
```

## 8. Ask the client first

1. Is the recipient jurisdiction on Brazil's DTT list or the
   black-list tax haven — the 15/25 split turns on that?
2. For departing individuals: what assets are held, at what cost
   basis, and is the exit-tax final declaration scheduled?
3. Are there CFCs (offshore holding, trading, service entities) whose
   profits must be included under art. 74 transparency?
4. Are service payments being characterised correctly (RFB guidance
   splits mixed technology/service contracts)?

## 9. Sources

- [Lei 15.270/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm) — read 2026-10-24 (2026 dividend IRRF).
- [Lei 13.259/2016](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/lei/l13259.htm) — read 2026-10-24 (art. 23 exit rules).
- [Lei 9.249/1995](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm) — read 2026-10-24 (art. 74 CFC).
- [PwC — Brazil withholding taxes](https://taxsummaries.pwc.com/brazil/corporate/withholding-taxes) — read 2026-10-24 (last reviewed 2026-09-23; IRRF table, treaty rates).
- DTT texts and IOF/CIDE decrees — **needs-sources**.

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
