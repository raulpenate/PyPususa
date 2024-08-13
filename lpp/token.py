from enum import(
    auto,
    Enum,
    unique
)
from typing import (
    NamedTuple,
    Dict
)

@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    DIV = auto()
    ELSE = auto()
    EOF = auto()
    EQ = auto()
    FALSE = auto()
    FUNCTION = auto()
    GT = auto()
    GT_EQ = auto()
    IDENT = auto()
    IF = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    LT = auto()
    LT_EQ = auto()
    MULT = auto()
    MINUS = auto()
    NOT = auto()
    NOT_EQ = auto()
    PLUS = auto()
    RBRACE = auto()
    RETURN = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    TRUE = auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'

def lookup_token_type(literal: str) -> TokenType:
    # Un bolado es un chunche y un chunche es un bolado
    keywords: Dict[str, TokenType] = {
        'bolado': TokenType.LET,
        'chunche': TokenType.LET,
        'maje': TokenType.LET,
        'simon': TokenType.TRUE,
        'nel': TokenType.FALSE,
        'mabe': TokenType.FUNCTION,
        'si': TokenType.IF,
        'tonces': TokenType.ELSE,
        'vuelto': TokenType.RETURN
    }
    
    return keywords.get(literal, TokenType.IDENT)
    