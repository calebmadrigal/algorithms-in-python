############ HashTable helper functions
def hash_function(key_str, size):
    return sum([ord(c) for c in key_str]) % size


############ HashTable class
class HashTable:
    """ Hash table which uses strings for keys. Value can be any object.

    Example usage:

        ht = HashTable(10)
        ht.set('a', 1).set('b', 2).set('c', 3)
        ht['c'] = 30

    """

    def __init__(self, capacity=1000):
        """ Capacity defaults to 1000. """

        self.capacity = capacity
        self.size = 0
        self._keys = []
        # Storage format: [ [ [key1, value], [key2, value] ], [ [key3, value] ] ]
        # The outmost list is the one which the hash function maps the index to. The next inner
        # Array is the list of objects in that storage cell. The 3rd level is the individual
        # item array, where the 1st item is the key, and the 2nd item is the value.
        self.data = [[] for _ in range(capacity)]

    def _find_by_key(self, key, find_result_func):
        index = hash_function(key, self.capacity)
        hash_table_cell = self.data[index]
        found_item = None
        for item in hash_table_cell:
            if item[0] == key:
                found_item = item
                break

        return find_result_func(found_item, hash_table_cell)

    def set(self, key, obj):
        """ Insert object with key into hash table. If key already exists, then the object will be
        updated. Key must be a string. Returns self. """

        def find_result_func(found_item, hash_table_cell):
            if found_item:
                found_item[1] = obj
            else:
                hash_table_cell.append([key, obj])
                self.size += 1
                self._keys.append(key)

        self._find_by_key(key, find_result_func)
        return self

    def get(self, key):
        """ Get object with key (key must be a string). If not found, it will raise a KeyError. """

        def find_result_func(found_item, _):
            if found_item:
                return found_item[1]
            else:
                raise KeyError(key)

        return self._find_by_key(key, find_result_func)

    def remove(self, key):
        """ Remove the object associated with key from the hashtable. If found, the object will
        be returned. If not found, KeyError will be raised. """

        def find_result_func(found_item, hash_table_cell):
            if found_item:
                hash_table_cell.remove(found_item)
                self._keys.remove(key)
                self.size -= 1
                return found_item[1]
            else:
                raise KeyError(key)

        return self._find_by_key(key, find_result_func)

    ####### Python's dict interface

    def keys(self):
        return self._keys

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.remove(key)

    def __repr__(self):
        return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self._keys]) + ' }'

if __name__ == "__main__":
    # Run unit tests
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*hashtable*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)
