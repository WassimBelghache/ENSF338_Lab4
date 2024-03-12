class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if not current_node:
            return TreeNode(key)

        if key < current_node.key:
            current_node.left = self._insert_recursive(current_node.left, key)
        else:
            current_node.right = self._insert_recursive(current_node.right, key)

        current_node.height = 1 + max(self._get_height(current_node.left), self._get_height(current_node.right))
        balance_factor = self._get_balance(current_node)

        if balance_factor > 1 and key < current_node.left.key:
            return self._right_rotate(current_node)

        if balance_factor < -1 and key > current_node.right.key:
            return self._left_rotate(current_node)

        if balance_factor > 1 and key > current_node.left.key:
            current_node.left = self._left_rotate(current_node.left)
            return self._right_rotate(current_node)

        if balance_factor < -1 and key < current_node.right.key:
            current_node.right = self._right_rotate(current_node.right)
            return self._left_rotate(current_node)

        return current_node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

def test_cases():
    avl_tree = AVLTree()
    avl_tree.insert(20)
    avl_tree.insert(4)
    avl_tree.insert(26)
    print("Test Case 1: Pivot not detected")

    avl_tree = AVLTree()
    avl_tree.insert(20)
    avl_tree.insert(4)
    avl_tree.insert(15)
    print("Test Case 2: Pivot exists, node added to the shorter subtree")

    avl_tree = AVLTree()
    avl_tree.insert(30)
    avl_tree.insert(10)
    avl_tree.insert(20)
    print("Test Case 3a: Left-Right rotation completed")

    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(30)
    avl_tree.insert(20)
    print("Test Case 3b: Right-Left rotation completed")

    avl_tree = AVLTree()
    avl_tree.insert(40)
    avl_tree.insert(20)
    avl_tree.insert(30)
    print("Additional Test Case for 3b: Right-Left rotation completed")

    avl_tree = AVLTree()
    avl_tree.insert(20)
    avl_tree.insert(40)
    avl_tree.insert(30)
    print("Additional Test Case for 3b: Right-Left rotation completed")

test_cases()