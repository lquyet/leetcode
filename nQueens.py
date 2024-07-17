from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        current = []
        board = [['.' for i in range(n)] for j in range(n)]

        def canPlace(x, y):
            for [px, py] in current:
                if x - px == 0 or y - py == 0 or \
                (abs(x-px) == (x-py)):
                    return False
            return True

        def helper(current, index):
            if index == n:
                res.append(board.copy())
                return
            
            for y in range(n):
                if canPlace(index, y):
                    current.append([index, y])
                    board[index][y] = 'Q'
                    helper(current, index + 1)
                    current.pop()
                    board[index][y] = '.'
        


