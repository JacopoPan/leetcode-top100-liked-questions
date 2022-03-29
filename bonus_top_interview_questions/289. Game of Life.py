"""
Runtime: 57 ms, faster than 28.89% of Python3 online submissions for Game of Life.
Memory Usage: 14 MB, less than 52.07% of Python3 online submissions for Game of Life.
"""
from typing import List
from typing import Optional

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        flip = []
        for i in range(rows):
            for j in range(cols):
                count = self.neighborCount(i, j, board)
                if (board[i][j]==1 and count<2) \
                    or (board[i][j]==1 and count>3) \
                    or (board[i][j]==0 and count==3):
                    flip.append([i,j])
        for pair in flip:
            if board[pair[0]][pair[1]] == 1:
                 board[pair[0]][pair[1]] = 0
            else:
                 board[pair[0]][pair[1]] = 1
    
    def neighborCount(self, i: int, j: int, board: List[List[int]]) -> int:
        rows = len(board)
        cols = len(board[0])
        neighbors = []
        for x in [i-1, i ,i+1]:
            for y in [j-1, j ,j+1]:
                if x >= 0 and x < rows and y >= 0 and y < cols:
                    if not (x==i and y==j):
                        neighbors.append(board[x][y])
        return sum(neighbors)

def main():
    sol = Solution()
    inp = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    sol.gameOfLife(inp)
    print('Output:', inp)
    print('Expected:', [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])

if __name__ == "__main__":
    main()
