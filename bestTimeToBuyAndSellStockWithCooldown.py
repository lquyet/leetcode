from typing import List

# Using the same idea as this brilliant guy on LC who came up with a Finite State Machine
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/75928/share-my-dp-solution-by-state-machine-thinking/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        s0 = [None] * n
        s1 = [None] * n
        s2 = [None] * n

        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = 0

        for i in range(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]
        
        return max(s0[n-1], s1[n-1], s2[n-1])
