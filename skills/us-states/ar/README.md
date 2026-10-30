---
jurisdiction: US-AR
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  SC: ar-unemployment-contributions
  PR: ar-payroll-withholding
---

# Arkansas (US-AR) pack

Jurisdiction: Arkansas, United States. Tax year 2026. Pack drafted 2026-10-27 (source-cited drafts, tier 2).

Arkansas modernized its corporate income tax with **SB 567 / Act 719 of 2025** (signed 2025-04-16): the Act amends Arkansas' adoption of UDITPA, adopts **market-based sourcing for sales of services and intangibles**, and establishes an **economic nexus filing threshold for non-resident corporations and partnerships** (all read from the DFA Corporation Income Tax page, 2026-10-27). The corporate rate itself was reduced by the same reform; the current percentage could not be read from an official page from this host this run and carries **needs-sources**. Corporations file AR-1100 (with AR-1100ADJ adjustment schedule) and AR-1100S; withholding runs through the DFA Withholding Tax Branch, which also administers corporate (Sub-S) withholding and the pass-through entity tax. Unemployment is administered by the Division of Workforce Services (workservices.arkansas.gov -- unreachable from this host this run). Individuals pay a post-2018 flat income tax (see `ar-income-tax`).

## applicable

- `IT-IND` -- individual income tax -- present: `ar-income-tax.md`
- `IT-CORP` -- corporate income tax (AR-1100; SB 567 reform) -- drafted: `ar-corporate-income-tax.md`
- `VAT` -- sales & use tax -- present: `arkansas-sales-tax.md`
- `SC` -- social contributions (UI via Division of Workforce Services) -- drafted: `ar-unemployment-contributions.md`
- `PR` -- payroll withholding (DFA Withholding Tax Branch, PET) -- drafted: `ar-payroll-withholding.md`
- `TP` -- transfer pricing / market-based sourcing / combined filing -- drafted: `ar-transfer-pricing.md`
- `XB` -- cross-border / economic nexus (SB 567) -- drafted: `ar-cross-border.md`

## not_applicable

- none -- Arkansas has income, corporate, sales, payroll, and social-contribution regimes; all
  pilot domains apply.

## Source status

- DFA Corporation Income Tax page: verified 2026-10-27 (dfa.arkansas.gov, 200, text read -- SB 567/Act 719 of 2025 signed 2025-04-16; UDITPA amendment; market-based sourcing for services and intangibles; economic nexus threshold for non-resident corporations/partnerships; AR-1100/AR-1100S/AR-1100ADJ forms dated 2026-01-08 located via DFA search).
- DFA Withholding Tax Branch page: verified 2026-10-27 (200, text read -- corporate (Sub-S) withholding, pass-through entity tax, composite filing, ATAP e-file).
- **Corporate rate percentage: needs-sources** -- arkleg.state.ar.us returns empty bodies / 500s from this host; the Act 719 PDF downloaded 0 bytes. Confirm the current rate against the AR-1100 instructions before publishing figures.
- Division of Workforce Services (workservices.arkansas.gov): DNS did not resolve from this host -- UI figures **needs-sources**.
- Ark. Code Ann. title 26: not retrievable this run -- statutory section text **needs-sources**.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | ar-income-tax | existing (pre-pilot) |
| IT-CORP, corporate income tax | ar-corporate-income-tax | source-cited draft (rate needs-sources) |
| VAT / GST / sales tax | arkansas-sales-tax | existing (pre-pilot) |
| SC, social contributions | ar-unemployment-contributions | source-cited draft (figures needs-sources) |
| PR, payroll withholding | ar-payroll-withholding | source-cited draft |
| TP, transfer pricing | ar-transfer-pricing | source-cited draft |
| XB, cross-border | ar-cross-border | source-cited draft |

## Official sources

- DFA Corporation Income Tax: https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/ (read 2026-10-27)
- DFA Withholding Tax Branch: https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/withholding-tax-branch/ (read 2026-10-27)
- Arkansas Taxpayer Access Point (ATAP): linked from DFA pages (read 2026-10-27)
- Act 719 of 2025 (SB 567): https://www.arkleg.state.ar.us/Acts/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf (200 but 0 bytes from this host -- **needs-sources**)
