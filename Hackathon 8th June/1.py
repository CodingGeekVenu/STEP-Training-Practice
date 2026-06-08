import sys 

class Node:
    def __init__(self, key, value, next_node = None):
        self.key = key
        self.value = value
        self.next = next

class HashMap:
    def __init__(self):
        self.capacity = 16
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash_fn(self, key):
        h = 0
        for c in key:
            h = (h * 31 + ord(c)) % self.capacity
        return h
    
    def put(self, key, value):
        index = self.hash_fn(key)
        curr = self.buckets[index]

        while curr:
            if curr.key == key:
                curr.value = value 
                return
            curr = curr.next

    

        

