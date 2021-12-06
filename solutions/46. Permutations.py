"""
Runtime: 44 ms, faster than 44.87% of Python3 online submissions for Permutations.
Memory Usage: 14.4 MB, less than 45.94% of Python3 online submissions for Permutations.
"""
from typing import List
from typing import Optional

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        else:
            ret = []
            for i in range(len(nums)):
                init = nums[i]
                per_of_rest = self.permute(self.removeJth(nums,i))
                for per in per_of_rest:
                    ret.append([init]+per)
            return ret
        
    def removeJth(self, nums: List[int], j: int) -> List[int]:
        if len(nums) <= 1:
            return []
        else:
            return nums[:j] + nums[j+1:]

def main():
    sol = Solution()
    print('Output:', sol.permute([1,2,3]))
    print('Expected:', [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

if __name__ == "__main__":
    main()
