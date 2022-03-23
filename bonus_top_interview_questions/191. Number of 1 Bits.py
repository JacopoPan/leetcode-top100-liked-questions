"""
Runtime: 32 ms, faster than 89.11% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.8 MB, less than 57.30% of Python3 online submissions for Number of 1 Bits.
"""
from typing import List
from typing import Optional

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n%2
            n = n//2
        return ans

def main():
    sol = Solution()
    print('Output:', sol.hammingWeight(11))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
