# We can solve this problem in O(1) by solving the equation
# x(x+1)/2 = (n+x)(n-x+1)/2
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = (n*n + n) / 2
        return int(x**0.5) if x**0.5 == int(x**0.5) else -1
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.pivotInteger(8))