
class TreeNode:
    def __init__(self, node_value, parent_node=None, left_child=None, right_child=None):
        self.node_value = node_value
        self.parent_node = parent_node
        self.left_child = left_child
        self.right_child = right_child
        self.node_balance = 0

class BinarySearchTree:
    def __init__(self):
        self.root_node = None
        self.pivot_node = None

    def insert_node(self, node_value, setup_flag):
        current_node = self.root_node
        parent_node = None

        while current_node is not None:
            parent_node = current_node
            if node_value <= current_node.node_value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

        new_node = TreeNode(node_value, parent_node)
        if parent_node is None:
            self.root_node = new_node
        elif node_value <= parent_node.node_value:
            parent_node.left_child = new_node
        else:
            parent_node.right_child = new_node

        self.update_balances(new_node, setup_flag)
        return new_node

    def search_node(self, node_value):
        current_node = self.root_node
        while current_node is not None:
            if node_value == current_node.node_value:
                return current_node
            elif node_value <= current_node.node_value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return None

    def update_balances(self, inserted_node, setup_flag):
        self.pivot_node = None
        node_inserted = inserted_node
        parent_node = inserted_node.parent_node
        pivot_balance_value = 0

        while inserted_node != None:
            if inserted_node.node_balance >=1 or inserted_node.node_balance<=-1:
                if self.pivot_node is None:
                    self.pivot_node = inserted_node
                    pivot_balance_value = inserted_node.node_balance
            inserted_node.node_balance = self.calculate_balance(inserted_node)
            inserted_node = inserted_node.parent_node

        if self.pivot_node is None:
            if setup_flag == 0:
                print("Case 1 - No pivot found")
        else:
            if pivot_balance_value >=1:
                if node_inserted.node_value < self.pivot_node.node_value and setup_flag == 0:
                    print("Case 2 - Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.node_value > self.pivot_node.node_value and setup_flag == 0:
                    print("Case 3 - not supported")

            elif pivot_balance_value <=-1:
                if node_inserted.node_value > self.pivot_node.node_value and setup_flag == 0:
                    print("Case 2 - Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.node_value < self.pivot_node.node_value and setup_flag == 0:
                    print("Case 3 - not supported")

    def calculate_balance(self, tree_node):
        left_subtree_height = self.calculate_height(tree_node.left_child)
        right_subtree_height = self.calculate_height(tree_node.right_child)
        return right_subtree_height - left_subtree_height

    def calculate_height(self, tree_node):
        if tree_node is None:
            return 0

        node_queue = [tree_node]
        tree_height = 0

        while len(node_queue) > 0:
            queue_size = len(node_queue)

            for i in range(queue_size):
                current_node = node_queue.pop(0)

                if current_node.left_child:
                    node_queue.append(current_node.left_child)
                if current_node.right_child:
                    node_queue.append(current_node.right_child)
            tree_height += 1
        return tree_height

    def calculate_largest_balance(self):
        if self.root_node is None:
            return 0
        balance_list = []
        node_stack = [self.root_node]
        while len(node_stack) > 0:
            tree_node = node_stack.pop()
            balance_value = abs(tree_node.node_balance)
            balance_list.append(balance_value)

            if tree_node.right_child:
                node_stack.append(tree_node.right_child)
            if tree_node.left_child:
                node_stack.append(tree_node.left_child)

        max_balance_value = max(balance_list)
        return max_balance_value

bst = BinarySearchTree()
bst.insert_node(10, 1)
bst.insert_node(8, 1)
bst.insert_node(11, 1)
bst.insert_node(6, 0)


bst = BinarySearchTree()
bst.insert_node(10,1)
bst.insert_node(12,1)
bst.insert_node(13,1)
bst.insert_node(9,1)
bst.insert_node(8,0)

bst = BinarySearchTree()
bst.insert_node(8,1)
bst.insert_node(9,1)
bst.insert_node(10,1)
bst.insert_node(11,1)
bst.insert_node(12,0)