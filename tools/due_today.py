"""
due_today.py  --  print the review queue. Run at the start of every session.

STATUS: unimplemented stub. Write this yourself.

WHAT IT DOES
------------
Reads log.csv and prints which problems are due for review today, oldest first,
so the session starts with reviews rather than new problems.

INPUT
-----
  log.csv -- append-only, one row per attempt. Columns:
    date, problem, pattern, difficulty, attempt, hint_level,
    t1_approach_min, t2_code_min, t3_debug_min, solved_cold,
    next_review, status, notes

  A problem appears many times. Only its LAST row is current -- that row holds
  the live next_review and status. Earlier rows are history.

OUTPUT
------
  DUE TODAY (2026-08-06)
    0424  sliding_window   A2   due 2026-08-06   last: hint=2 T 4/22/9
    0003  sliding_window   A4   due 2026-08-04   OVERDUE 2d

  Then a one-line summary: n due, n overdue, n active, n retired.

REQUIRED BEHAVIOUR
------------------
1. Group rows by problem, keep the row with the highest attempt number.
2. Skip anything with status == "retired".
3. Due when next_review <= today. Flag overdue with the day count.
4. Sort by next_review ascending -- most overdue first.
5. Exit code 0 always; this is informational, not a test.

STRETCH -- the flags that actually change behaviour
---------------------------------------------------
  --stale     problems at attempt >= 4 that are still active. These are real
              gaps, not bad luck, and warrant rereading the TRIGGERS row rather
              than another blind re-solve.
  --pattern P restrict to one pattern folder.
  --slow      active problems whose latest T1 is above the target for their
              difficulty (easy 2, med 3, hard 5 minutes). High T1 means the gap
              is recognition, so the fix is the recognition drill, not solving.

EDGE CASES TO HANDLE
--------------------
  - empty log.csv (header row only)
  - blank next_review on an active row (data error -- report it, do not crash)
  - a malformed date string
  - duplicate rows with the same problem and attempt number

CONSTRAINTS
-----------
Standard library only: csv, datetime, argparse, collections.

USAGE
-----
  python tools/due_today.py
  python tools/due_today.py --stale
  python tools/due_today.py --pattern 03_sliding_window
"""


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
