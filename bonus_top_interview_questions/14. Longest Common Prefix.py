"""
Runtime: 40 ms, faster than 76.15% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.1 MB, less than 23.58% of Python3 online submissions for Longest Common Prefix.
"""
from typing import List
from typing import Optional

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        for s in strs:
            if len(s) == 0:
                return ''
        idx = 0
        while True:
            for i, s in enumerate(strs):
                if idx > len(s)-1:
                    return s
                if i==0:
                    char = strs[i][idx]
                    continue
                if s[idx] != char:
                    return s[:idx]
            idx += 1

def main():
    sol = Solution()
    print('Output:', sol.longestCommonPrefix(["flower","flow","flight"]))
    print('Expected:', 'fl')

if __name__ == "__main__":
    main()
