class TreeNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BSTDictionary(object):
    def __init__(self, root=None):
        self.root = root
        self.count = 0

    def add(self, key, value):
        self.root = self._add(self.root, key, value)
        self.count += 1

    def _add(self, node, key, value):
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

    def set(self, key, value):
        self.add(key, value)

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def remove(self, key):
        self.root, removed = self._remove(self.root, key)
        if removed:
            self.count -= 1
        return removed

    def _remove(self, node, key):
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

    def member(self, key):
        return self._member(self.root, key)

    def _member(self, node, key):
        if node is None:
            return False
        if str(key) == str(node.key):
            return node.value
        elif str(key) < str(node.key):
            return self._member(node.left, key)
        else:
            return self._member(node.right, key)

    def size(self):
        return self.count

    def from_dict(self, dictionary):
        for key, value in dictionary.items():
            self.add(key, value)

    def to_dict(self):
        result = {}
        self._to_dict(self.root, result)
        return result

    def _to_dict(self, node, result):
        if node is None:
            return
        self._to_dict(node.left, result)
        result[node.key] = node.value
        self._to_dict(node.right, result)

    def filter(self, f):
        filtered_dict = {}
        self._filter(self.root, filtered_dict, f)
        return filtered_dict

    def _filter(self, node, filtered_dict, f):
        if node is None:
            return
        self._filter(node.left, filtered_dict, f)
        if f(node.key):
            filtered_dict[node.key] = node.value
        self._filter(node.right, filtered_dict, f)

    def map(self, f):
        mapped_dict = {}
        self._map(self.root, mapped_dict, f)
        return mapped_dict

    def _map(self, node, mapped_dict, f):
        if node is None:
            return
        self._map(node.left, mapped_dict, f)
        mapped_key, mapped_value = f(node.key, node.value)
        mapped_dict[mapped_key] = mapped_value
        self._map(node.right, mapped_dict, f)

    def reduce(self, f, initial_state):
        def _reduce(node, state):
            if node is None:
                return state
            state = _reduce(node.left, state)
            state = f(node.key, node.value, state)
            return _reduce(node.right, state)

        return _reduce(self.root, initial_state)

    def __iter__(self):
        self.stack = []
        self._traverse_left(self.root)
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        self._traverse_left(node.right)
        return node.key, node.value

    def _traverse_left(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

    @staticmethod
    def empty():
        return BSTDictionary()

    def concat(self, dict2):
        result = BSTDictionary()
        result._concat(self.root, dict2.root)
        result.count = self.size() + dict2.size()
        return result

    def _concat(self, node1, node2):
        if node1:
            self.add(node1.key, node1.value)
            self._concat(node1.left, node1.right)
        if node2:
            self.add(node2.key, node2.value)
            self._concat(node2.left, node2.right)
