"""
Runtime: 64 ms, faster than 90.63% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.3 MB, less than 73.63% of Python3 online submissions for Add Two Numbers.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        init = cur
        carry = 0
        while True:      
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            cur.val = l1_val + l2_val + carry
            carry = 0
            if cur.val >= 10:
                carry = 1
                cur.val = cur.val - 10    
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is None and l2 is None and carry == 0:
                break
            cur.next = ListNode()
            cur = cur.next
        return init

def main():
    sol = Solution()
    l1 =  ListNode(2, ListNode(4, ListNode(3)))
    l2 =  ListNode(5, ListNode(6, ListNode(4)))
    ans = sol.addTwoNumbers(l1, l2)
    list_ans = []
    p = ans
    while p is not None:
        list_ans.append(p.val)
        p = p.next
    print('Output:', list_ans)
    print('Expected:', [7,0,8])

if __name__ == "__main__":
    main()
