from typing import Optional
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a copy of original list without the random pointer
        pre = None
        cp = None
        cur = head

        old_new_map = {}

        while cur:
            temp = Node(cur.val)
            if pre == None:
                cp = temp
                pre = temp
            else:
                pre.next = temp
                pre = pre.next

            old_new_map[cur] = temp
            cur = cur.next

        old = head
        new = cp

        while old and new:
            if old.random:
                new.random = old_new_map[old.random]
            old = old.next
            new = new.next

        return cp
    
if __name__ == "__main__":
    solution = Solution()
    head = Node(1)
    cp = solution.copyRandomList(head)
    while cp:
        print(cp.val)
        cp = cp.next