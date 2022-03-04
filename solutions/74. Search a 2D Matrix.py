"""
Runtime: 56 ms, faster than 64.54% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.4 MB, less than 69.06% of Python3 online submissions for Search a 2D Matrix.
"""
from typing import List
from typing import Optional

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = 0, 0
        while True:
            val = matrix[row][column]
            if val == target:
                return True
            if row < len(matrix)-1 or column < len(matrix[0])-1:
                if row < len(matrix)-1 and target >= matrix[row+1][0]:
                    row += 1
                elif column < len(matrix[0])-1:
                    column += 1
                else:
                    break
            else:
                break 
        return False

def main():
    sol = Solution()
    print('Output:', sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print('Expected:', True)

if __name__ == "__main__":
    main()
