class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def canDecode(i):
            ii = int(i)
            if 0 < ii < 10 and len(i) == 1:
                return True
            if 9 < ii < 27 and len(i) == 2:
                return True
            return False

        if n == 1:
            return 1 if canDecode(s) else 0

        dp = [0] * n
        dp[0] = 1 if canDecode(s[0]) else 0

        for i in range(1, n):
            if canDecode(s[i]):
                dp[i] += dp[i-1]
            if canDecode(s[i-1:i+1]):
                dp[i] += dp[i-2] if i > 1 else 1
        return dp[n-1]


class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]

        if s[0] == "0":
            return 0
        else:
            dp[1] = 1

        for i in range(2, n+1):
            check = False
            if s[i-2] != "0" and 1 <= int(s[i-2:i]) <= 26:
                dp[i] += max(dp[i-2], 1)
                check = True

            if s[i-1] != "0":
                dp[i] += max(dp[i-1], 1)
                check = True
            
            if not check:
                return 0
        
        return dp[n]

