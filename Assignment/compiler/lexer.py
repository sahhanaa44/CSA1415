class Token:

    def __init__(self, token_type, value, position):
        self.type = token_type
        self.value = value
        self.position = position

    def to_dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "position": self.position
        }


class Lexer:

    keywords = {
        "if": "IF",
        "then": "THEN",
        "else": "ELSE"
    }

    two_char_operators = {
        "<=": "LE",
        ">=": "GE",
        "==": "EQ",
        "!=": "NE"
    }

    one_char_tokens = {
        "+": "PLUS",
        "-": "MINUS",
        "*": "MULTIPLY",
        "/": "DIVIDE",
        "<": "LT",
        ">": "GT",
        "=": "ASSIGN",
        "(": "LPAREN",
        ")": "RPAREN",
        ";": "SEMICOLON"
    }

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.tokens = []
        self.errors = []

    def tokenize(self):

        while self.pos < len(self.text):

            ch = self.text[self.pos]

            # Whitespace
            if ch.isspace():
                self.pos += 1
                continue

            # Identifier / Keyword
            if ch.isalpha() or ch == "_":

                start = self.pos

                while (
                    self.pos < len(self.text)
                    and (
                        self.text[self.pos].isalnum()
                        or self.text[self.pos] == "_"
                    )
                ):
                    self.pos += 1

                word = self.text[start:self.pos]

                token_type = self.keywords.get(
                    word,
                    "IDENTIFIER"
                )

                self.tokens.append(
                    Token(token_type, word, start)
                )

                continue

            # Integer
            if ch.isdigit():

                start = self.pos

                while (
                    self.pos < len(self.text)
                    and self.text[self.pos].isdigit()
                ):
                    self.pos += 1

                number = self.text[start:self.pos]

                self.tokens.append(
                    Token("INTEGER", number, start)
                )

                continue

            # Two-character operators
            if self.pos + 1 < len(self.text):

                pair = self.text[
                    self.pos:self.pos + 2
                ]

                if pair in self.two_char_operators:

                    self.tokens.append(
                        Token(
                            self.two_char_operators[pair],
                            pair,
                            self.pos
                        )
                    )

                    self.pos += 2
                    continue

            # One-character operators
            if ch in self.one_char_tokens:

                self.tokens.append(
                    Token(
                        self.one_char_tokens[ch],
                        ch,
                        self.pos
                    )
                )

                self.pos += 1
                continue

            # Invalid symbol
            self.errors.append({
                "type": "Lexical Error",
                "message": f"Invalid symbol '{ch}'",
                "position": self.pos
            })

            self.pos += 1

        self.tokens.append(
            Token("EOF", "", self.pos)
        )

        return self.tokens
