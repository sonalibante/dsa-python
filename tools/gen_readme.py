"""
gen_readme.py  --  regenerate the README progress tables. Run weekly.

STATUS: unimplemented stub. Write this yourself.

WHAT IT DOES
------------
Walks patterns/, parses the docstring header of every solution file, cross-
references log.csv, and rewrites two sections of README.md in place:
"Progress by pattern" and "Rotation status". Everything else in the README is
left untouched.

INPUTS
------
  patterns/<nn>_<name>/<easy|medium|hard>/<nn>_<title>.py
      Each file opens with a module docstring containing lines of the form
      "KEY : value", plus a REPS block of the form
          REPS:
            A1  2026-08-06  hint=2  T 4/22/9  cold=n
  log.csv
      Append-only, one row per attempt. Columns:
      date, problem, pattern, difficulty, attempt, hint_level,
      t1_approach_min, t2_code_min, t3_debug_min, solved_cold,
      next_review, status, notes

OUTPUT
------
  README.md, rewritten between the existing section headings.

REQUIRED BEHAVIOUR
------------------
1. Discover pattern folders from the filesystem, not a hardcoded list, so a new
   folder appears in the table automatically. Sort by the numeric prefix.
2. Per pattern, count: solved (files whose REPS block has a dated A1 line; all 250 files exist from the start), in rotation
   (latest log row status == "active"), retired (status == "retired").
3. Median T1 per pattern, computed over first attempts only (attempt == 1).
   Median, not mean -- one 40-minute disaster should not move the number.
4. Totals row.
5. Rotation status: total active, total retired, problems whose next_review is
   on or before today, and the problem with the highest attempt number.
6. Idempotent -- running twice in a row produces an identical file.
7. Never touch the "Daily loop", "Review schedule", "Timing metrics", or
   "Repo map" sections.

EDGE CASES TO HANDLE
--------------------
  - a pattern folder with no solutions yet (print blanks, not 0/0 division)
  - a solution file whose header is half-filled or malformed
  - a problem present in patterns/ but absent from log.csv, and vice versa
  - blank next_review on retired rows
  - an even number of samples when taking the median

CONSTRAINTS
-----------
Standard library only: pathlib, csv, re, datetime, statistics.

USAGE
-----
  python tools/gen_readme.py            rewrite README.md
  python tools/gen_readme.py --dry-run  print the tables, change nothing
"""


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
