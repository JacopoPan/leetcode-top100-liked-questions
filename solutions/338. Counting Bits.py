"""
Runtime: 107 ms, faster than 68.02% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 83.65% of Python3 online submissions for Counting Bits.
"""
from typing import List
from typing import Optional
import math

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        else:
            ans = [0, 1]
            for i in range(int(math.log2(n))):
                ans = ans + [i+1 for i in ans]
            return ans[:n+1]

def main():
    sol = Solution()
    print('Output:', sol.countBits(5))
    print('Expected:', [0,1,1,2,1,2])

if __name__ == "__main__":
    main()
