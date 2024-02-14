from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # store indices to know if an element is out of window
        res = []

        for i in range(len(nums)):
            while len(q) > 0 and nums[q[-1]] < nums[i]:
                q.pop()

            while len(q) > 0 and q[0] < i - k + 1:
                q.popleft()
            
            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res
    
if __name__ == "__main__":
    s = Solution()
    nums = [7, 2, 4]
    k = 2
    print(s.maxSlidingWindow(nums, k))
