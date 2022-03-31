"""
Runtime: 98 ms, faster than 44.64% of Python3 online submissions for Flatten Nested List Iterator.
Memory Usage: 18 MB, less than 6.51% of Python3 online submissions for Flatten Nested List Iterator.
"""
from typing import List
from typing import Optional

class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self): # -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat = self.flatten(nestedList)
        self.idx = 0
        self.len = len(self.flat)
        
    def flatten(self, nestedList: [NestedInteger]) -> [int]:
        ans = []
        all_int = True
        for e in nestedList:
            if not e.isInteger():
                all_int = False
                break
        if all_int:
            for e in nestedList:
                ans.append(e.getInteger())
            return ans
        else:
            for e in nestedList:
                if e.isInteger():
                    ans.append(e.getInteger())
                else:
                    ans = ans + self.flatten(e.getList())
            return ans

    def next(self) -> int:
        self.idx += 1
        return self.flat[self.idx-1]

    def hasNext(self) -> bool:
        if self.idx < self.len:
            return True
        else:
            return False

def main():
    print('Output:', 'Missing "NestedInteger" class implementation')
    print('Expected:', [1,1,2,1,1])

if __name__ == "__main__":
    main()
