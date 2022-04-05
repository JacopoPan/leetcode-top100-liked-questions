"""
Runtime: 69 ms, faster than 36.79% of Python3 online submissions for Largest Number.
Memory Usage: 13.9 MB, less than 24.02% of Python3 online submissions for Largest Number.
"""
from typing import List
from typing import Optional
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        temp = []
        for n in nums:
            temp.append(str(n)) 
        def cmp(b, a):
            return ((a+b)>(b+a))-((a+b)<(b+a))
        temp.sort(key = functools.cmp_to_key(cmp))
        ans = ''
        for n in temp:
            ans += n
        if ans.startswith('00'):
            return '0'
        else:
            return ans

def main():
    sol = Solution()
    print('Output:', sol.largestNumber([3,30,34,5,9]))
    print('Expected:', "9534330")

if __name__ == "__main__":
    main()
