# Step 2 — check-shipping-charge

**Progress: Step 2 of 3**

Read the current step in full. Advance only when its completion gate is met. If you cannot meet it, follow the blocked instruction and stop the workflow.

**Input**: The scoped case from the previous step, with the observed and expected shipping charges converted to integer cents.

**Output**: One comparison line from scripts/check-shipping.py and its exit status (0 match, 1 mismatch, 2 invalid input).

**Done when**: The script was run with two valid integer-cent arguments and its exit status is recorded, or the input problem is identified.

**On blocked**: If the exit status is 2, correct the cent values and rerun; if they cannot be determined, report the missing amounts.

Use [scripts/check-shipping.py](../scripts/check-shipping.py) with `python3` as directed below. Resolve the script path from the skill root.


## check-shipping-charge

Compare the observed shipping charge with the expected charge for the scoped cart, both as integer cents, using `scripts/check-shipping.py`.

Usage: `python3 scripts/check-shipping.py OBSERVED_CENTS EXPECTED_CENTS`

- Both arguments are required non-negative integer cents (for example `499` for 4.99).
- It prints one comparison line and has no side effects.
- Exit 0: charges match. Exit 1: mismatch. Exit 2: invalid input (wrong argument count, non-integer, or negative).

Record the exact command and its exit status for the report.

When done, read the [next step](step-03.md).
