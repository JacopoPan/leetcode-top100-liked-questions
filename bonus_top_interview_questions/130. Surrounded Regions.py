"""
Runtime: 153 ms, faster than 80.27% of Python3 online submissions for Surrounded Regions.
Memory Usage: 15.2 MB, less than 87.41% of Python3 online submissions for Surrounded Regions.
"""
from typing import List
from typing import Optional

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        save = []
        for k in range(rows):
            save += (k, 0), (k, cols-1)
        for k in range(cols):
            save += (0, k), (rows-1, k)
        while len(save) > 0:
            i, j = save.pop()
            if (0 <= i < rows) and (0 <= j < cols) and (board[i][j] == 'O'):
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'

def main():
    sol = Solution()
    inp = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    sol.solve(inp)
    print('Output:', inp)
    print('Expected:', [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])

if __name__ == "__main__":
    main()
