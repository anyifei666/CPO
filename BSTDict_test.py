import unittest
from hypothesis import given, strategies

from BSTDict import *


class TestBSTDict(unittest.TestCase):

    def test_add(self):
        mydict = BSTDictionary()
        mydict.add(3, 4)
        mydict.add(1, 2)
        mydict.add(2, 3)
        mydict.add(4, 5)
        mydict.add(5, 6)
        self.assertEqual(mydict.to_dict(), {1: 2, 2: 3, 3: 4, 4: 5, 5: 6})

    def test_set(self):
        mydict = BSTDictionary()
        mydict.add(3, 4)
        mydict.add(1, 2)
        mydict.add(2, 3)
        mydict.add(4, 5)
        mydict.add(5, 6)
        mydict.set(1, 4)
        self.assertEqual(mydict.to_dict(), {1: 4, 2: 3, 3: 4, 4: 5, 5: 6})

    def test_remove(self):
        mydict = BSTDictionary()
        mydict.add(1, 2)
        mydict.add(2, 3)
        mydict.add(3, 4)
        mydict.add(4, 5)
        mydict.add(5, 6)
        self.assertEqual(mydict.to_dict(), {1: 2, 2: 3, 3: 4, 4: 5, 5: 6})
        mydict.remove(3)
        self.assertEqual(mydict.to_dict(), {1: 2, 2: 3, 4: 5, 5: 6})

    def test_member(self):
        mydict = BSTDictionary()
        mydict.add(3, 4)
        mydict.add(1, 2)
        mydict.add(2, 3)
        mydict.add(4, 5)
        mydict.add(5, 6)
        self.assertEqual(mydict.member(3), 4)
        self.assertEqual(mydict.member(5), 6)
        self.assertEqual(mydict.member(6), False)

    def test_size(self):
        mydict = BSTDictionary()
        mydict.add(3, 4)
        mydict.add(1, 2)
        self.assertEqual(mydict.size(), 2)
        mydict.add(2, 3)
        mydict.add(4, 5)
        mydict.add(5, 6)
        self.assertEqual(mydict.size(), 5)

    def test_from_to_dict(self):
        mydict = BSTDictionary()
        mydict.from_dict({1: 2, 2: 3, 3: 4, 4: 5, 5: 6})
        self.assertEqual(mydict.to_dict(), {1: 2, 2: 3, 3: 4, 4: 5, 5: 6})