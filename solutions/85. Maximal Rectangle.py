"""
Runtime: 500 ms, faster than 29.13% of Python3 online submissions for Maximal Rectangle.
Memory Usage: 15.1 MB, less than 92.44% of Python3 online submissions for Maximal Rectangle.
"""
from typing import List
from typing import Optional

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        ones_in_col_up_to_row = [0] * cols
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    ones_in_col_up_to_row[c] += 1
                else:
                    ones_in_col_up_to_row[c] = 0
            max_area = max(max_area, self.maxRectangleUpToRow(ones_in_col_up_to_row))
        return max_area

    def maxRectangleUpToRow(self, heights) -> int:
        n = len(heights)
        stack = [-1]
        max_area = 0
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h*w)
            stack.append(i)
        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = n - stack[-1] - 1
            max_area = max(max_area, h*w)
        return max_area

def main():
    sol = Solution()
    print('Output:', sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print('Expected:', 6)

if __name__ == "__main__":
    main()
