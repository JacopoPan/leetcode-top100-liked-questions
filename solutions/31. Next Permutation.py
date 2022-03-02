"""
Runtime: 48 ms, faster than 72.20% of Python3 online submissions for Next Permutation.
Memory Usage: 13.9 MB, less than 89.21% of Python3 online submissions for Next Permutation.
"""
from typing import List
from typing import Optional

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                nums[:] = nums[:][::-1]
                break
            elif nums[i] > nums[i-1]:
                target_idx = i
                for j in range(len(nums[i:])):
                    if nums[i+j] > nums[i-1]:
                        target_idx = i+j
                    elif (i+j+1) == len(nums) or nums[i+j+1] < nums[i-1]:
                        break
                temp = nums[i-1]
                nums[i-1] = nums[target_idx]
                nums[target_idx] = temp
                nums[i:] = nums[i:][::-1]
                break

def main():
    sol = Solution()
    nums = [1,1,5]
    sol.nextPermutation(nums)
    print('Output:', nums)
    print('Expected:', [1, 5, 1])

if __name__ == "__main__":
    main()
