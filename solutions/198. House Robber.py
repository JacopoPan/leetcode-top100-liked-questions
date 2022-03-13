"""
Runtime: 24 ms, faster than 99.02% of Python3 online submissions for House Robber.
Memory Usage: 14 MB, less than 45.67% of Python3 online submissions for House Robber.
"""
from typing import List
from typing import Optional

class Solution:
    
    def __init__(self):
        self.cache = {}
    
    def rob(self, nums: List[int], idx: int=0) -> int:
        if idx in self.cache.keys():
            return self.cache[idx]
        temp = nums[idx:]
        length = len(temp) 
        if length==1:
            val = temp[0]
            return val
        elif length==2:
            val = max(temp[0], temp[1])
            return val
        else:
            temp1 = temp[0]+self.rob(nums, idx+2)
            self.cache[idx+2] = temp1-temp[0]
            temp2 = self.rob(nums, idx+1)
            self.cache[idx+1] = temp2
            val = max(temp1, temp2)
            return val

def main():
    sol = Solution()
    print('Output:', sol.rob([6,6,4,8,4,3,3,10]))
    print('Expected:', 27)

if __name__ == "__main__":
    main()
