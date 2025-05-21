from typing import List

# Backtracking with memoization 
# This memoization approach helps solving some cases where there are multiple identical elements in the input 
# Eg: [1, 1, 1, 1, ... (1000 numbers), 100, 100]
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums) / 2
        dp = {}

        if target % 1 != 0:
            return False

        def helper(i, cur):
            if cur == target:
                return True
            
            if (i, cur) in dp and not dp[(i, cur)]:
                return False

            if cur > target: 
                return False

            if i > n - 1:
                return False
            
            dp[(i, cur)] = helper(i+1, cur + nums[i]) or helper(i+1, cur)

            return dp[(i, cur)]
        
        return helper(0, 0)