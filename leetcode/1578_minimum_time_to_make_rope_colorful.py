from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        if n == 1:
            return 0

        r = [0]

        for i in range(1, n):
            if colors[i] != colors[r[-1]]:
                r.append(i)
                continue
            
            if neededTime[i] > neededTime[r[-1]]:
                r[-1] = i
        
        originalSum = sum(neededTime)
        target = 0
        for i in r:
            target += neededTime[i]
        
        return originalSum - target
            