"""
Runtime: 44 ms, faster than 98.29% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.3 MB, less than 43.64% of Python3 online submissions for Reverse Nodes in k-Group.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 0
        ans = head
        ptr = head
        while ptr is not None: 
            counter += 1
            if counter == k:
                rest_of_list = ptr.next
                ptr.next = None
                ans = self.invertList(head)
                now_end_of_prefix = head
                now_end_of_prefix.next = self.reverseKGroup(rest_of_list,k)
                break
            ptr = ptr.next
        return ans
  
    def invertList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        this = head
        nxt = this.next
        first = True
        while this is not None and nxt is not None:
            old_this = this
            old_nxt = nxt
            this = nxt
            nxt = nxt.next
            if first:
                old_this.next = None
                first = False
            old_nxt.next = old_this
        return this

def main():
    sol = Solution()
    inp = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    ans = sol.reverseKGroup(inp, 2)
    list_ans = []
    while ans is not None:
        list_ans.append(ans.val)
        ans = ans.next
    print('Output:', list_ans)
    print('Expected:', [2,1,4,3,6,5])

if __name__ == "__main__":
    main()
