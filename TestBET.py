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
        expected_str = -5
        self.assertEqual(root.evaluate(), expected_str)

    def test_evaluate_tree2(self):
        cards = ["A", "2", "3", "4"]
        result = find_solutions(cards)
        self.assertEqual(len(result), 7680)


class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        pass

    def test_hand2(self):
        pass


class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        pass

    def test_A23Q(self):
        pass


unittest.main()
