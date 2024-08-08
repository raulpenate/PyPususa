# Theory

You can’t compile your compiler using itself
yet, but if you have another compiler for your
language written in some other language, you
use that one to compile your compiler once.
Now you can use the compiled version of
your own compiler to compile future
versions of itself and you can discard the
original one compiled from the other
compiler. This is called “bootstrapping” from
the image of pulling yourself up by your own
bootstraps.

![Alt text](URL or path to the image)


## Parts of a language



### Lexical analysis
- Is when we convert a sequence of characters into tokens.
- Identifies basic components of our software. 
- Each token has a name and a value.

### Tokens
- Tokens are the building block of a programming language.
- These can be variables, keywords, numbers, identifiers, special characters and more.
- Usually are defined as ENUM (name & value).

**Fun fact:** Chat GTP is similar, turning words into tokens and tokens into a numeric value.

# Functionality
`__init__` help us to let `mypy` that we're in a package.

### Sources
- [Crafting Interpreters](https://craftinginterpreters.com/)
