from typing import List

# Naive with hashset
# Time complexity: O(n)
# Space complexity: O(n)
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         s = set()
#         for i in nums:
#             if i not in s:
#                 s.add(i)
#             else:
#                 return i
#         return None

# Floyd's Tortoise and Hare (Cycle Detection)
# Time complexity: O(n)
# Space complexity: O(1)
# The idea is that we can think about nums[i] as a pointer to the next node in a linked list.
# For instance, if nums[0] = 1, we can think of this as a pointer pointing to the node at index 1 in the list.
# Note that the numbers are in range [1, n], and there are n+1 numbers in nums, which means there is at least 
# 1 duplicate number.  
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[0], nums[0]

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast
            
if __name__ == "__main__":
    solution = Solution()
    print(solution.findDuplicate([2,5,9,6,9,3,8,9,7,1]))  # 2
