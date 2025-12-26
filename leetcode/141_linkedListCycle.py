from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution using Floyd's cycle detection algorithm
# Basically we have 2 pointers, one moves twice as fast as the other
# If there is a cycle, the 2 pointers will eventually meet
# If there is no cycle, the faster pointer will reach the end of the list
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(solution.hasCycle(head)) # True