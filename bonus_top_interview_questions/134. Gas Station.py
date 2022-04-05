"""
Runtime: 716 ms, faster than 86.07% of Python3 online submissions for Gas Station.
Memory Usage: 19.2 MB, less than 71.74% of Python3 online submissions for Gas Station.
"""
from typing import List
from typing import Optional
import math

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_surplus = 0
        surplus = 0
        start = 0
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        if total_surplus < 0:
            return -1
        else:
            return start

def main():
    sol = Solution()
    print('Output:', sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
