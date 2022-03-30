"""
Runtime: 20 ms, faster than 99.96% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14.1 MB, less than 60.82% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level_list = [root]
        level_depth = 0
        ans = []
        while len(level_list) > 0:
            this_level_ints = []
            next_level_list = []
            for n in level_list:
                this_level_ints.append(n.val)
                if n.left is not None:
                    next_level_list.append(n.left)
                if n.right is not None:
                    next_level_list.append(n.right)
            if level_depth%2==0:
                ans.append(this_level_ints)
            else:
                ans.append(this_level_ints[::-1])
            level_depth += 1
            level_list = next_level_list
        return ans

def main():
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print('Output:', sol.zigzagLevelOrder(root))
    print('Expected:', [[3],[20,9],[15,7]])

if __name__ == "__main__":
    main()
