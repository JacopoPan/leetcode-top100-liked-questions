"""
Runtime: 240 ms, faster than 83.26% of Python3 online submissions for Wildcard Matching.
Memory Usage: 13.9 MB, less than 89.46% of Python3 online submissions for Wildcard Matching.
"""
from typing import List
from typing import Optional

class Solution:  
    def isMatch(self, s: str, p: str) -> bool:
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for character in p:
            if character != '*':
                for n in range(length-1,-1,-1):
                    if dp[n]==True and (character == s[n] or character == '?'):
                        dp[n+1] = True
                    else:
                        dp[n+1] = False
            else:
                for n in range(1, length+1):
                    if dp[n-1] or dp[n]:
                        dp[n] = True
                    else:
                        dp[n] = False
            if dp[0]==True and character == '*':
                dp[0] = True
            else:
                dp[0] = False
        return dp[-1]

def main():
    sol = Solution()
    print('Output:', sol.isMatch("aa", "a"))
    print('Expected:', False)

if __name__ == "__main__":
    main()
