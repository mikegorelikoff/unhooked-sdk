---
name: regression-check
description: Reproduce a reported functional regression with a focused test.
---

# Regression check

Use when a user reports that previously working behavior now fails. Skip for new feature planning.

1. State the reported behavior and the expected result.
2. Identify the smallest input that exposes the difference.
3. Run or write one focused test. If the prior working version is available, run the same test there.
4. Use the [evidence checklist](references/evidence.md) to report the result. Do not change implementation unless requested.

This sample illustrates an Agent Skills package layout. Installation and discovery depend on the host.
