#!/usr/bin/env python3
"""Compare observed and expected shipping charges given in integer cents.

Usage: check-shipping.py OBSERVED_CENTS EXPECTED_CENTS

Exit status:
  0  charges match
  1  charges differ
  2  invalid input (wrong argument count, non-integer, or negative value)

The script has no side effects and uses only the standard library.
"""
import sys


def parse_cents(text):
    """Return a non-negative integer for text, or None if it is invalid."""
    try:
        value = int(text, 10)
    except ValueError:
        return None
    return value if value >= 0 else None


def main(argv):
    if len(argv) != 2:
        print("invalid input: expected 2 arguments: OBSERVED_CENTS EXPECTED_CENTS")
        return 2
    observed = parse_cents(argv[0])
    expected = parse_cents(argv[1])
    if observed is None or expected is None:
        print("invalid input: both arguments must be non-negative integer cents")
        return 2
    if observed == expected:
        print(f"MATCH: observed {observed} cents equals expected {expected} cents")
        return 0
    diff = observed - expected
    print(f"MISMATCH: observed {observed} cents, expected {expected} cents (difference {diff:+d})")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
