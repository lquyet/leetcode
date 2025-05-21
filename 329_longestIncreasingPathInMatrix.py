from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        max_length = 1

        def helper(cl, prev_i, prev_j, i, j):
            if i<0 or j < 0 or i > n-1 or j > m-1:
                return cl
            
            if matrix[i][j] > matrix[prev_i][prev_j] or (prev_i == i and prev_j == j):
                if dp[i][j] > 0:
                    return cl + dp[i][j]
                
                top = helper(cl+1, i, j, i-1, j)
                bottom = helper(cl+1, i, j, i+1, j)
                left = helper(cl+1, i, j, i, j-1)
                right = helper(cl+1, i, j, i, j+1)

                return max(top, bottom, left, right)
            
            return cl
        
        for ii in range(n):
            for jj in range(m):
                # print(f"processing: {ii}:{jj}")
                dp[ii][jj] = helper(0, ii, jj, ii, jj)
                max_length = max(max_length, dp[ii][jj])
        return max_length

def main():
    matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
    print(Solution().longestIncreasingPath(matrix))

main()