"""
Runtime: 96 ms, faster than 71.82% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.6 MB, less than 12.96% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""
from typing import List
from typing import Optional

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if len(nums) == 0:
            return ans
        ans[0] = self.searchBottom(nums, target)
        ans[1] = self.searchTop(nums, target)
        return ans
    
    def searchBottom(self, nums: List[int], target: int, offset: int=0) -> List[int]:
        if len(nums) == 1:
            if nums[0] == target:
                return offset
            else:
                return -1
        elif len(nums) == 2:
            if nums[0] == target:
                return offset
            elif nums[1] == target:
                return offset + 1
            else:
                return -1
        else:
            if target <= nums[:len(nums)//2][-1]:
                return self.searchBottom(nums[:len(nums)//2], target, offset)
            else:
                return self.searchBottom(nums[len(nums)//2:], target, offset+len(nums)//2)
            
    def searchTop(self, nums: List[int], target: int, offset: int=0) -> List[int]:
        if len(nums) == 1:
            if nums[0] == target:
                return offset
            else:
                return -1
        elif len(nums) == 2:
            if nums[1] == target:
                return offset + 1
            elif nums[0] == target:
                return offset
            else:
                return -1
        else:
            if target >= nums[len(nums)//2:][0]:
                return self.searchTop(nums[len(nums)//2:], target, offset+len(nums)//2)
            else:
                return self.searchTop(nums[:len(nums)//2], target, offset)

def main():
    sol = Solution()
    print('Output:', sol.searchRange([5,7,7,8,8,10], 8))
    print('Expected:', [3,4])

if __name__ == "__main__":
    main()
