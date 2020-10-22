# Indentations

Let’s try to follow the boundary of the world: We move forward if there is no wall, otherwise turn to the left.

```python
def move_or_turn():
    if bot.front_is_clear():
        bot.move()
    else:
        bot.turn_left()

for i in range(20): 
    move_or_turn()
```

## With singing and dancing...

```python
def dance():
    for i in range(4):
        bot.turn_left()

def move_or_turn():
    if bot.front_is_clear():
        dance()
        bot.move()
    else:
        bot.turn_left()
        bot.drop_beeper()

for i in range(18): 
    move_or_turn()
```

Note the indentation in the `move_or_turn()` function. What would happen if `bot.drop_beeper()` gets out of the `else:` statement?

```python
def dance():
    for i in range(4):
        bot.turn_left()

def move_or_turn():
    if bot.front_is_clear():
        dance()
        bot.move()
    else:
        bot.turn_left()
    bot.drop_beeper() # ← What happens now?

for i in range(18): 
    move_or_turn()
```

What happens if `bot.drop_beeper()` gets out of the function?

```python
def dance():
    for i in range(4):
        bot.turn_left()

def move_or_turn():
    if bot.front_is_clear():
        dance()
        bot.move()
    else:
        bot.turn_left()
bot.drop_beeper() # ← ...and now?

for i in range(18): 
    move_or_turn()
```

# Many choices!

Deciding your robot's next action may be somewhat complicated. 

```python
if bot.on_beeper(): 
    bot.pick_beeper()
else:
    if bot.front_is_clear():
        bot.move()
    else:
        if bot.left_is_clear(): 
            bot.turn_left()
        else:
            if bot.right_is_clear():
                turn_right() 
            else:
                turn_around()
```

This is not very readable!

You can re-write the code above with `elif` statement like this:

```python
if bot.on_beeper(): 
    bot.pick_beeper()
elif bot.front_is_clear():
    bot.move()
elif bot.left_is_clear(): 
    bot.turn_left()
elif bot.right_is_clear():
    turn_right() 
else:
    turn_around()
```

`elif` combines `else` and `if` to express many alternatives without complicated indentation.


