# More Return Values

Compute the absolute value (like builtin function `abs`):

```python
def absolute(x):
    if x < 0:
        return -x 
    else:
        return x
```

The same function can be written like this:

```python
def absolute(x):
    if x < 0:
        return -x 
    return x
```

The function ends when it returns something. It can't return `x` after returning `-x`.

But the function **cannot** be written like this:

```python
def absolute(x):
    if x < 0:
        return -x 
    if x > 0:
        return x
```

Hint: What happens when `x` is `0`?

## Returning a boolean

A function that tests a condition and returns either `True` or `False` is often called a **predicate**:

```python
# is integer a divisible by b? 
def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False
```

A predicate (function) can be used directly in an `if` or `while` statement:

```python
if is_divisible(x, y):
    print('x is divisible by y')
```

Tip: Easier implementation of `is_divisible`:

```python
def is_divisible(a, b): 
    return a % b == 0
```

## Return Tuples

A function can only return one value.

But this value can be a tuple, and functions can return arbitrarily many values by returning them as a tuple:

```python
def student():
  name = "Doe, John"
  student_id = 20101234
  return name, student_id
```

Often function results are unpacked immediately:

```python
name, id = student()
```

## Functions without results

We have seen many functions that do not use `return`:

```python
def turn_right(): 
    for i in range(3): 
        hubo.turn_left()
```

In fact, a function that does not call `return` automatically returns `None`:

```python
s = turn_right()
print(s)
# None
```

## Calling functions

When a function is called, the **arguments** of the function call are assigned to the **parameters**:

```python
def print_twice(text): # ← "text" is a parameter
    print(text)
    print(text)
```

The number of arguments in the function call must be the same as the number of parameters.

```python
print_twice("I love CS101")
# ↑ this will print:
#    I love CS101
#    I love CS101
print_twice(math.pi)
# ↑ this will print:
#    3.14159265359
#    3.14159265359
```

## Robot's family

We can now write a `turn_right` function that will work for any robot, not just for `bot`:

```python
def turn_right(robot): 
    for i in range(3):
        robot.turn_left()
```

```python
bot = Robot()
bot2 = Robot()
turn_right(bot)
turn_right(bot2)
```

Remember: A **parameter** is a **name** for an object. The name can only be used **inside** the function.
