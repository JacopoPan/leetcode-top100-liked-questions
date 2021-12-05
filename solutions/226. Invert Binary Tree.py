"""
Runtime: 24 ms, faster than 97.42% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.2 MB, less than 76.47% of Python3 online submissions for Invert Binary Tree.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        else:
            return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))

def main():
    sol = Solution()
    t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    ans = sol.invertTree(t)
    list_ans = []
    ptrs = [ans]
    while len(ptrs) > 0:
        new_ptrs = []
        for p in ptrs:
            if p is not None:
                list_ans.append(p.val)
                new_ptrs.append(p.left)
                new_ptrs.append(p.right)
        ptrs = new_ptrs
    print('Output:', list_ans)
    print('Expected:', [4,7,2,9,6,3,1])

if __name__ == "__main__":
    main()
