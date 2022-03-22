"""
Runtime: 2038 ms, faster than 16.45% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.9 MB, less than 66.65% of Python3 online submissions for Sqrt(x).
"""
from typing import List
from typing import Optional

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        for i in range(x+1):
            if i*i > x:
                return i-1

def main():
    sol = Solution()
    print('Output:',sol.mySqrt(4))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
