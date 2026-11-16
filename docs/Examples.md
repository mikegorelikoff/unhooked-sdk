# Try these prompts in Codex

First [set up the SDK](Install-in-Codex.md) in a project you control. Then choose a prompt and paste it into the chat.

## Draft and package a skill

> Build a reusable skill for checking release notes against a project’s changes. It should verify every claim and report claims it couldn’t verify. Show me the draft, validate it, and prepare a BMAD package in a new folder. Tell me what was checked and what still needs live verification.

Expect a draft, validation results, a package location, and an explicit account of what has yet to be verified in a host.

## Reproduce a regression

> At exactly $50, checkout started charging $4.99 for shipping. Orders at $50 used to qualify for free shipping. Reproduce this with a focused test and report the expected and actual values. Leave the implementation unchanged.

In a project with that behavior and the installed BMAD workflow, Codex should read the regression workflow and its evidence card, then run the test. You do not need to name the skill.

## Plan a feature in the same area

> Plan an indicator that shows how much more someone needs to add to qualify for free shipping. Read the current shipping policy and give two acceptance criteria. Make no file changes.

The project rule should skip the regression workflow for this request.
