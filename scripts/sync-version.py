#!/usr/bin/env python3
"""Keep the plugin version identical across every manifest.

  python3 scripts/sync-version.py --check      # exit 1 if manifests disagree
  python3 scripts/sync-version.py 0.5.0        # write 0.5.0 everywhere
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFESTS = [ROOT / ".claude-plugin" / "plugin.json", ROOT / ".claude-plugin" / "marketplace.json"]


def read_versions() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for m in MANIFESTS:
        if not m.exists():
            continue
        d = json.loads(m.read_text())
        if "plugins" in d:
            out[str(m.relative_to(ROOT))] = [p.get("version", "?") for p in d["plugins"]]
        else:
            out[str(m.relative_to(ROOT))] = [d.get("version", "?")]
    return out


def write_version(v: str) -> None:
    for m in MANIFESTS:
        if not m.exists():
            continue
        d = json.loads(m.read_text())
        if "plugins" in d:
            for p in d["plugins"]:
                p["version"] = v
        else:
            d["version"] = v
        m.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
        print(f"{m.relative_to(ROOT)} -> {v}")


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] == "--check":
        vs = read_versions()
        flat = {v for vals in vs.values() for v in vals}
        for k, v in vs.items():
            print(f"{k}: {', '.join(v)}")
        if len(flat) != 1:
            print("ERROR: manifests disagree on version")
            return 1
        print("OK")
        return 0
    write_version(sys.argv[1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
