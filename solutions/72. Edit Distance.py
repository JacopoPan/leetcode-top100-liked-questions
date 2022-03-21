"""
Runtime: 4308 ms, faster than 16.57% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 65.12% of Python3 online submissions for Two Sum.
"""
from typing import List
from typing import Optional

class Solution:
    def __init__(self):
        self.cache = {}
    
    def minDistance(self, word1: str, word2: str) -> int:
        if (word1, word2) in self.cache.keys():
            return self.cache[(word1, word2)]
        ans = -1
        if word1 == '' and word2 == '':
            ans = 0
        elif word1 == '':
            ans = len(word2)
        elif word2 == '':
            ans = len(word1)
        elif word1[0] == word2[0]:
            ans = self.minDistance(word1[1:], word2[1:])
        else:
            insert = self.minDistance(word1, word2[1:])
            delete = self.minDistance(word1[1:], word2)
            replace = self.minDistance(word1[1:], word2[1:])
            ans = min([insert, replace, delete]) + 1
        self.cache[(word1, word2)] = ans
        return ans

def main():
    sol = Solution()
    print('Output:', sol.minDistance("horse", "ros"))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
