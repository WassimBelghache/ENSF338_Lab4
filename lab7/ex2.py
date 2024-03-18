class TreeNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.balance = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.pivot = None

    def insert(self, value, setup_flag):
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if value <= current.value:
                current = current.left
            else:
                current = current.right

        new_node = TreeNode(value, parent)
        if parent is None:
            self.root = new_node
        elif value <= parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self.update_balances(new_node, setup_flag)
        return new_node

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value <= current.value:
                current = current.left
            else:
                current = current.right
        return None

    def update_balances(self, inserted_node, setup_flag):
        self.pivot = None
        node_inserted = inserted_node
        parent = inserted_node.parent
        pivot_balance_value = 0

        while inserted_node is not None:
            if inserted_node.balance >= 1 or inserted_node.balance <= -1:
                if self.pivot is None:
                    self.pivot = inserted_node
                    pivot_balance_value = inserted_node.balance
            inserted_node.balance = self.calculate_balance(inserted_node)
            inserted_node = inserted_node.parent

        if self.pivot is None:
            if setup_flag == 0:
                print("Case 1 - No pivot found")
        else:
            if pivot_balance_value >= 1:
                if node_inserted.value < self.pivot.value and setup_flag == 0:
                    print("Case 2 - Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.value > self.pivot.value and setup_flag == 0:
                    print("Case 3 - not supported")

            elif pivot_balance_value <= -1:
                if node_inserted.value > self.pivot.value and setup_flag == 0:
                    print("Case 2 - Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.value < self.pivot.value and setup_flag == 0:
                    print("Case 3 - not supported")

    def calculate_balance(self, node):
        left_subtree_height = self.calculate_height(node.left)
        right_subtree_height = self.calculate_height(node.right)
        return right_subtree_height - left_subtree_height

    def calculate_height(self, node):
        if node is None:
            return 0

        node_queue = [node]
        tree_height = 0

        while len(node_queue) > 0:
            queue_size = len(node_queue)

            for i in range(queue_size):
                current = node_queue.pop(0)

                if current.left:
                    node_queue.append(current.left)
                if current.right:
                    node_queue.append(current.right)
            tree_height += 1
        return tree_height

    def calculate_largest_balance(self):
        if self.root is None:
            return 0
        balance_list = []
        node_stack = [self.root]
        while len(node_stack) > 0:
            node = node_stack.pop()
            balance_value = abs(node.balance)
            balance_list.append(balance_value)

            if node.right:
                node_stack.append(node.right)
            if node.left:
                node_stack.append(node.left)

        max_balance_value = max(balance_list)
        return max_balance_value

BST = BinarySearchTree()
BST.insert(10, 1)
BST.insert(8, 1)
BST.insert(11, 1)
BST.insert(6, 0)


BST = BinarySearchTree()
BST.insert(10,1)
BST.insert(12,1)
BST.insert(13,1)
BST.insert(9,1)
BST.insert(8,0)

BST = BinarySearchTree()
BST.insert(8,1)
BST.insert(9,1)
BST.insert(10,1)
BST.insert(11,1)
BST.insert(12,0)
