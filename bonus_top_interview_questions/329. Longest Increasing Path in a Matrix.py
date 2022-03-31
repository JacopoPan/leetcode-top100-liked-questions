"""
Runtime: 488 ms, faster than 85.56% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 16 MB, less than 58.01% of Python3 online submissions for Longest Increasing Path in a Matrix.
"""
from typing import List
from typing import Optional

class Solution:
    def __init__(self):
        self.cache = {}
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = -1
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        for i in range(self.rows):
            for j in range(self.cols):
                ans = max(ans, self.longestPathFrom(i,j))
        return ans
    
    def longestPathFrom(self, i: int, j: int) -> int:
        if (i,j) in self.cache.keys():
            return self.cache[(i,j)]
        ans = 1
        if i-1 >= 0:
            top = self.matrix[i-1][j]
            if top > self.matrix[i][j]:
                ans = max(ans, 1+self.longestPathFrom(i-1,j))
        if i+1 < self.rows:
            bottom = self.matrix[i+1][j]
            if bottom > self.matrix[i][j]:
                ans = max(ans, 1+self.longestPathFrom(i+1,j))
        if j-1 >= 0:
            left = self.matrix[i][j-1]
            if left > self.matrix[i][j]:
                ans = max(ans, 1+self.longestPathFrom(i,j-1))
        if j+1 < self.cols:
            right = self.matrix[i][j+1]
            if right > self.matrix[i][j]:
                ans = max(ans, 1+self.longestPathFrom(i,j+1))
        self.cache[(i,j)] = ans
        return ans

def main():
    sol = Solution()
    print('Output:', sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
    print('Expected:', 4)

if __name__ == "__main__":
    main()
