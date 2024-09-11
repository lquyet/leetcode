from typing import List

# O(nlogn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        l = [nums[0]]
        seen = set(l)
        
        for i in range(1, n):
            if nums[i] > l[-1]:
                l.append(nums[i])
                continue

            le, ri = 0, len(l) - 1
            while le != ri:
                m = (le + ri) // 2
                if l[m] < nums[i]:
                    le = m + 1
                else:
                    ri = m
            l[le] = nums[i]
        return len(l)
    
# O(n^2)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = -1

        for i in range(n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
            res = max(res, dp[i])
        
        return res
"""