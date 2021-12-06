"""
Runtime: 36 ms, faster than 67.35% of Python3 online submissions for Rotate Image.
Memory Usage: 14.3 MB, less than 60.70% of Python3 online submissions for Rotate Image.
"""
from typing import List
from typing import Optional

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N):
            for j in range(i,N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
        for i in range(N):
            matrix[i].reverse()

def main():
    sol = Solution()
    inp = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(inp)
    print('Output:', inp)
    print('Expected:', [[7,4,1],[8,5,2],[9,6,3]])

if __name__ == "__main__":
    main()
