from typing import List, Optional
from heapq import heappush, heappop, heapify

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapify(heap)

        dummy = ListNode(0)
        cur = dummy

        ln = len(lists)
        while any(lists):
            for i in range(ln):
                if lists[i]:
                    heappush(heap, lists[i].val)
                    lists[i] = lists[i].next

            
            # push the minimum value to the new list
            cur.next = ListNode(heappop(heap))
            cur = cur.next
        
        while heap:
            cur.next = ListNode(heappop(heap))
            cur = cur.next

        return dummy.next

if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]
    result = solution.mergeKLists(lists)
    while result:
        print(result.val)
        result = result.next