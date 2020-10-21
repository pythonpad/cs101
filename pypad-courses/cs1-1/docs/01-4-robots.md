# Robots

Here is a Python code that creates and controls a robot. 

```python
# create a robot with one beeper
bot = Robot(beepers = 1)

# move one step forward 
bot.move() 

# turn left 90 degrees 
bot.turn_left()
```

Dot notation is used in `bot.move()` and `bot.turn_left()`. It means that `move` or `turn_left` is a function of the `bot`. 

```python
# create a robot with one beeper
bot = Robot(beepers = 1)

# move one step forward 
bot.move() 
#  ↑ dot notation

# turn left 90 degrees 
bot.turn_left()
#  ↑ dot notation
```

Now, how can `bot` turn right? 

Define a function!

```python
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
```

## Newspaper delivery

Now let's solve an exercise problem with a robot. 

> A robot should climb the stairs to the front door, drop a newspaper there, and return to his starting point.



We can write a problem outline for this exercise. 

- Climb up four stairs 
- Drop the newspaper 
- Turn around
- Climb down four stairs

And this can be converted to a Python version like this.

```python
climb_up_four_stairs()
hubo.drop_beeper()
turn_around()
climb_down_four_stairs()
```

However, there are no functions like `climb_up_four_stairs()`, `turn_around()`, or `climb_down_four_stairs()`. We need to **implement** them.

## Implementing the steps

Here is the implementation of `turn_around()`. 

```python
def turn_around():
    hubo.turn_left()
    hubo.turn_left()
```

But how do we implement the `climb_up_four_stairs()`?

```python
def climb_up_four_stairs(): 
    # how?
```

Let's assume that there is a function `climb_up_one_stair()`. Then we can implement it like this. 

```python
def climb_up_four_stairs():
    climb_up_one_stair()
    climb_up_one_stair()
    climb_up_one_stair()
    climb_up_one_stair()
```

And we can implement `climb_up_one_stair()` like this.

```python
def climb_up_one_stair():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()
```

## Top-down design

What we did now is called **top-down design**. Start at the top of the problem, and make an outline of a solution.

For each step of this solution, either write code directly, or outline a solution for this step.

When all the partial problems have become so small that we can solve them directly, we are done and the program is finished.
