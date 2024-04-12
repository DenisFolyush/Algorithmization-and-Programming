class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def is_tree_balanced(node):
    if node is None:
        return True

    bf = balance_factor(node)

    if abs(bf) <= 1 and is_tree_balanced(node.left) and is_tree_balanced(node.right):
        return True

    return False
