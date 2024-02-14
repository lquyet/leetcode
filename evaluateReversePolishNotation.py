from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(self.perform(token, n2, n1))
            else:
                stack.append(int(token))
        return stack.pop()

    def perform(self, operator, n1, n2):
        if operator == '-':
            return n1 - n2
        elif operator == '+':
            return n1 + n2
        elif operator == '*':
            return n1 * n2
        elif operator == '/':
            return int(n1 / n2)


def main():
    print(Solution().evalRPN(["4","13","5","/","+"]))


if __name__ == "__main__":
    main()
