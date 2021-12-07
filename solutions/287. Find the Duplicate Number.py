"""
Runtime: 596 ms, faster than 90.25% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 31.8 MB, less than 13.84% of Python3 online submissions for Find the Duplicate Number.
"""
from typing import List
from typing import Optional

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for n in nums:
            if n in seen.keys():
                return n
            else:
                seen[n] = 'a'

def main():
    sol = Solution()
    print('Output:', sol.findDuplicate([1,3,4,2,2]))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
