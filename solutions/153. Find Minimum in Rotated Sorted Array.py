"""
Runtime: 44 ms, faster than 85.59% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 14.2 MB, less than 67.29% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
"""
from typing import List
from typing import Optional

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        if len(nums) == 3:
            return min(min(nums[0], nums[1]),nums[2])
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]
        if right[0] > right[-1]:
            return self.findMin(right)
        elif left[0] > left[-1]:
            return self.findMin(left)
        else:
            return min(left[0],right[0])
        
def main():
    sol = Solution()
    print('Output:', sol.findMin([3,4,5,1,2]))
    print('Expected:', 1)

if __name__ == "__main__":
    main()
