"""
Runtime: 184 ms, faster than 32.94% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 82.92% of Python3 online submissions for Majority Element.
"""
from typing import List
from typing import Optional

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
                if counts[i] > len(nums)/2:
                    return i

def main():
    sol = Solution()
    print('Output:', sol.majorityElement([3,2,3]))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
