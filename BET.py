import itertools


class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {"+", "-", "*", "/"}
    CARD_VAL_DICT = {
        "A": 1,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
    }

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None:
            return False
        return (
            self.value == other.value
            and self.left == other.left
            and self.right == other.right
        )

    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))

    # START HERE
    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right

    def evaluate(self):
        """Evaluate the node and return the result"""
        if self.value not in BETNode.OPERATORS:
            return BETNode.CARD_VAL_DICT.get(self.value)
        if self.value == "+":
            return self.left.evaluate() + self.right.evaluate()
        if self.value == "-":
            return self.left.evaluate() - self.right.evaluate()
        if self.value == "*":
            return self.left.evaluate() * self.right.evaluate()
        if self.value == "/":
            if self.right.evaluate() == 0:
                return 1000000000
            return self.left.evaluate() / self.right.evaluate()

        else:
            return self.CARD_VAL_DICT[self.value]

    # def postfix_to_infix(self, expression):
    #     """Convert a postfix expression to an infix expression"""
    #     stack = []
    #     operators = set(["+", "-", "*", "/"])
    #     # if integer, keep going, once operator: take previous two items and pop them out
    #     for char in expression.split(","):
    #         if char.strip() not in operators:
    #             stack.append(char.strip())
    #         else:
    #             operand_2 = stack.pop()
    #             operand_1 = stack.pop()
    #             # Add parentheses around the operands if they contain operators with lower precedence
    #             stack.append("({}{}{})".format(operand_1, char.strip(), operand_2))
    #             # stack.append(f"{operand_1}{char}{operand_2}")
    #     return stack.pop()

    def __repr__(self):

        if self.value not in BETNode.OPERATORS:
            return self.value
        return f"({repr(self.left)}{self.value}{repr(self.right)})"


def create_trees(cards):
    possible_tree_structures = {"CCXCCXX", "CCXCXCX", "CCCXXCX", "CCCXCXX", "CCCCXXX"}
    operators = {"+", "-", "*", "/"}
    operator_combinations = list(itertools.product(operators, repeat=3))
    card_combinations = list(itertools.permutations(cards))
    total_tree_combinations = set()
    for combo_cards in card_combinations:
        for combo_operators in operator_combinations:
            for possible_tree in possible_tree_structures:
                tree = ""
                cards_used = 0
                operators_used = 0
                for i in range(len(possible_tree)):
                    if possible_tree[i] == "C":
                        tree += combo_cards[cards_used] + ","
                        cards_used += 1
                    else:
                        tree += combo_operators[operators_used] + ","
                        operators_used += 1
                total_tree_combinations.add(tree)
    # print(total_tree_combinations)
    return total_tree_combinations
    # print(len(total_tree_combinations))


def find_solutions(cards):
    possible_trees = create_trees(cards)
    operators = ["+", "-", "*", "/"]
    result = set()
    # Create all trees
    count = 0
    for tree in possible_trees:
        # To handle card '10'
        tree_list = tree.split(",")
        root = BETNode(tree_list[6])
        root.add_right(BETNode(tree_list[5]))
        # Perfect Tree
        if tree[5] in operators and tree[2] in operators:
            root.add_left(BETNode(tree_list[2]))
            root.right.add_right(BETNode(tree_list[4]))
            root.right.add_left(BETNode(tree_list[3]))
            root.left.add_right(BETNode(tree_list[1]))
            root.left.add_left(BETNode(tree_list[0]))
        # Right weighted tree
        elif tree_list[5] in operators:
            root.right.add_right(BETNode(tree_list[4]))
            if tree_list[4] in operators:
                root.right.right.add_right(BETNode(tree_list[3]))
                root.right.right.add_left(BETNode(tree_list[2]))
                root.right.add_left(BETNode(tree_list[1]))
                root.add_left(BETNode(tree_list[0]))
            else:
                root.right.add_left(BETNode(tree_list[3]))
                root.right.left.add_right(BETNode(tree_list[2]))
                root.right.left.add_left(BETNode(tree_list[1]))
                root.add_left(BETNode(tree_list[0]))
        # Left weighted tree
        elif tree_list[5] not in operators:
            root.add_left(BETNode(tree_list[4]))
            root.left.add_right(BETNode(tree_list[3]))
            if tree_list[3] in operators:
                root.left.right.add_right(BETNode(tree_list[2]))
                root.left.right.add_left(BETNode(tree_list[1]))
                root.left.add_left(BETNode(tree_list[0]))
            else:
                root.left.add_left(BETNode(tree_list[2]))
                root.left.left.add_right(BETNode(tree_list[1]))
                root.left.left.add_left(BETNode(tree_list[0]))
        if root.evaluate() == 24:
            result.add(repr(root))
            if len(repr(root)) == len("(Q*(2*A))"):
                count += 1
                print(
                    tree_list[0],
                    tree_list[1],
                    tree_list[2],
                    tree_list[3],
                    tree_list[4],
                    tree_list[5],
                    tree_list[6],
                )
    print(count)
    print(len(result))


if __name__ == "__main__":
    cards = ["A", "2", "3", "Q"]
    find_solutions(cards)

# node = BETNode(3)

# # Call the postfix_to_infix() method with an expression argument
# expression = "1, 2, 3, 4, -, +, *"
# infix_expression = node.postfix_to_infix(expression)
# print(infix_expression)
