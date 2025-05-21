# One of the very typical 2-D DP problem
# Could be optimized if we filter out all characters that belongs to only 1 in 2 strings
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        for i in range(1, n):
            dp[i][0] = 1 if text1[i] == text2[0] else dp[i-1][0]

        for j in range(1, m):
            dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j-1]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j-1] + 1 if text1[i] == text2[j] else max(dp[i-1][j], dp[i][j-1])
        
        return dp[n-1][m-1]