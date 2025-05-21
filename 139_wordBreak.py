from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) 
        
        def helper(s, i):
            if i == n:
                return True
            if i > n:
                return False
            
            for w in wordDict:
                if s[i:i+len(w)] == w and helper(s, i+len(w)):
                    return True
        
        return helper(s, 0)