"""
Runtime: 40 ms, faster than 89.32% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.2 MB, less than 61.09% of Python3 online submissions for Delete Node in a Linked List.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node is not None:
            node.val = node.next.val
            if node.next.next == None:
                node.next = None
            node = node.next

def main():
    sol = Solution()
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(1)
    n4 = ListNode(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    sol.deleteNode(n2)
    list_ans = []
    head = n1
    while head is not None:
        list_ans.append(head.val)
        head = head.next
    print('Output:', list_ans)
    print('Expected:', [4,1,9])

if __name__ == "__main__":
    main()
