#!/usr/bin/env bash
# Self-test for scripts/spectrum-guard.py. Exit 0 = all assertions pass.
set -u
cd "$(dirname "$0")/.."
G="node scripts/spectrum-guard.js"
SID="selftest-$$"
fail=0
assert() { local want=$1 got=$2 msg=$3; if [ "$want" != "$got" ]; then echo "FAIL: $msg (want exit $want, got $got)"; fail=1; else echo "ok:   $msg"; fi; }
run() { echo "$2" | $G "$1" >/dev/null 2>&1; echo $?; }

# Not a spectrum prompt -> guard off -> Write allowed
run user-prompt-submit "{\"session_id\":\"$SID\",\"prompt\":\"hello\"}" >/dev/null
assert 0 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"Write\",\"tool_input\":{\"file_path\":\"x\"}}")" "Write allowed outside /spectrum:"

# Spectrum prompt -> guard on
run user-prompt-submit "{\"session_id\":\"$SID\",\"prompt\":\"/spectrum:analyze-ticket foo.md\"}" >/dev/null
assert 2 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"Write\",\"tool_input\":{\"file_path\":\"x\"}}")" "Write blocked during /spectrum:"
assert 2 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"x\"}}")" "Edit blocked"
assert 2 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"git commit -m x\"}}")" "git commit blocked"
assert 2 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"echo hi > out.txt\"}}")" "redirection blocked"
assert 0 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"git log --oneline -5 2>&1\"}}")" "git log allowed"
assert 0 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"grep -rn foo src/\"}}")" "grep allowed"
assert 2 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"mcp__Atlassian__addCommentToJiraIssue\",\"tool_input\":{}}")" "Jira comment blocked"
assert 2 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"mcp__Atlassian__transitionJiraIssue\",\"tool_input\":{}}")" "Jira transition blocked"
assert 0 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"mcp__Atlassian__getJiraIssue\",\"tool_input\":{}}")" "Jira read allowed"
assert 0 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"Read\",\"tool_input\":{}}")" "Read allowed"

# Stop -> guard off
run stop "{\"session_id\":\"$SID\"}" >/dev/null
assert 0 "$(run pre-tool-use "{\"session_id\":\"$SID\",\"tool_name\":\"Write\",\"tool_input\":{\"file_path\":\"x\"}}")" "Write allowed after Stop"

# Override
run user-prompt-submit "{\"session_id\":\"$SID\",\"prompt\":\"/spectrum:review-tests x\"}" >/dev/null
assert 0 "$(echo "{\"session_id\":\"$SID\",\"tool_name\":\"Write\",\"tool_input\":{}}" | SPECTRUM_ALLOW_WRITE=1 $G pre-tool-use >/dev/null 2>&1; echo $?)" "SPECTRUM_ALLOW_WRITE=1 disables guard"
run stop "{\"session_id\":\"$SID\"}" >/dev/null
exit $fail
