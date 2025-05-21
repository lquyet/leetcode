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


