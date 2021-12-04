"""
Runtime: 56 ms, faster than 9.04% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.4 MB, less than 7.90% of Python3 online submissions for Valid Parentheses.
"""
from typing import List
from typing import Optional

class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{' ]:
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] == '(':
                    stack = stack[0:len(stack)-1]
                else:
                    return False
            elif s[i] == ']':
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] == '[':
                    stack = stack[0:len(stack)-1]
                else:
                    return False
            elif s[i] == '}':
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] == '{':
                    stack = stack[0:len(stack)-1]
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

def main():
    sol = Solution()
    print('Output:', sol.isValid("()"))
    print('Expected:', True)

if __name__ == "__main__":
    main()
