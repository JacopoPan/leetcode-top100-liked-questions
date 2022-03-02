"""
Runtime: 36 ms, faster than 97.81% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.1 MB, less than 96.40% of Python3 online submissions for Search in Rotated Sorted Array.
"""
from typing import List
from typing import Optional

class Solution:
    def search(self, nums: List[int], target: int, offset: int=0) -> int:  
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
            left_start = nums[:len(nums)//2][0]
            left_end = nums[:len(nums)//2][-1]
            right_start = nums[len(nums)//2:][0]
            right_end = nums[len(nums)//2:][-1]            
            if left_end >= left_start:
                rotation_on_left = False
            else:
                rotation_on_left = True
            if right_end >= right_start:
                rotation_on_right = False
            else:
                rotation_on_right = True
            if not rotation_on_left and target >= left_start and target <= left_end:
                return self.search(nums[:len(nums)//2], target, offset) # L
            elif not rotation_on_right and target >= right_start and target <= right_end:
                return self.search(nums[len(nums)//2:], target, offset+len(nums)//2) #R
            elif rotation_on_left and (target > right_end or target < right_start):
                return self.search(nums[:len(nums)//2], target, offset) # L
            else:
                return self.search(nums[len(nums)//2:], target, offset+len(nums)//2) #R

def main():
    sol = Solution()
    print('Output:', sol.search([4,5,6,7,0,1,2], 0))
    print('Expected:', 4)

if __name__ == "__main__":
    main()
