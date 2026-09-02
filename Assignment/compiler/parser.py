from .tree import Node


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.errors = []

    def current(self):
        return self.tokens[self.pos]

    def advance(self):
        token = self.current()
        self.pos += 1
        return token

    def error(self, message):

        self.errors.append({
            "type": "Syntax Error",
            "message": message,
            "position": self.current().position
        })

    def expect(self, token_type):

        token = self.current()

        if token.type == token_type:
            return self.advance()

        self.error(
            f"Expected {token_type}, "
            f"found '{token.value}'"
        )

        return None

    # program → statement*
    def parse(self):

        children = []

        while self.current().type != "EOF":

            node = self.statement()

            if node:
                children.append(node)
            else:
                if self.current().type != "EOF":
                    self.advance()

        return Node("PROGRAM", children)

    # statement → assignment | conditional
    def statement(self):

        if self.current().type == "IF":
            return self.conditional()

        if self.current().type == "IDENTIFIER":
            return self.assignment()

        token = self.current()

        self.error(
            f"Unexpected '{token.value}'"
        )

        return None

    # assignment → IDENTIFIER "=" expression ";"
    def assignment(self):

        identifier = self.expect("IDENTIFIER")

        if not identifier:
            return None

        self.expect("ASSIGN")

        if self.current().type in {
            "SEMICOLON",
            "EOF",
            "THEN",
            "ELSE"
        }:

            self.error(
                "Missing expression after '='"
            )

            return Node(
                "ASSIGNMENT",
                [
                    Node(
                        f"IDENTIFIER: {identifier.value}"
                    )
                ]
            )

        expression = self.expression()

        self.expect("SEMICOLON")

        children = [
            Node(
                f"IDENTIFIER: {identifier.value}"
            )
        ]

        if expression:
            children.append(expression)

        return Node("ASSIGNMENT", children)

    # conditional →
    # IF condition THEN statement ELSE statement
    def conditional(self):

        self.expect("IF")

        condition = self.condition()

        self.expect("THEN")

        then_statement = self.statement()

        self.expect("ELSE")

        else_statement = self.statement()

        children = []

        if condition:
            children.append(condition)

        children.append(Node("THEN"))

        if then_statement:
            children.append(then_statement)

        children.append(Node("ELSE"))

        if else_statement:
            children.append(else_statement)

        return Node("IF_STATEMENT", children)

    # condition → expression relational_op expression
    def condition(self):

        left = self.expression()

        operator = self.relational_op()

        if self.current().type in {
            "THEN",
            "ELSE",
            "EOF",
            "SEMICOLON"
        }:

            self.error(
                "Missing expression after "
                "relational operator"
            )

            return left

        right = self.expression()

        if not operator:
            return left

        children = []

        if left:
            children.append(left)

        children.append(
            Node(
                f"RELATIONAL_OP: {operator.value}"
            )
        )

        if right:
            children.append(right)

        return Node("CONDITION", children)

    # < > <= >= == !=
    def relational_op(self):

        relational_tokens = {
            "LT",
            "GT",
            "LE",
            "GE",
            "EQ",
            "NE"
        }

        if self.current().type in relational_tokens:
            return self.advance()

        token = self.current()

        self.error(
            "Expected relational operator, "
            f"found '{token.value}'"
        )

        return None

    # expression → term ((+ | -) term)*
    def expression(self):

        left = self.term()

        while self.current().type in {
            "PLUS",
            "MINUS"
        }:

            operator = self.advance()
            right = self.term()

            if right:

                left = Node(
                    f"EXPRESSION: {operator.value}",
                    [left, right]
                )

        return left

    # term → factor ((* | /) factor)*
    def term(self):

        left = self.factor()

        while self.current().type in {
            "MULTIPLY",
            "DIVIDE"
        }:

            operator = self.advance()
            right = self.factor()

            if right:

                left = Node(
                    f"TERM: {operator.value}",
                    [left, right]
                )

        return left

    # factor → IDENTIFIER | INTEGER | "(" expression ")"
    def factor(self):

        token = self.current()

        if token.type == "IDENTIFIER":

            self.advance()

            return Node(
                f"IDENTIFIER: {token.value}"
            )

        if token.type == "INTEGER":

            self.advance()

            return Node(
                f"INTEGER: {token.value}"
            )

        if token.type == "LPAREN":

            self.advance()

            node = self.expression()

            self.expect("RPAREN")

            return Node(
                "PARENTHESIS",
                [node] if node else []
            )

        self.error(
            "Expected identifier, integer or '('; "
            f"found '{token.value}'"
        )

        return None