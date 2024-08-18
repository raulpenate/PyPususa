from lpp.lexer import Lexer
from lpp.token import (
    Token,
    TokenType
)

# END OF FILE TOKEN
EFO_TOKEN : Token =  Token(TokenType.EOF, '')

# := is walrus operator / operator morsa
# This assigns and evaluate the value
def start_repl() -> None:
    while (source := input('>> ')) != 'saquese()':
        lexer: Lexer = Lexer(source)

        while (token := lexer.next_token()) != EFO_TOKEN:
            print(token)