"""
Runtime: 132 ms, faster than 70.60% of Python3 online submissions for Single Number.
Memory Usage: 16.7 MB, less than 61.03% of Python3 online submissions for Single Number.
"""
from typing import List
from typing import Optional

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        twice = {nums[0]: False}
        for i in range(1,len(nums)):
            if nums[i] in twice:
                twice[nums[i]] = True
            else:
                twice[nums[i]] = False
        for i in twice:
            if twice[i] == False:
                return i

def main():
    sol = Solution()
    print('Output:', sol.singleNumber([2,2,1]))
    print('Expected:', 1)

if __name__ == "__main__":
    main()
