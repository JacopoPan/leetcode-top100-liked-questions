"""
Runtime: 86 ms, faster than 53.12% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
Memory Usage: 14.4 MB, less than 16.35% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
"""
from typing import List
from typing import Optional

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counters = {}
        for char in s:
            if char not in counters.keys():
                counters[char] = 1
            else:
                counters[char] += 1
        if all (count >= k for count in counters.values()):
            return len(s)
        else:
            chars_below_count = []
            for key ,v in counters.items():
                if v < k:
                    chars_below_count.append(key)
            substrings = []
            temp = ''
            for idx, char in enumerate(s):
                if char not in chars_below_count:
                    temp += char
                else:
                    if temp != '':
                        substrings.append(temp)
                    temp = ''
                substrings.append(temp)
            results = []
            for subs in substrings:
                results.append(self.longestSubstring(subs,k))
            if results:
                return max(results)
            else:
                return 0

def main():
    sol = Solution()
    print('Output:', sol.longestSubstring("bbaaacbd", 3))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
