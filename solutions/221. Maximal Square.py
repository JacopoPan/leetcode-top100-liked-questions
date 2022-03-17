"""
Runtime: 859 ms, faster than 34.17% of Python3 online submissions for Maximal Square.
Memory Usage: 16.5 MB, less than 69.25% of Python3 online submissions for Maximal Square.
"""
from typing import List
from typing import Optional
from copy import deepcopy

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        cache = deepcopy(matrix)
        ones = False
        for i in range(rows):
            for j in range(cols):
                cache[i][j] = int(cache[i][j])
                if cache[i][j]==1 and not ones:
                    ones = True
        if not ones:
            return 0
        max_edge = 1
        for i in range(1, rows):
            for j in range(1, cols):
                if int(cache[i][j]) == 1:
                    val_1 = min(cache[i-1][j-1], cache[i-1][j])
                    val_2 = min(val_1, cache[i][j-1])
                    cache[i][j] = val_2 + 1
                    max_edge = max(max_edge, cache[i][j])
        return max_edge**2

def main():
    sol = Solution()
    print('Output:', sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print('Expected:', 4)

if __name__ == "__main__":
    main()
