from typing import List


# we might come up with an idea that after add a open bracket, there are 2 possible ways to add another bracket
# 1. add a open bracket
# 2. add a close bracket
# Bruteforce is possible, but very complicated to implement
# So we use recursion to "bruteforce" it in a more elegant way

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(current, open, close):
            if open == 0 and close == 0:
                res.append(current)
                return
            
            if open > 0:
                helper(current+"(", open-1, close+1)
            
            if close > 0:
                helper(current+")", open, close-1)
        
        helper("", n, 0)
        return res


def main():
    print(Solution().generateParenthesis(3))


if __name__ == "__main__":
    main()
