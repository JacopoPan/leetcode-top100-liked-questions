"""
Runtime: 4308 ms, faster than 16.57% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 65.12% of Python3 online submissions for Two Sum.
"""
from typing import List
from typing import Optional

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sum_before_current = 0
        num_paths_to_sum = {}
        num_paths_to_sum[0] = 1
        for i in range(len(nums)):
            current_sum = sum_before_current + nums[i]
            if current_sum-k in num_paths_to_sum.keys():
                ans = ans + num_paths_to_sum[current_sum-k]
            if current_sum not in num_paths_to_sum.keys():
                num_paths_to_sum[current_sum] = 1
            else:
                num_paths_to_sum[current_sum] = num_paths_to_sum[current_sum]+1
            sum_before_current = current_sum 
        return ans

def main():
    sol = Solution()
    print('Output:', sol.subarraySum([1, 1, 1], 2))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
