from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        non_duplicated_nums = list(dict.fromkeys(nums))
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        minn = self.getK(non_duplicated_nums, 0, len(non_duplicated_nums) - 1, freq, k)
        res = []
        for k in freq:
            if freq[k] >= freq[minn]:
                res.append(k)
        return res

    def partition(self, nums: List[int], l: int, r: int, m: dict):
        # the right most is pivot
        pivot = r
        swapIndex = l
        for i in range(l, r):
            if m[nums[i]] < m[nums[pivot]]:
                # move to the left of the pivot if smaller
                nums[swapIndex], nums[i] = nums[i], nums[swapIndex]
                swapIndex += 1
        # move the pivot
        nums[swapIndex], nums[pivot] = nums[pivot], nums[swapIndex]
        # partition the right side of the pivot since we need to find the k most...
        return swapIndex

    def getK(self, nums: List[int], l: int, r: int, m: dict, k: int):
        if 0 < k <= r - l + 1:
            index = self.partition(nums, l, r, m)

            if r - index + 1 == k:
                return nums[index]

            if r - index + 1 > k:
                return self.getK(nums, index + 1, r, m, k)
            else:
                # NOTE that the k is changed here. Draw to visualize to understand.
                return self.getK(nums, l, index - 1, m, k - (r - index + 1))


def main():
    nums = [2,3,4,1,4,0,4,-1,-2,-1]
    k = 2
    solution = Solution()
    print(solution.topKFrequent(nums, k))


if __name__ == "__main__":
    main()
