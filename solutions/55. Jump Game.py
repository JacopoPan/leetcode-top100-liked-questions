"""
Runtime: 536 ms, faster than 76.84% of Python3 online submissions for Jump Game.
Memory Usage: 15.2 MB, less than 62.63% of Python3 online submissions for Jump Game.
"""
from typing import List
from typing import Optional

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if len(nums) <= 1:
            return True
        for i in range(length):
            if nums[i] >= length-i-1:
                return True
            if nums[i] == 0:
                preceedings = nums[:i]
                not_found = True
                for j in range(i):
                    if preceedings[j] > (i-j):
                        not_found = False
                        break
                if not_found:
                    return False
        return True

def main():
    sol = Solution()
    print('Output:', sol.canJump([4,2,0,0,1,1,4,4,4,0,4,0]))
    print('Expected:', True)

if __name__ == "__main__":
    main()
