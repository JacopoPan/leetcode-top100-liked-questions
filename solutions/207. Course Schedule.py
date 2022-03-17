"""
Runtime: 104 ms, faster than 85.03% of Python3 online submissions for Course Schedule.
Memory Usage: 16.6 MB, less than 59.08% of Python3 online submissions for Course Schedule.
"""
from typing import List
from typing import Optional

class Solution:
    def __init__(self):
        self.prereq_of = None
        self.cache = None
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.prereq_of = [[] for _ in range(numCourses)]
        self.cache = [None for _ in range(numCourses)]
        for p in prerequisites:
            self.prereq_of[p[0]].append(p[1])
        for course in range(numCourses):
            if not self.doableCourse(course):
                return False
        return True
    
    def doableCourse(self, i):
        if self.cache[i] is not None:
            return self.cache[i]
        self.cache[i] = False
        for j in self.prereq_of[i]:
            if not self.doableCourse(j):
                return False
        self.cache[i] = True
        return True

def main():
    sol = Solution()
    print('Output:', sol.canFinish(2, [[1,0],[0,1]]))
    print('Expected:', False)

if __name__ == "__main__":
    main()