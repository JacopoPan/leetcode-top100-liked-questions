"""
Runtime: 120 ms, faster than 63.33% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 16 MB, less than 15.76% of Python3 online submissions for Trapping Rain Water.
"""
from typing import List
from typing import Optional

class Solution:
    def trap(self, height: List[int]) -> int:
        highest_left = [0]*len(height)
        highest_right = [0]*len(height)
        temp_hi = 0
        for i in range(len(height)):
            highest_left[i] = temp_hi
            temp_hi = max(temp_hi, height[i])
        temp_hi = 0
        for i in range(len(height)):
            highest_right[len(height)-i-1] = temp_hi
            temp_hi = max(temp_hi, height[len(height)-i-1])
        rain = [0]*len(height)
        for i in range(len(height)):
            rain[i] = max(0,min(highest_left[i], highest_right[i])-height[i])
        return sum(rain)

def main():
    sol = Solution()
    print('Output:', sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print('Expected:', 6)

if __name__ == "__main__":
    main()
