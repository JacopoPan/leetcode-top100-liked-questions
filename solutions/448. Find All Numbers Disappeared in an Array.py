"""
Runtime: 352 ms, faster than 61.54% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 22.2 MB, less than 58.46% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
from typing import List
from typing import Optional

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        ret2 = []
        for i in range(len(nums)):
            ret.append(i+1)
        for i in range(len(nums)):
            ret[nums[i]-1] = 0
        for i in range(len(ret)):
            if ret[i] != 0:
                ret2.append(ret[i])
        return ret2

def main():
    sol = Solution()
    print('Output:', sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print('Expected:', [5,6])

if __name__ == "__main__":
    main()
