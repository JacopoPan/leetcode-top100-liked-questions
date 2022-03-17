"""
Runtime: 689 ms, faster than 26.71% of Python3 online submissions for Path Sum III.
Memory Usage: 15.4 MB, less than 51.69% of Python3 online submissions for Path Sum III.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.counter = 0
        self.path = []
        self.sums_up_to = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is not None:
            self.path.append(root.val)
            for i in range(len(self.sums_up_to)):
                self.sums_up_to[i] += root.val
            self.sums_up_to.append(root.val)
            for i in range(len(self.sums_up_to)):
                if self.sums_up_to[i]==targetSum:
                    self.counter += 1
            self.pathSum(root.left, targetSum)
            self.pathSum(root.right, targetSum)
            self.path.pop()
            for i in range(len(self.sums_up_to)):
                self.sums_up_to[i] -= self.sums_up_to[-1]
            self.sums_up_to.pop()
        return self.counter

def main():
    sol = Solution()
    inp = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3, TreeNode(-2))), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
    print('Output:', sol.pathSum(inp, 8))
    print('Expected:', 3)

if __name__ == "__main__":
    main()