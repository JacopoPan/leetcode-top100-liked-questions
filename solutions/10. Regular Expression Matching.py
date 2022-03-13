"""
Runtime: 47 ms, faster than 89.57% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 15.2 MB, less than 6.45% of Python3 online submissions for Regular Expression Matching.
"""
from typing import List
from typing import Optional

class Solution:

    cache = {}

    def isMatch(self, s: str, p: str) -> bool:
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        length = len(s)
        if p == '':
            if length == 0:
                return True
            else:
                return False
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if length>0 and (s[-1]==p[-2] or p[-2]=='.') and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True
        if length>0 and (p[-1]==s[-1] or p[-1]=='.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False

def main():
    sol = Solution()
    print('Output:', sol.isMatch('ab', '.*'))
    print('Expected:', True)

if __name__ == "__main__":
    main()
