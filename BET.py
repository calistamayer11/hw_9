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

    def evaluate(self, postfix):
        """Evaluate the node and return the result"""
        if self.value in BETNode.OPERATORS:
            return self.value
        if self.value == "+":
            return self.left.evaluate(postfix) + self.right.evaluate(postfix)
        if self.value == "-":
            return self.left.evaluate(postfix) - self.right.evaluate(postfix)
        if self.value == "*":
            return self.left.evaluate(postfix) * self.right.evaluate(postfix)
        if self.value == "/":
            return self.left.evaluate(postfix) / self.right.evaluate(postfix)

        else:
            return self.CARD_VAL_DICT[self.value]

        # if self.value == "=":
        #     return self.left.evaluate(postfix) == self.right.evaluate(postfix)

        # for item in postfix:
        #     if isinstance(self.CARD_VAL_DICT[item], int):
        #         pass
        #     if self.CARD_VAL_DICT[item] == "=":
        #         pass
        #     if self.CARD_VAL_DICT[item] == "+":
        #         pass
        #     if self.CARD_VAL_DICT[item] == "-":
        #         pass
        #     if self.CARD_VAL_DICT[item] == "*":
        #         pass
        #     if self.CARD_VAL_DICT[item] == "/":
        #         pass

    def postfix_to_infix(self, postfix):
        """Convert a postfix expression to an infix expression"""
        stack = []
        for item in postfix:
            # if integer, keep going, once operator: take previous two items and pop them out
            pass

    def __repr__(self):
        return f"{self.value} {self.left} {self.right}"


def create_trees():
    pass


def find_solutions():
    pass
