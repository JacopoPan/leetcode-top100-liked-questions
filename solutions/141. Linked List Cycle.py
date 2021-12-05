"""
Runtime: 4552 ms, faster than 5.04% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.7 MB, less than 24.84% of Python3 online submissions for Linked List Cycle.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next
            for n in nodes:
                if head == n:
                    return True
        return False

def main():
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    sol = Solution()
    print('Output:', sol.hasCycle(n1))
    print('Expected:', True)

if __name__ == "__main__":
    main()
