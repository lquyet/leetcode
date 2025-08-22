### Memo: Minimum Time to Make Rope Colorful

**Problem:** Given `colors` (string) and `neededTime` (array), remove balloons so no two adjacent balloons share the same color, minimizing total removal time.

**Mental model**
- Imagine the rope as segments of identical color laid back-to-back.
- Within each segment, to avoid adjacent duplicates, you need to leave exactly one balloon and remove the rest.
- Different segments don’t affect each other once separated by a different color.

**Key observations**
- **Segment independence**: Each maximal run of the same color can be handled on its own.
- **Must keep one**: In a run of length `k`, you must remove `k-1` balloons.
- **Cost structure**: The cost for a run depends on which single balloon you decide to keep.
- **Global cost**: Total cost is the sum of all runs’ costs.

**Mini-examples**
- `colors = "aba"`, times `[1,5,3]`: All adjacent pairs are already different ⇒ cost should be 0.
- `colors = "aa"`, times `[3,4]`: One run of length 2 ⇒ remove one of them.
- `colors = "aaab"`, times `[2,5,1,7]`: One run `"aaa"` then `"b"` ⇒ handle the first run only.
- `colors = "aabaa"`, times `[1,2,3,4,5]`: Multiple runs: `"aa"`, `"b"`, `"aa"`.

**Guiding questions**
- For a run of same color, if you must leave one balloon, which choice minimizes the run’s removal cost?
- How can you detect when a run starts and ends while scanning left-to-right?
- How do you ensure the final run is accounted for when reaching the end?
- Can you express the total answer using per-run aggregates (like sums and a single chosen value per run)?

**Approach outline (no code)**
- Scan `colors` once, maintaining the current run’s color and tracking:
  - the cumulative time of balloons in the run,
  - the single balloon in the run that you decide to keep.
- When the color changes (or at the end):
  - add the run’s removal cost to the answer,
  - reset tracking for the next run.
- Accumulate across all runs.

**Why this works**
- Fixing adjacency in a run only depends on choices within that run; separating colors breaks cross-run dependencies.
- Keeping exactly one balloon per run guarantees adjacent uniqueness.

**Edge cases**
- Single character strings.
- All characters distinct (answer is 0).
- All characters identical (one long run).
- Ties in `neededTime` within a run.
- Very long input (ensure O(1) extra memory beyond a few counters).

**Complexity intuition**
- Single pass over the rope ⇒ linear time in `n`.
- Constant extra state to track the current run.

**Common pitfalls**
- Forgetting to finalize the last run at the end of the scan.
- Miscounting when runs are of length 1 (their cost is 0).
- Mixing runs across color boundaries.
- Recomputing aggregates inefficiently instead of maintaining them on the fly.

**Self-check prompts**
- For a run `[t1, t2, ..., tk]`, what is the minimal total removal time if exactly one is kept?
- If you concatenate two runs of different colors, does your logic avoid merging them?
- Try `colors="abbbaa"`, `times=[3,2,10,1,4,6]`. What are the runs? What cost do you get per run? Does the sum make sense?