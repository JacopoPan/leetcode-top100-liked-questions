"""
Runtime: 2856 ms, faster than 5.05% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.2 MB, less than 48.73% of Python3 online submissions for Kth Largest Element in an Array.
"""
from typing import List
from typing import Optional

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counter = 0
        while True:
            largest = nums[0]
            largest_idx = 0
            for idx, n in enumerate(nums[1:]):
                if n > largest:
                    largest_idx = idx+1
                    largest = n
            nums = nums[:largest_idx] + nums[largest_idx+1:]
            counter += 1
            if counter == k:
                return largest

def main():
    sol = Solution()
    print('Output:', sol.findKthLargest([3,2,1,5,6,4], 2))
    print('Expected:', 5)

if __name__ == "__main__":
    main()
