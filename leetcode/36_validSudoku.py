from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.is_valid(board[i]):
                return False

        for i in range(9):
            col = [j[i] for j in board]
            if not self.is_valid(col):
                return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                v = [board[i + m][j + n] for m in [0, 1, 2] for n in [0, 1, 2]]
                if not self.is_valid(v):
                    return False

        return True

    def is_valid(self, values):
        vs = [i for i in values if i != '.']
        m = {}
        for v in vs:
            if v in m:
                return False
            else:
                m[v] = 1
        return True


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().isValidSudoku(board))


if __name__ == '__main__':
    main()
