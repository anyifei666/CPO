import unittest
from hypothesis import given, strategies as st
from BSTDict import BSTDictionary


class TestBSTDict(unittest.TestCase):

    def test_add(self):
        # Test adding key-value pairs
        mydict = BSTDictionary()
        mydict.add('Name', 'AnYifei')
        mydict.add('LabWork', 1)
        mydict.add('Variant', 6)
        mydict.add('GroupName', 'I LIKE STUDYING')
        self.assertEqual(mydict.to_dict(),
                         {
                             'GroupName': 'I LIKE STUDYING',
                             'LabWork': 1,
                             'Name': 'AnYifei',
                             'Variant': 6})
        # Test the implementation correctly works with None value:
        with self.assertRaises(ValueError):
            mydict.add(None, '123')

    def test_set(self):
        # Test set feature
        mydict = BSTDictionary()
        mydict.add('Name', 'AnYifei')
        mydict.add('LabWork', 1)
        mydict.add('Variant', 6)
        mydict.add('GroupName',
                   'I LIKE STUDYING')
        mydict.set('GroupName',
                   'I DONT LIKE STUDYING')
        self.assertEqual(mydict.to_dict(),
                         {
                             'GroupName': 'I DONT LIKE STUDYING',
                             'LabWork': 1,
                             'Name': 'AnYifei',
                             'Variant': 6})

    def test_remove(self):
        # test remove and size features
        mydict = BSTDictionary()
        mydict.add('Name', 'AnYifei')
        mydict.add('LabWork', 1)
        mydict.add('Variant', 6)
        mydict.add('GroupName', 'I LIKE STUDYING')
        self.assertEqual(mydict.size(), 4)
        self.assertEqual(mydict.remove('GroupName'), True)
        self.assertEqual(mydict.size(), 3)
        self.assertEqual(mydict.remove('GroupName'), False)
        self.assertEqual(mydict.size(), 3)
        self.assertEqual(mydict.to_dict(), {'LabWork': 1,
                                            'Name': 'AnYifei',
                                            'Variant': 6})

    def test_member(self):
        mydict = BSTDictionary()
        mydict.add('Name', 'AnYifei')
        mydict.add('LabWork', 1)
        mydict.add('Variant', 6)
        mydict.add('GroupName', 'I LIKE STUDYING')
        self.assertEqual(mydict.member('Name'), 'AnYifei')
        self.assertEqual(mydict.member('LabWork'), 1)
        self.assertEqual(mydict.member('Variant'), 6)
        self.assertEqual(mydict.member('GroupName'), 'I LIKE STUDYING')
        self.assertEqual(mydict.member(1), False)
        self.assertEqual(mydict.member(None), False)

    def test_size(self):
        mydict = BSTDictionary()
        mydict.add('Name', 'AnYifei')
        self.assertEqual(mydict.size(), 1)
        mydict.add('LabWork', 1)
        self.assertEqual(mydict.size(), 2)
        mydict.add('Variant', 6)
        self.assertEqual(mydict.size(), 3)

    def test_from_dict(self):
        mydict = BSTDictionary()
        mydict.from_dict({1: 'Value1', 'Pi': 3.14, 4: None, '5': 6})
        self.assertEqual(mydict.size(), 4)
        self.assertEqual(mydict.member(1), 'Value1')
        self.assertEqual(mydict.member('Pi'), 3.14)
        self.assertEqual(mydict.member(4), None)
        self.assertEqual(mydict.member('5'), 6)
        self.assertEqual(mydict.member(2), False)

    def test_to_dict(self):
        mydict = BSTDictionary()
        mydict.add(1, 'Value1')
        mydict.add('Pi', 3.14)
        mydict.add(4, None)
        mydict.add('5', 6)
        self.assertEqual(mydict.to_dict(),
                         {1: 'Value1', 4: None, '5': 6, 'Pi': 3.14, })

    def test_filter(self):
        mydict = BSTDictionary()
        mydict.from_dict({1: 1, 2: 'a', 'b': 3, '4': 4, 5: None})
        self.assertEqual(mydict.filter(lambda key: isinstance(key, int)),
                         {1: 1, 2: 'a', 5: None})

    def test_map(self):
        mydict = BSTDictionary()
        mydict.from_dict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
        self.assertEqual(mydict.map(lambda key, value:
                                    (str(key), str(value))),
                         {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5'})
        mydict.from_dict({'1': 1, '2': 2, '3': 3, '4': 4, '5': 5})
        self.assertEqual(mydict.map(lambda key, value:
                                    (int(key), value * key)),
                         {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})

    def test_reduce(self):
        mydict = BSTDictionary()
        mydict.from_dict({})
        self.assertEqual(mydict.reduce(lambda key, value, st:
                                       st + key + value, 0), 0)
        mydict.from_dict({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
        self.assertEqual(mydict.reduce(lambda key, value, st:
                                       st + key, 0), 10)
        test_data = [
            {},
            {'a': '1', 'b': '2'},
            {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
        ]
        for e in test_data:
            mydict = BSTDictionary()
            mydict.from_dict(e)
            self.assertEqual(mydict.reduce(lambda key, value, st:
                                           st + 1, 0), mydict.size())

    @given(st.dictionaries(st.text(), st.text()))
    def test_from_dict_to_dict_equality(self, a):
        mydict = BSTDictionary()
        mydict.from_dict(a)
        b = mydict.to_dict()
        self.assertEqual(a, b)

    @given(st.dictionaries(st.text(), st.text()))
    def test_python_len_and_mydict_size_inequality(self, a):
        mydict = BSTDictionary()
        mydict.from_dict(a)
        self.assertEqual(mydict.size(), len(a))

    def test_iter(self):
        data = {2: 'b', 1: 'a', 4: 'd', 3: 'c'}
        mydict = BSTDictionary()
        mydict.from_dict(data)

        keys_in_order = sorted(data.keys())

        tmp_keys = []
        tmp_values = []
        for key, value in mydict:
            tmp_keys.append(key)
            tmp_values.append(value)
        self.assertEqual(keys_in_order, tmp_keys)
        self.assertEqual([data[key] for key in keys_in_order], tmp_values)

        self.assertEqual(data, mydict.to_dict())

        empty_dict = BSTDictionary()
        self.assertRaises(StopIteration, lambda: next(iter(empty_dict)))

    def test_empty(self):
        empty_dict = BSTDictionary().empty()
        self.assertEqual(empty_dict.size(), 0)

    def test_concat(self):
        dict1 = BSTDictionary()
        dict1.from_dict({"a": 1, "b": 2, "c": 3})
        dict2 = BSTDictionary()
        dict2.from_dict({"c": 3, "d": 4, "e": 5})
        concat_dict = dict1.concat(dict2)
        self.assertEqual(concat_dict.to_dict(),
                         {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
