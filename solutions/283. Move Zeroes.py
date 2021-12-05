"""
Runtime: 5308 ms, faster than 5.00% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.2 MB, less than 98.92% of Python3 online submissions for Move Zeroes.
"""
from typing import List
from typing import Optional

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_zero_at = len(nums)-1
        
        for i in range(len(nums)):
            if nums[len(nums)-1-i] == 0:
                write_zero_at = len(nums)-1-i-1
            else:
                break
        i = 0
        while i < write_zero_at:
            if nums[i] == 0:
                for j in range(i+1,write_zero_at+1):
                    nums[j-1] = nums[j]
                nums[write_zero_at] = 0
                write_zero_at -= 1 
            else:
                i += 1

def main():
    sol = Solution()
    inp = [0,1,0,3,12]
    sol.moveZeroes(inp)
    print('Output:', inp)
    print('Expected:', [1,3,12,0,0])

if __name__ == "__main__":
    main()
