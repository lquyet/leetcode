from typing import List

def join(a, b):
    if a is None and b is None:
        return None
    elif a is not None:
        return a
    elif b is not None:
        return b
    return None

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        res = self.search(nums, l, r)
        return res


    def search(self, nums, l, r):
        if l > r:
            return None
        
        mid = (l + r) // 2
        # print(l, r, mid)
        if mid == 0:
            if nums[mid] < nums[mid + 1] and nums[mid] < nums[len(nums) - 1]:
                return nums[mid]
            else:
                return self.search(nums, mid + 1, r)
        elif mid == len(nums) - 1:
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[0]:
                return nums[mid]
            else:
                return self.search(nums, l, mid - 1)
        elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
            return nums[mid]
        else:
            return join(self.search(nums, l, mid - 1), self.search(nums, mid + 1, r))


if __name__ == "__main__":
    nums = [2,1]
    solution = Solution()
    print(solution.findMin(nums))