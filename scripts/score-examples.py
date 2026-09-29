#!/usr/bin/env python3
"""Score SPECTRUM reports against human expectations in examples/expected/.

For each examples/expected/<id>.yaml with a matching examples/reports/<id>.md:
  * compare the verdict (🟢 ready / 🔴 not ready / 🟠 inconclusive)
  * check that every expected blocking finding appears in the 🔴 Bloquants
    section (any of its keywords, case-insensitive)
  * count unexpected blocking findings (heuristic: bullet lines in 🔴 section
    that match no expected keyword set)
Prints a table and summary rates. Exit 0 always (this is a measurement, not a gate).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EXP = ROOT / "examples" / "expected"
REP = ROOT / "examples" / "reports"

VERDICT_MAP = {
    "🟢": "ready_for_implementation",
    "🔴": "not_ready_for_implementation",
    "🟠": "assessment_inconclusive",
}


def extract_verdict(report: str) -> str | None:
    m = re.search(r"\*\*Verdict\s*:\*\*\s*(🟢|🔴|🟠)", report)
    if not m:
        m = re.search(r"Verdict[^\n]*?(🟢|🔴|🟠)", report)
    return VERDICT_MAP.get(m.group(1)) if m else None


def extract_section(report: str, header_regex: str) -> str:
    m = re.search(header_regex + r"(.*?)(?=\n##+ |\Z)", report, re.S)
    return m.group(1) if m else ""


def main() -> int:
    rows, n_verdict_ok, n_total, n_inconclusive = [], 0, 0, 0
    missed_total = expected_total = unexpected_total = 0
    for exp_file in sorted(EXP.glob("*.yaml")):
        exp = yaml.safe_load(exp_file.read_text(encoding="utf-8")) or {}
        tid = exp.get("ticket", exp_file.stem)
        rep_file = REP / f"{tid}.md"
        if not rep_file.exists():
            rows.append((tid, "—", "pas de rapport", "", ""))
            continue
        report = rep_file.read_text(encoding="utf-8")
        n_total += 1
        got = extract_verdict(report)
        want = exp.get("expected_verdict")
        verdict_ok = got == want or (exp.get("tolerated_inconclusive") and got == "assessment_inconclusive")
        n_verdict_ok += 1 if verdict_ok else 0
        n_inconclusive += 1 if got == "assessment_inconclusive" else 0

        blocking = extract_section(report, r"###\s*🔴[^\n]*\n")
        blocking_l = blocking.lower()
        missed = []
        for f in exp.get("expected_blocking_findings", []) or []:
            expected_total += 1
            if not any(k.lower() in blocking_l for k in f.get("keywords", [])):
                missed.append(f.get("note", "/".join(f.get("keywords", []))))
        missed_total += len(missed)
        bullets = [b for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", blocking) if b.strip()]
        all_kw = [k.lower() for f in (exp.get("expected_blocking_findings") or []) for k in f.get("keywords", [])]
        unexpected = [b for b in bullets if not any(k in b.lower() for k in all_kw)]
        unexpected_total += len(unexpected)
        rows.append((tid, "OK" if verdict_ok else f"KO ({got})", f"{len(missed)} manqué(s)", f"{len(unexpected)} inattendu(s)", "; ".join(missed)[:80]))

    print(f"{'ticket':22s} {'verdict':18s} {'bloquants attendus':20s} {'bloquants en trop':18s} détail")
    for r in rows:
        print(f"{r[0]:22s} {r[1]:18s} {r[2]:20s} {r[3]:18s} {r[4]}")
    if n_total:
        print()
        print(f"verdicts corrects : {n_verdict_ok}/{n_total} ({100*n_verdict_ok//n_total}%)")
        print(f"inconclusifs      : {n_inconclusive}/{n_total} ({100*n_inconclusive//n_total}%)  -> >30% = politique trop exigeante")
        if expected_total:
            print(f"rappel bloquants  : {expected_total-missed_total}/{expected_total} ({100*(expected_total-missed_total)//expected_total}%)")
        print(f"bloquants en trop : {unexpected_total} (à lire un par un — chaque faux bloquant coûte la confiance des devs)")
    else:
        print("\nAucun rapport dans examples/reports/. Lance /spectrum:analyze-ticket sur examples/tickets/*.md et colle les rapports.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
