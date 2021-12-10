"""
Runtime: 32 ms, faster than 61.05% of Python3 online submissions for Decode String.
Memory Usage: 14.5 MB, less than 19.91% of Python3 online submissions for Decode String.
"""
from typing import List
from typing import Optional

class Solution:
    def decodeString(self, s: str) -> str:
        while True:
            no_par = True
            for idx, c in enumerate(s):
                exit = False
                if c == ']':
                    no_par = False
                    start = idx
                    while True:
                        if s[start] == '[':
                            init_num = start
                            while True:
                                init_num -= 1
                                if not s[init_num].isnumeric():
                                    init_num += 1
                                    break
                            repetitions = int(s[init_num:start])
                            replacement = ''
                            for i in range(repetitions):
                                replacement += s[start+1:idx]
                            new_s = s[:init_num] + replacement + s[idx+1:]
                            exit = True
                            break
                        start -= 1
                if exit:
                    start = 0
                    s = new_s
                    break
            if no_par:
                break
        return s

def main():
    sol = Solution()
    print('Output:', sol.decodeString("3[a2[c]]"))
    print('Expected:', "accaccacc")

if __name__ == "__main__":
    main()
