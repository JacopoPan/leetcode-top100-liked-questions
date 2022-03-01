"""
Runtime: 878 ms, faster than 55.75% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 37.8 MB, less than 6.83% of Python3 online submissions for Palindrome Partitioning.
"""
from typing import List
from typing import Optional

class Solution(object):
    def partition(self, s):
        ret = []
        if len(s) == 0:
            ret.append([])
        else:
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:
                    for suf in self.partition(s[i+1:]):
                        ret.append([s[:i+1]] + suf)
        return ret

def main():
    sol = Solution()
    print('Output:', sol.partition('aab'))
    print('Expected:', [["a","a","b"],["aa","b"]])

if __name__ == "__main__":
    main()
