from lpp.repl import start_repl
from utils.welcome import user_welcome        

def main() -> None:
    user_welcome()
    start_repl()
    pass

if __name__ == '__main__':
    main()