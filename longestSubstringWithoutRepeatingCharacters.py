class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        currentMap = {}
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        currentMap[s[0]] = 0
        start = 0

        for i in range(1, len(s)):
            if s[i] not in currentMap:
                dp[i] = dp[i - 1] + 1
            else:
                if currentMap[s[i]] >= start:
                    start = currentMap[s[i]] + 1
                    dp[i] = i - currentMap[s[i]]
                else:
                    dp[i] = dp[i - 1] + 1
            currentMap[s[i]] = i

        return max(dp)
    

if __name__ == "__main__":
    solution = Solution()
    input = "dvdf"
    output = solution.lengthOfLongestSubstring(input)
    print(output)