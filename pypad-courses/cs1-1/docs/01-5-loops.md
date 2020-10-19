# Loops

For-loops are used to repeat the same instruction multiple times.

To repeat the same instruction 4 times:

```python
for i in range(4): 
    print('CS101 is fantastic!')
```

Use indentation to clarify which lines of code are included in the for loop. 

```python
for i in range(4): # ← for-loop
    print('CS101 is fantastic!')
# ↑ Don't forget the indentation!
```

Indentations make big differences. Check out these two code snippets.

What is the difference:

```python
for i in range(4):
    print('CS101 is great!')
    print('I love programming!')
```

and

```python
for i in range(4):
    print('CS101 is great!')
print('I love programming!')
```

## Avoiding repetitions

Let's go back to the *Newspaper delivery* and see the implementation of `climb_up_four_stairs()` function again.

```python
def climb_up_four_stairs():
    climb_up_one_stair()
    climb_up_one_stair()
    climb_up_one_stair()
    climb_up_one_stair()
```

We should avoid writing the same code repeatedly. A **for**-loop allows us to write this more elegantly:

```python
def climb_up_four_stairs():
    for i in range(4):
        climb_up_one_stair()
```
