from typing import List


# Idea: Split the houses into 2 lists: 0 -> n-1, and 1-> n.
# Then use house robber (normal) to solve each -> get max
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        elif n == 3:
            return max(nums[0], nums[1], nums[2])
        dp1 = [0] * (n+1)
        dp2 = [0] * (n+1)

        def robHelper(nums: List[int], n: int, dp: List[int]) -> int:            
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            return dp[n-1]
        
        return max(robHelper(nums[0:n-1], n-1, dp1), robHelper(nums[1:n], n-1, dp2))