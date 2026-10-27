---
name: pr-transfer-pricing
description: >
  Puerto Rico transfer pricing reference for 2026. Thin source-cited draft: the Code 1-2011 taxes related-party interest at 29 percent (sections 1091.01, 1092.01, read from the OGP May 2026 revision), defines controlled groups (1010.04) and related entities (1010.05), and carries an anti-abuse rule in the corporate AMT (1022.03(e)); the Code's dedicated transfer-pricing section number and documentation rules are needs-sources. Trigger on Puerto Rico transfer pricing, partes relacionadas PR, precios de transferencia. Source-cited draft, needs-sources.
jurisdiction: PR
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Puerto Rico transfer pricing

## 1. Scope and sources

Source-cited draft with a real gap: the OGP consolidated PDF of the
Código de Rentas Internas de Puerto Rico de 2011 (rev. 28 May 2026) was
read directly, but the dedicated transfer-pricing section of the Code was
not located in the text searched, and its section number and
documentation requirements are needs-sources. What follows is anchored in
the sections that were read.

## 2. Who applies

Related parties under the Code: controlled groups of corporations
(80% vote/value tests, §1010.04, read) and groups of related entities
(§1010.05, read). Any PR taxpayer allocating income or deductions with a
related party — including US-mainland affiliates, which are foreign for
PR income-tax purposes — is in scope.

## 3. Rates and standards

| Item | Amount | Source |
|---|---|---|
| Related-party interest received by non-resident individuals / foreign corporations | 29% (not the portfolio 10%) | §§1091.01(a)(1)(i), 1092.01(a)(1)(i) (read) |
| Corporate AMT anti-abuse: transactions with a principal tax-avoidance purpose disregarded for the tentative minimum tax | 50%-100% special administrative penalty on underpayment | §1022.03(e) area (read) |
| Arm's-length standard and documentation | Code section number needs-sources | Code Subtítulo (needs-sources) |

## 4. Base and timing

The related-party interest rule shows the Code's method: reclassify
related-party flows and tax them at the flat non-resident rate rather
than the portfolio rate. The general arm's-length base rules and any
contemporaneous documentation requirement are needs-sources.

## 5. Deadlines

Any PR transfer-pricing disclosure or informative return rides with the
annual return: 15 April calendar-year (§1061.16, read), 3-month automatic
extension available (read). Whether a separate TP informative return
exists: needs-sources.

## 6. Penalties and interest

Underpayment interest 10% annually (§6030.01, read); failure-to-file 5%
plus 10% per 30-day period (§6030.11, read); the special administrative
penalty of 50%-100% of the tax owed applies where the Secretary finds the
taxpayer priced below comparable competitors without a good-faith
explanation (read from the penalties subtitle).

## 7. Cross-border interactions

The US-mainland/PR boundary is the dominant related-party flow: a US
parent licensing intangibles to a PR subsidiary, or a PR company
borrowing from its US affiliate, hits the 29% related-party interest rule
and the corporate surtax/AMT anti-abuse net. Act 60/20 (now Act 138-2022
export-services decree) companies must keep decree substance separate
from affiliate pricing (decree citations needs-sources).

## 8. Worked examples

A foreign related corporation lends its PR subsidiary and receives
USD 200,000 of PR-source interest. Because the lender is a related
person, the 29% rate applies rather than the 10% portfolio rate
(§1092.01(a)(1)(i), read):

```oa-check
name: related-party interest 29 percent on 200000
inputs:
  interes: 200000
  tasa: 0.29
steps:
  - contribucion: interes * tasa
expected:
  contribucion: 58000.00
```

A PR regular corporation underprices affiliate services and the Secretary
finds it charged less than comparable competitors without proving good
faith: the special administrative penalty runs 50%-100% of the tax owed
(read) — on a USD 40,000 deficiency that is USD 20,000 to USD 40,000:

```oa-check
name: special penalty 50 to 100 percent on 40000 deficiency
inputs:
  deficiencia: 40000
  min: 0.5
  max: 1.0
steps:
  - penalidad_min: deficiencia * min
  - penalidad_max: deficiencia * max
expected:
  penalidad_min: 20000.00
  penalidad_max: 40000.00
```

## 9. Ask the client / sources

Ask: Which affiliates touch PR entities (mainland parents, decree
companies)? Are intercompany interest flows screened against the 29%
related-party rule? Is there contemporaneous pricing support for
affiliate services and intangibles? Decree companies: substance files
current?

Sources: OGP consolidated Code PDF (read 2026-10-27). Needs-sources: the
Code's dedicated transfer-pricing section and documentation rules,
decree (Act 60/20, Act 138-2022) interaction text, Treasury/Hacienda
regulations.

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
