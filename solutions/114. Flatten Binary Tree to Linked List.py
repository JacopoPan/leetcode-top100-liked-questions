"""
Runtime: 36 ms, faster than 80.89% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.4 MB, less than 15.00% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    cache = []
    main = 0

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        this = False
        if self.main == 0:
            this = True
            self.cache = []
            self.main = 1
        if root is not None:
            self.cache.append(root.val)
            self.flatten(root.left)
            self.flatten(root.right)
            if this:
                self.cache = self.cache[::-1]
                root.left = None
                nxt_r = None
                for i in self.cache[0:-1]:
                    nxt_r = TreeNode(i, None, nxt_r)
                root.right = nxt_r

def main():
    sol = Solution()
    t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    sol.flatten(t)
    list_ans = []
    p = t
    while p is not None:
        list_ans.append(p.val)
        p = p.right
    print('Output:', list_ans)
    print('Expected:', [1,2,3,4,5,6])

if __name__ == "__main__":
    main()
