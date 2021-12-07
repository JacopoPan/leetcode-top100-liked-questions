"""
Runtime: 36 ms, faster than 64.67% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.7 MB, less than 25.77% of Python3 online submissions for Binary Tree Level Order Traversal.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = [root]
        ret = []
        while len(nodes) > 0:
            new_nodes = []
            temp = []
            for n in nodes:
                if n is not None:
                    temp.append(n.val)
                    if n.left is not None:
                        new_nodes.append(n.left)
                    if n.right is not None:
                        new_nodes.append(n.right)
            nodes = new_nodes
            if len(temp) > 0:
                ret.append(temp)
        return ret

def main():
    sol = Solution()
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print('Output:', sol.levelOrder(t))
    print('Expected:', [[3],[9,20],[15,7]])

if __name__ == "__main__":
    main()
