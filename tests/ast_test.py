from unittest import TestCase
from typing import List

from lpp.ast import (
    Expression,
    Identifier,
    LetStatement,
    ReturnStatement,
    Program,
)

from lpp.token import (
    Token,
    TokenType,
)


class AstTest(TestCase):

    def test_let_statement(self) -> None:
        program: Program = Program(statements=[
            LetStatement(
                token=Token(TokenType.LET, literal='bolado'),
                name=Identifier(
                        token=Token(TokenType.IDENT, literal='my_var'),
                        value='my_var'
                    ),
                value=Identifier(
                        token=Token(TokenType.IDENT, literal='another_var'),
                        value='another_var'
                    ),
            )
        ])

        program_str = str(program)

        self.assertEqual(program_str, 'bolado my_var = another_var;')

    def test_return_statement(self) -> None:
        program: Program = Program(statements=[
            ReturnStatement(
                token=Token(TokenType.RETURN, literal='vuelto'),
                return_value =Identifier(
                    token=Token(TokenType.IDENT, literal='my_var'),
                    value='my_var'
                ),
            )
        ])

        program_str = str(program)

        self.assertEqual(program_str, 'vuelto my_var;')