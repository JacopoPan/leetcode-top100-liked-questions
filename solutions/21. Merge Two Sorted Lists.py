"""
Runtime: 28 ms, faster than 98.36% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.1 MB, less than 96.31% of Python3 online submissions for Merge Two Sorted Lists.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = l1
        l2 = l2
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            head = ListNode()
            cur = head
            while l1 is not None or l2 is not None:            
                if l1 is None:
                    cur.next = l2
                    break
                elif l2 is None:
                    cur.next = l1
                    break
                else:
                    new = ListNode()
                    if l1.val <= l2.val:
                        new.val = l1.val
                        l1 = l1.next
                    else:
                        new.val = l2.val
                        l2 = l2.next
                    cur.next = new
                    cur = new
            return head.next

def main():
    sol = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))
    ans = sol.mergeTwoLists(l1, l2)
    list_ans = []
    while ans is not None:
        list_ans.append(ans.val)
        ans = ans.next
    print('Output:', list_ans)
    print('Expected:', [1,1,2,3,4,4])

if __name__ == "__main__":
    main()
