"""
Runtime: 672 ms, faster than 95.54% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28.8 MB, less than 33.53% of Python3 online submissions for Maximum Subarray.
"""
from typing import List
from typing import Optional

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = nums[0]
        max_sum = running_sum
        for i in range(1,len(nums)):
            if max_sum < 0 and nums[i] > max_sum:
                running_sum = nums[i]
                max_sum = running_sum
            elif running_sum + nums[i] <= 0:
                running_sum = 0
            else:
                running_sum += nums[i]
                if running_sum > max_sum:
                    max_sum = running_sum
        return max_sum

def main():
    sol = Solution()
    print('Output:', sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print('Expected:', 6)

if __name__ == "__main__":
    main()
