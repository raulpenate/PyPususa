from re import match

from lpp.token import(
    Token,
    TokenType,
    lookup_token_type
)
from typing import (
    Dict,
    List
) 

class Lexer:
    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0
        self._two_char_token_type: TokenType = TokenType.ILLEGAL

        self._read_character()
        
    def next_token(self) -> Token:
        
        token_dict: Dict[str, TokenType] = {
            r"^=$": TokenType.ASSIGN,
            r"^\!$": TokenType.NOT,
            r"^\+$": TokenType.PLUS,
            r"^\*$": TokenType.MULT,
            r"^\-$": TokenType.MINUS,
            r"^\/$": TokenType.DIV,
            r"^\($": TokenType.LPAREN,
            r"^\)$": TokenType.RPAREN,
            r"^{$": TokenType.LBRACE,
            r"^}$": TokenType.RBRACE,
            r"^,$": TokenType.COMMA,
            r"^;$": TokenType.SEMICOLON,
            r"^>$": TokenType.GT,
            r"^<$": TokenType.LT,
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
                if self._check_two_character_operator():
                    token = self._make_two_character_token(self._two_char_token_type)
                    self._two_char_token_type = TokenType.ILLEGAL # Cleaning TokenType 
                    break
                else:
                    token = Token(token_type, self._character)
                    break
            
        if token is None:
            token = Token(TokenType.ILLEGAL, self._character)

        self._read_character()

        return token

    def _check_two_character_operator(self) -> bool:
        char_suffix: List[str] = [
            r"^=$",
            r"^!$",
            r"^>$",
            r"^<$"
        ]

        for i in range(len(char_suffix)):
            if match(char_suffix[i], self._character):
                return self._save_two_char_type()
        
        return False
        
    def _is_letter(self, character: str) -> bool:
        return bool(match(r'^[a-záéíóúA-ZÁÉÍÓÚñÑ_]$', character))
    
    def _is_number(self, character: str) -> bool:
        return bool(match(r'^\d$', character))
    
    def _make_two_character_token(self, token_type: TokenType) -> Token:
        prefix = self._character
        self._read_character()
        suffix = self._character
        
        return Token(token_type, f'{prefix}{suffix}')
    
    def _read_character(self) -> None:
        # We read the source order of strs
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

        # We cut the number by sending the [initial position:current position]
        return self._source[initial_position: self._position]
    
    def _read_identifier(self) -> str:
        initial_position = self._position

        while self._is_letter(self._character) or self._is_number(self._character):
            self._read_character()

        # We cut the word by sending the [initial position:current position]
        return self._source[initial_position: self._position]

    def _peek_character(self) -> str:
        if self._read_position >= len(self._source):
            return ''
        
        return self._source[self._read_position]
    
    # This func save the token type and returns a boolean in case it existed
    def _save_two_char_type(self) -> bool:
        two_char_dict : Dict[str, TokenType] = {
            r"^==$": TokenType.EQ,
            r"^>=$": TokenType.GT_EQ,
            r"^<=$": TokenType.LT_EQ,
            r"^!=$": TokenType.NOT_EQ,
        }

        prefix = self._character
        suffix = self._peek_character()
        two_char = f'{prefix}{suffix}'

        for regex, token_type in two_char_dict.items():
            if match(regex, two_char):
                self._two_char_token_type = token_type
                return True 
        
        return False
    
    def _skip_whitespace(self) -> None:
        while match(r'^\s', self._character):
            self._read_character()