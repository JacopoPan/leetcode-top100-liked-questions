"""
Runtime: 4308 ms, faster than 16.57% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 65.12% of Python3 online submissions for Two Sum.
"""
from typing import List
from typing import Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

def main():
    sol = Solution()
    print('Output:', sol.twoSum([2,7,11,15], 9))
    print('Expected:', [0, 1])

if __name__ == "__main__":
    main()
