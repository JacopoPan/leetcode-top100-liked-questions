"""
Runtime: 147 ms, faster than 29.00% of Python3 online submissions for Power of Three.
Memory Usage: 14 MB, less than 11.57% of Python3 online submissions for Power of Three.
"""
from typing import List
from typing import Optional

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1 or n == 3:
            return True
        val = 3
        while val < n:
            val *=3
            if val == n:
                return True
        return False

def main():
    sol = Solution()
    print('Output:', sol.isPowerOfThree(27))
    print('Expected:', True)

if __name__ == "__main__":
    main()
