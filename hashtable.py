############ HashTable helper functions
def hash_function(key_str, size):
    return sum([ord(c) for c in key_str]) % size


############ HashTable class
class HashTable:
    """ Hash table which uses strings for keys. Value can be any object. """

    def __init__(self, capacity=1000):
        """ Capacity defaults to 1000. """

        self.capacity = capacity
        self.size = 0
        # Storage format: [ [ [key1, value], [key2, value] ], [ [key3, value] ] ]
        # The outmost list is the one which the hash function maps the index to. The next inner
        # Array is the list of objects in that storage cell. The 3rd level is the individual
        # item array, where the 1st item is the key, and the 2nd item is the value.
        self.data = [[] for i in range(capacity)]

    def set(self, key, obj):
        """ Insert object with key into hashtable. If key already exists, then the object will be
        updated. Key must be a string. Returns self. """

        index = hash_function(key, self.capacity)
        storage_cell = self.data[index]
        for item in storage_cell:
            if item[0] == key:
                item[1] = obj
        else:
            storage_cell.append([key, obj])
            self.size += 1

        return self

    def get(self, key):
        """ Get object with key (key must be a string). If not found, it will raise a KeyError. """

        index = hash_function(key, self.capacity)
        storage_cell = self.data[index]
        for item in storage_cell:
            if item[0] == key:
                return item[1]
        else:
            raise KeyError(key)

    def remove(self, key):
        """ Remove the object associated with key from the hashtable. If found, the object will
        be returned. If not found, KeyError will be raised. """

        index = hash_function(key, self.capacity)
        storage_cell = self.data[index]
        item_to_remove = None
        for item in storage_cell:
            if item[0] == key:
                item_to_remove = item
        if item_to_remove:
                storage_cell.remove(item)
                self.size -= 1
                return item[1]
        else:
            raise KeyError(key)

if __name__ == "__main__":
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*hashtable*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)

