import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    if value < root.value:
        if root.left is not None:
            return contains(root.left, value)
        else:
            return False
    elif value > root.value:
        if root.right is not None:
            return contains(root.right, value)
        else:
            return False
    else:
        return True


n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
print(contains(n2, 3))
