"""
Runtime: 246 ms, faster than 29.65% of Python3 online submissions for Missing Number.
Memory Usage: 15.6 MB, less than 12.17% of Python3 online submissions for Missing Number.
"""
from typing import List
from typing import Optional

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cache = {}
        for val in range(len(nums)+1):
            cache[val] = 1
        for n in nums:
            cache[n] = 0
        for k, v in cache.items():
            if cache[k]==1:
                return k

def main():
    sol = Solution()
    print('Output:', sol.missingNumber([3,0,1]))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
