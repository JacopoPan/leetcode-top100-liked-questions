"""
Runtime: 3730 ms, faster than 5.04% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14.4 MB, less than 19.92% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""
from typing import List
from typing import Optional
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        active = tokens
        while len(active) > 1:
            for idx, t in enumerate(active):
                if t == '+':
                    res = int(active[idx-2]) + int(active[idx-1])
                    active = active[:idx-2] + [res] + active[idx+1:]
                    break
                if t == '-':
                    res = int(active[idx-2]) - int(active[idx-1])
                    active = active[:idx-2] + [res] + active[idx+1:]
                    break
                if t == '*':
                    res = int(active[idx-2]) * int(active[idx-1])
                    active = active[:idx-2] + [res] + active[idx+1:]
                    break
                if t == '/':
                    res = int(int(active[idx-2]) / int(active[idx-1]))
                    active = active[:idx-2] + [res] + active[idx+1:]
                    break
        return active[0]

def main():
    sol = Solution()
    print('Output:', sol.evalRPN(["2","1","+","3","*"]))
    print('Expected:', 9)

if __name__ == "__main__":
    main()
