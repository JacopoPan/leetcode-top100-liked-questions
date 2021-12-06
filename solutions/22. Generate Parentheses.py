"""
Runtime: 32 ms, faster than 87.16% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.6 MB, less than 41.07% of Python3 online submissions for Generate Parentheses.
"""
from typing import List
from typing import Optional

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = ['(']
        opened = [1]
        closed = [0]
        steps = 1
        while steps < (2*n):
            new_ret = []
            new_opened = []
            new_closed = []
            for idx, s in enumerate(ret):
                if opened[idx] < n:
                    new_ret.append(s+'(')
                    new_opened.append(opened[idx] + 1)
                    new_closed.append(closed[idx])
                if opened[idx] > closed[idx]:
                    new_ret.append(s+')')
                    new_opened.append(opened[idx])
                    new_closed.append(closed[idx] + 1)
            ret = new_ret
            opened = new_opened
            closed = new_closed
            steps += 1    
        return ret

def main():
    sol = Solution()
    print('Output:', sol.generateParenthesis(3))
    print('Expected:', ["((()))","(()())","(())()","()(())","()()()"])

if __name__ == "__main__":
    main()
