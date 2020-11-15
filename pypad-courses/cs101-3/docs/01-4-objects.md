# Objects

## States and actions

We have met some interesting types of objects: tuples, strings, robots, photos, and graphic objects like circles and squares.

An object has **state** and can perform **actions**.

`Robot`: The robot’s state includes its position, orientation, and number of beepers carried.  
It supports actions to move, turn, drop and pick beepers, and to test various conditions.

`Circle`: Its state consists of its radius, position, depth, border and fill color.  
It supports various actions to change its color, size, and position, and to perform transformations.

`Picture`: Its state consists of the photo’s width and height, and a color value for every pixel.  
It supports actions to look at or modify the color of each pixel.

## Mutable and immutable objects

Objects whose state can never change are called **immutable**. In Python, string and tuple objects are immutable.

Objects whose state can change are called **mutable**. Robots, photos, and graphic objects are mutable.

Remember that we can have more than one name for the same object. Be careful if this is a mutable object!

```python
sun = Circle(30)
sun.setFillColor("dark orange")
moon = sun
moon.setFillColor("wheat")
print(sun.getFillColor())
```

## Functions are objects

A function is an object:

```python
def f(x):
    return math.sin(x / 3.0 + math.pi/4.0)

print(f) 
# # ↑ this will print: <function f at 0xb7539a3c> 
print(type(f))   
# ↑ this will print: <type 'function'>
```

We can use a function as an argument:

```python
def print_table(func, x0, x1, step): 
    x = x0
    while x <= x1:
        print(x, func(x))
        x += step

print_table(f, -math.pi, 3 * math.pi, math.pi / 8)
```
