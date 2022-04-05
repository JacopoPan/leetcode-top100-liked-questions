"""
Runtime: 52 ms, faster than 77.08% of Python3 online submissions for Find Peak Element.
Memory Usage: 14 MB, less than 86.09% of Python3 online submissions for Find Peak Element.
"""
from typing import List
from typing import Optional

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        skip = [False] * len(nums)
        for idx in range(1,len(nums)-1):
            if skip[idx]:
                continue
            if nums[idx] > nums[idx-1] and nums[idx] > nums[idx+1]:
                return idx
            if nums[idx-1] > nums[idx] and nums[idx] > nums[idx+1]:
                skip[idx+1] = True

def main():
    sol = Solution()
    print('Output:', sol.findPeakElement([1,2,3,1]))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
