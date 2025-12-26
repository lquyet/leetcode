from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                continue
            prefix[i] = prefix[i - 1] * nums[i-1]

        for j in reversed(range(len(nums))):
            if j == len(nums) - 1:
                continue
            suffix[j] = suffix[j + 1] * nums[j+1]

        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res


def main():
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.productExceptSelf(nums))


if __name__ == "__main__":
    main()
