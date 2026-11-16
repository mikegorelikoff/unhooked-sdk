# Prompts to try

After [setting up the SDK](Quickstart.md), paste one of these into a compatible agent chat.

## Create and package a skill

> Create a skill for functional regressions. Have it find one focused test, compare expected and observed behavior, and report the relevant source and test evidence. Validate the draft and prepare a BMAD package in a new folder. Tell me what ran and what still needs live verification.

Expect a draft, validation results, and a package location. The [example skill](../examples/regression-check/SKILL.md) shows what instructions and a supporting reference can look like.

## Verify that the workflow is picked up

> At exactly $50, checkout started charging $4.99 for shipping. Orders at $50 used to qualify for free shipping. Reproduce this with a focused test and report the expected and actual values. Leave the implementation unchanged.

Use a project where you can safely reproduce that behavior and have installed the regression workflow. In the [recorded BMAD setup](Demo.md), the agent opened the workflow and its evidence card before running the test.

## Compare with a feature request

> Plan an indicator that shows how much more a customer needs to add to qualify for free shipping. Read the current policy and propose two acceptance criteria. Make no file changes.

This is a planning request. The regression workflow should stay inactive.
