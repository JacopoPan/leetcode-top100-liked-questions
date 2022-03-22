"""
Runtime: 116 ms, faster than 49.08% of Python3 online submissions for Implement strStr().
Memory Usage: 14.2 MB, less than 27.99% of Python3 online submissions for Implement strStr().
"""
from typing import List
from typing import Optional

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L1 = len(needle)
        L2 = len(haystack)
        if L1==0 or haystack==needle:
            return 0
        if L2==0 or L1 > L2:
            return -1
        for idx in range(len(haystack[:L2-L1+1])):
            if haystack[idx:idx+L1]==needle:
                return idx
        return -1

def main():
    sol = Solution()
    print('Output:',sol.strStr("hello", "ll"))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
