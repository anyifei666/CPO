from typing import Optional, Tuple, Dict, Callable, Iterator, List, Union, Any

Keytype = Union[int, float, str]
Valuetype = Union[int, float, str, None]


class TreeNode(object):
    def __init__(self, key: Keytype, value: Valuetype) -> None:
        self.key: Keytype = key
        self.value: Valuetype = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BSTDictionary(object):
    def __init__(self, root: Optional[TreeNode] = None):
        self.root: Optional[TreeNode] = root
        self.count: int = 0

    def add(self, key: Keytype, value: Valuetype) -> None:
        self.root = self._add(self.root, key, value)
        self.count += 1

    def _add(self, node: Optional[TreeNode],
             key: Keytype, value: Valuetype) -> TreeNode:
        if key is None:
            raise ValueError("Key cannot be None")
        if node is None:
            return TreeNode(key, value)
        if str(key) < str(node.key):
            node.left = self._add(node.left, key, value)
        elif str(key) > str(node.key):
            node.right = self._add(node.right, key, value)
        else:  # key already exists, update value
            node.value = value
        return node

    def set(self, key: Keytype, value: Valuetype) -> None:
        self.add(key, value)

    def _find_min(self, node: Optional[TreeNode]) -> TreeNode:
        while node and node.left:
            node = node.left
        assert node is not None
        return node

    def remove(self, key: Keytype) -> bool:
        self.root, removed = self._remove(self.root, key)
        if removed:
            self.count -= 1
        return removed

    def _remove(self, node: Optional[TreeNode], key: Keytype) \
            -> Tuple[Optional[TreeNode], bool]:
        if node is None:
            return None, False
        if str(key) < str(node.key):
            node.left, removed = self._remove(node.left, key)
        elif str(key) > str(node.key):
            node.right, removed = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                successor = self._find_min(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right, _ = self._remove(node.right, successor.key)
                removed = True
        return node, removed

    def member(self, key: Keytype) -> Valuetype:
        return self._member(self.root, key)

    def _member(self, node: Optional[TreeNode], key: Keytype) -> Valuetype:
        if node is None:
            return False
        if str(key) == str(node.key):
            return node.value
        elif str(key) < str(node.key):
            return self._member(node.left, key)
        else:
            return self._member(node.right, key)

    def size(self) -> int:
        return self.count

    def from_dict(self, dictionary: Dict[Keytype, Valuetype]) -> None:
        for key, value in dictionary.items():
            self.add(key, value)

    def to_dict(self) -> Dict[Keytype, Valuetype]:
        result: Dict[Keytype, Valuetype] = {}
        self._to_dict(self.root, result)
        return result

    def _to_dict(self, node: Optional[TreeNode],
                 result: Dict[Keytype, Valuetype]) -> None:
        if node is None:
            return
        self._to_dict(node.left, result)
        result[node.key] = node.value
        self._to_dict(node.right, result)

    def filter(self, f: Callable[[Keytype], bool]) -> Dict[Keytype, Valuetype]:
        filtered_dict: Dict[Keytype, Valuetype] = {}
        self._filter(self.root, filtered_dict, f)
        return filtered_dict

    def _filter(self, node: Optional[TreeNode],
                filtered_dict: Dict[Keytype, Valuetype],
                f: Callable[[Keytype], bool]) -> None:
        if node is None:
            return
        self._filter(node.left, filtered_dict, f)
        if f(node.key):
            filtered_dict[node.key] = node.value
        self._filter(node.right, filtered_dict, f)

    def map(self, f: Callable[[Any, Any], Tuple[Keytype, Valuetype]])\
            -> Dict[Keytype, Valuetype]:
        mapped_dict: Dict[Keytype, Valuetype] = {}
        self._map(self.root, mapped_dict, f)
        return mapped_dict

    def _map(self, node: Optional[TreeNode],
             mapped_dict: Dict[Keytype, Valuetype],
             f: Callable[[Keytype, Valuetype],
             Tuple[Keytype, Valuetype]]) -> None:
        if node is None:
            return
        self._map(node.left, mapped_dict, f)
        mapped_key, mapped_value = f(node.key, node.value)
        mapped_dict[mapped_key] = mapped_value
        self._map(node.right, mapped_dict, f)

    def reduce(self, f: Callable[[Any, Any, int], int],
               initial_state: int) -> int:
        def _reduce(node: Optional[TreeNode], state: int) -> int:
            if node is None:
                return state
            state = _reduce(node.left, state)
            state = f(node.key, node.value, state)
            return _reduce(node.right, state)

        return _reduce(self.root, initial_state)

    def __iter__(self) -> Iterator[Tuple[Keytype, Valuetype]]:
        self.stack: List[TreeNode] = []
        self._traverse_left(self.root)
        return self

    def __next__(self) -> Tuple[Keytype, Valuetype]:
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        self._traverse_left(node.right)
        return node.key, node.value

    def _traverse_left(self, node: Optional[TreeNode]) -> None:
        while node is not None:
            self.stack.append(node)
            node = node.left

    # I think concat is already a mutable implementation. Maybe?
    def concat(self, dict2: 'BSTDictionary') -> 'BSTDictionary':
        if dict2.root:
            self._concat(self.root, dict2.root)
            self.count = self.size() + dict2.size()
        return self

    def _concat(self,
                node1: Optional[TreeNode],
                node2: Optional[TreeNode]) -> None:
        if node2 is not None:
            self.add(node2.key, node2.value)
            self._concat(node1, node2.left)
            self._concat(node1, node2.right)

    @staticmethod
    def empty() -> 'BSTDictionary':
        return BSTDictionary()
