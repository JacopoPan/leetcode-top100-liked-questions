"""
Runtime: 239 ms, faster than 22.31% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 13.7 MB, less than 99.98% of Python3 online submissions for First Unique Character in a String.
"""
from typing import List
from typing import Optional

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache = {}
        for idx, char in enumerate(s):
            if char not in cache.keys():
                cache[char] = [idx, 1]
            else:
                temp = cache[char]
                cache[char] = [temp[0], temp[1] + 1]
        for k, v in cache.items():
            if v[1]==1:
                return v[0]
        return -1

def main():
    sol = Solution()
    print('Output:', sol.firstUniqChar("leetcode"))
    print('Expected:', 0)

if __name__ == "__main__":
    main()
