# How Unhooked works

Unhooked helps coding teams turn repeatable agent workflows into reusable skill packages. A skill has instructions, conditions for when to use them, and optional reference files. The agent using the SDK works from your prompt and calls the SDK to compose, check, and package the draft.

![Four stages: compose a draft, validate it, export for a target, verify in the agent host](assets/workflow.svg)

| Stage | What you get |
| --- | --- |
| Describe | A draft with when-to-use rules, ordered steps, and evidence requirements. |
| Compose and check | Reused instructions in dependency order, plus diagnostics for missing inputs or unsupported behavior. |
| Package | Target-specific files and a report on what the target preserves. |
| Verify | A live check in the selected host. Package preparation alone does not prove installation or activation. |

| Target | Output |
| --- | --- |
| Agent Skills | A skill directory containing `SKILL.md` and its reference files. |
| BMAD | A custom module and help entry. The demo adds a project rule for Codex to open the workflow on a regression report. |
| OpenSpec | A companion skill used with an explicit change ID. |
| Spec Kit | An opt-in extension with an explicitly invoked command. |

A compatible host can discover the local MCP tools. The SDK also has Rust and CLI entry points; the public guides use prompts as the user interface. The [demo](Demo.md) verifies one host setup. It does not claim equivalent activation across all hosts.

[Quickstart](Quickstart.md) · [Sample exported shape](../examples/regression-check/SKILL.md)
