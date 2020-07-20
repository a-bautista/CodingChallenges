class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.D = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.D == False:
            return -1
        n = self.D[key]
        self.remove(n)
        self.add(n)
        return n.value

    def put(self, key: int, value: int) -> None:
        if key in self.D:
            self.remove(self.D[key])
            del self.D[key]
        elif len(self.D) == self.capacity:
            n = self.head.next
            self.remove(n)
            del self.D[n.key]

        # add back the removed item to the LRU cache
        n = Node(key, value)
        self.D[key] = n
        self.add(n)

    def remove(self, node):
        p = node.prev
        p.next = node.next
        node.next.prev = p

    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
    Time complexity: O(1)
    Space complexity: O(N)
    This code is not working at all because of this line  n = self.D[key]
'''