# GROUP-"I like studying" - lab 1 - variant 6

This is my lab1 of CPO class, implementation of mutable data structure dictionary
based on binary search tree(Variant6).

## Project structure

- `BSTDict.py` -- implementation of `BSTDictionary` class with features in `Features`.
- `BSTDict_test.py` -- unit and PBT test for `BSTDict`.

## Features

- Add element: `add(self, key, value)`
- Set element(setting value by key): `set(self, key, value)`
- Remove element: `def remove(self, key)`
- Size: `size(self)`
- Is member(getting value by key): `member(self, key)`
- From built-in dict: `from_dict(self, dictionary)`
- To built-in dict: `to_dict(self)`
- Filter dictionary: `filter(self, f)`
- Map dictionary: `map(self, f)`
- Reduce process elements: `def reduce(self, f, initial_state)`
- Iterator dictionary: `__iter__(self)` and `__next__(self)`
- Empty implementation: `empty()`
- Concat implementation: `concat(self, dict2)`

## Contribution

- AnYifei (645192770@qq.com) -- all work.

## Changelog

- 27.2.2024 - 4
   - The `concat` function modification.
   - Add static typing to the library.
   - Update `check.yml`: --strict in CI for mypy.
   - Update README.
- 20.4.2024 - 3
   - Add PBT tests for monoid.
   - Add code formatter to CI.
- 17.4.2024 - 2
   - Update README.
   - Add test coverage.
- 17.4.2024 - 1
   - Modification of part features.
   - Implementation of part features.
   - Unit tests
- 16.4.2024 - 0
   - Initialization.
   - Implementation of part features.

## Design notes

- Since my dictionary data struction mutable implementation is based on
  binary search tree, so this is an ordered dictionary. The keys of the
  dictionary correspond to the indices of the binary search tree. Keys
  are unique and can be integers, floating-point values, or strings.
  During the binary search tree traversal, the keys are converted to
  string values. The order of the elements in the dictionary is only
  related to the key and is fixed. When the items are added to the dictionary,
  they are automatically sorted by their key and added to the binary search
  tree. So the order of the items in the dictionary can't be changed.
  I think this is a feature of the implementation, and probably a restriction
- In my opinion, unit tests are easy to understand and write, and the
  execution time is fast. Relatively speaking, PBT is more complex and takes
  longer to execute. Unit tests can only test a single function or module in
  the code, can't cover the behavior of the entire system. And unit tests may
  miss some edge cases or exceptions. In contrast, PBT describes the system
  behavior based on attributes, and can generate a large number of random test
  cases, which can cover more code paths and boundary cases. In addition,
  PBT can automatically generate test cases, reducing the workload of manually
  writing test cases.
