"""
Runtime: 39 ms, faster than 64.54% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14 MB, less than 30.15% of Python3 online submissions for Pascal's Triangle.
"""
from typing import List
from typing import Optional

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for r in range(numRows):
            ans.append([])
            if r==0:
                ans[r].append(1)
            elif r==1:
                ans[r].append(1)
                ans[r].append(1)
            else:
                for i in range(r+1):
                    if i==0 or i==r:
                        ans[r].append(1)
                    else:
                        ans[r].append(ans[r-1][i-1]+ans[r-1][i])      
        return ans

def main():
    sol = Solution()
    print('Output:', sol.generate(5))
    print('Expected:', [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

if __name__ == "__main__":
    main()
