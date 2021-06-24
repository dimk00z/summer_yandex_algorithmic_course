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

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

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
for node in nodes[1:-1]:
    root.insert(node)
# print(max_depth(root))

with open('output.txt', 'w') as file:
    file.write(str(max_depth(root)))
