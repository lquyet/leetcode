from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(hnums):
            if len(hnums) == 1:
                return [[hnums[0]], []]
            r = helper(hnums[1:])
            return r + [a + [hnums[0]] for a in r]
        return helper(nums)