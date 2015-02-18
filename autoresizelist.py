"""autoresizelist.py - list wrapper that automatically expands the list when
indices outside its current range are accessed """

__author__ = 'caleb'
__date__ = "2015-02-17"


class AutoResizeList:
    def __init__(self, initial_data=None, fill=None):
        if initial_data is None:
            self._data = []
        else:
            self._data = initial_data
        self.fill = fill

    def __setitem__(self, key, value):
        if key >= len(self._data):
            self._data += [self.fill] * (key - len(self._data) + 1)
        self._data[key] = value

    def __getitem__(self, key):
        #if key >= len(self._data):
        #    self._data += [self.fill] * (key - len(self._data) + 1)
        return self._data[key]

    def __delitem__(self, key):
        del self._data[key]

    def __repr__(self):
        return str(self._data)

    def __eq__(self, other):
        return self._data == other._data

    def __len__(self):
        return len(self._data)

    def append(self, item):
        self._data.append(item)

    def prepend(self, item):
        self._data = [item] + self._data

if __name__ == "__main__":
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*autoresizelist*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)
