"""
Runtime: 36 ms, faster than 98.86% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15 MB, less than 88.44% of Python3 online submissions for Fizz Buzz.
"""
from typing import List
from typing import Optional

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            flag1 = i%3
            flag2 = i%5
            if flag1==0 and flag2==0:
                ans.append("FizzBuzz")
            elif flag1==0:
                ans.append("Fizz")
            elif flag2==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans

def main():
    sol = Solution()
    print('Output:', sol.fizzBuzz(3))
    print('Expected:', ["1","2","Fizz"])

if __name__ == "__main__":
    main()
