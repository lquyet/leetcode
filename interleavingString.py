class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if m+n != len(s3):
            return False
        
        if m == n == 0:
            return True

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(0, n+1):
            for j in range(0, m+1):
                if i == j == 0:
                    continue
                elif i == 0:
                    if s2[j-1] == s3[j-1] and dp[i][j-1] == 1: 
                        dp[i][j] = 1
                elif j == 0:
                    if s1[i-1] == s3[i-1] and dp[i-1][j] == 1:
                        dp[i][j] = 1
                else:
                    if s2[j-1] == s3[i+j-1] and dp[i][j-1] == 1:
                        dp[i][j] = 1

                    if s1[i-1] == s3[i+j-1] and dp[i-1][j] == 1:
                        dp[i][j] = 1
        
        return dp[n][m]