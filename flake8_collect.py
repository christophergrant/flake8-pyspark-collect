from __future__ import annotations

import ast
from typing import Any
from typing import Generator


MSG = "PS001 do not use collect()"

# Define a custom visitor class that inherits from ast.NodeVisitor
class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.match_statements: list[tuple[int, int]] = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and node.func.attr == "collect":
            self.match_statements.append((node.lineno, node.col_offset))
            self.generic_visit(node)


class Plugin:
    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col in visitor.match_statements:
            yield line, col, MSG, type(self)
