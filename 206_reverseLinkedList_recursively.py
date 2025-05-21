from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head, None)

    def helper(self, node, prev):
        if node.next is None:
            node.next = prev
            return node
        
        head = self.helper(node.next, node)
        node.next = prev
        return head
        
# co solution dung node.next.next, tham khao tren leetcode solution

        

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
        