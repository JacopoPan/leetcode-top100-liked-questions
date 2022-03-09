"""
Runtime: 8509 ms, faster than 25.13% of Python3 online submissions for Word Search.
Memory Usage: 14 MB, less than 68.71% of Python3 online submissions for Word Search.
"""
from typing import List
from typing import Optional
import math

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.searchFrom(board, i, j, word):
                    return True
        return False 

    def searchFrom(self, board: List[List[str]], row: int, col: int, word: str) -> bool:
        if len(word) == 0:
            return True
        if (row >= len(board)) or (row < 0) or (col >= len(board[0])) or (col < 0) or board[row][col] != word[0]:
            return False
        temp = board[row][col]
        board[row][col] = -1
        ans = self.searchFrom(board, row+1, col, word[1:]) or \
            self.searchFrom(board, row-1, col, word[1:]) or \
            self.searchFrom(board, row, col+1, word[1:]) or \
            self.searchFrom(board, row, col-1, word[1:])
        board[row][col] = temp
        return ans

def main():
    sol = Solution()
    print('Output:', sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
    print('Expected:', False)

if __name__ == "__main__":
    main()
