"""
Runtime: 204 ms, faster than 86.62% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.8 MB, less than 41.73% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""
from typing import List
from typing import Optional

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        left = matrix[0][0]
        right = matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if self.countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
    def countLessOrEqual(self, x):
        counter = 0
        c = self.cols - 1
        for r in range(self.rows):
            while c >= 0 and self.matrix[r][c] > x:
                c -= 1
            counter += (c + 1)
        return counter

def main():
    sol = Solution()
    print('Output:', sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
    print('Expected:', 13)

if __name__ == "__main__":
    main()
