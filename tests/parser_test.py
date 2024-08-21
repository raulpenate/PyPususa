from unittest import TestCase

from lpp.ast import (
    LetStatement,
    Program,
    ReturnStatement,
) 
from lpp.lexer import Lexer
from lpp.parser import Parser

from typing_extensions import (
    cast,
    List,
)

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

    def test_identifier(self) -> None:
        source: str = '''
            bolado foo = 5;
            chunche bar = 10;
            maje fizz = 20;
        '''
        lexer: Lexer =  Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertEqual(len(program.statements), 3)

        expected_names = ['foo', 'bar', 'fizz']

        names: List[str] = []
        for statement in program.statements:
            statement = cast(LetStatement, statement)
            assert statement.name
            names.append(statement.name.value)
        
        self.assertEqual(names, expected_names)

    def test_parse_errors(self) -> None:
        source: str = 'bolado foo 5'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()
        print(parser.errors)

        self.assertEqual(len(parser.errors), 1)

    def test_return_statement(self) -> None:
        source: str = '''
            vuelto 5;
            vuelto foo;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertEqual(len(program.statements), 2)
        for statement in program.statements:
            self.assertEqual(statement.token_literal(), 'vuelto')
            self.assertIsInstance(statement, ReturnStatement)
