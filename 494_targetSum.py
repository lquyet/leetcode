from typing import List

# Same problem as the one I got in the promotion interview
# Target can be either a negative or positive number, that's tricky
# However we have this observation, if there are N ways to conduct the sum S from input list I, there are also N ways to conduct the sum -S from I
# as we reverse all +/- operations.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        target = -target if target < 0 else target
        mx = [abs(x) for x in nums]
        ms = sum(mx)
        dp = [[0 for _ in range(1001)] for _ in range(n+1)]

        dp[0][abs(nums[0])] = 1 if nums[0] != 0 else 2

        for i in range(1, n):
            for j in range(ms+1):
                tg1 = abs(j-nums[i]) if j - nums[i] < 0 else (j-nums[i])
                tg2 = abs(j+nums[i]) if j + nums[i] < 0 else (j+nums[i])
                if tg1 <= ms:
                    dp[i][j] += dp[i-1][tg1]
                if tg2 <= ms:
                    dp[i][j] += dp[i-1][tg2]
        return dp[n-1][target]