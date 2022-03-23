"""
Runtime: 64 ms, faster than 61.38% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.5 MB, less than 70.90% of Python3 online submissions for Valid Anagram.
"""
from typing import List
from typing import Optional

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = {}
        for char in s:
            if char in cache.keys():
                cache[char] += 1
            else:
                cache[char] = 1
        for char in t:
            if char not in cache.keys():
                return False
            cache[char] -= 1
            if cache[char] < 0:
                return False
        for v in cache.values():
            if v != 0:
                return False
        return True

def main():
    sol = Solution()
    print('Output:', sol.isAnagram("anagram", "nagaram"))
    print('Expected:', True)

if __name__ == "__main__":
    main()
