### Memo: Unique Binary Search Trees (Catalan Numbers)

**Problem:** Given `n` nodes, how many structurally unique Binary Search Trees (BSTs) can be constructed storing values `1`..`n`?

**Definitions**
- **G(n)**: number of unique BSTs with `n` nodes.
- **F(i, n)**: number of BSTs where `i` is the root using nodes `1..n`.

**Recurrence**
- G(n) = F(1,n) + F(2,n) + ... + F(n,n)
- For root `i`: left has `i-1` nodes, right has `n-i` nodes, so:
  - **F(i,n) = G(i-1) * G(n-i)**
- Therefore:
  - **G(n) = G(0)*G(n-1) + G(1)*G(n-2) + ... + G(n-1)*G(0)**

**Base cases**
- **G(0) = 1** (empty tree)
- **G(1) = 1** (single node)

**DP solution**
- Use `dp` (or `g`) array of size `n+1`:
  - `dp = [0] * (n + 1)`
  - `dp[0] = 1`; `dp[1] = 1` (if n >= 1)
- Fill:
```python
for i in range(2, n+1):
    for j in range(0, i):
        dp[i] += dp[j] * dp[i - 1 - j]
```
- `dp[n]` is the answer.

**Complexity**
- Time: **O(n^2)** (nested loops).
- Space: **O(n)** for the DP array.

**Notes**
- The sequence `G(n)` are the **Catalan numbers** (1, 1, 2, 5, 14, 42, ...).
- Closed-form: `C_n = (1 / (n + 1)) * binom(2n, n)` — computing factorials/binomials for large `n` may require arbitrary-precision arithmetic, so runtime is not strictly O(1) in practice.

