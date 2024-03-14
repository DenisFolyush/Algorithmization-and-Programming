from ..str.lab3_v2 import TreeNode, is_tree_balanced

import unittest

class TestBinaryTree(unittest.TestCase):
    def test_is_tree_balanced(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertFalse(is_tree_balanced(root))

if __name__ == '__main__':
    unittest.main()