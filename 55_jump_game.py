from typing import List

# BFS idea, tracking the furthest point we can reach when traveling
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthestIdx = 0
        n = len(nums)

        for i in range(n):
            if furthestIdx >= i:
                furthestIdx = max(furthestIdx, i + nums[i])
        
        return furthestIdx >= n - 1
        
