"""
Runtime: 440 ms, faster than 8.17% of Python3 online submissions for Max Points on a Line.
Memory Usage: 14.9 MB, less than 28.30% of Python3 online submissions for Max Points on a Line.
"""
from typing import List
from typing import Optional

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<3:
            return len(points)
        cache = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                one = points[i]
                two = points[j]
                a = one[1] - two[1]
                b = two[0] - one[0]
                c = one[0]*two[1] - two[0]*one[1]
                g = self.gcd(self.gcd(a, b), c)
                a /= g
                b /= g
                c /= g
                if (a,b,c) not in cache.keys():
                    cache[(a,b,c)] = 0
        ans = -1
        for i in range(len(points)):
            for k, v in cache.items():
                if (k[0]*points[i][0]+k[1]*points[i][1]+k[2]) == 0.0:
                    cache[k] += 1
                    ans = max(ans, cache[k])
        return ans
    
    def gcd(self, x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

def main():
    sol = Solution()
    print('Output:', sol.maxPoints([[-6,-1],[3,1],[12,3]]))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
