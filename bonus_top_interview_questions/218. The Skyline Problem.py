"""
Runtime: 104 ms, faster than 99.68% of Python3 online submissions for The Skyline Problem.
Memory Usage: 20.1 MB, less than 38.81% of Python3 online submissions for The Skyline Problem.
"""
from typing import List
from typing import Optional
from heapq import heappush, heappop
import math

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for _, R, _ in buildings] 
        events.sort()
        res = [[0, 0]]
        live = [(0, math.inf)]
        for pos, negH, R in events:
            while live[0][1] <= pos:
                heappop(live)
            if negH != 0:
                heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [ [pos, -live[0][0]] ]
        return res[1:]

def main():
    sol = Solution()
    print('Output:', sol.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    print('Expected:', [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])

if __name__ == "__main__":
    main()
