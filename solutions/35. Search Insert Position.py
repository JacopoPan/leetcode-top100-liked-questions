"""
Runtime: 48 ms, faster than 79.03% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.3 MB, less than 24.33% of Python3 online submissions for Search Insert Position.
"""
from typing import List
from typing import Optional

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        search_in = nums
        base = 0
        if target < nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
        else:
            while len(search_in) > 0:
                left = search_in[:len(search_in)//2]
                right = search_in[len(search_in)//2:]
                if target == search_in[len(search_in)//2]:
                    return base + len(search_in)//2
                elif target < search_in[len(search_in)//2] and target > search_in[len(search_in)//2 - 1]:
                    return base + len(search_in)//2
                elif target < search_in[len(search_in)//2]:
                    search_in = left
                elif target > search_in[len(search_in)//2]:
                    base += len(left)
                    search_in = right
            return base

def main():
    sol = Solution()
    print('Output:', sol.searchInsert([1,3,5,6], 5))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
