"""
Runtime: 44 ms, faster than 92.75% of Python3 online submissions for Count and Say.
Memory Usage: 14.1 MB, less than 36.67% of Python3 online submissions for Count and Say.
"""
from typing import List
from typing import Optional

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        else:
            string = self.countAndSay(n-1)
            if len(string)==1:
                return '1'+str(string[0])
            say = ''
            counter = 1
            for idx, char in enumerate(string):
                if idx == 0:
                    continue
                if char != string[idx-1]:
                    say = say + str(counter) + str(string[idx-1])
                    counter = 1
                else:
                    counter += 1
            if counter != 0:
                say = say + str(counter) + str(string[-1])
            return say

def main():
    sol = Solution()
    print('Output:', sol.countAndSay(4))
    print('Expected:', '1211')

if __name__ == "__main__":
    main()
