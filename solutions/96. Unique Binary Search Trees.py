"""
Runtime: 27 ms, faster than 81.37% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 14.3 MB, less than 50.41% of Python3 online submissions for Unique Binary Search Trees.
"""
from typing import List
from typing import Optional

class Solution:
    def numTrees(self, n: int) -> int:
        return self.catalanNumber(n)
     
    def catalanNumber(self, n: int) -> int:
        prod = 1
        for i in range(2,n+1):
            prod *= ((n + i) / i)
        return int(round(prod))

def main():
    sol = Solution()
    print('Output:', sol.numTrees(7))
    print('Expected:', 429)

if __name__ == "__main__":
    main()
