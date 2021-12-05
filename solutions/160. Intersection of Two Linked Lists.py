"""
Runtime: 168 ms, faster than 49.62% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.6 MB, less than 36.80% of Python3 online submissions for Intersection of Two Linked Lists.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == headB:
            return headA
        a_ptr = []
        b_ptr = []
        while headA is not None:
            a_ptr.append(headA)
            headA = headA.next
        while headB is not None:
            b_ptr.append(headB)
            headB = headB.next
        for i in range(max(len(a_ptr), len(b_ptr))):
            a = a_ptr[len(a_ptr)-1-i] if (len(a_ptr)-1-i) >= 0 else None
            b = b_ptr[len(b_ptr)-1-i] if (len(b_ptr)-1-i) >= 0 else None
            if a !=  b:
                if i == 0:
                    return None
                else:
                    return a_ptr[len(a_ptr)-i]
        else:
            return None

def main():
    n1a = ListNode(4)
    n2a = ListNode(1)
    #
    n1b = ListNode(5)
    n2b = ListNode(6)
    n3b = ListNode(1)
    #
    n1 = ListNode(8)
    n2 = ListNode(4)
    n3 = ListNode(5)
    #
    n1a.next = n2a
    n2a.next = n1
    #
    n1b.next = n2b
    n2b.next = n3b
    n3b.next = n1
    #
    n1.next = n2
    n2.next = n3
    #
    sol = Solution()
    ans = sol.getIntersectionNode(n1a, n1b)
    print('Output:', ans.val)
    print('Expected:', 8)

if __name__ == "__main__":
    main()
