import unittest
import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import hashtable


class HashFunctionTest(unittest.TestCase):

    def test(self):
        hash10 = lambda key: hashtable.hash_function(key, 10)
        self.assertIn(hash10("a"), range(10))
        self.assertIn(hash10("b"), range(10))
        self.assertIn(hash10("caleb"), range(10))
        self.assertIn(hash10("more than a feeling"), range(10))

        hash4 = lambda key: hashtable.hash_function(key, 4)
        self.assertIn(hash4("a"), range(4))
        self.assertIn(hash4("b"), range(4))
        self.assertIn(hash4("caleb"), range(4))
        self.assertIn(hash4("more than a feeling"), range(4))


class HashTableTest(unittest.TestCase):
    def testCreate(self):
        ht = hashtable.HashTable(10)
        self.assertEqual(ht.capacity, 10)
        self.assertEqual(ht.size, 0)

        ht = hashtable.HashTable()
        self.assertEqual(ht.capacity, 1000)

    def testSetAndGet(self):
        # Basic set and get
        ht = hashtable.HashTable(10)
        ht.set('a', 1)
        self.assertEqual(ht.get('a'), 1)
        self.assertEqual(ht.size, 1)

        # Check update functionality
        ht.set('a', 2)
        self.assertEqual(ht.get('a'), 2)
        self.assertEqual(ht.size, 1)

        # Make sure we can add a 2nd element
        ht.set('b', 10)
        self.assertEqual(ht.get('b'), 10)
        self.assertEqual(ht.get('a'), 2)
        self.assertEqual(ht.size, 2)

        # Assert ht.set returns itself (for fluent calls)
        self.assertEqual(ht.set('c', 5), ht)

        # Test fluent set functionality
        ht.set('d', 100).set('e', 200).set('f', 300)
        self.assertEqual(ht.get('d'), 100)
        self.assertEqual(ht.get('e'), 200)
        self.assertEqual(ht.get('f'), 300)

    def testBadGet(self):
        ht = hashtable.HashTable(10)
        self.assertRaises(KeyError, ht.get, 'a')

    def testRemove(self):
        ht = hashtable.HashTable(10)
        self.assertRaises(KeyError, ht.remove, 'a')

        ht.set('a', 1)
        removed_item = ht.remove('a')
        self.assertEqual(removed_item, 1)
        self.assertEqual(ht.size, 0)

    def testPythonDictInterface(self):
        ht = hashtable.HashTable(10)

        ht['a'] = 10
        self.assertEqual(ht.get('a'), 10)

        ht['a'] = 20
        self.assertEqual(ht['a'], 20)

        self.assertIn('a', ht.keys())

        del ht['a']
        self.assertRaises(KeyError, ht.get, 'a')

if __name__ == '__main__':
    unittest.main()

