# Well at first I think dp[i][j] should be the state considering s[0:i+1] and t[0:j+1]
# However it causes a lot of edge cases and fails at testcase 64th, where s = 1000 * 'a' and t = 999 * 'a'
# The expected result is 0, but I think it should be 1000? Still don't know why
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def filter_common_chars(a, b):
            common_chars = set(a) & set(b)
            
            result_a = ''.join([char for char in a if char in common_chars])
            result_b = ''.join([char for char in b if char in common_chars])
    
            return result_a, result_b
        
        s, t = filter_common_chars(s, t)
        n = len(s)
        m = len(t)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if i < j:
                    dp[i][j] = 0
                elif i == j:
                    dp[i][j] = 1 if s[0:i+1] == t[0:j+1] else 0
                else:
                    dp[i][j] += dp[i-1][j]
                    if s[i] == t[j]:
                        if i>0 and j>0 and dp[i-1][j-1] != 0:
                            dp[i][j] += dp[i-1][j-1]
                        elif i<=0 or j <= 0:
                            dp[i][j] += 1
                        else:
                            pass
                
        return dp[n-1][m-1]
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][m]