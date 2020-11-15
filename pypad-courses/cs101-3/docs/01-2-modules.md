# Modules

A Python module is a collection of functions that are grouped together in a file. Python comes with a large number of useful modules. We can also create our own modules.


- `math` for mathematical functions
- `random` for random numbers and shuffling
- `sys` and `os` for accessing the operating system 
- `urllib` to download files from the web
- `cs1robots` for playing with robots
- `cs1graphics` for graphics
- `cs1media` for processing photos

You can get information about a Python builtin module using the official documentation website's search page. 

[Go search about a Python module](https://docs.python.org/3/search.html)

For example, if want to know about the `math` module, you can search **"math"** and find a documentation like [this](https://docs.python.org/3/library/math.html?highlight=math#module-math). 

## Importing modules

Before you can use a module you have to `import` it: 

```python
import math
print(math.sin(math.pi / 4))
```

Sometimes it is useful to be able to use the functions from a
module without the module name:

```python
from math import *
print(sin(pi / 4)) # OK
print(math.pi) # NameError: name 'math'
```

Or only import the functions you need:

```python
from math import sin, pi
    print(sin(pi / 4)) # OK
    print(cos(pi / 4)) # NameError: name 'cos'
    print(math.cos(pi / 4)) # NameError: name 'math'
```

## Importing examples

We already used this:

```python
from cs1robots import * 
create_world()
bot = Robot()
bot.move()
bot.turn_left()
```

Instead we could use this:

```python
import cs1robots
cs1robots.create_world()
bot = cs1robots.Robot()
bot.move()
bot.turn_left()
```

In general, it is considered better not to use `import *`.
