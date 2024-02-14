from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerBound = max(sum(piles) // h, 1)
        upperBound = max(piles)

        while lowerBound < upperBound:
            mid = (lowerBound + upperBound) // 2
            sumHours = 0
            for pile in piles:
                sumHours += pile // mid
                if pile % mid != 0:
                    sumHours += 1
            if sumHours <= h:
                upperBound = mid
            elif sumHours > h:
                lowerBound = mid + 1
        
        return lowerBound
    

if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    solution = Solution()
    print(solution.minEatingSpeed(piles, h))