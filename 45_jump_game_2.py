from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        furthestIdx = 0
        n = len(nums)

        jump = 0
        currentEnd = 0

        for i in range(n):
            furthestIdx = max(furthestIdx, i + nums[i])
            
            if furthestIdx >= n-1:
                return jump

            if i == currentEnd:
                jump += 1
                currentEnd = furthestIdx

        # Should never be here since it's guaranteed that we can always reach the end
        return -1

            

