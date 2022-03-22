"""
Runtime: 28 ms, faster than 97.72% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.9 MB, less than 15.03% of Python3 online submissions for Excel Sheet Column Number.
"""
from typing import List
from typing import Optional

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d = {}
        for x in range(len(characters)):
            d[characters[x]] = x+1
        ans = 0
        for c in columnTitle:
            ans = 26*ans + d[c]
        return ans

def main():
    sol = Solution()
    print('Output:', sol.titleToNumber("AB"))
    print('Expected:', 28)

if __name__ == "__main__":
    main()
