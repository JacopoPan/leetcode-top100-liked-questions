"""
Runtime: 32 ms, faster than 92.79% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 60.85% of Python3 online submissions for Remove Nth Node From End of List.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            temp = head
            pos = 0
            while temp is not None:
                pos += 1
                temp = temp.next
            remove = pos - n + 1
            if remove == 1:
                return head.next
            else:
                temp = head
                pos = 0
                while temp is not None:
                    pos += 1
                    if pos+1 == remove:
                        next_node = temp.next
                        temp.next = next_node.next
                    temp = temp.next
                return head

def main():
    sol = Solution()
    l =  ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ans = sol.removeNthFromEnd(l, 2)
    list_ans = []
    p = ans
    while p is not None:
        list_ans.append(p.val)
        p = p.next
    print('Output:', list_ans)
    print('Expected:', [1,2,3,5])

if __name__ == "__main__":
    main()
