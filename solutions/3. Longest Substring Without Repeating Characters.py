"""
Runtime: 84 ms, faster than 38.85% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB, less than 25.40% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
from typing import List
from typing import Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        start = 0
        length = 0
        max_length = 0
        for idx, l in enumerate(s):
            if l in s[start:idx]:
                start = s.index(l, start, idx) + 1
                length = len(s[start:idx]) + 1
            else:
                length += 1
                if length > max_length:
                    max_length = length
        return max_length

def main():
    sol = Solution()
    print('Output:', sol.lengthOfLongestSubstring("abcabcbb"))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
