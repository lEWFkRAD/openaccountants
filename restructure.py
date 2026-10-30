#!/usr/bin/env python3
"""Move conform-stub content into exemplar headings for 4 CA files."""
import re, sys

D = "skills/us-states/ca/"
EXEMPLAR = ["Who this applies to", "Rates, bands and thresholds", "The taxable base", "Deadlines and filing",
            "Penalties and interest", "Cross-border points", "Worked examples", "Ask the client first",
            "Sources", "Talk to a verified accountant"]

def sections(md):
    """Return (preamble, [(head, body)]) for ## and ### headings, in order."""
    m = re.match(r"\A(---\n.*?\n---\n)", md, re.S)
    fm = m.group(1) if m else ""
    rest = md[len(fm):]
    parts = re.split(r"(?m)^(##|###) (.+)$", rest)
    pre = parts[0]
    secs = [(parts[i + 1].strip(), parts[i + 2]) for i in range(1, len(parts), 3)]
    return fm, pre, secs

def demote(body):
    """Demote ### -> #### inside a moved body."""
    return re.sub(r"(?m)^### ", "#### ", body)

def get(secs, pred):
    out = []
    for h, b in secs:
        if pred(h):
            out.append((h, b))
    return out

def one(secs, pat):
    r = get(secs, lambda h: re.search(pat, h))
    assert len(r) == 1, (pat, [h for h, _ in r])
    return r[0][1]

def join(*parts):
    return "\n" + "\n".join(p.strip("\n") for p in parts if p.strip()) + "\n"

def process(fname, mapping):
    md = open(D + fname).read()
    fm, pre, secs = sections(md)
    used = set()
    def body(pat):
        r = one(secs, pat)
        used.add(pat)
        return demote(r)
    blocks = {}
    for head, pats in mapping.items():
        blocks[head] = join(*[body(p) for p in pats])
    # leftover ## sections (keep as-is, demoted)
    leftovers = [(h, b) for h, b in secs if not any(re.search(p, h) for p in mapping_pats)]
    return fm, pre, blocks, leftovers

# ---- per-file mapping ----
CORP = {
 "Rates, bands and thresholds": [r"^Rates$"],
 "The taxable base": [r"^Base and timing$"],
 "Deadlines and filing": [r"^Deadlines"],
 "Penalties and interest": [r"^Penalties and interest$"],
 "Cross-border points": [r"^Cross-border interactions"],
 "Worked examples": [r"^Worked examples$"],
 "Ask the client first": [r"^Ask the client"],
}
XB = dict(CORP)
TP = dict(CORP)
SC = dict(CORP)

def rebuild(fname, mapping, sources_block, tail_note=""):
    md = open(D + fname).read()
    fm, pre, secs = sections(md)
    # normalize: strip leading 'N. ' numbering; map already-renamed heads
    secs2 = []
    for h, b in secs:
        m = re.match(r"^\d+\. (.+)$", h)
        if m:
            h = m.group(1)
        if h in ("Rates and mechanics", "Rates, bands and thresholds"):
            h = "Rates" if len(b) >= 60 else "@stub"
        if h in ("The taxable base", "Deadlines and filing", "Cross-border points",
                 "Ask the client first", "Talk to a verified accountant"):
            h = "@stub"
        if h in ("Penalties and interest", "Worked examples") and len(b) < 60:
            h = "@stub"
        secs2.append((h, b))
    secs = secs2
    blocks = {}
    for head, plist in mapping.items():
        parts = []
        for p in plist:
            r = [(h, b) for h, b in secs if re.search(p, h)]
            assert len(r) == 1, (fname, p, [h for h, _ in secs])
            parts.append(r[0][1])
        blocks[head] = join(*parts)
    # 'Who this applies to' stays where it is (first ##). Rebuild doc:
    out = fm + pre.rstrip("\n") + "\n\n"
    out += "## Who this applies to\n" + one(secs, r"^Who this applies to$").strip("\n") + "\n\n"
    for head in ["Rates, bands and thresholds", "The taxable base", "Deadlines and filing",
                 "Penalties and interest", "Cross-border points", "Worked examples",
                 "Ask the client first"]:
        out += "## " + head + "\n" + blocks[head].strip("\n") + "\n\n"
    out += "## Sources\n" + sources_block.strip("\n") + "\n\n"
    out += "## Talk to a verified accountant\n" + tail_note.strip("\n") + "\n"
    open(D + fname, "w").write(out)
    print("wrote", fname)

# extract old sources bodies + CTA lines before rebuild
def old_sources(secs):
    r = [(h, b) for h, b in secs if h == "Sources"]
    if r:
        return r[0][1]
    r = [(h, b) for h, b in secs if h == "### Sources" or h == "Sources"]
    return ""

def grab(fname):
    md = open(D + fname).read()
    _, _, secs = sections(md)
    return secs

TABLE = """| Source | URL | Read on |
| --- | --- | --- |
"""

def make_sources(rows, unconfirmed):
    s = TABLE + "".join(rows) + "\nNot yet confirmed: " + unconfirmed + "\n"
    return s

# ---------- ca-corporate-income-tax ----------
secs = grab("ca-corporate-income-tax.md")
cta = "\n<!-- openaccountants-cta-block -->\n**Talk to a verified accountant** — for California franchise-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult\n"
src = make_sources(
 ["| FTB — Corporation Tax Rates | https://www.ftb.ca.gov/file/business/tax-rates.html | 2026-10-28 |\n",
  "| FTB — Form 100 (2025) | https://www.ftb.ca.gov/forms/2025/2025-100.pdf | 2026-10-28 |\n",
  "| FTB — Form 3539 (2025) | https://www.ftb.ca.gov/forms/2025/2025-3539.pdf | 2026-10-28 |\n",
  "| FTB — Form 568 (2025) | https://www.ftb.ca.gov/forms/2025/2025-568.pdf | 2026-10-28 |\n",
  "| FTB — Penalties and Interest | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html | 2026-10-28 |\n",
  "| FTB — Interest and Estimate Penalty Rates | https://www.ftb.ca.gov/pay/penalties-and-interest/interest-and-estimate-penalty-rates.html | 2026-10-28 |\n"],
 "the 8.84% rate, $800 minimum franchise tax, first-year exemption, LLC fee bands ($800–$11,790), economic-nexus thresholds ($750,000 / 25%), the 25% late-filing penalty, current FTB interest rates, and the 90%/100%/110% estimated-tax safe harbors are not yet confirmed against archived sources; the R&TC §§23151, 23153, 23101 and 25128 statute cites (leginfo 403 on 2026-10-27) remain pending verification.")
rebuild("ca-corporate-income-tax.md", CORP, src, cta)

# ---------- ca-s-corporation-tax ----------
cta = "\n<!-- openaccountants-cta-block -->\n**Talk to a verified accountant** — for California S-corporation questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult\n"
src = make_sources(
 ["| FTB — Form 100S (2025) | https://www.ftb.ca.gov/forms/2025/2025-100S.pdf | 2026-10-28 |\n",
  "| FTB — Corporation Tax Rates | https://www.ftb.ca.gov/file/business/tax-rates.html | 2026-10-28 |\n",
  "| FTB — Penalties and Interest | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html | 2026-10-28 |\n"],
 "the 1.5% entity-level tax rate, $800 minimum franchise tax, shareholder rates (1–13.3%), Form 7004 extension dates, estimated-tax schedule and safe-harbor percentages, and the R&TC §§23803 and 23153 statute cites (leginfo 403 on 2026-10-27) are not yet confirmed against archived sources.")
rebuild("ca-s-corporation-tax.md", SC, src, cta)

# ---------- ca-cross-border ----------
cta = "\n<!-- openaccountants-cta-block -->\n**Talk to a verified accountant** — for California nexus and cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult\n"
src = make_sources(
 ["| FTB — Corporation Tax Rates | https://www.ftb.ca.gov/file/business/tax-rates.html | 2026-10-28 |\n",
  "| FTB — Penalties and Interest | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html | 2026-10-28 |\n"],
 "the 8.84% rate and $800 minimum franchise tax, economic-nexus thresholds ($750,000 / 25%), the 18 CCR §§23101/25128/25110 and 15 U.S.C. §381 (PL 86-272) texts cited from Cornell LII, the credit-for-taxes-paid cites (R&TC §§17059, 24011), and the R&TC §§23101, 23151, 25128, 25134 and 25123 statute cites (leginfo 403 on 2026-10-27) are not yet confirmed against archived sources.")
rebuild("ca-cross-border.md", XB, src, cta)

# ---------- ca-transfer-pricing ----------
cta = "\n<!-- openaccountants-cta-block -->\n**Talk to a verified accountant** — for California combined-reporting and transfer-pricing questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult\n"
src = make_sources(
 ["| FTB — Corporation Tax Rates | https://www.ftb.ca.gov/file/business/tax-rates.html | 2026-10-28 |\n",
  "| FTB — Penalties and Interest | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html | 2026-10-28 |\n"],
 "the 8.84% rate, the 18 CCR §25110 water's-edge text cited from Cornell LII, and the R&TC §§25101, 25109, 25110, 25128 and 25134 statute cites (leginfo 403 on 2026-10-27) are not yet confirmed against archived sources.")
rebuild("ca-transfer-pricing.md", TP, src, cta)
