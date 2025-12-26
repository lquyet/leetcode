from typing import List


# the basic idea is when we meet a upward trend, we need to find all
# the previous temperature that is lower than the current one (consecutively)
# and update the result array.
# so using a stack is a good idea, since we only need the recent temperatures

# another approach is to start from the right side and when we meet temperatures[i],
# the stack stores those temperatures that are higher than temperatures[i] (from temperatures[i+1] to temperatures[n-1])
# and we can pop those temperatures that are lower than temperatures[i] from the stack (top down), then
# insert temperatures[i] into the stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in temperatures]
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(i)
                continue
            while len(stack) > 0 and t > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res


def main():
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))


if __name__ == "__main__":
    main()
