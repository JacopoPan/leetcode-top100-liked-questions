"""
Runtime: 458 ms, faster than 81.17% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 14.3 MB, less than 80.86% of Python3 online submissions for Partition Equal Subset Sum.
"""
from typing import List
from typing import Optional

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0 or len(nums)<2:
            return False
        target = sum(nums)//2        
        sums = {}
        sums[0] = True
        for i in range(len(nums)):
            if target-nums[i] in sums.keys():
                return True
            else:
                new_sums = {}
                for k in sums.keys():
                    new_sums[k] = True
                    if k+nums[i] < target:
                        new_sums[k+nums[i]] = True
                sums = new_sums         
        return False

def main():
    sol = Solution()
    print('Output:', sol.canPartition([1,5,11,5]))
    print('Expected:', True)

if __name__ == "__main__":
    main()