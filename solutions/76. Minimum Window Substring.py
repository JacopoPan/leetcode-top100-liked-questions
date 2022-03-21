"""
Runtime: 104 ms, faster than 89.46% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.8 MB, less than 45.43% of Python3 online submissions for Minimum Window Substring.
"""
from typing import List
from typing import Optional

class Solution:    
    def minWindow(self, s: str, t: str) -> str:
        t_counters = {}
        for c in t:
            if c not in t_counters.keys():
                t_counters[c] = 1
            else:
                t_counters[c] += 1
        start = 0
        end = 0
        min_window = ''
        target_len = len(t)        
        for end in range(len(s)):
            if s[end] in t_counters.keys() and t_counters[s[end]] > 0:
                target_len -= 1
            if s[end] in t_counters.keys():
                t_counters[s[end]] -= 1
            while target_len == 0:
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
                    min_window = s[start:end+1]
                if s[start] in t_counters.keys():
                    t_counters[s[start]] += 1
                if s[start] in t_counters.keys() and t_counters[s[start]] > 0:
                    target_len += 1
                start+=1                
        return min_window

def main():
    sol = Solution()
    print('Output:', sol.minWindow("ADOBECODEBANC", "ABC"))
    print('Expected:', "BANC")

if __name__ == "__main__":
    main()
