from typing import List

def i_to_xy(i, n):
    return (i//n, i%n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        v = self.helper(l, r, matrix, target)
        return v

    def helper(self, l, r, matrix, target):
        if l <= r:
            mid = (l+r) // 2
            x, y = i_to_xy(mid, len(matrix[0]))
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                return self.helper(l, mid-1, matrix, target)
            else:
                return self.helper(mid+1, r, matrix, target)
        return False


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 1
    solution = Solution()
    print(solution.searchMatrix(matrix, target))

