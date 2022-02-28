"""
Runtime: 47 ms, faster than 45.19% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 43.00% of Python3 online submissions for Swap Nodes in Pairs.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            old_head = head
            old_rest_of = head.next.next
            head = head.next
            head.next = old_head
            head.next.next = self.swapPairs(old_rest_of)
            return head

def main():
    sol = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    ans = sol.swapPairs(l)
    list_ans = []
    while ans is not None:
        list_ans.append(ans.val)
        ans = ans.next
    print('Output:', list_ans)
    print('Expected:', [2,1,4,3])

if __name__ == "__main__":
    main()
