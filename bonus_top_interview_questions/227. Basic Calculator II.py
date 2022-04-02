"""
Runtime: 189 ms, faster than 16.21% of Python3 online submissions for Basic Calculator II.
Memory Usage: 20.1 MB, less than 5.55% of Python3 online submissions for Basic Calculator II.
"""
from typing import List
from typing import Optional

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        list_eq = []    
        operand = ''
        for idx, character in enumerate(s):
            if character in ['*', '/', '+', '-']:
                val = int(operand)
                operand = ''
                list_eq.append(val)
                list_eq.append(character)
            elif idx==len(s)-1:
                operand += character
                val = int(operand)
                list_eq.append(val)
            else:
                operand += character
        temp = []
        for idx in range(len(list_eq)):
            if list_eq[idx-1] == '*':
                temp.pop()
                temp.pop()
                res = list_eq[idx-2]*list_eq[idx]
                list_eq[idx] = res
                temp.append(res)
            elif list_eq[idx-1] == '/':
                temp.pop()
                temp.pop()
                res = list_eq[idx-2]//list_eq[idx]
                list_eq[idx] = res
                temp.append(res)
            else:
                temp.append(list_eq[idx])
        list_eq = temp
        temp = []
        for idx in range(len(list_eq)):
            if list_eq[idx-1] == '+':
                temp.pop()
                temp.pop()
                res = list_eq[idx-2]+list_eq[idx]
                list_eq[idx] = res
                temp.append(res)
            elif list_eq[idx-1] == '-':
                temp.pop()
                temp.pop()
                res = list_eq[idx-2]-list_eq[idx]
                list_eq[idx] = res
                temp.append(res)
            else:
                temp.append(list_eq[idx])
        list_eq = temp
        return list_eq[0]

def main():
    sol = Solution()
    print('Output:', sol.calculate("1+1+1"))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
