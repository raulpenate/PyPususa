from unittest import TestCase

from lpp.ast import Program
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