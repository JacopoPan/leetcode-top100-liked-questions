"""
Runtime: 32 ms, faster than 84.30% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.2 MB, less than 79.09% of Python3 online submissions for Symmetric Tree.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pointers = [root]
        while len(pointers) > 0:
            new_pointers = []
            values = []
            for p in pointers:
                if p is not None:
                    values.append(p.val)
                    new_pointers.append(p.left)
                    new_pointers.append(p.right)
                else:
                    values.append(-101)
            pointers = new_pointers
            for i in range(int(len(values)/2)):
                if values[i] != values[len(values)-1-i]:
                    return False    
        return True

def main():
    sol = Solution()
    t = TreeNode(1,TreeNode(2,TreeNode(3,None,None),TreeNode(4,None,None)),TreeNode(2,TreeNode(4,None,None),TreeNode(3,None,None)))
    print('Output:', sol.isSymmetric(t))
    print('Expected:', True)

if __name__ == "__main__":
    main()
