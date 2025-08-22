### Memo: Unique Binary Search Trees II (Generate All Trees)

**Problem:** Given `n`, construct all structurally unique BSTs that store values `1..n`.

**Mental model**
- Think of placing a value as the root. Everything smaller must live on the left; everything larger on the right.
- For any chosen root `i`, the left side must be built from the values `< i`, and the right side from the values `> i`.
- All possible left shapes can be paired with all possible right shapes. Each pair forms a different tree with `i` at the top.

**Key observations**
- **Partition by root choice**: The numbers split into two disjoint ranges around the root.
- **Independence of sides**: Left and right can be designed independently, then combined.
- **Empty side is valid**: When a side has no numbers, treat it as a single “empty subtree” option.
- **No duplicates**: Since each side uses a disjoint value range, pairing shapes won’t create duplicate structures.

**Mini-examples**
- **n = 0**: No trees ⇒ return an empty list (or treat as one empty structure when combining at higher levels).
- **n = 1**: Only one shape — a single node.
- **n = 2**:
  - Root = 1: left = empty, right = [2]
  - Root = 2: left = [1], right = empty
- **n = 3**:
  - Root = 1: left = empty, right = all shapes from {2,3}
  - Root = 2: left = all shapes from {1}, right = all shapes from {3}
  - Root = 3: left = all shapes from {1,2}, right = empty
  - Pair each left-option with each right-option for that root.

**Guiding questions**
- If you pick a root `i`, exactly which numbers can appear on each side?
- What should be returned when the range of numbers for a side is empty?
- How can you systematically “pair” every left possibility with every right possibility for a root?
- How do you avoid duplicates without extra bookkeeping?
- What smaller subproblems naturally appear when you choose a root in a range?

**Approach outline (no code)**
- Work with a function defined on a range `[L, R]` that returns all tree shapes using those values.
- If `L > R`, return a single “empty” option to enable valid pairings.
- Otherwise, for each `i` in `[L, R]`:
  - Build all possible left shapes from `[L, i-1]`.
  - Build all possible right shapes from `[i+1, R]`.
  - For every combination of (left, right), assemble a new tree with `i` as the root.
- Start from `[1, n]` and collect the assembled trees.

**Why this works**
- Each tree has a unique topmost value. For that choice, left and right must be independently valid. Combining all independent possibilities covers all valid structures without overlap.

**Edge cases**
- **n = 0**: Decide API behavior — usually return `[]` at the top.
- **Value labels**: Even though you combine shapes, each node’s label is determined by its position in the BST.
- **Memory**: The total number of trees grows quickly; holding all shapes is intrinsic to the task.

**Complexity intuition**
- The number of trees for `n` grows according to the count from your `96` memo. Generating all shapes requires time proportional to that count, multiplied by the cost to assemble nodes.

**Common pitfalls**
- Forgetting to include the “empty subtree” option when a side has no values (this blocks valid pairings).
- Mixing value ranges when constructing sides.
- Reusing nodes across different trees (each pairing should create fresh nodes).

**Cross-check**
- The total number of trees you generate for `n` should match the count from `96_unique_bst_memo.md`.

**Try these to self-test**
- Sketch all trees for `n = 3`. Count and compare with your `96` memo.
- For `n = 4`, pick root `2`. How many left options come from `{1}`? How many right options from `{3,4}`? How many total for this root?