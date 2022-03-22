"""
Runtime: 64 ms, faster than 59.87% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.9 MB, less than 82.92% of Python3 online submissions for Roman to Integer.
"""
from typing import List
from typing import Optional

class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        new_s = []
        for digit in s:
            new_s.append(mapping[digit])
        print(new_s)
        ans = 0
        temp = 0
        for idx, val in enumerate(new_s):
            if idx == 0:
                temp = val
                continue
            if val == new_s[idx-1]:
                temp += val
            else:
                if val > new_s[idx-1]:
                    ans -= temp
                    temp = val
                else:
                    ans += temp
                    temp = val
        ans += temp
        return ans

def main():
    sol = Solution()
    print('Output:', sol.romanToInt("III"))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
