# Skills and steps

A skill starts with the activation guidance in `SKILL.md`. Its first link opens step 1 directly. Each step explains its input, output, what counts as complete and what to do if blocked. The next-step link shows where to continue after meeting the gate.

## The package

| File | What it contains |
| --- | --- |
| [SKILL.md](../examples/checkout-threshold-audit/SKILL.md) | Activation conditions and the first-step link. |
| [customize.toon](../examples/checkout-threshold-audit/customize.toon) | The IDs and paths of the steps in HX run order. |
| [steps/step-01.md](../examples/checkout-threshold-audit/steps/step-01.md) | Scope the report and establish the expected and observed values. |
| [steps/step-02.md](../examples/checkout-threshold-audit/steps/step-02.md) | Run the comparison and capture its output and exit code. |
| [steps/step-03.md](../examples/checkout-threshold-audit/steps/step-03.md) | Report the result and evidence. |
| [scripts/check-shipping.py](../examples/checkout-threshold-audit/scripts/check-shipping.py) | Source of the script the agent runs in step 2. |

## Authoring and execution

For new authoring drafts, the current SDK contract requires a step on every section. Reusable components can supply those steps. Existing drafts explicitly marked as version 1 use the earlier contract. Scripts are optional and go under `scripts/`; the step names the interpreter and explains when to run them.

HX can read the ordered step mapping and advance through the checkout package. Completion instructions in these exported steps are evaluated by the agent. For checks that run as code during `hx done`, the skill needs executable HX gates. [Run the checkout helper](Examples.md#run-the-exported-checkout-helper)
