from typing import List


# we might come up with an idea that after add a open bracket, there are 2 possible ways to add another bracket
# 1. add a open bracket
# 2. add a close bracket
# Bruteforce is possible, but very complicated to implement
# So we use recursion to "bruteforce" it in a more elegant way


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, n, "", res)
        return res

    def helper(self, open: int, close: int, current: str, res: List[str]):
        if open == close == 0:
            res.append(current)
            return

        if open == 0:
            # add all close
            self.helper(open, 0, current + ")" * close, res)
            return

        if open == close:
            # add open bracket
            current += "("
            self.helper(open - 1, close, current, res)
        elif open < close:
            self.helper(open - 1, close, current + "(", res)
            self.helper(open, close - 1, current + ")", res)


def main():
    print(Solution().generateParenthesis(3))


if __name__ == "__main__":
    main()
