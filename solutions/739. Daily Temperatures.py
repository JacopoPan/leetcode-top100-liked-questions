"""
Runtime: 1368 ms, faster than 23.12% of Python3 online submissions for Daily Temperatures.
Memory Usage: 25.8 MB, less than 23.67% of Python3 online submissions for Daily Temperatures.
"""
from typing import List
from typing import Optional

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []
        for idx, t in enumerate(temperatures):
            if idx == 0: stack.append([idx, t])
            elif len(stack) == 0 or t <= stack[-1][1]:
                stack.append([idx, t])
            else:
                popped = 0
                while len(stack) > 0 and t > stack[-1][1]:
                    p = stack.pop()
                    popped += 1
                    ret[p[0]] = idx - p[0]
                stack.append([idx, t])
        return ret

def main():
    sol = Solution()
    print('Output:', sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print('Expected:', [1,1,4,2,1,1,0,0])

if __name__ == "__main__":
    main()
