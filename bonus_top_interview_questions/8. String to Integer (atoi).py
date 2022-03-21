"""
Runtime: 40 ms, faster than 78.24% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 41.92% of Python3 online submissions for String to Integer (atoi).
"""
from typing import List
from typing import Optional

class Solution:
    def myAtoi(self, s: str) -> int:
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        while len(s)>0 and s[0]==' ':
            s = s[1:]
        if s == '':
            return 0
        if s[0]=='-':
            negative = True
            s = s[1:]
        elif s[0]=='+':
            negative = False
            s = s[1:]
        else:
            negative = False
        ans = 0
        for c in s:
            if c not in digits:
                break
            else:
                ans = ans*10+int(c)
                if ans >= 2**31:
                    if negative:
                        ans = 2**31
                    else:
                        ans = 2**31-1
                    break
        if negative:
            ans = -ans
        return ans

def main():
    sol = Solution()
    print('Output:', sol.myAtoi("   -42"))
    print('Expected:', -42)

if __name__ == "__main__":
    main()
