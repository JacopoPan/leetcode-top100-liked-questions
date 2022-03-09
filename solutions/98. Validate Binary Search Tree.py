"""
Runtime: 477 ms, faster than 5.10% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.9 MB, less than 25.22% of Python3 online submissions for Validate Binary Search Tree.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is not None:
            if root.left is None and root.right is None:
                return True
            elif root.left is not None and root.right is None:
                if root.val > self.maxInSubTree(root.left) and self.isValidBST(root.left):
                    return True
                else:
                    return False
            elif root.left is None and root.right is not None:
                if root.val < self.minInSubTree(root.right) and self.isValidBST(root.right):
                    return True
                else:
                    return False
            else:
                if root.val > self.maxInSubTree(root.left) and root.val < self.minInSubTree(root.right) \
                    and self.isValidBST(root.left) and self.isValidBST(root.right):
                    return True
                else:
                    return False            
            
    def maxInSubTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        else:
            candidates = [root.val, self.maxInSubTree(root.left), self.maxInSubTree(root.right)]
            return max(x for x in candidates if x is not None)
        
    def minInSubTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        else:
            candidates = [root.val, self.minInSubTree(root.left), self.minInSubTree(root.right)]
            return min(x for x in candidates if x is not None)

def main():
    sol = Solution()
    print('Output:', sol.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))
    print('Expected:', True)

if __name__ == "__main__":
    main()
