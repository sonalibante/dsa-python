# DSA in Python — Sonali's practice

Two tracks in one repo:

1. **`data_structures/`** — data structures from the ground up. For each data
   structure, implement every operation yourself in `operations/` and keep a
   short-notes file in `data_structures/short_notes/`. Roadmap order:
   Array → String → Hashing → Stack → Queue → Linked List → Tree, then Heap,
   Trie, Graph.
2. **`patterns/`** — 250 problems grouped by the pattern they teach. Every
   problem file already exists. Solve them in the order of
   [SEQUENCE.md](SEQUENCE.md).

Every attempt is logged so that recognition speed and coding speed can be
tracked separately.

---

## Daily loop

Timeboxes: **easy 15 min · medium 25 min · hard 35 min.**

1. Open the next unticked problem in `SEQUENCE.md`. Its file is already in
   `patterns/<pattern>/<easy|medium|hard>/`. Fill in `LINK` and paste the
   problem statement into `STATEMENT`. **Leave `PATTERN` blank.**
2. Start the timer. Read the statement.
3. Before writing any code, fill `TRIGGER`, `PATTERN` (a guess), and `APPROACH`
   in plain English. **Stop T1 here.**
4. Code the `_brute` method first, then the `_improved` method, until it
   first runs. **Stop T2.**
5. Debug until it passes. **Stop T3.**
6. If stuck past the timebox — hint ladder:
   `hint=1` pattern name only, retry 10 min · `hint=2` watch the solution, close
   the tab, rewrite from a blank file.
7. Fill `COMPLEXITY`, `MISTAKES`, `REVISIT`. Append the `A1` line to `REPS`.
8. Append one row to `log.csv`.
9. Add a row to `TRIGGERS.md` only if a new tell was learned.
10. Tick the box in `SEQUENCE.md`.
11. `git add . && git commit -m "<sequence #> <pattern>"`

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
  brute + improved pair per problem.

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
| 04 | Binary Search | | | | |
| 05 | Linked List | | | | |
| 06 | Stack | | | | |
| 07 | Trees | | | | |
| 08 | Tries | | | | |
| 09 | Backtracking | | | | |
| 10 | Heap / Priority Queue | | | | |
| 11 | Graphs | | | | |
| 12 | Advanced Graphs | | | | |
| 13 | 1-D DP | | | | |
| 14 | 2-D DP | | | | |
| 15 | Greedy | | | | |
| 16 | Intervals | | | | |
| 17 | Bit Manipulation | | | | |
| 18 | Math & Geometry | | | | |
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
data_structures/              data-structures track
  short_notes/                one notes file per data structure
  01_array/operations/        one file per operation, implement yourself
  ... 10_graph/operations/
  patterns/sorting_algos/     one file per sorting algorithm
  patterns/searching_algos/   one file per searching algorithm
  operation_template.py       copy for any extra operation
patterns/                     250 problems, one folder per pattern
  01_arrays_hashing/
    easy/ medium/ hard/       <nn>_<title>.py, nn = order within the pattern
SEQUENCE.md                   all 250 problems in solve order, with checkboxes
drills/                       recognition drill log, weekly cold sessions
tools/                        gen_readme.py, due_today.py
template.py                   for extra problems outside the 250
log.csv                       one row per attempt, append-only
TRIGGERS.md                   statement signal -> pattern lookup table
```

Every problem file has two methods: `<name>_brute` and `<name>_improved`.

Pattern recognition lives in [TRIGGERS.md](TRIGGERS.md). Read it before an
interview, not the solutions.
