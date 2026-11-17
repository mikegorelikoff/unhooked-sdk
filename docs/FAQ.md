# FAQ

## Can I install the SDK from this public repository?

The repository contains documentation and runnable sample packages. Installation requires an approved SDK source or release. Use the sample directly to explore the file layout and run its helper. [Quickstart](Quickstart.md) · [Example](Examples.md)

## Which agent can I use?

Use an agent with local MCP support and access to the project. Loading skills and running their scripts follow that host's configuration. The [recorded demo](Demo.md) shows an earlier Codex setup with BMAD.

## Does every skill come with a script?

The agent authors a script when the task needs a repeatable check or another small helper. New drafts require structured steps. Inspect their inputs, outputs and completion gates in the generated package. [Skills and steps](Skills.md)

## How can I tell two runs agree?

Compare the entire file digest map and test outcomes in receipts from independent sessions. Keep the composed draft, target and SDK version fixed to reproduce the exact package. [Verification](Verification.md)
