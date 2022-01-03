"""
Runtime: 3055 ms, faster than 27.68% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.5 MB, less than 35.37% of Python3 online submissions for Longest Palindromic Substring.
"""
from typing import List
from typing import Optional

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = s[0]
        for idx, char in enumerate(list(s)):
            temp_pal = char
            start = idx
            end = idx
            while True:
                start -= 1
                end += 1
                if (start < 0) or (end >= len(s)) or (s[start] != s[end]):
                    break
                else:
                    temp_pal = s[start:end+1]
                    if len(temp_pal) > len(max_pal):
                        max_pal = temp_pal
            start = idx + 1
            end = idx
            while True:
                start -= 1
                end += 1
                if (start < 0) or (end >= len(s)) or (s[start] != s[end]):
                    break
                else:
                    temp_pal = s[start:end+1]
                    if len(temp_pal) > len(max_pal):
                        max_pal = temp_pal
        return max_pal

def main():
    sol = Solution()
    print('Output:', sol.longestPalindrome("babad"))
    print('Expected:', "bab")

if __name__ == "__main__":
    main()
