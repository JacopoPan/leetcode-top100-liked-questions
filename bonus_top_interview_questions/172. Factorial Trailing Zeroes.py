"""
Runtime: 108 ms, faster than 33.37% of Python3 online submissions for Factorial Trailing Zeroes.
Memory Usage: 14.2 MB, less than 6.93% of Python3 online submissions for Factorial Trailing Zeroes.
"""
from typing import List
from typing import Optional

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            return int(n/5 + self.trailingZeroes(n/5))

def main():
    sol = Solution()
    print('Output:', sol.trailingZeroes(12))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
