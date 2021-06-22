class HashTable:
    def __init__(self, size):

        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):

        hashvalue = self.hashfunction(key, len(self.slots))

        # empty slots, you can place an item in an empty slot
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:

            # the key already exists, just replace the value
            if self.slots[hashvalue]== key:
                self.data[hashvalue] = data

            # there is not any slot available, you need to do a rehash
            else:

                nextSlot = self.rehash(hashvalue, len(self.slots))

                # find an empty slot
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data

                else:
                    self.data[nextSlot] = data

    def get(self, key):

        startSlot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startSlot

        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.slots[position]

            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    stop = True
        return data

    # this is the magic method that allows you to get the data
    def __getitem__(self, key):
        return self.get(key)

    # this is the magic method that allows you to set the data
    def __setitem__(self, key, data):
        self.put(key, data)

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        # go onto the next slot of the list
        return (oldhash+1)%size

def main():
    hash_table = HashTable(5)
    hash_table[2] = "Two"
    hash_table[1] = "One"
    print(hash_table[0])


main()