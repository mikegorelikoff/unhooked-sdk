# Quickstart

Use a project you control, an MCP-capable agent and an approved SDK source or release. The SDK exposes its authoring operations through a local MCP server. Installation paths and skill discovery depend on the host.

## Install from a prompt

> Install Unhooked SDK from **[approved source and revision]** in this project. Follow that revision’s installation guide. Configure the local MCP server and install the complete authoring skill using this host’s conventions. Preserve the project’s existing tools and skills. Report the installed revision, tool discovery and any step that needs the host to reload.

Start a fresh session or reload the project setup if the host requires it. Ask the agent to discover the SDK tools and read the authoring skill. A configured fresh-host adapter is needed for live verification. [Verification](Verification.md)

## Author your first skill

> Build a checkout audit skill for reports of an unexpected shipping charge. Use separate scope, comparison and reporting steps. Write a Python helper to compare observed and expected amounts in cents. Export an Agent Skills package and return the validation result, package tree and SHA-256 digests. If a checkout case is configured, return the verification receipt too.

Ask the agent to save the composed draft. You can export that same draft again and compare the file digests. See [the checkout example](Examples.md) for the expected structure and script output.
