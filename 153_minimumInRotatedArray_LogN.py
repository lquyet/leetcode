from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        mid = (l + r) // 2

        while l < r:
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
            mid = (l + r) // 2
        return nums[l]
    

if __name__ == "__main__":
    nums = [2,1]
    solution = Solution()
    print(solution.findMin(nums))