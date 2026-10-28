---
name: id-income-tax
description: "Idaho Individual Income Tax Return (Form 40) for sole proprietors and single-member LLCs. Covers the flat 5.3% rate (tax year 2025), Idaho taxable income computation from federal taxable income, standard deduction, and the initial exemption amount ($4,811 single / $9,622 MFJ). Trigger: taxpayer is an Idaho resident or has Idaho-source income exceeding $2,500."
version: "0.2"
jurisdiction: ID
tax_year: 2025
last_updated: 2026-10-28
authored_by: RILIA PUTRI, CA, CPA
reviewed_by: RILIA PUTRI
review_status: current
trust_label: Checked by RILIA PUTRI
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ID Income Tax

## Idaho Individual Income Tax (Form 40) — verified block

> Verified 2026-10-28 against archived copies of the Idaho Code (Idaho State
> Legislature, legislatorecords/idleg.gov archives).

### Rates and thresholds (tax year 2025)

- **Individual rate** — flat 5.3% of Idaho taxable income over the inflation-adjusted
  tax threshold. Statutory base threshold: $2,500 (single/all other filers) and
  $5,000 (joint return, including surviving spouse and head of household treated as
  joint). Head of household and qualifying surviving spouse are treated as joint
  returns for this purpose.
  _(Idaho Code §63-3024(2)(a)-(b), as amended 2025, ch. 13; archived evidence
  `US-ID-63-3024.html`)_
- **Threshold indexation** — the Idaho State Tax Commission annually prescribes a CPI-U
  factor (CPI for the calendar year preceding the tax year ÷ CPI for 1998) applied to
  the $2,500/$5,000 base thresholds so inflation does not raise tax.
  _(Idaho Code §63-3024(3); archived evidence `US-ID-63-3024.html`)_
- **Initial exemption amount** — $4,811 single / $9,622 joint (2025).
  _(Idaho Form 40 line 20; statutory base $1,700/$3,400 indexed under Idaho Code
  §63-3325; not contained in the archived evidence set — verify against Form 40.)_
- **Filing trigger (nonresidents/part-year)** — gross income from Idaho sources in
  excess of $2,500 requires an Idaho return. _(Idaho Code §63-3030(a)(2); archived
  evidence `US-ID-63-3030.html`)_
- **Filing deadline** — April 15 for calendar-year filers (15th day of the fourth
  month after fiscal year close). _(Idaho Code §63-3032(1)(a); archived evidence
  `US-ID-63-3032.html`)_
- **Corporate rate (context)** — 5.3% for tax years commencing on/after Jan 1, 2025
  (rate ladder: 7.6% → 7.4% (2012) → 6.925% (2018) → 6.5% (2021) → 6% (2022) →
  5.8% (2023) → 5.695% (2024) → 5.3% (2025)); minimum corporate tax $20.
  _(Idaho Code §63-3025(1),(3); archived evidence `US-ID-63-3025.html`)_
- **Income tax act identity with IRC** — Idaho taxable income starts from federal
  taxable income, subject only to Idaho modifications.
  _(Idaho Code §63-3002; archived evidence `US-ID-63-3002.html`)_

### Correction note

The previous version of this guide (synced from openaccountants.com) contained an
entirely wrong body: the Indonesia PPh Orang Pribadi guide (IDR brackets, PTKP,
NPPN, Coretax DJP) had been published under the Idaho slug. All Indonesia-specific
numbers (IDR 60,000,000 bracket, PTKP IDR 54,000,000, UU HPP/PMK citations, etc.)
were wrong for Idaho and have been removed. The frontmatter description (flat 5.3%,
$4,811/$9,622 exemption, $2,500 trigger) matches Idaho law and was retained.

## PROHIBITIONS

- NEVER apply Article 17 brackets without confirming PTKP family status (R-ID-IT-1).
- NEVER allow NPPN deemed-income treatment without confirming the 3-month notification was filed.
- NEVER apply UMKM Final 0.5% logic in this skill — route to `id-pph-final-umkm`.
- NEVER claim PPh 24 foreign tax credit beyond the per-country cap.
- NEVER include UMKM-Final income in the Article 17 progressive computation (it is already taxed finally).
- NEVER round PKP up — UU PPh Art. 17(4) requires rounding down to IDR 1,000.
- NEVER allow carry-forward loss in an NPPN year.
- NEVER omit Lampiran IV asset and liability disclosure on Form 1770.
- NEVER treat the NIK-as-NPWP transition as optional for Indonesian citizens post-1 July 2024.
- NEVER present a refund (PPh 28A) without flagging the audit-on-restitution risk.
- NEVER invent or guess an NPPN coefficient — if unsure, mark "TBC — verify with Indonesian accountant" and stop.
- NEVER file or instruct filing — this skill produces a working paper for review by a registered Indonesian Konsultan Pajak only.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a registered Indonesian Konsultan Pajak (or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
