#!/usr/bin/env python3
"""G2/G3/G4/G5 fix for md-income-tax.md: exemplar headings + Sources table."""
import re, pathlib

p = pathlib.Path("/home/jeffrey-watts/.hermes/cache/scratch/oa-pack-md/skills/us-states/md/md-income-tax.md")
md = p.read_text()
m = re.match(r"\A(---\n.*?\n---\n)(.*)", md, re.S)
fm, rest = m.group(1), m.group(2)
parts = re.split(r"(?m)^## (.+)$", rest)
intro = parts[0].rstrip()
secs = [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]

EX = ["Who this applies to", "Rates, bands and thresholds", "The taxable base",
      "Deadlines and filing", "Penalties and interest", "Cross-border points",
      "Worked examples", "Ask the client first", "Sources", "Talk to a verified accountant"]

RENAME = {
    "Rates and figures": "Rates, bands and thresholds",
    "Worked cases": "Worked examples",
    "Filing and payment steps with deadlines": "Deadlines and filing",
}

ask_body = next(b for h, b in secs if h == "Ask the client first")
we_body = next(b for h, b in secs if h == "Worked cases")
talk_body = next(b for h, b in secs if h == "Talk to a verified accountant")
ask_body = next(b for h, b in secs if h == "Ask the client first")

out = [(RENAME.get(h, h), b) for h, b in secs if h not in ("Ask the client first", "Talk to a verified accountant")]

def insert(want, body):
    have = [h for h, _ in out]
    idx = len(out)
    for w2 in EX[EX.index(want) + 1:]:
        if w2 in have:
            idx = have.index(w2)
            break
    out.insert(idx, (want, body))


insert("Who this applies to", """
Full-year Maryland residents filing Form 502, including sole proprietors, single-member LLC owners, employees and investors. Part-year and nonresident (Form 505) filers, fiduciaries and pass-through entities (Form 510/511) are out of scope - see "When to refuse or refer".
""")


insert("The taxable base", """
Maryland starts from federal adjusted gross income (Form 502 Line 1), not federal taxable income: the federal standard deduction and the section 199A (QBI) deduction never reduce Maryland income. Add Maryland additions (Lines 2-6, e.g. non-Maryland bond interest and Form 500DM decoupling add-backs) and subtract Maryland subtractions (Lines 8-15, e.g. Social Security, the pension exclusion, U.S. obligation interest, the two-income subtraction) to get Maryland AGI (Line 16); subtract the standard or itemized deduction and personal exemptions to get Maryland taxable net income (Line 20), which is also the base for the county tax.
""")

insert("Penalties and interest", """
The Comptroller may assess a penalty of up to 10% for failing to pay tax or file a return when due, plus interest (10.8133% a year for 2025 balances paid between 15 April 2026 and 1 January 2027). Underpayment of 2025 estimated tax caused by the 2025 rate increases has interest waived. Refunds must be claimed within three years of the original due date. Details sit under "Deadlines and filing" and "Tax year 2025 returns" below.
""")

insert("Cross-border points", """
Full-year residents are covered here; nonresidents and part-year filers (Form 505, the 2.25% Special Nonresident Tax, DC/PA/VA/WV reciprocity) are handled in the `md-cross-border` skill. Credit for tax paid to another state or locality goes on Form 502CR with the other state's return attached.
""")



out = [(h,b) for h,b in out if h != "Worked examples"]
insert("Worked examples", we_body)
insert("Ask the client first", ask_body)

src = """
| Source | What it covers | Read on |
|---|---|---|
| Md. Code, Tax-General § 10-105 (rate schedules, 2% capital gains surtax) | [https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false) | 2026-10-28 |
| Md. Code, Tax-General § 10-106 (county income tax floor and cap) | [https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-106&enactments=false](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-106&enactments=false) | 2026-10-28 |
| Md. Code, Tax-General § 10-301 (taxable-year and filing-base definitions) | [https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-301&enactments=false](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-301&enactments=false) | 2026-10-28 |
| Md. Code, Tax-General § 11-203 (credit for tax paid to other states) | [https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gti&section=11-203&enactments=false](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gti&section=11-203&enactments=false) | 2026-10-28 |
| Comptroller of Maryland, 2025 resident booklet | [https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf) | not archived yet |
| Comptroller of Maryland, 2026 estimated-tax (PV) worksheet | [https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf) | not archived yet |
| Comptroller of Maryland, Technical Bulletin 58 (capital gains surtax) | [https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf) | not archived yet |
| Comptroller of Maryland, Tax Alert on 2025 legislative changes | [https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-changes-to-standard-and-itemized-deductions-and-to-state-and-local-income-tax-rates-from-the-2025-legislative-session.pdf](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-changes-to-standard-and-itemized-deductions-and-to-state-and-local-income-tax-rates-from-the-2025-legislative-session.pdf) | not archived yet |
| Comptroller of Maryland, 2025 nonresident booklet | [https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/nonresident-booklet.pdf](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/nonresident-booklet.pdf) | not archived yet |
| Comptroller of Maryland, 2026 employer withholding guide (PM-225) | [https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/withholding/2026/pm225.pdf](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/withholding/2026/pm225.pdf) | not archived yet |
| Md. Code, Tax-General §§ 10-211, 10-217, 10-218 (exemptions, standard and itemized deductions) | statute text quoted in the sections above | not archived yet |

Not yet confirmed: the final indexed 2026 standard deduction and pension-exclusion amounts (the Comptroller had not published the 2026 resident instructions when this skill was written), the 2026 final county-rate confirmations beyond the PV worksheet, and archived copies of the Comptroller booklets, worksheets, Tax Alert and Technical Bulletin 58 cited above (only the four mgaleg statute pages are archived so far).
"""
out.append(("Sources", src))

body = intro + "\n"
for h, b in out:
    body += f"\n## {h}\n{b.rstrip()}\n"
body += "\n<!-- openaccountants-cta-block -->\n\n## Talk to a verified accountant\n" + talk_body.rstrip() + "\n"
p.write_text(fm + body)
print("done")
