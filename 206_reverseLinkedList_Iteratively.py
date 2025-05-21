from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur, nxt = None, head, head.next
        while cur != None:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt != None:
                nxt = nxt.next
        return pre

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = s.reverseList(head)
    while head != None:
        print(head.val)
        head = head.next
    # Output: 5 4 3 2 1
    # Explanation: After calling your function, the linked list is: 5 -> 4 -> 3 -> 2 -> 1
    # The function should return the new head of the reversed list.
        