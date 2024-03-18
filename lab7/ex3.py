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

        current_node.height = 1 + max(self._get_height(current_node.left),
                                      self._get_height(current_node.right))

        balance_factor = self._get_balance(current_node)

        #Case 1
        if balance_factor > 1 and key < current_node.left.key:
            print("Case 1 Complete - pivot not found")
            return self._right_rotate(current_node)
            
        #Case 2
        if balance_factor < -1 and key > current_node.right.key:
            print("\nCase 2 Complete - Pivot exists. The node was added to the shorter subtree\n")
            return self._left_rotate(current_node)

        #Case 3a
        if balance_factor > 1 and key > current_node.left.key:
            print("Case #3a Complete - adding a node to an outside subtree")
            current_node.left = self._left_rotate(current_node.left)
            return self._right_rotate(current_node)

        #Case 3b
        if balance_factor < -1 and key < current_node.right.key:
            print("\nCase #3b Complete - not supported")
            current_node.right = self._right_rotate(current_node.right)
            return self._left_rotate(current_node)

        return current_node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

def test_case(avl_tree, case):
    if case == 1:
        avl_tree.insert(30)
        avl_tree.insert(20)
        avl_tree.insert(10)
    elif case == 2:
        avl_tree.insert(10)
        avl_tree.insert(20)
        avl_tree.insert(30)
    elif case == 3:
        avl_tree.insert(30)
        avl_tree.insert(10)
        avl_tree.insert(20)
    elif case == 4:
        avl_tree.insert(10)
        avl_tree.insert(30)
        avl_tree.insert(20)

for i in range(1, 5):
    avl_tree = AVLTree()
    test_case(avl_tree, i)
