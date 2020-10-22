# Methods and Operators

## Methods

Methods are what objects can do depends on the type of object: a bird can fly, a fish can swim.

Objects provide **methods** to perform these actions.


The methods of an object are used through dot-syntax:

```python
bot = Robot()
bot.move()
bot.turn_left()
```

```python
img = load_picture()
print(img.size()) # ← get width and height in pixels
# ↑ this will print (58, 50)
img.show() # ← display the image
```

```python
b = "banana"
print(b.upper())
# ↑ this will print BANANA
```

## Operators

For numbers, we use the operators +, -, *, /, //, %, and **.

```python
print(2**16) # ← 2 to the power of 16
# ↑ this will print 65536
print(7 % 3) # ← Remainder after division
# ↑ this will print 1
print(9 / 7)
# ↑ this will print 1.2857142857142858
```

`//` is integer division (division without fractional part):

```python
print(13.0 // 4.0)
# ↑ this will print 3.0
```

## Expressions

An **expression** is a combination of objects, variables, operators, and function calls:

```python
3.0 * (2 ** 15 - 12 / 4) + 4 ** 3
```

The operators have precedence as in mathematics:

1. exponentiation `**`
2. multiplication and division `*`, `/`, `//`, `%` 
3. addition and subtraction `+`, `-`

When in doubt, use parentheses!

All operators also work for complex numbers.

## String Expressions

The operators `+` and `*` can be used for strings:

```python
print("Hello" + "CS101")
# ↑ this will print HelloCS101
print("CS101 " * 8)
# ↑ this will print CS101 CS101 CS101 CS101 CS101 CS101 CS101 CS101 
```

## Boolean Expressions

A **boolean expression** is an expression whose value has type `bool`. They are used in `if` and `while` statements.

The operators `==`, `!=`, `>`, `<`, `<=`, and `>=` return boolean values.

```python
print(3 < 5) 
# ↑ this will print True
print(27 == 14) # ← Equality! don’t confuse with =
# ↑ this will print False
print(3.14 != 3.14 )
# ↑ this will print False
print(3.14 >= 3.14 )
# ↑ this will print True
print("Cheong" < "Choe")
# ↑ this will print True
print("3" == 3)
# ↑ this will print False
```

## Logical Operators

The keywords `not`, `and`, and `or` are logical operators:

```python
not True == False
not False == True

False and False == False
False and True == False
True and False == False
True and True == True

False or False == False
False or True == True
True or False == True
True or True == True
```

**Careful**: if the second operand is not needed, Python does not even compute its value.

```python
not True == False
not False == True

False and False == False # ← does not even compute the second value.
False and True == False # ← does not even compute the second value.
True and False == False
True and True == True

False or False == False
False or True == True
True or False == True # ← does not even compute the second value.
True or True == True # ← does not even compute the second value.
```
