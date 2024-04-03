class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            self.root.color = 'black'
        else:
            self._insert(new_node, self.root)

    def _insert(self, node, root):
        if node.value < root.value:
            if root.left:
                self._insert(node, root.left)
            else:
                root.left = node
                node.parent = root
                self._fix_insert(node)
        else:
            if root.right:
                self._insert(node, root.right)
            else:
                root.right = node
                node.parent = root
                self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_left(node.parent.parent)
        self.root.color = 'black'

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

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
    def inorder_traversal_with_colors(self):
        self._inorder_traversal_with_colors(self.root)

    def _inorder_traversal_with_colors(self, node):
        if node:
            self._inorder_traversal_with_colors(node.left)
            print("Value:", node.value, "Color:", node.color)
            self._inorder_traversal_with_colors(node.right)

rbt = RedBlackTree()
rbt.insert(5)
rbt.insert(3)
rbt.insert(7)
rbt.insert(1)
rbt.insert(4)
rbt.insert(6)
rbt.insert(8)

assert rbt.root.color == 'black'

def check_consecutive_red_nodes(node):
    if not node:
        return
    if node.color == 'red':
        left_color = node.left.color if node.left else 'black'
        right_color = node.right.color if node.right else 'black'
        assert left_color != 'red' and right_color != 'red'
    check_consecutive_red_nodes(node.left)
    check_consecutive_red_nodes(node.right)

def check_black_height(node, black_height, current_height):
    if not node:
        if black_height == -1:
            black_height = current_height
        else:
            assert black_height == current_height
        return
    if node.color == 'black':
        current_height += 1
    check_black_height(node.left, black_height, current_height)
    check_black_height(node.right, black_height, current_height)

check_black_height(rbt.root, -1, 0)

rbt.inorder_traversal_with_colors()

print("All tests passed!")

