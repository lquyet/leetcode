from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        res = 0
        seen = [
            [0 for _ in range(col)] for _ in range(row)
        ]
    
        def helper(i, j, seen):
            print("calling: ", i, j)
            if i < 0 or i >= row or j < 0 or j >= col:
                return 0

            if seen[i][j]:
                return 0

            # visit current cell
            seen[i][j] = 1
            
            if grid[i][j] == 0:
                return 0

            top = helper(i-1, j, seen)
            bottom = helper(i+i, j, seen)
            left = helper(i, j-1, seen)
            right = helper(i, j+1, seen)

            return 1 + top + bottom + left + right
        
        for r in range(row):
            for c in range(col):
                connected = helper(r, c, seen)
                print(r, c, connected)
                if connected > 1:
                    res += connected

        return res
            

        

# Generate test
grid = [[1,0],[1,1]]
sol = Solution()
print(sol.countServers(grid)) # Expected 4