"""
Runtime: 62 ms, faster than 49.24% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 16.6 MB, less than 81.51% of Python3 online submissions for Odd Even Linked List.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        odd_ptr = head
        even_ptr = head.next
        even_head = even_ptr
        while odd_ptr is not None:
            old_odd = odd_ptr
            old_even = even_ptr
            if even_ptr is not None:
                odd_ptr = even_ptr.next
                if odd_ptr is not None:
                    even_ptr = odd_ptr.next
                else: 
                    even_ptr = None
            else:
                odd_ptr = None
                even_ptr = None
            old_odd.next = odd_ptr
            if old_odd.next is None:
                old_odd.next = even_head
            if old_even is not None:
                old_even.next = even_ptr
        return head

def main():
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ans = sol.oddEvenList(head)
    list_ans = []
    while ans is not None:
        list_ans.append(ans.val)
        ans = ans.next
    print('Output:', list_ans)
    print('Expected:', [1,3,5,2,4])

if __name__ == "__main__":
    main()
