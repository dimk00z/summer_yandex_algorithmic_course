class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    def get_branches(self, root):
        result = []
        if root:
            result = self.get_branches(root.left)
            result = result+self.get_branches(root.right)
            if (root.left is not None and root.right is None) or \
               (root.left is None and root.right is not None):
                result.append(root.data)
        return result

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def get_node_from_tree(self, node, data, depth=0):
        depth += 1
        if not data:
            return None
        if data == node.data:
            return node, depth
        if data < node.data:
            if node.left:
                return self.get_node_from_tree(node.left, data, depth)
        if data > node.data:
            if node.right:
                return self.get_node_from_tree(node.right, data, depth)

    def __str__(self):
        return str(self.data)


def max_depth(node):

    if node is None:
        return 0
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)

    if left_depth > right_depth:
        return left_depth+1
    else:
        return right_depth+1


with open('input.txt') as file:
    nodes = tuple(map(int, file.readlines()[0].split()))
root = Node(nodes[0])
result = []
for node in nodes[1:-1]:
    root.insert(node)


with open('output.txt', 'w') as file:
    file.write('\n'.join(tuple(map(str, sorted(root.get_branches(root))))))
