# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f"<{self.key}, {self.value}>"

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0 


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # apply hash function to key to find the bucket index

        # # double size if half full
        # if self.size > len(self.storage)/2:
        #     self.resize()

        self.size += 1

        bucket_index = self._hash_mod(key)

        list_node = self.storage[bucket_index]

        if list_node is None:
            self.storage[bucket_index] = LinkedPair(key, value)
            return
        
        else:
            prev = None
            while list_node is not None:
                if list_node.key == key:
                    list_node.value = value
                    return
                prev = list_node
                list_node = list_node.next
            prev.next = LinkedPair(key, value)
            return 

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        bucket_index = self._hash_mod(key)
        # list_node = self.storage[bucket_index]
        current = prev = self.storage[bucket_index]

        if not current:
            return
        if current.key == key:
            self.storage[bucket_index] = current.next
        else:
            current = current.next
            while current:
                if current.key == key:
                    prev.next = current.next
                    break
                else:
                    current, prev = current.next, prev.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        bucket_index = self._hash_mod(key)
        list_node = self.storage[bucket_index]
        prev = None

        while list_node is not None and list_node.key != key:
            prev = list_node
            list_node = list_node.next

        if list_node is None:
            return None
        
        else:
            if prev is None:
                return list_node.value
            else:
                return prev.next.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity*2

        ht = HashTable(self.capacity)

        for i in range(len(self.storage)):
            if self.storage[i] is None:
                continue

            list_node = self.storage[i]

            # prev = None

            while list_node is not None:
                ht.insert(list_node.key, list_node.value)
                # prev = list_node
                list_node = list_node.next

        self.storage = ht.storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
