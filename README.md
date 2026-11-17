<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.svg">
    <img src="docs/assets/banner-light.svg" alt="Unhooked SDK" width="100%">
  </picture>
</p>

<p align="center">
  <a href="docs/Guide.md"><img alt="Guide" src="https://img.shields.io/badge/docs-guide-F97316"></a>
  <a href="https://github.com/mikegorelikoff/unhooked-sdk/wiki"><img alt="Wiki" src="https://img.shields.io/badge/docs-wiki-52525B"></a>
  <a href="LICENSE"><img alt="Documentation license CC BY 4.0" src="https://img.shields.io/badge/docs%20license-CC%20BY%204.0-blue"></a>
</p>

**Build installable AI agent skills from a prompt. A package can include numbered steps, reusable instructions, scripts, and evidence from a test in a fresh agent session.**

## Why

When a team keeps explaining the same task to agents, it can capture that task once as a skill. The agent authors the instructions and helpers. The SDK orders the components, checks what each step needs and produces an installable package with SHA-256 digests.

## Quickstart

Give an MCP-capable agent your approved SDK source or release and paste this prompt in the project where you want to use the skill. [Full setup guide](docs/Quickstart.md)

> Set up Unhooked SDK from my approved source or release. Discover its MCP tools, then create a skill to audit checkout shipping. Reuse the scope and evidence steps. Add a step and a Python helper that compare observed and expected shipping in cents. Export the Agent Skills package and return the step files, script, and file digests. If a fresh-host checkout case is configured, run it and return the verification receipt.

The [checkout example](examples/checkout-threshold-audit/SKILL.md) is a six-file package:

```text
checkout-threshold-audit/
├── SKILL.md
├── customize.toon
├── steps/
│   ├── step-01.md
│   ├── step-02.md
│   └── step-03.md
└── scripts/
    └── check-shipping.py
```

`SKILL.md` opens step 1 directly. `customize.toon` gives HX the same order. Step 2 runs the Python helper, which reports 499 cents observed versus 0 expected and exits with code 1. [Run the example](docs/Examples.md#run-the-exported-checkout-helper)

## How it works

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/authoring-flow-dark.svg">
    <img src="docs/assets/authoring-flow-light.svg" alt="Prompt, compose, package, verify" width="100%">
  </picture>
</p>

| Capability | What you get |
| --- | --- |
| Compose | Reusable components ordered by their dependencies. |
| Validate | Diagnostics for missing step contracts, broken references and conflicting files. |
| Export | Agent Skills, BMAD, OpenSpec or Spec Kit output. See the [profile matrix](docs/How-it-works.md#export-profiles) for differences. |
| Verify | A receipt for a configured fresh-host case. It records the package hashes, session and observed test result. |
| Compare | A check that two independent passing receipts agree on the package and test outcomes. |

## Documentation

| Guide | Learn how to |
| --- | --- |
| [Quickstart](docs/Quickstart.md) | Set up the SDK and create a skill from a prompt. |
| [How it works](docs/How-it-works.md) | Understand composition, packaging and export profiles. |
| [Skills and steps](docs/Skills.md) | Read an exported package and follow the HX step order. |
| [Verification](docs/Verification.md) | Read a test receipt and compare independent runs. |
| [Examples](docs/Examples.md) | Try prompts and run the checkout script. |
| [Recorded demo](docs/Demo.md) | Watch the earlier BMAD setup and regression run. |
| [FAQ](docs/FAQ.md) | Find answers about access, scripts and reproducibility. |

[Guide index](docs/Guide.md) · [GitHub Wiki](https://github.com/mikegorelikoff/unhooked-sdk/wiki)

## Availability

This public repository contains guides, examples and demo media under [CC BY 4.0](LICENSE). SDK source and releases require separate access. [Report a documentation issue](https://github.com/mikegorelikoff/unhooked-sdk/issues/new/choose)
