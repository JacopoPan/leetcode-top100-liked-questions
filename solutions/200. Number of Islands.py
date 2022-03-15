"""
Runtime: 488 ms, faster than 35.46% of Python3 online submissions for Number of Islands.
Memory Usage: 23.8 MB, less than 9.86% of Python3 online submissions for Number of Islands.
"""
from typing import List
from typing import Optional

class Solution:
    
    def __init__(self):
        self.rows = None
        self.cols = None
        self.temp = []
        self.explored = {}
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        counter = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '1':
                    name = str(i)+'-'+str(j)
                    if name in self.explored.keys():
                        continue
                    counter += 1
                    self.temp = []
                    self.findAllConnectedLand(grid, i, j)
                    for s in self.temp:
                        self.explored[s] = True
        return(counter)

    def findAllConnectedLand(self, grid: List[List[str]], i: int, j: int):
        this_name = str(i)+'-'+str(j)
        if this_name in self.temp:
            return
        else:
            self.temp.append(this_name)
            if i-1 >= 0 and grid[i-1][j]=='1' and str(i-1)+'-'+str(j) not in self.temp:
                self.findAllConnectedLand(grid, i-1, j)
            if i+1 < self.rows and grid[i+1][j]=='1' and str(i+1)+'-'+str(j) not in self.temp:
                self.findAllConnectedLand(grid, i+1, j)
            if j-1 >= 0 and grid[i][j-1]=='1' and str(i)+'-'+str(j-1) not in self.temp:
                self.findAllConnectedLand(grid, i, j-1)
            if j+1 < self.cols and grid[i][j+1]=='1' and str(i)+'-'+str(j+1) not in self.temp:
                self.findAllConnectedLand(grid, i, j+1)        

def main():
    sol = Solution()
    print('Output:', sol.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
    print('Expected:', 1)

if __name__ == "__main__":
    main()
