"""
Runtime: 584 ms, faster than 53.62% of Python3 online submissions for Contains Duplicate.
Memory Usage: 25.8 MB, less than 95.96% of Python3 online submissions for Contains Duplicate.
"""
from typing import List
from typing import Optional

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for n in nums:
            if n in cache.keys():
                return True
            cache[n] = 1
        return False

def main():
    sol = Solution()
    print('Output:', sol.containsDuplicate([1,2,3,1]))
    print('Expected:', Truep)

if __name__ == "__main__":
    main()
