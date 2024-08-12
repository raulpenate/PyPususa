from re import match

from lpp.token import(
    Token,
    TokenType,
    lookup_token_type
)
from typing import Dict

class Lexer:
    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0

        self._read_character()
        
    def next_token(self) -> Token:
        
        token_dict: Dict[str, TokenType] = {
            r"^=$": TokenType.ASSIGN,
            r"^\+$": TokenType.PLUS,
            r"^\($": TokenType.LPAREN,
            r"^\)$": TokenType.RPAREN,
            r"^{$": TokenType.LBRACE,
            r"^}$": TokenType.RBRACE,
            r"^,$": TokenType.COMMA,
            r"^;$": TokenType.SEMICOLON,
            r"^$": TokenType.EOF,
        }

        token = None

        self._skip_whitespace()
        
        if self._is_letter(self._character):
            literal = self._read_identifier()
            token_type = lookup_token_type(literal)
            return Token(token_type, literal)

        if self._is_number(self._character):
            literal = self._read_number()
            return Token(TokenType.INT, literal)

        for regex, token_type in token_dict.items():
            if match(regex, self._character):
                token = Token(token_type, self._character)
                break
            
        if token is None:
            token = Token(TokenType.ILLEGAL, self._character)

        self._read_character()

        return token

    def _is_letter(self, character: str) -> bool:
        return bool(match(r'^[a-záéíóúA-ZÁÉÍÓÚñÑ_]$', character))
    
    def _is_number(self, character: str) -> bool:
        return bool(match(r'^\d$', character))
    
    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1

    def _read_number(self) -> str:
        initial_position = self._position

        while self._is_number(self._character):
            self._read_character()

        return self._source[initial_position: self._position]
    
    def _read_identifier(self) -> str:
        initial_position = self._position

        while self._is_letter(self._character):
            self._read_character()

        # We cut the word by sending the [initial position:last position]
        return self._source[initial_position: self._position]
    
    def _skip_whitespace(self) -> None:
        while match(r'^\s', self._character):
            self._read_character()