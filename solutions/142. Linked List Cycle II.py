"""
Runtime: 1626 ms, faster than 5.01% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.3 MB, less than 73.61% of Python3 online submissions for Linked List Cycle II.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cache = []
        while head is not None:
            cache.append(head)
            head = head.next
            if head in cache:
                return head
        return None

def main():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    sol = Solution()
    ans = sol.detectCycle(n1)
    print('Output:',ans.val)
    print('Expected:', 2)

if __name__ == "__main__":
    main()
