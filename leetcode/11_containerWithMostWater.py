from typing import List


# Inductive proof
# https://leetcode.com/problems/container-with-most-water/solutions/200246/proof-by-formula/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_area = 0

        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            # move right to get potentially larger area
            if height[l] < height[r]:
                l += 1
            # move left to get potentially larger area
            else:
                r -= 1

        return max_area


def main():
    height = [1, 1]
    print(Solution().maxArea(height))


if __name__ == "__main__":
    main()
