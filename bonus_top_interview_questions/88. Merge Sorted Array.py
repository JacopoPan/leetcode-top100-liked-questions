"""
Runtime: 66 ms, faster than 24.27% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.1 MB, less than 17.98% of Python3 online submissions for Merge Sorted Array.
"""
from typing import List
from typing import Optional

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        read_idx1 = m-1
        read_idx2 = n-1
        write_idx = len(nums1)-1
        while read_idx1 >= 0 or read_idx2 >= 0:
            if read_idx2==-1:
                nums1[write_idx] = nums1[read_idx1]
                write_idx -= 1
                read_idx1 -= 1
            elif read_idx1==-1:
                nums1[write_idx] = nums2[read_idx2]
                write_idx -= 1
                read_idx2 -= 1
            elif nums1[read_idx1] > nums2[read_idx2]:
                nums1[write_idx] = nums1[read_idx1]
                write_idx -= 1
                read_idx1 -= 1
            else:
                nums1[write_idx] = nums2[read_idx2]
                write_idx -= 1
                read_idx2 -= 1

def main():
    sol = Solution()
    inp = [1,2,3,0,0,0]
    sol.merge(inp, 3, [2,5,6], 3)
    print('Output:', inp)
    print('Expected:', [1,2,2,3,5,6])

if __name__ == "__main__":
    main()
