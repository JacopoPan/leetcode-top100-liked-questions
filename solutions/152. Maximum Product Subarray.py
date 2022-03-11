"""
Runtime: 84 ms, faster than 92.88% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 16 MB, less than 5.67% of Python3 online submissions for Maximum Product Subarray.
"""
from typing import List
from typing import Optional

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], max(nums[1], nums[0]*nums[1]))
        prod_up_to = []
        prod_from = []
        prod_so_far = 1        
        for i in range(len(nums)):
            if prod_so_far == 0:
                prod_up_to.append(1*nums[i])
            else:
                prod_up_to.append(prod_so_far*nums[i])
            prod_so_far = prod_up_to[-1]
            if i < (len(nums) - 1):
                prod_from.append(-99-i)        
        prod_so_far = 1
        len_prod_from = len(prod_from)
        for i in range(len_prod_from):
            if prod_so_far == 0:
                prod_from[len_prod_from-i-1] = nums[-1-i]
            else:
                prod_from[len_prod_from-i-1] = prod_so_far*nums[-1-i]
            prod_so_far = prod_from[len_prod_from-i-1]
        return max(max(prod_up_to), int(max(prod_from)))

def main():
    sol = Solution()
    print('Output:', sol.maxProduct([-1,-2,-3,0]))
    print('Expected:', 6)

if __name__ == "__main__":
    main()
