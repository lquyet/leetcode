class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        dp = [1000 for _ in range(n+1)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[n-1], dp[n-2])