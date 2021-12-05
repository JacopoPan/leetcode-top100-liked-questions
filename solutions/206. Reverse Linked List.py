"""
Runtime: 40 ms, faster than 42.39% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.7 MB, less than 25.23% of Python3 online submissions for Reverse Linked List.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        this = head
        ptr_to_previous = None
        counter = -1
        while this is not None:
            counter += 1
            if this.next is None:
                this.next = ptr_to_previous
                return this
            else:
                nxt = this.next
                this.next = ptr_to_previous
                ptr_to_previous = this
                this = nxt

def main():
    sol = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ans = sol.reverseList(l)
    list_ans = []
    while ans is not None:
        list_ans.append(ans.val)
        ans = ans.next
    print('Output:', list_ans)
    print('Expected:', [5,4,3,2,1])

if __name__ == "__main__":
    main()
