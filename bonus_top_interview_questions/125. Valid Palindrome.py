"""
Runtime: 107 ms, faster than 11.33% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.5 MB, less than 24.06% of Python3 online submissions for Valid Palindrome.
"""
from typing import List
from typing import Optional

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_down_s = []
        low = ['a']
        for c in s:
            if c.isdigit():
                stripped_down_s.append(c)
            elif c.isalpha():
                if c.isupper():
                    stripped_down_s.append(c.lower())
                elif c.islower():
                    stripped_down_s.append(c)                    
        length = len(stripped_down_s)
        if length <= 1:
            return True
        for i in range(length//2):
            if stripped_down_s[i] != stripped_down_s[length-1-i]:
                return False
        return True

def main():
    sol = Solution()
    print('Output:', sol.isPalindrome("A man, a plan, a canal: Panama"))
    print('Expected:', True)

if __name__ == "__main__":
    main()
