import unittest

from ..str.lab3_v2 import BinaryTree, post_order_traversal

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.left.left = BinaryTree(5)
root.left.right = BinaryTree(12)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

result = post_order_traversal(root)
expected_result = [5, 12, 9, 15, 7, 20, 3]

assert result == expected_result, f"Expected: {expected_result}, but got: {result}"
