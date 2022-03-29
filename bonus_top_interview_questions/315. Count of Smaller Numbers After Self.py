"""
Runtime: 3284 ms, faster than 74.29% of Python3 online submissions for Count of Smaller Numbers After Self.
Memory Usage: 33.2 MB, less than 76.39% of Python3 online submissions for Count of Smaller Numbers After Self.
"""
from typing import List
from typing import Optional

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.ans = [0] * len(nums)
        indexes = list(range(len(nums)))
        _ = self.sortIndices(indexes)
        return self.ans
    
    def sortIndices(self, indexes):
        half = len(indexes) // 2
        if half > 0:
            left = self.sortIndices(indexes[:half])
            right = self.sortIndices(indexes[half:])
            for i in range(len(indexes)-1,-1,-1):
                if len(right)==0 or \
                    (len(left)>0 and self.nums[left[-1]] > self.nums[right[-1]]):
                    self.ans[left[-1]] += len(right)
                    indexes[i] = left.pop()
                else:
                    indexes[i] = right.pop()
        return indexes

def main():
    sol = Solution()
    print('Output:', sol.countSmaller([5,2,6,1]))
    print('Expected:', [2,1,1,0])

if __name__ == "__main__":
    main()
