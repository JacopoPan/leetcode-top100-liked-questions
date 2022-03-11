"""
Runtime: 6845 ms, faster than 5.03% of Python3 online submissions for Sort List.
Memory Usage: 28.7 MB, less than 99.95% of Python3 online submissions for Sort List.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp = []
        save_head = head
        while head is not None:
            temp.append(head.val)
            head = head.next
        ordered = self.sortList2(temp)
        head = save_head
        idx = 0
        while head is not None:
            head.val = ordered[idx]
            idx += 1
            head = head.next
        return save_head

    def sortList2(self, l: List[int]) -> List[int]:
        if len(l) <= 1:
            return l
        else:
            head = self.sortList2(l[:len(l)//2])
            tail = self.sortList2(l[len(l)//2:])
            new = []
            while len(head) > 0 or len(tail) > 0:
                if len(head) == 0:
                    new.append(tail[0])
                    tail = tail[1:]
                elif len(tail) == 0:
                    new.append(head[0])
                    head = head[1:]
                elif head[0] < tail[0]:
                    new.append(head[0])
                    head = head[1:]
                else:
                    new.append(tail[0])
                    tail = tail[1:]
            return new

def main():
    sol = Solution()
    inp = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    ans = sol.sortList(inp)
    list_ans = []
    while ans is not None:
        list_ans.append(ans.val)
        ans = ans.next
    print('Output:', list_ans)
    print('Expected:', [1,2,3,4])

if __name__ == "__main__":
    main()
