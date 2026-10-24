---
name: cr-cross-border
description: >
  Use this skill whenever asked about Costa Rica cross-border taxation — territorial source principle, outbound withholding on dividends/interest/royalties (remesas), the narrow treaty network, permanent-establishment rules, and repatriation. Trigger on phrases like "remesas Costa Rica retención", "dividendo a no residente Costa Rica", "renta de fuente costarricense", "convenio doble tributación Costa Rica", "establecimiento permanente Costa Rica", "territorial tax Costa Rica". Tax year 2026 draft; current WHT rates carry PwC citations, pre-2019 statutory rates verified in the as-enacted LIR text.
jurisdiction: CR
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Costa Rica cross-border taxation

## 1. Who applies

- **Residents** — taxed on Costa Rica-source income only: Costa Rica is a **territorial** system (LIR arts. 1–2, 8; verified in the as-enacted text on official mirrors).
- **Non-residents** — taxed on CR-source income, almost entirely through final withholding on remittances (LIR Título IV, arts. 199 et seq.).
- **Foreign companies** — taxed through a permanent establishment (establecimiento permanente: fixed place, office, factory, mine, etc. — definition verified in the as-enacted LIR text).

## 2. Rates and thresholds

Outbound withholding on remittances to non-residents (current rates per PwC, read 2026-10-24; the pre-2019 statutory rates 15% dividends / 25% royalties-technical / 30% other are verified in the as-enacted LIR text):

| Remittance | Current WHT |
|---|---|
| Dividends — qualifying ≥20% intercompany | 5% (exemption phase-in history noted by PwC) |
| Dividends — other cases | 15% |
| Interest / financial expenses | 5.5%–15% |
| Technical services, management fees, royalties, patents, franchises | 25% |
| Transportation/communications | 8.5% |
| Other CR-source income | 30% |

Treaty network is narrow: Germany, Canada, Spain, Dominican Republic, Ecuador, Mexico, Chile (status/dates vary) — **verify each instrument** before applying a reduced rate.

## 3. Base

- Source: income is CR-source when the activity is carried out in Costa Rica or the payer is a CR resident/entity (LIR arts. 9–10).
- Withholding is **final** for non-residents on most categories — no annual return needed unless the recipient elects otherwise.
- Exports are outside the territorial base.

## 4. Deadlines

- Monthly remittance withholding (D-163) via TRIBU-CR, generally by the 15th of the following month — confirm the current DGT resolution (**needs-sources**).
- Treaty relief: certificate of residence + DGT procedure before applying a reduced rate.

## 5. Penalties and interest

- Failure to withhold: the payer is jointly liable for the tax plus Ley 4755 fines and interest.
- Late monthly return: Ley 4755 late-filing fine (1% of monthly income, min 25% base salary).

## 6. Cross-border

- MAP only with treaty partners; no treaty with the US or Colombia — statutory rates govern those flows.
- TP rules apply to all related-party remittances — see `cr-transfer-pricing`.
- Repatriating profits: dividend WHT (5%/15%) is the main cost; profit capitalised and reinvested is not remitted until distributed.

## 7. Worked examples

**Example 1 — dividend to a non-treaty parent (other case).**

```oa-check
name: Dividend CRC 20,000,000 at 15%
inputs:
  dividend: 20000000
steps:
  - wht: dividend * 0.15
expected:
  wht: 3000000
```

**Example 2 — interest remittance at 15%.**

```oa-check
name: Interest CRC 10,000,000 at 15%
inputs:
  interest: 10000000
steps:
  - wht: interest * 0.15
expected:
  wht: 1500000
```

**Example 3 — royalty remittance at 25%.**

```oa-check
name: Royalty CRC 10,000,000 at 25%
inputs:
  royalty: 10000000
steps:
  - wht: royalty * 0.25
expected:
  wht: 2500000
```

## 8. Ask the client

1. Residence of the recipient and whether a Costa Rican treaty applies (which one, in force?).
2. Characterisation of the remittance — dividend, interest, royalty, technical service?
3. Does the ≥20% intercompany dividend condition hold?
4. Is there a permanent establishment risk for the foreign supplier?
5. Monthly D-163 filings current?

## 9. Sources

- [Ley 7092 LIR as-enacted PDF — COMEX mirror](https://www.comex.go.cr/media/1894/ley_7092.pdf) / [MEP mirror](https://www.mep.go.cr/sites/default/files/2024-12/3LeyImpestoRentaN%C2%B07092.pdf) — verified resolving 2026-10-24; Título IV rates (15%/25%/30%) and PE definition verified in extracted text.
- [PwC Tax Summaries — Costa Rica withholding](https://taxsummaries.pwc.com/costa-rica/corporate/withholding-taxes) — read 2026-10-24 (current 5/15, 5.5/15, 25, 8.5, 30 schedule).
- Consolidated LIR text and DGT resolutions — **needs-sources** (SCIJ JS-rendered; hacienda.go.cr unreachable 2026-10-24).

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
