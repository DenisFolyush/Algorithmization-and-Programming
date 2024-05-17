import unittest

from src.is_tree_balanced import TreeNode, is_tree_balanced


class TestTreeMethods(unittest.TestCase):

    def test_balanced_tree(self):
        root = TreeNode(48)
        root.left = TreeNode(20)
        root.left.left = TreeNode(18)
        root.left.right = TreeNode(25)
        root.left.left.left = TreeNode(11)
        root.left.left.right = TreeNode(19)
        root.right = TreeNode(50)
        root.right.left = TreeNode(49)
        root.right.right = TreeNode(55)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = TreeNode(48)
        root.left = TreeNode(20)
        root.left.left = TreeNode(18)
        root.left.left.left = TreeNode(11)
        root.left.left.left.left = TreeNode(10)  # Making it unbalanced
        root.right = TreeNode(50)
        self.assertFalse(is_tree_balanced(root))

    def test_balanced_tree_with_one_argument(self):
        root = TreeNode(0)
        self.assertTrue(is_tree_balanced(root))


if __name__ == '__main__':
    unittest.main()
