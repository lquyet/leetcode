from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        cur = head
        temp = cur

        if not head:
            return None

        # first, make sure that the current list has at least k nodes
        while count < k:
            temp = temp.next
            count += 1
            if not temp:
                return head
        
        # reverse the first k nodes
        _next = temp.next if temp else None
        cur, cur_end = self.reverse(cur, temp)
            
        # recursively reverse the rest of the list
        cur_end.next = self.reverseKGroup(_next, k) 

        return cur   
    
    def reverse(self, head: Optional[ListNode], end: Optional[ListNode]):
        prev = None
        cur = head
        while cur != end:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        cur.next = prev

        return cur, head
    
        
if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
    result = solution.reverseKGroup(l1, 8)
    while result:
        print(result.val)
        result = result.next