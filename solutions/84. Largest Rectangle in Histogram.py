"""
Runtime: 1750 ms, faster than 13.66% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 28.9 MB, less than 24.95% of Python3 online submissions for Largest Rectangle in Histogram.
"""
from typing import List
from typing import Optional

class Solution:
    def largestRectangleArea(self, heights: List[int], start: int=0) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans  

def main():
    sol = Solution()
    print('Output:', sol.largestRectangleArea([2,1,5,6,2,3]))
    print('Expected:', 10)

if __name__ == "__main__":
    main()
