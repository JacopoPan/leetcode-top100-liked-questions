"""
Runtime: 211 ms, faster than 64.53% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.4 MB, less than 55.02% of Python3 online submissions for Search a 2D Matrix II.
"""
from typing import List
from typing import Optional

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        row, col = rows-1, columns-1
        for r in range(rows):
            if matrix[r][0] <= target and matrix[r][-1] >= target:
                search_in = matrix[r][:]
                while True:
                    if search_in[len(search_in)//2] == target:
                        return True
                    elif len(search_in)==1:
                        break
                    elif search_in[len(search_in)//2] > target:
                        search_in = search_in[:len(search_in)//2]
                    else:
                        search_in = search_in[len(search_in)//2:]
        return False

def main():
    sol = Solution()
    print('Output:', sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
    print('Expected:', True)

if __name__ == "__main__":
    main()
