---
name: br-social-contributions
description: >
  Brazil employer social contributions reference for 2026. Covers
  the 20% employer INSS payroll contribution (Lei 8.212/1991 art.
  22), RAT (1%–3% by risk grade, multiplied by the FAP factor), the
  ~5.8% "third-party" system-s contributions (SESI/SESC/SENAI/SEBRAE
  and salary-education), employee INSS progressive to 14% capped at
  the teto, FGTS 8% monthly deposit (Lei 8.036/1990 art. 15), and
  the CPRB revenue-based substitute where applicable. Trigger on
  Brazil payroll contributions, contribuicao patronal, INSS
  employer, RAT, terceiros, FGTS. Source-cited draft.
jurisdiction: BR
category: social
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Brazil employer social contributions

## 1. Scope and sources

Source-cited draft, sources read 24 October 2024: Lei 8.212/1991
consolidated (funding), Lei 8.036/1990 consolidated (FGTS), Lei
7.689/1988 (CSLL context), plus the accountant-reviewed `br-inss`
skill for the 2026 teto/minimum figures and the PwC Brazil chapter.
Currency: real (BRL). This skill is the **employer/patronal** side;
the self-employed side is in `br-inss`, wage IRRF is in
`brazil-payroll`.

## 2. Who the rules apply to

- **Every employer (pessoa juridica) with employees**: pays the
  patronal contribution on gross payroll (remuneracao de contribuicao
  — CLT arts. 457–458 scope, including 13th salary and paid vacation).
- **Construction and listed sectors** may instead owe CPRB on gross
  revenue (Lei 12.546/2011 arts. 7–9, as extended/amended by Lei
  14.973/2024 — current scope and rates **needs-sources**).
- **Agroindustry**: 2.5% + 0.1% on gross production revenue in place
  of payroll-based contribution (Lei 8.212/1991 art. 22A, read
  2026-10-24).
- **Simples Nacional** employers pay INSS inside the DAS — outside
  this skill's tables.

## 3. Rates table

| Contribution | Rate | Base | Source |
|---|---|---|---|
| Employer INSS (patronal) | 20% | Gross monthly payroll | Lei 8.212/1991 art. 22 I, read 2026-10-24 |
| RAT (workplace accident risk) | 1% / 2% / 3% by risk grade, x FAP factor | Gross monthly payroll | Lei 8.212/1991 art. 22 II (as amended Lei 9.732/1998) — rate table **needs-sources** confirm current FAP decree |
| Third-party system-s (Sistema S + salary-education) | approx 5.8% total (1.2% SESC/SES I, 1.2% SENAI/SES II, 0.2% SESI/SESC III, 0.4% SEBRAE, 2.5% SENAR where applicable, 1.0% salary-education) | Gross monthly payroll | Lei 8.212/1991 art. 3 and system statutes — exact per-entity list **needs-sources** |
| Employee INSS | progressive 7.5%–14%, capped at teto R$ 8,475.55 (2026) | Gross wage | br-inss (reviewed; Portaria Interministerial MPS/MF nº 13/2026) |
| FGTS | 8% | Monthly remuneration incl. 13th | Lei 8.036/1990 art. 15, read 2026-10-24 |
| FGTS penalty on dismissal | 40% of accumulated FGTS | Severance context | Lei 8.036/1990 art. 18, **needs-sources** confirm current |

## 4. Tax base and computation

Payroll base = total remuneration (salary, commissions, bonuses,
13th, vacation pay, notice). Non-salary items (meal allowance under
PAT, transport allowance) are excluded when the program rules are met
(**needs-sources** for current PAT limits). The eSocial/DCTFWeb
workflow computes the contribution from digital payroll records; the
employer's DARF (code per Receita table) consolidates INSS+RAT+system-s.

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| eSocial payroll events | Per event calendar (monthly payroll by ~7th–15th of following month) | eSocial/RFB — exact current calendar **needs-sources** |
| DCTFWeb + DARF payment (patronal) | 20th of the month following the competency | RFB normative — **needs-sources** confirm current day |
| FGTS (FGTS Digital) | 7th of the month following the competency | Lei 8.036/1990 art. 15 ("ate o dia 7"), read 2026-10-24 |
| GPS (self-employed, legacy) | 15th of following month | br-inss (reviewed) |

## 6. Penalties and interest

Late patronal payment: 0.33% per day capped at 20% plus SELIC (br-inss
reviewed block, Lei 8.212/1991; Lei 9.430/1996). Assessment-of-office
underpayment: 75% / 150% fraud (Lei 9.430/1996 art. 44, read
2026-10-24). Retroactive collection window: 5 years (CTN arts.
173–174, per br-inss).

## 7. Worked examples

**Example 1 — monthly employer burden.** A company with BRL 100,000
gross payroll (medium risk RAT 2%, standard system-s 5.8%):

```oa-check
name: employer monthly burden
inputs:
  payroll: 100000
  inss: 20
  rat: 2
  terceiros: 5.8
  fgts: 8
steps:
  - inss: payroll * pct(1, inss)
  - rat: payroll * pct(1, rat)
  - terceiros: payroll * pct(1, terceiros)
  - fgts: payroll * pct(1, fgts)
  - total: inss + rat + terceiros + fgts
expected:
  inss: 20000.00
  rat: 2000.00
  terceiros: 5800.00
  fgts: 8000.00
  total: 35800.00
```

**Example 2 — employee INSS at the teto (2026).** The 14% top band
applies only to wages up to the teto R$ 8,475.55, so the maximum
employee INSS deduction is 14% of the teto:

```oa-check
name: employee INSS ceiling 2026
inputs:
  teto: 8475.55
  top_rate: 14
steps:
  - max_inss: teto * pct(1, top_rate)
expected:
  max_inss: 1186.58
```

(tolerance widened below because the ceiling is rounded to cents)

```oa-check
name: employee INSS ceiling rounded
tolerance: 1
inputs:
  teto: 8475.55
  top_rate: 14
steps:
  - max_inss: teto * pct(1, top_rate)
expected:
  max_inss: 1187.00
```

## 8. Ask the client first

1. What is the company's risk grade (RAT) and current FAP factor?
2. Is the entity in a CPRB sector (revenue-based) or Simples Nacional
   (DAS) instead of the payroll tables above?
3. Are eSocial events and DCTFWeb reconciled to payroll, and is FGTS
   Digital payment current?
4. Any exempt/non-salary benefits (PAT, transport) being excluded
   correctly?

## 9. Sources

- [Lei 8.212/1991 consolidated](https://www.planalto.gov.br/ccivil_03/leis/l8212cons.htm) — read 2026-10-24 (arts. 22, 22A).
- [Lei 8.036/1990 consolidated (FGTS)](https://www.planalto.gov.br/ccivil_03/leis/L8036consol.htm) — read 2026-10-24 (art. 15).
- [Receita Federal do Brasil](https://www.gov.br/receitafederal/pt-br) — read 2026-10-24.
- Existing reviewed pack skill `br-inss` — 2026 teto/minimum figures with their citations (Portaria MPS/MF nº 13/2026).
- [PwC — Brazil](https://taxsummaries.pwc.com/brazil/corporate) — read 2026-10-24.

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
