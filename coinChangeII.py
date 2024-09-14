from typing import List

# An important note is that in the inner loop of j, j is incremental which means we can pick a coin any number of times.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]
        return dp[amount]

