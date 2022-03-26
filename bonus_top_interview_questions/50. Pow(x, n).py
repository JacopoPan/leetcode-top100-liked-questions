"""
Runtime: 28 ms, faster than 95.51% of Python3 online submissions for Pow(x, n).
Memory Usage: 13.9 MB, less than 74.72% of Python3 online submissions for Pow(x, n).
"""
from typing import List
from typing import Optional

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        ans = x
        if n%2==0:
            ans = self.myPow(ans*ans, n//2)
        else:
            ans = ans*self.myPow(ans, n-1)
        return ans

def main():
    sol = Solution()
    print('Output:', sol.myPow(2, 10))
    print('Expected:', 1024)

if __name__ == "__main__":
    main()
