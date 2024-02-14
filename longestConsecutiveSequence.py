from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = list(set(nums))
        max_len = None
        m = {}
        # m[i] means the length of the longest consecutive sequence that CONTAINS i
        for i in nums:
            m[i] = 1
            if i - 1 in m:
                m[i] += m[i - 1]
            if i + 1 in m:
                m[i] += m[i + 1]

            if i - 1 in m:
                m[i - m[i-1]] = m[i]
            if i + 1 in m:
                m[i + m[i+1]] = m[i]

            if max_len is None or m[i] > max_len:
                max_len = m[i]

        return max_len

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) == 0: return 0
    #     nums = set(nums)
    #     max_len = 1
    #     for i in nums:
    #         if i - 1 in nums:
    #             continue
    #         else:
    #             temp = i+1
    #             while temp in nums:
    #                 temp += 1
    #             max_len = max(max_len, temp-i)
    #     return max_len


def main():
    nums = [-3, 2, 8, 5, 1, 7, -8, 2, -8, -4, -1, 6, -6, 9, 6, 0, -7, 4, 5, -4, 8, 2, 0, -2, -6, 9, -4, -1]
    print(Solution().longestConsecutive(nums))


if __name__ == "__main__":
    main()
