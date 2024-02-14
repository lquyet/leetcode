from typing import Optional
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []

        # push all nodes into stack
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        l = len(stack)

        # pop from stack and insert into list
        cur = head
        for i in range(l//2):
            temp = stack.pop()

            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        cur.next = None

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution.reorderList(head)
    while head:
        print(head.val)
        head = head.next
        
        