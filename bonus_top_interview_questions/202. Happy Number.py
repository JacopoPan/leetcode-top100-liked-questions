"""
Runtime: 49 ms, faster than 52.60% of Python3 online submissions for Happy Number.
Memory Usage: 13.9 MB, less than 23.80% of Python3 online submissions for Happy Number.
"""
from typing import List
from typing import Optional

class Solution:
    def isHappy(self, n: int) -> bool:
        history = []
        while True:
            string = str(n)
            squares_sum = 0
            for digit in string:
                squares_sum += int(digit)*int(digit)
            n = squares_sum
            if n == 1:
                return True
            if n in history:
                return False
            history.append(n)

def main():
    sol = Solution()
    print('Output:', sol.isHappy(19))
    print('Expected:', True)

if __name__ == "__main__":
    main()
