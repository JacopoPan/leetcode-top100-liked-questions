"""
Runtime: 31 ms, faster than 93.16% of Python3 online submissions for Decode Ways.
Memory Usage: 13.9 MB, less than 46.20% of Python3 online submissions for Decode Ways.
"""
from typing import List
from typing import Optional

class Solution:
    def __init__(self):
        self.cache = {}
    
    def numDecodings(self, s: str) -> int:
        if s in self.cache.keys():
            return self.cache[s]
        if len(s)==1:
            if s=='0':
                return 0
            else:
                return 1
        else:
            if s[0]=='0':
                return 0
            else:
                take_one = self.numDecodings(s[1:])
                if len(s)==2 and int(s[:2]) <=26:
                    take_two = 1
                elif len(s)>2 and int(s[:2]) <=26:
                    take_two = self.numDecodings(s[2:])
                else:
                    take_two = 0
                self.cache[s] = take_one + take_two
                return take_one + take_two

def main():
    sol = Solution()
    print('Output:', sol.numDecodings("2101"))
    print('Expected:', 1)

if __name__ == "__main__":
    main()
