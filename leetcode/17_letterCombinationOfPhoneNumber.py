from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        n = len(digits)

        res = []

        def helper(index, current_combination):
            if index == n:
                res.append(current_combination)
                return

            for c in dictionary[digits[index]]:
                helper(index+1, current_combination + c)

        helper(0, "")
        
        return res