# Keyboard Input

The `input` function waits for the user to enter a string on the keyboard. When the user presses the Enter key, the whole string is returned:

```python
name = input("What is your name? ") 
print("Welcome to CS101, " + name)
```

If we need a number, we should convert the string:

```python
raw_n = input("Enter a positive integer > ") 
n = int(raw_n)
for i in range(n):  
    print("*" * i)
```