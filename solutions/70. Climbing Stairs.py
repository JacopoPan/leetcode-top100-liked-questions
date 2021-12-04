"""
Runtime: 32 ms, faster than 62.49% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.3 MB, less than 44.55% of Python3 online submissions for Climbing Stairs.
"""
from typing import List
from typing import Optional

class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:   
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if str(n-2) not in self.cache:
                self.cache[str(n-2)] = self.climbStairs(n-2)
            if str(n-1) not in self.cache:
                self.cache[str(n-1)] = self.climbStairs(n-1)
            return self.cache[str(n-2)] + self.cache[str(n-1)]

def main():
    sol = Solution()
    print('Output:', sol.climbStairs(2))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
