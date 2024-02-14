from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find minimum value then do binary search on the corresponding side
        min_index = self.find_min(nums)
        if target == nums[min_index]:
            return min_index
        elif target == nums[-1]:
            return len(nums) - 1
        elif target == nums[0]:
            return 0
        elif target > nums[-1]:
            return self.binary_search(nums, target, 0, min_index - 1)
        else:
            return self.binary_search(nums, target, min_index, len(nums) - 1)

    def binary_search(self, nums, target, l, r) -> int:
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1


    # find_min returns the index of the minimum value in nums in O(logN) time 
    def find_min(self, nums) -> int:
        l, r = 0, len(nums) - 1

        if r == 0:
            return r

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return l

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4,5,6,7,0,1,2], 3)) # -1