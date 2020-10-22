# Being Euclid

Define a function `is_triangle` that satisfies following requirements.

- The function takes three float values (as three parameters).
- The function returns `True` or `False` depending on whether these three values can be lengths of the three sides of a trianble.

Let the user enter three float values with the keyboard. Print out a message `YES` or `NO` on the screen, depending on whether those three values can be lengths of the sides of a triangle.

# Tip

Use `input()` function to get user input from the keyboard:

```python
a = input('Side a: ')
print('Value of a is', a)
```

Return value of the `input()` function is a string value. **Convert** the value to a float value with `float()` function.

```python
a_string = input('Side a: ')
a = float(a_string)
print('This value is now in a float variable', a)
```

# Examples

```
Side a: 3
Side b: 4
Side c: 5
YES
```

```
Side a: 2.3
Side b: 4.3
Side c: 5.6
YES
```

```
Side a: 1
Side b: 2
Side c: 3
NO
```

```
Side a: 1.5
Side b: 1.5
Side c: 6.0
NO
```

## Exercise

<iframe class="u-pad-embed" src="../pads/euclid/
exercise_embed/" frameborder="0"></iframe>

## Solution

<a class="c-button" href="../04-2-euclid-solution">View Solution</a>
