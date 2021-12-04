"""
Runtime: 28 ms, faster than 86.44% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.4 MB, less than 13.97% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            ret = []
            if root.left is not None:
                ret.append(self.inorderTraversal(root.left))
            ret.append([root.val])
            if root.right is not None:
                ret.append(self.inorderTraversal(root.right))
            ret = [item for sublist in ret for item in sublist]
            return ret 

def main():
    sol = Solution()
    t = TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))
    print('Output:', sol.inorderTraversal(t))
    print('Expected:', [1,3,2])

if __name__ == "__main__":
    main()
