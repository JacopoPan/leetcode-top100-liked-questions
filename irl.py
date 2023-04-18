'''Question 1:  Given a graph grid of water and land, write a function that
return the number of islands on the grid. An island is a vertically or 
horizontally connected region of Land.
'''

from collections import deque

class Problem:
    def __init__(self):
        pass

    def islandCount(self, grid) -> int:
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'L':
                    num_islands += 1
                    grid[row][col] = 'E'
                    q = deque([(row,col)])
                    while len(q) > 0:
                        curr_row, curr_col = q.popleft()
                        if curr_row < len(grid)-1:
                            if grid[curr_row+1][curr_col] == 'L':
                                grid[curr_row+1][curr_col] = 'E'
                                q.append((curr_row+1, curr_col))
                        if curr_row > 0:
                            if grid[curr_row-1][curr_col] == 'L':
                                grid[curr_row-1][curr_col] = 'E'
                                q.append((curr_row-1, curr_col))
                        if curr_col < len(grid[0])-1:
                            if grid[curr_row][curr_col+1] == 'L':
                                grid[curr_row][curr_col+1] = 'E'
                                q.append((curr_row, curr_col+1))
                        if curr_col > 0:
                            if grid[curr_row][curr_col-1] == 'L':
                                grid[curr_row][curr_col-1] = 'E'
                                q.append((curr_row, curr_col-1))      
        return num_islands

def main():
    sol = Problem()
    test_case1 = [
                ['W', 'W'],
                ['W', 'W'],
                ['W', 'W'],
            ]
    test_case2 = [ 
            ['L', 'L', 'L'],
            ['L', 'L', 'L'],      
            ['L', 'L', 'L'],
            ]
    test_case3 = [ 
            ['L', 'L', 'L'],
            ['L', 'W', 'L'],      
            ['L', 'L', 'L'],
            ]
    test_case4 = [ 
            ['L', 'W', 'L'],
            ['W', 'L', 'W'],      
            ['L', 'W', 'L'],
            ]
    print(sol.islandCount(test_case1))
    print(sol.islandCount(test_case2))
    print(sol.islandCount(test_case3))
    print(sol.islandCount(test_case4))


if __name__ == "__main__":
    print('IRL')

    main()
