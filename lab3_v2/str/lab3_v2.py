class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def depth(node: TreeNode, d: int) -> int:
    if node is None:
        return 0
    return d + depth(node.left, d + 1) + depth(node.right, d + 1)

def sum_of_depths(root: TreeNode) -> int:
    if root is None:
        return 0
    return depth(root, 0) + sum_of_depths(root.left) + sum_of_depths(root.right)

# Тестовий приклад:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sum_of_depths(root))  # Повинно вивести 4
