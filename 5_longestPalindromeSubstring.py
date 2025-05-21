# The naive idea is to loop through all substrings, then check if each of them is a palindrome. -> O(n^3): O(n^2) for all substrings traversal, O(n) for palindrome check
# One way to optimize it is we can somehow "memorize" the previous calculated palindrome, and use 
# that result to quickly calculate the next one.
# The following is the solution:
# If s[l:r] is a palindrome, s[l-1:r+1] is a palindrome if s[l-1] = s[r]
# This approach reduces the overall time complexity to O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = None
        resLength = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    res = s[l: r+1]
                    resLength = r - l + 1
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    res = s[l: r+1]
                    resLength = r - l + 1
                l -= 1
                r += 1
        return res