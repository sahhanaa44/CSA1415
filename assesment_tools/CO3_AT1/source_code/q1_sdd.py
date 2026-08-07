# Q1 - Syntax Directed Definition (SDD)
# Arithmetic Expression Evaluation
# Synthesized Attributes + Syntax Tree + Bottom-Up Evaluation

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.result = None


# ============================================================
# DISPLAY SDD RULES
# ============================================================

def display_sdd():

    print("\n" + "=" * 65)
    print("SYNTAX-DIRECTED DEFINITION (SDD)")
    print("=" * 65)

    print("""
E → E + T       { E.val = E1.val + T.val }
E → E - T       { E.val = E1.val - T.val }
E → T           { E.val = T.val }

T → T * F       { T.val = T1.val * F.val }
T → T / F       { T.val = T1.val / F.val }
T → F           { T.val = F.val }

F → (E)         { F.val = E.val }
F → number      { F.val = number.lexval }
""")


# ============================================================
# DISPLAY ATTRIBUTE EXPLANATION
# ============================================================

def display_attribute_explanation():

    print("=" * 65)
    print("SYNTHESIZED ATTRIBUTES")
    print("=" * 65)

    print("""
These are synthesized attributes because the value of a parent
node is calculated from the values of its children.

For example:

        E
       /|\\
      E + T

The value of E is calculated using the values of E and T:

        E.val = E1.val + T.val

Therefore, information flows from the children toward the parent.
This produces a bottom-up evaluation.
""")


# ============================================================
# TOKENIZER
# ============================================================

def tokenize(expression):

    tokens = []
    i = 0

    while i < len(expression):

        if expression[i].isspace():
            i += 1
            continue

        if expression[i].isdigit():

            number = ""

            while i < len(expression) and expression[i].isdigit():
                number += expression[i]
                i += 1

            tokens.append(("NUMBER", int(number)))
            continue

        if expression[i] in "+-*/()":
            tokens.append((expression[i], expression[i]))
            i += 1
            continue

        raise ValueError(
            "Invalid character: " + expression[i]
        )

    tokens.append(("EOF", "EOF"))

    return tokens


# ============================================================
# PARSER
#
# E → T ((+|-) T)*
# T → F ((*|/) F)*
# F → (E) | number
#
# This grammar automatically gives:
#
# * and / higher precedence than + and -
# ============================================================

class Parser:

    def __init__(self, tokens):

        self.tokens = tokens
        self.position = 0

    def current(self):

        return self.tokens[self.position]

    def eat(self, token_type):

        if self.current()[0] == token_type:

            value = self.current()[1]

            self.position += 1

            return value

        raise ValueError(
            "Expected " + token_type +
            " but found " + str(self.current()[1])
        )

    def parse(self):

        node = self.expression()

        if self.current()[0] != "EOF":
            raise ValueError("Invalid expression")

        return node

    # E → T ((+|-) T)*
    def expression(self):

        left = self.term()

        while self.current()[0] in ("+", "-"):

            operator = self.current()[0]

            self.eat(operator)

            right = self.term()

            left = Node(operator, left, right)

        return left

    # T → F ((*|/) F)*
    def term(self):

        left = self.factor()

        while self.current()[0] in ("*", "/"):

            operator = self.current()[0]

            self.eat(operator)

            right = self.factor()

            left = Node(operator, left, right)

        return left

    # F → (E) | number
    def factor(self):

        if self.current()[0] == "NUMBER":

            number = self.eat("NUMBER")

            return Node(str(number))

        if self.current()[0] == "(":

            self.eat("(")

            node = self.expression()

            self.eat(")")

            return node

        raise ValueError("Expected number or '('")


# ============================================================
# BOTTOM-UP SDD EVALUATION
# ============================================================

def evaluate(node):

    # Leaf node
    if node.left is None and node.right is None:

        node.result = int(node.value)

        return node.result

    # First evaluate children
    left_value = evaluate(node.left)

    right_value = evaluate(node.right)

    # Apply semantic rule
    if node.value == "+":

        node.result = left_value + right_value

    elif node.value == "-":

        node.result = left_value - right_value

    elif node.value == "*":

        node.result = left_value * right_value

    elif node.value == "/":

        if right_value == 0:
            raise ZeroDivisionError("Division by zero")

        node.result = left_value / right_value

    return node.result


# ============================================================
# DISPLAY BOTTOM-UP EVALUATION STEPS
# ============================================================

def show_steps(node):

    if node is None:
        return

    # Visit children first
    show_steps(node.left)
    show_steps(node.right)

    if node.left is not None and node.right is not None:

        left = node.left.result
        right = node.right.result

        print(
            str(left) + " " +
            node.value + " " +
            str(right) +
            " = " +
            str(node.result)
        )


# ============================================================
# DISPLAY ANNOTATED SYNTAX TREE
# ============================================================

def display_tree(node, level=0):

    if node is None:
        return

    display_tree(node.right, level + 1)

    print(
        "    " * level +
        str(node.value) +
        " [val = " +
        str(node.result) +
        "]"
    )

    display_tree(node.left, level + 1)


# ============================================================
# DISPLAY BOTTOM-UP EXPLANATION
# ============================================================

def display_bottom_up():

    print("\n" + "=" * 65)
    print("BOTTOM-UP EVALUATION")
    print("=" * 65)

    print("""
For the expression:

        (2 + 3) * 4

the evaluation happens from the leaves toward the root:

        2       3
         \\     /
          2 + 3
             ↓
             5
             ↓
           5 * 4
             ↓
            20

Therefore:

        2 + 3 = 5
        5 * 4 = 20

The final synthesized value is:

        20
""")


# ============================================================
# DISPLAY PRECEDENCE
# ============================================================

def display_precedence():

    print("=" * 65)
    print("OPERATOR PRECEDENCE AND ASSOCIATIVITY")
    print("=" * 65)

    print("""
Operator precedence:

        * and /  → Higher precedence
        + and -  → Lower precedence

Therefore:

        2 + 3 * 4

is interpreted as:

        2 + (3 * 4)

and NOT:

        (2 + 3) * 4

This is achieved because the grammar processes multiplication
and division inside T before addition and subtraction in E.

Associativity:

        +, -, *, / are left-associative.

For example:

        10 - 3 - 2

is interpreted as:

        (10 - 3) - 2
""")


# ============================================================
# MAIN PROGRAM
# ============================================================

print("\n")
print("=" * 65)
print(" SDD BASED ARITHMETIC EXPRESSION EVALUATOR")
print("=" * 65)

# Show theory
display_sdd()

display_attribute_explanation()

display_precedence()

# Input
print("=" * 65)

expression = input(
    "Enter arithmetic expression: "
)

try:

    # Tokenize
    tokens = tokenize(expression)

    # Create parser
    parser = Parser(tokens)

    # Construct syntax tree
    root = parser.parse()

    # Evaluate using synthesized attributes
    result = evaluate(root)

    # Show input
    print("\n" + "=" * 65)
    print("INPUT EXPRESSION")
    print("=" * 65)

    print(expression)

    # Show evaluation
    print("\n" + "=" * 65)
    print("BOTTOM-UP COMPUTATION")
    print("=" * 65)

    show_steps(root)

    # Show annotated tree
    print("\n" + "=" * 65)
    print("ANNOTATED SYNTAX TREE")
    print("=" * 65)

    print("""
Each node is displayed as:

operator/operand [val = synthesized value]
""")

    display_tree(root)

    # Final result
    print("\n" + "=" * 65)
    print("FINAL RESULT")
    print("=" * 65)

    print(
        "Expression =", expression
    )

    print(
        "Computed Value =", result
    )

    # Demonstration
    display_bottom_up()

    print("=" * 65)
    print("SDD EVALUATION COMPLETED SUCCESSFULLY")
    print("=" * 65)


except Exception as e:

    print("\nERROR:", e)