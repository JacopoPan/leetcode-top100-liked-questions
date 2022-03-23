"""
Runtime: 56 ms, faster than 76.59% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.1 MB, less than 27.08% of Python3 online submissions for Intersection of Two Arrays II.
"""
from typing import List
from typing import Optional

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        cache = {}
        for n in nums1:
            if n not in cache.keys():
                cache[n] = 1
            else:
                cache[n] += 1
        for n in nums2:
            if n in cache.keys():
                if cache[n] > 0:
                    cache[n] -= 1
                    ans.append(n)
        return ans

def main():
    sol = Solution()
    print('Output:', sol.intersect([1,2,2,1], [2,2]))
    print('Expected:', [2, 2])

if __name__ == "__main__":
    main()
