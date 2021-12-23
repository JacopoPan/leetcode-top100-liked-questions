"""
Runtime: 80 ms, faster than 33.51% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 25.7 MB, less than 45.85% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.pathToP = None
        self.pathToQ = None
        self.printPathsRec(root, [], 0)
        return next((a for a in self.pathToP[::-1] if a in self.pathToQ[::-1]), None)
 
    def printPathsRec(self, root, path, pathLen):
        if root is not None:
            if(len(path) > pathLen):
                # path[pathLen] = root.val
                path[pathLen] = root
            else:
                # path.append(root.val)
                path.append(root)
            pathLen = pathLen + 1
            if root == self.p:
                self.pathToP = path[:pathLen]
            if root == self.q:
                self.pathToQ = path[:pathLen]
            if root.left is not None or root.right is not None:
                self.printPathsRec(root.left, path, pathLen)
                self.printPathsRec(root.right, path, pathLen)
            else:
                pass
                # print(path[:pathLen])

def main():
    sol = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    a.left = b
    ans = sol.lowestCommonAncestor(a, a, b)
    print('Output:', ans.val)
    print('Expected:', 1)

if __name__ == "__main__":
    main()
