# Variables

Objects can be given a **name**:

```python
message = "CS101 is fantastic"
n = 17
bot = Robot()
pi = 3.1415926535897931
finished = True
img = load_picture("geese.jpg")
```

We call a statement like `n = 17` an **assignment**, because the **name** `n` is **assigned** to the object `17`.

In the Python zoo, the name is a sign board on the animal's cage.

<img src="../assets/01-2-zoo-sign.png" style="max-width:320px" />

## Variable names

There are rules for variable and function names:

- A name consists of letters, digits, and the underscore `_`.
- The first character of a name is a letter.
- The name cannot be a keyword such as `def`, `if`, `else`, or
`while`.
- Upper case and lower case are different: `Pi` is not the same
as `pi`.

Good:

```python
my_message = "CS101 is fantastic"
a13 = 13.0
```

Bad:

```python
more@ = "illegal character" 
13a = 13.0
def = "Definition 1"
```

## Variables

Names are often called **variables**, because the meaning of a name is variable: the same name can be assigned to different objects during a program:

```python
n = 17
n = "Seventeen" 
n = 17.0
```

In the Python zoo, this means that the sign board is moved from one animal to a different animal.

The object assigned to a name is called the **value** of the variable. The value can change over time.

To indicate that a variable is **empty**, we use the special object `None` (of type `NoneType`):

```python
m = None
```

## Objects with two names

The same object can have more than one name:

```python
bot = Robot()
bot.move()
robocop = bot
robocop.turn_left()
bot.move()
```

In this code, both `bot` and `robocop` represents the same robot.

```
bot → [Robot 1] ← robocop
```

However, if we add one more robot and name it `bot`:

```python
bot = Robot()
bot.move()
robocop = bot
robocop.turn_left()
bot.move()

# Add one more robot!
bot = Robot()
bot.move()
robocop.turn_left()
robocop.move()
```

Now `robocop` represents the first robot and `bot` represents the new robot.

```
[Robot 1] ← robocop
[Robot 2] ← bot
```