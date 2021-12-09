"""
Runtime: 192 ms, faster than 39.67% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 88 MB, less than 37.36% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        else:
            this_val = preorder[0]
            this_val_inorder_idx = inorder.index(this_val)
            return TreeNode(this_val, self.buildTree(preorder[1:this_val_inorder_idx+1], inorder[:this_val_inorder_idx]), self.buildTree(preorder[this_val_inorder_idx+1:], inorder[this_val_inorder_idx+1:]))

list_ans = []

def printTree(head):
    if head is not None:
        list_ans.append(head.val)
        printTree(head.left)
        printTree(head.right)

def main():
    sol = Solution()
    printTree(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]))
    print('Output:', list_ans)
    print('Expected:', [3,9,20,15,7])

if __name__ == "__main__":
    main()
