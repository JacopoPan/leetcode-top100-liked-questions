"""
Runtime: 42 ms, faster than 63.24% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 67.96% of Python3 online submissions for Plus One.
"""
from typing import List
from typing import Optional

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for idx in range(len(digits)-1,-1,-1):
            if idx == len(digits)-1:
                this_val = digits[idx] + 1
            else:
                this_val = digits[idx] + carry
            if this_val < 10:
                digits[idx] = this_val
                carry = 0
            else:
                digits[idx] = 0
                carry = 1
        if carry == 1:
            digits = [1] + digits
        return digits

def main():
    sol = Solution()
    print('Output:',sol.plusOne([1,2,3]))
    print('Expected:', [1,2,4])

if __name__ == "__main__":
    main()
