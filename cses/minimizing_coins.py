# https://cses.fi/problemset/task/1634/

import sys

input = sys.stdin.readline
print = sys.stdout.write

n, x = map(int, input().split())    # n: number of coins, x: desired sum of money

coins = list(map(int, input().split()))

dp = [0]*(x+1)
dp[0] = 1


for coin in coins:
    for i in range(x+1):
        if i >= coin:
            dp[i] += dp[i-coin]

print(str(dp[x]))
