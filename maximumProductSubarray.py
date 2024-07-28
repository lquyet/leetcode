from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        n = len(nums)
        left = 1
        right = 1

        for i in range(n):
            left = nums[i] * left
            right = nums[n-1-i] * right

            res = max(res, left, right)
            if left == 0:
                left = 1
            if right == 0:
                right = 1           

        return res