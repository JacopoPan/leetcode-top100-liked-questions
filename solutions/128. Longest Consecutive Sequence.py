"""
Runtime: 268 ms, faster than 70.75% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 29.5 MB, less than 17.90% of Python3 online submissions for Longest Consecutive Sequence.
"""
from typing import List
from typing import Optional

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        table = {}
        max_seq = 1
        for i in nums:
            if i in table.keys():
                continue
            current_seq = 1
            flag_a, flag_b = False, False
            if i - 1 in table.keys():
                current_seq = current_seq + table[i - 1]
                flag_a = True
            if i + 1 in table.keys():
                current_seq = current_seq + table[i + 1]
                flag_b = True
            table[i] = current_seq
            if flag_a:
                table[i - table[i-1]] = current_seq
            if flag_b:
                table[i + table[i+1]] = current_seq
            if current_seq > max_seq:
                max_seq = current_seq
        return max_seq

def main():
    sol = Solution()
    print('Output:', sol.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
    print('Expected:', 7)

if __name__ == "__main__":
    main()