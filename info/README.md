# Theory

> [!NOTE]
> Most of the info was extracted from this book [Crafti ng Interpreters](https://craftinginterpreters.com/), please consider supporting the autor buying this book if you enjoy what you see.

> [!TIP]
> This README will be more enjoyable if you use dark mode.


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


## What's a compiler?
You can think of the compiler as a pipeline where each stage’s job is to organize
the data representing the user’s code in a way that makes the next stage simpler
to implement. The front end of the pipeline is specific to the source language
the program is written in. The back end is concerned with the final architecture
where the program will run.

## Parts of a language/compiler

![pl map](https://raw.githubusercontent.com/raulpenate/futebol/main/info/img/mountain.jpg)
You start off at the bottom with the program as raw source text,
literally just a string of characters. Each phase analyzes the program and
transforms it to some higher-level representation where the semantics—what
the author wants the computer to do—becomes more apparent.
Eventually we reach the peak. We have a bird’s-eye view of the users’s program
and can see what their code means. We begin our descent down the other side of
the mountain. We transform this highest-level representation down to
successively lower-level forms to get closer and closer to something we know
how to make the CPU actually execute.


### Lexical analysis (Scanning)
- Is when we convert a sequence of characters into tokens.
- Identifies basic components of our software. 
- Each token has a name and a value.
![words](https://raw.githubusercontent.com/raulpenate/futebol/main/info/img/words.jpg)
![tokens such as keywords, symbols and more](https://raw.githubusercontent.com/raulpenate/futebol/main/info/img/tokens.jpg)

### Tokens
- Tokens are the building block of a programming language.
- These can be variables, keywords, numbers, identifiers, special characters and more.
- Usually are defined as ENUM (name & value).

**Fun fact:** Chat GTP is similar, turning words into tokens and tokens into a numeric value.

### Parsing
- Our syntax gets grammar, the ability to compose larger expressions and statements out of smaller parts.
- Takes a flat sequence of tokens aed builds a tree structure that mirror the nested nature of grammar.
- Usually are called syntax trees or ASTs, often just trees
![parser tree](https://raw.githubusercontent.com/raulpenate/futebol/main/info/img/parser.jpg)

### Static analysis
- This is the binding or resolution.
- If our language is typed, this is when we type check.
- Expression like `a + b` are resolved by checking where is declared, if both have the right type, and depending the type if both are __numbers__ we execute a __sum__, if both are __strings__ we can execute a `concat`, if one is a __string__ and the other is a __boolean__ we can throw an __error__, or any resolution we want.

### Intermediate representations (IR)
- Is the data structure or code used internally by a compiler or virtual machine(VM) to represent source code.
- In the middle, the code may be stored in some intermediate representation (or
IR) that isn’t tightly tied to either the source or destination forms (hence
“intermediate”). Instead, the IR acts as an interface between these two languages.
- This lets you support multiple source languages and target platforms with less
effort. Say you want to implement Pascal, C and Fortran compilers and you
want to target x86, ARM, and, I dunno, SPARC. Normally, that means you’re
signing up to write nine full compilers: Pascal→x86, C→ARM, and every other
combination.
- A shared intermediate representation reduces that dramatically. You write one
front end for each source language that produces the IR. Then one back end for
each target architecture. Now you can mix and match those to get every
combination.

>[!Important]
> Intermediate language
> Any language targeting a virtual machine or p-code machine can be considered an intermediate language for e.g:
> * __Java bycode__
> * __Microsoft's Common Intermediate Language__ is an intermediate language designed to be shared by all compilers for the .NET Framework, before static or dynamic compilation to machine code.
> * __MATLAB precompiled code__
> * __The GNU Compiler Collection (GCC)__ uses several intermediate languages internally to simplify portability and cross-compilation.
> * __Microsoft P-Code__
> * __Pascal p-Code__

### Optimization
- Once we understand what the user’s program is doing, we can optimize it by replacing inefficient code with more efficient alternatives that maintain the same functionality.
```python
# Compute the sum of the first n positive integers
sum = 0;
for (int i = 1; i <= n; i++) {
    sum += i;
}
# Area of a penny
pennyArea = 3.14159 * (0.75 / 2) * (0.75 / 2);
```
- In this case, the loop is straightforward but not the most efficient way to compute the sum. Since the sum of the first `n` positive integers is a well-known mathematical formula, we can replace this loop with a more efficient calculation. And also we can do the math of the penny by ourselves.
```python
# Compute the sum of the first n positive integers using the formula
sum = n * (n + 1) / 2;
# Area of a penny calculated
pennyArea = 0.4417860938;
```

# Functionality
`__init__` help us to let `mypy` that we're in a package.

// Compute the sum of the first n positive integers
sum = 0;
for (int i = 1; i <= n; i++) {
    sum += i;
}
