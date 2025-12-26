#
# @lc app=leetcode id=2216 lang=python3
#
# [2216] Minimum Deletions to Make Array Beautiful
#

# @lc code=start
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        last = nums[0]
        count = 1
        n = len(nums)

        for i in nums[1:]:
            if count % 2 == 0 or last != i:
                last = i
                count += 1

        if count % 2 == 0:
            return n - count
        
        return n - count + count % 2

# @lc code=end

