---
name: chile-transfer-pricing
description: >
  Chile transfer pricing reference for 2026. Covers the arm's-length
  regime of Art. 41 bis LIR (OECD-aligned, introduced by Ley
  21.210/2020), the accepted methods, the 3:1 thin-capitalisation
  rule that bites when related debt bears interest below the 35%
  withholding rate, related-party definitions, documentation and
  the SII audit/revaluation route, and the interaction with the
  30% royalty and 35% interest withholding rates. Trigger on Chile
  transfer pricing, precios de transferencia, Art. 41 bis, thin
  capitalisation, partes relacionadas. Source-cited draft.
jurisdiction: CL
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Chile transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the PwC Chile
corporate withholding chapter (last reviewed 19 December 2025), which
confirms the 3:1 thin-capitalisation rule and the WHT rates the TP
regime interacts with, plus the existing `cl-corporate-income-tax`
skill for the FCT mechanics.

**Source status caveat:** Chile's arm's-length rule sits in **Art. 41
bis LIR**, introduced by Ley 21.210 (2020) and OECD-aligned. The
statute text could not be fetched this pass (leychile.cl serves a JS
shell; the SII transfer-pricing sub-pages did not resolve), so the
method list, documentation thresholds and procedural articles below
are **needs-sources** — treat them as the standard OECD-aligned
framework Chile adopted, and confirm against Art. 41 bis LIR and SII
Resolutions before citing an article number in client work.

## 2. Who the rules apply to

- **Resident taxpayers (FCT taxpayers) transacting with related
  parties abroad** — related parties include entities under common
  control, branches/permanent establishments, and the treaty-defined
  relationships; Chile's definition also reaches certain transactions
  with low-tax regimes even without a relationship (**needs-sources**
  confirm the current scope list).
- **Inbound**: Chilean payers deducting interest, royalties or
  services charged by foreign related parties.
- **Outbound**: Chilean exporters/licensors to affiliates — the FCT
  base is worldwide, so underpricing Chilean-side functions shifts
  profit within the group, not out of Chile's net-tax base, but the
  WHT layer still prices the flow.

## 3. Rules table

| Rule | Content | Source |
|---|---|---|
| Arm's-length standard | Art. 41 bis LIR (Ley 21.210/2020): related-party transactions priced as independent parties; OECD methods (CUP, resale price, cost-plus, TNMM, profit split) | statute text **needs-sources**; framework per Ley 21.210 |
| Thin capitalisation | 3:1 debt-to-equity; interest on related debt above the ratio is recharacterised (and the rule bites when the interest bears a WHT rate lower than the general 35%) | PwC Chile withholding, read 2026-10-24 |
| WHT overlay | Interest 35% general (4% for foreign-bank loans); royalties 30% (software +15% additional unless standard); services 35% | PwC Chile withholding, read 2026-10-24 |
| Documentation | Master/local file and TP affidavit regime per SII resolutions — thresholds and forms **needs-sources** | needs-sources |
| Advance pricing | APA route exists under Art. 41 bis — procedure **needs-sources** | needs-sources |

## 4. Tax base and computation

An SII revaluation adjusts the FCT base (27% PIS / 25% pro-Pyme) by
the difference between the declared and arm's-length price. The
withholding layer is separate: recharacterised interest or inflated
royalties may also have under-withheld 30%/35% WHT on the gross.
Thin-cap interest denial: interest on related debt beyond 3:1 is
non-deductible (and typically recharacterised as a dividend, which in
the PIS chain carries the additional-tax WHT with the 65% FCT credit —
see chile-cross-border).

## 5. Deadlines

- TP affidavit (declaracion jurada de precios de transferencia):
  filed with the April Operacion Renta cycle — exact form/deadline
  **needs-sources**.
- FCT provisional payments (PPM) monthly; annual FCT return with Form
  22 before 30 April (PwC Chile tax administration, read 2026-10-24).
- Audit window: 3 years, extended to 6 where no return was filed or
  the return was maliciously false (PwC Chile, read 2026-10-24).

## 6. Penalties and interest

Underpaid FCT/WHT from a revaluation runs Art. 97 CT penalties plus
promedio interest (percentages **needs-sources**). Ley 21.713 (2024)
added SII anti-evasion tools including the anonymous-informant regime
(PwC Chile tax administration, read 2026-10-24).

## 7. Worked examples

**Example 1 — inflated royalty to the parent.** A Chilean licensee
pays CLP 400,000 where the arm's-length royalty is CLP 600,000 — the
SII uplifts the FCT base by the difference (27% PIS).

```oa-check
name: royalty underpayment FCT uplift
inputs:
  paid: 400000
  arm_length: 600000
  fct: 27
steps:
  - uplift: arm_length - paid
  - extra_fct: uplift * pct(1, fct)
expected:
  uplift: 200000.00
  extra_fct: 54000.00
```

**Example 2 — thin-capitalisation interest denial.** A Chilean company
with CLP 200,000 equity carries CLP 900,000 related-party debt at 10%;
the 3:1 ratio caps deductible related debt at CLP 600,000, so interest
on the CLP 300,000 excess is denied (FCT 27% add-back).

```oa-check
name: thin cap 3 to 1 interest denial
inputs:
  debt: 900000
  equity: 200000
  ratio: 3
  rate: 10
  fct: 27
steps:
  - max_debt: equity * ratio
  - excess_debt: debt - max_debt
  - denied_interest: excess_debt * pct(1, rate)
  - extra_fct: denied_interest * pct(1, fct)
expected:
  max_debt: 600000.00
  excess_debt: 300000.00
  denied_interest: 30000.00
  extra_fct: 8100.00
```

## 8. Ask the client first

1. Which related-party flows (goods, services, interest, royalties)
   ran in the year, and is each benchmarked?
2. Is related debt within 3:1, and does its interest bear 35% WHT or
   a treaty/4% rate (the thin-cap trigger)?
3. Was the TP affidavit filed with the April return, and are master/
   local files current?
4. Are software royalties split correctly (standard vs customised —
   the +15% additional turns on that)?

## 9. Sources

- [PwC — Chile withholding taxes](https://taxsummaries.pwc.com/chile/corporate/withholding-taxes) — read 2026-10-24 (3:1 thin cap, WHT rates, treaty table).
- [PwC — Chile tax administration](https://taxsummaries.pwc.com/chile/corporate/tax-administration) — read 2026-10-24 (deadlines, limitation, Ley 21.713).
- [SII — home](https://www.sii.cl/) — read 2026-10-24 (TP sub-pages unreachable this pass).
- Art. 41 bis LIR / Ley 21.210 text, SII TP resolutions, Art. 97 CT percentages — **needs-sources**.

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
