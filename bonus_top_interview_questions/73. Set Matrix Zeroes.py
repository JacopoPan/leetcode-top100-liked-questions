"""
Runtime: 156 ms, faster than 66.71% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 14.8 MB, less than 19.17% of Python3 online submissions for Set Matrix Zeroes.
"""
from typing import List
from typing import Optional

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroed_rows = []
        zeroed_cols = []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    if i not in zeroed_rows:
                        zeroed_rows.append(i)
                    if j not in zeroed_cols:
                        zeroed_cols.append(j)
        for r in zeroed_rows:
            for c in range(cols):
                matrix[r][c]=0
        for c in zeroed_cols:
            for r in range(rows):
                matrix[r][c]=0

def main():
    sol = Solution()
    inp = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(inp)
    print('Output:', inp)
    print('Expected:', [[1,0,1],[0,0,0],[1,0,1]])

if __name__ == "__main__":
    main()
