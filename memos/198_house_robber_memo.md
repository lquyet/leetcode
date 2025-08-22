### Memo: House Robber

**Problem:** Given a list of non-negative integers representing money in each house along a street, determine the maximum total you can steal without robbing two adjacent houses.

**Mental model**
- Imagine walking along a line of houses. Each time you stand at a house, you can either:
  - take it (but then you must skip its immediate neighbor), or
  - skip it (keeping your previous best).
- This is like choosing checkpoints on a line where adjacent picks are forbidden.

**Key observations**
- **Local choice with memory**: The best decision at a house depends on outcomes you’ve already accumulated from earlier houses.
- **Adjacency constraint**: If you take the current house, you cannot take the immediately previous one.
- **Two prior anchors**: The only relevant “history” you need for a new decision comes from the previous house and the one before that.
- **Base handling**: Very short streets (length 0, 1, 2) need straightforward handling.

**Mini-examples**
- `[a]`: Only one option to consider.
- `[a, b]`: You may take at most one of them.
- `[a, b, c]`: Either you took one of the first two already, or you combine `a` with `c` if that’s better overall.
- `[a, b, c, d]`: Each new house asks: pair with the best up to two steps back, or keep the best so far?

**Guiding questions**
- If you include the current house, which previous house’s result can you legally combine it with?
- If you skip the current house, what value do you carry forward?
- What initial values should you start with for 0, 1, or 2 houses?
- How can you update your running answer using only constant extra space?
- In what order should you update your rolling values to avoid overwriting something you still need?

**Approach outline (no code)**
- Walk left to right, maintaining two running quantities:
  - the best total up to the previous house,
  - the best total up to the house before the previous one.
- For each new house:
  - compute the best if you take it (combine its value with the “two-back” total),
  - compute the best if you skip it (keep the “one-back” total),
  - choose the better, then shift your rolling window forward.
- Return the final running best.

**Why this works**
- Every valid plan either includes the current house (forcing a gap) or excludes it. Considering both options using the two prior anchors captures all legal possibilities without re-evaluating earlier choices.

**Edge cases**
- Empty list ⇒ 0.
- Single house.
- Two houses (pick the better).
- All zeros (answer is 0).
- Large inputs (ensure single pass, constant extra storage).

**Complexity intuition**
- Time: linear in the number of houses (single pass).
- Space: constant (keep only a couple of running totals).

**Common pitfalls**
- Off-by-one mistakes in initialization (especially for small arrays).
- Updating rolling values in the wrong order and losing needed information.
- Allocating an entire array for history when only two prior values are required.

**Self-check prompts**
- For `[2, 1, 1, 2]`, which positions do you end up taking if you reason step-by-step?
- For `[1, 2, 3, 1]`, what does your running pair of totals look like after each step?
- How would you adapt your base handling when the input has length 1 or 2?
