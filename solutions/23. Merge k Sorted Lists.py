"""
Runtime: 7612 ms, faster than 5.00% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.6 MB, less than 80.72% of Python3 online submissions for Merge k Sorted Lists.
"""
from typing import List
from typing import Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = None
        running_ptr = None
        while True:
            non_inf_val = False
            min_idx = -1
            min_val = math.inf
            for i in range(len(lists)):
                if lists[i] is not None:
                    non_inf_val = True
                    if lists[i].val < min_val:
                        min_val = lists[i].val
                        min_idx = i
            if non_inf_val == False:
                break
            to_add = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            if ans == None:
                ans = to_add
                running_ptr = ans
            else:
                running_ptr.next = to_add
                running_ptr = running_ptr.next
        return ans

def main():
    n11 = ListNode(1)
    n12 = ListNode(4)
    n13 = ListNode(5)
    n11.next = n12
    n12.next = n13
    n21 = ListNode(1)
    n22 = ListNode(3)
    n23 = ListNode(4)
    n21.next = n22
    n22.next = n23
    n31 = ListNode(2)
    n32 = ListNode(6)
    n31.next = n32
    inp = [n11, n21, n31]
    sol = Solution()
    ans = sol.mergeKLists(inp)
    list_ans = []
    while ans is not None:
        list_ans.append(ans.val)
        ans = ans.next
    print('Output:', list_ans)
    print('Expected:', [1,1,2,3,4,4,5,6])

if __name__ == "__main__":
    main()
