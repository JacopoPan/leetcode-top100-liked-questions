"""
Runtime: 509 ms, faster than 14.68% of Python3 online submissions for Wiggle Sort II.
Memory Usage: 17.6 MB, less than 10.60% of Python3 online submissions for Wiggle Sort II.
"""
from typing import List
from typing import Optional

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        temp = self.mergeSort(nums)
        for i in range(1, len(nums), 2):
            nums[i] = temp.pop() 
        for i in range(0, len(nums), 2):
            nums[i] = temp.pop() 

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums)==0 or len(nums)==1:
            return nums
        elif len(nums)==2:
            if nums[0] > nums[1]:
                return nums[::-1]
            else:
                return nums
        else:
            left = self.mergeSort(nums[:len(nums)//2])
            right = self.mergeSort(nums[len(nums)//2:])
            temp = []
            i = 0
            j = 0
            while i < len(left) or j < len(right):
                if j==len(right):
                    temp.append(left[i])
                    i += 1
                elif i==len(left):
                    temp.append(right[j])
                    j += 1
                elif left[i]<right[j]:
                    temp.append(left[i])
                    i += 1
                else:
                    temp.append(right[j])
                    j += 1
            return temp

def main():
    sol = Solution()
    inp = [1,3,2,2,3,1]
    sol.wiggleSort(inp)
    print('Output:', inp)
    print('Expected:', [2,3,1,3,1,2])

if __name__ == "__main__":
    main()
