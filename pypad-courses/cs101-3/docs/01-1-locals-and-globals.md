# Local Variables and Global Variables

## Local variables

Think of a function to evaluate the quadratic function *ax<sup>2</sup> + bx + c*:

```python
def quadratic(a, b, c, x): 
    quad_term = a * x ** 2
    lin_term = b * x
    return quad_term + lin_term + c
```

The names `quad_term` and `lin_term` exist only during the execution of the function `quadratic`. They are called **local variables**.

A function’s **parameters** are also **local variables**. When the function is called, the arguments in the function call are assigned to them.

## Variable are names

```python
def quadratic(a, b, c, x): 
    quad_term = a * x ** 2
    lin_term = b * x
    return quad_term + lin_term + c

result = quadratic(2, 4, 5, 3)
```

Local variables are names that only exist during the execution of the function:

```
a → 2
b → 4
c → 5
x → 3
quad_term → 18
lin_term → 12
```

## Why local variables?

Humans are not good at remembering too many things at the same time. We can only understand software if we can use each part without needing to remember how it works internally.

To use the function `quadratic`, we only want to remember this:

```python
def quadratic(a, b, c, x):
  # implemented somehow
```

**Modularization** means that software consists of parts that are developed and tested separately. To use a part, you do not need to understand how it is implemented.

`cs1robots` is a module that implements the **object** type `Robot`. You can use `Robot` easily without understanding how it is implemented. **→ object-oriented programming**

## Global variables

Variables defined outside of a function are called **global variables**.

Global variables can be used inside a function:

```python
bot = Robot() # ← global variable bot

def turn_right(): 
    for i in range(3): 
        bot.turn_left() # ← using global variable
```

In large programs, using global variables is dangerous, as they can be accessed (by mistake) by all functions of the program.

## Local and global

If a name is only used inside a function, it is global:

```python
def f1():
  return 3 * a + 5
```

If a name is assigned to in a function, it is local:

```python
def f2(x):
    a = 3 * x + 17
    return a * 3 + 5 * a
```

What does this test function print?

```python
a = 17
def test():
    print(a)
    a = 13
    print(a)

test()
```

The answer is: **Error!**

`a` is a **local** variable in `test` because of the assignment, but has no value inside the first `print(a)`.

## Assigning to global variables

Sometimes we want to change the value of a global variable inside a function.

```python
bot = Robot()
bot_direction = 0

def turn_left():
    bot.turn_left()
    global bot_direction
    bot_direction += 90

def turn_right():
    for i in range(3):
        bot.turn_left()
    global bot_direction
    bot_direction -= 90
```

## Local and global variables

What does this code print?

```python
a = "Letter a"
def f(a):
    print("A = ", a)
def g(): 
    a = 7
    f(a + 1)
pr  int("A = ", a)
print("A = ", a )
f(3.14)
print("A = ", a )
g()
print("A = ", a)
```

This code prints:

```
A =  Letter a 
A =  3.14
A =  Letter a 
A =  8
A =  7
A =  Letter a
```

## Parameters are names

What does this code print?

```python
def swap(a, b):
    a, b = b, a

x, y = 123, 456
swap(x, y)
print(x, y)
```

When `swap` is called with parameters, the parameter `a` is a new name for the object `123`, not for the name `x`!

Therefore, the code prints:

```
123 456
```