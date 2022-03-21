"""
Runtime: 864 ms, faster than 94.50% of Python3 online submissions for First Missing Positive.
Memory Usage: 77.2 MB, less than 6.99% of Python3 online submissions for First Missing Positive.
"""
from typing import List
from typing import Optional

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cache = {}
        for n in nums:
            cache[n] = True
        for val in range(1,len(nums)+2):
            if val in cache.keys():
                continue
            else:
                return val

def main():
    sol = Solution()
    print('Output:', sol.firstMissingPositive([7,8,9,11,12]))
    print('Expected:', 1)

if __name__ == "__main__":
    main()
