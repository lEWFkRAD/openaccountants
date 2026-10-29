#!/usr/bin/env python3
"""G2/G3/G4/G5 restructure for the four numbered MD pack files."""
import re, json, glob, pathlib

D = pathlib.Path("/home/jeffrey-watts/.hermes/cache/scratch/oa-pack-md/skills/us-states/md")

MAP = {
    "1. Scope and sources": "Who this applies to",
    "2. Who applies": "Rates, bands and thresholds",
    "3. Rates and base": "The taxable base",
    "4. Deadlines": "Deadlines and filing",
    "5. Penalties and interest": "Penalties and interest",
    "6. Cross-border / multistate": "Cross-border points",
    "6. Cross-border patterns": "Cross-border points",
    "6. Cross-border": "Cross-border points",
    "7. Worked examples": "Worked examples",
    "8. Ask the client": "Ask the client first",
    "9. Sources": "Sources",
}

CTA = ("**Talk to a verified accountant** — for Maryland questions on live client facts, "
       "book time with an OA Partner.")

def strip_marker_words(t):
    t = re.sub(r"\s*\*\*needs-sources\*\*", "", t)
    t = re.sub(r"\bneeds-sources\b", "", t)
    t = re.sub(r"\s+([;.,])", r"\1", t)
    t = re.sub(r"\(\s*;", "(", t)
    t = re.sub(r"\(\s*\)", "", t)
    t = re.sub(r"[ \t]+([)\n])", r"\1", t)
    t = re.sub(r"[ \t]+—(\s*$)", r"\1", t, flags=re.M)
    t = re.sub(r"—\s+([;.,])", r"\1", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    return t

def split_lead(body):
    """Return (lead_paragraphs, rest) where rest starts at first list/table/subheading."""
    bm = body.lstrip("\n")
    stop = re.search(r"(?m)^(?:[-*] |\||#)", bm)
    if not stop:
        return bm.strip(), ""
    # lead ends at the blank line before the first list item
    idx = stop.start()
    lead = bm[:idx].strip()
    rest = bm[idx:]
    return lead, rest

def make_table(lead, readon_by_url):
    hdr = "| Source | What it covers | Read on |\n|---|---|---|"
    lines = []
    for ln in lead.splitlines():
        ln = ln.strip()
        mm = re.match(r"^\d+\.\s+(.*)$", ln)
        if not mm:
            continue
        item = strip_marker_words(mm.group(1))
        um = re.search(r"<(https?://[^>]+)>", item)
        url = um.group(1) if um else ""
        if url:
            date = readon_by_url.get(url.rstrip("/"), "not archived yet")
            desc = re.split(r"<https?://", item)[0].strip().rstrip(":—- ").strip()
            lines.append(f"| {desc or item} | [{url}]({url}) | {date} |")
        else:
            lines.append(f"| {item} | internal skill reference | n/a |")
    return hdr + "\n" + "\n".join(lines)

def process(fname, not_conf, dates):
    p = D / fname
    md = p.read_text()
    m = re.match(r"\A(---\n.*?\n---\n)(.*)", md, re.S)
    fm, rest = m.group(1), m.group(2)
    parts = re.split(r"(?m)^## (.+)$", rest)
    intro = parts[0]
    secs = [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]

    out_secs = []
    for head, body in secs:
        if head.startswith("Talk to a verified accountant"):
            continue
        new = MAP[head]
        lead, rest = split_lead(body)
        if new == "Sources":
            lead = re.sub(r"<!-- openaccountants-cta-block -->.*", "", lead, flags=re.S).strip()
            body = "\n\n" + make_table(lead, dates) + "\n\nNot yet confirmed: " + not_conf + "\n"
        else:
            body = strip_marker_words(body)
        out_secs.append((new, body))

    EX = ["Who this applies to", "Rates, bands and thresholds", "The taxable base",
          "Deadlines and filing", "Penalties and interest", "Cross-border points",
          "Worked examples", "Ask the client first", "Sources", "Talk to a verified accountant"]
    have = [h for h, _ in out_secs]
    for want in EX:
        if want not in have:
            idx = len(out_secs)
            for w2 in EX[EX.index(want) + 1:]:
                if w2 in have:
                    idx = have.index(w2)
                    break
            out_secs.insert(idx, (want, "\nNo Maryland-specific rule was found in the sources read for this topic.\n"))
            have = [h for h, _ in out_secs]

    body_md = intro.rstrip() + "\n"
    for h, b in out_secs:
        body_md += f"\n## {h}\n{b.rstrip()}\n"
    body_md += f"\n<!-- openaccountants-cta-block -->\n\n## Talk to a verified accountant\n\n{CTA}\n"
    p.write_text(fm + body_md)
    print("rewrote", fname)

dates = {}
for j in glob.glob("/home/jeffrey-watts/oa-correction-evidence/sources/US-MD-*.json"):
    s = json.load(open(j))
    d = s["retrieved_at"][:10]
    for k in ("requested_url", "final_url"):
        if s.get(k):
            dates[s[k].rstrip("/")] = d

process("md-corporate-income-tax.md",
        "the statute text behind Tax-General §7-204 (corporate rate citation) and §13-701 "
        "(late-filing penalty percentage) — the 8.25% rate itself is confirmed in the archived "
        "Tax-General §10-106(b)(1) and the 2024 Corporation Tax Booklet.",
        dates)
process("md-cross-border.md",
        "the 2025 Form 505 instruction PDF (404 on 2026-10-27), the Tax-General §10-106.1 statute "
        "text for the 2.25% Special Nonresident Tax, the MW506NRS waiver mechanics, the current "
        "MW507B reciprocity form number, and the §13-701 penalty percentage.",
        dates)
process("md-social-contributions.md",
        "the FAMLI contribution-rate percentage (the published rate page 404'd on 2026-10-27) and "
        "the FAMLI penalty schedule (regulations page not fetched).",
        dates)
process("md-transfer-pricing.md",
        "the COMAR 03.04.08 regulation text (cited inside the booklet, not independently fetched), "
        "the Tax-General §7-401 et seq. and §7-404 statute text, the deadline for "
        "alternative-apportionment or separate-accounting requests, and the §13-701 penalty percentage.",
        dates)
