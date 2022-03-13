"""
Runtime: 364 ms, faster than 41.99% of Python3 online submissions for Rotate Array.
Memory Usage: 25.3 MB, less than 83.97% of Python3 online submissions for Rotate Array.
"""
from typing import List
from typing import Optional

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k == 0 or k == length:
            return
        k = k % length
        for i in range((length-k)//2):
            temp = nums[i]
            nums[i] = nums[length-k-1-i]
            nums[length-k-1-i] = temp
        for i in range(k//2):
            offset = length-k
            temp = nums[i+offset]
            nums[i+offset] = nums[k-1-i+offset]
            nums[k-1-i+offset] = temp
        for i in range(length//2):
            temp = nums[i]
            nums[i] = nums[length-1-i]
            nums[length-1-i] = temp

def main():
    sol = Solution()
    inp = [1,2,3,4,5,6,7,8,9,10]
    sol.rotate(inp, 3)
    print('Output:', inp)
    print('Expected:', [8,9,10,1,2,3,4,5,6,7])

if __name__ == "__main__":
    main()
