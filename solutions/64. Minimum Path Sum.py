"""
Runtime: 312 ms, faster than 5.05% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15 MB, less than 93.25% of Python3 online submissions for Minimum Path Sum.
"""
from typing import List
from typing import Optional

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        reached = [[0, 0]]
        costs = [grid[0][0]]
        rows = len(grid)
        cols = len(grid[0])
        if rows == 1 and cols == 1:
            return grid[0][0]
        while not [rows-1, cols-1] in reached:
            new_reached = []
            new_costs = []
            for idx, s in enumerate(reached):
                move_right = [s[0], s[1]+1]
                if move_right[1] < cols:
                    if not move_right in new_reached:
                        new_reached.append(move_right)
                        new_costs.append(costs[idx] + grid[move_right[0]][move_right[1]])
                    else:
                        old_cost = new_costs[new_reached.index(move_right)]
                        new_cost = costs[idx] + grid[move_right[0]][move_right[1]]
                        new_costs[new_reached.index(move_right)] = min(old_cost, new_cost)
                move_down = [s[0]+1, s[1]]
                if move_down[0] < rows:
                    if not move_down in new_reached:
                        new_reached.append(move_down)
                        new_costs.append(costs[idx] + grid[move_down[0]][move_down[1]])
                    else:
                        old_cost = new_costs[new_reached.index(move_down)]
                        new_cost = costs[idx] + grid[move_down[0]][move_down[1]]
                        new_costs[new_reached.index(move_down)] = min(old_cost, new_cost)
            reached = new_reached
            costs = new_costs
            if [rows-1, cols-1] in reached:
                return costs[reached.index([rows-1, cols-1])]

def main():
    sol = Solution()
    print('Output:', sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print('Expected:', 7)

if __name__ == "__main__":
    main()
