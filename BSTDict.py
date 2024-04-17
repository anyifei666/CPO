class TreeNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BSTDictionary(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def add(self, key, value):
        self.root = self._add(self.root, key, value)
        self.count += 1

    def _add(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
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

    def _remove(self, node, key):
        if node is None:
            return None, False
        if key < node.key:
            node.left, removed = self._remove(node.left, key)
        elif key > node.key:
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
        if key == node.key:
            return node.value
        elif key < node.key:
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

    # def filter(self, filter_func):
    #     filtered_dict = {}
    #     self._filter(self.root, filtered_dict, filter_func)
    #     return filtered_dict
    #
    # def _filter(self, node, filtered_dict, filter_func):
    #     if node is None:
    #         return
    #     self._filter(node.left, filtered_dict, filter_func)
    #     if filter_func(node.key):
    #         filtered_dict[node.key] = node.value
    #     self._filter(node.right, filtered_dict, filter_func)
