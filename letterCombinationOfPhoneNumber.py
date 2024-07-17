from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        dictionary = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        current = []
        n = len(digits)

        def helper(current, index):
            if index == n:
                res.append(''.join(current))
                return 
            
            for c in dictionary[digits[index]]:
                current.append(c)
                helper(current, index + 1)
                current.pop()
        
        helper(current, 0)
        return res