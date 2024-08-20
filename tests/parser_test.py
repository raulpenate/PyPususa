from unittest import TestCase

from lpp.ast import (
    LetStatement,
    Program,
) 
from lpp.lexer import Lexer
from lpp.parser import Parser

class ParserText(TestCase):
    
    def test_parse_program(self) -> None:
        source: str = 'bolado x = 5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertIsNotNone(program)
        self.assertIsInstance(program, Program)
    
    def test_let_statements(self) -> None:
        source: str = '''
            bolado foo = 5;
            chunche bar = 10;
            maje fizz = 20;
        '''
        lexer: Lexer =  Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertEqual(len(program.statements), 3)

        expected_literals = ['bolado', 'chunche', 'maje']

        for statement in program.statements:
            self.assertIn(statement.token_literal(), expected_literals)
            self.assertIsInstance(statement, LetStatement)