"""
Runtime: 76 ms, faster than 69.96% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.7 MB, less than 49.50% of Python3 online submissions for Populating Next Right Pointers in Each Node.
"""
from typing import List
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        level_list = [root]
        while len(level_list) > 0:
            next_level_list = []
            for n in level_list:
                if n.left is not None:
                    next_level_list.append(n.left)
                if n.right is not None:
                    next_level_list.append(n.right)
            for idx, n in enumerate(next_level_list[0:len(next_level_list)-1]):
                n.next = next_level_list[idx+1]
            level_list = next_level_list
        return root

ans_list = []

def tree_print(root):
    if root is not None:
        ptr = root
        temp = []
        while ptr is not None:
            temp.append(ptr.val)
            ptr = ptr.next
        ans_list.append(temp)
        tree_print(root.left)

def main():
    sol = Solution()
    inp = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    ans = sol.connect(inp)
    tree_print(ans)
    print('Output:', ans_list)
    print('Expected:', [[1], [2,3], [4,5,6,7]])

if __name__ == "__main__":
    main()
