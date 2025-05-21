from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.l = [i for i in range(1, n + 1)]
        
        return self.helper(n, k)
    
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        return n * self.factorial(n - 1)
    
    def helper(self, n, k):
        if len(self.l) == 1:
            return str(self.l[0])

        # calculate the current first digit

        fac = self.factorial(n - 1)

        digit_index = (k-1) // fac
        if digit_index > len(self.l) - 1:
            digit_index = digit_index % (len(self.l) - 1)

        res = self.l[digit_index]

        # remove that digit in l
        self.l.remove(res)
        return str(res) + self.helper(n - 1, k - digit_index * fac)

if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(3, 2)) # "213"