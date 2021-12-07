"""
Runtime: 1016 ms, faster than 5.76% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 14.2 MB, less than 67.80% of Python3 online submissions for Palindromic Substrings.
"""
from typing import List
from typing import Optional

class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                this = s[i:j+1]
                if self.palindromeCheck(this):
                    counter += 1
        return counter
    
    def palindromeCheck(self, s: str) -> bool:
        if len(s) == 1:
            return True
        else:
            if len(s)%2 == 0:
                first_half = s[:int(len(s)//2)]
                second_half = s[int(len(s)//2):]
            else:
                first_half = s[:int(len(s)//2)]
                second_half = s[int(len(s)//2)+1:]
            if first_half == second_half[::-1]:
                return True
            else:
                return False

def main():
    sol = Solution()
    print('Output:', sol.countSubstrings("abc"))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
