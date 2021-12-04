"""
Runtime: 44 ms, faster than 54.69% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.2 MB, less than 40.74% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right) ) + 1

def main():
    sol = Solution()
    t = TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))
    print('Output:', sol.maxDepth(t))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
