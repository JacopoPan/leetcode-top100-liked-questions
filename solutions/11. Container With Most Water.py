"""
Runtime: 6200 ms, faster than 5.01% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.5 MB, less than 57.22% of Python3 online submissions for Container With Most Water.
"""
from typing import List
from typing import Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        used_min_vert = min(height[i], height[j])
        max_water = (j - i) * used_min_vert
        while i+1 != j:  
            if height[i] > height[j]:
                j -= 1
                if height[j] < used_min_vert:
                    continue
            else:
                i +=1
                if height[i] < used_min_vert:
                    continue
            if max(height[i:j]) < min(height[i], height[j]):
                break
            elif (max(height[i:j]) * (j - i)) < max_water:
                break
            else:
                used_min_vert = min(height[i], height[j])
                water = (j - i) * used_min_vert
                if water > max_water:
                    max_water = water
        return max_water

def main():
    sol = Solution()
    print('Output:', sol.maxArea([2,3,10,5,7,8,9]))
    print('Expected:', 36)

if __name__ == "__main__":
    main()
