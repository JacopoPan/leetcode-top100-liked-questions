"""
Runtime: 12 ms, faster than 100.00% of Python3 online submissions for Divide Two Integers.
Memory Usage: 14 MB, less than 40.31% of Python3 online submissions for Divide Two Integers.
"""
from typing import List
from typing import Optional

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        invert = False
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            invert = True
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        ans = 0
        summation = divisor
        while dividend >= summation:
            current_ans = 1
            while (summation + summation) <= dividend:
                summation += summation
                current_ans += current_ans
            dividend -= summation
            summation = divisor
            ans += current_ans  
        if invert:
            ans = -ans
        return min(2147483647, max(ans, -2147483648))

def main():
    sol = Solution()
    print('Output:', sol.divide(7, -3))
    print('Expected:', -2)

if __name__ == "__main__":
    main()
