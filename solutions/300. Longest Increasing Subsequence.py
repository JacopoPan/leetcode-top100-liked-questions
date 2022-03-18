"""
Runtime: 88 ms, faster than 92.41% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.4 MB, less than 32.18% of Python3 online submissions for Longest Increasing Subsequence.
"""
from typing import List
from typing import Optional

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = []
        for val in nums:
            pos = self.insert(sequence, val)
            if pos == len(sequence):
                sequence.append(val)
            else:
                sequence[pos] = val
        return len(sequence)
    
    def insert(self, subseq, val):
        lo = 0
        hi = len(subseq)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if val > subseq[mid]:
                lo = mid + 1
            elif val < subseq[mid]:
                hi = mid - 1
            elif val == subseq[mid]:
                return mid
        return lo

def main():
    sol = Solution()
    print('Output:', sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print('Expected:', 4)

if __name__ == "__main__":
    main()
