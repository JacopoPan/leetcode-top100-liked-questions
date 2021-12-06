"""
Runtime: 472 ms, faster than 6.80% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 16 MB, less than 93.37% of Python3 online submissions for Diameter of Binary Tree.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if (root is None) or (root.left is None and root.right is None):
            return 0
        elif root.left is None:
            return max(self.diameterOfBinaryTree(root.right), self.depthOfBinaryTree(root.right)+1)
        elif root.right is None:
            return max(self.diameterOfBinaryTree(root.left), self.depthOfBinaryTree(root.left) + 1)
        else:
            l_dia = self.diameterOfBinaryTree(root.left)
            r_dia = self.diameterOfBinaryTree(root.right)
            l_dep = self.depthOfBinaryTree(root.left)
            r_dep = self.depthOfBinaryTree(root.right)
            choices = [l_dia, r_dia, l_dep + r_dep + 2]
            return max(choices)
        
    def depthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if (root is None) or (root.left is None and root.right is None):
            return 0
        elif root.left is None:
            return self.depthOfBinaryTree(root.right) + 1
        elif root.right is None:
            return self.depthOfBinaryTree(root.left) + 1
        else:
            max_d = max(self.depthOfBinaryTree(root.right), self.depthOfBinaryTree(root.left))
            return max_d + 1

def main():
    sol = Solution()
    t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print('Output:', sol.diameterOfBinaryTree(t))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
