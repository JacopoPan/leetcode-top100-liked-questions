"""
Runtime: 76 ms, faster than 98.05% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 15.6 MB, less than 28.24% of Python3 online submissions for Merge Two Binary Trees.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        else:
            return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right))

def main():
    sol = Solution()
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    ans = sol.mergeTrees(t1, t2)
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
    print('Expected:', [3,4,5,5,4,7])

if __name__ == "__main__":
    main()
