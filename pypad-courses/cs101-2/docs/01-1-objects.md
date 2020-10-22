# Objects

Programs work with data. Every piece of data in a Python program is called an **object**.
Objects can be very small (the number **3**) or very large (a digital photograph).

Every object has a **type**. The type determines what you can do with an object.

## The Python zoo

Imagine there is a zoo inside your Python interpreter.

Every time you create an object, an animal is born.

What an animal can do depends on the type (kind) of animal: birds can fly, fish can swim, elephants can lift weights, etc. When an animal is no longer used, it dies (disappears).

## Making objects

You can create objects as follows:

**Numbers**: Simply write them: 

```python
13
3.14159265
-5
```

**Strings**: (a piece of text)

Write text between quotation marks (" and ’ are both okay): 

```python
"CS101 is wonderful"
'The instructor said: "Well done!" and smiled'
```

**Booleans**: (truth values) Write True or False.

```python
True
False
```

## Making more objects

Complicated objects are made by calling functions that create them:

```python
from cs1robots import *
Robot()

from cs1media import * 
load_picture("photos/geese.jpg")
```

A **tuple** object is an object that contains other objects.

To create a tuple, write objects separated by commas (usually in parenthesis):

```python
(3, 2.5, 7)
("red", "yellow", "green") (20100001, "Hong Gildong")
```

## Different animals: Types

Every object has a **type**. The type determines what the object can do, and what you can do with the object. For instance, you can add two numbers, but you cannot add two robots.

The Python can tell you the type of an object:

```python
print(type(3)) # ← Integer number: int
# ↑ this will print "<type 'int'>"
print(type(3.1415)) # ← Floating point number: float
# ↑ this will print "<type 'float'>"
print(type("CS101 is fantastic")) # ← String: str
# ↑ this will print "<type 'str'>"
print(type(3 + 7j)) # ← Complex number: complex
# ↑ this will print "<type 'complex'>"
print(type(True)) # ← Boolean: bool
# ↑ this will print "<type 'bool'>"
```

## More types

Types of more complicated objects:

```python
print(type(Robot()))
# ↑ this will print "<class 'cs1robots.Robot'>"
print(type((3, -1.5, 7))) 
# ↑ this will print "<type 'tuple'>"
print(type(load_picture("photos/geese.jpg")))
# ↑ this will print "<class 'cs1media.Picture'>"
```

Some object types are built into the Python language:

`<type 'xxx'>`

Other object types are defined by Python modules:

`<class 'xxx'>`
