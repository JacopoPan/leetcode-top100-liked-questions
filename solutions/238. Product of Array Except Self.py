"""
Runtime: 240 ms, faster than 68.27% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.2 MB, less than 47.96% of Python3 online submissions for Product of Array Except Self.
"""
from typing import List
from typing import Optional

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1
        zeros = 0
        for i in nums:
            if i != 0:
                val *= i
            if i == 0:
                zeros += 1
        ret = []
        for i in nums:
            if zeros > 1:
                ret.append(0)
            elif zeros == 1:
                if i != 0:
                    ret.append(0)
                else:
                    ret.append(val)
            else:
                ret.append(int(val/i))
        return ret

def main():
    sol = Solution()
    print('Output:', sol.productExceptSelf([1,2,3,4]))
    print('Expected:', [24,12,8,6])

if __name__ == "__main__":
    main()
