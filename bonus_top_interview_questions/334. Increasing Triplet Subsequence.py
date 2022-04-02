"""
Runtime: 672 ms, faster than 66.56% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 24.6 MB, less than 48.46% of Python3 online submissions for Increasing Triplet Subsequence.
"""
from typing import List
from typing import Optional
import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        triplet_start = [math.inf, math.inf]
        for idx in range(len(nums)):
            if nums[idx] <= triplet_start[0]:
                triplet_start[0] = nums[idx]
            if nums[idx] > triplet_start[0] and nums[idx] <= triplet_start[1]:
                triplet_start[1] = nums[idx]
            if nums[idx] > triplet_start[0] and nums[idx] > triplet_start[1]:
                return True
        return False

def main():
    sol = Solution()
    print('Output:', sol.increasingTriplet([20,100,10,12,5,13]))
    print('Expected:', True)

if __name__ == "__main__":
    main()
