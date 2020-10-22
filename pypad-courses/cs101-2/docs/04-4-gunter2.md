# Being Edmund Gunter 2

Modify the program from **Being Edmund Gunter** exercise to print a **sine** curve with `#` characters.

Draw a sine curve with 26 lines of `#` characters. Print maximum 30 `#` characters in a line. 

## Tip

Use `math.sin` function from `math` library.

```python
import math
print(math.sin(0.5 * math.pi)) # this prints out a sine value of 0.5π
```

Convert the result of `sin` function to a required number of `#` characters.

- *sin(π/2) = 1* → `####...####` (30 `#`s)
- *sin(π) = 0* → `##...##` (15 `#`s)
- *sin(3π/2) = -1* → (No `#`)

Convert the value to a integer value with `int()` function.

```python
x = math.pi
print(x) # 3.141592...
x = int(x)
print(x) # 3
```

## Expected Result

```bash
###############
##################
######################
#########################
###########################
#############################
#############################
#############################
############################
##########################
#######################
####################
################
#############
#########
######
###
#



##
####
#######
###########
##############
```

## Exercise

<iframe class="u-pad-embed" src="../pads/gunter2/
exercise_embed/" frameborder="0"></iframe>

## Solution

<a class="c-button" href="../04-4-gunter2-solution">View Solution</a>
