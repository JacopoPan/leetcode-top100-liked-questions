"""
Runtime: 1896 ms, faster than 7.52% of Python3 online submissions for 4Sum II.
Memory Usage: 21.4 MB, less than 5.42% of Python3 online submissions for 4Sum II.
"""
from typing import List
from typing import Optional

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        first_half = {}
        second_half = {}
        length = len(nums1)
        for i in range(length):
            for j in range(length):
                total = nums1[i]+nums2[j]
                if total not in first_half.keys():
                    first_half[total] = [[i,j]]
                else:
                    first_half[total].append([i,j])
        for i in range(length):
            for j in range(length):
                total = nums3[i]+nums4[j]
                if total not in second_half.keys():
                    second_half[total] = [[i,j]]
                else:
                    second_half[total].append([i,j])
        ans = 0
        for total, pairs in first_half.items():
            if -total in second_half.keys():
                other_pairs = second_half[-total]
                ans += len(pairs)*len(other_pairs)
        return ans

def main():
    sol = Solution()
    print('Output:', sol.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
