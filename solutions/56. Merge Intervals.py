"""
Runtime: 136 ms, faster than 99.03% of Python3 online submissions for Merge Intervals.
Memory Usage: 18.8 MB, less than 25.39% of Python3 online submissions for Merge Intervals.
"""
from typing import List
from typing import Optional

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        for val in intervals[1:]:
            if val[0] <= current_end:
                current_end = max(current_end, val[1])
            else:
                ans.append([current_start, current_end])
                current_start = val[0]
                current_end = val[1]
        ans.append([current_start, current_end])
        return ans

def main():
    sol = Solution()
    print('Output:', sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    print('Expected:', [[1,6],[8,10],[15,18]])

if __name__ == "__main__":
    main()
