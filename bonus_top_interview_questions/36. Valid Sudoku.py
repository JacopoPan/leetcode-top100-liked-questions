"""
Runtime: 231 ms, faster than 5.19% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.9 MB, less than 48.77% of Python3 online submissions for Valid Sudoku.
"""
from typing import List
from typing import Optional
from copy import deepcopy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bak_search_cache = {}
        for i in range(10):
            bak_search_cache[str(i)] = 1
        for row in range(len(board)):
            search_cache = deepcopy(bak_search_cache)
            for elem in board[row]:
                if elem != '.':
                    search_cache[elem] -= 1
                    if search_cache[elem] < 0:
                        return False
        for col in range(len(board[0])):
            search_cache = deepcopy(bak_search_cache)
            for row in range(len(board)):
                val = board[row][col]
                if val != '.':
                    search_cache[val] -= 1
                    if search_cache[val] < 0:
                        return False
        for big_row in range(3):
            for big_col in range(3):
                search_cache = deepcopy(bak_search_cache)
                for row in range(3):
                    for col in range(3):
                        val = board[row+3*big_row][col+3*big_col]
                        if val != '.':
                            search_cache[val] -= 1
                            if search_cache[val] < 0:
                                return False
        return True

def main():
    sol = Solution()
    print('Output:', sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    print('Expected:', True)

if __name__ == "__main__":
    main()
