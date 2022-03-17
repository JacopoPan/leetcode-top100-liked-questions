"""
Runtime: 75 ms, faster than 35.53% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 14 MB, less than 94.23% of Python3 online submissions for Longest Valid Parentheses.
"""
from typing import List
from typing import Optional

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        longest = 0
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                if len(stack)>1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest

def main():
    sol = Solution()
    print('Output:', sol.longestValidParentheses("()(()"))
    print('Expected:', 2)

if __name__ == "__main__":
    main()
