"""
Runtime: 52 ms, faster than 64.15% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.1 MB, less than 60.89% of Python3 online submissions for Kth Smallest Element in a BST.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.vals = []
        self.ans = None
        self.depthFirst(root)
        return self.ans

    def depthFirst(self, root: Optional[TreeNode]):
        if self.ans is not None:
            return
        if root is not None:
            self.depthFirst(root.left)
            self.vals.append(root.val)
            if len(self.vals) == self.k:
                self.ans = self.vals[-1]
            self.depthFirst(root.right)

def main():
    sol = Solution()
    t = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print('Output:', sol.kthSmallest(t, 1))
    print('Expected:', 1)

if __name__ == "__main__":
    main()
