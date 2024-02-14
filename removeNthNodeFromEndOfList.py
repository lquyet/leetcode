from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and not head.next:
            return None

        fast = head
        slow = head
        pre = None

        for _ in range(n-1):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            pre = slow
            slow = slow.next
        
        if not pre:
            head = head.next
            slow = None
            return head
        pre.next = slow.next
        slow = None
        return head
    

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = solution.removeNthFromEnd(head, 2)
    while head:
        print(head.val)
        head = head.next
