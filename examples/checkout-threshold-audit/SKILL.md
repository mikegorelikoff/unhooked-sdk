---
name: "checkout-threshold-audit"
description: "Audit a checkout shipping charge that crosses a free-shipping or price threshold by comparing the observed charge with the expected charge in integer cents. Use when a user reports a wrong shipping fee at checkout."
metadata:
  version: "1.0.0"
  source-skill: "checkout-threshold-audit"
---

## Activation

### Use when

A user reports an unexpected shipping charge at a checkout threshold

### Avoid when

General bug investigation unrelated to checkout shipping charges

## Execution

Start with [step 1](steps/step-01.md). Read one step at a time and advance only when its completion gate is met.
