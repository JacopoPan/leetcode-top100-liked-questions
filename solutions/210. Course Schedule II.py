"""
Runtime: 118 ms, faster than 73.32% of Python3 online submissions for Course Schedule II.
Memory Usage: 16.8 MB, less than 44.34% of Python3 online submissions for Course Schedule II.
"""
from typing import List
from typing import Optional

class Solution:      
    def __init__(self):
        self.prereq_of = None
        self.cache = None
        self.order = []
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.prereq_of = [[] for _ in range(numCourses)]
        self.cache = [None for _ in range(numCourses)]
        for p in prerequisites:
            self.prereq_of[p[0]].append(p[1])
        for course in range(numCourses):
            if not self.doableCourse(course):
                return []
        return self.order
    
    def doableCourse(self, i):
        if self.cache[i] is not None:
            return self.cache[i]
        self.cache[i] = False
        for j in self.prereq_of[i]:
            if not self.doableCourse(j):
                return False
        self.cache[i] = True
        self.order.append(i)
        return True

def main():
    sol = Solution()
    print('Output:', sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print('Expected:', [0,2,1,3])

if __name__ == "__main__":
    main()