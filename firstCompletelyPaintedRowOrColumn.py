from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        store = {}
        m = len(mat)
        n = len(mat[0])
        length = len(arr)

        for i in range(m):
            for j in range(n):
                store[mat[i][j]] = (i, j)
        
        count_row = [0] * m
        count_col = [0] * n

        for i in range(length):
            row = store[arr[i]][0]
            col = store[arr[i]][1]

            count_row[row] += 1
            count_col[col] += 1

            if count_row[row] == n or count_col[col] == m:
                return i
            
        
            