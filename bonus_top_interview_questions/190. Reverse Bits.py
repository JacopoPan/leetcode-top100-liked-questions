"""
Runtime: 57 ms, faster than 25.80% of Python3 online submissions for Reverse Bits.
Memory Usage: 13.9 MB, less than 58.76% of Python3 online submissions for Reverse Bits.
"""
from typing import List
from typing import Optional

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = [0] * 32
        write_idx = 31
        while n > 0:
            binary[write_idx] = n%2
            n = n//2
            write_idx -= 1
        ans = 0
        for read_idx in range(31,-1,-1):
            ans = 2*ans + binary[read_idx]
        return ans

def main():
    sol = Solution()
    print('Output:', sol.reverseBits(43261596))
    print('Expected:', 964176192)

if __name__ == "__main__":
    main()
