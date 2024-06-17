import math


# Quite simple and intuitive solution. Time complexity O(sqrt(n))
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        mid = math.floor(math.sqrt(c // 2))
        for i in range(mid + 1):
            if math.sqrt(c - i*i) % 1 == 0:
                return True
        return False
