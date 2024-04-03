class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(value, self.root)

    def _insert(self, value, node):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self._insert(value, node.left)
        else:
            node.right = self._insert(value, node.right)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)

        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)

        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_right(self, node):
        left_child = node.left
        right_grandchild = left_child.right

        left_child.right = node
        node.left = right_grandchild

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_child.height = 1 + max(self.get_height(left_child.left), self.get_height(left_child.right))

        return left_child

    def _rotate_left(self, node):
        right_child = node.right
        left_grandchild = right_child.left

        right_child.left = node
        node.right = left_grandchild

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_child.height = 1 + max(self.get_height(right_child.left), self.get_height(right_child.right))

        return right_child

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

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

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self._rotate_right(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self._rotate_left(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

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

avl = AVLTree()
avl.insert(5)
avl.insert(3)
avl.insert(7)
avl.insert(1)
avl.insert(4)
avl.insert(6)
avl.insert(8)

assert avl.root.value == 5
assert avl.root.left.value == 3
assert avl.root.right.value == 7
assert avl.root.left.left.value == 1
assert avl.root.left.right.value == 4
assert avl.root.right.left.value == 6
assert avl.root.right.right.value == 8

assert avl.search(3) is True
assert avl.search(10) is False

avl.delete(3)
assert avl.search(3) is False

assert avl.inorder_traversal() == [1, 4, 5, 6, 7, 8]

print("All tests passed!")

