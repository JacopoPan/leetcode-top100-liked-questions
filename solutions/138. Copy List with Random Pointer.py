"""
Runtime: 49 ms, faster than 58.17% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 14.8 MB, less than 85.55% of Python3 online submissions for Copy List with Random Pointer.
"""
from typing import List
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        old_to_new_ptrs = {}
        new_head = Node(head.val, random=head.random)
        old_to_new_ptrs[head] = new_head
        ptr1 = head.next
        ptr2 = new_head
        while ptr1 is not None:
            temp = Node(ptr1.val, random=ptr1.random)
            ptr2.next = temp
            old_to_new_ptrs[ptr1] = temp
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2 = new_head
        while ptr2 is not None:
            if ptr2.random is not None:
                ptr2.random = old_to_new_ptrs[ptr2.random]
            ptr2 = ptr2.next
        return new_head

def main():
    sol = Solution()
    n2 = Node(2)
    n1 = Node(1,next=n2)
    n0 = Node(0,next=n1)
    n1.random = n0
    ans = sol.copyRandomList(n0)
    output = []
    while ans is not None: 
        if ans.random is not None:
            output.append([ans.val, ans.random.val])
        else:
            output.append([ans.val, None])
        ans = ans.next
    print('Output:', output)
    print('Expected:', [[0, None], [1, 0], [2, None]])

if __name__ == "__main__":
    main()
