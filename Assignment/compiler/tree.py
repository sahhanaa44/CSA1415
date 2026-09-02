class Node:

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def to_dict(self):

        return {
            "name": self.name,
            "children": [
                child.to_dict()
                for child in self.children
            ]
        }