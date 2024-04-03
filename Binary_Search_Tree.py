class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left:
                self._insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(value, node.right)
            else:
                node.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _delete(self, value, node):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            node.value = self._min_value(node.right)
            node.right = self._delete(node.value, node.right)
        return node

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node.value

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(8)

assert bst.search(3) is True
assert bst.search(10) is False

bst.delete(3)
assert bst.search(3) is False

assert bst.inorder_traversal() == [1, 4, 5, 6, 7, 8]

print("All tests passed!")

