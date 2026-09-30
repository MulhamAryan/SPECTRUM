#!/usr/bin/env python3
"""SPECTRUM read-only guard (Claude Code hook).

Makes the "read-only by default" promise mechanical instead of textual.

How it works
------------
* UserPromptSubmit : if the prompt is a `/spectrum:*` command, a marker file is
  created for this session -> read-only mode ON. Any other prompt removes the
  marker -> read-only mode OFF. The guard therefore only affects SPECTRUM
  analyses, not the rest of your Claude Code usage.
* PreToolUse       : while the marker exists, Write/Edit/MultiEdit/NotebookEdit
  are blocked, Bash commands matching write patterns are blocked, and MCP tools
  whose name looks like a mutation (create/update/edit/delete/transition/comment
  /push/merge/publish...) are blocked. Blocking = exit code 2 + reason on stderr,
  which Claude Code shows to the model.
* Stop             : the marker is removed when the turn ends.

Environment overrides
---------------------
* SPECTRUM_READ_ONLY=1  -> guard always ON, regardless of the prompt.
* SPECTRUM_ALLOW_WRITE=1 -> guard always OFF (use only when you explicitly want
  SPECTRUM to write, e.g. an authorized Jira comment).

Limitations (documented, not hidden)
------------------------------------
* A follow-up prompt that is not a `/spectrum:` command ends read-only mode.
* Bash detection is pattern-based; it blocks common write commands, not every
  conceivable one. It is a safety net, not a sandbox.
"""
import json
import os
import re
import sys
import tempfile

MUTATING_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}

BASH_WRITE_PATTERNS = [
    r"\bgit\s+(commit|push|add|rm|mv|checkout|switch|reset|rebase|merge|cherry-pick|stash|tag|apply|am|restore|clean)\b",
    r"\bgit\s+branch\s+-[dDmM]",
    r"\bgh\s+(pr|issue|release|repo|api)\b.*\b(create|edit|merge|close|comment|delete|reopen|-X\s*(POST|PUT|PATCH|DELETE))",
    r"(^|[^<])>{1,2}\s*[^&\s]",            # redirection to a file (but not 2>&1)
    r"\btee\b",
    r"\b(rm|mv|cp|mkdir|touch|chmod|chown|ln)\s",
    r"\bsed\s+(-[a-zA-Z]*i|--in-place)",
    r"\b(npm|pnpm|yarn)\s+(install|ci|add|publish|remove|uninstall|link)\b",
    r"\bpip3?\s+(install|uninstall)\b",
    r"\bcurl\b.*\s-X\s*(POST|PUT|PATCH|DELETE)",
    r"\b(jira|acli)\s+.*\b(create|edit|update|transition|comment|assign|delete)\b",
    r"\bdocker\s+(run|exec|rm|rmi|build|push)\b",
]
BASH_WRITE_RE = [re.compile(p, re.IGNORECASE) for p in BASH_WRITE_PATTERNS]

MCP_MUTATION_RE = re.compile(
    r"^mcp__.*__.*(create|update|edit|delete|remove|transition|addcomment|addworklog|comment|write|push|merge|publish|assign|move|archive|upload|send|post)",
    re.IGNORECASE,
)

SPECTRUM_PROMPT_RE = re.compile(r"^\s*/spectrum:", re.IGNORECASE)


def marker_path(session_id: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", session_id or "unknown")
    return os.path.join(tempfile.gettempdir(), f"spectrum-readonly-{safe}")


def read_payload() -> dict:
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}


def guard_active(session_id: str) -> bool:
    if os.environ.get("SPECTRUM_ALLOW_WRITE") == "1":
        return False
    if os.environ.get("SPECTRUM_READ_ONLY") == "1":
        return True
    return os.path.exists(marker_path(session_id))


def block(reason: str) -> None:
    sys.stderr.write(
        "🔒 SPECTRUM guard: action bloquée — mode lecture seule actif pendant une analyse SPECTRUM.\n"
        f"Raison : {reason}\n"
        "Une analyse, un constat ou un verdict n'autorise aucune écriture. "
        "Pour autoriser explicitement une écriture, relancez hors commande /spectrum: "
        "ou exportez SPECTRUM_ALLOW_WRITE=1.\n"
    )
    sys.exit(2)


def on_user_prompt_submit(payload: dict) -> None:
    session_id = payload.get("session_id", "")
    prompt = payload.get("prompt", "") or ""
    path = marker_path(session_id)
    if SPECTRUM_PROMPT_RE.match(prompt):
        with open(path, "w") as fh:
            fh.write(prompt[:200])
    else:
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
    sys.exit(0)


def on_stop(payload: dict) -> None:
    try:
        os.remove(marker_path(payload.get("session_id", "")))
    except FileNotFoundError:
        pass
    sys.exit(0)


def on_pre_tool_use(payload: dict) -> None:
    session_id = payload.get("session_id", "")
    if not guard_active(session_id):
        sys.exit(0)
    tool = payload.get("tool_name", "") or ""
    tool_input = payload.get("tool_input", {}) or {}

    if tool in MUTATING_TOOLS:
        block(f"outil de modification de fichier `{tool}` (cible : {tool_input.get('file_path', '?')})")

    if tool == "Bash":
        cmd = tool_input.get("command", "") or ""
        for rx in BASH_WRITE_RE:
            if rx.search(cmd):
                block(f"commande Bash à effet d'écriture détectée : `{cmd[:120]}`")
        sys.exit(0)

    if MCP_MUTATION_RE.match(tool):
        block(f"outil MCP de mutation `{tool}`")

    sys.exit(0)


def main() -> None:
    event = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = read_payload()
    if event == "user-prompt-submit":
        on_user_prompt_submit(payload)
    elif event == "pre-tool-use":
        on_pre_tool_use(payload)
    elif event == "stop":
        on_stop(payload)
    sys.exit(0)


if __name__ == "__main__":
    main()
