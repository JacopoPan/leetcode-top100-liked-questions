"""
Runtime: 126 ms, faster than 48.44% of Python3 online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 21.4 MB, less than 66.36% of Python3 online submissions for Binary Tree Maximum Path Sum.
"""
from typing import List
from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_path = -math.inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxGain(root)
        return self.max_path 

    def maxGain(self, node):
        if node is None:
            return 0
        left_gain = max(0, self.maxGain(node.left))
        right_gain = max(0, self.maxGain(node.right))
        current_max_path = node.val + left_gain + right_gain
        self.max_path = max(self.max_path, current_max_path)
        return node.val + max(left_gain, right_gain)

def main():
    sol = Solution()
    t = TreeNode(-10,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    print('Output:', sol.maxPathSum(t))
    print('Expected:', 42)

if __name__ == "__main__":
    main()
