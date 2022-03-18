"""
Runtime: 527 ms, faster than 33.49% of Python3 online submissions for Target Sum.
Memory Usage: 15.1 MB, less than 51.66% of Python3 online submissions for Target Sum.
"""
from typing import List
from typing import Optional

class Solution:
    def __init__(self):
        self.cache = {}
    
    def findTargetSumWays(self, nums: List[int], target: int, idx: int=0) -> int:
        if (target, idx) in self.cache.keys():
            return self.cache[(target, idx)]
        ans = 0
        if len(nums[idx:])==1:
            if nums[idx]==target:
                ans += 1
            if nums[idx]==-target:
                ans +=1
            return ans
        else:
            v1 = self.findTargetSumWays(nums, target-nums[idx], idx+1)
            self.cache[(target-nums[idx], idx+1)] = v1
            v2 = self.findTargetSumWays(nums, target+nums[idx], idx+1)
            self.cache[(target+nums[idx], idx+1)] = v2
            return v1 + v2

def main():
    sol = Solution()
    print('Output:', sol.findTargetSumWays([1,1,1,1,1], 3))
    print('Expected:', 5)

if __name__ == "__main__":
    main()
