import unittest
from BET import BETNode, create_trees, find_solutions


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4

        """
        root = BETNode("*")
        root.add_left(BETNode("A"))
        root.add_right(BETNode("-"))
        root.right.add_left(BETNode("2"))
        root.right.add_right(BETNode("+"))
        root.right.right.add_left(BETNode("3"))
        root.right.right.add_right(BETNode("4"))
        expected_str = "(A*(2-(3+4)))"
        self.assertEqual(repr(root), expected_str)

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self):
        r"""String representation
               ___+___
              /       \
             *         -
            / \       / \
           3   +     10  K
              / \
             2   Q
        """
        root = BETNode("+")
        root.add_left(BETNode("*"))
        root.add_right(BETNode("-"))
        if root.right is not None and root.left is not None:
            root.left.add_left(BETNode("3"))
            root.left.add_right(BETNode("+"))
            root.right.add_left(BETNode("10"))
            root.right.add_right(BETNode("K"))
            root.left.right.add_left(BETNode("2"))
            root.left.right.add_right(BETNode("Q"))
        expected_evaluation = 39
        self.assertEqual(root.evaluate(), expected_evaluation)

    def test_evaluate_tree2(self):
        r"""String representation
               ___*___
              /       \
             -         /
            / \       / \
           *   9     10  2
          / \
         2   Q
        """
        root = BETNode("*")
        root.add_left(BETNode("-"))
        root.add_right(BETNode("/"))
        if root.right is not None and root.left is not None:
            root.left.add_left(BETNode("*"))
            root.left.add_right(BETNode("9"))
            root.right.add_left(BETNode("10"))
            root.right.add_right(BETNode("2"))
            root.left.left.add_left(BETNode("2"))
            root.left.left.add_right(BETNode("Q"))
        expected_evaluation = 75
        self.assertEqual(root.evaluate(), expected_evaluation)


class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        cards = ["A", "2", "3", "Q"]
        self.assertEqual(len(create_trees(cards)), 7680)

    def test_hand2(self):
        cards = ["A", "A", "3", "Q"]
        self.assertEqual(len(create_trees(cards)), 3840)


class TestFindSolutions(unittest.TestCase):
    """tests for when there are 0 solutions"""

    def test0sols(self):
        cards = ["A", "A", "A", "A"]
        self.assertEqual(len(find_solutions(cards)), 0)

    def test_A23Q(self):
        """should be 33 solutions"""
        cards = ["A", "2", "3", "Q"]
        self.assertEqual(len(find_solutions(cards)), 33)


unittest.main()
