"""
Runtime: 115 ms, faster than 58.29% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.8 MB, less than 6.22% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        elif len(nums)==2:
            return  TreeNode(nums[1],TreeNode(nums[0]))
        elif len(nums)==3:
            return  TreeNode(nums[1],TreeNode(nums[0]),TreeNode(nums[2]))
        else:
            return TreeNode(nums[len(nums)//2], 
                            self.sortedArrayToBST(nums[:len(nums)//2]),
                            self.sortedArrayToBST(nums[len(nums)//2+1:])
                           )

ans_list = []

def tree_print(root):
    if root is not None:
        ans_list.append(root.val)
        tree_print(root.left)
        tree_print(root.right)

def main():
    sol = Solution()
    ans = sol.sortedArrayToBST([-10,-3,0,5,9])
    tree_print(ans)
    print('Output:', ans_list)
    print('Expected:', [0,-3,9,-10,5])

if __name__ == "__main__":
    main()
