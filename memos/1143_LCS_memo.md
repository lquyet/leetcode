### **Memo: Longest Common Subsequence (LCS)**

**Problem Definition:**
Given two sequences (strings), find the length of the longest subsequence present in both of them.
*   A **subsequence** is formed by deleting zero or more characters from the original sequence while maintaining the relative order of the remaining characters. (e.g., "ACE" is a subsequence of "ABCDE").
*   A **substring** requires consecutive characters.

**Core Idea (Recursive Thinking):**
Consider the last characters of the two input strings, `word1` and `word2`.

1.  **Case 1: Characters Match (`word1[i-1] == word2[j-1]`)**
    If the last characters of the current prefixes match, then this character *can* be part of the LCS. The length of the LCS will be `1` (for the matched character) plus the LCS of the strings *excluding* these last characters.

2.  **Case 2: Characters Do Not Match (`word1[i-1] != word2[j-1]`)**
    If the last characters do not match, then at least one of them cannot be part of the LCS at this position. We must explore two possibilities:
    *   Find the LCS by excluding the last character of `word1`.
    *   Find the LCS by excluding the last character of `word2`.
    We take the maximum of these two results, as we want the *longest* subsequence.

**Dynamic Programming Approach (Bottom-Up):**

This problem exhibits **overlapping subproblems** (the same subproblems are solved multiple times recursively) and **optimal substructure** (the optimal solution to the problem can be constructed from optimal solutions to its subproblems), making it suitable for Dynamic Programming.

1.  **DP State Definition:**
    Let `dp[i][j]` represent the length of the Longest Common Subsequence between the first `i` characters of `word1` (`word1[0...i-1]`) and the first `j` characters of `word2` (`word2[0...j-1]`).
    *(Note: We use 1-based indexing for the `dp` table for simpler logic, aligning with lengths of prefixes.)*

2.  **Base Cases (Initialization):**
    *   `dp[0][j] = 0` for all `j`: The LCS of an empty string and any prefix of `word2` is `0`.
    *   `dp[i][0] = 0` for all `i`: The LCS of any prefix of `word1` and an empty string is `0`.

3.  **Recurrence Relation (Filling the `dp` table):**
    Iterate `i` from 1 to `len(word1)` and `j` from 1 to `len(word2)`.

    *   **If `word1[i-1] == word2[j-1]` (characters match):**
        `dp[i][j] = dp[i-1][j-1] + 1`
        (The common character at `i-1`/`j-1` extends the LCS found in the previous prefixes.)

    *   **Else (`word1[i-1] != word2[j-1]` - characters do not match):**
        `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
        (We consider the LCS obtained by either excluding `word1[i-1]` or excluding `word2[j-1]`. The scenario where *both* are excluded (`dp[i-1][j-1]`) is implicitly covered because `dp[i-1][j]` and `dp[i][j-1]` will be at least `dp[i-1][j-1]`.)

4.  **Final Answer:**
    If `N = len(word1)` and `M = len(word2)`, the length of the Longest Common Subsequence of the entire `word1` and `word2` will be `dp[N][M]`.
