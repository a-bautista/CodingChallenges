'''
        I need a data structure that performs the following in O(1):
            Gets the key/ check if the key exists.
            Puts the key.
            Deletes the least used key.

        There's a data structure called ordered dictionary that preserves the order in which keys were inserted.
        Time complexity is O(1) because all get and put operations are in the OrderedDict
'''
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self: # if the key is not contained
            return -1

        self.move_to_end(key) # get the requested key from the dict
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key) # add the key to the OrderedDict

        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False) # least used

def main():
    obj = LRUCache(capacity=2)
    param_1 = obj.get(2) # it's going to display an error
    obj.put(2,2)
    obj.put(3,3)
    print(param_1)

    param_2 = obj.get(2)
    print(param_2)

    obj.put(4,4)
    param_3 = obj.get(3) # this value has been deleted because a put was inserted and 3 was deleted because it wasn't used
    print(param_3)

main()





