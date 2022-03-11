"""
Runtime: 1546 ms, faster than 64.71% of Python3 online submissions for Perfect Squares.
Memory Usage: 205.1 MB, less than 5.05% of Python3 online submissions for Perfect Squares.
"""
from typing import List
from typing import Optional
import math

class Solution:
    def numSquares(self, n: int) -> int:
        values = []
        for i in range(1,math.floor(math.sqrt(n))+1):
            values.append(i**2)
        if n in values:
            return 1
        steps = 1
        attempts = values
        while True:
            new_attempts = []
            steps += 1
            for a in attempts:
                for v in values:
                    if a+v == n:
                        return steps
                    elif a+v < n:
                        new_attempts.append(a+v)
                    elif a+v > n:
                        break
            attempts = new_attempts

def main():
    sol = Solution()
    print('Output:', sol.numSquares(12))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
