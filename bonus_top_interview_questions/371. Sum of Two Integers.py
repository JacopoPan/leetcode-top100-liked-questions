"""
Runtime: 59 ms, faster than 11.31% of Python3 online submissions for Sum of Two Integers.
Memory Usage: 13.9 MB, less than 66.37% of Python3 online submissions for Sum of Two Integers.
"""
from typing import List
from typing import Optional

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        add = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        while carry != 0:
            new_add = (add ^ carry) & mask
            new_carry = ((add & carry) << 1) & mask
            add = new_add
            carry = new_carry
        if add <= MAX:
            return add 
        else:
            return ~(add ^ mask)

def main():
    sol = Solution()
    print('Output:', sol.getSum(2, 3))
    print('Expected:', 5)

if __name__ == "__main__":
    main()
