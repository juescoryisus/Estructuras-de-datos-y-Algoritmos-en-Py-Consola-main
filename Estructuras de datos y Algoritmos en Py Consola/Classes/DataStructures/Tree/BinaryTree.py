from Classes.DataStructures.Nodes.BinaryNode import BinaryNode


class BinaryTree:
    def __init__(self):
        self.root = None

    def print_tree(self):
        tree_graph = self.generate_tree_graph()
        print(tree_graph)

    def generate_tree_graph(self):
        tree_graph = []
        self._generate_tree_graph(self.root, "", True, tree_graph)
        return "\n".join(tree_graph)

    def _generate_tree_graph(self, node, prefix, is_left, tree_graph):
        if node is not None:
            tree_graph.append(f"{prefix}{ '├── ' if is_left else '└── '}{node.data}")
            self._generate_tree_graph(node.left, prefix + ("│   " if is_left else "    "), True, tree_graph)
            self._generate_tree_graph(node.right, prefix + ("│   " if is_left else "    "), False, tree_graph)

    def add(self, value):
        self.root = self._add(self.root, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def search(self, value):
        return self._search(self.root, value)

    def pre_order(self):
        self._pre_order(self.root)
        print()

    def post_order(self):
        self._post_order(self.root)
        print()

    def in_order(self):
        self._in_order(self.root)
        print()

    def _add(self, node, value):
        if node is None:
            return BinaryNode(value)

        if value < node.data:
            node.left = self._add(node.left, value)
        elif value > node.data:
            node.right = self._add(node.right, value)
        return node

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.data:
            node.left = self._delete(node.left, value)
        elif value > node.data:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data = self.min_value(node.right)
            node.right = self._delete(node.right, node.data)
        return node

    def min_value(self, node):
        min_val = node.data
        while node.left is not None:
            min_val = node.left.data
            node = node.left
        return min_val

    def _search(self, node, value):
        if node is None:
            print(f"The value doesn't exist in the tree")
            return False

        if value == node.data:
            print(f"The value exists in the list")
            return True

        if value < node.data:
            return self._search(node.left, value)

        return self._search(node.right, value)

    def get_pre_order(self):
        result = []
        self._get_pre_order(self.root, result)
        return result

    def get_post_order(self):
        result = []
        self._get_post_order(self.root, result)
        return result

    def get_in_order(self):
        result = []
        self._get_in_order(self.root, result)
        return result

    def _get_pre_order(self, node, result):
        if node is not None:
            result.append(node.data)
            self._get_pre_order(node.left, result)
            self._get_pre_order(node.right, result)

    def _get_post_order(self, node, result):
        if node is not None:
            self._get_post_order(node.left, result)
            self._get_post_order(node.right, result)
            result.append(node.data)

    def _get_in_order(self, node, result):
        if node is not None:
            self._get_in_order(node.left, result)
            result.append(node.data)
            self._get_in_order(node.right, result)

    def _pre_order(self, tree):
        if tree is not None:
            print(tree.data, end=" ")
            self._pre_order(tree.left)
            self._pre_order(tree.right)

    def _post_order(self, tree):
        if tree is not None:
            self._post_order(tree.left)
            self._post_order(tree.right)
            print(tree.data, end=" ")

    def _in_order(self, tree):
        if tree is not None:
            self._in_order(tree.left)
            print(tree.data, end=" ")
            self._in_order(tree.right)
