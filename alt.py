class BinaryTree:
    SENTINEL = object()  # Unique value.

    def __init__(self):
        self.head = Node(self.SENTINEL)

    def insert(self, data):
        try:
            self.head.attach(data)
        except TypeError:
            if self.head.data is self.SENTINEL:  # Empty tree?
                self.head.data = data  # First is special case.
            else:
                raise

    def print(self):
        self.head.print()
        print()


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def attach(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.attach(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.attach(data)

    def print(self):
        if self.left:
            self.left.print()
        print(self.data, end=' ')
        if self.right:
            self.right.print()


if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(19)
    tree.insert(5)
    tree.insert(3)

    tree.print()  # -> 2 4 6