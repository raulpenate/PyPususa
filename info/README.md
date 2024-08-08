# Theory

> [!NOTE]
> - This README will be more enjoyable if you use dark mode.
> - I extracted the info from [Crafting Interpreters](https://craftinginterpreters.com/), please consider supporting the autor (Robert Nystrom, creator of Dart) if you enjoy what you see.


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

### Code generation (code gen)
-  __Generating code__ (or __code gen__), where “code” here usually refers to the
kind of primitive assembly-like instructions a CPU runs and not the kind of
“source code” a human might want to read.
- We have a decision to make. Do we generate instructions for a real CPU or a
virtual one? If we generate real machine code, we get an executable that the OS
can load directly onto the chip. Native code is lightning fast, but generating it is
a lot of work. Today’s architectures have piles of instructions, complex
pipelines, and enough historical baggage to fill a 747’s luggage bay.
- Speaking the chip’s language also means your compiler is tied to a specific
architecture. If your compiler targets x86 machine code, it’s not going to run on
an ARM device. All the way back in the 60s, during the Cambrian explosion of
computer architectures, that lack of portability was a real obstacle.
- To get around that, hackers like Martin Richards and Niklaus Wirth, of BCPL
and Pascal fame, respectively, made their compilers produce virtual machine
code. Instead of instructions for some real chip, they produced code for a
hypothetical, idealized machine. Wirth called this “__p-code__” for “__portable__”, but
today, we generally call it bytecode because each instruction is often a single
byte long.

### Virtual machine (VM)
- If your compiler produces bytecode, your work isn’t over once that’s done.
Since there is no chip that speaks that bytecode, it’s your job to translate. Again,
you have two options. You can write a little mini-compiler for each target
architecture that converts the bytecode to native code for that machine. You still
have to do work for each chip you support, but this last stage is pretty simple
and you get to reuse the rest of the compiler pipeline across all of the machines
you support. You’re basically using your bytecode as an intermediate
representation.
- Or you can write a virtual machine (VM), a program that emulates a
hypothetical chip supporting your virtual architecture at runtime. Running
bytecode in a VM is slower than translating it to native code ahead of time
because every instruction must be simulated at runtime each time it executes. In
return, you get simplicity and portability. Implement your VM in, say, C, and
you can run your language on any platform that has a C compiler. This is how
the second interpreter we build in this book works.bill russel
- The kind of VMs we’ll talk about are language virtual machines or process
virtual machines if you want to be
unambiguous.

### Runtime
- We have finally hammered the user’s program into a form that we can execute.
The last step is running it. If we compiled it to machine code, we simply tell the
operating system to load the executable and off it goes. If we compiled it to
bytecode, we need to start up the VM and load the program into that.
- In both cases, for all but the basest of low-level languages, we usually need some
services that our language provides while the program is running. For example,
if the language automatically manages memory, we need a garbage collector
going in order to reclaim unused bits. If our language supports “instance of”
tests so you can see what kind of object you have, then we need some
representation to keep track of the type of each object during execution.
- All of this stuff is going at __runtime__, so it’s called, appropriately, the runtime. In
a fully compiled language, the code implementing the runtime gets inserted
directly into the resulting executable. In, say, Go, each compiled application has
its own copy of Go’s runtime directly embedded in it. If the language is run
inside an interpreter or VM, then the runtime lives there. This is how most
implementations of languages like Java, Python, and JavaScript work.


## Shortcuts and Alternate Routes

### Single-pass compilers
- Some simple compilers interleave parsing, analysis, and code generation so that they produce output code directly in the parser, without ever allocating any syntax trees or other IRs. These __single-pass compilers__ restrict the design of the language. You have no intermediate data structures to store global information about the program, and you don’t revisit any previously parsed part of the code. That means as soon as you see some expression, you need to know enough to correctly compile it.
- Pascal and C were designed around this limitation. At the time, memory was so precious that a compiler might not even be able to hold an entire source file in memory, much less the whole program. This is why Pascal’s grammar requires type declarations to appear first in a block. It’s why in C you can’t call a function above the code that defines it unless you have an explicit forward declaration that tells the compiler what it needs to know to generate code for a call to the later function.

### Tree-walk interpreters
- Some programming languages begin executing code right after parsing it to an AST (with maybe a bit of static analysis applied). To run the program, the interpreter traverses the syntax tree one branch and leaf at a time, evaluating each node as it goes.
- This implementation style is common for student projects and little languages, but is not widely used for general-purpose languages since it tends to be slow. Some people use “interpreter” to mean only these kinds of implementations, but others define that word more generally.

### Transpilers
- Is when we convert the source code from one high-level programming language to another, for example Typescripts that convert `ts` code to Javascript.
![ts to js](https://raw.githubusercontent.com/raulpenate/futebol/main/info/img/tstojs.jpg)
- Writing a complete back end for a language can be a lot of work. If you have some existing generic IR to target, you could bolt your front end onto that. Otherwise, it seems like you’re stuck. __But what if you treated some other source language as if it were an intermediate representation?__
![transpiler](https://raw.githubusercontent.com/raulpenate/futebol/main/info/img/transpiler.jpg)

- You write a front end for your language. Then, in the back end, instead of doing all the work to lower the semantics to some primitive target language, you produce a string of valid source code for some other language that’s about as high level as yours. Then, you use the existing compilation tools for that language as your escape route off the mountain and down to something you can execute.
- They used to call this a __source-to-source__ compiler or a __transcompiler__. After
the rise of languages that compile to JavaScript in order to run in the browser,
they’ve affected the hipster sobriquet __transpiler__.

### Just-in-time compilation



# Functionality
`__init__` help us to let `mypy` that we're in a package.