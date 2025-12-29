class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        m = {}
        currentStart = 0
        maxLen = 0

        for i in range(n):
            if s[i] in m:
                if m[s[i]] < currentStart:
                    m[s[i]] = i
                else:
                    # Should terminate at i-1
                    maxLen = max(i-currentStart, maxLen)
                    currentStart = m[s[i]] + 1
                    m[s[i]] = i
            else:
                m[s[i]] = i

        # Should terminate at i == n-1
        maxLen = max(i-currentStart+1, maxLen)
        return maxLen
    

if __name__ == "__main__":
    solution = Solution()
    input = "dvdf"
    output = solution.lengthOfLongestSubstring(input)
    print(output)