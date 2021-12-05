"""
Runtime: 816 ms, faster than 64.11% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 47.3 MB, less than 38.55% of Python3 online submissions for Palindrome Linked List.
"""
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        ptr = head
        while ptr is not None:
            l.append(ptr.val)
            ptr = ptr.next
        for i in range(int(len(l)//2)):
            if l[i] != l[len(l)-1-i]:
                return False
        return True

def main():
    sol = Solution()
    l = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print('Output:', sol.isPalindrome(l))
    print('Expected:', True)

if __name__ == "__main__":
    main()
