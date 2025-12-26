from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        lw = len(word)
        lb = len(board)
        lb0 = len(board[0])

        def backtrack(i, j, l):
            if l == lw:
                return True
            
            if board[i][j] != word[l]:
                return False
            
            if visited[i][j]:
                return False
            
            # handle the case when word is of length 1
            if l == lw-1:
                return True

            visited[i][j] = True
            if i > 0 and backtrack(i-1, j, l+1):
                return True
            if i < lb-1 and backtrack(i+1, j, l+1):
                return True
            if j > 0 and backtrack(i, j-1, l+1):
                return True
            if j < lb0-1 and backtrack(i, j+1, l+1):
                return True
            visited[i][j] = False
            
            return False

            
        for i in range(lb):
            for j in range(lb0):
                if backtrack(i, j, 0):
                    return True
        return False

if __name__ == "__main__":
    # Test case 1
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word1 = "ABCCED"
    solution = Solution()
    print(solution.exist(board1, word1))  # Expected output: True

    # Test case 2
    board2 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word2 = "SEE"
    solution = Solution()
    print(solution.exist(board2, word2))  # Expected output: True

    # Test case 3
    board3 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word3 = "ABCB"
    solution = Solution()
    print(solution.exist(board3, word3))  # Expected output: False