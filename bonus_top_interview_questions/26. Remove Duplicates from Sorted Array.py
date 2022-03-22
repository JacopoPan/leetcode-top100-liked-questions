"""
Runtime: 88 ms, faster than 91.69% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 24.01% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
from typing import List
from typing import Optional

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_shift = 0
        for idx, val in enumerate(nums):
            if idx==0:
                continue
            if val == nums[idx-1]:
                left_shift += 1
            else:
                nums[idx-left_shift] = val
        return len(nums)-left_shift

def main():
    sol = Solution()
    inp = [1,1,2]
    ans =  sol.removeDuplicates(inp)
    print('Output:', inp[:ans])
    print('Expected:', [1,2])

if __name__ == "__main__":
    main()
