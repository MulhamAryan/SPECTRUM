#!/usr/bin/env node
"use strict";
const fs = require("fs");
const os = require("os");
const path = require("path");

const MUTATING_TOOLS = new Set(["Write", "Edit", "MultiEdit", "NotebookEdit"]);

const BASH_WRITE_PATTERNS = [
  /\bgit\s+(commit|push|add|rm|mv|checkout|switch|reset|rebase|merge|cherry-pick|stash|tag|apply|am|restore|clean)\b/i,
  /\bgit\s+branch\s+-[dDmM]/,
  /\bgh\s+(pr|issue|release|repo|api)\b.*\b(create|edit|merge|close|comment|delete|reopen|-X\s*(POST|PUT|PATCH|DELETE))/i,
  /(^|[^<])>{1,2}\s*[^&\s]/,
  /\btee\b/i,
  /\b(rm|mv|cp|mkdir|touch|chmod|chown|ln)\s/i,
  /\bsed\s+(-[a-zA-Z]*i|--in-place)/,
  /\b(npm|pnpm|yarn)\s+(install|ci|add|publish|remove|uninstall|link)\b/i,
  /\bpip3?\s+(install|uninstall)\b/i,
  /\bcurl\b.*\s-X\s*(POST|PUT|PATCH|DELETE)/i,
  /\b(jira|acli)\s+.*\b(create|edit|update|transition|comment|assign|delete)\b/i,
  /\bdocker\s+(run|exec|rm|rmi|build|push)\b/i,
  /\b(del|erase|rmdir|rd|copy|move|ren|rename|mklink)\s/i,
  /\b(Remove-Item|Move-Item|Copy-Item|New-Item|Set-Content|Add-Content|Out-File)\b/i,
];

const MCP_MUTATION_RE =
  /^mcp__.*__.*(create|update|edit|delete|remove|transition|addcomment|addworklog|comment|write|push|merge|publish|assign|move|archive|upload|send|post)/i;

const SPECTRUM_PROMPT_RE = /^\s*\/spectrum:/i;

function markerPath(sessionId) {
  const safe = String(sessionId || "unknown").replace(/[^A-Za-z0-9_.-]/g, "_");
  return path.join(os.tmpdir(), `spectrum-readonly-${safe}`);
}
function guardActive(sessionId) {
  if (process.env.SPECTRUM_ALLOW_WRITE === "1") return false;
  if (process.env.SPECTRUM_READ_ONLY === "1") return true;
  return fs.existsSync(markerPath(sessionId));
}
function block(reason) {
  process.stderr.write(
    "🔒 SPECTRUM guard: action bloquée — mode lecture seule actif pendant une analyse SPECTRUM.\n" +
      `Raison : ${reason}\n` +
      "Une analyse, un constat ou un verdict n'autorise aucune écriture. " +
      "Pour autoriser explicitement une écriture, relancez hors commande /spectrum: ou exportez SPECTRUM_ALLOW_WRITE=1.\n"
  );
  process.exit(2);
}
function safeUnlink(p) { try { fs.unlinkSync(p); } catch (_) {} }

function onUserPromptSubmit(payload) {
  const p = markerPath(payload.session_id);
  const prompt = String(payload.prompt || "");
  if (SPECTRUM_PROMPT_RE.test(prompt)) { try { fs.writeFileSync(p, prompt.slice(0, 200)); } catch (_) {} }
  else safeUnlink(p);
  process.exit(0);
}
function onStop(payload) { safeUnlink(markerPath(payload.session_id)); process.exit(0); }
function onPreToolUse(payload) {
  if (!guardActive(payload.session_id)) process.exit(0);
  const tool = String(payload.tool_name || "");
  const input = payload.tool_input || {};
  if (MUTATING_TOOLS.has(tool)) block(`outil de modification de fichier \`${tool}\` (cible : ${input.file_path || "?"})`);
  if (tool === "Bash") {
    const cmd = String(input.command || "");
    for (const rx of BASH_WRITE_PATTERNS) if (rx.test(cmd)) block(`commande Bash à effet d'écriture détectée : \`${cmd.slice(0, 120)}\``);
    process.exit(0);
  }
  if (MCP_MUTATION_RE.test(tool)) block(`outil MCP de mutation \`${tool}\``);
  process.exit(0);
}
function main() {
  const event = process.argv[2] || "";
  let raw = "";
  process.stdin.setEncoding("utf8");
  process.stdin.on("data", (c) => (raw += c));
  process.stdin.on("end", () => {
    let payload = {};
    try { payload = raw.trim() ? JSON.parse(raw) : {}; } catch (_) { payload = {}; }
    if (event === "user-prompt-submit") return onUserPromptSubmit(payload);
    if (event === "pre-tool-use") return onPreToolUse(payload);
    if (event === "stop") return onStop(payload);
    process.exit(0);
  });
  if (process.stdin.isTTY) process.stdin.emit("end");
}
main();
