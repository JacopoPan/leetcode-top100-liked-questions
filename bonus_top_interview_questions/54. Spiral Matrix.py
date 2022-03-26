"""
Runtime: 27 ms, faster than 96.00% of Python3 online submissions for Spiral Matrix.
Memory Usage: 14 MB, less than 9.73% of Python3 online submissions for Spiral Matrix.
"""
from typing import List
from typing import Optional

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        if rows > 0:
            cols = len(matrix[0])
        else:
            cols = 0
        if rows == 0 or cols == 0:
            return []
        if rows == 1 and cols == 1:
            return [matrix[0][0]]
        ans = []
        if rows == 1:
            for i in matrix[0]:
                ans.append(i)
            return ans
        if cols == 1:
            for i in matrix:
                ans.append(i[0])
            return ans
        for i in range(cols):
            ans.append(matrix[0][i])
        for i in range(1, rows):
            ans.append(matrix[i][cols-1])
        for i in range(cols-2, -1, -1):
            ans.append(matrix[rows-1][i])
        for i in range(rows-2, 0, -1):
            ans.append(matrix[i][0])     
        inside_matrix = []
        for i in range(rows-2):
            inside_matrix.append([])
            for j in range(cols-2):
                inside_matrix[i].append(matrix[i+1][j+1])
        ans += self.spiralOrder(inside_matrix)
        return ans

def main():
    sol = Solution()
    print('Output:', sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
    print('Expected:', [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])

if __name__ == "__main__":
    main()
