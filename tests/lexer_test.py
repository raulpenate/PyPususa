from unittest import TestCase
from typing import List

from lpp.token import (
    Token,
    TokenType
)
from lpp.lexer import Lexer 

class LexerTest(TestCase):

    def test_illegal(self) -> None:
        source: str = '¡¿@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@'),
        ]

        self.assertEqual(tokens, expected_tokens)
    
    def test_one_character_operator(self) -> None:
        source: str = '=+-/*<>!'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.DIV, '/'),
            Token(TokenType.MULT, '*'),
            Token(TokenType.LT, '<'),
            Token(TokenType.GT, '>'),
            Token(TokenType.NOT, '!'),
        ]

        self.assertEqual(tokens, expected_tokens)
    
    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source ) + 1):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, ''),
        ]

        self.assertEqual(tokens, expected_tokens)
    
    def test_delimiters(self) -> None:
        source = '(){},;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_assignment_bolado(self) -> None:
        source: str = 'bolado cinco = 5;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(5):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'bolado'),
            Token(TokenType.IDENT, 'cinco'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';')
        ]

        self.assertEqual(tokens, expected_tokens)
        
    def test_assignment_chunche(self) -> None:
        source: str = 'chunche cinco = 5;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(5):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'chunche'),
            Token(TokenType.IDENT, 'cinco'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';')
        ]

        self.assertEqual(tokens, expected_tokens)
        
    def test_assignment_maje(self) -> None:
        source: str = 'maje siete = 7;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(5):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'maje'),
            Token(TokenType.IDENT, 'siete'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '7'),
            Token(TokenType.SEMICOLON, ';')
        ]

        self.assertEqual(tokens, expected_tokens)
    
    def test_function_declaration(self) -> None:
        source: str = '''
            maje suma = mabe(x, y) {
                x + y;
            };
        '''
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(16):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'maje'),
            Token(TokenType.IDENT, 'suma'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.FUNCTION, 'mabe'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.SEMICOLON, ';'),
        ]
        
        self.assertEqual(tokens, expected_tokens)

    def test_function_call(self) -> None:
        source: str = 'bolado resultado = suma(dos, tres);'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(10):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'bolado'),
            Token(TokenType.IDENT, 'resultado'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.IDENT, 'suma'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'dos'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'tres'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.SEMICOLON, ';'),
        ]
        
        self.assertEqual(tokens, expected_tokens)
    
    def test_control_statement(self) -> None:
        # simon = true
        # nel = false
        source: str = '''
            si (5 < 10){
                vuelto simon;
            } tonces {
                vuelto nel;
            }
        '''
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(17):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.IF, 'si'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.INT, '5'),
            Token(TokenType.LT, '<'),
            Token(TokenType.INT, '10'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'vuelto'),
            Token(TokenType.TRUE, 'simon'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.ELSE, 'tonces'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'vuelto'),
            Token(TokenType.FALSE, 'nel'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
        ]
        
        self.assertEqual(tokens, expected_tokens)

    def test_two_character_operators(self) -> None:
        source: str = '''
            10 == 10;
            10 != 9;
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(8):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.INT, '10'),
            Token(TokenType.EQ, '=='),
            Token(TokenType.INT, '10'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.INT, '10'),
            Token(TokenType.NOT_EQ, '!='),
            Token(TokenType.INT, '9'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEqual(tokens, expected_tokens)
        
    def test_variable_snake(self) -> None:
        source: str = '''
            bolado number_one = 1;
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(5):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'bolado'),
            Token(TokenType.IDENT, 'number_one'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '1'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEqual(tokens, expected_tokens)
        

    def test_variable_snake_case_int(self) -> None:
        source: str = '''
            maje number_1 = 1;
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(5):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'maje'),
            Token(TokenType.IDENT, 'number_1'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '1'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEqual(tokens, expected_tokens)
        
    def test_variable_with_int(self) -> None:
        source: str = '''
            chunche number1 = 1;
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(5):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'chunche'),
            Token(TokenType.IDENT, 'number1'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '1'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEqual(tokens, expected_tokens)