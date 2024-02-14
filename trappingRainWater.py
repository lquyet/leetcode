from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # if len(height) <= 1:
        #     return 0
        #
        # highest_heights = [0 for _ in height]  # highest_heights[i] mean the highest height from i+1 to the end
        # highest_heights[-1] = -1
        #
        # for i in reversed(range(len(height) - 1)):
        #     highest_heights[i] = max(height[i + 1], highest_heights[i + 1])
        # total = 0
        # s = 0
        # e = 1
        # water = 0
        # while e < len(height):
        #     if height[s] > highest_heights[s]:
        #         s += 1
        #         e = s + 1
        #         continue
        #     if height[e] >= height[s]:
        #         if e - s == 1:
        #             s = e
        #             e += 1
        #         else:
        #             # calculate water
        #             water += (e - s - 1) * height[s] - sum(height[s + 1:e])
        #             total += water
        #             s = e
        #             e += 1
        #             water = 0
        #     else:
        #         e += 1
        # return total


        # Stack-base solution
        # another solution using 2 sums from left and right can be found here: https://www.youtube.com/watch?v=ZI2z5pq0TqA
        # or just view solutions page on leetcode
        if len(height) == 0:
            return 0

        stack = []
        total = 0
        i = 0

        while i < len(height):
            if len(stack) == 0 or height[i] < height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                bot = stack.pop()
                if len(stack) == 0:
                    continue
                total += (min(height[i], height[stack[-1]]) - height[bot]) * (i - stack[-1] - 1)
        return total


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))


if __name__ == "__main__":
    main()
