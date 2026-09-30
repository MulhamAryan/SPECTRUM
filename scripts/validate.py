#!/usr/bin/env python3
"""SPECTRUM structural validator.

Turns the *structural* invariants of evaluation/contracts/*.yaml into real,
executable checks. Run locally (`python3 scripts/validate.py`) or in CI.
Exit code 1 on any error; warnings do not fail the build.

Requires: PyYAML (`pip install pyyaml`).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
ERRORS: list[str] = []
WARNINGS: list[str] = []
COVERED_INVARIANTS: set[str] = set()


def err(msg: str, invariant: str | None = None) -> None:
    ERRORS.append(msg)
    if invariant:
        COVERED_INVARIANTS.add(invariant)


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def covered(*ids: str) -> None:
    COVERED_INVARIANTS.update(ids)


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        err(f"{path.relative_to(ROOT)}: YAML parse error: {exc}")
        return None


def frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception as exc:  # noqa: BLE001
        err(f"{path.relative_to(ROOT)}: frontmatter parse error: {exc}")
        return None


# --------------------------------------------------------------------------- #
# 1. Manifests
# --------------------------------------------------------------------------- #
def check_manifests() -> str | None:
    plugin = ROOT / ".claude-plugin" / "plugin.json"
    market = ROOT / ".claude-plugin" / "marketplace.json"
    if not plugin.exists() or not market.exists():
        err("missing .claude-plugin/plugin.json or marketplace.json")
        return None
    p = json.loads(plugin.read_text())
    m = json.loads(market.read_text())
    version = p.get("version")
    for entry in m.get("plugins", []):
        if entry.get("version") != version:
            err(f"version mismatch: plugin.json={version} marketplace.json={entry.get('version')}")
    for stale in ["gemini-extension.json"]:
        if (ROOT / stale).exists():
            g = json.loads((ROOT / stale).read_text())
            if g.get("version") != version:
                err(f"version mismatch: {stale}={g.get('version')} plugin.json={version}")
    return version


# --------------------------------------------------------------------------- #
# 2. Frontmatter of skills / agents / commands
# --------------------------------------------------------------------------- #
def check_skills() -> set[str]:
    skills: set[str] = set()
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            err(f"skills/{skill_dir.name}: missing SKILL.md")
            continue
        fm = frontmatter(skill_md)
        if fm is None:
            err(f"skills/{skill_dir.name}/SKILL.md: missing frontmatter")
            continue
        if fm.get("name") != skill_dir.name:
            err(f"skills/{skill_dir.name}: frontmatter name '{fm.get('name')}' != directory name")
        if not fm.get("description"):
            err(f"skills/{skill_dir.name}: missing description")
        skills.add(skill_dir.name)
    return skills


def check_agents() -> set[str]:
    agents: set[str] = set()
    for md in sorted((ROOT / "agents").glob("*.md")):
        if md.name == "README.md":
            continue
        fm = frontmatter(md)
        if fm is None:
            err(f"agents/{md.name}: missing frontmatter")
            continue
        if fm.get("name") != md.stem:
            err(f"agents/{md.name}: frontmatter name '{fm.get('name')}' != file name")
        for key in ("description", "model", "tools"):
            if not fm.get(key):
                err(f"agents/{md.name}: missing '{key}'")
        if "Task" in (fm.get("tools") or []):
            err(f"agents/{md.name}: declares Task — sub-agents cannot spawn sub-agents")
        if "supervisor" in md.stem:
            err("agents/: a supervisor agent must not exist (orchestrator is the slash command)")
        agents.add(md.stem)
    return agents


def check_commands() -> None:
    for md in sorted((ROOT / "commands").glob("*.md")):
        fm = frontmatter(md)
        if fm is None or not fm.get("description"):
            err(f"commands/{md.name}: missing frontmatter description")
        text = md.read_text(encoding="utf-8")
        if "supervisor.md" in text:
            err(f"commands/{md.name}: references the removed supervisor agent")


# --------------------------------------------------------------------------- #
# 3. Registry
# --------------------------------------------------------------------------- #
def check_registry(skills: set[str], agents: set[str]) -> dict:
    reg = load_yaml(ROOT / "agents" / "registry.yaml") or {}
    entries = reg.get("agents", {})
    for agent, spec in entries.items():
        if agent not in agents:
            err(f"registry: agent '{agent}' has no agents/{agent}.md")
        for key in ("required_skills", "optional_skills"):
            for s in spec.get(key, []) or []:
                if s not in skills:
                    err(f"registry: agent '{agent}' references unknown skill '{s}'")
        if "global_readiness" not in (spec.get("forbidden_decisions") or []) and agent != "report-composer":
            err(f"registry: agent '{agent}' must forbid global_readiness")
        if not spec.get("stages"):
            err(f"registry: agent '{agent}' declares no stages")
    for agent in agents:
        if agent not in entries:
            err(f"registry: agents/{agent}.md is not registered")
    return entries


# --------------------------------------------------------------------------- #
# 4. Workflow graph
# --------------------------------------------------------------------------- #
def check_workflow(skills: set[str], registry: dict) -> tuple[dict, set[str]]:
    wf_path = ROOT / "workflows" / "ticket-analysis.yaml"
    wf = load_yaml(wf_path) or {}
    meta = wf.get("workflow", {})
    if not meta.get("id") or not meta.get("version"):
        err("workflow: missing id or version", "TAW-001")
    covered("TAW-001")
    if "ticket" not in (wf.get("inputs", {}).get("required") or []):
        err("workflow: 'ticket' must be a required input", "TAW-001")

    stages = wf.get("stages", [])
    ids = [s.get("id") for s in stages]
    if len(ids) != len(set(ids)):
        err("workflow: duplicate stage ids")
    idset = set(ids)
    used_skills: set[str] = set()
    used_agents: set[str] = set()
    graph: dict[str, list[str]] = {}

    for s in stages:
        sid = s.get("id", "?")
        for key in ("phase", "agent", "purpose", "produces"):
            if key not in s:
                err(f"workflow stage '{sid}': missing '{key}'")
        deps = s.get("depends_on", []) or []
        graph[sid] = deps
        if sid != ids[0] and not deps:
            err(f"workflow stage '{sid}': non-root stage without depends_on", "TAW-002")
        for d in deps:
            if d not in idset:
                err(f"workflow stage '{sid}': unknown dependency '{d}'", "TAW-002")
        agent = s.get("agent")
        if agent and agent != "orchestrator":
            used_agents.add(agent)
            if agent not in registry:
                err(f"workflow stage '{sid}': agent '{agent}' not in registry")
            else:
                allowed = set(registry[agent].get("required_skills", []) or []) | set(registry[agent].get("optional_skills", []) or [])
                for sk in s.get("skills", []) or []:
                    if sk not in allowed:
                        err(f"workflow stage '{sid}': skill '{sk}' not allowed for agent '{agent}'", "TAW-004")
                if sid not in (registry[agent].get("stages") or []):
                    err(f"workflow stage '{sid}': registry entry for '{agent}' does not list this stage")
        if "skills" in s and "engine" in s:
            err(f"workflow stage '{sid}': declares both skills and engine", "TAW-004")
        if "skills" not in s and "engine" not in s and agent != "orchestrator" and sid not in ("qa", "compose_report", "ingest"):
            err(f"workflow stage '{sid}': neither skills nor engine", "TAW-004")
        for sk in s.get("skills", []) or []:
            if sk not in skills:
                err(f"workflow stage '{sid}': unknown skill '{sk}'", "TAW-004")
            used_skills.add(sk)
    covered("TAW-002", "TAW-004")

    # acyclicity (Kahn)
    indeg = {n: 0 for n in graph}
    for n, deps in graph.items():
        for d in deps:
            if d in indeg:
                indeg[n] += 1
    queue = [n for n, d in indeg.items() if d == 0]
    seen = 0
    rev: dict[str, list[str]] = {n: [] for n in graph}
    for n, deps in graph.items():
        for d in deps:
            if d in rev:
                rev[d].append(n)
    while queue:
        n = queue.pop()
        seen += 1
        for m in rev[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                queue.append(m)
    if seen != len(graph):
        err("workflow: stage dependency graph contains a cycle", "TAW-003")
    covered("TAW-003")

    # readiness only in decide_readiness
    for s in stages:
        prods = s.get("produces", []) or []
        if "Decision" in prods and s.get("id") != "decide_readiness":
            err(f"workflow stage '{s.get('id')}': only decide_readiness may produce Decision", "TAW-010")
    covered("TAW-010", "TAW-009")

    # ordering invariants
    def before(a: str, b: str) -> bool:
        """True if a is a (transitive) dependency of b."""
        stack, seen_ = list(graph.get(b, [])), set()
        while stack:
            x = stack.pop()
            if x == a:
                return True
            if x in seen_:
                continue
            seen_.add(x)
            stack.extend(graph.get(x, []))
        return False

    for a, b, inv in [
        ("multi_source_reasoning", "consolidate_findings", "TAW-015"),
        ("consolidate_findings", "consolidate", "TAW-017"),
        ("analyze_cross_artifacts", "multi_source_reasoning", "TAW-020"),
        ("consolidate", "decide_readiness", "TAW-009"),
        ("analyze_business_rules", "analyze_adversarial_requirements", "TAW-031"),
    ]:
        if a in idset and b in idset and not before(a, b):
            err(f"workflow: '{a}' must precede '{b}'", inv)
        covered(inv)

    # independent must not depend on drift (decision v8) and must be isolated
    ind = next((s for s in stages if s.get("id") == "analyze_independent"), None)
    if ind:
        if "analyze_spec_implementation_drift" in (ind.get("depends_on") or []):
            err("workflow: analyze_independent must not depend on drift analysis (parallel by decision v8)")
        if not (ind.get("isolation") or {}).get("must_not_read_primary_agent_conclusions_before_own_analysis"):
            err("workflow: analyze_independent must declare isolation")

    # parallel groups must be mutually independent
    for group in (wf.get("execution_model", {}).get("parallelizable_groups") or []):
        for a in group:
            if a not in idset:
                err(f"workflow: parallel group references unknown stage '{a}'")
            for b in group:
                if a != b and a in idset and b in idset and before(a, b):
                    err(f"workflow: parallel group contains dependent stages '{a}' -> '{b}'", "TAW-005")
    covered("TAW-005")

    # profiles
    profiles = wf.get("profiles", {})
    if "default" not in profiles or profiles["default"] not in profiles:
        err("workflow: profiles.default must name an existing profile")
    for name, prof in profiles.items():
        if name == "default":
            continue
        pol = prof.get("readiness_policy_ref")
        if not pol or not (ROOT / pol).exists():
            err(f"workflow profile '{name}': readiness policy '{pol}' not found", "TAW-013")
        st = prof.get("stages")
        if isinstance(st, list):
            for x in st:
                if x not in idset:
                    err(f"workflow profile '{name}': unknown stage '{x}'")
            if "decide_readiness" in st and "consolidate" not in st:
                err(f"workflow profile '{name}': decide_readiness requires consolidate")
        for x in prof.get("excluded_stages", []) or []:
            if x not in idset:
                err(f"workflow profile '{name}': unknown excluded stage '{x}'")
    covered("TAW-013")

    # no other file may define phases
    orch = load_yaml(ROOT / "models" / "agent-orchestration.yaml") or {}
    if "phases" in orch:
        err("models/agent-orchestration.yaml defines 'phases' — the graph must live only in the workflow")

    # registry agents unused by workflow
    for agent in registry:
        if agent not in used_agents:
            warn(f"registry agent '{agent}' is not used by any workflow stage")
    return wf, used_skills


# --------------------------------------------------------------------------- #
# 5. Orphan skills
# --------------------------------------------------------------------------- #
def check_orphans(skills: set[str], used_by_workflow: set[str], registry: dict) -> None:
    reachable = set(used_by_workflow)
    for spec in registry.values():
        reachable |= set(spec.get("required_skills", []) or []) | set(spec.get("optional_skills", []) or [])
    for s in sorted(skills - reachable):
        err(f"skills/{s}: orphan — not used by any workflow stage or registry agent (move to experimental/ or wire it)")


# --------------------------------------------------------------------------- #
# 6. Policies, report contract, schema, hooks
# --------------------------------------------------------------------------- #
def check_policies() -> None:
    for pol in sorted((ROOT / "policies").glob("*.yaml")):
        d = load_yaml(pol) or {}
        meta = d.get("policy", {})
        if not meta.get("id") or not meta.get("version"):
            err(f"{pol.name}: policy needs id and version")
        crit = d.get("criteria", {})
        if not crit:
            err(f"{pol.name}: no criteria")
        for name, c in crit.items():
            for key in ("applicability", "satisfied_when", "blocking_conditions"):
                if key not in c:
                    err(f"{pol.name}: criterion '{name}' missing '{key}'")
        outcomes = d.get("outcomes", {}).get("permitted", {})
        for o in ("ready_for_implementation", "not_ready_for_implementation", "assessment_inconclusive"):
            if o not in outcomes:
                err(f"{pol.name}: missing outcome '{o}'")


def check_misc() -> None:
    schema = ROOT / "models" / "agent-execution-result.schema.json"
    if not schema.exists():
        err("missing models/agent-execution-result.schema.json")
    else:
        try:
            d = json.loads(schema.read_text())
            for key in ("execution_id", "agent_id", "status", "skill_executions", "findings", "evidence_refs"):
                if key not in d.get("required", []):
                    err(f"agent result schema: '{key}' must be required")
        except Exception as exc:  # noqa: BLE001
            err(f"agent result schema: invalid JSON: {exc}")
    load_yaml(ROOT / "outputs" / "ticket-analysis-report.yaml")
    hooks = ROOT / "hooks" / "hooks.json"
    if not hooks.exists():
        err("missing hooks/hooks.json (read-only guard)")
    else:
        try:
            h = json.loads(hooks.read_text())
            if "PreToolUse" not in h.get("hooks", {}):
                err("hooks.json: PreToolUse guard missing")
            for event in h.get("hooks", {}).values():
                for entry in event:
                    for hk in entry.get("hooks", []):
                        m = re.search(r"CLAUDE_PLUGIN_ROOT\}/([^\"\s]+)", hk.get("command", ""))
                        if m and not (ROOT / m.group(1)).exists():
                            err(f"hooks.json: script '{m.group(1)}' not found")
        except Exception as exc:  # noqa: BLE001
            err(f"hooks.json: invalid JSON: {exc}")
    for ph in ("core/orchestration-procedure.md", "core/agent-brief.md", "CHANGELOG.md", "NOTICE"):
        if not (ROOT / ph).exists():
            warn(f"missing {ph}")


# --------------------------------------------------------------------------- #
def main() -> int:
    version = check_manifests()
    skills = check_skills()
    agents = check_agents()
    check_commands()
    registry = check_registry(skills, agents)
    _wf, used = check_workflow(skills, registry)
    check_orphans(skills, used, registry)
    check_policies()
    check_misc()

    print(f"SPECTRUM validate — version {version} — {len(skills)} skills, {len(agents)} agents, {len(registry)} registry entries")
    print(f"structural invariants covered: {', '.join(sorted(COVERED_INVARIANTS))}")
    for w in WARNINGS:
        print(f"WARN  {w}")
    for e in ERRORS:
        print(f"ERROR {e}")
    print(f"{len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
