# Our design of LRU Cache contains 2 following parts:
# 1. A hash map
# 2. A doubly linked list
# The hash map stores the key-value pairs. The key is the key of the cache, and the value is 
# the node of the doubly linked list.
# The doubly linked list is used to store items in the cache. Each time an item is accessed/updated,
# we move it to the head of the list. When the capacity is full, we remove the last item in the list.
# By using 2 dummy node _head and _tail, we can avoid many edge cases, such as when the list is empty, list has only 1 item, etc.


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self._head = Node(0, 0)
        self._tail = Node(0, 0)
        self._head.next = self._tail
        self._tail.prev = self._head

        self.hash_map = {}

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        
        obj = self.hash_map[key]
        # since we always have 2 dummies head and tail, we don't have to worry if obj.prev or obj.next is None
        obj.prev.next = obj.next
        obj.next.prev = obj.prev

        # put obj to the head of the list
        obj.next = self._head.next
        obj.prev = self._head
        self._head.next.prev = obj
        self._head.next = obj

        print(obj.value)
        return obj.value


    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            obj = self.hash_map[key]
            obj.prev.next = obj.next
            obj.next.prev = obj.prev

            obj.value = value

            # put obj to the head of the list
            obj.next = self._head.next
            obj.prev = self._head
            self._head.next.prev = obj
            self._head.next = obj
        else:
            obj = Node(key, value)
            if len(self.hash_map) >= self.capacity:
                # remove the last item in the list
                last = self._tail.prev
                last.prev.next = self._tail
                self._tail.prev = last.prev

                del self.hash_map[last.key]
            
            # put obj to the head of the list
            obj.next = self._head.next
            obj.prev = self._head
            self._head.next.prev = obj
            self._head.next = obj
            self.hash_map[key] = obj

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
    
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(2,1)
    cache.put(3,2)
    cache.get(3)
    cache.get(2)
    cache.put(4,3)
    cache.get(2)
    cache.get(3)
    cache.get(4)