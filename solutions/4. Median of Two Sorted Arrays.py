"""
Runtime: 158 ms, faster than 31.95% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.1 MB, less than 79.59% of Python3 online submissions for Median of Two Sorted Arrays.
"""
from typing import List
from typing import Optional

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = []
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                merge.append(nums2[j])
                j += 1
            elif j == len(nums2):
                merge.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1
        return self.findMedian(merge)
    
    def findMedian(self, nums: List[int]) -> float:
        if len(nums)%2==0:
            return (nums[len(nums)//2-1] + nums[len(nums)//2])/2
        else:
            return nums[len(nums)//2]

def main():
    sol = Solution()
    print('Output:', sol.findMedianSortedArrays([1,2,4,7,8], [2,3,8]))
    print('Expected:', 3.5)

if __name__ == "__main__":
    main()
