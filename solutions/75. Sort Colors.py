"""
Runtime: 32 ms, faster than 76.36% of Python3 online submissions for Sort Colors.
Memory Usage: 14.1 MB, less than 92.21% of Python3 online submissions for Sort Colors.
"""
from typing import List
from typing import Optional

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)
        nums[:zeros] = [0] * zeros
        nums[zeros:ones] = [1] * ones
        nums[zeros+ones:] = [2] * twos        

def main():
    sol = Solution()
    inp = [2,0,2,1,1,0]
    sol.sortColors(inp)
    print('Output:', inp)
    print('Expected:', [0,0,1,1,2,2])

if __name__ == "__main__":
    main()
