from __future__ import annotations

import ast

from flake8_collect import Plugin


def results(s):
    return {"{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()}


def test_trivial():
    assert not results("")


def test_assignment_expression_not_ok():
    src = """\
df.collect()
"""
    (msg,) = results(src)
    assert msg == "1:0: PS001 do not use collect()"
