"""
Runtime: 36 ms, faster than 44.03% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 14.4 MB, less than 21.58% of Python3 online submissions for Binary Tree Right Side View.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        nodes = [root]
        vals_by_level = []
        while len(nodes) > 0:
            new_nodes = []
            temp = []
            for n in nodes:
                temp.append(n.val)
                if n.left is not None:
                    new_nodes.append(n.left)
                if n.right is not None:
                    new_nodes.append(n.right)
            vals_by_level.append(temp)
            nodes = new_nodes
        ret = []
        for l in vals_by_level:
            ret.append(l[-1])
        return ret

def main():
    sol = Solution()
    t = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print('Output:', sol.rightSideView(t))
    print('Expected:', [1,3,4])

if __name__ == "__main__":
    main()
