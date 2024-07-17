from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def isPalindrome(ss):
            if len(ss) == 0:
                return False
            l = 0
            r = len(ss) - 1

            while l <= r:
                if ss[l] != ss[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def helper(current, index):
            if index == n:
                if isPalindrome(current[-1]):
                    res.append(current.copy())
                return

            if len(current) == 0 or isPalindrome(current[-1]):
                current.append(s[index])
                helper(current, index+1)
                current.pop()
            
            if len(current) > 0:
                current[-1] += s[index]
                helper(current, index + 1)
    
        helper([], 0)
        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))