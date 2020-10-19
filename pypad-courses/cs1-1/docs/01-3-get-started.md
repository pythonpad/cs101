# Get Started

Now let me show you some Python code...

- Python programs (scripts)
- comments
- your own instructions: functions 
- keywords

## Python programs and comments

This is a Python program that says: "Hello world!".

```python
print('Hello world!')
```

And this is a Python program that does the same thing as the one above. 

```python
# This is a first comment.
print('Hello world!') # This is a second comment. Hello world it says!
```

Comments in Python start with the hash character (`#`), and extend to the end of that line. Comments are used to clarify code and they are not interpreted by Python.

## Adding new functions

A **function definition** specifies the name of a new function and the sequence of statements that execute when the function is **called**.

```python
def print_message():
    print('CS101 is fantastic!') 
    print('Programming is fun!')
```

In this code, `def` keyword is used to define a new function, and indentations (four space characters before the "print" in last two lines of the code) are used to clarify that those two lines are included in the function definition.

```python
# ↓ "def" is a keyword for defining a new function.
def print_message(): # ← don't forget the colon here.
    print('CS101 is fantastic!') 
    print('Programming is fun!')
# ↑ indentation is needed to clarify that 
# these two lines of "print"s are included in the function definition.
```

You can call a function inside another function:

```python
def repeat_message(): 
    print_message()
    print_message()
```

## Flow of execution

```python
def print_message():
    print('CS101 is fantastic!') 
    print('Programming is fun!')

def repeat_message(): 
    print_message()
    print_message()

repeat_message()
```

Execution begins at the first statement. Statements are executed one-by-one, top to bottom.

Function definitions do not change the flow of execution—but only define a function.

```python
def print_message(): # ← function definition
    print('CS101 is fantastic!') 
    print('Programming is fun!')

def repeat_message(): # ← function definition
    print_message()
    print_message()

repeat_message()
```

Function calls are like detours in the flow of execution.

```python
def print_message(): # ← function definition
    print('CS101 is fantastic!') 
    print('Programming is fun!')

def repeat_message(): # ← function definition
    print_message() # ← function call
    print_message() # ← function call

repeat_message() # ← function call
```