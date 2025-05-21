from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums) - 1, target)

    def helper(self, nums, l, r, target) -> int:
        if l >= r:
            if nums[l] == target:
                return l
            return -1

        mid = l + (r-l)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.helper(nums, l, mid-1, target)
        else:
            return self.helper(nums, mid+1, r, target)



def main():
    print(Solution().search([2,5], 0))

if __name__ == "__main__":
    main()