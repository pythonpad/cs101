# Tuples

A tuple is an object that contains other objects:

```python
position = (3.14, -5, 7.5)
animals = ("Elephant", "American Eagle", "Owl")
```

A tuple is a single object of type **tuple**: 

```python
print(position, type(position))
# ↑ this will print (3.14, -5, 7.5) <type 'tuple'>
```

We can "unpack" tuples:

```python
x, y, z = position
```

Packing and unpacking in one line:

```python 
a, b = b, a
```

## Colors

Colors are often represented as a tuple with three elements that specify the intensity of red, green, and blue light:

```python
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)
```

```python
from cs1media import *

img = create_picture(100, 100, purple) img.show()
img.set_pixels(yellow)
img.show()
```