"""
Runtime: 28 ms, faster than 94.84% of Python3 online submissions for Subsets.
Memory Usage: 14.5 MB, less than 19.72% of Python3 online submissions for Subsets.
"""
from typing import List
from typing import Optional

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(2**len(nums)):
            val = i
            binary = []
            while val > 0:
                binary.append(val%2)
                val = val // 2
            temp = []
            for idx, d in enumerate(binary):
                if d == 1:
                    temp.append(nums[idx])
            ret.append(temp)
        return ret

def main():
    sol = Solution()
    print('Output:', sol.subsets([1,2,3]))
    print('Expected:', [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])

if __name__ == "__main__":
    main()
