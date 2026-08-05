# DSA in Python — NeetCode 250

Pattern-first practice. Every problem is filed by the pattern it teaches, not by
number, and every attempt is logged so that recognition speed and coding speed
can be tracked separately.

---

## Daily loop

Timeboxes: **easy 15 min · medium 25 min · hard 35 min.**

1. Copy `template.py` into the correct pattern folder, named
   `<4-digit number>_<snake_case_title>.py`. Fill `PROBLEM`, `LINK`,
   `DIFFICULTY`. **Leave `PATTERN` blank.**
2. Start the timer. Read the statement.
3. Before writing any code, fill `TRIGGER`, `PATTERN` (a guess), and `APPROACH`
   in plain English. **Stop T1 here.**
4. Code until it first runs. **Stop T2.**
5. Debug until it passes. **Stop T3.**
6. If stuck past the timebox — hint ladder:
   `hint=1` pattern name only, retry 10 min · `hint=2` watch the solution, close
   the tab, rewrite from a blank file.
7. Fill `COMPLEXITY`, `MISTAKES`, `REVISIT`. Append the `A1` line to `REPS`.
8. Append one row to `log.csv`.
9. Add a row to `TRIGGERS.md` only if a new tell was learned.
10. `git add . && git commit -m "<number> <pattern>"`

A wrong pattern guess is kept, never erased:
`guessed: sliding window -> actually: two pointers`.

---

## Review schedule

Reviews are scheduled **+1, +3, +7 days** from the first solve.

- A failed review **resets the ladder, not the counter**: `next_review` goes back
  to +1 day, but the attempt number keeps climbing. A problem sitting at A7 is a
  real gap, not bad luck.
- **Retirement:** two consecutive attempts with `hint_level=0`, `solved_cold=y`,
  and under the timebox → `status=retired`, `next_review` blank. Retired problems
  move to a monthly sweep.
- Re-solves are written from blank into `scratch.py` (gitignored). The committed
  file is overwritten only if the new version is genuinely better — one canonical
  solution per problem.

Daily volume target: **3–4 new + 3–5 reviews.**

---

## Timing metrics

| Metric | Measures | If it stays high |
| --- | --- | --- |
| T1 approach | statement → "I know the algorithm" | recognition gap → do the 5-min drill |
| T2 code | approach → first run | idiom gap → blank-file rewrites |
| T3 debug | first run → passing | coding before thinking → write the plan first |

Medium-difficulty targets by interview time: **T1 ≤ 3 · T2 ≤ 12 · T3 ≤ 5.**

---

## Progress by pattern

| # | Pattern | Solved | In rotation | Retired | Median T1 |
| --- | --- | --- | --- | --- | --- |
| 01 | Arrays & Hashing | | | | |
| 02 | Two Pointers | | | | |
| 03 | Sliding Window | | | | |
| 04 | Stack | | | | |
| 05 | Binary Search | | | | |
| 06 | Linked List | | | | |
| 07 | Trees | | | | |
| 08 | Tries | | | | |
| 09 | Heap / Priority Queue | | | | |
| 10 | Backtracking | | | | |
| 11 | Graphs | | | | |
| 12 | Advanced Graphs | | | | |
| 13 | 1-D DP | | | | |
| 14 | 2-D DP | | | | |
| 15 | Greedy | | | | |
| 16 | Intervals | | | | |
| 17 | Math & Geometry | | | | |
| 18 | Bit Manipulation | | | | |
| | **Total** | | | | |

_Regenerated weekly by `tools/gen_readme.py`._

---

## Rotation status

- Active:
- Retired:
- Overdue reviews:
- Longest-running problem (highest attempt number):

---

## Repo map

```
patterns/          solutions, filed by pattern
drills/            recognition drill log, weekly cold sessions
tools/             gen_readme.py, due_today.py
template.py        copy this for every new problem
log.csv            one row per attempt, append-only
TRIGGERS.md        statement signal -> pattern lookup table
```

Pattern recognition lives in [TRIGGERS.md](TRIGGERS.md). Read it before an
interview, not the solutions.
