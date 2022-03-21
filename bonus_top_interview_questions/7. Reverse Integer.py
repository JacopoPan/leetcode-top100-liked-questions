"""
Runtime: 67 ms, faster than 9.95% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.9 MB, less than 72.31% of Python3 online submissions for Reverse Integer.
"""
from typing import List
from typing import Optional

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = True
            x = -x
        else:
            negative = False
        ans = 0
        while x > 0:
            digit = x%10
            x = (x - digit)/10
            ans = 10*ans + digit
        if ans > 2**31:
            ans = 0
        if negative:
            ans = -ans
        return int(ans)

def main():
    sol = Solution()
    print('Output:', sol.reverse(123))
    print('Expected:', 321)

if __name__ == "__main__":
    main()
