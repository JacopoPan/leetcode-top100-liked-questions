"""
Runtime: 108 ms, faster than 42.41% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.8 MB, less than 38.77% of Python3 online submissions for Top K Frequent Elements.
"""
from typing import List
from typing import Optional

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for item in nums:
            if item in cache.keys():
                cache[item] += 1
            else:
                cache[item] = 1
        sorted_cache = {k: v for k, v in sorted(cache.items(), key=lambda item: item[1], reverse=True)}
        ret = []
        for key, val in sorted_cache.items():
            ret.append(key)
            if len(ret) == k:
                return ret

def main():
    sol = Solution()
    print('Output:', sol.topKFrequent([1,1,1,2,2,3], 2))
    print('Expected:', [1,2])

if __name__ == "__main__":
    main()
