"""
Runtime: 2413 ms, faster than 31.09% of Python3 online submissions for Jump Game II.
Memory Usage: 15.2 MB, less than 48.71% of Python3 online submissions for Jump Game II.
"""
from typing import List
from typing import Optional

class Solution:

    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        steps = 0
        earliest_idx = -1
        while earliest_idx != 0:
            steps += 1
            l = len(nums)
            for i in range(l):
                if nums[i] >= (l-1-i):
                    earliest_idx = i
                    break  
            nums = nums[:earliest_idx+1] 
        return steps

def main():
    sol = Solution()
    print('Output:', sol.jump([2,3,1,1,4]))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
