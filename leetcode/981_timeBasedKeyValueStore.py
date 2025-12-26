class TimeMap:
    def __init__(self):
        # store data in a hashmap
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # check if key already exists
        if key in self.storage:
            # if it does, append the new value to the list
            self.storage[key].append((value, timestamp))
        else:
            # otherwise, create a new list with the value
            self.storage[key] = [(value, timestamp)]

        return None

    def get(self, key: str, timestamp: int) -> str:
        # check if key exists
        if key not in self.storage:
            return ""
        
        # get the list of values
        values = self.storage[key]
        return self.binary_search(values, timestamp)
    
    def binary_search(self, values, timestamp) -> str:
        l, r = 0, len(values) - 1

        while l <= r:
            # avoid overflow, not sure it could happen or not in Python =))
            mid = l + (r - l) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        return values[r][0] if values[r][1] <= timestamp else ""


"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.

void set(String key, String value, int timestamp) Stores the key key with the value value at the given time 
timestamp.

String get(String key, int timestamp) Returns a value such that set was called previously, with 
timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated 
with the largest timestamp_prev. If there are no values, it returns "".
"""

# Personal notes: the timestamp for the same key is in increasing order

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
    

